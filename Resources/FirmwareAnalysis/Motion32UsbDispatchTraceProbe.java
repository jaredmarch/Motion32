// Ghidra headless script: trace USB-MIDI receive dispatch/callback tables.
// Usage:
//   -postScript Motion32UsbDispatchTraceProbe.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.address.AddressSetView;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.mem.MemoryBlock;
import ghidra.program.model.scalar.Scalar;
import ghidra.program.model.symbol.Reference;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Motion32UsbDispatchTraceProbe extends GhidraScript {
    private static final long[] FOCUS_ADDRS = {
        0x03a14L, 0x03ab8L, 0x03ac4L, 0x03af0L,
        0x04854L, 0x05854L,
        0x097e4L, 0x09818L, 0x09874L, 0x098c4L
    };

    private static final long[] POINTER_TARGETS = {
        0x03ac4L, 0x03af0L, 0x097e4L, 0x09818L, 0x09874L, 0x098c4L
    };

    private PrintWriter out;
    private DecompInterface decompiler;

    private static class Hit {
        Function fn;
        int score;
        String c;
        List<String> reasons = new ArrayList<String>();
    }

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/usb_dispatch_trace_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 USB-MIDI Dispatch Trace Probe");
        out.println();
        out.println("Focus: endpoint setup around `FUN_00003a14`, callback labels near");
        out.println("`0x97e4`/`0x9874`, and any recovered path that resembles USB-MIDI");
        out.println("CIN `0x08` / Note Off packet handling.");
        out.println();

        writeFocusFunctions();
        writePointerTableHits();
        writeRankedCinHits();

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private void writeFocusFunctions() throws Exception {
        out.println("## Focus Functions / Labels");
        out.println();
        for (long raw : FOCUS_ADDRS) {
            Address addr = toAddr(raw);
            Function fn = getFunctionAt(addr);
            if (fn == null) {
                fn = getFunctionContaining(addr);
            }
            if (fn == null) {
                disassemble(addr);
                try {
                    createFunction(addr, "PROBE_" + addr.toString());
                }
                catch (Exception ignored) {
                }
                fn = getFunctionAt(addr);
            }
            out.printf("### `%s` `%s`%n%n", addr, fn == null ? "<none>" : fn.getName());
            writeReferencesTo(addr);
            dumpInstructions(addr, 18);
            if (fn != null) {
                dumpDecompile(fn, 220);
            }
        }
    }

    private void writeReferencesTo(Address target) {
        out.println("References to this address:");
        int count = 0;
        for (Reference ref : getReferencesTo(target)) {
            Function fn = getFunctionContaining(ref.getFromAddress());
            out.printf("- from `%s` in `%s` @ `%s` type=%s%n",
                ref.getFromAddress(),
                fn == null ? "<none>" : fn.getName(),
                fn == null ? "<none>" : fn.getEntryPoint().toString(),
                ref.getReferenceType());
            count++;
        }
        if (count == 0) {
            out.println("- none");
        }
        out.println();
    }

    private void writePointerTableHits() throws Exception {
        out.println("## Raw Function-Pointer / Callback Table Hits");
        out.println();
        for (long target : POINTER_TARGETS) {
            out.printf("### target `%08x` / thumb `%08x`%n%n", target, target | 1);
            int hits = 0;
            for (MemoryBlock block : currentProgram.getMemory().getBlocks()) {
                if (!block.isInitialized()) {
                    continue;
                }
                Address start = block.getStart();
                Address end = block.getEnd();
                Address cur = start;
                while (cur.compareTo(end) <= 0 && cur.addNoWrap(3).compareTo(end) <= 0) {
                    long value = getIntLE(cur);
                    if (value == target || value == (target | 1)) {
                        Function fn = getFunctionContaining(cur);
                        out.printf("- `%s`: value `%08x` in block `%s`, containing `%s` @ `%s`%n",
                            cur, value, block.getName(),
                            fn == null ? "<none>" : fn.getName(),
                            fn == null ? "<none>" : fn.getEntryPoint().toString());
                        dumpInstructions(cur, 8);
                        hits++;
                        if (hits >= 60) {
                            out.println("- truncated");
                            break;
                        }
                    }
                    cur = cur.addNoWrap(1);
                }
            }
            if (hits == 0) {
                out.println("- no raw pointer-sized hits found");
            }
            out.println();
        }
    }

    private void writeRankedCinHits() throws Exception {
        out.println("## Ranked CIN / Channel-Voice Receive Candidates");
        out.println();
        List<Hit> hits = new ArrayList<Hit>();
        FunctionIterator it = currentProgram.getFunctionManager().getFunctions(true);
        while (it.hasNext()) {
            Function fn = it.next();
            DecompileResults results = decompiler.decompileFunction(fn, 20, monitor);
            if (!results.decompileCompleted() || results.getDecompiledFunction() == null) {
                continue;
            }
            String c = results.getDecompiledFunction().getC();
            Hit hit = score(fn, c);
            if (hit.score >= 34) {
                hit.c = c;
                hits.add(hit);
            }
        }
        Collections.sort(hits, new Comparator<Hit>() {
            public int compare(Hit a, Hit b) {
                return b.score - a.score;
            }
        });
        int count = Math.min(35, hits.size());
        for (int i = 0; i < count; i++) {
            Hit hit = hits.get(i);
            out.printf("### `%s` @ `%s` score `%d`%n%n",
                hit.fn.getName(), hit.fn.getEntryPoint(), hit.score);
            out.println("- reasons: " + String.join(", ", hit.reasons));
            out.println();
            dumpDecompileText(hit.c, 140);
        }
        if (count == 0) {
            out.println("No candidates crossed the threshold.");
        }
    }

    private Hit score(Function fn, String c) {
        Hit hit = new Hit();
        hit.fn = fn;
        addIf(hit, containsAny(c, "+ 4)", "+4)", "[4]", "param_1 + 4", "param_2 + 4"), 12, "event/CIN byte offset 4");
        addIf(hit, containsAny(c, "+ 8)", "+8)", "[8]", "param_1 + 8", "param_2 + 8"), 12, "payload byte offset 8");
        addIf(hit, containsAny(c, "== '\\b'", "== 8", "==0x8", "== 0x8", "0x8)"), 10, "possible CIN 0x08");
        addIf(hit, containsAny(c, "== '\\x02'", "== 2", "==0x2", "== 0x2"), 6, "observed event code 0x02");
        addIf(hit, containsAny(c, "== '\\x04'", "== 4", "==0x4", "== 0x4"), 6, "observed event code 0x04");
        addIf(hit, containsAny(c, "0x8f", "0x80", "& 0xf0", "&0xf0", "& 0xf", "&0xf"), 16, "channel-voice/status nibble clue");
        addIf(hit, containsAny(c, "0x7f", "127"), 6, "value 127");
        addIf(hit, containsAny(c, "0x200040a0", "FUN_00001d6c", "FUN_000020a4", "DAT_20005b60"), 20, "known inbound SysEx queue path");
        addIf(hit, containsAny(c, "0x20005cd4", "0x20005d24", "0x20003800", "0x40047000"), 12, "USB endpoint context/register state");
        addIf(hit, containsAny(c, "switch", "case"), 6, "dispatch structure");
        addIf(hit, containsAny(c, "UTF", "glyph", "font", "draw", "lv_"), -16, "text/graphics false positive");
        addIf(hit, containsAny(c, "0x8f0", "FUN_0002654c", "FUN_0002754c"), -12, "outgoing SysEx false positive");
        return hit;
    }

    private boolean hasScalar(Instruction ins, long value) {
        for (int i = 0; i < ins.getNumOperands(); i++) {
            Object[] objs = ins.getOpObjects(i);
            for (Object obj : objs) {
                if (obj instanceof Scalar && ((Scalar)obj).getUnsignedValue() == value) {
                    return true;
                }
            }
        }
        return false;
    }

    private long getIntLE(Address address) throws Exception {
        long b0 = currentProgram.getMemory().getByte(address) & 0xffL;
        long b1 = currentProgram.getMemory().getByte(address.addNoWrap(1)) & 0xffL;
        long b2 = currentProgram.getMemory().getByte(address.addNoWrap(2)) & 0xffL;
        long b3 = currentProgram.getMemory().getByte(address.addNoWrap(3)) & 0xffL;
        return b0 | (b1 << 8) | (b2 << 16) | (b3 << 24);
    }

    private void dumpInstructions(Address address, int radius) {
        out.printf("Instructions near `%s`:%n%n", address);
        out.println("```asm");
        Instruction cur = getInstructionAt(address);
        if (cur == null) {
            cur = currentProgram.getListing().getInstructionAfter(address);
        }
        for (int i = 0; i < radius && cur != null; i++) {
            Instruction prev = currentProgram.getListing().getInstructionBefore(cur.getAddress());
            if (prev == null) {
                break;
            }
            cur = prev;
        }
        for (int i = 0; i < radius * 2 + 1 && cur != null; i++) {
            out.printf("%s: %s%n", cur.getAddress(), cur);
            cur = currentProgram.getListing().getInstructionAfter(cur.getAddress());
        }
        out.println("```");
        out.println();
    }

    private void dumpDecompile(Function fn, int maxLines) throws Exception {
        DecompileResults results = decompiler.decompileFunction(fn, 30, monitor);
        out.println("```c");
        if (!results.decompileCompleted() || results.getDecompiledFunction() == null) {
            out.println("/* decompile failed */");
        }
        else {
            dumpDecompileTextRaw(results.getDecompiledFunction().getC(), maxLines);
        }
        out.println("```");
        out.println();
    }

    private void dumpDecompileText(String c, int maxLines) {
        out.println("```c");
        dumpDecompileTextRaw(c, maxLines);
        out.println("```");
        out.println();
    }

    private void dumpDecompileTextRaw(String c, int maxLines) {
        String[] lines = c.split("\\n");
        for (int i = 0; i < lines.length && i < maxLines; i++) {
            out.println(lines[i]);
        }
        if (lines.length > maxLines) {
            out.println("/* ... truncated ... */");
        }
    }

    private boolean containsAny(String s, String... needles) {
        for (String needle : needles) {
            if (s.contains(needle)) {
                return true;
            }
        }
        return false;
    }

    private void addIf(Hit hit, boolean condition, int points, String reason) {
        if (condition) {
            hit.score += points;
            hit.reasons.add(reason);
        }
    }
}
