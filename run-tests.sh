#!/usr/bin/env bash
#
# The offline suite. No Ableton, no hardware.
#
#   bash run-tests.sh
#
# A green run is 3,999 assertions across 169 groups. Anything less than "every guard ran"
# is a failure, not a pass — see §6b-13: an unrunnable guard used to report success.

set -uo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

fail=0

# --- preconditions ---------------------------------------------------------
# Four guards decompile Live's own framework. Without these two things they cannot run,
# and the suite correctly reports that as failure rather than skipping quietly.

if ! python3 -c "import xdis" 2>/dev/null; then
  echo "WARNING: xdis is not installed — 4 framework guards cannot run."
  echo "  pip3 install xdis --break-system-packages"
  echo
  fail=1
fi

if [[ ! -d "Resources/control_surface" ]]; then
  echo "WARNING: Resources/control_surface/ is absent — 4 framework guards cannot run."
  echo "  Copy ableton/v3/control_surface/ out of your Live 12 installation."
  echo "  (Gitignored on purpose: it is Ableton's proprietary .pyc, not ours to redistribute.)"
  echo
  fail=1
fi

# --- run -------------------------------------------------------------------
python3 tests/test_screen.py
status=$?

echo
if [[ $status -eq 0 && $fail -eq 0 ]]; then
  echo "Green. Safe to try on hardware."
elif [[ $status -eq 0 ]]; then
  echo "Assertions passed, but the framework guards were skipped — this is NOT a full green run."
  exit 1
else
  echo "Failures above. Do not run this on hardware yet."
fi

exit $status
