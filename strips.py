"""Touch-strip LED bars — nine LEDs per strip, driven by contact and position.

**The behaviour is the factory's, from the manual** (`Motion32_Pads_Banking_and_Strips.md` §5.3b):

| Strip | Rest | Movement | Release |
|---|---|---|---|
| 1 — pitch | centre LED | follows the finger from centre; jumps to a touch | returns to centre |
| 2 — mod | bottom LED | **fills upward**; jumps to a touch above the bottom | **holds** |

So "grab at the touched position, hold it on release" is not an invention — it is what the hardware
does standalone, and matching it is why the strip feels like the instrument rather than like a
generic fader.

⚠️ **Strip 1 gets touch only, and this is a hard constraint rather than an omission.**
Position arrives as pitch bend, and the 2026-08-10 hardware test established that declaring a
pitch-bend element **consumes** it — strip 2 stopped reaching the armed instrument the moment it was
declared. Strip 1's pitch bend into the instrument is behaviour we want to keep, so we cannot also
read its position. Reading the bar and playing the instrument are mutually exclusive for a given
strip until `ScriptForwarding.non_consuming` is shown to behave differently for pitch bend, which
the bytecode suggests it does not (`forward_midi_pitchbend` never receives `should_consume_event`).

⚠️ **Index mapping is the factory's**, `round((count - 1) * normalized)` (§5.4). Deriving it any
other way puts the lit LED half a step off the finger at the ends, which is exactly where it shows.
"""

import logging
from typing import Optional

from . import midi
from .palette import rgb7

logger = logging.getLogger(__name__)

#: Nine per strip — `midi.CC_TOUCHSTRIP_1_LEDS` / `_2_LEDS`.
LED_COUNT = 9

#: The strip's own blue, `TOUCHSTRIPPRIMARY` `#0069CC` `[SRC]`.
PRIMARY = rgb7(0x0069CC)

#: 14-bit pitch bend, but the low four bits are always zero — the signal is ~10-bit in a 14-bit
#: field (§5.1c, and every value in the 2026-08-10 capture is a multiple of 16).
POSITION_MAX = 16383


def led_index(value: int, count: Optional[int] = None) -> int:
    """Position -> which LED, using the factory's rounding.

    ⚠️ **Module level and self-contained on purpose**, like `sends.page_table`: `strips.py` is
    importable offline, but keeping the rule as a free function means the suite can execute it
    rather than re-implement it. A guard that re-derives the arithmetic tests its own arithmetic.

    ⚠️ **`count` defaults to `None`, not to `LED_COUNT`.** A default of `LED_COUNT` is evaluated
    when the `def` executes, and `_exec_module_function` compiles this node into an empty namespace
    before the suite injects the module constants — so a module-level default raises `NameError`
    the moment the guard lifts it. Resolving inside the body defers the lookup to call time, which
    is after the injection. Same trap will catch any future lifted function with a constant default.
    """
    if count is None:
        count = LED_COUNT
    if count <= 1:
        return 0
    if value <= 0:
        return 0
    if value >= POSITION_MAX:
        return count - 1
    return int(round((count - 1) * (value / POSITION_MAX)))


class TouchStripLeds:
    """One strip's bar. Owns nothing but its own LED group."""

    def __init__(self, leds, fill_from_bottom: bool = True, colour=PRIMARY) -> None:
        self._leds = leds
        self._fill = bool(fill_from_bottom)
        self._colour = colour
        self._index: Optional[int] = None
        self._touched = False

    @property
    def index(self) -> Optional[int]:
        """The lit index, or `None` if the bar has never been driven."""
        return self._index

    @property
    def touched(self) -> bool:
        return self._touched

    def set_touched(self, touched: bool) -> None:
        """Contact opened or closed.

        **Release holds.** Strip 2's bar stays where the finger left it — the manual's word is
        "holds" — so this deliberately does *not* clear. It exists so the strip can light
        differently while in contact later (§5.5), and so a touch with no movement still shows
        something.
        """
        self._touched = bool(touched)
        if self._touched and self._index is None:
            # A tap before any position has arrived: show the bottom, which is strip 2's rest.
            self.set_position(0)

    def set_position(self, value: int) -> None:
        """Drive the bar from a raw 14-bit position."""
        index = led_index(value)
        if index == self._index:
            return
        self._index = index
        self._paint()

    def clear(self) -> None:
        self._index = None
        for i in range(self._leds.count):
            self._leds.set(i, None)

    def _paint(self) -> None:
        index = self._index or 0
        for i in range(self._leds.count):
            lit = (i <= index) if self._fill else (i == index)
            self._leds.set(i, self._colour if lit else None)
