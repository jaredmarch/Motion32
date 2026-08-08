# Motion 32 — Scale & Chord: who generates the notes, and how we do it in Live

**Why this file exists.** Four folders in `From Studio Pro/` — `Musical Scales/`, `Chorder/`, `Chords/`
and `Chord Sounds/` — were cited by no doc and were absent from `Motion32_Source_Inventory.md`, which
concluded "nothing substantial is left unmined." They turn out to settle the project's last genuinely
blocking question and to **correct a guiding principle**.

Everything in §1–§4 is **[SRC]** (read directly from the factory integration). §5 is design, not fact.

---

## 1. The headline, and the assumption it corrects

> **In native host mode, Scale and Chord are host-side. Studio One generates the notes, not the
> Motion's firmware.** The pads always send a fixed note per pad. Everything musical happens in the
> host.

The prior assumption across these docs was the opposite — reasonably, because the device *does* ship a
Scale and Chord engine with these exact scales and progressions, and it *does* use them standalone. The
inference was that native mode invoked the same firmware assets. It does not. The device's local engines
are for the stand-alone scene; when a native host attaches, the host takes over.

Docs this corrects, all of which should now be read through this file:

| Doc | Claim that is wrong for native mode |
|---|---|
| `Motion32_Ableton_Build_Handoff.md` §1 | Guiding principle 4: *"note generation runs on-device. Don't reimplement the musical engine."* |
| `Motion32_Native_Host_Architecture.md` §6 | *"Motion firmware owns … Scale engine (16 scales) + root + Lock/Guide, Chord/Famous-progression engine"* |
| `Motion32_Gap_Analysis.md` §2.4 / §3.8 | Pad note output *"generated locally by the firmware … can fall outside 36–67"* |
| `Motion32_Handshake_and_SysEx_Spec.md` §2 | Same, in the "two separate pad namespaces" note |
| `Motion32_Build_Roadmap.md` §5.4 | The pad-note capture, listed as the one blocking item |

## 2. The evidence chain

Five independent pieces, each verifiable in the factory package:

1. **The scale is pushed into a host object.**
   `Motion32Component extends ATOMSQCoreComponent`, and the chain is
   `onPadSectionScaleChanged(scaleId)` → `configureMusicInputPads(kScale, scaleId)` →
   **`component.setScale(value)`**, where `component` is the host's `PadSectionComponent`.
   The same path carries octave (`setCurrentOctave`), root (`setRootOffset`), range (`setPadOffset`)
   and layout (`setKeyboardModeLayout`).

2. **The SDK says outright that the scale engine is host C++.**
   `sdk/musicprotocol.js`: *"Musical scales supported by `PadSectionComponent::setScale ()`. Keep in
   sync with host `musicalscales.h`."*

3. **The chord tables are imported by the host.**
   `MotionSharedChordMenuHelperComponent.onInit()`:
   ```js
   const famousChordsUrl = this.model.findResource("chords_famous");
   this.padSection.chordTriggerModeSettings.importChordProgressions(famousChordsUrl, "Famous");
   const simpleChordsUrl = this.model.findResource("chords_simple");
   this.padSection.chordTriggerModeSettings.importChordProgressions(simpleChordsUrl, "Simple");
   ```
   `kChordTrigger` is a host `PadSectionRole`, alongside `kMusicInput`, `kStepEdit`,
   `kVelocityTrigger`, `kRateTrigger`, `kLauncherInput`, `kIdle`.

4. **The surface XML gives every pad a fixed address.**
   ```xml
   <foreach variable="$padIndex" count="16">
     <define name="$messageAddress" value="@eval:$padIndex+36">
       <Control name="pad[0][$padIndex]" type="trigger" options="receive">
         <MidiMessage status="NoteTrigger" address="$messageAddress" options="through"/>
   ```
   Lane 0 = notes 36–51, lane 1 = 52–67. No transform, no variability.

5. **"Symbolic pitch" is a pad identity, and the mapping is reversible.**
   `Music.padIndexToSymbolicPitch(i) = (36 + i) % 128` has an inverse,
   `Music.symbolicPitchToPadIndex(pitch)`. That inverse only exists because incoming pad notes *are*
   the symbolic ones and the host needs to recover which pad was hit.

**Therefore the "pad musical-note capture" is closed.** In native mode the pads emit notes 36–67, one
fixed note each, regardless of Octave, A–H range, Scale or Chord. The earlier claim that output escapes
36–67 came from the 36–86 pitch range inside `Famous.chords` — which is the *host's* voicing library,
exactly what you would expect if the host generates the notes. `Motion32_Source_Inventory.md` had
already flagged that caveat; this is its resolution.

> **Worth one cheap capture anyway.** Hold Octave-up and hit a pad. If the note is still in 36–67,
> this is settled on hardware as well as in source. That is a confirmation, not an investigation, and
> it does not block design work.

## 3. What each folder is

| Folder | What it actually is | Value to us |
|---|---|---|
| `Musical Scales/` | 15 `.musicalscale` XML files — a 12-slot semitone bitmask (`255` in, `0` out) | **High.** The complete scale table, verified against the SDK enum — see §4 |
| `Chorder/` | 25 presets for the **Studio One `Chorder` NoteFX plugin** (class `{D2D9B002-…}` = `DeviceClassID.kNoteFXChorder`), not the device | Design reference — and the strongest hint for our own chord approach (§5.3) |
| `Chords/` | 104 Studio One **Chord Track** presets (`Major/` 55, `Minor/` 49) | Low for pads. This is Chord Track content, used by the User-mode "Chord Track" command page |
| `Chord Sounds/` | One **Mai Tai** synth patch, "Chord Preview" | None. The audition sound for the chord selector |

### 3.1 The `Chorder` preset model
```xml
<Attributes x:id="chorder" transpose="0" loKey="48" hiKey="72" autofill="1" filterOutsideRange="0"/>
…
<Attributes inPitch="60"><Attributes outPitch="60"/><Attributes outPitch="64"/><Attributes outPitch="67"/></Attributes>
```
A plain `inPitch → [outPitch…]` table. `Chord Types/` and `Intervals/` define **one** chord on C4 with
`autofill="1"`, so the host transposes it across `loKey`–`hiKey`; `Chord Groups/` are explicit
per-key voicings with `autofill="0"`. Note the categories match the `Simple.chords` groups.

### 3.2 The `Chords/` (Chord Track) format — `root` is a circle of fifths
```xml
<ChordEvent timeFormat="2" length="4">
  <Attributes x:id="chord" root="0" intervals="FF 0 0 0 FF 0 0 FF 0 0 0 0" type="0"/>
```
`intervals` is the same 12-slot mask as a scale. **`root` is a circle-of-fifths index, not a
semitone** — convert with `semitone = (root * 7) % 12`. Verified on
`Major/I V vi IV - Four Chords.chords`: roots `0, 1, 3, -1` → C, G, A, F, with `type` `0, 0, 1, 0`
(0 = major, 1 = minor). Observed roots span `-2…5`; `type` also takes 2, 4 and 5 for diminished and
suspended qualities.

### 3.3 Distinguish the two chord formats
`Famous.chords` / `Simple.chords` (JSON, absolute `pitches`, 16 rows = 16 pads) are the **pad**
tables the host imports for chord-trigger mode. `Chords/*.chords` (XML, abstract root + mask) are
**Chord Track** presets. Different features, different consumers — do not conflate them.

## 4. The scale table (complete, verified)

All 15 files decode to the SDK's `MusicalScaleID` enum **exactly and in order**, and every set is
musically correct. Degrees are semitone offsets from the root.

| ID | Name | Mask | Degrees |
|---|---|---|---|
| 0 | `Chromatic` | `111111111111` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` |
| 1 | `Major` | `1.1.11.1.1.1` | `[0, 2, 4, 5, 7, 9, 11]` |
| 2 | `Melodic Minor` | `1.11.1.1.1.1` | `[0, 2, 3, 5, 7, 9, 11]` |
| 3 | `Harmonic Minor` | `1.11.1.11..1` | `[0, 2, 3, 5, 7, 8, 11]` |
| 4 | `Natural Minor` | `1.11.1.11.1.` | `[0, 2, 3, 5, 7, 8, 10]` |
| 5 | `Major Pentatonic` | `1.1.1..1.1..` | `[0, 2, 4, 7, 9]` |
| 6 | `Minor Pentatonic` | `1..1.1.1..1.` | `[0, 3, 5, 7, 10]` |
| 7 | `Blues` | `1..1.111..1.` | `[0, 3, 5, 6, 7, 10]` |
| 8 | `Dorian` | `1.11.1.1.11.` | `[0, 2, 3, 5, 7, 9, 10]` |
| 9 | `Phrygian` | `11.1.1.11.1.` | `[0, 1, 3, 5, 7, 8, 10]` |
| 10 | `Lydian` | `1.1.1.11.1.1` | `[0, 2, 4, 6, 7, 9, 11]` |
| 11 | `Mixolydian` | `1.1.11.1.11.` | `[0, 2, 4, 5, 7, 9, 10]` |
| 12 | `Locrian` | `11.1.11.1.1.` | `[0, 1, 3, 5, 6, 8, 10]` |
| 13 | `Major Triad` | `1...1..1....` | `[0, 4, 7]` |
| 14 | `Minor Triad` | `1..1...1....` | `[0, 3, 7]` |

Ready to paste:

```python
# Motion 32 scale table — from From Studio Pro/Musical Scales/*.musicalscale,
# indices match PreSonus.MusicalScaleID (sdk/musicprotocol.js).
SCALES = {
    0:  ("Chromatic",        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)),
    1:  ("Major",            (0, 2, 4, 5, 7, 9, 11)),
    2:  ("Melodic Minor",    (0, 2, 3, 5, 7, 9, 11)),
    3:  ("Harmonic Minor",   (0, 2, 3, 5, 7, 8, 11)),
    4:  ("Natural Minor",    (0, 2, 3, 5, 7, 8, 10)),
    5:  ("Major Pentatonic", (0, 2, 4, 7, 9)),
    6:  ("Minor Pentatonic", (0, 3, 5, 7, 10)),
    7:  ("Blues",            (0, 3, 5, 6, 7, 10)),
    8:  ("Dorian",           (0, 2, 3, 5, 7, 9, 10)),
    9:  ("Phrygian",         (0, 1, 3, 5, 7, 8, 10)),
    10: ("Lydian",           (0, 2, 4, 6, 7, 9, 11)),
    11: ("Mixolydian",       (0, 2, 4, 5, 7, 9, 10)),
    12: ("Locrian",          (0, 1, 3, 5, 6, 8, 10)),
    13: ("Major Triad",      (0, 4, 7)),
    14: ("Minor Triad",      (0, 3, 7)),
}
```

Two notes from the factory component. Studio Pro exposes **16** menu entries, not 15: `initSupportedScales`
adds `kIonian → kMajor` and `kAeolian → kNaturalMinor` as aliases. And an unrecognised title falls back to
`kChromatic`, which is the right default for us too. Pad layouts are
`PadSectionLayout`: `kKeyboard = 0`, `kContinuous = 1`, `kScale = 2`.

---

## 5. Implementing this in Live — **Scale is BUILT (2026-08-03); Chord remains parked**

> ✅ **Scale mode shipped and is confirmed on hardware.** `scales.py` (the engine), `menu.py` (the
> Template 1 list) and `scalemode.py` (state, soft buttons, wheel). What follows is the design
> record; the **as-built** account is `Motion32_Ableton_Build_Handoff.md` §7 and the three hardware
> bugs are `Motion32_Implementation_Notes.md` §6b-35 / §6b-36.
>
> **What the build changed about this section:**
>
> - **§5.3b's prediction held exactly.** `pads.py` did not generalise; `scales.py` is a separate
>   generator, and the two-lane piano stayed one implementation of the "pitches or `None`" interface
>   rather than the interface itself. `keyboard._is_dead` needed no change at all.
> - **§5.3c's one-lane collapse is verified, not merely reasoned.** 15 scales × 12 roots × 7 octaves
>   × 8 bank positions, 0 duplicate pitches, strictly ascending throughout — and the measured spans
>   match this document's own figures (Major 26, pentatonics 36, triads 60).
> - **`Guide` / `Lock` are defined.** The factory names them in two places and defines them nowhere;
>   the user settled it: **`Locked`** is the one-lane scale layout (the default) and **`Guide`** is
>   the ordinary piano with in-scale notes bright and the rest dimmed.
> - **The soft buttons are the factory's**, from `Motion32_State_Trace_Table.md` §Scale `[SRC]`:
>   `Main / Modes / Key` on the bottom row and the single `Guide`/`Locked` toggle top-right.
> - ⚠️ **Two deliberate divergences.** Chromatic is not offered (leaving Scale mode *is* chromatic),
>   and **the triads are not offered as scales** — `(0, 4, 7)` across sixteen pads spans 60
>   semitones, and the firmware keeps `Triad`/`Sus2`/`Sus4`/`Add 7` in its *chord* strings. They stay
>   in `SCALES` for Phase 11. So the menu is 7 + 7 = **14** where the factory shows 16.

### 5.0-prime — the original plan, kept for its reasoning

> **Scheduling decision (2026-07-25), now superseded for Scale:** it was to be the last feature.
> Scale was in fact taken ahead of the touch strips at the user's request on 2026-08-03. Chord
> remains last. The rest of this section is the original thinking, kept because it proved accurate
> without re-deriving it. Build the rest of the roadmap first. See `Motion32_Build_Roadmap.md`
> Phases 10-11.

**Read the confidence tags.** §1–§4 above are `[SRC]` throughout — established fact from the factory
package. This section is a mix, and the mix is the point:

| Tag | Meaning |
|---|---|
| `[SRC]` | Read directly from Live's framework bytecode or the factory package. Trust it. |
| `[DERIVED]` | Follows necessarily from something `[SRC]`. Sound unless the premise is wrong. |
| `[SPEC]` | **Design speculation. Never tested, on hardware or otherwise.** Treat as a starting point for a design conversation, not a plan of record. |
| `[VERIFY]` | A specific factual question with a known way to answer it. Answer these before building. |

### 5.0 The one constraint that governs everything `[DERIVED]`

**No Python in the pad→note path.** A remote script runs on Live's control-surface thread, which is
serviced on a timer rather than per MIDI event, so anything that receives a pad note in Python and
then emits notes adds scheduling jitter to *playing*. For a keybed that is disqualifying. Every option
below is judged against this first, and one is rejected outright because of it.

This is a constraint on *note generation only*. Python setting a parameter when you change a mode is
fine — that is a mode switch, not a note.

### 5.1 What the framework offers `[SRC]`

Read from `Resources/control_surface/`:

| Mechanism | Where | Shape |
|---|---|---|
| Per-button note remap | `components/playable.pyc` — `PlayableComponent._note_translation_for_button(button)` returns `(identifier, channel)`, applied by `_set_button_control_properties` | Sets the **element's** `identifier` and `channel`, i.e. rewrites what note that pad *is* |
| Bulk pad translation | `components/drum_group.pyc` — `_create_and_set_pad_translations` builds `(x, y, identifier, channel)` tuples and calls `_set_pad_translations(...)` | Hands a translation table to Live itself |
| Channel-only passthrough | `components/background.pyc` — `TranslatingBackgroundComponent` sets `state.channel = _base_translation_channel + index`; skin keys `Translation.Channel.Selected/NotSelected` | Shifts **channel only**, not note. The Atom SQ passthrough idiom |

Both note mechanisms are **static 1:1 remaps**, recomputed when something changes rather than per note
played. There is **no browser or device-insertion support** in the v3 framework — `view_toggle.pyc`
has a browser *view* toggle and nothing else, so loading a device means raw LOM calls outside the
framework.

### 5.2 Scale — the strong case `[DERIVED]`

A scale layout is exactly a **static per-pad note assignment**: pad *i* → the *i*-th degree of the
selected scale from the current root and octave. That is precisely what note translation expresses, so
the mechanism and the requirement are the same shape.

- Compute 32 pad→note assignments from `SCALES[id]` (§4), root offset, octave, layout and range.
- Apply as element `identifier`s; recompute **only** on scale/root/octave/layout/range change — a
  handful of times per session, never while playing.
- The note path stays inside Live's MIDI engine. **Zero added latency by construction.**
- Pad LED colouring (root vs in-scale vs out) falls out of the same table. Studio Pro's own per-key
  gradient, captured in `Motion32_Implementation_Notes.md` §6b-12, is a reference to copy.

Confidence: high. The scale data is verified `[SRC]`, the mechanism is verified `[SRC]`, and the fit
between them is direct. The unknowns are in §5.4, and none of them threaten the approach.

### 5.3 Chord — the shape we'd try `[SPEC]`

**A 1:1 translation cannot express one pad → four notes**, so §5.2's mechanism does not extend to
chords. The approach below is untested speculation, recorded because it is the only route found that
respects §5.0.

**The proposal: Python owns the UI and picks the mapping; Live's own MIDI effects generate the notes.**

```
pads → [our note translation: scale layout]   ← Python, static, recomputed on change only
     → Chord   (interval set)                 ← Python sets parameters
     → Scale   (key + mode)                   ← Python sets parameters
     → instrument
```

Only the first stage is ours, and it is a static remap. The two generating stages sit in the audio
engine. Python moves parameters when you change a setting and never when you play a note, so §5.0 is
satisfied.

**The ordering matters, and it is the crux of the idea.** Live's Chord device applies **fixed semitone
shifts**, so a +4 stays a major third on every degree — used alone it produces parallel/planing triads,
which are wrong over a progression. Placing a **Scale device after Chord** quantises those parallel
triads into the key, which should yield correct diatonic chords. `[SPEC]` — the reasoning is sound but
this has not been tried.

**It mirrors the factory**, which is the strongest argument for it: `Chorder/` is a Studio One **NoteFX
plugin** and the SDK exposes `HostUtils.addNoteFXDevice(kNoteFXChorder)` `[SRC]`. Studio One solves
chording with a device in the signal path, not with logic in the surface script. Same architecture,
different device names.

**What this gives:** chord **types** — every pad plays a triad / 7th / sus rooted on its own scale
degree. That covers Fender's `Chord Types/` and `Intervals/` presets, which is the bulk of the value.

**What it does not give:** `Famous.chords`-style **progressions**, where the 16 pads are 16 *different*
chords (I–V–vi–IV). Live's Chord device applies one interval set to all incoming notes. Per-pad chords
would need per-pad routing — a Rack with key-zoned chains, each holding its own Chord — which is
buildable but a large, fragile object for a script to manage and keep in sync. **Scope any v1 to chord
types; treat progressions as a separate decision.**

**Four frictions to settle before building** `[SPEC]`:

1. **Who inserts the devices.** No framework support (§5.1), and raw browser calls mutate the user's
   set. Cleanest first pass: the user adds Chord + Scale, and we **detect and drive** them — greying
   the mode out when they are absent, the way the factory greys unassigned slots rather than hiding
   them. Silent no-op is the failure mode this project keeps rediscovering.
2. **Undo and automation pollution.** Script-written device parameters enter undo history and can be
   captured as automation. Switching chord type should not litter the undo stack or get recorded.
3. **Per-track scope.** The devices live on one track; the Motion's mode is global. Needs a
   follow-focus rule and a defined behaviour when the focused track has no chord device.
4. **Two-way state.** If the user turns the Chord device's knobs by hand, our screen goes stale unless
   we listen to those parameters.

### 5.3b What the pad layout API must become for scales `[SPEC]`

The Phase 5 keyboard works and generalises **partly**. Worth being precise about which parts,
because the difference decides how much of `pads.py` survives Phase 10.

**Generalises as-is:**

* `keyboard._is_dead(index)` is simply `self._pitches[index] is None`. *Any* layout that yields
  `None` for a pad automatically gets the full dead treatment — identity translation, `listenable`
  mode, no LED, no held state. A scale with a different number of gaps needs no new code here.
* `_recompute()` re-pushes **both** the translation and the mode, so a layout change is a complete
  redraw of pad behaviour, not a partial one.
* LEDs key on **physical index** throughout, never on pitch, so two pads sounding the same note
  cannot share visual state.
* Deadness has a single source: `pad_roles` derives it from `pad_pitches`.

**Does not generalise — `pads.py`'s shape is diatonic to the bone:**

| Assumption | Why a scale breaks it |
|---|---|
| `WHITE_KEY_SEMITONES` (7 per octave) | Pentatonic has 5, blues 6, chromatic 12 |
| `% 7` for roots and octaves | The period is the scale's length, not 7 |
| `NO_BLACK_KEY_ABOVE = (2, 6)` | The gap pattern is a property of *this* scale only |
| `root_offset` measured in **white keys** | For a scale it should be **scale degrees**; for chromatic it is semitones |

So the Phase 10 signature is not "add a scale argument to the existing functions" — it is a
different function that takes a **scale mask** (the 12-slot bitmasks in §4) plus a root, and
returns 32 pitches-or-`None`. The two-lane piano then becomes one implementation of that
interface rather than the interface itself.

> **The property to preserve, whatever the shape:** the layout module returns *pitches or None*,
> and every other behaviour — silence, darkness, translation, press feedback — is derived from
> that one answer. Nothing else may form a second opinion about which pads are playable.

### 5.3c The factory pad layouts for Scale and Chord `[MAN — user, 2026-07-25]` ✅ resolved

The open question — what the factory puts on the top lane — is answered, and it is the simplest of
the three options:

> **Scale mode:** the **top row is entirely off**. The scale's pitches collapse onto the **bottom
> row only**, with the tonics marked in the special colour.
>
> **Chord mode:** the top row is likewise dead, and the bottom row is split into **4 groups of 4** —
> root position plus three inversions, for each chord of a four-chord progression.

**This dissolves the duplicate-pitch problem.** With the top lane dead, a scale layout is 16
consecutive degrees on one lane: strictly ascending, so duplicates are impossible by construction.
Verified across **all 15 scales × roots -3…+3 × octaves -2…+2** — no duplicates, always ascending.
The naive two-lane pentatonic that produced fifteen collisions was solving a problem the factory
simply does not have.

Worth noting the span it buys: Major covers 26 semitones across the 16 pads, the pentatonics 36, and
the triad "scales" 60 — so a scale layout reaches much further than the two-octave piano.

#### `Famous.chords` **is** the chord pad table — confirmed

Checking the user's description against the data settles the structure completely. `I - V - vi - IV`:

| Pads | Chord | Bass held | Upper voices |
|---|---|---|---|
| 1-4 | **C major** (C E G) | C3 | rotate up: C-E-G → E-G-C → G-C-E → C-E-G+8ve |
| 5-8 | **G major** (G B D) | G3 | same rotation |
| 9-12 | **A minor** (A C E) | A3 | same rotation |
| 13-16 | **F major** (F A C) | F3 | same rotation |

All four rows in a group share one pitch-class set and one bass note — so these are **voicing
rotations over a pedal bass**, not textbook inversions (the bass never moves). 16 rows = 4 chords ×
4 voicings, exactly as described, and the file's 39 progressions are 39 ready-made pad tables.

#### What this changes for the Live design

**Scales become straightforward.** 16 pads, one pitch each, strictly ascending, top lane dead. That
is the same shape `keyboard.py` already handles — `_is_dead` is `pitches[i] is None`, and the layout
module answers "pitch or None". A scale is a different *generator*, not a different mechanism.

**Chords get materially better than §5.3 assumed.** Knowing each pad is a **fixed set of 3-4
notes**, the Rack route is concrete rather than hand-wavy: 16 key-zoned chains, each holding a Chord
device configured with that pad's interval set relative to its bass. The pads translate to the 16
bass notes; the Rack supplies the voicing. Still zero added latency — everything musical happens in
the audio engine — and it now supports **full progressions with inversions**, not merely chord
types. `Famous.chords` provides the interval sets directly.

The earlier concern that per-pad voicings "don't map onto one interval set" was right, and the
answer is simply that it is not one device but sixteen chains. That is a bigger object to build and
keep in sync, so it remains a Phase 11 decision — but it is no longer an open design question.

### 5.4 Open questions — **mostly answered by the build (2026-08-03)** `[VERIFY]`

| # | Status after building Scale mode |
|---|---|
| 1-2 | **Moot.** `_set_pad_translations` was never needed: `PlayableComponent`'s per-element `identifier`/`channel` does the whole job, and Scale mode simply hands the keyboard a different pitch list. |
| 3-4 | **Still open** — they belong to Chord (Phase 11), not Scale. |
| 5 | ✅ **Yes, and better than hoped.** Live 12 exposes `root_note`, `scale_name`, `scale_intervals` and `scale_mode`, all **observable** and the first two writable. This took the Template 1 `MenuView` off Scale's critical path entirely. ⚠️ `scale_name` takes **Live's** vocabulary, not the Motion's, and an unrecognised name is silently ignored — hence `scales.LIVE_SCALE_NAMES`. |
| 6 | ✅ **No measurable latency.** The pad→note path is unchanged: translation still happens on the element, and Scale mode only changes *which* pitch list the keyboard is given. |
| 8 | ✅ **Answered by building it rather than by capture.** A–H moves the layout by one scale degree in every layout, and the gaps and tint both follow because both are derived from the pitch list. The first attempt froze that list and produced the classic symptom — see §6b-35. |

The original table follows, for the reasoning behind each question.

#### 5.4-prime — the questions as originally posed

| # | Question | How to answer |
|---|---|---|
| 1 | Does `_set_pad_translations` apply to us at all? It is *called* in `drum_group.pyc` but *defined* in `_Framework.ControlSurface`, which is **not** in our `Resources/control_surface/` copy | Read `_Framework/ControlSurface.py` from the Live install |
| 2 | `DrumGroupComponent._can_set_pad_translations` gates on a **4×4** matrix; the Motion has two lanes of 16. Does that rule the API out, leaving per-element `identifier` as the only route? | Same file, plus the matrix shape we declare in `elements.py` |
| 3 | Live's Chord device — actual parameter names, count, and shift range | Inspect a Chord device's `parameters` in a live set |
| 4 | Are the Scale device's root and mode **settable parameters**, or UI-only? | Same |
| 5 | Is Live 12's scale awareness (`Song.root_note` / `scale_name`) readable from a script? | LOM check. If yes, the Motion could follow the set's key automatically — cheap and a genuinely nice touch |
| 6 | Does pad-note translation actually add zero measurable latency? | Record chromatic passthrough and a scale layout into a clip; compare note timing |
| ~~7~~ | ~~What does the factory put on the top lane in a scale?~~ **Answered (§5.3c): the top row is off and the pitches collapse onto the bottom row.** A capture would still be worth having to confirm the tonic colouring and the exact starting degree | — |
| 8 | **How does the factory redraw the pads as A-H nudges the root?** Do the gaps move as predicted, and does the root tint stay on pad 1? | One Studio Pro capture: press F, then G, then D, reading the LED burst after each |

Standing rule applies to all of these: **read the framework before writing against it**
(`Motion32_Implementation_Notes.md` §6c).

### 5.5 Explicitly rejected, so it isn't retried

**Generating chord notes in Python on pad-down.** Receive the pad, emit note-ons from the script. This
puts our thread — serviced on a timer, not per MIDI event — directly in the pad→note path, violating
§5.0. Legitimate *only* for non-realtime features (writing a progression into a clip, previewing on the
screen), and if it ever ships it must be a separate, clearly-labelled feature rather than the
pad-play path.

**Pushing the chord onto the device.** Not available. §2 shows the firmware engine is not what native
mode uses, and `Motion32_Implementation_Notes.md` §6b-12 established there is no on-wire command to
enable a device-side mode. There is nothing to hand control back to.

### 5.6 What the screen needs — ✅ **built 2026-08-03**

`menu.py` is the Template 1 `MenuView`: header title, four header button labels, a 2 × 6 list with a
selection highlight, and four footer button labels. Written generically because three things want it
— Scale (built), **Chord's progressions**, and browser navigation.

⚠️ **The Template 1 ownership question this section raised is settled.** The menu shares the template
with the notification bar. They are never both active, each claims **every** element on the way in
(§6b-25), and the incoming view `forget()`s so an unchanged snapshot cannot leave it stranded — which
is exactly what happened first time and is written up in §6b-36. In Scale mode the bar is suppressed
outright, because it would blank the list being scrolled once per detent.

For Chord, Studio Pro's captured layout is `"Progressions"` as the header title with `"Major"`,
`"Minor"`, `"Key"`, `"Simple"` as the four header buttons, plus six progression rows — the same shape
Scale now uses, so it should need content rather than code.

### 5.7 Supervisor predicates `[DERIVED]`

Studio Pro gates these modes (`Motion32_Native_Host_Architecture.md` §3): Scale needs a poly/mono synth
focused **and** keyboard pads; Chord needs a poly synth. The Live analogue is "the focused track hosts
an instrument." Worth keeping — a scale mode that silently does nothing because the track holds an
audio effect is the same class of invisible failure this project keeps running into.
