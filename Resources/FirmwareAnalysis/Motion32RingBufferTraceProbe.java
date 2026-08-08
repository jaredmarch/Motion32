// Ghidra headless script: trace generic ring buffers around 0x20004080.
// Usage:
//   -postScript Motion32RingBufferTraceProbe.java <output.md>

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

public class Motion32RingBufferTraceProbe extends GhidraScript {
    private static final long[] FUNCTIONS = {
        0x17c0l, 0x17f8l, 0x1c8cl, 0x1cfcl, 0x1d28l,
        0x1d54l, 0x1d6cl, 0x1d94l, 0x1dc0l, 0x3ab8l,
        0x3a14l, 0x3ac4l, 0x3af0l, 0x3f54l, 0x3fec, 0x4034l, 0x4048l
    };

    private static final long[] RAM_TARGETS = {
        0x20004080l, 0x20004081l, 0x20004084l, 0x20004098l,
        0x200040a0l, 0x200040b4l, 0x20004290l, 0x20004320l
    };

    private PrintWriter out;
    private DecompInterface decompiler;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/ring_buffer_trace_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 Ring Buffer Trace Probe");
        out.println();
        writeFunctions();
        writeRamRefs();

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private void writeFunctions() throws Exception {
        out.println("## Functions");
        out.println();
        for (long raw : FUNCTIONS) {
            Address addr = toAddr(raw);
            Function fn = getFunctionAt(addr);
            if (fn == null) {
                fn = getFunctionContaining(addr);
            }
            if (fn == null) {
                disassemble(addr);
                try {
                    createFunction(addr, "PROBE_" + addr.toString());
                }
                catch (Exception ignored) {
                }
                fn = getFunctionAt(addr);
            }
            out.printf("### `%s` `%s`%n%n", addr, fn == null ? "" : fn.getName());
            if (fn != null) {
                dumpDecompile(fn, 150);
                writeCallers(addr);
            }
            else {
                dumpInstructions(addr, 12);
            }
        }
    }

    private void writeCallers(Address target) {
        List<Function> callers = new ArrayList<Function>();
        for (Reference ref : getReferencesTo(target)) {
            Function fn = getFunctionContaining(ref.getFromAddress());
            if (fn != null && !callers.contains(fn)) {
                callers.add(fn);
            }
        }
        out.println("Callers:");
        if (callers.isEmpty()) {
            out.println("- none");
        }
        for (Function fn : callers) {
            out.printf("- `%s` @ `%s`%n", fn.getName(), fn.getEntryPoint());
        }
        out.println();
    }

    private void writeRamRefs() throws Exception {
        out.println("## RAM References");
        out.println();
        for (long raw : RAM_TARGETS) {
            Address target = toAddr(raw);
            out.printf("### `%s`%n%n", target);
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
                out.printf("#### Function `%s` @ `%s`%n%n", fn.getName(), fn.getEntryPoint());
                dumpInstructionsNearRefs(fn, target, 6);
                dumpDecompile(fn, 100);
            }
        }
    }

    private void dumpInstructionsNearRefs(Function fn, Address target, int radius) {
        for (Reference ref : getReferencesTo(target)) {
            if (!fn.getBody().contains(ref.getFromAddress())) {
                continue;
            }
            out.printf("Site `%s`:%n%n", ref.getFromAddress());
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

    private void dumpInstructions(Address address, int radius) {
        out.printf("Site `%s`:%n%n", address);
        out.println("```asm");
        Instruction cur = getInstructionAt(address);
        if (cur == null) {
            cur = currentProgram.getListing().getInstructionAfter(address);
        }
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
