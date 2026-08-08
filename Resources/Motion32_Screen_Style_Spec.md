# Motion 32 — Screen Style Spec: text limits, label abbreviation, and the colour palette

**Why this file exists:** the screen map gives *addresses*; the architecture doc gives *when to draw*.
Neither said **how the content should look** — how long text may be, how Fender shortens labels that
don't fit, or what the factory colours actually are. All of it is in the sources and none of it was
documented. This file closes that gap.

Sources: `From Studio Pro/Motion 32.surface.xml` (`$MOTION32_*` / `$MOTIONSHARED_*` defines) and
`From Studio Pro/Motion32Component.js` (`StringFormatter`). Everything here is **[SRC]**.

---

## 1. Text length limits (`MAXCHARS`)

The surface XML pins a hard character budget per text element and pipes **every** string through
`formatFunction_compactify(<limit>)` before sending. Sending longer text is not a protocol error, but
the device will clip or overflow it — the factory never sends more than these:

| Screen element | Constant | Limit |
|---|---|---|
| Encoder label, Template 0 (Main) | `$MOTION32_SCREEN_MAIN_ENCODER_LABEL_CC_ENC_MAXCHARS` | **7** |
| Param value, Template 3 (Params) | `$MOTION32_SCREEN_PARAMS_VALUE_MAXCHARS` | **7** |
| Mixer channel label, Template 2 | `$MOTION32_SCREEN_MIXER_CHANNEL_LABEL_MAXCHARS` | **8** |
| Header title (Main + Params) | `$MOTION32_SCREEN_COMMON_HEADER_TITLE_MAXCHARS` | **13** |
| Menu header button text, Template 1 | `$MOTION32_SCREEN_MENU_HEADER_BUT_TEXT_MAXCHARS` | **16** |
| Param **label**, Template 3 | *(no constant declared)* | we use **10** |
| Params centre bar, Template 3 zone 7 | *(no constant declared)* | we use **20** |

The last two have no factory constant. 10 matches what Studio Pro actually renders in a Template 3
tile label ("Transport", "Position", "Nudge"), and 20 comfortably fits its centre bar
("Song 1 of 1"). The header title's **13** is the reason our Song header reads "Session" /
"Arrangement" rather than "…Mode": `compactify("Arrangement Mode", 13)` yields `ArrangemeMode`.

Note what the budget implies about the design: an encoder tile gets **7 characters** for a parameter
name. Live parameter names are routinely far longer ("Filter Freq", "Delay Feedback"), so the
abbreviation step below is not a nicety — it is load-bearing for the Plugin view.

## 2. `compactify` — the factory label-abbreviation algorithm

`StringFormatter.compactify(input, maxLength)` in `Motion32Component.js`. Ported to Python below,
verbatim in behaviour (including its quirks — e.g. hyphens are stripped *before* anything else, and
vowel removal only applies to single words and never touches the first or last character).

```python
import re

_VOWELS = re.compile(r"[aeiouAEIOU]")
_WS = re.compile(r"\s+")


def compactify(text: str, max_length: int) -> str:
    """Fender/PreSonus label shortening, ported from Motion32Component.js StringFormatter."""
    if not text or max_length <= 0:
        return ""
    if len(text) <= max_length:
        return text

    # 1. hyphens are dropped outright
    s = text.replace("-", "")
    if not s:
        return ""
    if len(s) <= max_length:
        return s

    words = [w for w in _WS.split(s.strip()) if w]

    # 2. multi-word: keep initials, then grow each word round-robin until the budget is spent
    if len(words) > 1:
        if max_length <= len(words):
            return "".join(w[0] for w in words[:max_length])
        take = [1] * len(words)
        remaining = max_length - len(words)
        while remaining > 0:
            advanced = False
            for i, w in enumerate(words):
                if remaining == 0:
                    break
                if take[i] < len(w):
                    take[i] += 1
                    remaining -= 1
                    advanced = True
            if not advanced:
                break
        return "".join(w[:take[i]] for i, w in enumerate(words))

    # 3. single word: strip interior vowels, keeping first and last characters
    base = s
    if len(s) > 2:
        no_vowels = s[0] + _VOWELS.sub("", s[1:-1]) + s[-1]
        if no_vowels:
            base = no_vowels
    if len(base) <= max_length:
        return base

    # 4. last resort: elide the middle, keeping the head and tail
    no_spaces = _WS.sub("", base)
    if len(no_spaces) <= max_length:
        return no_spaces
    half = max_length // 2
    return no_spaces[:half] + no_spaces[len(no_spaces) - (max_length - half):]
```

### 2.1 Verification

The port above was **differentially tested against Fender's own JavaScript**: the real
`StringFormatter` class was extracted verbatim from `Motion32Component.js` and run under Node against
this Python implementation over **315 input/limit combinations** (45 strings × 7 limits, including real
Live parameter and device names, hyphenated names, all-vowel words, multi-space input, single
characters, and limits smaller than the word count). **Every case matched.** Worth re-running if the
port is ever refactored.

Verified output on Live-style names:

| Input | Limit | Result |
|---|---|---|
| `Filter Freq` | 7 | `FiltFre` |
| `Auto Filter` | 7 | `AutoFil` |
| `Delay Feedback Amount` | 7 | `DelFeAm` |
| `Hi-Pass Frequency Cutoff` | 7 | `HiPFrCu` |
| `Frequency` | 7 | `Frqncy` |
| `Resonance` | 7 | `Rsnnce` |
| `Envelope` | 7 | `Envlpe` |
| `Attack` | 7 | `Attack` (fits) |
| `Dry/Wet` | 7 | `Dry/Wet` (fits) |
| `Reverb Send A` | 8 | `ReveSenA` |
| `Lead Synth 2` | 8 | `LeadSyn2` |
| `Drum Rack` | 8 | `DrumRack` |
| `Spectral Resonator` | 8 | `SpecReso` |
| `Glue Compressor` | 13 | `GlueCompresso` |
| `Oscillator Pitch Coarse` | 13 | `OscilPitcCoar` |

Two behaviours worth knowing before you rely on it: **hyphens vanish** (`Hi-Pass` → `HiP…`, and
`Chorus-Ensemble` at 7 becomes `Chrmble`, not `Chor-En`), and **multi-word abbreviation beats vowel
removal** — a two-word name keeps recognisable prefixes, while a single long word gets gutted
(`Operator` at 7 → `Oprtr`). If a label reads badly on the device, prefer renaming the source string
over special-casing the algorithm.

**Build note:** put this in a `formatting.py` (or alongside `display.py`) and route **every** string
through it at the point of the SysEx write, keyed by the element's limit — not at the call sites. That
keeps the "one owner per element" rule intact and makes over-long text structurally impossible.

## 3. Colour palette (factory values, with 7-bit conversions)

Screen colours take `<R> <G> <B>` as three 7-bit bytes (`attr 0x01`); LED/halo/pad colours take the
same three values across status `0xB1/0xB2/0xB3`. Conversion is `v7 = v8 >> 1`.

### 3.1 Screen chrome (Motion 32 specific)

| Constant | Source | Hex | 7-bit R,G,B |
|---|---|---|---|
| `SCREENBACKGROUND` | black | `#000000` | 0, 0, 0 |
| `SCREENHEADERBACKGROUND` | `#0069CC` | `#0069CC` | 0, 52, 102 |
| `SCREENHEADERTITLE` | white | `#FFFFFF` | 127, 127, 127 |
| `SCREENHEADERTEXTDEFAULT` | `#CCCCCC` | `#CCCCCC` | 102, 102, 102 |
| `SCREENHEADERTEXTSELECTED` | white | `#FFFFFF` | 127, 127, 127 |
| `SCREENFOOTERBACKGROUND` | black | `#000000` | 0, 0, 0 |
| `SCREENFOOTERDIVIDER` | `#303336` | `#303336` | 24, 25, 27 |
| `SCREENFOOTERTEXTDEFAULT` | white | `#FFFFFF` | 127, 127, 127 |
| `SCREENFOOTERTEXTSELECTED` | white | `#FFFFFF` | 127, 127, 127 |
| `MENUTEXTDEFAULT` | `#BBBFC3` | `#BBBFC3` | 93, 95, 97 |
| `MENUTEXTSELECTED` | white | `#FFFFFF` | 127, 127, 127 |
| `PARAMSVALUE` | white | `#FFFFFF` | 127, 127, 127 |
| `PARAMSVALUETRIGGERED` | `#0069CC` | `#0069CC` | 0, 52, 102 |
| `PARAMSPLUGINTITLE` | white | `#FFFFFF` | 127, 127, 127 |
| `PARAMSPLUGINTITLEBACKGROUND` | `#303336` | `#303336` | 24, 25, 27 |
| `PARAMSPLUGINVALUE` | white | `#FFFFFF` | 127, 127, 127 |
| `PARAMSPLUGINDISABLED` | `#BBBFC3` | `#BBBFC3` | 93, 95, 97 |

The design language reads clearly: **black canvas, `#0069CC` blue header, white for the selected/active
item, `#BBBFC3` grey for the present-but-inactive one, `#303336` for dividers.**

### 3.2 Buttons, halos, pads (shared across Motion 16/32)

| Constant | Source | Hex | 7-bit R,G,B |
|---|---|---|---|
| `BUTTONDEFAULT` | `#0069CC` | `#0069CC` | 0, 52, 102 |
| `BUTTONSELECTED` | white | `#FFFFFF` | 127, 127, 127 |
| `BUTTONINACTIVE` | `#1c1c1c` | `#1C1C1C` | 14, 14, 14 |
| `BUTTONOFF` | black | `#000000` | 0, 0, 0 |
| `KNOBDEFAULT` | `#0069CC` | `#0069CC` | 0, 52, 102 |
| `KNOBTOUCHED` | white | `#FFFFFF` | 127, 127, 127 |
| `MODIFIERKEY` | magenta | `#FF00FF` | 127, 0, 127 |
| `RECORDACTIVE` | red | `#FF0000` | 127, 0, 0 |
| `STOPACTIVE` | orange | `#FFA500` | 127, 82, 0 |
| `TRANSPORTALTBUTTON` | white | `#FFFFFF` | 127, 127, 127 |
| `CHANNELSOLO` | yellow | `#FFFF00` | 127, 127, 0 |
| `CHANNELMUTE` | red | `#FF0000` | 127, 0, 0 |
| `CHANNELLABELBACKGROUNDDEFAULT` | `#000000` | `#000000` | 0, 0, 0 |
| `CHANNELLABELBACKGROUNDSELECTED` | `#0069CC` | `#0069CC` | 0, 52, 102 |
| `CONTROLLINKGLOBALASSIGNED` | `#4fd3ff` | `#4FD3FF` | 39, 105, 127 |
| `CONTROLLINKFOCUSASSIGNED` | `#fcca03` | `#FCCA03` | 126, 101, 1 |
| `TOUCHSTRIPPRIMARY` | `#0069CC` | `#0069CC` | 0, 52, 102 |
| `TOUCHSTRIPSECONDARY` | orange | `#FFA500` | 127, 82, 0 |
| `OCTAVEDEFAULT` | `#0069CC` | `#0069CC` | 0, 52, 102 |
| `OCTAVESHIFT` | white | `#FFFFFF` | 127, 127, 127 |
| `PADCOMMAND` | white | `#FFFFFF` | 127, 127, 127 |
| `VELOCITYTOGGLEACTIVE` | red | `#FF0000` | 127, 0, 0 |
| `LAUNCHERMENU` | `#562157` | `#562157` | 43, 16, 43 |
| `BUTTONUSERMODEACTIVE` / `BUTTONUSERCOMMANDACTIVE` | `#0069CC` | `#0069CC` | 0, 52, 102 |
| `BUTTONUSERMODEINACTIVE` / `BUTTONUSERCOMMANDINACTIVE` | `#BBBFC3` | `#BBBFC3` | 93, 95, 97 |
| `USERCOMMANDASSIGNED` | white | `#FFFFFF` | 127, 127, 127 |
| `USERCOMMANDUNASSIGNED` | `#BBBFC3` | `#BBBFC3` | 93, 95, 97 |
| `SPLASHSCREENWARNINGBACKGROUND` | red | `#FF0000` | 127, 0, 0 |

Cross-check: the build's existing `colors.py` derives `ORANGE = (127, 82, 0)` and
`BLUE = (0, 52, 102)` — both match the factory values exactly. Confirmed, no change needed.

### 3.3 Meaningful pairs
Two conventions worth adopting wholesale, because they are what makes the device read correctly:

- **Assigned vs unassigned:** white text = assigned/active; `#BBBFC3` = present but unassigned. The
  factory never hides an unassigned slot, it greys it.
- **Control-Link scope colour:** `#4fd3ff` cyan = a **global** assignment, `#fcca03` amber = a
  **focus** (per-plugin) assignment. This is a two-colour scope language on the encoder halos that
  we get for free — see `Motion32_ControlLink_and_User_Mode.md`.

## 4. Roadmap tie-in
This file supplies Phase 2 (screen engine) and Phase 4 (colour system) with the values they need.
Phase 4's "define our own palette only for non-Live UI states" now has a factory baseline to start
from rather than Atom SQ approximations.
