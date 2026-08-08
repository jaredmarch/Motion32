// Ghidra headless script for finding likely MIDI receive/parser functions.
// Usage:
//   -postScript Motion32MidiReceiveProbe.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.scalar.Scalar;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Motion32MidiReceiveProbe extends GhidraScript {
    private PrintWriter out;
    private DecompInterface decompiler;

    private static final long[] MIDI_CONSTANTS = {
        0x00, 0x01, 0x06, 0x08, 0x09, 0x0b, 0x0f,
        0x10, 0x11, 0x20, 0x21, 0x22, 0x26, 0x7e, 0x7f,
        0x80, 0x8f, 0x90, 0x9f, 0xa0, 0xb0, 0xbf, 0xc0, 0xd0,
        0xe0, 0xf0, 0xf7, 0xff
    };

    private static final Set<Long> MIDI_SET = new HashSet<Long>();
    static {
        for (long value : MIDI_CONSTANTS) {
            MIDI_SET.add(value);
        }
    }

    private static class Score {
        Function function;
        Set<Long> constants = new HashSet<Long>();
        int hits = 0;
        boolean hasStatus = false;
        boolean hasMask = false;
        boolean hasVelocity = false;
        boolean hasFender = false;
        boolean hasUniversal = false;
    }

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/midi_receive_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 MIDI Receive Probe");
        out.println();
        out.println("- Program: `" + currentProgram.getName() + "`");
        out.println("- Language: `" + currentProgram.getLanguageID() + "`");
        out.println();

        Map<Function, Score> scores = collectScores();
        writeRanked(scores);
        writeFocused(scores);

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private Map<Function, Score> collectScores() {
        Map<Function, Score> scores = new LinkedHashMap<Function, Score>();
        for (Instruction inst : currentProgram.getListing().getInstructions(true)) {
            Function fn = getFunctionContaining(inst.getAddress());
            if (fn == null) {
                continue;
            }
            for (int opIndex = 0; opIndex < inst.getNumOperands(); opIndex++) {
                for (Object obj : inst.getOpObjects(opIndex)) {
                    if (!(obj instanceof Scalar)) {
                        continue;
                    }
                    long value = ((Scalar)obj).getValue();
                    if (!MIDI_SET.contains(value)) {
                        continue;
                    }
                    Score score = scores.computeIfAbsent(fn, k -> {
                        Score s = new Score();
                        s.function = k;
                        return s;
                    });
                    score.constants.add(value);
                    score.hits++;
                }
            }
        }

        for (Score score : scores.values()) {
            score.hasStatus = hasAny(score, 0x80, 0x90, 0xb0, 0xe0, 0xf0);
            score.hasMask = hasAny(score, 0x0f, 0xf0, 0x7f, 0xff);
            score.hasVelocity = hasAny(score, 0x7f, 0x00);
            score.hasFender = hasAll(score, 0x08, 0x26) || hasAny(score, 0x20, 0x21, 0x22);
            score.hasUniversal = hasAll(score, 0x7e, 0x06);
        }
        return scores;
    }

    private boolean hasAny(Score score, long... values) {
        for (long value : values) {
            if (score.constants.contains(value)) {
                return true;
            }
        }
        return false;
    }

    private boolean hasAll(Score score, long... values) {
        for (long value : values) {
            if (!score.constants.contains(value)) {
                return false;
            }
        }
        return true;
    }

    private int rank(Score score) {
        int rank = score.constants.size() * 10 + score.hits;
        if (score.hasStatus) {
            rank += 60;
        }
        if (score.hasMask) {
            rank += 35;
        }
        if (score.hasVelocity) {
            rank += 20;
        }
        if (score.hasFender) {
            rank += 25;
        }
        if (score.hasUniversal) {
            rank += 25;
        }
        if (score.constants.contains(0x80L) && score.constants.contains(0x0fL) &&
            score.constants.contains(0x7fL)) {
            rank += 120;
        }
        if (score.constants.contains(0x80L) && score.constants.contains(0xf0L)) {
            rank += 70;
        }
        return rank;
    }

    private void writeRanked(Map<Function, Score> scores) {
        List<Score> ranked = new ArrayList<Score>(scores.values());
        ranked.sort((a, b) -> Integer.compare(rank(b), rank(a)));

        out.println("## Ranked Candidate Functions");
        out.println();
        int count = 0;
        for (Score score : ranked) {
            if (count >= 80) {
                break;
            }
            if (!score.hasStatus && !score.hasFender && !score.hasUniversal) {
                continue;
            }
            out.printf("- rank `%d` `%s` @ `%s` hits=%d constants=",
                rank(score), score.function.getName(), score.function.getEntryPoint(), score.hits);
            writeConstantsInline(score);
            out.println();
            count++;
        }
        out.println();
    }

    private void writeFocused(Map<Function, Score> scores) throws Exception {
        List<Score> ranked = new ArrayList<Score>(scores.values());
        ranked.sort((a, b) -> Integer.compare(rank(b), rank(a)));

        out.println("## Decompiled Top Candidates");
        out.println();
        int count = 0;
        for (Score score : ranked) {
            if (count >= 20) {
                break;
            }
            if (!(score.hasStatus && score.hasMask)) {
                continue;
            }
            out.printf("### `%s` @ `%s` rank `%d`%n%n",
                score.function.getName(), score.function.getEntryPoint(), rank(score));
            out.print("- constants=");
            writeConstantsInline(score);
            out.println();
            writeDecompile(score.function, 180);
            count++;
        }
        out.println();
    }

    private void writeConstantsInline(Score score) {
        List<Long> constants = new ArrayList<Long>(score.constants);
        constants.sort(Long::compareTo);
        for (long value : constants) {
            out.printf(" `0x%02x`", value);
        }
    }

    private void writeDecompile(Function fn, int maxLines) throws Exception {
        DecompileResults results = decompiler.decompileFunction(fn, 30, monitor);
        out.println();
        out.println("```c");
        if (!results.decompileCompleted()) {
            out.println("/* decompile failed */");
        }
        else {
            String[] lines = results.getDecompiledFunction().getC().split("\\n");
            for (int i = 0; i < lines.length && i < maxLines; i++) {
                out.println(lines[i]);
            }
            if (lines.length > maxLines) {
                out.println("/* ... truncated ... */");
            }
        }
        out.println("```");
        out.println();
    }
}
