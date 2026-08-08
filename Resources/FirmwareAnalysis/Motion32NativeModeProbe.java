// Ghidra headless script for probing Motion 32 native-mode-ish handlers.
// Usage:
//   -postScript Motion32NativeModeProbe.java <output.md>

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
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Motion32NativeModeProbe extends GhidraScript {
    private PrintWriter out;
    private DecompInterface decompiler;

    private static final long[] BYTE_PATTERN_HITS = {
        0x0890dcl, 0x0a26f1l, 0x0a88f8l
    };

    private static final long[] INTERESTING_CONSTANTS = {
        0x08, 0x20, 0x21, 0x22, 0x24, 0x26, 0x7e, 0x7f, 0x8f, 0xf0, 0xf7
    };

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/native_mode_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        DecompileOptions options = new DecompileOptions();
        decompiler.setOptions(options);
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 Native Mode Firmware Probe");
        out.println();
        out.println("- Program: `" + currentProgram.getName() + "`");
        out.println("- Language: `" + currentProgram.getLanguageID() + "`");
        out.println();

        writePatternHitOwners();
        writeConstantFunctionIndex();
        writeTargetFunctions();
        writeTopMultiConstantFunctions();

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private void writePatternHitOwners() throws Exception {
        out.println("## Raw `8f 00 00` Pattern Hits");
        out.println();
        for (long offset : BYTE_PATTERN_HITS) {
            Address addr = toAddr(offset);
            Function fn = getFunctionContaining(addr);
            out.printf("- `%s`", addr);
            if (fn == null) {
                out.println(" — no containing function");
                continue;
            }
            out.printf(" — `%s` @ `%s`%n", fn.getName(), fn.getEntryPoint());
            writeInstructionsAround(addr, 8);
            writeDecompile(fn, 60);
        }
        out.println();
    }

    private void writeConstantFunctionIndex() {
        Map<Long, Set<Function>> byConstant = new LinkedHashMap<>();
        for (long value : INTERESTING_CONSTANTS) {
            byConstant.put(value, new LinkedHashSet<Function>());
        }

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
                    if (byConstant.containsKey(value)) {
                        byConstant.get(value).add(fn);
                    }
                }
            }
        }

        out.println("## Functions Using Interesting Constants");
        out.println();
        for (long value : INTERESTING_CONSTANTS) {
            Set<Function> functions = byConstant.get(value);
            out.printf("- `0x%02x`: %d functions", value, functions.size());
            int count = 0;
            for (Function fn : functions) {
                if (count == 0) {
                    out.println();
                }
                if (count >= 20) {
                    out.println("  - ...");
                    break;
                }
                out.printf("  - `%s` @ `%s`%n", fn.getName(), fn.getEntryPoint());
                count++;
            }
            if (functions.isEmpty()) {
                out.println();
            }
        }
        out.println();
    }

    private void writeTargetFunctions() throws Exception {
        long[] entries = {0x2164cl, 0x3bb58l, 0x3e600l};
        out.println("## Targeted `0x8f` Constant Functions");
        out.println();
        for (long entry : entries) {
            Function fn = getFunctionAt(toAddr(entry));
            if (fn == null) {
                fn = getFunctionContaining(toAddr(entry));
            }
            if (fn == null) {
                out.printf("- `%s` — no function%n", toAddr(entry));
                continue;
            }
            out.printf("### `%s` @ `%s`%n", fn.getName(), fn.getEntryPoint());
            writeInstructionsAround(fn.getEntryPoint(), 6);
            writeDecompile(fn, 160);
        }
        out.println();
    }

    private void writeTopMultiConstantFunctions() throws Exception {
        Map<Function, Set<Long>> constantsByFunction = new LinkedHashMap<>();
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
                    for (long interesting : INTERESTING_CONSTANTS) {
                        if (value == interesting) {
                            constantsByFunction.computeIfAbsent(fn, k -> new LinkedHashSet<Long>()).add(value);
                        }
                    }
                }
            }
        }

        List<Map.Entry<Function, Set<Long>>> entries = new ArrayList<>(constantsByFunction.entrySet());
        entries.sort((a, b) -> Integer.compare(b.getValue().size(), a.getValue().size()));

        out.println("## Highest-Signal Multi-Constant Functions");
        out.println();
        int written = 0;
        for (Map.Entry<Function, Set<Long>> entry : entries) {
            if (entry.getValue().size() < 4) {
                continue;
            }
            Function fn = entry.getKey();
            out.printf("### `%s` @ `%s`%n%n", fn.getName(), fn.getEntryPoint());
            out.print("- constants:");
            for (long value : entry.getValue()) {
                out.printf(" `0x%02x`", value);
            }
            out.println();
            writeDecompile(fn, 90);
            written++;
            if (written >= 12) {
                break;
            }
        }
        out.println();
    }

    private void writeInstructionsAround(Address addr, int radius) {
        out.println();
        out.println("```asm");
        Instruction inst = currentProgram.getListing().getInstructionAt(addr);
        if (inst == null) {
            inst = currentProgram.getListing().getInstructionBefore(addr);
        }
        if (inst == null) {
            out.println("; no instruction nearby");
            out.println("```");
            return;
        }
        Instruction start = inst;
        for (int i = 0; i < radius; i++) {
            Instruction prev = currentProgram.getListing().getInstructionBefore(start.getAddress());
            if (prev == null) {
                break;
            }
            start = prev;
        }
        Instruction cur = start;
        for (int i = 0; i < radius * 2 + 1 && cur != null; i++) {
            out.printf("%s: %s%n", cur.getAddress(), cur);
            cur = currentProgram.getListing().getInstructionAfter(cur.getAddress());
        }
        out.println("```");
        out.println();
    }

    private void writeDecompile(Function fn, int maxLines) throws Exception {
        DecompileResults results = decompiler.decompileFunction(fn, 30, monitor);
        if (!results.decompileCompleted()) {
            out.println();
            out.println("```c");
            out.println("/* decompile failed */");
            out.println("```");
            out.println();
            return;
        }
        String[] lines = results.getDecompiledFunction().getC().split("\\n");
        out.println();
        out.println("```c");
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
