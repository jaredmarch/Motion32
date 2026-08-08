// Ghidra headless script: survey the Motion 32 firmware import.
// @category Motion32

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.address.AddressSet;
import ghidra.program.model.listing.Data;
import ghidra.program.model.listing.DataIterator;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.listing.Listing;
import ghidra.program.model.mem.Memory;
import ghidra.program.model.mem.MemoryBlock;
import ghidra.program.model.scalar.Scalar;
import ghidra.program.model.symbol.Reference;
import ghidra.program.model.symbol.ReferenceIterator;
import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

public class Motion32FirmwareSurvey extends GhidraScript {
    private PrintWriter out;
    private Listing listing;
    private Memory memory;

    private static final List<String> TERMS = Arrays.asList(
        "Scale", "Chord", "Scales", "Famous", "Simple", "Progressions",
        "Chords/Intervals", "Choose Key", "Guide", "Layout", "Type", "Quality",
        "DAW mode", "Global Settings", "Firmware", "Ionian", "Dorian",
        "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian",
        "Major Pent", "M. Minor", "Minor Pent", "Minor Blues", "Major Blues",
        "Triad", "Sus2", "Sus4", "Add 7", "I V vi IV"
    );

    @Override
    protected void run() throws Exception {
        String[] args = getScriptArgs();
        String outputPath = args.length > 0 ? args[0] : "Resources/FirmwareAnalysis/firmware_survey.md";
        long vectorBase = args.length > 1 ? Long.decode(args[1]) : currentProgram.getMinAddress().getOffset();
        listing = currentProgram.getListing();
        memory = currentProgram.getMemory();

        File output = new File(outputPath);
        File parent = output.getParentFile();
        if (parent != null) {
            parent.mkdirs();
        }

        try (PrintWriter writer = new PrintWriter(output, "UTF-8")) {
            out = writer;
            writeHeader();
            writeVectorTable(vectorBase);
            writeFunctionSummary();
            writeTermSurvey();
            writeLikelyMidiConstants();
        }
        println("Wrote " + output.getAbsolutePath());
    }

    private void writeHeader() {
        out.println("# Motion 32 Firmware Survey");
        out.println();
        out.println("- Program: `" + currentProgram.getName() + "`");
        out.println("- Language: `" + currentProgram.getLanguageID() + "`");
        out.println("- Compiler spec: `" + currentProgram.getCompilerSpec().getCompilerSpecID() + "`");
        out.println("- Image base/min address: `" + currentProgram.getImageBase() + "` / `" + currentProgram.getMinAddress() + "`");
        out.println("- Max address: `" + currentProgram.getMaxAddress() + "`");
        out.println();
    }

    private void writeVectorTable(long vectorBase) throws Exception {
        out.println("## Vector Table Candidate");
        out.println();
        Address base = toAddr(vectorBase);
        out.println("- Vector-table base used by survey: `" + base + "`");
        out.println();
        for (int i = 0; i < 32; i++) {
            Address addr = base.add(i * 4L);
            long raw = Integer.toUnsignedLong(memory.getInt(addr));
            if (raw == 0 || raw == 0xffffffffL) {
                out.printf("- `%02d` @ `%s`: `0x%08x`%n", i, addr, raw);
                continue;
            }
            boolean thumb = (raw & 1L) != 0;
            long target = raw & ~1L;
            Function f = listing.getFunctionContaining(toAddr(target));
            out.printf(
                "- `%02d` @ `%s`: `0x%08x`%s -> `%s` %s%n",
                i,
                addr,
                raw,
                thumb ? " (Thumb)" : "",
                toAddr(target),
                f == null ? "" : "`" + f.getName() + "`"
            );
        }
        out.println();
    }

    private void writeFunctionSummary() {
        out.println("## Function Summary");
        out.println();
        FunctionIterator functions = listing.getFunctions(true);
        int count = 0;
        int withBodies = 0;
        long bytes = 0;
        List<Function> first = new ArrayList<>();
        while (functions.hasNext()) {
            Function f = functions.next();
            count++;
            if (f.getBody() != null) {
                withBodies++;
                bytes += f.getBody().getNumAddresses();
            }
            if (first.size() < 40) {
                first.add(f);
            }
        }
        out.println("- Functions: `" + count + "`");
        out.println("- Functions with bodies: `" + withBodies + "`");
        out.println("- Function-body bytes: `" + bytes + "`");
        out.println();
        out.println("First functions by address:");
        for (Function f : first) {
            out.println("- `" + f.getEntryPoint() + "` `" + f.getName() + "` size=" + f.getBody().getNumAddresses());
        }
        out.println();
    }

    private void writeTermSurvey() throws Exception {
        out.println("## Scale/Chord String Survey");
        out.println();
        Map<String, List<Address>> hits = new TreeMap<>();
        for (String term : TERMS) {
            hits.put(term, findAscii(term));
        }

        DecompInterface decompiler = new DecompInterface();
        decompiler.openProgram(currentProgram);
        Set<Function> interesting = new HashSet<>();

        for (String term : TERMS) {
            List<Address> addresses = hits.get(term);
            if (addresses.isEmpty()) {
                continue;
            }
            out.println("### `" + term + "`");
            out.println();
            for (Address addr : addresses) {
                out.println("- string bytes at `" + addr + "`");
                ReferenceIterator refs = currentProgram.getReferenceManager().getReferencesTo(addr);
                int refCount = 0;
                while (refs.hasNext()) {
                    Reference ref = refs.next();
                    refCount++;
                    Function f = listing.getFunctionContaining(ref.getFromAddress());
                    out.println("  - ref from `" + ref.getFromAddress() + "`" + (f == null ? "" : " in `" + f.getName() + "` @ `" + f.getEntryPoint() + "`"));
                    if (f != null) {
                        interesting.add(f);
                    }
                    if (refCount >= 20) {
                        out.println("  - ... more refs omitted");
                        break;
                    }
                }
                if (refCount == 0) {
                    out.println("  - no direct Ghidra xrefs");
                    Function near = nearestFunctionBefore(addr);
                    if (near != null) {
                        out.println("  - nearest prior function: `" + near.getName() + "` @ `" + near.getEntryPoint() + "`");
                    }
                }
            }
            out.println();
        }

        out.println("## Decompile Snippets For String-Referencing Functions");
        out.println();
        Function[] funcs = interesting.toArray(new Function[0]);
        Arrays.sort(funcs, Comparator.comparing(Function::getEntryPoint));
        int emitted = 0;
        for (Function f : funcs) {
            if (emitted >= 30) {
                out.println("- More functions omitted.");
                break;
            }
            emitted++;
            out.println("### `" + f.getName() + "` @ `" + f.getEntryPoint() + "`");
            out.println();
            DecompileResults result = decompiler.decompileFunction(f, 20, monitor);
            if (result != null && result.decompileCompleted() && result.getDecompiledFunction() != null) {
                out.println("```c");
                out.println(limit(result.getDecompiledFunction().getC(), 7000));
                out.println("```");
            } else {
                out.println("Decompiler did not complete; first instructions:");
                out.println();
                out.println("```asm");
                emitInstructions(f, 80);
                out.println("```");
            }
            out.println();
        }
        decompiler.dispose();
    }

    private void writeLikelyMidiConstants() {
        out.println("## Immediate Constants Worth Checking");
        out.println();
        int[] constants = {0x08, 0x20, 0x21, 0x22, 0x23, 0x36, 0x7e, 0x7f, 0xf0, 0xf7};
        for (int constant : constants) {
            int count = 0;
            List<String> examples = new ArrayList<>();
            InstructionIterator instructions = listing.getInstructions(true);
            while (instructions.hasNext()) {
                Instruction instr = instructions.next();
                for (Object obj : instr.getOpObjects(0)) {
                    if (obj instanceof Scalar && ((Scalar) obj).getUnsignedValue() == constant) {
                        count++;
                        if (examples.size() < 8) {
                            Function f = listing.getFunctionContaining(instr.getAddress());
                            examples.add("`" + instr.getAddress() + "` " + instr + (f == null ? "" : " in `" + f.getName() + "`"));
                        }
                    }
                }
            }
            out.printf("- `0x%02x`: %d operand-0 hits%n", constant, count);
            for (String example : examples) {
                out.println("  - " + example);
            }
        }
        out.println();
    }

    private List<Address> findAscii(String needle) throws Exception {
        List<Address> found = new ArrayList<>();
        byte[] pattern = needle.getBytes("US-ASCII");
        for (MemoryBlock block : memory.getBlocks()) {
            if (!block.isInitialized()) {
                continue;
            }
            long size = block.getSize();
            if (size <= 0 || size > 4_000_000L) {
                continue;
            }
            byte[] bytes = new byte[(int) size];
            memory.getBytes(block.getStart(), bytes);
            for (int i = 0; i <= bytes.length - pattern.length; i++) {
                boolean ok = true;
                for (int j = 0; j < pattern.length; j++) {
                    if (bytes[i + j] != pattern[j]) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    found.add(block.getStart().add(i));
                }
            }
        }
        return found;
    }

    private Function nearestFunctionBefore(Address addr) {
        FunctionIterator it = listing.getFunctions(addr, false);
        if (it.hasNext()) {
            return it.next();
        }
        return null;
    }

    private void emitInstructions(Function f, int max) {
        AddressSet set = new AddressSet(f.getBody());
        InstructionIterator it = listing.getInstructions(set, true);
        int count = 0;
        while (it.hasNext() && count++ < max) {
            Instruction instr = it.next();
            out.println(instr.getAddress() + ": " + instr);
        }
    }

    private String limit(String s, int max) {
        if (s == null || s.length() <= max) {
            return s;
        }
        return s.substring(0, max) + "\n/* ... truncated ... */";
    }
}
