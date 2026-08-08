// Ghidra headless script: trace the framed byte-stream parser callback/state.
// Usage:
//   -postScript Motion32ParserCallbackTraceProbe.java <output.md>

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

public class Motion32ParserCallbackTraceProbe extends GhidraScript {
    private static final long[] TARGETS = {
        0x1d54l, 0x1d6cl, 0x1d94l, 0x1dc0l,
        0x20a4l, 0x2098l, 0x2e6cl, 0x3ab8l, 0x3f88l
    };

    private static final long[] RAM_TARGETS = {
        0x20004290l, 0x20004291l, 0x20004292l, 0x20004294l,
        0x20004298l, 0x2000429cl, 0x200042a0l,
        0x20004320l, 0x20004321l
    };

    private PrintWriter out;
    private DecompInterface decompiler;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/parser_callback_trace_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 Parser/Callback Trace Probe");
        out.println();
        writeFunctionCallers();
        writeRamRefs();

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private void writeFunctionCallers() throws Exception {
        out.println("## Function Callers");
        out.println();
        for (long raw : TARGETS) {
            Address target = toAddr(raw);
            Function fn = getFunctionAt(target);
            if (fn == null) {
                fn = getFunctionContaining(target);
            }
            out.printf("### `%s` `%s`%n%n", target, fn == null ? "" : fn.getName());
            List<Function> callers = uniqueCallers(target);
            for (Function caller : callers) {
                out.printf("- `%s` @ `%s`%n", caller.getName(), caller.getEntryPoint());
            }
            if (callers.isEmpty()) {
                out.println("- no direct function callers found");
            }
            out.println();
            if (fn != null) {
                out.printf("#### Target `%s` @ `%s`%n%n", fn.getName(), fn.getEntryPoint());
                dumpDecompile(fn, 120);
            }
            for (Function caller : callers) {
                out.printf("#### Caller `%s` @ `%s`%n%n", caller.getName(), caller.getEntryPoint());
                dumpInstructionsAroundCalls(caller, target, 7);
                dumpDecompile(caller, 120);
            }
        }
    }

    private void writeRamRefs() throws Exception {
        out.println("## RAM References");
        out.println();
        for (long raw : RAM_TARGETS) {
            Address target = toAddr(raw);
            out.printf("### `%s`%n%n", target);
            List<Function> funcs = new ArrayList<Function>();
            int refs = 0;
            for (Reference ref : getReferencesTo(target)) {
                refs++;
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
            if (refs == 0) {
                out.println("- no direct references found");
            }
            out.println();
            for (Function fn : funcs) {
                out.printf("#### Function `%s` @ `%s`%n%n", fn.getName(), fn.getEntryPoint());
                dumpInstructionsNearRefs(fn, target, 7);
                dumpDecompile(fn, 100);
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

    private void dumpInstructionsAroundCalls(Function caller, Address target, int radius) {
        for (Reference ref : getReferencesTo(target)) {
            if (!caller.getBody().contains(ref.getFromAddress())) {
                continue;
            }
            dumpInstructions(ref.getFromAddress(), radius);
        }
    }

    private void dumpInstructionsNearRefs(Function fn, Address target, int radius) {
        for (Reference ref : getReferencesTo(target)) {
            if (!fn.getBody().contains(ref.getFromAddress())) {
                continue;
            }
            dumpInstructions(ref.getFromAddress(), radius);
        }
    }

    private void dumpInstructions(Address address, int radius) {
        out.printf("Site `%s`:%n%n", address);
        out.println("```asm");
        Instruction cur = getInstructionAt(address);
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
