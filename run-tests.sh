#!/usr/bin/env bash
#
# The offline suite. No Ableton, no hardware.
#
#   bash run-tests.sh
#
# A full green run is 171 groups and 4,157 assertions. Those are enforced as **floors**
# below, not just documented: a suite that quietly stops asserting still exits zero, so
# "0 failures" on its own is not evidence that anything ran. See §6b-13 — an earlier
# version of the suite reported success while checking nothing.

set -uo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

# Raise these when guards are added. They may never be lowered without saying why.
MIN_GROUPS=171
MIN_ASSERTIONS=4157

missing=0

# --- preconditions ---------------------------------------------------------
# Two guards decompile Live's own framework. Without these they cannot run, and the
# suite correctly reports that as failure rather than skipping quietly.

if ! python3 -c "import xdis" 2>/dev/null; then
  echo "WARNING: xdis is not installed — the framework guards cannot run."
  echo "  pip3 install xdis --break-system-packages"
  echo
  missing=1
fi

if [[ ! -d "Resources/control_surface" ]]; then
  echo "WARNING: Resources/control_surface/ is absent — the framework guards cannot run."
  echo "  Copy ableton/v3/control_surface/ out of your Live 12 installation."
  echo "  (Gitignored on purpose: it is Ableton's proprietary .pyc, not ours to redistribute.)"
  echo
  missing=1
fi

# --- run -------------------------------------------------------------------
output="$(mktemp)"
trap 'rm -f "$output"' EXIT

python3 tests/test_screen.py 2>&1 | tee "$output"
status="${PIPESTATUS[0]}"

groups="$(grep -oE '[0-9]+ test groups' "$output" | grep -oE '^[0-9]+' | head -1)"
assertions="$(grep -oE '^[0-9]+ assertions' "$output" | grep -oE '^[0-9]+' | head -1)"
groups="${groups:-0}"
assertions="${assertions:-0}"

echo
echo "--- completeness ---"
printf 'groups:     %5s  (floor %s)\n' "$groups" "$MIN_GROUPS"
printf 'assertions: %5s  (floor %s)\n' "$assertions" "$MIN_ASSERTIONS"

shortfall=0
if (( groups < MIN_GROUPS )); then
  echo "SHORTFALL: fewer test groups than expected — a guard was removed or stopped being collected."
  shortfall=1
fi
if (( assertions < MIN_ASSERTIONS )); then
  echo "SHORTFALL: fewer assertions than expected — a guard ran but stopped asserting,"
  echo "  or a prerequisite above is missing. This is the failure 'PASSED' cannot show you."
  shortfall=1
fi
if (( groups > MIN_GROUPS || assertions > MIN_ASSERTIONS )) && (( shortfall == 0 )); then
  echo "note: above the floor — raise MIN_GROUPS/MIN_ASSERTIONS in this script to lock the gain in."
fi

# --- verdict ---------------------------------------------------------------
echo
if (( status != 0 )); then
  echo "Failures above. Do not run this on hardware yet."
  exit "$status"
fi
if (( shortfall != 0 || missing != 0 )); then
  echo "Assertions passed, but the run was INCOMPLETE — this is not a green run."
  exit 1
fi
echo "Green: $groups groups, $assertions assertions. Safe to try on hardware."
