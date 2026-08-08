"""The Motion 32 pad layout — which pad is which key, and which pads are not keys at all.

**Reconstructed from a Studio Pro track-change capture (2026-07-25)**, and every prediction
below was checked against it before this file was written:

```
Note On  ch2/3/4  C1 (36)   127, 21, 21     <- root, in the track's colour
Note On  ch2/3/4  C#1 (37)  127,127,127     <- an ordinary key, white
...
Note Off ch1/2/3/4  F#2 (54)  0             <- dark: there is no black key above E
```

The layout is a **piano**, not a chromatic grid:

* **Bottom lane, notes 36-51** — 16 **white** keys: C D E F G A B C D E F G A B C D.
* **Top lane, notes 52-67** — the **black** key sitting above each white key, and **dark where
  no black key exists** (above E and above B). That is why four top-lane pads are unlit.

Confirmed addresses from the capture:

| | Predicted | In the capture |
|---|---|---|
| Root pads (the C's — `pitch % 12 == 0`) | 36, 43, 50 | C1, G1, D2 — the three tinted pads |
| Absent black keys (white index % 7 in {2, 6}) | 54, 58, 61, 65 | F#2, A#2, C#3, F3 — the four zeroed pads |

⚠️ **That capture was taken at bank E, and two of the numbers above are frame-ambiguous there.**
At rest the C's sit on pads 1, 8 and 15, so "the roots are `index % 7 == 0`" and "the roots are the
pads playing C" give the same answer. They diverge at every other bank, and the second is the true
one — see `roles_for_pitches`. A capture of a single state cannot distinguish two rules that agree
in that state; it took banking on hardware to tell them apart.

Framework-free so the offline suite can execute it. `root_offset` is what the **A-H buttons**
move (roadmap Phase 6): the factory rests on bank `E`, and F/G/H slide the window right while
D/C/B/A slide it left, one white key — one bottom-row pad — per step.
"""

from __future__ import annotations

from typing import List, Optional, Tuple

#: Semitone offsets of the seven white keys within an octave.
WHITE_KEY_SEMITONES = (0, 2, 4, 5, 7, 9, 11)

#: White-key positions in an octave with **no** black key above them: E (index 2) and B (6).
NO_BLACK_KEY_ABOVE = (2, 6)

PADS_PER_LANE = 16
LANE_0_FIRST_NOTE = 36  # white keys
LANE_1_FIRST_NOTE = 52  # black keys

#: The pitch class the root tint marks. C, in the Keys layout — the landmark that tells you
#: where you are on a piano. A parameter of `roles_for_pitches` rather than a hard constant so
#: Phase 10's Scale mode can tint its tonic instead.
ROOT_PITCH_CLASS = 0

#: Pad roles, in the order the renderer cares about.
ROOT = "root"
KEY = "key"
ABSENT = "absent"

# -- A-H banking (roadmap Phase 6) ------------------------------------------
#
# The eight buttons are a **radio**, and `E` is where the factory rests: "Bank E will be
# selected and Pad 1 will be assigned to the root note". E is index 4, which leaves four
# steps down (D C B A) and three up (F G H) — a bank resting at one end would leave half the
# buttons dead until you moved.
BANK_LETTERS = ("A", "B", "C", "D", "E", "F", "G", "H")
BANK_COUNT = len(BANK_LETTERS)
BANK_REST_INDEX = BANK_LETTERS.index("E")


def bank_step(index: int) -> int:
    """Signed distance of bank `index` from rest. `E` -> 0, `H` -> +3, `A` -> -4.

    ⚠️ **Deliberately unitless.** What one step *means* is the layout's business, not the
    button's — `keyboard.DEGREES_PER_BANK_STEP` is the conversion. In every layout so far it is
    **one scale degree**, i.e. one pad along the bottom row, because that is what the factory
    does: A-H only ever shifts the bottom row. Keeping the button's value unitless is what lets
    the same eight buttons serve Keys and Scale without a mode-dependent handler.
    """
    return int(index) - BANK_REST_INDEX


def bank_index_for_step(step: int) -> int:
    """Inverse of `bank_step`, clamped into the eight real buttons."""
    return max(0, min(BANK_COUNT - 1, int(step) + BANK_REST_INDEX))


def _in_range(pitch: int) -> bool:
    """MIDI is 7-bit. A pad whose pitch falls outside it is not playable, so it is **not a key**.

    ⚠️ This has to be decided *here*, not by the caller. `keyboard.py` also rejects out-of-range
    pitches, and if this function returned one anyway the two would disagree: `pad_roles` would
    call the pad a KEY and light it white, while the keyboard treated it as dead and silenced it
    — a lit pad that does nothing. Reachable today at root -1 with the octave floored, which is
    inside the ranges A-H and Octave will offer.
    """
    return 0 <= pitch < 128


def white_key_semitone(position: int) -> int:
    """Semitone of white-key `position` relative to white key 0 (C).

    Works for **negative** positions: `divmod(-1, 7) == (-1, 6)`, so position -1 is the B an
    octave-and-a-bit down, i.e. one white key below C. Getting this wrong is easy — Python's
    floor division and modulo for negatives are not the C behaviour most people expect — and it
    is why the earlier `root_offset` maths sent pad 1 to note 13 instead of 35.
    """
    octave, degree = divmod(position, 7)
    return 12 * octave + WHITE_KEY_SEMITONES[degree]


def roles_for_pitches(
    pitches: List[Optional[int]], root_pitch_class: int = ROOT_PITCH_CLASS
) -> List[str]:
    """Role of each pad, derived **only** from the pitch list.

    🔑 **This is the single source of deadness, and it takes the pitches rather than the
    offsets that produced them.** A caller that already holds a pitch list — `keyboard.py`
    holds exactly the one it translates notes with — can pass it straight in, so the lights and
    the notes are not merely computed from the same inputs, they are computed from the same
    *list*. That is the strongest available form of the rule in §6b-24, and it is what the
    handoff means by "the lights and the notes must not disagree".

    🐛 **The tint is a property of the pitch, not of the pad.** This used to mark
    `index % 7 == 0` — pads 1, 8 and 15, always, whatever the bank — on the strength of the
    manual's "Bank E will be selected and Pad 1 will be assigned to the root note". That reads
    like "pad 1 *is* the root"; it is in fact a description of the **default**, where the window
    happens to start on C.

    The two frames coincide at bank E and nowhere else, which is exactly why it survived: the
    capture that verified this layout was taken at rest. Banking exposed it — the gaps in the
    top lane moved (they come from the pitches) while the bottom lane's tint sat still (it came
    from the pad index), so half the keybed redrew and half did not. **One frame for both rows:
    a root pad is one that plays the root pitch class.**

    `root_pitch_class` is a parameter rather than a constant so Phase 10 can pass a scale's
    tonic. In the Keys layout it is C.
    """
    roles: List[str] = []
    for index, pitch in enumerate(pitches):
        if pitch is None:
            roles.append(ABSENT)
        # The lane test is belt and braces: a top-lane pad is always a white key plus one
        # semitone, so it can never carry the root pitch class anyway.
        elif index < PADS_PER_LANE and pitch % 12 == root_pitch_class % 12:
            roles.append(ROOT)
        else:
            roles.append(KEY)
    return roles


def pad_roles(root_offset: int = 0, semitone_offset: int = 0) -> List[str]:
    """Role of each of the 32 pads, indexed by `note - 36`.

    `root_offset` slides the keyboard window along the piano in **white keys** — what A-H does;
    `semitone_offset` transposes the whole layout rigidly, and carries Octave ±.

    ⚠️ **Both the gaps and the tint move, and for the same reason: they are properties of the pitches, not the pads.**

    * **The dead pads move with the window.** Whether a black key exists depends on *which white
      key* a position now represents. Sliding a window along a piano changes where the gaps in
      the black keys fall — that is the whole shape of a keyboard.
    * **The root tint moves too.** It marks the pads playing the root pitch class, so as the
      window slides the C's travel across the keybed. This used to be pinned to
      `index % 7 == 0`, which is the same answer only at bank E; see `roles_for_pitches`.

    At `root_offset == 0` and `semitone_offset == 0` both reduce to the layout verified against
    the Studio Pro capture.

    ⚠️ **`semitone_offset` is passed through, and that is a correction.** This used to hard-code
    `0` for the transposition, on the reasoning that a rigid shift cannot change which positions
    have a black key above them. True — but it *can* push a pad off the end of MIDI, and
    `pad_pitches` calls such a pad dead. With Octave alone the layout could not reach the edge
    (±3 octaves over a ~2½-octave span stays inside 0-127), so the two never disagreed. A-H adds
    up to four more semitones downward, which reaches **-4** at the bottom — and the disagreement
    would have shown up as a lit pad that plays nothing.
    """
    # ⚠️ Deadness is derived from `pad_pitches`, never recomputed here. It used to test
    # `(index + root_offset) % 7` independently, which is two predicates for one fact — the
    # failure mode recorded in Motion32_Implementation_Notes.md §6b-16. It matters more once
    # scales arrive: a pentatonic or blues layout has a different number of gaps in different
    # places, and any second opinion about which pads are dead will disagree with the pitches.
    return roles_for_pitches(pad_pitches(root_offset, semitone_offset))


def pad_pitches(root_offset: int = 0, octave_semitones: int = 0) -> List[Optional[int]]:
    """The pitch each pad *represents*, or None for a pad that is not a key.

    ⚠️ Not what the pad **sends**. In native mode a pad always transmits its own fixed note
    (36-67) and every musical transform is host-side — see `Motion32_Scale_and_Chord_Engine.md`
    §2. This is the note we would translate that pad to, and it is what the Phase 10 scale work
    will build on.
    """
    pitches: List[Optional[int]] = [None] * (PADS_PER_LANE * 2)
    for index in range(PADS_PER_LANE):
        # One expression, valid for negative offsets: pad `index` is white key
        # `index + root_offset`, measured from C at note 36.
        base = (
            LANE_0_FIRST_NOTE + white_key_semitone(index + root_offset) + octave_semitones
        )
        pitches[index] = base if _in_range(base) else None
        if (index + root_offset) % 7 not in NO_BLACK_KEY_ABOVE:
            pitches[PADS_PER_LANE + index] = base + 1 if _in_range(base + 1) else None
    return pitches


def safe_semitone_range(root_offset: int = 0) -> Tuple[int, int]:
    """The transposition range that keeps **every** pad inside MIDI's 0-127.

    🔑 **A bottom-lane pad must never be dead.** The gaps in this layout are *missing black
    keys*, and they only exist on the top lane — the bottom lane is sixteen white keys and every
    one of them is a real note. So a dark pad on the bottom row means the layout has been pushed
    off the end of MIDI, which is a range failure, not a layout feature. In particular the root
    lives on the bottom lane, and a dead root is nonsense.

    `OCTAVE_LIMIT = 3` used to guarantee this on its own: the layout spans ~2½ octaves, so ±3
    octaves stayed inside 0-127 at both ends. A-H added up to four more semitones downward and
    quietly broke it — bank `A` at octave -3 is -40 semitones and puts pad 1 on note **-4**.
    Deriving the limit here instead of hard-coding one keeps it true as the layout changes,
    which matters for the Phase 10 scale layouts.
    """
    base = [pitch for pitch in pad_pitches(root_offset, 0) if pitch is not None]
    if not base:
        return (0, 0)
    return (-min(base), 127 - max(base))


def note_for_index(index: int) -> int:
    """LED/note address for pad `index` (0-31). Lane 0 is 36-51, lane 1 is 52-67."""
    if index < PADS_PER_LANE:
        return LANE_0_FIRST_NOTE + index
    return LANE_1_FIRST_NOTE + (index - PADS_PER_LANE)


def dead_indices(root_offset: int = 0, semitone_offset: int = 0) -> Tuple[int, ...]:
    """Pad indices with no key at all — dark, and silent."""
    return tuple(
        i
        for i, role in enumerate(pad_roles(root_offset, semitone_offset))
        if role == ABSENT
    )


def root_indices(root_offset: int = 0, semitone_offset: int = 0) -> Tuple[int, ...]:
    """Pad indices carrying the root — the ones the factory tints with the track colour.

    These **move** as A-H slides the window; they are the pads playing the root pitch class,
    not a fixed set of pad positions.
    """
    return tuple(
        i
        for i, role in enumerate(pad_roles(root_offset, semitone_offset))
        if role == ROOT
    )
