// ⚠️ SUPERSEDED — DO NOT RUN EXPECTING NEWS. Kept for its method, not its question.
//
// This probe hunts internal id 0x72 on the hypothesis that it was the native-mode trigger.
// **That hypothesis was wrong and has been retracted.** The handshake carries id 0x0f, from the
// inbound assignment table, and is handled by FUN_101044b8 — see native_mode_lifecycle_resolved.md.
// Every consumer of 0x72 that has been found discards it.
//
// The lifecycle is now fully mapped (lifecycle_state_machine.md) and the strip translation chain
// with it (strip_translation_chain.md). Sections 4 and 5 below — the app's own 0xF0 SysEx handler
// at 0x10106928, and whether a host can reach the configuration setters — remain genuinely
// unexplored and are the only reason to keep this file.
//
// ---------------------------------------------------------------------------------------------
// Ghidra headless script: find the consumer of internal id 0x72 and the host-reachable path
// to the MIDI assignment setters.
//
// CONTEXT — read app_midi_routing_engine.md first.
//
// The application (second code region, runtime base 0x10100000, file offset 0x20000) contains a
// full MIDI routing engine. What is already established:
//
//   FUN_1010671c(port, byte)      running-status parser; per-port ctx stride 0x1f0
//   FUN_101065f4(port, st, d1, d2) channel-voice handler
//   FUN_10106508(...)             event-5 callback; routes outward, but ONLY for id < 0x40
//   FUN_1010646c(dest, st, d1, d2) builds the 4-byte USB-MIDI packet (cable<<4)|CIN
//
//   0x20002088  inbound assignment table  [channel][port] -> source id   (0x7f = unassigned)
//   0x20001e88  outbound routing table    [source][dest]  -> channel     (0xff = unrouted)
//   0x20003f78  per-port parser ctx, stride 0x1f0; +0 enable, +1 type, +2 OWN CHANNEL
//   0x20001e80  event-5 message struct: [0] type, [1] id, [2..3] d1, [4..5] d2
//
// The key line in FUN_101065f4: when the incoming channel equals the port's own channel, the
// message is tagged with the fixed id 0x72 rather than a table lookup. FUN_10106508 forwards only
// ids < 0x40, so 0x72 is consumed internally and never reaches an output. `8F 00 7F` is Note Off
// on channel 0x0F and fits that path exactly.
//
// WHAT IS MISSING: the consumer that acts on id 0x72. That is the mode switch. This probe hunts it.
//
// It also answers the question that replaced "can we patch the firmware": the assignment is a RAM
// table written by setters around 0x10106ae0-0x10106b80, so if a host-reachable path reaches those
// setters, retargeting the strips needs no firmware modification at all.
//
// USAGE (read-only; the block must already exist from Motion32NativeBlockProbe):
//   ~/Downloads/ghidra_12.1.2_PUBLIC/support/analyzeHeadless \
//     "<repo>/Resources/FirmwareAnalysis/ghidra_project" Motion32Firmware \
//     -process motion32_fw_payload_0x1000.bin -noanalysis -readOnly \
//     -scriptPath "<repo>/Resources/FirmwareAnalysis" \
//     -postScript Motion32NativeSwitchProbe.java "<repo>/Resources/FirmwareAnalysis/native_switch_probe.md"

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.address.AddressSet;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
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

public class Motion32NativeSwitchProbe extends GhidraScript {

    private static final long APP_BASE = 0x10100000L;
    private static final long APP_TOP  = 0x101990a4L;
    private static final long DELTA    = 0x100e0000L;

    // Established anchors.
    private static final long F_EVENT_POST   = 0x10100264L;  // FUN_10100264(event, arg)
    private static final long F_PARSER       = 0x1010671cL;  // byte-stream parser
    private static final long F_CHANVOICE    = 0x101065f4L;  // channel-voice handler
    private static final long F_EVENT5_CB    = 0x10106508L;  // event-5 callback (routes id < 0x40)
    private static final long F_EMIT         = 0x1010646cL;  // USB-MIDI packet builder
    private static final long F_SYSEX_F0     = 0x10106928L;  // app's own 0xF0 handler
    private static final long EVENT_TABLE    = 0x101964f0L;  // flash event table

    // The configuration setter cluster.
    private static final long SETTERS_LO     = 0x10106ad0L;
    private static final long SETTERS_HI     = 0x10106b90L;

    // RAM structures.
    private static final long TBL_INBOUND    = 0x20002088L;
    private static final long TBL_OUTBOUND   = 0x20001e88L;
    private static final long CTX_PORT       = 0x20003f78L;
    private static final long MSG_STRUCT     = 0x20001e80L;

    private PrintWriter out;
    private DecompInterface decomp;

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        out = new PrintWriter(new File(args.length > 0 ? args[0] : "native_switch_probe.md"), "UTF-8");
        decomp = new DecompInterface();
        try {
            decomp.setOptions(new DecompileOptions());
            decomp.openProgram(currentProgram);

            out.println("# Motion 32 — the native-mode switch, and the path to the setters");
            out.println();
            if (!checkEnvironment()) return;

            dumpEventTable();
            probeEventPost();
            hunt0x72();
            probeSysExHandler();
            probeSetters();
            probeReceiveEntry();

            out.println();
            out.println("---");
            out.println();
            out.println("Generated by `Motion32NativeSwitchProbe.java`.");
        } finally {
            if (decomp != null) decomp.dispose();
            out.close();
        }
        println("Report written.");
    }

    // ------------------------------------------------------------ environment

    private boolean checkEnvironment() {
        out.println("## 0. Environment");
        out.println();
        MemoryBlock b = null;
        for (MemoryBlock blk : currentProgram.getMemory().getBlocks()) {
            if (blk.getStart().getOffset() <= APP_BASE && blk.getEnd().getOffset() >= APP_BASE) {
                b = blk; break;
            }
        }
        if (b == null) {
            out.println("**ABORT** — nothing is mapped at `0x10100000`.");
            out.println();
            out.println("Run `Motion32NativeBlockProbe.java` first, or add the block by hand:");
            out.println("start `0x10100000`, length `0x990a4`, File Bytes offset `0x20000`.");
            return false;
        }
        out.println("App block: `" + b.getName() + "` `" + b.getStart() + "`-`" + b.getEnd() + "`");
        int n = 0;
        for (Function f : currentProgram.getFunctionManager().getFunctions(true)) {
            long a = f.getEntryPoint().getOffset();
            if (a >= APP_BASE && a <= APP_TOP) n++;
        }
        out.println("Functions in the app region: **" + n + "**");
        out.println();
        if (n < 200) {
            out.println("⚠️ That is low. Analysis may have under-run, which would make the");
            out.println("cross-reference sections below misleadingly empty.");
            out.println();
        }
        return true;
    }

    // ------------------------------------------------------------ event table

    private void dumpEventTable() {
        out.println("## 1. Flash event table @ `0x101964f0`");
        out.println();
        out.println("Walked until an entry stops looking like `{event, init, callback}`.");
        out.println();
        out.println("| # | event | init | callback |");
        out.println("|---|---|---|---|");
        for (int i = 0; i < 48; i++) {
            try {
                Address at = toAddr(EVENT_TABLE + 12L * i);
                int ev = getInt(at);
                long init = getInt(at.add(4)) & 0xffffffffL;
                long cb = getInt(at.add(8)) & 0xffffffffL;
                boolean ok = (init >= APP_BASE && init <= APP_TOP)
                          && (cb >= APP_BASE && cb <= APP_TOP);
                if (!ok) break;
                out.println("| " + i + " | `" + ev + "` | `0x" + Long.toHexString(init)
                        + "` | `0x" + Long.toHexString(cb) + "` |");
                ensureFunction(init & ~1L);
                ensureFunction(cb & ~1L);
            }
            catch (Exception e) { break; }
        }
        out.println();
        out.println("Every init and callback above has been defined as a function so the");
        out.println("cross-references below can see them.");
        out.println();
    }

    // ------------------------------------------------------- the post function

    private void probeEventPost() {
        out.println("## 2. `FUN_10100264` — the event post");
        out.println();
        out.println("`FUN_10100264(5, 0)` is what `FUN_101065f4` calls after tagging a message.");
        out.println("Understanding its dispatch tells us who can receive event 5.");
        out.println();
        emitFunction(F_EVENT_POST, true);

        out.println("### Every call site, with the event number where it is a literal");
        out.println();
        Function post = getFunctionAt(toAddr(F_EVENT_POST));
        if (post == null) { out.println("_function not defined_"); out.println(); return; }
        List<String> rows = new ArrayList<>();
        for (Reference ref : getReferencesTo(post.getEntryPoint())) {
            Address from = ref.getFromAddress();
            Function in = getFunctionContaining(from);
            String ev = literalArgBefore(from);
            rows.add("| `" + from + "` | " + (in != null ? "`" + in.getName() + "`" : "—")
                    + " | " + (ev == null ? "?" : "`" + ev + "`") + " |");
        }
        if (rows.isEmpty()) out.println("_no references found — analysis likely under-ran_");
        else {
            out.println("| call site | in function | event # |");
            out.println("|---|---|---|");
            for (String r : rows) out.println(r);
        }
        out.println();
        out.println("**Rows with event `5` are the producers.** The consumer side is the callback");
        out.println("registered in the table in section 1 — entry 1, `0x10106509`, is");
        out.println("`FUN_10106508`, which forwards only ids `< 0x40`. If any *other* code also");
        out.println("receives event 5, it is the candidate for handling `0x72`.");
        out.println();
    }

    // ------------------------------------------------------------- the id 0x72

    private void hunt0x72() {
        out.println("## 3. The internal id `0x72`");
        out.println();
        out.println("`FUN_101065f4` writes `0x72` when the incoming channel equals the port's own");
        out.println("channel. Something must compare against it. Also listed: `0x40` (the routable");
        out.println("boundary) and `0x7f` (unassigned), because the consumer probably tests those too.");
        out.println();
        long[] wanted = { 0x72L, 0x40L, 0x7fL, 0x0fL };
        for (long w : wanted) {
            Set<String> fns = new TreeSet<>();
            List<String> sites = new ArrayList<>();
            InstructionIterator ii = currentProgram.getListing()
                    .getInstructions(new AddressSet(toAddr(APP_BASE), toAddr(APP_TOP)), true);
            while (ii.hasNext()) {
                Instruction insn = ii.next();
                String m = insn.getMnemonicString().toLowerCase();
                boolean cmpLike = m.startsWith("cmp") || m.startsWith("sub")
                        || m.startsWith("and") || m.startsWith("mov") || m.startsWith("teq");
                if (!cmpLike) continue;
                for (int op = 0; op < insn.getNumOperands(); op++) {
                    Scalar s = insn.getScalar(op);
                    if (s != null && s.getUnsignedValue() == w) {
                        Function f = getFunctionContaining(insn.getAddress());
                        sites.add(insn.getAddress() + "  " + insn
                                + (f != null ? "   in " + f.getName() : ""));
                        if (f != null) fns.add(f.getName() + " @ " + f.getEntryPoint());
                    }
                }
            }
            out.println("### `0x" + Long.toHexString(w) + "` — " + sites.size() + " site(s), "
                    + fns.size() + " function(s)");
            out.println();
            if (sites.isEmpty()) { out.println("_none_"); out.println(); continue; }
            out.println("```");
            int k = 0;
            for (String s : sites) {
                if (k++ >= 80) { out.println("... " + (sites.size() - 80) + " more"); break; }
                out.println(s);
            }
            out.println("```");
            out.println();
        }
        out.println("**A function comparing against `0x72` that is not `FUN_101065f4` is the answer.**");
        out.println("Decompile it by hand if it is not already covered below.");
        out.println();
    }

    // --------------------------------------------------------- the SysEx entry

    private void probeSysExHandler() {
        out.println("## 4. `0x10106928` — the application's own `0xF0` handler");
        out.println();
        out.println("Distinct from the base-0 updater parser at `FUN_000010a4`. This is the one a");
        out.println("host could actually talk to while the device is running normally. The question");
        out.println("is whether anything downstream of it reaches the setters in section 5.");
        out.println();
        ensureFunction(F_SYSEX_F0);
        emitFunction(F_SYSEX_F0, true);
        out.println("### Callees, two levels deep");
        out.println();
        Set<Long> seen = new LinkedHashSet<>();
        collectCallees(F_SYSEX_F0, 2, seen);
        if (seen.isEmpty()) out.println("_none resolved_");
        for (Long a : seen) {
            Function f = getFunctionAt(toAddr(a));
            boolean isSetter = a >= SETTERS_LO && a <= SETTERS_HI;
            out.println("- `0x" + Long.toHexString(a) + "`"
                    + (f != null ? " `" + f.getName() + "`" : "")
                    + (isSetter ? "  **<- REACHES THE SETTER CLUSTER**" : ""));
        }
        out.println();
        out.println("If any line above is marked, a host-reachable configuration path exists and");
        out.println("the strips can be retargeted without touching firmware.");
        out.println();
    }

    // ------------------------------------------------------------- the setters

    private void probeSetters() {
        out.println("## 5. The configuration setters `0x10106ad0`-`0x10106b90`");
        out.println();
        out.println("These write the RAM tables. Whoever calls them is what native mode changes.");
        out.println();
        for (long a = SETTERS_LO; a < SETTERS_HI; a += 2) {
            Function f = getFunctionAt(toAddr(a));
            if (f == null) continue;
            out.println("### `" + f.getName() + "` @ `" + f.getEntryPoint() + "`");
            out.println();
            emitCallers(f);
            out.println("```c");
            out.println(decompile(f));
            out.println("```");
            out.println();
        }
        out.println("### Anything that references the RAM tables directly");
        out.println();
        long[] ram = { TBL_INBOUND, TBL_OUTBOUND, CTX_PORT, MSG_STRUCT };
        String[] names = { "inbound assignment", "outbound routing", "per-port ctx", "msg struct" };
        for (int i = 0; i < ram.length; i++) {
            out.println("**" + names[i] + "** `0x" + Long.toHexString(ram[i]) + "`:");
            Set<String> fns = new TreeSet<>();
            for (Reference ref : getReferencesTo(toAddr(ram[i]))) {
                Function f = getFunctionContaining(ref.getFromAddress());
                if (f != null) fns.add(f.getName() + " @ " + f.getEntryPoint());
            }
            out.println(fns.isEmpty() ? "  _no direct references (loaded from literal pools)_"
                    : "  " + String.join(", ", fns));
            out.println();
        }
        out.println("Thumb-1 code loads constants via `ldr rX,[pc,#imm]`, so Ghidra often records no");
        out.println("reference. If the lists above are empty that is expected, not a failure — the");
        out.println("literal-pool addresses are `0x10106718`, `0x10106b7c` (inbound) and");
        out.println("`0x10106454`, `0x10106548`, `0x10106bac` (outbound).");
        out.println();
    }

    // -------------------------------------------------------- receive entry

    private void probeReceiveEntry() {
        out.println("## 6. Who feeds the parser");
        out.println();
        out.println("Tracing upward from the parser reaches the USB receive path for the application,");
        out.println("which the base-0 region never had.");
        out.println();
        long[] fns = { F_PARSER, F_CHANVOICE, F_EVENT5_CB, F_EMIT };
        String[] labels = { "parser FUN_1010671c", "channel-voice FUN_101065f4",
                            "event-5 callback FUN_10106508", "USB-MIDI emit FUN_1010646c" };
        for (int i = 0; i < fns.length; i++) {
            ensureFunction(fns[i]);
            Function f = getFunctionAt(toAddr(fns[i]));
            out.println("### " + labels[i]);
            out.println();
            if (f == null) { out.println("_not defined_"); out.println(); continue; }
            emitCallers(f);
        }
    }

    // --------------------------------------------------------------- helpers

    private void ensureFunction(long addr) {
        try {
            Address a = toAddr(addr & ~1L);
            if (getInstructionAt(a) == null) disassemble(a);
            if (getFunctionAt(a) == null) createFunction(a, null);
        }
        catch (Exception ignored) { }
    }

    /** Best-effort: the most recent literal moved into r0 before a call. */
    private String literalArgBefore(Address callSite) {
        try {
            Instruction insn = getInstructionAt(callSite);
            for (int i = 0; i < 8 && insn != null; i++) {
                insn = insn.getPrevious();
                if (insn == null) break;
                if (insn.getMnemonicString().toLowerCase().startsWith("mov")
                        && insn.getNumOperands() > 1
                        && insn.getRegister(0) != null
                        && "r0".equalsIgnoreCase(insn.getRegister(0).getName())) {
                    Scalar s = insn.getScalar(1);
                    if (s != null) return Long.toString(s.getUnsignedValue());
                }
            }
        }
        catch (Exception ignored) { }
        return null;
    }

    private void collectCallees(long from, int depth, Set<Long> acc) {
        if (depth <= 0) return;
        Function f = getFunctionAt(toAddr(from));
        if (f == null) return;
        for (Function c : f.getCalledFunctions(monitor)) {
            long a = c.getEntryPoint().getOffset();
            if (acc.add(a)) collectCallees(a, depth - 1, acc);
        }
    }

    private void emitCallers(Function f) {
        Set<String> callers = new TreeSet<>();
        for (Reference ref : getReferencesTo(f.getEntryPoint())) {
            Function c = getFunctionContaining(ref.getFromAddress());
            callers.add(c != null ? c.getName() + " @ " + c.getEntryPoint()
                                  : "raw " + ref.getFromAddress());
        }
        out.println("callers (" + callers.size() + "): "
                + (callers.isEmpty() ? "_none_" : String.join(", ", callers)));
        out.println();
    }

    private void emitFunction(long addr, boolean withC) {
        ensureFunction(addr);
        Function f = getFunctionAt(toAddr(addr & ~1L));
        if (f == null) {
            out.println("`0x" + Long.toHexString(addr) + "` — could not define a function here.");
            out.println();
            return;
        }
        out.println("### `" + f.getName() + "` @ `" + f.getEntryPoint() + "`");
        out.println();
        emitCallers(f);
        if (withC) {
            out.println("```c");
            out.println(decompile(f));
            out.println("```");
            out.println();
        }
    }

    private String decompile(Function f) {
        try {
            DecompileResults r = decomp.decompileFunction(f, 90, monitor);
            if (r != null && r.decompileCompleted() && r.getDecompiledFunction() != null) {
                return r.getDecompiledFunction().getC();
            }
            return "// decompilation did not complete";
        }
        catch (Exception e) { return "// decompilation raised " + e; }
    }
}
