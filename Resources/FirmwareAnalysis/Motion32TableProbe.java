// Ghidra headless script: search firmware data for callback pointers and MIDI-map-like tables.
// Usage:
//   -postScript Motion32TableProbe.java <output.md>

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.address.AddressSpace;
import ghidra.program.model.listing.Function;
import ghidra.program.model.mem.MemoryBlock;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Motion32TableProbe extends GhidraScript {
    private static class Target {
        String name;
        long address;

        Target(String name, long address) {
            this.name = name;
            this.address = address;
        }
    }

    private static class Pattern {
        String name;
        byte[] bytes;

        Pattern(String name, int... values) {
            this.name = name;
            this.bytes = new byte[values.length];
            for (int i = 0; i < values.length; i++) {
                this.bytes[i] = (byte)(values[i] & 0xff);
            }
        }
    }

    private static final Target[] POINTER_TARGETS = {
        new Target("outgoing Fender SysEx builder / false 0x8f lead", 0x2164c),
        new Target("UI redraw/update candidate", 0x21f24),
        new Target("MIDI/control map refresh candidate", 0x22b70),
        new Target("config getter", 0x2ec30),
        new Target("config setter-ish candidate", 0x2ea70),
        new Target("ranked 0x8f UI/graphics candidate", 0x3e600),
        new Target("ranked 0x8f UI/assert candidate", 0x3bb58),
        new Target("Tiny/packet-ish ranked candidate", 0x5ed60)
    };

    private static final Pattern[] BYTE_PATTERNS = {
        new Pattern("native transport ascending tap/rec/play/stop", 0x69, 0x6b, 0x6d, 0x6f),
        new Pattern("native transport descending stop/play/rec/tap", 0x6f, 0x6d, 0x6b, 0x69),
        new Pattern("pre-native transport symptom", 0x66, 0x67, 0x68, 0x69),
        new Pattern("native nav exact", 0x57, 0x59, 0x5a, 0x66),
        new Pattern("encoder CCs", 0x0e, 0x0f, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15),
        new Pattern("encoder touch CCs", 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77),
        new Pattern("native pads 36-51", 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x2b,
            0x2c, 0x2d, 0x2e, 0x2f, 0x30, 0x31, 0x32, 0x33),
        new Pattern("native pads 52-67", 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3a, 0x3b,
            0x3c, 0x3d, 0x3e, 0x3f, 0x40, 0x41, 0x42, 0x43),
        new Pattern("standalone pads 80-95", 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57,
            0x58, 0x59, 0x5a, 0x5b, 0x5c, 0x5d, 0x5e, 0x5f),
        new Pattern("standalone pads 96-111", 0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67,
            0x68, 0x69, 0x6a, 0x6b, 0x6c, 0x6d, 0x6e, 0x6f)
    };

    private PrintWriter out;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/table_probe.md";
        out = new PrintWriter(new File(outputPath));

        out.println("# Motion 32 Firmware Table Probe");
        out.println();
        out.println("- Program: `" + currentProgram.getName() + "`");
        out.println("- Language: `" + currentProgram.getLanguageID() + "`");
        out.println();

        writePointerHits();
        writePatternHits();

        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
    }

    private void writePointerHits() throws Exception {
        out.println("## Thumb/ARM Pointer Hits");
        out.println();
        for (Target target : POINTER_TARGETS) {
            out.printf("### `%s` @ `0x%08x`%n%n", target.name, target.address);
            int count = 0;
            count += writeU32Hits(target.address + 1, "thumb");
            count += writeU32Hits(target.address, "arm/plain");
            if (count == 0) {
                out.println("- no raw pointer hits");
            }
            out.println();
        }
    }

    private int writeU32Hits(long value, String kind) throws Exception {
        byte[] needle = new byte[] {
            (byte)(value & 0xff),
            (byte)((value >> 8) & 0xff),
            (byte)((value >> 16) & 0xff),
            (byte)((value >> 24) & 0xff)
        };
        int count = 0;
        for (Hit hit : findBytes(needle, 80)) {
            count++;
            out.printf("- `%s` pointer at `%s`%n", kind, hit.address);
            writeContext(hit.address, 24);
        }
        return count;
    }

    private void writePatternHits() throws Exception {
        out.println("## MIDI Map Byte-Pattern Hits");
        out.println();
        for (Pattern pattern : BYTE_PATTERNS) {
            out.printf("### `%s`%n%n", pattern.name);
            List<Hit> hits = findBytes(pattern.bytes, 40);
            if (hits.isEmpty()) {
                out.println("- no exact hits");
                out.println();
                continue;
            }
            for (Hit hit : hits) {
                out.printf("- hit at `%s`%n", hit.address);
                writeContext(hit.address, 32);
            }
            out.println();
        }
    }

    private static class Hit {
        Address address;
        byte[] blockBytes;
        int offset;

        Hit(Address address, byte[] blockBytes, int offset) {
            this.address = address;
            this.blockBytes = blockBytes;
            this.offset = offset;
        }
    }

    private List<Hit> findBytes(byte[] needle, int maxHits) throws Exception {
        List<Hit> hits = new ArrayList<Hit>();
        for (MemoryBlock block : currentProgram.getMemory().getBlocks()) {
            if (!block.isInitialized()) {
                continue;
            }
            long size = block.getSize();
            if (size <= 0 || size > Integer.MAX_VALUE) {
                continue;
            }
            byte[] haystack = new byte[(int)size];
            block.getBytes(block.getStart(), haystack);
            for (int i = 0; i <= haystack.length - needle.length; i++) {
                boolean found = true;
                for (int j = 0; j < needle.length; j++) {
                    if (haystack[i + j] != needle[j]) {
                        found = false;
                        break;
                    }
                }
                if (found) {
                    hits.add(new Hit(block.getStart().add(i), haystack, i));
                    if (hits.size() >= maxHits) {
                        return hits;
                    }
                }
            }
        }
        return hits;
    }

    private void writeContext(Address address, int radius) {
        Function fn = getFunctionContaining(address);
        out.printf("  - containing function: `%s` @ `%s`%n",
            fn == null ? "<none>" : fn.getName(),
            fn == null ? "<none>" : fn.getEntryPoint().toString());
        out.print("  - bytes:");
        try {
            AddressSpace space = address.getAddressSpace();
            long startOffset = Math.max(0, address.getOffset() - radius);
            Address start = space.getAddress(startOffset);
            for (int i = 0; i < radius * 2 + 16; i++) {
                Address cur = start.add(i);
                if (!currentProgram.getMemory().contains(cur)) {
                    continue;
                }
                out.printf(" %02x", currentProgram.getMemory().getByte(cur) & 0xff);
            }
        }
        catch (Exception e) {
            out.print(" <context unavailable>");
        }
        out.println();
    }
}
