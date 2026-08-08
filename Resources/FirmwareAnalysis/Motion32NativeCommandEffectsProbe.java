// Ghidra headless script: trace concrete firmware effects around host/native mode.
// Usage:
//   -postScript Motion32NativeCommandEffectsProbe.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.scalar.Scalar;
import ghidra.program.model.symbol.Reference;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Motion32NativeCommandEffectsProbe extends GhidraScript {
    private static final long[] FUNCTIONS = {
        0x01e5cL, 0x01e50L,
        0x03a14L, 0x03ac4L, 0x03ab8L,
        0x05df4L, 0x05f2cL, 0x05f14L, 0x05854L, 0x0657cL,
        0x097e4L, 0x09818L, 0x09874L, 0x098c4L, 0x098c8L,
        0x020a4L, 0x02098L, 0x03f88L,
        0x026f4L, 0x0240cL, 0x027d4L,
        0x019c0L, 0x019e8L, 0x01b30L, 0x01bf0L, 0x01c8cL, 0x01cfcL
    };

    private static final long[] ADDRS = {
        0x20004291L, 0x20004292L, 0x20004294L, 0x20004298L,
        0x20004084L, 0x200040a0L,
        0x20004538L, 0x200045caL, 0x200045ccL,
        0x20005cbcL, 0x20005cd4L, 0x20005d04L, 0x20005d24L,
        0x000097e4L, 0x00009818L, 0x00009874L, 0x000098c4L, 0x000098c8L
    };

    private PrintWriter out;
    private DecompInterface decompiler;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/native_command_effects_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 Native Command Effects Probe");
        out.println();
        writeFunctions();
        writeAddressReferences();
        writeScalarHits();
        writeConfigKeyScan();

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
            if (fn == null) {
                disassemble(addr);
                try {
                    createFunction(addr, "PROBE_" + addr.toString());
                }
                catch (Exception ignored) {
                }
                fn = getFunctionAt(addr);
            }
            out.printf("### `%s` `%s`%n%n", addr, fn == null ? "<none>" : fn.getName());
            if (fn != null) {
                dumpDecompile(fn, 220);
                writeCallers(addr);
            }
            else {
                dumpInstructions(addr, 16);
            }
        }
    }

    private void writeAddressReferences() throws Exception {
        out.println("## Address References");
        out.println();
        for (long raw : ADDRS) {
            Address target = toAddr(raw);
            out.printf("### `%s`%n%n", target);
            List<Function> funcs = new ArrayList<Function>();
            int refCount = 0;
            for (Reference ref : getReferencesTo(target)) {
                refCount++;
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
            if (refCount == 0) {
                out.println("- no direct references found");
            }
            out.println();
            for (Function fn : funcs) {
                out.printf("#### `%s` @ `%s`%n%n", fn.getName(), fn.getEntryPoint());
                dumpInstructionsNearRefs(fn, target, 8);
            }
        }
    }

    private void writeScalarHits() {
        long[] values = {0x204L, 0x8fL, 0x7fL, 0x00L, 0x09L, 0x08L};
        out.println("## Scalar/Immediate Hits");
        out.println();
        for (long value : values) {
            out.printf("### `0x%x`%n%n", value);
            int count = 0;
            InstructionIterator it = currentProgram.getListing().getInstructions(true);
            while (it.hasNext()) {
                Instruction insn = it.next();
                for (int op = 0; op < insn.getNumOperands(); op++) {
                    Object[] objs = insn.getOpObjects(op);
                    for (Object obj : objs) {
                        if (obj instanceof Scalar) {
                            long scalar = ((Scalar)obj).getUnsignedValue();
                            if (scalar == value) {
                                count++;
                                Function fn = getFunctionContaining(insn.getAddress());
                                out.printf("- `%s: %s` in `%s` @ `%s`%n",
                                    insn.getAddress(),
                                    insn.toString(),
                                    fn == null ? "<none>" : fn.getName(),
                                    fn == null ? "<none>" : fn.getEntryPoint().toString());
                                if (count >= 80) {
                                    out.println("- ... truncated after 80 hits");
                                    break;
                                }
                            }
                        }
                    }
                    if (count >= 80) {
                        break;
                    }
                }
                if (count >= 80) {
                    break;
                }
            }
            if (count == 0) {
                out.println("- no scalar hits");
            }
            out.println();
        }
    }

    private void writeConfigKeyScan() throws Exception {
        out.println("## Decompiled Function Scan");
        out.println();
        out.println("Functions whose decompiled C mentions the config key or mode/effect globals.");
        out.println();
        FunctionIterator it = currentProgram.getFunctionManager().getFunctions(true);
        while (it.hasNext()) {
            Function fn = it.next();
            DecompileResults results = decompiler.decompileFunction(fn, 15, monitor);
            if (!results.decompileCompleted()) {
                continue;
            }
            String c = results.getDecompiledFunction().getC();
            boolean hit = c.contains("0x204") ||
                c.contains("DAT_20004291") ||
                c.contains("20004291") ||
                c.contains("DAT_200045cc") ||
                c.contains("DAT_200045ca") ||
                c.contains("0x20004538") ||
                c.contains("0x200040a0");
            if (!hit) {
                continue;
            }
            out.printf("### `%s` @ `%s`%n%n", fn.getName(), fn.getEntryPoint());
            dumpDecompile(fn, 160);
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
