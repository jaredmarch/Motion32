// Ghidra headless script: raw pointer search for callback targets.
// Usage:
//   -postScript Motion32PointerSearchProbe.java <output.md>

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.mem.Memory;
import ghidra.program.model.scalar.Scalar;
import ghidra.program.model.symbol.Reference;

import java.io.File;
import java.io.PrintWriter;

public class Motion32PointerSearchProbe extends GhidraScript {
    private static final long[] TARGETS = {
        0x00003ac4L, 0x00003ac5L,
        0x000020a4L, 0x000020a5L,
        0x00002098L, 0x00002099L,
        0x00002e6cL, 0x00002e6dL
    };

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/pointer_search_probe.md";
        PrintWriter out = new PrintWriter(new File(outputPath));

        out.println("# Motion 32 Pointer Search Probe");
        out.println();
        Memory memory = currentProgram.getMemory();

        for (long target : TARGETS) {
            out.printf("## Target `0x%08x`%n%n", target);
            Address targetAddr = toAddr(target & ~1L);
            int refCount = 0;
            for (Reference ref : getReferencesTo(targetAddr)) {
                refCount++;
                Function fn = getFunctionContaining(ref.getFromAddress());
                out.printf("- Ghidra ref from `%s` in `%s` @ `%s` type=%s%n",
                    ref.getFromAddress(),
                    fn == null ? "<none>" : fn.getName(),
                    fn == null ? "<none>" : fn.getEntryPoint().toString(),
                    ref.getReferenceType());
            }
            if (refCount == 0) {
                out.println("- no Ghidra references to aligned address");
            }

            byte[] pattern = le32(target);
            out.printf("- raw little-endian pattern: `%02x %02x %02x %02x`%n",
                pattern[0] & 0xff, pattern[1] & 0xff, pattern[2] & 0xff, pattern[3] & 0xff);
            Address cur = currentProgram.getMinAddress();
            int hits = 0;
            while (true) {
                Address hit = memory.findBytes(cur, pattern, null, true, monitor);
                if (hit == null) {
                    break;
                }
                hits++;
                Function fn = getFunctionContaining(hit);
                out.printf("  - raw hit `%s` in `%s` @ `%s`%n",
                    hit,
                    fn == null ? "<none>" : fn.getName(),
                    fn == null ? "<none>" : fn.getEntryPoint().toString());
                cur = hit.add(1);
            }
            if (hits == 0) {
                out.println("  - no raw hits");
            }
            out.println("- instruction scalar/immediate hits:");
            int scalarHits = 0;
            InstructionIterator insns = currentProgram.getListing().getInstructions(true);
            while (insns.hasNext()) {
                Instruction insn = insns.next();
                for (int op = 0; op < insn.getNumOperands(); op++) {
                    Object[] objs = insn.getOpObjects(op);
                    for (Object obj : objs) {
                        if (obj instanceof Scalar) {
                            long value = ((Scalar)obj).getUnsignedValue();
                            if (value == target || value == (target & ~1L)) {
                                scalarHits++;
                                Function fn = getFunctionContaining(insn.getAddress());
                                out.printf("  - scalar hit `%s: %s` in `%s` @ `%s`%n",
                                    insn.getAddress(),
                                    insn.toString(),
                                    fn == null ? "<none>" : fn.getName(),
                                    fn == null ? "<none>" : fn.getEntryPoint().toString());
                            }
                        }
                    }
                }
            }
            if (scalarHits == 0) {
                out.println("  - no scalar hits");
            }
            out.println();
        }

        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private byte[] le32(long value) {
        return new byte[] {
            (byte)(value & 0xff),
            (byte)((value >> 8) & 0xff),
            (byte)((value >> 16) & 0xff),
            (byte)((value >> 24) & 0xff)
        };
    }
}
