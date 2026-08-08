// Ghidra headless script: trace callers and config-key uses around native-mode candidates.
// Usage:
//   -postScript Motion32FunctionTraceProbe.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.symbol.Reference;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Motion32FunctionTraceProbe extends GhidraScript {
    private static final long[] TARGETS = {
        0x2164cl, 0x21f24l, 0x22b70l, 0x2ea70l,
        0x2ec30l, 0x2ec74l, 0x2ecb8l, 0x2ece0l,
        0x2edc4l, 0x2754cl
    };

    private static final long[] DECOMPILE_CALLERS_OF = {
        0x2164cl, 0x21f24l, 0x22b70l
    };

    private PrintWriter out;
    private DecompInterface decompiler;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/function_trace_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 Function Trace Probe");
        out.println();
        writeTargetCallers();
        writeConfigGetterUses();

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private void writeTargetCallers() throws Exception {
        out.println("## Target Callers");
        out.println();
        for (long raw : TARGETS) {
            Address target = toAddr(raw);
            Function targetFn = getFunctionAt(target);
            out.printf("### `%s` `%s`%n%n",
                target, targetFn == null ? "" : targetFn.getName());

            List<Function> callers = new ArrayList<Function>();
            for (Reference ref : getReferencesTo(target)) {
                Function caller = getFunctionContaining(ref.getFromAddress());
                out.printf("- from `%s` in `%s` @ `%s` type=%s%n",
                    ref.getFromAddress(),
                    caller == null ? "<none>" : caller.getName(),
                    caller == null ? "<none>" : caller.getEntryPoint().toString(),
                    ref.getReferenceType());
                if (caller != null && !callers.contains(caller)) {
                    callers.add(caller);
                }
            }
            out.println();

            if (shouldDecompileCallers(raw)) {
                for (Function caller : callers) {
                    out.printf("#### Caller `%s` @ `%s`%n%n",
                        caller.getName(), caller.getEntryPoint());
                    dumpInstructionsAroundCalls(caller, target, 6);
                    dumpDecompile(caller, 180);
                }
            }
        }
    }

    private boolean shouldDecompileCallers(long raw) {
        for (long target : DECOMPILE_CALLERS_OF) {
            if (target == raw) {
                return true;
            }
        }
        return false;
    }

    private void writeConfigGetterUses() {
        out.println("## `FUN_0002ec30` Immediate-Key Uses");
        out.println();
        Address getter = toAddr(0x2ec30);
        for (Reference ref : getReferencesTo(getter)) {
            Function caller = getFunctionContaining(ref.getFromAddress());
            Instruction call = getInstructionAt(ref.getFromAddress());
            Long key = previousR0Immediate(call, 8);
            out.printf("- key `%s` from `%s` in `%s` @ `%s`%n",
                key == null ? "?" : String.format("0x%02x", key),
                ref.getFromAddress(),
                caller == null ? "<none>" : caller.getName(),
                caller == null ? "<none>" : caller.getEntryPoint().toString());
        }
        out.println();
    }

    private Long previousR0Immediate(Instruction call, int maxBack) {
        if (call == null) {
            return null;
        }
        Instruction cur = call;
        for (int i = 0; i < maxBack; i++) {
            cur = currentProgram.getListing().getInstructionBefore(cur.getAddress());
            if (cur == null) {
                return null;
            }
            String text = cur.toString();
            if (text.startsWith("movs r0,#0x")) {
                String hex = text.substring("movs r0,#0x".length()).trim();
                try {
                    return Long.parseLong(hex, 16);
                }
                catch (NumberFormatException ignored) {
                    return null;
                }
            }
        }
        return null;
    }

    private void dumpInstructionsAroundCalls(Function caller, Address target, int radius) {
        for (Reference ref : getReferencesTo(target)) {
            if (!caller.getBody().contains(ref.getFromAddress())) {
                continue;
            }
            out.printf("Call site `%s`:%n%n", ref.getFromAddress());
            out.println("```asm");
            Instruction cur = getInstructionAt(ref.getFromAddress());
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
    }

    private void dumpDecompile(Function fn, int maxLines) throws Exception {
        DecompileResults results = decompiler.decompileFunction(fn, 30, monitor);
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
