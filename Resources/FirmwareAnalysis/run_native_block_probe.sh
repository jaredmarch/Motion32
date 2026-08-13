#!/bin/sh
# Maps the second code region at 0x10100000 and searches it for the native-mode handler.
#
# ⚠️ UNLIKE THE OTHER PROBES, THIS ONE WRITES TO THE PROJECT.
#
# It creates a memory block, disassembles into it and runs analysis, so it cannot use
# -readOnly. The project is backed up first — see BACKUP below. If anything goes wrong,
# delete ghidra_project and restore the backup.
#
# It targets the PAYLOAD import only. `motion32_fw_payload_0x1000.bin` is the file whose
# offset 0x20000 corresponds to runtime 0x10100000; the same arithmetic does not hold for
# motionupgrade.bin, which carries an extra 0x1000-byte header.
#
#   Motion32Firmware  <- motion32_fw_payload_0x1000.bin   <- THIS ONE
#
# Override the Ghidra location if yours moved:
#   GHIDRA=/path/to/ghidra ./run_native_block_probe.sh
set -e
GHIDRA="${GHIDRA:-$HOME/Downloads/ghidra_12.1.2_PUBLIC}"
HERE="$(cd "$(dirname "$0")" && pwd)"
REPORT="$HERE/native_block_probe.md"

if [ ! -x "$GHIDRA/support/analyzeHeadless" ]; then
    echo "analyzeHeadless not found under $GHIDRA" >&2
    echo "Set GHIDRA=/path/to/ghidra_12.1.2_PUBLIC" >&2
    exit 1
fi

# --- backup, because this run is destructive -------------------------------
BACKUP="$HERE/ghidra_project.backup-$(date +%Y%m%d-%H%M%S)"
echo "Backing up project -> $BACKUP"
cp -R "$HERE/ghidra_project" "$BACKUP"

echo "=== Motion32Firmware / motion32_fw_payload_0x1000.bin"
echo "    block: file 0x20000 -> 0x10100000"
"$GHIDRA/support/analyzeHeadless" \
    "$HERE/ghidra_project" Motion32Firmware \
    -process motion32_fw_payload_0x1000.bin \
    -noanalysis \
    -scriptPath "$HERE" \
    -postScript Motion32NativeBlockProbe.java "$REPORT" \
    -log "$HERE/ghidra_native_block_probe.log"

echo
echo "Done."
echo "  Report: $REPORT"
echo "  Log:    $HERE/ghidra_native_block_probe.log"
echo "  Backup: $BACKUP"
echo
echo "Read section 3 first — the function count in the new block."
echo "If it is small, analysis under-ran and the searches mean little."
