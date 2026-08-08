// Ghidra headless script: trace the Motion 32 internal control-event encoder.
// Usage:
//   -postScript Motion32EventEncoderTraceProbe.java <output.md>

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
import java.util.List;

public class Motion32EventEncoderTraceProbe extends GhidraScript {
    private static final long[] TARGETS = {
        0x1d6cl, 0x1eecl, 0x1fb0l, 0x20a4l, 0x240cl
    };

    private static final long[] RAM_TARGETS = {
        0x20004081l, 0x20004084l
    };

    private PrintWriter out;
    private DecompInterface decompiler;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/event_encoder_trace_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 Event Encoder Trace Probe");
        out.println();
        writeTargetCallers();
        writeRamReferences();

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private void writeTargetCallers() throws Exception {
        out.println("## Function Callers");
        out.println();
        for (long raw : TARGETS) {
            Address target = toAddr(raw);
            Function targetFn = getFunctionAt(target);
            out.printf("### `%s` `%s`%n%n",
                target, targetFn == null ? "" : targetFn.getName());

            List<Function> callers = uniqueCallers(target);
            for (Function caller : callers) {
                out.printf("- `%s` @ `%s`%n", caller.getName(), caller.getEntryPoint());
            }
            if (callers.isEmpty()) {
                out.println("- no direct function callers found");
            }
            out.println();

            for (Function caller : callers) {
                out.printf("#### Caller `%s` @ `%s`%n%n", caller.getName(), caller.getEntryPoint());
                dumpInstructionsAroundCalls(caller, target, 8);
                dumpDecompile(caller, 180);
            }
        }
    }

    private List<Function> uniqueCallers(Address target) {
        List<Function> callers = new ArrayList<Function>();
        for (Reference ref : getReferencesTo(target)) {
            Function caller = getFunctionContaining(ref.getFromAddress());
            if (caller != null && !callers.contains(caller)) {
                callers.add(caller);
            }
        }
        return callers;
    }

    private void writeRamReferences() throws Exception {
        out.println("## RAM Address References");
        out.println();
        for (long raw : RAM_TARGETS) {
            Address target = toAddr(raw);
            out.printf("### `%s`%n%n", target);
            int count = 0;
            for (Reference ref : getReferencesTo(target)) {
                count++;
                Function caller = getFunctionContaining(ref.getFromAddress());
                out.printf("- from `%s` in `%s` @ `%s` type=%s%n",
                    ref.getFromAddress(),
                    caller == null ? "<none>" : caller.getName(),
                    caller == null ? "<none>" : caller.getEntryPoint().toString(),
                    ref.getReferenceType());
            }
            if (count == 0) {
                out.println("- no direct references found");
            }
            out.println();
        }
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
