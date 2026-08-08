// Ghidra headless script: recover the inbound command vocabulary and the full config block.
//
// Follow-up to Motion32HostConfigProbe, which established three things:
//
//   1. The payload import is the right target (its 0x9664 table matches the earlier survey).
//   2. `8F 00 7F` appears NOWHERE in the image, and no code compares `0x8f`. So the native
//      command is neither template-matched nor status-compared — it must be decoded from the
//      USB-MIDI packet header (the code-index-number nibble), not the MIDI status byte.
//   3. Section 2 found zero functions referencing the queues. That is an artefact, not a fact:
//      Thumb loads addresses from PC-relative literal pools, and `0x200040a0` is very likely
//      computed as `0x20004084 + 0x1c` rather than loaded directly, so `getReferencesTo`
//      has nothing to return.
//
// This probe fixes (3) properly and pushes on (1) and (2):
//
//   A. LITERAL-POOL SCAN. Walk every 4-byte word in memory looking for the target address as a
//      *value*. Each hit is a literal pool entry; whatever loads that literal is the code we
//      want. This finds users of an address even when there is no direct reference.
//   B. BASE-RELATIVE USERS. Also scan for words holding a nearby base, so `base + delta`
//      addressing is caught.
//   C. COMMAND IDS. Decompile every function found and list its small constants — the inbound
//      Fender dispatch is a compare chain or table on the byte after `F0 08 26`.
//   D. CONFIG BLOCK. Dump 0x9500-0x9760 whole, so the variant structure is visible rather than
//      inferred from two 96-byte windows.
//   E. USB-MIDI CIN DECODE. Hunt the packet-header path: functions comparing against the
//      code-index-numbers (0x08 Note Off, 0x09 Note On, 0x0b CC, 0x0e Pitch Bend, 0x04/0x05/
//      0x06/0x07 SysEx continuation). CIN 0x08 is where `8F 00 7F` would be recognised.
//
// Usage:
//   -postScript Motion32CommandVocabProbe.java <output.md>
// Run it against BOTH programs via run_command_vocab_probe.sh; the payload is the useful one.

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.address.AddressSetView;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.mem.Memory;
import ghidra.program.model.mem.MemoryBlock;
import ghidra.program.model.scalar.Scalar;
import ghidra.program.model.symbol.Reference;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Motion32CommandVocabProbe extends GhidraScript {

    /** Addresses to find users of, by literal-pool value rather than by reference. */
    private static final long[] TARGETS = {
        0x20004084L,  // outbound host event queue
        0x200040a0L,  // inbound Fender framed-byte queue
        0x20004324L,  // outbound copy staging buffer
        0x200045caL,  // absolute-control count
        0x200045ccL,  // relative-control count
        0x20004538L,  // candidate state word
        0x20005d24L,  // main USB endpoint context
        0x20005cd4L,  // secondary USB endpoint context
    };

    /** The config block: two framed prefixes then the per-variant tables. */
    private static final long CONFIG_START = 0x9500L;
    private static final long CONFIG_END = 0x9760L;

    /** USB-MIDI code index numbers. CIN 0x08 = Note Off, which is what 8F 00 7F is. */
    private static final long[] CIN_VALUES = { 0x04L, 0x05L, 0x06L, 0x07L, 0x08L, 0x09L, 0x0bL, 0x0eL };

    private DecompInterface decomp;
    private PrintWriter out;

    @Override
    protected void run() throws Exception {
        String[] args = getScriptArgs();
        File target = new File(args.length > 0 ? args[0] : "command_vocab_probe.md");

        decomp = new DecompInterface();
        decomp.setOptions(new DecompileOptions());
        decomp.openProgram(currentProgram);

        out = new PrintWriter(target, "UTF-8");
        try {
            out.println("# Motion 32 — command vocabulary and configuration block");
            out.println();
            out.println("Program: `" + currentProgram.getName() + "`  ");
            out.println("Image base: `" + currentProgram.getImageBase() + "`");
            out.println();
            out.println("Recovers users of the queue addresses via **literal-pool scanning**, because");
            out.println("`getReferencesTo` returns nothing for them — Thumb loads addresses from PC-");
            out.println("relative pools and the inbound queue is probably `outbound + 0x1c`.");
            out.println();

            sectionLiteralUsers();
            sectionConfigBlock();
            sectionCinDecode();
            sectionSysexTemplates();

            out.println();
            out.println("---");
            out.println();
            out.println("## Reading order");
            out.println();
            out.println("1. **Section 1**, the functions loading the inbound queue. One of them is the");
            out.println("   framed-message consumer; its small constants are the accepted command ids.");
            out.println("   Anything past `0x20`/`0x21`/`0x22` is undocumented host->device vocabulary.");
            out.println("2. **Section 3**, CIN `0x08`. `8F 00 7F` arrives as a USB-MIDI packet whose");
            out.println("   header nibble is 8; if the firmware switches on that, the native-entry");
            out.println("   handler is in that switch and every sibling case is another host command.");
            out.println("3. **Section 2**, the config block, to settle the variant count as data.");
        } finally {
            out.close();
            decomp.dispose();
        }
        println("Wrote " + target.getAbsolutePath());
    }

    // ------------------------------------------------------------------ 1
    private void sectionLiteralUsers() throws Exception {
        out.println("## 1. Who actually uses each address (literal-pool scan)");
        out.println();

        for (long targetAddr : TARGETS) {
            out.println("### `0x" + Long.toHexString(targetAddr) + "`");
            out.println();

            List<Address> literals = findWordsEqualTo(targetAddr);
            out.println("Literal-pool words holding this value: **" + literals.size() + "**");
            out.println();
            if (!literals.isEmpty()) {
                out.println("```text");
                for (Address lit : literals) {
                    out.println(lit.toString());
                }
                out.println("```");
                out.println();
            }

            Set<Function> users = new LinkedHashSet<>();
            for (Address lit : literals) {
                for (Reference r : getReferencesTo(lit)) {
                    Function f = getFunctionContaining(r.getFromAddress());
                    if (f != null) {
                        users.add(f);
                    }
                }
                // Thumb literal loads sit within ~1KB before the pool; catch functions whose
                // body simply contains the pool address too.
                Function near = getFunctionContaining(lit);
                if (near != null) {
                    users.add(near);
                }
            }
            out.println("Functions loading it: **" + users.size() + "**");
            out.println();
            for (Function f : users) {
                dumpFunction(f);
                out.println("**Small constants in `" + f.getName() + "` (candidate command ids):**");
                out.println();
                out.println("```text");
                for (String line : smallScalars(f)) {
                    out.println(line);
                }
                out.println("```");
                out.println();
            }
        }
    }

    // ------------------------------------------------------------------ 2
    private void sectionConfigBlock() throws Exception {
        out.println("## 2. The configuration block, whole");
        out.println();
        out.println("`0x95f4` = `F0 08 26 05` (Motion 32), `0x95f8` = `F0 08 24 05` (Motion 16),");
        out.println("then the per-variant tables. Dumped in full so the variant count is a fact.");
        out.println();
        out.println("```text");
        StringBuilder sb = new StringBuilder();
        for (long a = CONFIG_START; a < CONFIG_END; a++) {
            if ((a - CONFIG_START) % 16 == 0) {
                if (sb.length() > 0) {
                    out.println(sb.toString());
                    sb.setLength(0);
                }
                sb.append(String.format("%08x: ", a));
            }
            try {
                sb.append(String.format("%02x ", currentProgram.getMemory().getByte(toAddr(a)) & 0xff));
            } catch (Exception e) {
                sb.append(".. ");
            }
        }
        if (sb.length() > 0) {
            out.println(sb.toString());
        }
        out.println("```");
        out.println();
    }

    // ------------------------------------------------------------------ 3
    private void sectionCinDecode() throws Exception {
        out.println("## 3. USB-MIDI code-index-number decode");
        out.println();
        out.println("`8F 00 7F` reaches the device as a 4-byte USB-MIDI packet whose header low");
        out.println("nibble is the CIN. For a Note Off that is **8**. If the firmware switches on the");
        out.println("CIN, the native-entry handler is one case of that switch and its siblings are the");
        out.println("rest of the host command surface.");
        out.println();
        out.println("Functions comparing against CIN values, ranked by how many distinct CINs they use");
        out.println("(a real dispatch touches several):");
        out.println();

        java.util.Map<Function, Set<Long>> byFunc = new java.util.LinkedHashMap<>();
        InstructionIterator it = currentProgram.getListing().getInstructions(true);
        while (it.hasNext() && !monitor.isCancelled()) {
            Instruction insn = it.next();
            for (int i = 0; i < insn.getNumOperands(); i++) {
                Scalar s = insn.getScalar(i);
                if (s == null) {
                    continue;
                }
                long v = s.getUnsignedValue();
                for (long cin : CIN_VALUES) {
                    if (v == cin) {
                        Function f = getFunctionContaining(insn.getAddress());
                        if (f != null) {
                            byFunc.computeIfAbsent(f, k -> new TreeSet<Long>()).add(v);
                        }
                    }
                }
            }
        }

        List<Function> ranked = new ArrayList<>(byFunc.keySet());
        ranked.sort((a, b) -> byFunc.get(b).size() - byFunc.get(a).size());

        out.println("```text");
        int shown = 0;
        for (Function f : ranked) {
            Set<Long> cins = byFunc.get(f);
            if (cins.size() < 3) {
                continue;
            }
            StringBuilder line = new StringBuilder();
            for (long c : cins) {
                line.append(String.format("0x%02x ", c));
            }
            out.println(String.format("%-28s @ %s   CINs: %s",
                    f.getName(), f.getEntryPoint(), line.toString().trim()));
            if (++shown >= 40) {
                break;
            }
        }
        if (shown == 0) {
            out.println("(no function uses 3+ distinct CIN values — dispatch may be table-driven)");
        }
        out.println("```");
        out.println();

        out.println("### Decompilation of the top candidates");
        out.println();
        int dumped = 0;
        for (Function f : ranked) {
            if (byFunc.get(f).size() < 4) {
                continue;
            }
            dumpFunction(f);
            if (++dumped >= 8) {
                break;
            }
        }
        if (dumped == 0) {
            out.println("_No function used 4+ distinct CIN values._");
            out.println();
        }
    }

    // ------------------------------------------------------------------ 4
    private void sectionSysexTemplates() throws Exception {
        out.println("## 4. Fender header templates (`08 26` / `08 24` without the F0)");
        out.println();
        out.println("The inbound parser has to match the manufacturer and device id. A two-byte");
        out.println("template, or a compare against `0x26`, is where that happens.");
        out.println();

        byte[][] pats = { { 0x08, 0x26 }, { 0x08, 0x24 } };
        String[] names = { "08 26", "08 24" };
        for (int p = 0; p < pats.length; p++) {
            out.println("### `" + names[p] + "`");
            out.println();
            out.println("```text");
            int found = 0;
            Address a = currentProgram.getMinAddress();
            while (a != null && found < 30 && !monitor.isCancelled()) {
                Address hit = currentProgram.getMemory().findBytes(a, pats[p], null, true, monitor);
                if (hit == null) {
                    break;
                }
                found++;
                StringBuilder ctx = new StringBuilder();
                for (int i = -6; i < 12; i++) {
                    try {
                        ctx.append(String.format("%02x ",
                                currentProgram.getMemory().getByte(hit.add(i)) & 0xff));
                    } catch (Exception e) {
                        ctx.append(".. ");
                    }
                }
                Function f = getFunctionContaining(hit);
                out.println(hit + "  " + ctx + (f != null ? " in " + f.getName() : " (data)"));
                a = hit.add(1);
            }
            if (found == 0) {
                out.println("(not present)");
            }
            out.println("```");
            out.println();
        }

        out.println("### Functions comparing against the device id `0x26`");
        out.println();
        out.println("```text");
        Set<String> where = new TreeSet<>();
        InstructionIterator it = currentProgram.getListing().getInstructions(true);
        while (it.hasNext() && !monitor.isCancelled()) {
            Instruction insn = it.next();
            for (int i = 0; i < insn.getNumOperands(); i++) {
                Scalar s = insn.getScalar(i);
                if (s != null && s.getUnsignedValue() == 0x26L) {
                    Function f = getFunctionContaining(insn.getAddress());
                    where.add((f != null ? f.getName() + " @ " + f.getEntryPoint() : "(none)")
                            + "  [" + insn.getAddress() + " " + insn + "]");
                }
            }
        }
        int n = 0;
        for (String w : where) {
            out.println(w);
            if (++n >= 50) {
                out.println("... (" + (where.size() - n) + " more)");
                break;
            }
        }
        if (where.isEmpty()) {
            out.println("(none)");
        }
        out.println("```");
        out.println();
    }

    // ------------------------------------------------------------------ helpers
    /** Every 4-byte aligned word in memory whose value equals {@code value}. */
    private List<Address> findWordsEqualTo(long value) {
        List<Address> hits = new ArrayList<>();
        Memory mem = currentProgram.getMemory();
        for (MemoryBlock block : mem.getBlocks()) {
            if (!block.isInitialized()) {
                continue;
            }
            Address a = block.getStart();
            Address end = block.getEnd();
            while (a != null && a.compareTo(end) < 0) {
                if (monitor.isCancelled()) {
                    return hits;
                }
                try {
                    if ((mem.getInt(a) & 0xffffffffL) == value) {
                        hits.add(a);
                    }
                } catch (Exception ignored) {
                    // unreadable word, keep going
                }
                try {
                    a = a.add(4);
                } catch (Exception e) {
                    break;
                }
            }
        }
        return hits;
    }

    private List<String> smallScalars(Function f) {
        Set<String> seen = new TreeSet<>();
        AddressSetView body = f.getBody();
        InstructionIterator it = currentProgram.getListing().getInstructions(body, true);
        while (it.hasNext()) {
            Instruction insn = it.next();
            for (int i = 0; i < insn.getNumOperands(); i++) {
                Scalar s = insn.getScalar(i);
                if (s == null) {
                    continue;
                }
                long v = s.getUnsignedValue();
                if (v > 0 && v <= 0x7f) {
                    seen.add(String.format("0x%02x  (%s  %s)", v, insn.getAddress(), insn));
                }
            }
        }
        return new ArrayList<>(seen);
    }

    private void dumpFunction(Function f) {
        out.println("#### `" + f.getName() + "` @ `" + f.getEntryPoint() + "`");
        out.println();
        out.println("```c");
        try {
            DecompileResults res = decomp.decompileFunction(f, 90, monitor);
            if (res != null && res.decompileCompleted() && res.getDecompiledFunction() != null) {
                out.println(res.getDecompiledFunction().getC());
            } else {
                out.println("// decompilation failed: "
                        + (res != null ? res.getErrorMessage() : "no result"));
            }
        } catch (Exception e) {
            out.println("// decompilation threw: " + e);
        }
        out.println("```");
        out.println();
    }
}
