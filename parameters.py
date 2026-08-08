"""Which 8 Live parameters the encoders control — and therefore what the screen shows.

**Pinned against the real framework** (decompiled from Live 12's
`ableton/v3/control_surface/components/device.pyc`), so this is no longer guesswork:

* `DeviceComponent.parameters` -> `self._provided_parameters`, and it is a
  **`listenable_property`** — `_update_parameters()` calls `self.notify_parameters()`.
  That gives us a public change signal, which is what makes bank switching safe: the
  screen re-reads its labels whenever the mapped set changes, not only when the device
  changes.
* The list holds **`ParameterInfo`** objects, not raw Live parameters:
  `ParameterInfo(parameter=..., name=...)`, subclassing `v2`'s `ParameterInfoBase`.
  Reading `.min`/`.value` straight off one silently yields nothing — the label must come
  from `info.name` and the value from `info.parameter`. Using `info.name` is also
  *better* than `parameter.name`, because Live's curated bank definitions rename
  parameters per bank and `info.name` carries that name.
* `DeviceComponent.bank_name` / `.bank_index` expose the current bank, so the screen can
  show Live's real bank name instead of a synthetic "n/m" counter.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Optional

PARAMETERS_PER_BANK = 8


@dataclass(frozen=True)
class ParameterEntry:
    """One encoder slot. `parameter` is None when the slot is unassigned."""

    name: str = ""
    parameter: Optional[Any] = None

    @property
    def assigned(self) -> bool:
        return self.parameter is not None


EMPTY_ENTRY = ParameterEntry()


def _liveobj_valid(obj: Any) -> bool:
    """Live objects can outlive their C++ counterpart; touching a dead one raises."""
    if obj is None:
        return False
    try:
        obj.name  # probe
        return True
    except (RuntimeError, AttributeError):
        return False


def _as_entry(item: Any) -> ParameterEntry:
    """Normalise one element of `DeviceComponent.parameters` into an entry.

    Handles the documented `ParameterInfo` shape first, then degrades gracefully: a raw
    Live parameter (has `.value`) is accepted directly, and anything else becomes an
    unassigned slot rather than raising inside a listener.
    """
    if item is None:
        return EMPTY_ENTRY

    parameter = getattr(item, "parameter", None)
    if parameter is not None:
        name = getattr(item, "name", None) or getattr(parameter, "name", "") or ""
        if not _liveobj_valid(parameter):
            return ParameterEntry(name=str(name), parameter=None)
        return ParameterEntry(name=str(name), parameter=parameter)

    # Not a ParameterInfo — maybe a bare Live parameter.
    if hasattr(item, "value") and _liveobj_valid(item):
        return ParameterEntry(name=str(getattr(item, "name", "") or ""), parameter=item)

    return EMPTY_ENTRY


class ParameterSource:
    """Reads the framework Device component's current parameter bank."""

    #: How many read failures to log before going quiet. `entries()` runs on every repaint, so
    #: an unbounded log would flood; one line is enough to name the cause, and the count on the
    #: last one says it is still happening.
    MAX_LOGGED_READ_FAILURES = 3

    def __init__(self, log=None) -> None:
        self._log = log or (lambda _message: None)
        self._component = None
        self._read_failures = 0

    def _note_read_failure(self, what: str, error: BaseException) -> None:
        """Say that a read failed, without flooding.

        ⚠️ **The guards in this class exist to stop a framework crash wedging the surface, not
        to hide it.** The one that actually fires is
        `banking_util._get_parameters_for_bank_index`, which raises `IndexError` for Max for
        Live devices declaring bank indices beyond their own parameter list — entirely
        framework code, and nothing we can fix. Absorbing it is right. Absorbing it *silently*
        was not: it presented on hardware as all eight Plugin tiles going blank with nothing in
        `Log.txt` to explain it. Fixed 2026-08-03.
        """
        self._read_failures += 1
        if self._read_failures <= self.MAX_LOGGED_READ_FAILURES:
            self._log(
                f"Motion32: could not read {what} from the Device component "
                f"({type(error).__name__}: {error}) — the encoder tiles will be empty. "
                f"An IndexError here is a known Max for Live / framework bug, not ours."
            )
            if self._read_failures == self.MAX_LOGGED_READ_FAILURES:
                self._log("Motion32: further Device read failures will not be logged")

    def bind_device_component(self, component) -> None:
        self._component = component
        if component is None:
            self._log(
                "Motion32 WARNING: no Device component found; encoder labels will be empty"
            )
        else:
            self._log(
                f"Motion32: reading encoder parameters from {type(component).__name__}.parameters"
            )

    @property
    def component(self):
        """The Device component — the subject to listen to for `parameters` changes."""
        return self._component

    def entries(self) -> List[ParameterEntry]:
        """Exactly PARAMETERS_PER_BANK entries; unassigned slots are empty.

        The `except` absorbs a framework crash rather than letting it wedge the surface — see
        `_note_read_failure` for which crash, and for why it now says so in the log.
        """
        raw: List[Any] = []
        if self._component is not None:
            try:
                raw = list(self._component.parameters or [])
            except Exception as error:
                self._note_read_failure("the mapped parameters", error)
                raw = []

        entries = [_as_entry(item) for item in raw[:PARAMETERS_PER_BANK]]
        entries += [EMPTY_ENTRY] * (PARAMETERS_PER_BANK - len(entries))
        return entries

    def bank_label(self) -> str:
        """Live's own name for the current bank, e.g. "Filter". Empty if unavailable."""
        if self._component is None:
            return ""
        try:
            return str(self._component.bank_name or "")
        except Exception as error:
            self._note_read_failure("the bank name", error)
            return ""

    def device(self):
        """The device the framework currently has in focus.

        Preferred over reading `song.appointed_device` ourselves: this is by definition
        the device whose parameters the encoders are mapped to, so the screen cannot
        disagree with the knobs.
        """
        if self._component is None:
            return None
        try:
            device = self._component.device
        except Exception as error:
            self._note_read_failure("the focused device", error)
            return None
        return device if _liveobj_valid(device) else None
