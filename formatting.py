"""Text preparation for the Motion 32 screen.

The device's screen elements have hard character budgets, and the factory
integration never sends a raw string — every label goes through Fender's own
abbreviation function first. An encoder tile gets **7 characters**, so this is
load-bearing for the Plugin view, not cosmetic.

`compactify` below is a port of `StringFormatter.compactify` from the reference
`Motion32Component.js`. It was differentially tested against that JavaScript over
315 input/limit combinations (real Live parameter/device names, hyphenated names,
all-vowel words, multi-space input, single characters, and limits smaller than the
word count) — every case matched. See Motion32_Screen_Style_Spec.md §2.

Behaviour worth knowing: hyphens are removed outright, multi-word names keep
recognisable per-word prefixes, and single long words get their interior vowels
stripped (`Operator` -> `Oprtr`). If a label reads badly on the device, rename the
source string rather than special-casing the algorithm.
"""

from __future__ import annotations

import re

# Character budgets, from $MOTION32_SCREEN_*_MAXCHARS in Motion 32.surface.xml.
MAXCHARS_ENCODER_LABEL = 7
MAXCHARS_MIXER_CHANNEL = 8
MAXCHARS_HEADER_TITLE = 13

# Template 0's header title, when we use the *whole* width. Fender's 13 keeps the title inside
# the left half of the header — the right half belongs to the top soft-button labels. With
# those blank (Plugin mode claims none) the full width is free, so "Track | Device" fits.
MAXCHARS_HEADER_TITLE_WIDE = 26
MAXCHARS_MENU_BUTTON = 16

# Template 3's tile *label* has no MAXCHARS constant in the surface XML — only its value
# does. 10 matches what the factory actually renders there (the Song screen shows
# "Transport", "Position", "Nudge").
MAXCHARS_PARAMS_LABEL = 10

# The value *line* on Template 3. Fender's own `$MOTION32_SCREEN_PARAMS_VALUE_MAXCHARS` is 7,
# but that is the target it compacts **numeric** values to, not a device limit: its own Song
# screen renders "Timeline" (8) in this element. 9 fits a two-word hint like "Prev/Next" while
# staying close to what the factory is known to display. Numeric readouts are far shorter, so
# this only affects hints. (The unused `MAXCHARS_PARAMS_VALUE = 7` constant that recorded
# Fender's figure was removed 2026-08-03 — nothing read it, and it invited being used as if it
# were the element's real budget.)
MAXCHARS_PARAMS_VALUE_LINE = 9

# The grey centre bar on Template 3. Also undeclared; the factory shows "Song 1 of 1".
MAXCHARS_PARAMS_TITLE = 20

# The factory has no explicit constant for the 8 soft-button labels; the Menu
# template's header buttons allow 16, but the Main template's label zones are
# visually narrow. 8 matches the mixer channel label width and reads correctly.
MAXCHARS_SOFT_BUTTON = 8

_VOWELS = re.compile(r"[aeiouAEIOU]")
_WHITESPACE = re.compile(r"\s+")


def compactify(text: str, max_length: int) -> str:
    """Shorten `text` to `max_length` the way the factory integration does."""
    if not text or max_length <= 0:
        return ""
    if len(text) <= max_length:
        return text

    # 1. hyphens are dropped outright
    stripped = text.replace("-", "")
    if not stripped:
        return ""
    if len(stripped) <= max_length:
        return stripped

    words = [w for w in _WHITESPACE.split(stripped.strip()) if w]

    # 2. multi-word: start from initials, then grow each word round-robin
    if len(words) > 1:
        if max_length <= len(words):
            return "".join(word[0] for word in words[:max_length])
        take = [1] * len(words)
        remaining = max_length - len(words)
        while remaining > 0:
            advanced = False
            for index, word in enumerate(words):
                if remaining == 0:
                    break
                if take[index] < len(word):
                    take[index] += 1
                    remaining -= 1
                    advanced = True
            if not advanced:
                break
        return "".join(word[: take[index]] for index, word in enumerate(words))

    # 3. single word: strip interior vowels, keeping the first and last characters
    base = stripped
    if len(stripped) > 2:
        without_vowels = stripped[0] + _VOWELS.sub("", stripped[1:-1]) + stripped[-1]
        if without_vowels:
            base = without_vowels
    if len(base) <= max_length:
        return base

    # 4. last resort: elide the middle, keeping head and tail
    no_spaces = _WHITESPACE.sub("", base)
    if len(no_spaces) <= max_length:
        return no_spaces
    half = max_length // 2
    return no_spaces[:half] + no_spaces[len(no_spaces) - (max_length - half) :]


# The screen takes 7-bit ASCII. Anything outside the printable range is replaced
# rather than dropped, so a stray character can't silently shorten a label or push
# a non-7-bit byte onto the wire (which would corrupt the SysEx frame).
_PRINTABLE_MIN = 0x20
_PRINTABLE_MAX = 0x7E


def to_ascii_bytes(text: str, max_length: int) -> tuple:
    """Compactify, then encode to a tuple of 7-bit printable ASCII bytes."""
    compact = compactify(text or "", max_length)
    out = []
    for char in compact:
        code = ord(char)
        out.append(code if _PRINTABLE_MIN <= code <= _PRINTABLE_MAX else ord("?"))
    return tuple(out)


#: Most decimal places a numeric reading keeps once it has to be shortened.
#:
#: Live hands out more precision than any element here can show — a mixer volume arrives as
#: `-12.345 dB` — and the extra digits are the cheapest thing on the string to spend. Two is
#: what Live's own mixer displays (user, 2026-08-03).
MAX_VALUE_DECIMALS = 2

#: A reading that starts with a number: `-12.345 dB`, `440 Hz`, `0.00 %`, `127`.
#: Anything else (`-inf dB`, `Sine Wave`, `On`) has no number to round and falls through.
_NUMERIC_VALUE = re.compile(r"^([+-]?\d+(?:\.\d+)?)\s*(.*)$")


def _with_decimals(number: str, decimals: int) -> str:
    try:
        value = float(number)
    except ValueError:
        return number
    if decimals <= 0:
        return str(int(round(value)))
    return f"{value:.{decimals}f}"


def truncate_value(text: str, max_length: int) -> str:
    """Fit a parameter *value* into `max_length` without corrupting it.

    Deliberately NOT `compactify`. The factory pipes values through compactify too, but
    compactify's first move is to strip hyphens — which turns "-12.5 dB" into "12.5 dB"
    and silently flips the sign. For a value display that is a correctness bug, not a
    cosmetic one.

    🔑 **The unit is the LAST thing to go, not the first.** This used to drop it immediately —
    `"-12.00 dB"` became `"-12.00"` — which on the mixer meant every level below -10 dB lost its
    unit while every level above it kept one. A column of readings where the unit comes and goes
    with the value reads as a bug, and `-70.00` with no unit is genuinely ambiguous.

    So the string is now tightened in the order a person would, spending precision and then
    whitespace before ever touching the unit:

        1. leave it alone if it already fits
        2. round to MAX_VALUE_DECIMALS  ->  "-12.35 dB"
        3. close up the space           ->  "-12.35dB"
        4. one decimal, then none       ->  "-12.3dB", "-12dB"
        5. only now, drop the unit      ->  "-12.35"

    ⚠️ **Step 3 is the one that actually saves the mixer.** The strip label's budget is 8 and
    Live already sends two decimals, so `"-12.00 dB"` (9) is over by exactly the space. Rounding
    alone would not have fixed anything.

        budget 8   "-12.00 dB" -> "-12.00dB"     "-6.00 dB" -> "-6.00 dB"
                   "-12.345 dB" -> "-12.35dB"    "-inf dB"  -> "-inf dB"
        budget 7   "-6.00 dB"  -> "-6.00dB"      "Sine Wave" -> "Sine"
    """
    text = (text or "").strip()
    if not text or max_length <= 0:
        return ""
    if len(text) <= max_length:
        return text

    match = _NUMERIC_VALUE.match(text)
    unit = match.group(2).strip() if match else ""
    if match and unit:
        number = match.group(1)
        for decimals in range(MAX_VALUE_DECIMALS, -1, -1):
            rounded = _with_decimals(number, decimals)
            for gap in (" ", ""):
                candidate = f"{rounded}{gap}{unit}"
                if len(candidate) <= max_length:
                    return candidate
        # The unit genuinely cannot fit alongside any rounding of the number. Keep the number:
        # a wrong-looking magnitude is worse than a missing unit.
        return _with_decimals(number, MAX_VALUE_DECIMALS)[:max_length]

    # No number to round — keep the leading token, then hard-trim.
    head = text.split(" ", 1)[0]
    if len(head) <= max_length:
        return head
    return head[:max_length]


def format_parameter_value(parameter) -> str:
    """Best-effort display string for a Live device parameter.

    Live gives a nicely formatted string via `str(parameter)` (e.g. "-6.0 dB",
    "440 Hz", "On"), which is what we want on screen. Falls back to the raw value.
    """
    try:
        text = str(parameter)
    except Exception:
        text = ""
    if text:
        return text
    try:
        return f"{parameter.value:.2f}"
    except Exception:
        return ""
