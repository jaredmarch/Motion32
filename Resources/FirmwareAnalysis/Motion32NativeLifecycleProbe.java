// Ghidra headless script: hunt for the real host/native lifecycle receive path.
// Usage:
//   -postScript Motion32NativeLifecycleProbe.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.scalar.Scalar;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Motion32NativeLifecycleProbe extends GhidraScript {
    private PrintWriter out;
    private DecompInterface decompiler;

    private static class Hit {
        Function fn;
        int score;
        List<String> reasons = new ArrayList<String>();
        String c;
    }

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/native_lifecycle_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        List<Hit> hits = scanFunctions();
        Collections.sort(hits, new Comparator<Hit>() {
            public int compare(Hit a, Hit b) {
                return b.score - a.score;
            }
        });

        out.println("# Motion 32 Native Lifecycle Probe");
        out.println();
        out.println("Target: host command `8F 00 7F` / `8F 00 00`.");
        out.println("This pass scores decompiled functions for channel-voice MIDI parsing patterns,");
        out.println("USB-MIDI CIN/note-off handling, and writes to RAM state near known control flags.");
        out.println();

        writeScalarSites();
        writeHits(hits);

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private List<Hit> scanFunctions() throws Exception {
        List<Hit> hits = new ArrayList<Hit>();
        FunctionIterator it = currentProgram.getFunctionManager().getFunctions(true);
        while (it.hasNext()) {
            Function fn = it.next();
            DecompileResults results = decompiler.decompileFunction(fn, 20, monitor);
            if (!results.decompileCompleted() || results.getDecompiledFunction() == null) {
                continue;
            }
            String c = results.getDecompiledFunction().getC();
            Hit h = score(fn, c);
            if (h.score >= 36) {
                h.c = c;
                hits.add(h);
            }
        }
        return hits;
    }

    private Hit score(Function fn, String c) {
        Hit h = new Hit();
        h.fn = fn;

        addIf(h, containsAny(c, "0x8f", "0x8f00", "0x7f008f"), 35, "exact 8f-ish constant");
        addIf(h, containsAny(c, "0x8 ", "0x8)", "== 8", "==0x8"), 8, "possible USB-MIDI note-off CIN");
        addIf(h, containsAny(c, "0x80", "0x90", "0xb0"), 8, "MIDI status-class constant");
        addIf(h, containsAny(c, "& 0xf0", "&0xf0", ">> 4", ">>4"), 18, "status high-nibble test");
        addIf(h, containsAny(c, "& 0xf", "&0xf", "& 0xfU", "&0xfU"), 12, "channel low-nibble test");
        addIf(h, containsAny(c, "0x7f", "0x7fU", "127"), 10, "velocity/value 127");
        addIf(h, containsAny(c, "== 0", "==0", "!= 0", "!=0"), 5, "zero/nonzero tests");
        addIf(h, containsAny(c, "[0]", "[1]", "[2]", "[3]", "+ 1)", "+ 2)", "+ 3)", "param_1 + 1", "param_1 + 2", "param_1 + 3"), 12, "byte packet indexing");
        addIf(h, containsAny(c, "20005c", "20005b", "200040", "200042", "200064"), 16, "known RAM/control state");
        addIf(h, containsAny(c, "FUN_00001d6c", "FUN_000020a4", "FUN_00002098", "FUN_00003fb8"), 14, "near known queue/event helpers");
        addIf(h, containsAny(c, "switch", "case"), 6, "dispatch structure");

        addIf(h, containsAny(c, "UTF", "0xc0)","0xe0)"), -16, "UTF/text false positive");
        addIf(h, c.contains("FUN_0002754c"), -14, "outgoing MIDI/SysEx send false positive");
        addIf(h, c.contains("0x8f0"), -16, "little-endian F0 08 false positive");
        addIf(h, containsAny(c, "lv_", "draw", "font", "glyph"), -14, "graphics/text false positive");

        return h;
    }

    private void writeScalarSites() {
        out.println("## Interesting Scalar Sites");
        out.println();
        long[] values = {0x8fL, 0x8L, 0x7fL, 0x80L, 0xf0L, 0xfL, 0x20005cb6L, 0x20005cb8L};
        for (long value : values) {
            out.printf("### `0x%x`%n%n", value);
            int count = 0;
            Instruction ins = currentProgram.getListing().getInstructions(true).next();
            while (ins != null) {
                if (hasScalar(ins, value)) {
                    Function fn = getFunctionContaining(ins.getAddress());
                    out.printf("- `%s`: `%s` in `%s` @ `%s`%n",
                        ins.getAddress(),
                        ins,
                        fn == null ? "<none>" : fn.getName(),
                        fn == null ? "<none>" : fn.getEntryPoint().toString());
                    count++;
                    if (count >= 80) {
                        out.println("- truncated");
                        break;
                    }
                }
                ins = currentProgram.getListing().getInstructionAfter(ins.getAddress());
            }
            if (count == 0) {
                out.println("- no scalar operands found");
            }
            out.println();
        }
    }

    private boolean hasScalar(Instruction ins, long value) {
        for (int i = 0; i < ins.getNumOperands(); i++) {
            Object[] objs = ins.getOpObjects(i);
            for (Object obj : objs) {
                if (obj instanceof Scalar) {
                    long v = ((Scalar)obj).getUnsignedValue();
                    if (v == value) {
                        return true;
                    }
                }
                if (obj instanceof Address) {
                    long v = ((Address)obj).getOffset();
                    if (v == value) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private void writeHits(List<Hit> hits) {
        out.println("## Ranked Decompiled Hits");
        out.println();
        int count = Math.min(40, hits.size());
        for (int i = 0; i < count; i++) {
            Hit h = hits.get(i);
            out.printf("### `%s` @ `%s` score `%d`%n%n",
                h.fn.getName(), h.fn.getEntryPoint(), h.score);
            out.println("- reasons: " + String.join(", ", h.reasons));
            out.println();
            out.println("```c");
            String[] lines = h.c.split("\\n");
            int max = Math.min(lines.length, 160);
            for (int j = 0; j < max; j++) {
                out.println(lines[j]);
            }
            if (lines.length > max) {
                out.println("/* ... truncated ... */");
            }
            out.println("```");
            out.println();
        }
        if (count == 0) {
            out.println("No decompiled functions crossed the score threshold.");
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

    private void addIf(Hit h, boolean condition, int points, String reason) {
        if (condition) {
            h.score += points;
            h.reasons.add(reason);
        }
    }
}
