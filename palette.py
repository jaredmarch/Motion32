"""Colour translation — the single conversion layer between Live and the device.

**One owner.** Every colour that reaches the Motion goes through `rgb7()` here, whether it ends
up as a screen element (`attr 0x01`, three 7-bit bytes) or as an LED/halo/pad RGB triple
(`0xB1`/`0xB2`/`0xB3`, or `0x91`/`0x92`/`0x93` for pads). Screen and LEDs therefore cannot drift
apart, which is the whole point of `Motion32_Build_Roadmap.md` Phase 4. Nothing else in the
package may define its own conversion — `tests/test_screen.py` enforces that.

**No lookup table.** `live_rgb7()` reads an object's *real* `.color` from the LOM and converts it,
so an arbitrary user-chosen track/clip/scene colour renders correctly without appearing in any
map. The named `screen.Palette` values are for device chrome only — transport, mode focus,
dividers — i.e. states Live has no colour for.

Framework-free on purpose: the offline suite can execute this module, so the conversion is tested
by running it rather than by reading it.
"""

from __future__ import annotations

from typing import Any, Optional, Tuple

Rgb7 = Tuple[int, int, int]

# The device takes 7 bits per channel; Live gives 8. See Motion32_Screen_Style_Spec.md §3.
_SHIFT = 1


def rgb7(hex_colour: int) -> Rgb7:
    """0xRRGGBB (8-bit per channel) -> the 7-bit triple the wire takes."""
    return (
        ((hex_colour >> 16) & 0xFF) >> _SHIFT,
        ((hex_colour >> 8) & 0xFF) >> _SHIFT,
        (hex_colour & 0xFF) >> _SHIFT,
    )


def live_rgb7(obj: Any, default: Optional[Rgb7] = None) -> Optional[Rgb7]:
    """The 7-bit colour of a Live object (track / clip / scene), or `default`.

    `track.color`, `clip.color` and `scene.color` are real `0xRRGGBB` ints, so this is the whole
    of "make the device match the laptop screen" — no palette lookup, no nearest-match search.

    Returns `default` when there is nothing to read: no object, no `color` attribute, or a
    `color` of `None` (an uncoloured scene, an empty clip slot). **A colour of `0` is black, not
    missing** — the check is `is None`, deliberately, because `0` is falsy and the obvious
    truthiness test would silently turn every black object into the default.
    """
    if obj is None:
        return default
    try:
        # A Live object that has been deleted raises RuntimeError on *attribute access*, not
        # just on use — so the getattr itself has to be guarded, not only the conversion.
        colour = getattr(obj, "color", None)
    except RuntimeError:
        return default
    if colour is None:
        return default
    try:
        return rgb7(int(colour))
    except (TypeError, ValueError, RuntimeError):
        return default


# Rec. 601 luma weights, ×1000 so the whole thing stays in integers.
_LUMA = (299, 587, 114)
# Half of the 7-bit range. Above this the background is "light".
_LIGHT_THRESHOLD = 63


def luminance(rgb: Rgb7) -> int:
    """Perceived brightness of a 7-bit triple, 0-127."""
    return (_LUMA[0] * rgb[0] + _LUMA[1] * rgb[1] + _LUMA[2] * rgb[2]) // 1000


def text_on(background: Rgb7, light: Rgb7 = (127, 127, 127), dark: Rgb7 = (0, 0, 0)) -> Rgb7:
    """Pick a readable text colour for a background.

    Needed because Live's track colours are user-chosen and include very light ones — pale
    yellow, near-white. Fixed white text on those is unreadable on the device, and the failure
    is silent: the element is drawn, it just cannot be seen. Weighted by perceived brightness
    rather than raw sum, so a saturated blue counts as dark and a mid green counts as light.
    """
    return dark if luminance(background) > _LIGHT_THRESHOLD else light


def darken_under_fixed_light_text(rgb: Rgb7, headroom: float = 0.75) -> Rgb7:
    """Darken a background until **white text drawn by the firmware** reads on it.

    🐛 **For elements whose text colour we cannot set.** `text_on()` is the normal answer to
    Live's user-chosen track colours, half of which are pale — but it needs a `color` attribute
    on the text element to write to. `MIXER_CHANNEL_LABEL` on Template 2 has **only `text`**
    (no `color`, no `visible`), so the firmware picks the colour and it is light. A white or
    pale-yellow track therefore rendered white-on-white: drawn, present, invisible.

    Where the text colour is ours, keep using `text_on` — flipping the *text* preserves the
    track's real colour, which is the point of showing it. This is the fallback for the one
    element that does not offer the choice: keep the hue, lose some brightness.

    `headroom` scales the target below `_LIGHT_THRESHOLD` so the result is comfortably dark
    rather than exactly borderline. A colour already dark enough is returned untouched, so
    ordinary track colours are unaffected.
    """
    luma = luminance(rgb)
    target = _LIGHT_THRESHOLD * headroom
    if luma <= target:
        return rgb
    # Keep a floor so a very light colour becomes a dark tint of itself rather than black —
    # a black swatch would lose the track identity the swatch exists to carry.
    return dim(rgb, target / luma, floor=8)


def dim(rgb: Rgb7, factor: float, floor: int = 0) -> Rgb7:
    """Scale a triple's brightness, keeping its hue.

    For gradients and resting states where the LED's *state* byte isn't the right control —
    pads and halos carry colour and state at the same address, and Studio Pro's key-LED
    gradient is a colour falloff, not a state change (`Motion32_Implementation_Notes.md` §6b-11).

    `floor` keeps a scaled colour visible: Studio Pro never writes state 0 to a halo, so a
    colour that scales to black is usually a bug rather than an intent.
    """
    scaled = []
    for component in rgb:
        value = int(component * factor)
        if component > 0 and value < floor:
            value = floor
        scaled.append(0 if value < 0 else (127 if value > 127 else value))
    return (scaled[0], scaled[1], scaled[2])
