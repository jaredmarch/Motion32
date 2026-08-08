// Ghidra headless script: trace the internal event stream at 0x20004084.
// Usage:
//   -postScript Motion32EventStreamConsumerProbe.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.mem.MemoryBlock;
import ghidra.program.model.symbol.Reference;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Motion32EventStreamConsumerProbe extends GhidraScript {
    private static final long[] FOCUS_FUNCTIONS = {
        0x01d28L, 0x01d54L, 0x01d6cL, 0x01d94L, 0x01dc0L,
        0x01eecL, 0x01f6cL, 0x01fb0L, 0x02030L, 0x020a4L,
        0x02288L, 0x0234cL, 0x0240cL, 0x02618L,
        0x09944L, 0x09e1cL
    };

    private static final long[] QUEUE_TARGETS = {
        0x20004080L, 0x20004081L, 0x20004084L, 0x20004098L,
        0x200040a0L, 0x200040b4L
    };

    private PrintWriter out;
    private DecompInterface decompiler;

    private static class Hit {
        Function fn;
        int score;
        String c;
        List<String> reasons = new ArrayList<String>();
    }

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/event_stream_consumer_probe.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        out.println("# Motion 32 Event Stream Consumer Probe");
        out.println();
        out.println("Focus: queue `0x20004084` and opcodes `0x14`, `0x15`, `0x16`, `0x36`.");
        out.println();

        writeFocusFunctions();
        writeQueueReferences();
        writeRankedQueueUsers();
        writeRawPointerHits();

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private void writeFocusFunctions() throws Exception {
        out.println("## Focus Functions");
        out.println();
        for (long raw : FOCUS_FUNCTIONS) {
            Address addr = toAddr(raw);
            Function fn = getFunctionAt(addr);
            if (fn == null) {
                fn = getFunctionContaining(addr);
            }
            out.printf("### `%s` `%s`%n%n", addr, fn == null ? "<none>" : fn.getName());
            writeCallers(addr);
            dumpInstructions(addr, 14);
            if (fn != null) {
                dumpDecompile(fn, 180);
            }
        }
    }

    private void writeQueueReferences() throws Exception {
        out.println("## Queue RAM References");
        out.println();
        for (long raw : QUEUE_TARGETS) {
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
                out.printf("#### `%s` @ `%s`%n%n", fn.getName(), fn.getEntryPoint());
                dumpInstructionsNearRefs(fn, target, 8);
                dumpDecompile(fn, 140);
            }
        }
    }

    private void writeRankedQueueUsers() throws Exception {
        out.println("## Ranked Event-Queue Users");
        out.println();
        List<Hit> hits = new ArrayList<Hit>();
        FunctionIterator it = currentProgram.getFunctionManager().getFunctions(true);
        while (it.hasNext()) {
            Function fn = it.next();
            DecompileResults results = decompiler.decompileFunction(fn, 20, monitor);
            if (!results.decompileCompleted() || results.getDecompiledFunction() == null) {
                continue;
            }
            String c = results.getDecompiledFunction().getC();
            Hit hit = score(fn, c);
            if (hit.score >= 28) {
                hit.c = c;
                hits.add(hit);
            }
        }
        Collections.sort(hits, new Comparator<Hit>() {
            public int compare(Hit a, Hit b) {
                return b.score - a.score;
            }
        });
        int count = Math.min(50, hits.size());
        for (int i = 0; i < count; i++) {
            Hit hit = hits.get(i);
            out.printf("### `%s` @ `%s` score `%d`%n%n",
                hit.fn.getName(), hit.fn.getEntryPoint(), hit.score);
            out.println("- reasons: " + String.join(", ", hit.reasons));
            out.println();
            dumpDecompileText(hit.c, 140);
        }
        if (count == 0) {
            out.println("No candidates crossed the threshold.");
        }
    }

    private Hit score(Function fn, String c) {
        Hit hit = new Hit();
        hit.fn = fn;
        addIf(hit, c.contains("0x20004084"), 35, "exact event queue address");
        addIf(hit, c.contains("0x20004080") || c.contains("0x20004098"), 14, "adjacent event queue state");
        addIf(hit, c.contains("FUN_00001d54") || c.contains("FUN_00001d94") || c.contains("FUN_00001dc0"), 28, "possible queue read helper");
        addIf(hit, c.contains("FUN_00001d6c"), 16, "queue write helper");
        addIf(hit, c.contains("0x14") || c.contains("0x15") || c.contains("0x16") || c.contains("0x36"), 12, "event opcode constant");
        addIf(hit, c.contains("0xf0") || c.contains("0xf7") || c.contains("0x7f"), 8, "framing/7-bit MIDI-like value");
        addIf(hit, c.contains("FUN_00002030") || c.contains("FUN_00001eec") || c.contains("FUN_00001f6c") || c.contains("FUN_00001fb0"), 22, "known encoder function");
        addIf(hit, c.contains("FUN_0002654c") || c.contains("FUN_0002754c"), 16, "likely outbound MIDI send");
        addIf(hit, c.contains("switch") || c.contains("case"), 5, "dispatch");
        addIf(hit, c.contains("glyph") || c.contains("font") || c.contains("draw") || c.contains("UTF"), -12, "text/graphics false positive");
        return hit;
    }

    private void writeRawPointerHits() throws Exception {
        out.println("## Raw Queue Address DWord Hits");
        out.println();
        for (long target : QUEUE_TARGETS) {
            out.printf("### `%08x`%n%n", target);
            int hits = 0;
            for (MemoryBlock block : currentProgram.getMemory().getBlocks()) {
                if (!block.isInitialized()) {
                    continue;
                }
                Address cur = block.getStart();
                Address end = block.getEnd();
                while (cur.compareTo(end) <= 0 && cur.addNoWrap(3).compareTo(end) <= 0) {
                    long value = getIntLE(cur);
                    if (value == target) {
                        Function fn = getFunctionContaining(cur);
                        out.printf("- `%s`: in block `%s`, containing `%s` @ `%s`%n",
                            cur, block.getName(),
                            fn == null ? "<none>" : fn.getName(),
                            fn == null ? "<none>" : fn.getEntryPoint().toString());
                        hits++;
                        if (hits >= 80) {
                            out.println("- truncated");
                            break;
                        }
                    }
                    cur = cur.addNoWrap(1);
                }
            }
            if (hits == 0) {
                out.println("- no raw dword hits found");
            }
            out.println();
        }
    }

    private void writeCallers(Address target) {
        out.println("Callers/references:");
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

    private void dumpInstructionsNearRefs(Function fn, Address target, int radius) {
        for (Reference ref : getReferencesTo(target)) {
            if (fn.getBody().contains(ref.getFromAddress())) {
                dumpInstructions(ref.getFromAddress(), radius);
            }
        }
    }

    private long getIntLE(Address address) throws Exception {
        long b0 = currentProgram.getMemory().getByte(address) & 0xffL;
        long b1 = currentProgram.getMemory().getByte(address.addNoWrap(1)) & 0xffL;
        long b2 = currentProgram.getMemory().getByte(address.addNoWrap(2)) & 0xffL;
        long b3 = currentProgram.getMemory().getByte(address.addNoWrap(3)) & 0xffL;
        return b0 | (b1 << 8) | (b2 << 16) | (b3 << 24);
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
            dumpDecompileTextRaw(results.getDecompiledFunction().getC(), maxLines);
        }
        out.println("```");
        out.println();
    }

    private void dumpDecompileText(String c, int maxLines) {
        out.println("```c");
        dumpDecompileTextRaw(c, maxLines);
        out.println("```");
        out.println();
    }

    private void dumpDecompileTextRaw(String c, int maxLines) {
        String[] lines = c.split("\\n");
        for (int i = 0; i < lines.length && i < maxLines; i++) {
            out.println(lines[i]);
        }
        if (lines.length > maxLines) {
            out.println("/* ... truncated ... */");
        }
    }

    private void addIf(Hit hit, boolean condition, int points, String reason) {
        if (condition) {
            hit.score += points;
            hit.reasons.add(reason);
        }
    }
}
