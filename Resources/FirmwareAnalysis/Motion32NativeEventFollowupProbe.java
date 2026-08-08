// Ghidra headless script: focused native-mode event/USB follow-up.
// Usage:
//   -postScript Motion32NativeEventFollowupProbe.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.mem.Memory;
import ghidra.program.model.symbol.Reference;

import java.io.File;
import java.io.PrintWriter;

public class Motion32NativeEventFollowupProbe extends GhidraScript {
    private static final long[] FUNCTIONS = {
        0x00000e5cL, 0x00002a14L, 0x00002a60L, 0x00002ab8L, 0x00002ac4L, 0x00002af0L,
        0x00000d28L, 0x00000d54L, 0x00000d6cL, 0x00000dc0L,
        0x00000eecL, 0x00000f6cL, 0x00000fb0L, 0x00000ff4L, 0x00001030L,
        0x00001288L, 0x0000140cL, 0x000016f4L, 0x000017d4L,
        0x0000190cL, 0x00002120L, 0x0000308cL, 0x00008944L
    };

    private static final long[][] DATA_RANGES = {
        {0x000095f4L, 16},
        {0x000095fcL, 32},
        {0x00009664L, 32},
        {0x00002ac0L, 48},
        {0x000097e4L, 192},
        {0x00009874L, 64}
    };

    private PrintWriter out;
    private DecompInterface decompiler;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/native_event_followup_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 Native Event Follow-Up Probe");
        out.println();
        writeFunctions();
        writeDataRanges();

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private void writeFunctions() throws Exception {
        out.println("## Focus Functions");
        out.println();
        for (long raw : FUNCTIONS) {
            Address addr = toAddr(raw);
            Function fn = getFunctionAt(addr);
            if (fn == null) {
                fn = getFunctionContaining(addr);
            }
            out.printf("### `%s` `%s`%n%n", addr, fn == null ? "<none>" : fn.getName());
            writeReferencesTo(addr);
            dumpInstructions(addr, 18);
            if (fn != null) {
                dumpDecompile(fn, 180);
            }
        }
    }

    private void writeDataRanges() throws Exception {
        out.println("## Data Ranges");
        out.println();
        Memory mem = currentProgram.getMemory();
        for (long[] range : DATA_RANGES) {
            Address start = toAddr(range[0]);
            int len = (int) range[1];
            out.printf("### `%s` len `%d`%n%n", start, len);
            out.println("```");
            for (int row = 0; row < len; row += 16) {
                Address cur = start.add(row);
                out.printf("%s: ", cur);
                int rowLen = Math.min(16, len - row);
                for (int i = 0; i < rowLen; i++) {
                    out.printf("%02x ", mem.getByte(cur.add(i)) & 0xff);
                }
                out.print(" ");
                for (int i = 0; i < rowLen; i++) {
                    int b = mem.getByte(cur.add(i)) & 0xff;
                    out.print((b >= 0x20 && b <= 0x7e) ? (char)b : '.');
                }
                out.println();
            }
            out.println("```");
            out.println();
        }
    }

    private void writeReferencesTo(Address target) {
        out.println("References to this address:");
        int count = 0;
        for (Reference ref : getReferencesTo(target)) {
            Function fn = getFunctionContaining(ref.getFromAddress());
            out.printf("- from `%s` in `%s` @ `%s` type=%s%n",
                ref.getFromAddress(),
                fn == null ? "<none>" : fn.getName(),
                fn == null ? "<none>" : fn.getEntryPoint().toString(),
                ref.getReferenceType());
            count++;
        }
        if (count == 0) {
            out.println("- none");
        }
        out.println();
    }

    private void dumpInstructions(Address address, int radius) {
        out.printf("Instructions near `%s`:%n%n", address);
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
        if (!results.decompileCompleted() || results.getDecompiledFunction() == null) {
            out.println("/* decompile failed */");
        }
        else {
            String[] lines = results.getDecompiledFunction().getC().split("\\R");
            int count = Math.min(lines.length, maxLines);
            for (int i = 0; i < count; i++) {
                out.println(lines[i]);
            }
            if (lines.length > count) {
                out.println("/* ... truncated ... */");
            }
        }
        out.println("```");
        out.println();
    }
}
