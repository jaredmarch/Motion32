#!/bin/sh
# Runs Motion32EmitterProbe against the PAYLOAD import only.
#
# Unlike the previous two probes this one is deliberately single-program. Its addresses
# (0x00000e50, 0x00000fb0, 0x00000eec, 0x000016f4, 0x0000140c, 0x00001288) came out of
# host_config_probe_payload.md, so they are payload addresses and mean nothing in
# motionupgrade.bin. Running it against the full image would produce confident nonsense,
# which is the exact mistake the earlier pass made.
#
#   GHIDRA=/path/to/ghidra ./run_emitter_probe.sh
set -e
GHIDRA="${GHIDRA:-$HOME/Downloads/ghidra_12.1.2_PUBLIC}"
HERE="$(cd "$(dirname "$0")" && pwd)"

echo "=== Motion32Firmware / motion32_fw_payload_0x1000.bin -> emitter_probe_payload.md"
"$GHIDRA/support/analyzeHeadless" \
    "$HERE/ghidra_project" Motion32Firmware \
    -process motion32_fw_payload_0x1000.bin \
    -noanalysis -readOnly \
    -scriptPath "$HERE" \
    -postScript Motion32EmitterProbe.java "$HERE/emitter_probe_payload.md" \
    -log "$HERE/ghidra_emitter_probe.log"

echo
echo "Done: $HERE/emitter_probe_payload.md"
