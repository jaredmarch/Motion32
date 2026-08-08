// Ghidra headless script: the three functions at the centre of the control model.
//
// The command-vocab probe's own sections 1 and 4 came back empty, and that is itself the result:
//
//   * All eight RAM anchors have ZERO literal-pool words in the payload image. Base+offset only
//     explains some of them (0x20004538 is reached from a literal 0x20004540 sitting in
//     FUN_0000140c's pool at 0x179c), but the two *queue* addresses have neither a reference nor
//     a plausible nearby base. Those two anchors from NativeMode_USB_EventStream_Report.md do
//     not describe this image and should not be trusted.
//   * All thirteen `0x26` sites are `movs`/`adds`, not one `cmp`. Nothing validates the Fender
//     device id on inbound SysEx.
//   * Section 3's CIN ranking is noise: 0x04-0x0e are ubiquitous small constants, so "40
//     functions use 3+ of them" means nothing. Dropped as an approach.
//
// What DID resolve came from host_config_probe_payload.md section 3, which decompiled the real
// control model:
//
//   FUN_000016f4   boot config: cfg = FUN_00000e50(); cfg==0 -> {rel=8, abs=2} else {rel=9, abs=1}
//   FUN_0000140c   encoder scan, 9 unrolled slots gated by rel count. Slot i keeps its current
//                  value at 0x20004538 + i*0x10 and its last at 0x2000453c + i*0x10, and emits
//                  FUN_00000fb0(id, delta) with id = (&DAT_00009664)[cfg*9 + i].
//   FUN_00001288   absolute scan, `abs` channels of 10-bit ADC with hysteresis (tolerance 12,
//                  tightening to 2 below 0xc / above 0x3f4), emitting FUN_00000eec(ch, value).
//                  On the Motion 32 abs == 2 — these are the two touch strips.
//
// So this probe goes after the only things still unknown, all of them small:
//
//   1. FUN_00000e50 — what it reads. If it is a GPIO/OTP product-strap, configuration is fixed
//      at boot and no handshake can move it. If it reads RAM someone else writes, it is not.
//   2. FUN_00000fb0 (relative emitter) and FUN_00000eec (absolute emitter) — do they branch on a
//      native-mode flag? Whatever they test IS the host-takeover switch, which is the original
//      question stated exactly.
//   3. Everything those three call, one level down, plus every writer of the flag they test.
//
// Usage: -postScript Motion32EmitterProbe.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.address.AddressSetView;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.scalar.Scalar;
import ghidra.program.model.symbol.Reference;
import ghidra.program.model.symbol.RefType;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Motion32EmitterProbe extends GhidraScript {

    /** The three functions the control model hangs off, by payload-image address. */
    private static final long SELECTOR = 0x00000e50L;  // returns the config index
    private static final long REL_EMIT = 0x00000fb0L;  // FUN_00000fb0(control_id, delta)
    private static final long ABS_EMIT = 0x00000eecL;  // FUN_00000eec(channel, value)
    private static final long BOOT_CFG = 0x000016f4L;  // sets rel/abs counts
    private static final long ENC_SCAN = 0x0000140cL;  // encoder scanner
    private static final long ABS_SCAN = 0x00001288L;  // absolute/touch-strip scanner

    /**
     * The two functions the last run identified but did not decompile.
     *
     * FUN_000010a4 is the real inbound parser: FUN_00002ab8 does nothing but `return 0x200040a0`
     * and FUN_000010a4 is its only caller. If a command vocabulary exists, it is in there.
     *
     * FUN_00000e5c is the boot path. It is the sole writer of DAT_20004291 (the product selector)
     * AND the caller of FUN_00002a14, which picks between two USB endpoint descriptor sets
     * (0x97e4 = endpoints 0-3, 0x9874 = endpoints 4-7). Whatever decides that argument is the
     * only thing in this firmware that looks like a genuine second configuration.
     */
    private static final long INBOUND_PARSER = 0x000010a4L;
    private static final long BOOT_PATH = 0x00000e5cL;
    private static final long USB_CFG_PICK = 0x00002a14L;
    private static final long RING_DRAIN = 0x00000ff4L;

    private static final long[] ROOTS = {
        SELECTOR, REL_EMIT, ABS_EMIT, BOOT_CFG, ENC_SCAN, ABS_SCAN,
        INBOUND_PARSER, BOOT_PATH, USB_CFG_PICK, RING_DRAIN,
    };

    /**
     * Instruction addresses that materialise the two queue addresses, found by scanning for the
     * MOVW encoding directly in the image.
     *
     * This is why the literal-pool scan came back empty and why my "those anchors are stale"
     * call was wrong: the core is ARMv7-M, so a 32-bit constant is built with a MOVW/MOVT
     * immediate pair (`44 f2 84 00` = MOVW r0,#0x4084; `c2 f2 00 00` = MOVT r0,#0x2000) and
     * never appears as bytes in a literal pool at all. Both anchors are real.
     *
     * `0x20004084` (outbound ring) is materialised at 17 sites, all inside the emitter cluster
     * 0x00000f00-0x00001080. `0x200040a0` (inbound queue) at exactly 3, all in 0x2a18-0x2ad4 —
     * that tight cluster is the inbound command parser, which is the thing the vocabulary
     * question was actually about.
     */
    private static final long[] INBOUND_SITES = { 0x00002a18L, 0x00002ab8L, 0x00002ad4L };

    /** Ring writers outside the six roots — the rest of the outbound event vocabulary. */
    private static final long[] RING_SITES = {
        0x00000f6cL, 0x0000100eL, 0x00001046L, 0x00001068L, 0x0000107eL,
    };

    private DecompInterface decomp;
    private PrintWriter out;

    @Override
    protected void run() throws Exception {
        String[] args = getScriptArgs();
        File target = new File(args.length > 0 ? args[0] : "emitter_probe.md");

        decomp = new DecompInterface();
        decomp.setOptions(new DecompileOptions());
        decomp.openProgram(currentProgram);

        out = new PrintWriter(target, "UTF-8");
        try {
            out.println("# Motion 32 — the emitters and the config selector");
            out.println();
            out.println("Program: `" + currentProgram.getName() + "`  ");
            out.println("Image base: `" + currentProgram.getImageBase() + "`");
            out.println();
            out.println("Only useful against the **payload** import; these are payload addresses.");
            out.println();

            sectionRoots();
            sectionQueueSites();
            sectionCallees();
            sectionPeripheralReads();

            out.println();
            out.println("---");
            out.println();
            out.println("## Reading order");
            out.println();
            out.println("1. `FUN_00000e50`. A read of a GPIO input register or an OTP/flash word means");
            out.println("   configuration is strapped at boot and no handshake can change it. A read of");
            out.println("   plain RAM means something writes it, and section 1 lists the writers.");
            out.println("2. `FUN_00000fb0` and `FUN_00000eec`. Any branch on a global inside these is");
            out.println("   the host-takeover switch. Its writers are the native-mode entry path.");
            out.println("3. Section 3 classifies every global each root touches as peripheral vs RAM,");
            out.println("   so question 1 can be answered without reading ARM by hand.");
        } finally {
            out.close();
            decomp.dispose();
        }
        println("Wrote " + target.getAbsolutePath());
    }

    // ------------------------------------------------------------------ 1
    private void sectionRoots() throws Exception {
        out.println("## 1. The six roots, decompiled, with callers and writers");
        out.println();
        for (long addr : ROOTS) {
            Function f = getFunctionAt(toAddr(addr));
            if (f == null) {
                out.println("### `" + String.format("%08x", addr) + "` — no function here");
                out.println();
                continue;
            }
            dumpFunction(f);

            out.println("**Callers:**");
            out.println();
            out.println("```text");
            Set<String> callers = new TreeSet<>();
            for (Reference r : getReferencesTo(f.getEntryPoint())) {
                Function c = getFunctionContaining(r.getFromAddress());
                if (c != null) {
                    callers.add(c.getName() + " @ " + c.getEntryPoint()
                            + "   [" + r.getReferenceType() + " from " + r.getFromAddress() + "]");
                }
            }
            if (callers.isEmpty()) {
                out.println("(none)");
            }
            for (String c : callers) {
                out.println(c);
            }
            out.println("```");
            out.println();

            out.println("**Globals this function touches, and who else WRITES them:**");
            out.println();
            out.println("```text");
            for (Address g : globalsTouched(f)) {
                // Stack and register addresses are not memory; getReferencesTo throws on them.
                // That threw before and killed sections 2 and 3 outright.
                if (!g.isMemoryAddress()) {
                    continue;
                }
                out.println(describeGlobal(g));
                for (Reference r : getReferencesTo(g)) {
                    if (!r.getReferenceType().isWrite()) {
                        continue;
                    }
                    Function w = getFunctionContaining(r.getFromAddress());
                    out.println("      written by " + (w != null ? w.getName() + " @ " + w.getEntryPoint()
                            : "(no function)") + "  at " + r.getFromAddress());
                }
            }
            out.println("```");
            out.println();
        }
    }

    // ------------------------------------------------------------------ 1b
    /**
     * The functions that touch the queues, resolved from MOVW sites rather than from references.
     * The inbound cluster is the interesting half: it is the command parser, and its small
     * constants are the accepted command ids.
     */
    private void sectionQueueSites() throws Exception {
        out.println("## 1b. Queue users, found via MOVW/MOVT rather than references");
        out.println();
        out.println("`getReferencesTo` and a literal-pool scan both return nothing for these");
        out.println("addresses because ARMv7-M builds 32-bit constants with MOVW/MOVT immediates,");
        out.println("so the address never exists as bytes anywhere. Both anchors are real.");
        out.println();

        dumpSiteGroup("Inbound queue `0x200040a0` — the command parser", INBOUND_SITES, true);
        dumpSiteGroup("Outbound ring `0x20004084` — remaining event emitters", RING_SITES, false);
    }

    private void dumpSiteGroup(String title, long[] sites, boolean withConstants) throws Exception {
        out.println("### " + title);
        out.println();
        Set<Function> fns = new LinkedHashSet<>();
        for (long s : sites) {
            Function f = getFunctionContaining(toAddr(s));
            if (f != null) {
                fns.add(f);
            } else {
                out.println("- `" + String.format("%08x", s) + "` is not inside a defined function");
            }
        }
        out.println();
        for (Function f : fns) {
            dumpFunction(f);

            out.println("**Callers:**");
            out.println();
            out.println("```text");
            Set<String> callers = new TreeSet<>();
            for (Reference r : getReferencesTo(f.getEntryPoint())) {
                Function c = getFunctionContaining(r.getFromAddress());
                if (c != null) {
                    callers.add(c.getName() + " @ " + c.getEntryPoint());
                }
            }
            if (callers.isEmpty()) {
                out.println("(none)");
            }
            for (String c : callers) {
                out.println(c);
            }
            out.println("```");
            out.println();

            if (withConstants) {
                out.println("**Every constant `<= 0x7f` — the candidate command ids:**");
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

    private List<String> smallScalars(Function f) {
        Set<String> seen = new TreeSet<>();
        InstructionIterator it = currentProgram.getListing().getInstructions(f.getBody(), true);
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

    // ------------------------------------------------------------------ 2
    private void sectionCallees() throws Exception {
        out.println("## 2. One level down");
        out.println();
        Set<Function> callees = new LinkedHashSet<>();
        for (long addr : ROOTS) {
            Function f = getFunctionAt(toAddr(addr));
            if (f != null) {
                callees.addAll(f.getCalledFunctions(monitor));
            }
        }
        for (long addr : ROOTS) {
            Function f = getFunctionAt(toAddr(addr));
            if (f != null) {
                callees.remove(f);
            }
        }
        out.println("Distinct callees: **" + callees.size() + "**");
        out.println();
        for (Function f : callees) {
            dumpFunction(f);
        }
    }

    // ------------------------------------------------------------------ 3
    private void sectionPeripheralReads() throws Exception {
        out.println("## 3. Peripheral vs RAM, per root");
        out.println();
        out.println("Cortex-M map: `0x40000000-0x5fffffff` peripheral, `0x20000000-0x3fffffff` SRAM,");
        out.println("`0x00000000-0x1fffffff` flash. A selector reading peripheral or flash is strapped;");
        out.println("one reading SRAM is set by software and therefore potentially reachable.");
        out.println();
        for (long addr : ROOTS) {
            Function f = getFunctionAt(toAddr(addr));
            if (f == null) {
                continue;
            }
            out.println("### `" + f.getName() + "`");
            out.println();
            out.println("```text");
            boolean any = false;
            for (Address g : globalsTouched(f)) {
                long v = g.getOffset();
                String region;
                if (v >= 0x40000000L && v < 0x60000000L) {
                    region = "PERIPHERAL";
                } else if (v >= 0x20000000L && v < 0x40000000L) {
                    region = "SRAM";
                } else if (v < 0x20000000L) {
                    region = "FLASH/RODATA";
                } else {
                    region = "other";
                }
                out.println(String.format("  %-14s %s", region, g));
                any = true;
            }
            // Also surface raw large constants, which is how MMIO often appears.
            InstructionIterator it = currentProgram.getListing().getInstructions(f.getBody(), true);
            Set<String> consts = new TreeSet<>();
            while (it.hasNext()) {
                Instruction insn = it.next();
                for (int i = 0; i < insn.getNumOperands(); i++) {
                    Scalar s = insn.getScalar(i);
                    if (s == null) {
                        continue;
                    }
                    long v = s.getUnsignedValue();
                    if (v >= 0x40000000L && v < 0x60000000L) {
                        consts.add(String.format("  PERIPHERAL-CONST 0x%08x  (%s  %s)",
                                v, insn.getAddress(), insn));
                        any = true;
                    }
                }
            }
            for (String c : consts) {
                out.println(c);
            }
            if (!any) {
                out.println("  (no globals resolved — decompiler output above is authoritative)");
            }
            out.println("```");
            out.println();
        }
    }

    // ------------------------------------------------------------------ helpers
    private List<Address> globalsTouched(Function f) {
        Set<Address> seen = new java.util.LinkedHashSet<>();
        InstructionIterator it = currentProgram.getListing().getInstructions(f.getBody(), true);
        while (it.hasNext()) {
            Instruction insn = it.next();
            for (Reference r : insn.getReferencesFrom()) {
                if (r.getReferenceType().isData()) {
                    seen.add(r.getToAddress());
                }
            }
        }
        return new ArrayList<>(seen);
    }

    private String describeGlobal(Address g) {
        StringBuilder sb = new StringBuilder("  " + g);
        try {
            sb.append("  = ").append(String.format("0x%08x",
                    currentProgram.getMemory().getInt(g) & 0xffffffffL));
        } catch (Exception e) {
            sb.append("  (uninitialised)");
        }
        return sb.toString();
    }

    private void dumpFunction(Function f) {
        out.println("### `" + f.getName() + "` @ `" + f.getEntryPoint() + "`");
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
