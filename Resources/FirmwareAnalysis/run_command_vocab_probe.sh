#!/bin/sh
# Runs Motion32CommandVocabProbe against both firmware imports.
#
# Same two-program caveat as run_host_config_probe.sh:
#
#   Motion32Firmware      <- motion32_fw_payload_0x1000.bin   (the extracted payload)
#   Motion32FirmwareFull  <- motionupgrade.bin                (the whole upgrade file)
#
# The payload import is the one every anchor belongs to; host_config_probe_payload.md confirmed
# it by resolving 0x9664 to the expected control-id table. The full image is produced only so the
# two can be diffed.
#
# Note on -analysis. Unlike the host-config probe, this one is run WITH analysis enabled the first
# time, because the literal-pool scan wants Ghidra's data references to exist. If the project has
# already been analysed the flag costs nothing; pass NOANALYSIS=1 to force the fast path.
#
#   GHIDRA=/path/to/ghidra ./run_command_vocab_probe.sh
set -e
GHIDRA="${GHIDRA:-$HOME/Downloads/ghidra_12.1.2_PUBLIC}"
HERE="$(cd "$(dirname "$0")" && pwd)"

if [ -n "$NOANALYSIS" ]; then
    ANALYSIS_FLAG="-noanalysis"
else
    ANALYSIS_FLAG=""
fi

run_one() {
    project="$1"
    program="$2"
    report="$3"
    echo "=== $project / $program -> $(basename "$report")"
    "$GHIDRA/support/analyzeHeadless" \
        "$HERE/ghidra_project" "$project" \
        -process "$program" \
        $ANALYSIS_FLAG -readOnly \
        -scriptPath "$HERE" \
        -postScript Motion32CommandVocabProbe.java "$report" \
        -log "$HERE/ghidra_command_vocab_$(basename "$report" .md).log"
}

run_one Motion32Firmware     motion32_fw_payload_0x1000.bin "$HERE/command_vocab_payload.md"
run_one Motion32FirmwareFull motionupgrade.bin              "$HERE/command_vocab_full.md"

echo
echo "Done."
echo "  Payload (anchors valid here): $HERE/command_vocab_payload.md"
echo "  Full image (for comparison):  $HERE/command_vocab_full.md"
