"""Motion 32 RGB feedback colors.

Each Motion LED takes a state byte on the base channel (0xB0: off 0 / dim 63 / on 127) plus three
RGB bytes on channels 0xB1/0xB2/0xB3. A ComplexColor with one ColorPart per RGB channel + a
channel-less ColorPart (the state byte) produces exactly that.

Color values and the brightness model are taken from the Studio One integration source
(Motion32Component.js): MotionSharedButtonLEDState kOn=127 / kDimmed=63 / kOff=0; kButtonDefault
#0069CC (blue), kRecordActive red, kStopActive orange, kModifierKey magenta, alt/flash white.
"""

from ableton.v3.control_surface import BasicColors
from ableton.v3.control_surface.elements import ColorPart, ComplexColor, FallbackColor

# The one conversion layer (roadmap Phase 4). Never re-derive `>> 1` here — screen and LED
# colour must come from the same function or they drift.
#
# ⚠️ **`rgb7` is imported deliberately and `test_framework_colours_are_built_from_the_shared_layer`
# requires it**, even though nothing below calls it: the import *is* the assertion that this
# module takes its conversion from `palette` rather than defining one. Do not "clean it up" —
# that was tried on 2026-08-03 and the guard caught it, which is the guard working. (`dim` was
# also imported and was genuinely unused; that one is gone.)
from .palette import live_rgb7, rgb7  # noqa: F401  (see above)

RED_CHANNEL, GREEN_CHANNEL, BLUE_CHANNEL = 1, 2, 3
STATE_ON, STATE_DIM, STATE_OFF = 127, 63, 0


def create_color(red, green, blue, on_value=STATE_ON, fallback=None):
    color = ComplexColor((
        ColorPart(red, channel=RED_CHANNEL),
        ColorPart(green, channel=GREEN_CHANNEL),
        ColorPart(blue, channel=BLUE_CHANNEL),
        ColorPart(on_value),
    ))
    if fallback is not None:
        return FallbackColor(color, fallback)
    return color


# --------------------------------------------------------------------------------------
# Live object colours -> skin colours
#
# The named `Rgb` values below are device *chrome* — transport, modifiers, mode focus — i.e.
# states Live has no colour for. Anything mirroring a Live object (track, clip, scene) must
# use its real colour instead, so a user's arbitrary choice renders without being in a table.
# --------------------------------------------------------------------------------------

_dynamic_cache = {}


def color_from_rgb7(rgb, on_value=STATE_ON):
    """A `ComplexColor` for an already-converted 7-bit triple, memoised.

    Framework colours are compared and re-sent on every layer grab, so building a fresh object
    per repaint would churn allocations on a path that runs often. Keyed by the triple plus the
    state byte, because the same hue at dim and full are different colours to the device.
    """
    key = (tuple(rgb), on_value)
    color = _dynamic_cache.get(key)
    if color is None:
        color = create_color(rgb[0], rgb[1], rgb[2], on_value=on_value)
        _dynamic_cache[key] = color
    return color


def color_from_live(obj, default=None, on_value=STATE_ON):
    """A `ComplexColor` matching a Live object's own colour, or `default` when it has none.

    `default` follows the factory convention where it matters: the Motion greys a slot that is
    present-but-unassigned rather than hiding it, so callers generally want a grey here and not
    `Rgb.OFF`.

    ⚠️ **Nothing calls this yet, and that is not a reason to delete it** — a guard requires it.
    Everything on this surface that currently follows a Live colour (pads, encoder halos, the
    wheel) is driven by `leds.py`, which writes the four raw MIDI messages itself and wants a
    plain triple from `palette.live_rgb7`. This pair is the *skin*-side equivalent, for the
    first framework-owned control that has to wear a track or clip colour — Session mode's clip
    pads being the obvious one. Removing it on 2026-08-03 as "dead" was reverted.
    """
    rgb = live_rgb7(obj)
    if rgb is None:
        return default
    return color_from_rgb7(rgb, on_value=on_value)


class Rgb:
    OFF        = create_color(0, 0, 0, on_value=STATE_OFF, fallback=BasicColors.OFF)
    WHITE      = create_color(127, 127, 127, fallback=BasicColors.ON)          # flash / alt

    # Full vs dim (rest) pairs. Dim = state byte 63, full = 127.
    GREEN      = create_color(0, 127, 0, fallback=BasicColors.ON)
    GREEN_DIM  = create_color(0, 127, 0, on_value=STATE_DIM, fallback=BasicColors.OFF)
    RED        = create_color(127, 0, 0, fallback=BasicColors.ON)              # kRecordActive
    RED_DIM    = create_color(127, 0, 0, on_value=STATE_DIM, fallback=BasicColors.OFF)

    YELLOW     = create_color(127, 127, 0, fallback=BasicColors.ON)           # kChannelSolo
    ORANGE     = create_color(127, 82, 0, fallback=BasicColors.ON)            # kStopActive
    BLUE       = create_color(0, 52, 102, fallback=BasicColors.ON)            # kButtonDefault #0069CC
    # #8A2BE2 blueviolet — the same value as `screen.Palette.KNOB_SONG`, so Shift and the Song
    # halos read as one family. Deliberately NOT `MAGENTA`: side by side on the hardware the
    # factory magenta reads pink rather than purple.
    PURPLE     = create_color(69, 21, 113, fallback=BasicColors.ON)
    # Dim (state 63) variants that stay *lit*, unlike GREEN_DIM/RED_DIM whose dimness means
    # "off". The octave buttons rest here: the factory keeps them at 63 and only goes to 127
    # while the button is physically held, so brightness is press feedback and hue is state.
    BLUE_DIM   = create_color(0, 52, 102, on_value=STATE_DIM, fallback=BasicColors.ON)
    WHITE_DIM  = create_color(127, 127, 127, on_value=STATE_DIM, fallback=BasicColors.ON)
    MAGENTA    = create_color(127, 0, 127, fallback=BasicColors.ON)           # kModifierKey
