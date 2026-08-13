"""LED groups the framework does not own — encoder halos and pads.

The framework lights buttons through the skin, but nothing binds the **encoder halos** or the
**pads**, so they are ours to drive. Like the screen, writes are cached and diffed: an address
only goes on the wire when its state or colour actually changes, which matters because the
touch highlight, the per-mode colour and the track colour all repaint on every render.

**Two wire formats, one diff.** The only difference between a halo and a pad is the status
byte, so the status set is a parameter rather than a second copy of the cache:

| Group | State | Red | Green | Blue | Addresses |
|---|---|---|---|---|---|
| Encoder halos / wheel | `0xB0` | `0xB1` | `0xB2` | `0xB3` | the encoder's own CC, `0x0E`-`0x15` (the halo has **no address of its own** — `Motion32_Control_Surface_Definition.md` §2.5) |
| Pads | `0x90` | `0x91` | `0x92` | `0x93` | notes `36`-`67`, lane 0 = 36-51, lane 1 = 52-67 |

Pad state additionally accepts **Blink `0x01`** and **Pulse `0x02`** alongside Off/On, which
`set()` passes through unmodified.

Framework-free on purpose, so the offline suite can check the byte stream.
"""

from __future__ import annotations

from typing import Callable, Dict, Optional, Sequence, Tuple

from . import midi

Rgb = Tuple[int, int, int]

#: (state, red, green, blue) status bytes per group.
CC_STATUS = (midi.STATUS_CC, midi.STATUS_CC_RED, midi.STATUS_CC_GREEN, midi.STATUS_CC_BLUE)
NOTE_STATUS = (
    midi.STATUS_NOTE,
    midi.STATUS_NOTE_RED,
    midi.STATUS_NOTE_GREEN,
    midi.STATUS_NOTE_BLUE,
)


def _clamp7(value: int) -> int:
    return 0 if value < 0 else (127 if value > 127 else int(value))


class LedGroup:
    """A cached, diffed set of LED addresses: one brightness + one colour each."""

    def __init__(
        self,
        send: Callable[[Sequence[int]], None],
        addresses: Sequence[int] = midi.CC_ENCODER_HALO,
        status: Sequence[int] = CC_STATUS,
        release_state_repeats: int = 1,
        sends_state: bool = True,
    ) -> None:
        self._send = send
        self._addresses = tuple(addresses)
        self._status = tuple(status)
        #: Whether this group writes the channel-1 **state** byte at all. The halos and pads do;
        #: the touch strips do **not** — §5.4, the shutdown capture shows channels 2/3/4 for the
        #: strip addresses with no state write. Colour alone drives them.
        self._sends_state = bool(sends_state)
        #: How many times `release()` writes the state byte. Pads get **two** — the factory's
        #: state and animation handlers both release the same address, and the shutdown capture
        #: shows both writes (`Motion32_Implementation_Notes.md` §5.1).
        self._release_state_repeats = max(1, int(release_state_repeats))
        self._desired: Dict[int, Tuple[int, Rgb]] = {}
        self._sent: Dict[int, Tuple[int, Rgb]] = {}
        self._suspended = False

    @property
    def count(self) -> int:
        return len(self._addresses)

    def set_suspended(self, suspended: bool) -> None:
        self._suspended = bool(suspended)

    def invalidate(self) -> None:
        """Forget what the device has, so the next flush re-sends every halo."""
        self._sent.clear()

    def forget(self) -> None:
        """Drop both maps without transmitting anything.

        For teardown, where `__init__._clear_all_leds()` already resets every address this
        group owns and `release()` would send them all a second time. Separated from
        `release()` on 2026-08-03 for exactly that reason.
        """
        self._desired.clear()
        self._sent.clear()

    def set(self, index: int, rgb: Optional[Rgb], state: int = midi.LED_ON) -> None:
        """Queue a halo. `rgb=None` turns it off.

        ⚠️ An index outside the group is a **caller** bug — a mismatch between this group's
        address list and whatever is iterating it — so it raises rather than being absorbed.
        It used to return silently, which would have turned "the 33rd pad never lights" into no
        symptom at all until someone counted the pads.
        """
        if not 0 <= index < len(self._addresses):
            raise IndexError(
                f"LED index {index} is outside this group's {len(self._addresses)} addresses"
            )
        if rgb is None:
            self._desired[index] = (midi.LED_OFF, (0, 0, 0))
            return
        self._desired[index] = (
            _clamp7(state),
            (_clamp7(rgb[0]), _clamp7(rgb[1]), _clamp7(rgb[2])),
        )

    def all_off(self) -> None:
        for index in range(len(self._addresses)):
            self.set(index, None)

    def flush(self) -> int:
        """Send changed halos. Returns the number of MIDI messages sent."""
        if self._suspended:
            return 0
        count = 0
        state_status, red_status, green_status, blue_status = self._status
        for index, payload in self._desired.items():
            previous = self._sent.get(index)
            if previous == payload:
                continue
            state, (red, green, blue) = payload
            address = self._addresses[index]
            # State and colour are diffed **separately**. Studio Pro updates a lit pad with
            # colour-only writes and does not re-send the state byte (verified in a
            # track-change capture: channels 2/3/4 only). Re-sending "on" alongside every
            # colour change is both extra traffic and a needless risk of retriggering the
            # device's own state handling.
            if self._sends_state and (previous is None or previous[0] != state):
                self._send((state_status, address, state))
                count += 1
            if previous is None or previous[1] != (red, green, blue):
                self._send((red_status, address, red))
                self._send((green_status, address, green))
                self._send((blue_status, address, blue))
                count += 3
            self._sent[index] = payload
        return count

    def release(self) -> int:
        """Teardown: state off, colour white — the values the factory host sends on exit."""
        count = 0
        state_status, red_status, green_status, blue_status = self._status
        for address in self._addresses:
            for _ in range(self._release_state_repeats):
                self._send((state_status, address, midi.RESET_LED_STATE))
                count += 1
            self._send((red_status, address, midi.RESET_RGB))
            self._send((green_status, address, midi.RESET_RGB))
            self._send((blue_status, address, midi.RESET_RGB))
            count += 3
        self._desired.clear()
        self._sent.clear()
        return count

    def pending_count(self) -> int:
        return sum(1 for k, v in self._desired.items() if self._sent.get(k) != v)


class StripLeds(LedGroup):
    """Nine LEDs on one touch strip. CC-addressed and **colour-only**.

    ⚠️ **No state byte** — `sends_state=False`. §5.4: the shutdown capture shows channels 2/3/4 for
    these addresses with no channel-1 state write, so the factory drives them by colour alone.
    Confirmed on hardware 2026-08-10: with state enabled, MIDI Monitor showed a `Controller 117 127`
    on channel 1 alongside the `0 / 52 / 102` colour triple. The bar lit either way, but sending it
    is a byte Studio Pro never sends, and these addresses do double duty — writing extra bytes to a
    range that overlaps encoder cap-touch is not a risk worth taking for no benefit.

    ⚠️ **Strip 2's addresses collide with encoder cap-touch on input** (`0x70`-`0x77` are encoder
    touch device->host, `0x78` is wheel push in). Direction disambiguates and `midi.py` records it,
    but nothing in the framework will warn you.
    """

    def __init__(self, send, addresses, **k) -> None:
        k.setdefault("sends_state", False)
        super().__init__(send=send, addresses=addresses, status=CC_STATUS, **k)


class EncoderLeds(LedGroup):
    """The 8 encoder halos (and, with other addresses, the wheel halo). CC-addressed."""

    def __init__(
        self,
        send: Callable[[Sequence[int]], None],
        addresses: Sequence[int] = midi.CC_ENCODER_HALO,
    ) -> None:
        super().__init__(send, addresses, status=CC_STATUS)


class PadLeds(LedGroup):
    """The 32 pads. **Note**-addressed, and released with the state byte written twice.

    The double state write is not defensive padding — the factory's state and animation
    handlers own the same address and both release it, and the shutdown capture shows both.
    Matching it keeps our teardown byte-identical to Studio Pro's.
    """

    def __init__(
        self,
        send: Callable[[Sequence[int]], None],
        addresses: Sequence[int] = midi.PAD_NOTES,
    ) -> None:
        super().__init__(send, addresses, status=NOTE_STATUS, release_state_repeats=2)
