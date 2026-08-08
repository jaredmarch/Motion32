// Ghidra headless script: trace the small mode/state RAM area used by the event encoder.
// Usage:
//   -postScript Motion32ModeStateTraceProbe.java <output.md>

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

public class Motion32ModeStateTraceProbe extends GhidraScript {
    private static final long[] RAM_TARGETS = {
        0x20004291l, 0x20004294l, 0x200045ccl,
        0x20004538l, 0x2000453cl, 0x200064c0l,
        0x200064d4l, 0x200064d8l
    };

    private PrintWriter out;
    private DecompInterface decompiler;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/mode_state_trace_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 Mode/State Trace Probe");
        out.println();
        for (long raw : RAM_TARGETS) {
            writeRefs(raw);
        }

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private void writeRefs(long raw) throws Exception {
        Address target = toAddr(raw);
        out.printf("## `%s`%n%n", target);

        List<Function> funcs = new ArrayList<Function>();
        int count = 0;
        for (Reference ref : getReferencesTo(target)) {
            count++;
            Function fn = getFunctionContaining(ref.getFromAddress());
            out.printf("- from `%s` in `%s` @ `%s` type=%s%n",
                ref.getFromAddress(),
                fn == null ? "<none>" : fn.getName(),
                fn == null ? "<none>" : fn.getEntryPoint().toString(),
                ref.getReferenceType());
            if (fn != null && !funcs.contains(fn)) {
                funcs.add(fn);
            }
        }
        if (count == 0) {
            out.println("- no direct references found");
        }
        out.println();

        for (Function fn : funcs) {
            out.printf("### Function `%s` @ `%s`%n%n", fn.getName(), fn.getEntryPoint());
            dumpInstructionsNearRefs(fn, target, 8);
            dumpDecompile(fn, 160);
        }
    }

    private void dumpInstructionsNearRefs(Function fn, Address target, int radius) {
        for (Reference ref : getReferencesTo(target)) {
            if (!fn.getBody().contains(ref.getFromAddress())) {
                continue;
            }
            out.printf("Reference site `%s`:%n%n", ref.getFromAddress());
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
