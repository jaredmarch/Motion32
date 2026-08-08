// Ghidra headless script: rank decompiled functions by MIDI packet/buffer shape.
// Usage:
//   -postScript Motion32MidiPacketShapeProbe.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Motion32MidiPacketShapeProbe extends GhidraScript {
    private static class Hit {
        Function fn;
        String c;
        int score;
        List<String> reasons = new ArrayList<String>();
    }

    private PrintWriter out;
    private DecompInterface decompiler;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/midi_packet_shape_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        List<Hit> hits = new ArrayList<Hit>();
        for (Function fn : currentProgram.getFunctionManager().getFunctions(true)) {
            if (monitor.isCancelled()) {
                break;
            }
            DecompileResults results = decompiler.decompileFunction(fn, 20, monitor);
            if (!results.decompileCompleted()) {
                continue;
            }
            String c = results.getDecompiledFunction().getC();
            Hit hit = score(fn, c);
            if (hit.score >= 25) {
                hits.add(hit);
            }
        }

        hits.sort((a, b) -> Integer.compare(b.score, a.score));

        out.println("# Motion 32 MIDI Packet Shape Probe");
        out.println();
        int count = 0;
        for (Hit hit : hits) {
            if (count++ >= 60) {
                break;
            }
            out.printf("## `%s` @ `%s` score `%d`%n%n",
                hit.fn.getName(), hit.fn.getEntryPoint(), hit.score);
            out.print("- reasons:");
            for (String reason : hit.reasons) {
                out.print(" `" + reason + "`");
            }
            out.println();
            out.println();
            writeSnippet(hit.c, 180);
        }

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private Hit score(Function fn, String c) {
        Hit hit = new Hit();
        hit.fn = fn;
        hit.c = c;

        addIf(hit, c.contains("byte *param_"), 8, "byte* param");
        addIf(hit, c.contains("undefined1 *param_"), 5, "u8* param");
        addIf(hit, c.contains("*(byte *)"), 4, "byte deref");
        addIf(hit, c.contains("*(undefined1 *)"), 3, "u8 deref");

        addIf(hit, containsAny(c, "+ 1)", "+ 1]"), 6, "offset +1");
        addIf(hit, containsAny(c, "+ 2)", "+ 2]"), 6, "offset +2");
        addIf(hit, containsAny(c, "+ 3)", "+ 3]"), 6, "offset +3");
        addIf(hit, containsAny(c, "[1]", "[2]", "[3]"), 8, "small indexes");

        addIf(hit, containsAny(c, "& 0xf0", "& 0xfffffff0", "& 0xffffff0f"), 18, "status nibble mask");
        addIf(hit, containsAny(c, "& 0xf", "& 0x0f", "& 0xffffff0f"), 12, "channel nibble mask");
        addIf(hit, containsAny(c, "& 0x7f", "& 0x7fU"), 12, "7-bit mask");
        addIf(hit, containsAny(c, "== 0x80", "0x80)", "0x80,"), 12, "0x80");
        addIf(hit, containsAny(c, "== 0x90", "0x90)", "0x90,"), 10, "0x90");
        addIf(hit, containsAny(c, "== 0xb0", "0xb0)", "0xb0,"), 10, "0xb0");
        addIf(hit, containsAny(c, "== 0xf0", "0xf0)", "0xf0,"), 8, "0xf0");
        addIf(hit, containsAny(c, "0x8f", "0x8f0"), 12, "0x8f-ish");
        addIf(hit, containsAny(c, "0x7f", "127"), 6, "127");
        addIf(hit, c.contains("0x2b") && c.contains("0x1a"), 8, "record map shape");

        addIf(hit, containsAny(c, "FUN_0002754c", "0x0002754c"), 20, "midi send call");
        addIf(hit, containsAny(c, "F7", "0xf7"), 5, "sysex end");

        return hit;
    }

    private void addIf(Hit hit, boolean condition, int score, String reason) {
        if (condition) {
            hit.score += score;
            hit.reasons.add(reason);
        }
    }

    private boolean containsAny(String text, String... needles) {
        for (String needle : needles) {
            if (text.contains(needle)) {
                return true;
            }
        }
        return false;
    }

    private void writeSnippet(String c, int maxLines) {
        out.println("```c");
        String[] lines = c.split("\\n");
        for (int i = 0; i < lines.length && i < maxLines; i++) {
            out.println(lines[i]);
        }
        if (lines.length > maxLines) {
            out.println("/* ... truncated ... */");
        }
        out.println("```");
        out.println();
    }
}
