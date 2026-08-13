#!/bin/sh
# Hunts the consumer of internal id 0x72 (the native-mode switch) and checks whether the
# application's own SysEx handler can reach the MIDI assignment setters.
#
# Read app_midi_routing_engine.md first — this probe assumes its findings.
#
# PREREQUISITE: the app block must already be mapped at 0x10100000 (file offset 0x20000).
# Motion32NativeBlockProbe.java creates it, or add it by hand in Window -> Memory Map.
# This script is -readOnly and will abort cleanly if the block is missing.
#
# Override the Ghidra location if yours moved:
#   GHIDRA=/path/to/ghidra ./run_native_switch_probe.sh
set -e
GHIDRA="${GHIDRA:-$HOME/Downloads/ghidra_12.1.2_PUBLIC}"
HERE="$(cd "$(dirname "$0")" && pwd)"
REPORT="$HERE/native_switch_probe.md"

if [ ! -x "$GHIDRA/support/analyzeHeadless" ]; then
    echo "analyzeHeadless not found under $GHIDRA" >&2
    echo "Set GHIDRA=/path/to/ghidra_12.1.2_PUBLIC" >&2
    exit 1
fi

echo "=== Motion32Firmware / motion32_fw_payload_0x1000.bin"
"$GHIDRA/support/analyzeHeadless" \
    "$HERE/ghidra_project" Motion32Firmware \
    -process motion32_fw_payload_0x1000.bin \
    -noanalysis -readOnly \
    -scriptPath "$HERE" \
    -postScript Motion32NativeSwitchProbe.java "$REPORT" \
    -log "$HERE/ghidra_native_switch_probe.log"

echo
echo "Done. Report: $REPORT"
echo
echo "Read in this order:"
echo "  section 0 - function count. Under 200 means analysis under-ran and the rest is unreliable."
echo "  section 3 - any function comparing against 0x72 that is NOT FUN_101065f4 is the switch."
echo "  section 4 - a line marked 'REACHES THE SETTER CLUSTER' means no firmware patching is needed."
