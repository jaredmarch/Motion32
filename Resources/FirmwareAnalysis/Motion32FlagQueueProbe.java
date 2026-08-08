// Ghidra headless script: dump queue/flag helpers and references around host event flags.
// Usage:
//   -postScript Motion32FlagQueueProbe.java <output.md>

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

public class Motion32FlagQueueProbe extends GhidraScript {
    private static final long[] FUNCTIONS = {
        0x03f54L, 0x03f88L, 0x03f98L, 0x03fa8L, 0x03fb8L, 0x03fc8L,
        0x03fd8L, 0x03fecL, 0x04000L, 0x04014L, 0x04028L, 0x04034L,
        0x04048L, 0x0408cL, 0x041fcL, 0x0455cL, 0x045b0L, 0x045c0L
    };

    private static final long[] RAM_TARGETS = {
        0x20005cafL, 0x20005cb0L, 0x20005cb1L, 0x20005cb2L, 0x20005cb3L,
        0x20006465L, 0x20006466L, 0x200064bcL, 0x200064bdL,
        0x200064d4L, 0x200064d6L, 0x200064d8L, 0x200064dcL,
        0x200040f8L, 0x200040fcL
    };

    private PrintWriter out;
    private DecompInterface decompiler;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/flag_queue_probe.md";
        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 Flag/Queue Probe");
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
            out.printf("### `%s` `%s`%n%n", addr, fn == null ? "<none>" : fn.getName());
            if (fn != null) {
                dumpDecompile(fn, 180);
                writeCallers(addr);
            }
            else {
                dumpInstructions(addr, 10);
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
                out.printf("#### `%s` @ `%s`%n%n", fn.getName(), fn.getEntryPoint());
                dumpInstructionsNearRefs(fn, target, 8);
                dumpDecompile(fn, 140);
            }
        }
    }

    private void writeCallers(Address target) {
        out.println("Callers:");
        int count = 0;
        for (Reference ref : getReferencesTo(target)) {
            Function fn = getFunctionContaining(ref.getFromAddress());
            if (fn != null) {
                count++;
                out.printf("- `%s` @ `%s` from `%s` type=%s%n",
                    fn.getName(), fn.getEntryPoint(), ref.getFromAddress(), ref.getReferenceType());
            }
        }
        if (count == 0) {
            out.println("- none");
        }
        out.println();
    }

    private void dumpInstructionsNearRefs(Function fn, Address target, int radius) {
        for (Reference ref : getReferencesTo(target)) {
            if (!fn.getBody().contains(ref.getFromAddress())) {
                continue;
            }
            out.printf("Site `%s`:%n%n", ref.getFromAddress());
            dumpInstructions(ref.getFromAddress(), radius);
        }
    }

    private void dumpInstructions(Address address, int radius) {
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
