// Ghidra headless script: dump direct callers of FUN_00001e50 mode getter.
// Usage:
//   -postScript Motion32ModeGetterCallersDump.java <output.md>

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.symbol.Reference;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Motion32ModeGetterCallersDump extends GhidraScript {
    private PrintWriter out;
    private DecompInterface decompiler;

    @Override
    protected void run() throws Exception {
        String outputPath = getScriptArgs().length > 0
            ? getScriptArgs()[0]
            : "Resources/FirmwareAnalysis/mode_getter_callers_dump.md";

        out = new PrintWriter(new File(outputPath));
        decompiler = new DecompInterface();
        decompiler.setOptions(new DecompileOptions());
        decompiler.openProgram(currentProgram);

        Address getter = toAddr(0x1e50L);
        out.println("# Motion 32 Mode Getter Callers Dump");
        out.println();
        List<Function> callers = new ArrayList<Function>();
        for (Reference ref : getReferencesTo(getter)) {
            Function fn = getFunctionContaining(ref.getFromAddress());
            if (fn != null && !callers.contains(fn)) {
                callers.add(fn);
            }
        }
        Collections.sort(callers, new Comparator<Function>() {
            public int compare(Function a, Function b) {
                return a.getEntryPoint().compareTo(b.getEntryPoint());
            }
        });
        for (Function fn : callers) {
            out.printf("## `%s` @ `%s`%n%n", fn.getName(), fn.getEntryPoint());
            dumpDecompile(fn, 260);
        }

        decompiler.dispose();
        out.close();
        println("Wrote " + new File(outputPath).getAbsolutePath());
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
