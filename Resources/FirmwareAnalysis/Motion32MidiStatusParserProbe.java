// Ghidra headless script: search for likely true MIDI status-byte parsers.
// Usage:
//   -postScript Motion32MidiStatusParserProbe.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Motion32MidiStatusParserProbe extends GhidraScript {
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
            : "Resources/FirmwareAnalysis/midi_status_parser_probe.md";

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

        out.println("# Motion 32 MIDI Status Parser Probe");
        out.println();
        out.println("Search is intentionally biased toward real three-byte MIDI handling:");
        out.println("status nibble/channel tests plus separate data-byte references.");
        out.println();

        int count = Math.min(50, hits.size());
        for (int i = 0; i < count; i++) {
            Hit h = hits.get(i);
            out.printf("## `%s` @ `%s` score `%d`%n%n",
                h.fn.getName(), h.fn.getEntryPoint(), h.score);
            out.println("- reasons: " + String.join(", ", h.reasons));
            out.println();
            out.println("```c");
            String[] lines = h.c.split("\\n");
            int max = Math.min(180, lines.length);
            for (int j = 0; j < max; j++) {
                out.println(lines[j]);
            }
            if (lines.length > max) {
                out.println("/* ... truncated ... */");
            }
            out.println("```");
            out.println();
        }

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private List<Hit> scanFunctions() throws Exception {
        List<Hit> hits = new ArrayList<Hit>();
        FunctionIterator it = currentProgram.getFunctionManager().getFunctions(true);
        while (it.hasNext()) {
            Function fn = it.next();
            DecompileResults results = decompiler.decompileFunction(fn, 15, monitor);
            if (!results.decompileCompleted()) {
                continue;
            }
            String c = results.getDecompiledFunction().getC();
            Hit h = score(fn, c);
            if (h.score >= 22) {
                hits.add(h);
            }
        }
        return hits;
    }

    private Hit score(Function fn, String c) {
        Hit h = new Hit();
        h.fn = fn;
        h.c = c;

        addIf(h, c.contains("0x8f"), 18, "exact 0x8f");
        addIf(h, c.contains("0x80"), 6, "0x80");
        addIf(h, c.contains("0x90"), 6, "0x90");
        addIf(h, c.contains("0xb0"), 8, "0xb0");
        addIf(h, c.contains("0xf0"), 4, "0xf0");
        addIf(h, c.contains("0xf7"), 4, "0xf7");
        addIf(h, c.contains("0x7f"), 5, "0x7f");
        addIf(h, c.contains("0x78"), 3, "0x78");

        addIf(h, c.contains("& 0xf0") || c.contains("&0xf0"), 12, "status mask &0xf0");
        addIf(h, c.contains("& 0xf") || c.contains("&0xf"), 8, "channel nibble mask");
        addIf(h, c.contains(">> 4") || c.contains(">>4"), 6, "status shift >>4");
        addIf(h, c.contains("<< 4") || c.contains("<<4"), 3, "nibble compose <<4");

        addIf(h, c.contains("[1]") || c.contains("+ 1)"), 4, "data byte 1");
        addIf(h, c.contains("[2]") || c.contains("+ 2)"), 4, "data byte 2");
        addIf(h, c.contains("[3]") || c.contains("+ 3)"), 2, "byte 3");
        addIf(h, c.contains("param_1") && c.contains("param_2"), 3, "multi-param handler");

        addIf(h, c.contains("switch"), 3, "switch");
        addIf(h, c.contains("case"), 3, "case");
        addIf(h, c.contains("FUN_0002754c"), -20, "outgoing send false-lead");
        addIf(h, c.contains("0x8f0"), -12, "little-endian F0 08 false-lead");
        addIf(h, c.contains("UTF") || c.contains("0xc0") && c.contains("0xe0") && c.contains("0xf0"), -10, "utf8-like");

        return h;
    }

    private void addIf(Hit h, boolean condition, int points, String reason) {
        if (condition) {
            h.score += points;
            h.reasons.add(reason);
        }
    }
}
