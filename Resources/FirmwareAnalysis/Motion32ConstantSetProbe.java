// Ghidra headless script: find functions/data windows containing known Motion MIDI map value sets.
// Usage:
//   -postScript Motion32ConstantSetProbe.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.mem.MemoryBlock;
import ghidra.program.model.scalar.Scalar;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Motion32ConstantSetProbe extends GhidraScript {
    private static class SetSpec {
        String name;
        int[] values;

        SetSpec(String name, int... values) {
            this.name = name;
            this.values = values;
        }
    }

    private static final SetSpec[] SETS = {
        new SetSpec("native transport tap/rec/play/stop", 0x69, 0x6b, 0x6d, 0x6f),
        new SetSpec("pre-native transport symptom", 0x66, 0x67, 0x68, 0x69),
        new SetSpec("native nav", 0x57, 0x59, 0x5a, 0x66),
        new SetSpec("native pad endpoints", 0x24, 0x43),
        new SetSpec("native pad lane starts", 0x24, 0x34),
        new SetSpec("standalone pad endpoints", 0x50, 0x6f),
        new SetSpec("encoder plus wheel", 0x0e, 0x15, 0x1d),
        new SetSpec("noteoff ch16 decoded", 0x80, 0x0f, 0x7f),
        new SetSpec("midi status classes", 0x80, 0x90, 0xb0, 0xf0),
        new SetSpec("fender global settings sysex", 0xf0, 0x08, 0x26, 0x22, 0xf7)
    };

    private PrintWriter out;
    private DecompInterface decompiler;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/constant_set_probe.md";
        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 Constant Set Probe");
        out.println();
        writeFunctionSets();
        writeDataWindows();

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private void writeFunctionSets() throws Exception {
        out.println("## Function Constant Sets");
        out.println();

        Map<Function, Set<Integer>> functionConstants = new HashMap<Function, Set<Integer>>();
        for (Instruction inst : currentProgram.getListing().getInstructions(true)) {
            Function fn = getFunctionContaining(inst.getAddress());
            if (fn == null) {
                continue;
            }
            for (int opIndex = 0; opIndex < inst.getNumOperands(); opIndex++) {
                for (Object obj : inst.getOpObjects(opIndex)) {
                    if (obj instanceof Scalar) {
                        long value = ((Scalar)obj).getValue();
                        if (0 <= value && value <= 0xff) {
                            functionConstants
                                .computeIfAbsent(fn, key -> new HashSet<Integer>())
                                .add((int)value);
                        }
                    }
                }
            }
        }

        for (SetSpec spec : SETS) {
            out.printf("### `%s`%n%n", spec.name);
            List<Function> matches = new ArrayList<Function>();
            for (Map.Entry<Function, Set<Integer>> entry : functionConstants.entrySet()) {
                if (containsAll(entry.getValue(), spec.values)) {
                    matches.add(entry.getKey());
                }
            }
            matches.sort((a, b) -> a.getEntryPoint().compareTo(b.getEntryPoint()));
            if (matches.isEmpty()) {
                out.println("- no function matches");
                out.println();
                continue;
            }
            int count = 0;
            for (Function fn : matches) {
                if (count++ >= 20) {
                    out.println("- truncated after 20 matches");
                    break;
                }
                out.printf("- `%s` @ `%s`%n", fn.getName(), fn.getEntryPoint());
                dumpDecompile(fn, 80);
            }
            out.println();
        }
    }

    private boolean containsAll(Set<Integer> values, int[] required) {
        for (int value : required) {
            if (!values.contains(value)) {
                return false;
            }
        }
        return true;
    }

    private void writeDataWindows() throws Exception {
        out.println("## Data Proximity Windows");
        out.println();
        for (SetSpec spec : SETS) {
            out.printf("### `%s`%n%n", spec.name);
            int hits = 0;
            for (MemoryBlock block : currentProgram.getMemory().getBlocks()) {
                if (!block.isInitialized() || block.isExecute()) {
                    continue;
                }
                long size = block.getSize();
                if (size <= 0 || size > Integer.MAX_VALUE) {
                    continue;
                }
                byte[] bytes = new byte[(int)size];
                block.getBytes(block.getStart(), bytes);
                for (int offset = 0; offset < bytes.length; offset += 4) {
                    if (windowContains(bytes, offset, 96, spec.values)) {
                        Address addr = block.getStart().add(offset);
                        out.printf("- window at `%s`%n", addr);
                        writeBytes(bytes, offset, 96);
                        hits++;
                        if (hits >= 20) {
                            out.println("- truncated after 20 windows");
                            break;
                        }
                    }
                }
                if (hits >= 20) {
                    break;
                }
            }
            if (hits == 0) {
                out.println("- no non-executable data windows");
            }
            out.println();
        }
    }

    private boolean windowContains(byte[] bytes, int offset, int length, int[] required) {
        Set<Integer> found = new HashSet<Integer>();
        int end = Math.min(bytes.length, offset + length);
        for (int i = offset; i < end; i++) {
            found.add(bytes[i] & 0xff);
        }
        for (int value : required) {
            if (!found.contains(value)) {
                return false;
            }
        }
        return true;
    }

    private void writeBytes(byte[] bytes, int offset, int length) {
        out.print("  - bytes:");
        int end = Math.min(bytes.length, offset + length);
        for (int i = offset; i < end; i++) {
            out.printf(" %02x", bytes[i] & 0xff);
        }
        out.println();
    }

    private void dumpDecompile(Function fn, int maxLines) throws Exception {
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
