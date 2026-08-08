// Ghidra headless script: dump functions around specific raw-address clues.
// Usage:
//   -postScript Motion32AddressProbe.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;

import java.io.File;
import java.io.PrintWriter;

public class Motion32AddressProbe extends GhidraScript {
    private static final long[] ADDRESSES = {
        0x2607bl, 0x260c3l, 0x5fcffl, 0xa2179l,
        0x47bb4l, 0x21f24l, 0x22b70l,
        0x2164cl, 0x2064cl, 0x3ab58l, 0x3d600l,
        0x3f83al, 0x3f354l, 0x4b084l, 0x5ed60l,
        0x657cl, 0x6808l, 0x6b00l, 0x6cb4l,
        0x1e50l, 0x1fb0l, 0x240cl,
        0x2ea70l, 0x2ec30l, 0x2ec74l, 0x2ecb8l, 0x2ece0l, 0x2edc4l,
        0x2eadcl, 0x2eb4cl, 0x2eba8l, 0x2f1f8l, 0x2f220l, 0x2f234l,
        0x2f2f0l, 0x2f644l, 0x2fb60l,
        0x2ee68l, 0x2f304l, 0x2f788l, 0x2f7b8l, 0x2f7ecl,
        0x2f864l, 0x2f908l, 0x2f968l
    };

    private PrintWriter out;
    private DecompInterface decompiler;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/address_probe.md";
        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 Address Probe");
        out.println();
        for (long raw : ADDRESSES) {
            Address addr = toAddr(raw);
            Function fn = getFunctionContaining(addr);
            if (fn == null) {
                fn = getFunctionAt(addr);
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
            out.printf("## `%s`%n%n", addr);
            if (fn == null) {
                out.println("- no containing function");
                dumpInstructions(addr, 12);
                continue;
            }
            out.printf("- function: `%s` @ `%s`%n", fn.getName(), fn.getEntryPoint());
            dumpInstructions(addr, 14);
            dumpDecompile(fn, 220);
        }

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private void dumpInstructions(Address addr, int radius) {
        out.println();
        out.println("```asm");
        Instruction inst = currentProgram.getListing().getInstructionAt(addr);
        if (inst == null) {
            inst = currentProgram.getListing().getInstructionBefore(addr);
        }
        if (inst == null) {
            out.println("; no instruction nearby");
            out.println("```");
            out.println();
            return;
        }
        Instruction cur = inst;
        for (int i = 0; i < radius; i++) {
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
