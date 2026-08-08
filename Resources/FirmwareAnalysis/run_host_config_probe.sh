#!/bin/sh
# Runs Motion32HostConfigProbe against BOTH firmware imports.
#
# There are two programs in this folder's Ghidra projects and they are NOT interchangeable:
#
#   Motion32Firmware      <- motion32_fw_payload_0x1000.bin   (the extracted payload)
#   Motion32FirmwareFull  <- motionupgrade.bin                (the whole upgrade file)
#
# Every address in NativeMode_USB_EventStream_Report.md ("In the payload import, ...") is a
# **payload** address: the queues at 0x200040a0 / 0x20004084, the ring helpers at 0x00000d6c,
# the config selector FUN_00000e50, the tables at 0x9664 / 0x95fc / 0x9874.
#
# Running the probe against motionupgrade.bin resolves none of those: 0x9664 there decodes as
# `bx lr` / `push` / `pop` (code, not a control-id table) and both queues have zero references.
# Both reports are produced so the two can be compared rather than confused again.
#
# Override the Ghidra location if yours moved:
#   GHIDRA=/path/to/ghidra ./run_host_config_probe.sh
set -e
GHIDRA="${GHIDRA:-$HOME/Downloads/ghidra_12.1.2_PUBLIC}"
HERE="$(cd "$(dirname "$0")" && pwd)"

run_one() {
    project="$1"
    program="$2"
    report="$3"
    echo "=== $project / $program -> $(basename "$report")"
    "$GHIDRA/support/analyzeHeadless" \
        "$HERE/ghidra_project" "$project" \
        -process "$program" \
        -noanalysis -readOnly \
        -scriptPath "$HERE" \
        -postScript Motion32HostConfigProbe.java "$report" \
        -log "$HERE/ghidra_host_config_$(basename "$report" .md).log"
}

# The payload import first - this is the one the anchors belong to.
run_one Motion32Firmware     motion32_fw_payload_0x1000.bin "$HERE/host_config_probe_payload.md"
run_one Motion32FirmwareFull motionupgrade.bin              "$HERE/host_config_probe_full.md"

echo
echo "Done."
echo "  Payload (anchors valid here): $HERE/host_config_probe_payload.md"
echo "  Full image (for comparison):  $HERE/host_config_probe_full.md"
