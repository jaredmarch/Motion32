// Ghidra headless script: map the second code region and search it exhaustively for the
// native-mode (`8F 00 7F`) handler.
//
// WHY THIS EXISTS
// ---------------
// `Motion32HostConfigProbe` searched for a `0x8f` compare and found nothing. That was not a
// wrong question — it was the right question asked of the wrong bytes. The payload import maps
// the whole file at base 0, but **file offset 0x20000 corresponds to runtime 0x10100000**, so
// roughly 600 KB of code has always been sitting in the project as undisassembled data. See
// `second_code_region_at_0x10100000.md` for how that base was derived and verified.
//
// Evidence, in brief:
//   * The last 17 words of the image are odd (Thumb) pointers into 0x1013xxxx / 0x1010xxxx.
//   * No instruction in the base-0 region ever builds a 0x10xxxxxx address (zero `movt` sites),
//     so those pointers are not base-0 code referring outward — they belong to the region.
//   * Solving `runtime - file_offset` against function-prologue hits gives 0x100e0000 at
//     156/284, versus 58 for the next candidate. 0x10100000 - 0x100e0000 = 0x20000.
//   * Disassembling there yields coherent bodies with matched push/pop and in-region call
//     targets (e.g. 0x1013ad10 calls 0x1013a180 and 0x1013aef8).
//
// The base-0 region is now *excluded* as the answer, not merely unproven:
//   * The USB receive callback (FUN_00002ac4, from descriptor 0x9874 +0x14) feeds exactly one
//     ring, 0x200040a0, one byte per event.
//   * That ring has exactly three references in the whole base-0 region, and its single
//     consumer FUN_000010a4 is a SysEx-only state machine that discards any byte that is not
//     0xF0 in state 0 and aborts on any status byte mid-payload. `8F 00 7F` cannot survive it.
//   * The second endpoint is never configured: FUN_00002a14 has one caller (0x00000e84, with
//     r0 = 9) and descriptor 0x97e4's callback slot is all zeros.
//
// So the handler is in the new block or it is not in this image at all.
//
// WHAT THIS SCRIPT DOES
// ---------------------
//   1. Creates the `app` memory block at 0x10100000 from file bytes offset 0x20000 (idempotent).
//   2. Seeds disassembly from the tail pointer table, then runs analysis over the new block.
//   3. Searches exhaustively for the handshake: 0x8f scalars, 0x80/0xf0 status masking, the raw
//      byte patterns `8F 00 7F` and `8F 00 00`, the touch CCs 0x7A/0x7B, pitch-bend status
//      construction, and the Fender SysEx prefixes.
//   4. Decompiles every function containing a candidate, plus its callers and callees.
//
// USAGE — note this WRITES to the project, so no -readOnly:
//   ~/Downloads/ghidra_12.1.2_PUBLIC/support/analyzeHeadless \
//     "<repo>/Resources/FirmwareAnalysis/ghidra_project" Motion32Firmware \
//     -process motion32_fw_payload_0x1000.bin -noanalysis \
//     -scriptPath "<repo>/Resources/FirmwareAnalysis" \
//     -postScript Motion32NativeBlockProbe.java "<repo>/Resources/FirmwareAnalysis/native_block_probe.md"
//
// Back up ghidra_project first. This modifies the program.

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.database.mem.FileBytes;
import ghidra.program.model.address.Address;
import ghidra.program.model.address.AddressSet;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.mem.Memory;
import ghidra.program.model.mem.MemoryBlock;
import ghidra.program.model.scalar.Scalar;
import ghidra.program.model.symbol.Reference;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class Motion32NativeBlockProbe extends GhidraScript {

    private static final String BLOCK_NAME = "app";
    private static final long BLOCK_BASE   = 0x10100000L;
    private static final long FILE_OFFSET  = 0x20000L;
    private static final long DELTA        = BLOCK_BASE - FILE_OFFSET;   // 0x100e0000

    /** Tail pointer table: file 0xb9060 -> runtime 0x10199060, 17 words. */
    private static final long TAIL_TABLE   = 0x10199060L;
    private static final int  TAIL_COUNT   = 17;

    private PrintWriter out;
    private Address blockStart, blockEnd;

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        File target = new File(args.length > 0 ? args[0]
                : "native_block_probe.md");
        out = new PrintWriter(target, "UTF-8");
        try {
            out.println("# Motion 32 — native-mode handler probe (second code region)");
            out.println();
            out.println("Block `" + BLOCK_NAME + "` @ `0x" + Long.toHexString(BLOCK_BASE)
                    + "` from file offset `0x" + Long.toHexString(FILE_OFFSET)
                    + "`, delta `0x" + Long.toHexString(DELTA) + "`.");
            out.println();

            if (!ensureBlock()) {
                out.println("**ABORTED** — could not create or find the block. See section 1.");
                return;
            }
            seedAndAnalyze();
            reportInventory();
            searchHandshake();
            searchRawPatterns();
            searchStripAndPitchBend();
            decompileCandidates();

            out.println();
            out.println("---");
            out.println();
            out.println("Generated by `Motion32NativeBlockProbe.java`.");
        } finally {
            out.close();
        }
        println("Report written to " + target.getAbsolutePath());
    }

    // ---------------------------------------------------------------- block

    private boolean ensureBlock() {
        out.println("## 1. Memory block");
        out.println();
        Memory mem = currentProgram.getMemory();
        MemoryBlock existing = mem.getBlock(BLOCK_NAME);
        if (existing != null) {
            blockStart = existing.getStart();
            blockEnd = existing.getEnd();
            out.println("Block already present: `" + blockStart + "`-`" + blockEnd + "`. Reusing it.");
            out.println();
            return true;
        }
        try {
            List<FileBytes> all = mem.getAllFileBytes();
            if (all == null || all.isEmpty()) {
                out.println("No FileBytes in this program — was it imported from the raw binary?");
                out.println();
                out.println("Fall back to the manual route: **Window -> Memory Map -> Add Block**,");
                out.println("start `0x10100000`, length `0x990a4`, source File Bytes at offset `0x20000`.");
                out.println();
                return false;
            }
            FileBytes fb = all.get(0);
            long avail = fb.getSize() - FILE_OFFSET;
            long length = Math.max(0, avail);
            if (length == 0) {
                out.println("FileBytes too small (" + fb.getSize() + " bytes) for offset 0x"
                        + Long.toHexString(FILE_OFFSET) + ".");
                out.println();
                return false;
            }
            Address start = toAddr(BLOCK_BASE);
            MemoryBlock block = mem.createInitializedBlock(
                    BLOCK_NAME, start, fb, FILE_OFFSET, length, false);
            block.setRead(true);
            block.setWrite(false);
            block.setExecute(true);
            block.setComment("Second code region. file 0x" + Long.toHexString(FILE_OFFSET)
                    + " -> 0x" + Long.toHexString(BLOCK_BASE)
                    + "; see second_code_region_at_0x10100000.md");
            blockStart = block.getStart();
            blockEnd = block.getEnd();
            out.println("Created `" + BLOCK_NAME + "`: `" + blockStart + "`-`" + blockEnd
                    + "` (" + length + " bytes), r-x.");
            out.println();
            return true;
        }
        catch (Exception e) {
            out.println("Block creation failed: `" + e + "`");
            out.println();
            out.println("The base-0 block probably already covers these bytes. Either shrink it to");
            out.println("`0x0`-`0x1ffff` in the Memory Map first, or create `app` as an **overlay**.");
            out.println();
            return false;
        }
    }

    private void seedAndAnalyze() {
        out.println("## 2. Seeding and analysis");
        out.println();
        Memory mem = currentProgram.getMemory();
        int seeded = 0;
        List<Address> seeds = new ArrayList<>();

        // The tail table is a list of entry points into this region.
        for (int i = 0; i < TAIL_COUNT; i++) {
            try {
                long v = mem.getInt(toAddr(TAIL_TABLE + 4L * i)) & 0xffffffffL;
                if ((v & 1) == 1 && v >= BLOCK_BASE && v < BLOCK_BASE + 0x200000L) {
                    seeds.add(toAddr(v & ~1L));
                }
            }
            catch (Exception ignored) { }
        }
        // Plus every plausible in-region Thumb pointer stored anywhere in the block.
        try {
            long lo = blockStart.getOffset(), hi = blockEnd.getOffset();
            for (long a = lo; a + 4 <= hi && seeds.size() < 6000; a += 4) {
                long v = mem.getInt(toAddr(a)) & 0xffffffffL;
                if ((v & 1) == 1 && v > BLOCK_BASE && v < hi) {
                    seeds.add(toAddr(v & ~1L));
                }
            }
        }
        catch (Exception ignored) { }

        Set<Address> unique = new LinkedHashSet<>(seeds);
        for (Address a : unique) {
            try {
                if (getInstructionAt(a) == null) {
                    disassemble(a);
                }
                if (getFunctionAt(a) == null) {
                    createFunction(a, null);
                }
                seeded++;
            }
            catch (Exception ignored) { }
        }
        out.println("Seeded " + seeded + " entry point(s) from " + unique.size() + " candidate pointer(s).");
        out.println();
        try {
            analyzeChanges(currentProgram);
            out.println("`analyzeChanges` completed.");
        }
        catch (Exception e) {
            out.println("Analysis raised `" + e + "` — results below may be partial.");
        }
        out.println();
    }

    private void reportInventory() {
        out.println("## 3. What the block now contains");
        out.println();
        int inBlock = 0, total = 0;
        FunctionIterator it = currentProgram.getFunctionManager().getFunctions(true);
        while (it.hasNext()) {
            Function f = it.next();
            total++;
            if (inNewBlock(f.getEntryPoint())) inBlock++;
        }
        out.println("- Functions in `" + BLOCK_NAME + "`: **" + inBlock + "**");
        out.println("- Functions program-wide: " + total);
        out.println();
        out.println("Before this script the program had 1049 functions, all below `0x20000`.");
        out.println("A large number here is the headline result: the region is code.");
        out.println();
    }

    // ------------------------------------------------------------- searches

    /** Instruction scalars that would decode a Note Off on channel 16. */
    private void searchHandshake() {
        out.println("## 4. The handshake: `8F 00 7F`");
        out.println();
        out.println("`0x8F` is Note Off, channel 16. A decoder either compares the whole status");
        out.println("byte against `0x8f`, or masks with `0xf0` and compares against `0x80`.");
        out.println();

        long[] wanted = { 0x8fL, 0x80L, 0xf0L, 0x0fL, 0x7fL };
        Map<Long, List<Instruction>> hits = new LinkedHashMap<>();
        for (long w : wanted) hits.put(w, new ArrayList<Instruction>());

        InstructionIterator ii = currentProgram.getListing().getInstructions(newBlockSet(), true);
        while (ii.hasNext()) {
            Instruction insn = ii.next();
            String m = insn.getMnemonicString().toLowerCase();
            boolean interesting = m.startsWith("cmp") || m.startsWith("and")
                    || m.startsWith("sub") || m.startsWith("teq") || m.startsWith("tst")
                    || m.startsWith("mov") || m.startsWith("bic");
            if (!interesting) continue;
            for (int op = 0; op < insn.getNumOperands(); op++) {
                Scalar s = insn.getScalar(op);
                if (s == null) continue;
                long v = s.getUnsignedValue();
                if (hits.containsKey(v)) hits.get(v).add(insn);
            }
        }
        for (long w : wanted) {
            List<Instruction> list = hits.get(w);
            out.println("### scalar `0x" + Long.toHexString(w) + "` — " + list.size() + " site(s)");
            out.println();
            if (list.isEmpty()) { out.println("_none_"); out.println(); continue; }
            int shown = 0;
            out.println("```");
            for (Instruction insn : list) {
                if (shown++ >= 120) { out.println("... " + (list.size() - 120) + " more"); break; }
                Function f = getFunctionContaining(insn.getAddress());
                out.println(insn.getAddress() + "  " + insn
                        + (f != null ? "   in " + f.getName() : ""));
            }
            out.println("```");
            out.println();
        }
        out.println("**Read `0x8f` first.** A single compare against `0x8f` in a function that also");
        out.println("touches `0x7f` and `0x00` is the handshake decoder.");
        out.println();
    }

    private void searchRawPatterns() {
        out.println("## 5. Raw byte patterns");
        out.println();
        byte[][] pats = {
            { (byte)0x8f, 0x00, 0x7f },
            { (byte)0x8f, 0x00, 0x00 },
            { (byte)0xf0, 0x08, 0x26 },
            { (byte)0xf0, 0x08, 0x24 },
            { (byte)0xf0, 0x08, 0x26, 0x22 },
        };
        String[] names = {
            "native ON `8F 00 7F`", "native OFF `8F 00 00`",
            "Fender prefix (Motion 32) `F0 08 26`", "Fender prefix (Motion 16) `F0 08 24`",
            "Global Settings state `F0 08 26 22`",
        };
        Memory mem = currentProgram.getMemory();
        for (int p = 0; p < pats.length; p++) {
            out.println("### " + names[p]);
            out.println();
            int found = 0;
            Address at = blockStart;
            while (at != null && found < 40) {
                at = mem.findBytes(at, pats[p], null, true, monitor);
                if (at == null || at.getOffset() > blockEnd.getOffset()) break;
                Function f = getFunctionContaining(at);
                out.println("- `" + at + "`  (file `0x"
                        + Long.toHexString(at.getOffset() - DELTA) + "`)"
                        + (f != null ? " in `" + f.getName() + "`" : " — not in a function"));
                found++;
                at = at.add(1);
            }
            if (found == 0) out.println("_no hits_");
            out.println();
        }
    }

    private void searchStripAndPitchBend() {
        out.println("## 6. Strips: touch CCs and pitch-bend construction");
        out.println();
        out.println("The captured native behaviour is pitch bend on channels 0 and 1, with touch on");
        out.println("CC `0x7A`/`0x7B`. The base-0 emitter produces `0xB0/0xB1` + CC `0x16`/`0x36`");
        out.println("instead, so a second emitter must exist. These are its fingerprints.");
        out.println();
        long[] wanted = { 0x7aL, 0x7bL, 0xe0L, 0xe1L, 0x16L, 0x36L };
        Map<Long, List<Instruction>> hits = new LinkedHashMap<>();
        for (long w : wanted) hits.put(w, new ArrayList<Instruction>());
        InstructionIterator ii = currentProgram.getListing().getInstructions(newBlockSet(), true);
        while (ii.hasNext()) {
            Instruction insn = ii.next();
            for (int op = 0; op < insn.getNumOperands(); op++) {
                Scalar s = insn.getScalar(op);
                if (s == null) continue;
                long v = s.getUnsignedValue();
                if (hits.containsKey(v)) hits.get(v).add(insn);
            }
        }
        for (long w : wanted) {
            List<Instruction> list = hits.get(w);
            out.println("### scalar `0x" + Long.toHexString(w) + "` — " + list.size() + " site(s)");
            out.println();
            if (list.isEmpty()) { out.println("_none_"); out.println(); continue; }
            Set<String> fns = new TreeSet<>();
            for (Instruction insn : list) {
                Function f = getFunctionContaining(insn.getAddress());
                if (f != null) fns.add(f.getName() + " @ " + f.getEntryPoint());
            }
            out.println("containing functions (" + fns.size() + "):");
            out.println();
            int n = 0;
            for (String s : fns) {
                if (n++ >= 40) { out.println("- ... " + (fns.size() - 40) + " more"); break; }
                out.println("- `" + s + "`");
            }
            out.println();
        }
        out.println("**A function appearing under both `0x7a` and `0xe0` is the strip emitter.**");
        out.println();
    }

    // --------------------------------------------------------- decompilation

    private void decompileCandidates() {
        out.println("## 7. Decompilation of candidates");
        out.println();
        Set<Function> candidates = new LinkedHashSet<>();
        InstructionIterator ii = currentProgram.getListing().getInstructions(newBlockSet(), true);
        while (ii.hasNext()) {
            Instruction insn = ii.next();
            for (int op = 0; op < insn.getNumOperands(); op++) {
                Scalar s = insn.getScalar(op);
                if (s != null && s.getUnsignedValue() == 0x8fL) {
                    Function f = getFunctionContaining(insn.getAddress());
                    if (f != null) candidates.add(f);
                }
            }
        }
        if (candidates.isEmpty()) {
            out.println("No function in the block compares against `0x8f`.");
            out.println();
            out.println("That would be a genuinely important negative. It would mean either the");
            out.println("handshake is decoded from a USB-MIDI packet header (code index nibble `0x8`)");
            out.println("rather than the status byte, or the region needs more seeding before the");
            out.println("relevant code is disassembled. Check the section 3 function count first: a");
            out.println("low number means analysis, not absence, is the problem.");
            out.println();
            return;
        }
        DecompInterface decomp = new DecompInterface();
        try {
            decomp.setOptions(new DecompileOptions());
            decomp.openProgram(currentProgram);
            for (Function f : candidates) {
                out.println("### `" + f.getName() + "` @ `" + f.getEntryPoint() + "`");
                out.println();
                emitCallers(f);
                out.println("```c");
                try {
                    DecompileResults r = decomp.decompileFunction(f, 90, monitor);
                    out.println(r != null && r.decompileCompleted() && r.getDecompiledFunction() != null
                            ? r.getDecompiledFunction().getC()
                            : "// decompilation failed");
                }
                catch (Exception e) { out.println("// decompilation raised " + e); }
                out.println("```");
                out.println();
            }
        }
        finally { decomp.dispose(); }
    }

    private void emitCallers(Function f) {
        Set<String> callers = new TreeSet<>();
        for (Reference ref : getReferencesTo(f.getEntryPoint())) {
            Function c = getFunctionContaining(ref.getFromAddress());
            if (c != null) callers.add(c.getName() + " @ " + c.getEntryPoint());
        }
        out.println("callers: " + (callers.isEmpty() ? "_none found_" : String.join(", ", callers)));
        out.println();
    }

    // ------------------------------------------------------------- helpers

    private AddressSet newBlockSet() {
        return new AddressSet(blockStart, blockEnd);
    }

    private boolean inNewBlock(Address a) {
        return a != null && blockStart != null
                && a.getOffset() >= blockStart.getOffset()
                && a.getOffset() <= blockEnd.getOffset();
    }
}
