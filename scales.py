"""The scale engine — the 15 factory scales, and the two pad layouts Scale mode offers.

**Framework-free on purpose**, like `pads.py` and `palette.py`, so the offline suite can *execute*
every layout rather than parse it. The musical invariants below are checked by running them across
all 15 scales × 12 roots × the full octave range, which is the only way to be sure of a claim like
"duplicates are impossible".

The table is machine-decoded from the factory's own `From Studio Pro/Musical Scales/*.musicalscale`
files and matches the SDK's `PreSonus.MusicalScaleID` enum exactly and in order
(`Motion32_Scale_and_Chord_Engine.md` §4). Degrees are semitone offsets from the root.

---

**Two layouts, and they are the `Lock` / `Guide` soft buttons** (user, 2026-08-03). The factory
names them but never defines them; these are the agreed meanings:

* **`Lock` — the default.** One row. The bottom lane is 16 **consecutive ascending scale degrees**
  and the top lane is entirely dead, which is what the factory does (§5.3c). Only scale notes are
  reachable at all.
* **`Guide`.** Both rows, back to the ordinary piano layout — but scale notes at **full
  brightness** and everything else **much dimmer**. The scale guides rather than constrains.

🔑 **`Lock` is what makes duplicate pitches impossible**, and that is the whole reason the factory
collapses to one lane. 16 consecutive degrees ascend strictly, so no two pads can sound the same
note. The naive two-lane pentatonic that produced fifteen collisions was solving a problem the
factory does not have. `Guide` cannot collide either, because it *is* the piano layout, which is
already strictly ascending.

⚠️ **`Guide` is a lighting change, not a layout change.** It returns exactly `pads.pad_pitches()` —
the same list the keyboard already plays. Only the *roles* differ, so nothing about note
translation, dead pads or held-pad feedback needs a second code path. Resist the temptation to
generate its pitches here.

---

⚠️ **`pads.py` does not generalise to scales and must not be bent into doing so**
(`Motion32_Scale_and_Chord_Engine.md` §5.3b). It is diatomic to the bone: `WHITE_KEY_SEMITONES` is
7 per octave, `% 7` for roots and octaves, and `NO_BLACK_KEY_ABOVE` is a property of *this* scale
only. A pentatonic has 5 degrees, blues 6, chromatic 12 — the period is the scale's length. So this
is a **different generator**, and the two-lane piano stays one implementation of the interface
rather than the interface itself.

**The property both share, and the one that matters:** a layout returns *pitches or `None`*, and
every other behaviour — silence, darkness, translation, press feedback — is derived from that one
answer. Nothing else may form a second opinion about which pads are playable.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence, Tuple

from . import pads

#: Scale id -> (name, semitone degrees). Indices are `PreSonus.MusicalScaleID`; do not renumber.
SCALES: Dict[int, Tuple[str, Tuple[int, ...]]] = {
    0: ("Chromatic", (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)),
    1: ("Major", (0, 2, 4, 5, 7, 9, 11)),
    2: ("Melodic Minor", (0, 2, 3, 5, 7, 9, 11)),
    3: ("Harmonic Minor", (0, 2, 3, 5, 7, 8, 11)),
    4: ("Natural Minor", (0, 2, 3, 5, 7, 8, 10)),
    5: ("Major Pentatonic", (0, 2, 4, 7, 9)),
    6: ("Minor Pentatonic", (0, 3, 5, 7, 10)),
    7: ("Blues", (0, 3, 5, 6, 7, 10)),
    8: ("Dorian", (0, 2, 3, 5, 7, 9, 10)),
    9: ("Phrygian", (0, 1, 3, 5, 7, 8, 10)),
    10: ("Lydian", (0, 2, 4, 6, 7, 9, 11)),
    11: ("Mixolydian", (0, 2, 4, 5, 7, 9, 10)),
    12: ("Locrian", (0, 1, 3, 5, 6, 8, 10)),
    13: ("Major Triad", (0, 4, 7)),
    14: ("Minor Triad", (0, 3, 7)),
}

DEFAULT_SCALE_ID = 1  # Major
CHROMATIC_ID = 0

#: The two menu categories the factory's soft buttons select, from
#: `Motion32_State_Trace_Table.md` §Scale: *"soft buttons pick Main/Modes/Key + Guide/Lock"*.
#:
#: `Modes` is the church-mode block, which the firmware carries as its own contiguous run of
#: strings — `Ionian · Dorian · Phrygian · Lydian · Mixolydian · Aeolian · Locrian`. Two of those
#: are **aliases** rather than extra scales: `initSupportedScales` adds `kIonian → kMajor` and
#: `kAeolian → kNaturalMinor`, which is why Studio Pro shows more menu entries than there are
#: scales (§4).
#:
#: 🔑 **Chromatic is deliberately not a menu entry** (user, 2026-08-03): *"there is no chromatic
#: mode because the standard pad layout is chromatic."* Leaving Scale mode **is** selecting
#: chromatic, so offering it in the list would be a second way to say the same thing — and a
#: confusing one, because it would put the pads on one lane of consecutive semitones rather than
#: back on the piano.
#:
#: 🔑 **The two triads are out as well** (user, 2026-08-03): *"triads are specifically part of the
#: chords implementation."* Musically that is plainly right — `Major Triad` is `(0, 4, 7)`, and
#: stretching three notes across sixteen pads spans **60 semitones**, five octaves, which is a
#: chord voicing table rather than a scale. The firmware agrees about where they belong: `Triad`,
#: `Sus2`, `Sus4` and `Add 7` sit in the *chord* string block, next to `Chords/Intervals` and
#: `Progressions`, not with the scale names.
#:
#: ⚠️ **This is a deliberate divergence from the factory, and the entry count says so.** Studio
#: Pro's 16 entries are the 14 non-chromatic scales plus the Ionian and Aeolian aliases — the
#: triads included. Ours is 7 Main + 7 Modes = **14**. Recorded because an earlier note in this
#: file claimed 9 + 7 = 16 "matches the factory": that was true only while the triads were listed
#: as scales, and it is no longer the reason to trust the split.
#:
#: `SCALES` still holds all fifteen. Chromatic is the fallback for an unknown id (the factory's
#: own behaviour for an unrecognised title) and the triads are what Phase 11's Chord engine will
#: read its interval sets from. Neither is *offered*.
MAIN_IDS: Tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7)
MODE_ENTRIES: Tuple[Tuple[str, int], ...] = (
    ("Ionian", 1),        # alias of Major
    ("Dorian", 8),
    ("Phrygian", 9),
    ("Lydian", 10),
    ("Mixolydian", 11),
    ("Aeolian", 4),       # alias of Natural Minor
    ("Locrian", 12),
)

CATEGORY_MAIN = "Main"
CATEGORY_MODES = "Modes"
CATEGORY_KEY = "Key"
CATEGORIES = (CATEGORY_MAIN, CATEGORY_MODES, CATEGORY_KEY)

#: Note names for the 12 roots. Sharps rather than flats, matching Live's own chooser.
ROOT_NAMES: Tuple[str, ...] = (
    "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",
)

#: Our scale names -> Live's `song.scale_name` vocabulary.
#:
#: ⚠️ **`song.scale_name` is writable but takes Live's spelling, not ours.** Both tables are real
#: and they disagree: we inherited the Motion's names from the factory `.musicalscale` files, and
#: Live has its own chooser list. Writing a name Live does not recognise is silently ignored — no
#: raise, no log — which is the same class of failure as an unknown Layer control name, so the
#: translation is explicit and guarded rather than hopeful.
#:
#: A name absent from this map means "do not write" rather than "write it anyway and hope".
LIVE_SCALE_NAMES: Dict[str, str] = {
    "Chromatic": "Chromatic",
    "Major": "Major",
    "Melodic Minor": "Melodic Minor",
    "Harmonic Minor": "Harmonic Minor",
    "Natural Minor": "Minor",
    "Major Pentatonic": "Major Pentatonic",
    "Minor Pentatonic": "Minor Pentatonic",
    "Blues": "Blues",
    "Dorian": "Dorian",
    "Phrygian": "Phrygian",
    "Lydian": "Lydian",
    "Mixolydian": "Mixolydian",
    "Locrian": "Locrian",
    # ⚠️ The two triads have no counterpart in Live's scale chooser — they are pad layouts rather
    # than scales, and the factory offers them as such. Absent on purpose: the Motion still lays
    # its pads out from them, it simply does not push a meaningless name at the song.
}

#: Pad role for a note that is playable but **outside** the current scale. Only `Guide` produces
#: it; `Lock` has no out-of-scale pads to mark, because it has no out-of-scale pads.
OUT_OF_SCALE = "out"


def scale_name(scale_id: int) -> str:
    return SCALES.get(scale_id, SCALES[CHROMATIC_ID])[0]


def scale_degrees(scale_id: int) -> Tuple[int, ...]:
    """The semitone offsets of `scale_id`, falling back to Chromatic.

    Chromatic is the factory's own fallback for an unrecognised title (§4), and it is the right
    one here too: every note is in a chromatic scale, so a bad id degrades to "no filtering"
    rather than to an empty keybed.
    """
    return SCALES.get(scale_id, SCALES[CHROMATIC_ID])[1]


def pitch_classes(scale_id: int, root: int) -> frozenset:
    """The 12-tone pitch classes `scale_id` contains when rooted at `root`."""
    return frozenset((root + degree) % 12 for degree in scale_degrees(scale_id))


def menu_entries(category: str) -> Tuple[Tuple[str, int], ...]:
    """`(label, id)` rows for a menu category — what the wheel scrolls and the list draws.

    `Key` returns the twelve roots with the root number as the id, so a caller can treat every
    category the same way: a list of labelled ids, scrolled by one control.
    """
    if category == CATEGORY_MODES:
        return MODE_ENTRIES
    if category == CATEGORY_KEY:
        return tuple((name, index) for index, name in enumerate(ROOT_NAMES))
    return tuple((SCALES[i][0], i) for i in MAIN_IDS)


def locked_pitches(
    scale_id: int, root: int, octave_semitones: int = 0, degree_offset: int = 0
) -> List[Optional[int]]:
    """**`Lock`** — 16 consecutive ascending degrees on the bottom lane, top lane dead.

    `root` is a pitch class 0-11; `octave_semitones` is Octave ±; `degree_offset` is what A–H
    moves, in **scale degrees** — the same unit `keyboard.DEGREES_PER_BANK_STEP` already converts
    A–H presses into, so the one radio serves this layout and the piano without a mode-dependent
    handler.

    🔑 **Strictly ascending, therefore no duplicates.** Degree `i` is unambiguously
    `octave(i) * 12 + interval(i)`, and both terms are non-decreasing, so pad *n+1* is always
    higher than pad *n*. That is the property the factory's one-lane collapse buys, and it holds
    for every scale length — 3 for the triads, 12 for chromatic.

    The base octave is C1 = 36, matching `pads.LANE_0_FIRST_NOTE`, so a scale rooted at C with no
    transposition starts on the same note the piano layout does.
    """
    degrees = scale_degrees(scale_id)
    period = len(degrees)
    pitches: List[Optional[int]] = []
    for index in range(pads.PADS_PER_LANE):
        step = index + int(degree_offset)
        # divmod handles negative offsets correctly — `divmod(-1, 7) == (-1, 6)` — which is what
        # lets A–H walk the window *below* the root without a special case. Same reasoning as
        # `pads.white_key_semitone`.
        octave, degree = divmod(step, period)
        pitch = (
            pads.LANE_0_FIRST_NOTE
            + (root % 12)
            + 12 * octave
            + degrees[degree]
            + int(octave_semitones)
        )
        pitches.append(pitch if 0 <= pitch < 128 else None)
    # ⚠️ The top lane is dead, and it is dead by being `None` rather than by any separate flag.
    # `keyboard._is_dead` is `pitches[i] is None`, so every dead-pad behaviour — identity
    # translation on its own channel, `listenable` mode, no LED, no held state — follows without
    # a line of new code. That is the interface working as intended.
    return pitches + [None] * pads.PADS_PER_LANE


def locked_roles(pitches: Sequence[Optional[int]], root: int) -> List[str]:
    """Roles for the `Lock` layout: tonics tinted, other degrees plain, dead pads absent.

    Derived from the **pitch list**, never from the offsets that produced it — the same rule
    `pads.roles_for_pitches` follows, and for the same reason: the lights and the notes must come
    from one list so they cannot disagree about what the keybed is playing.
    """
    roles: List[str] = []
    for pitch in pitches:
        if pitch is None:
            roles.append(pads.ABSENT)
        elif pitch % 12 == root % 12:
            roles.append(pads.ROOT)
        else:
            roles.append(pads.KEY)
    return roles


def guide_roles(
    pitches: Sequence[Optional[int]], scale_id: int, root: int
) -> List[str]:
    """Roles for the **`Guide`** layout: the piano, with out-of-scale notes marked.

    The caller passes `pads.pad_pitches(...)` — the *unchanged* keyboard layout. Guide never
    generates its own pitches, so both rows keep playing exactly what they played before; only
    the lighting says which notes belong to the scale.

    Four roles: `ABSENT` for the four piano gaps, `ROOT` for the tonic, `KEY` for an in-scale
    note at full brightness, and `OUT_OF_SCALE` for everything else — which the renderer dims
    hard rather than darkening, because these pads still play.
    """
    members = pitch_classes(scale_id, root)
    roles: List[str] = []
    for pitch in pitches:
        if pitch is None:
            roles.append(pads.ABSENT)
        elif pitch % 12 == root % 12:
            roles.append(pads.ROOT)
        elif pitch % 12 in members:
            roles.append(pads.KEY)
        else:
            roles.append(OUT_OF_SCALE)
    return roles


def safe_octave_range(scale_id: int, root: int, degree_offset: int = 0) -> Tuple[int, int]:
    """The transposition range that keeps every *playable* pad inside MIDI 0-127.

    The same job `pads.safe_semitone_range` does for the piano, and needed for the same reason:
    a scale's span varies enormously — Major covers 26 semitones across the 16 pads, the
    pentatonics 36, and the triad layouts **60** — so a fixed ±3 octaves is meaningless here.
    A triad layout is already most of the keyboard before Octave touches it.
    """
    base = [p for p in locked_pitches(scale_id, root, 0, degree_offset)[: pads.PADS_PER_LANE]
            if p is not None]
    if not base:
        return (0, 0)
    return (-min(base), 127 - max(base))
