# Motion 32 — Chord Mode Implementation Guide

Status: design guide for roadmap Phase 11. Do not implement before Scale mode unless the roadmap is
explicitly reordered.

This guide turns the Chord-mode design into a reviewable plan of record. It assumes the facts
established in `Motion32_Scale_and_Chord_Engine.md`: in native host mode the Motion pads send fixed
notes, and all musical Scale/Chord processing is host-side. The core rule is unchanged:

> No Python in the pad-to-note performance path.

Python may update controller state, menus, LEDs, display content, and Live device parameters when the
user changes a mode or selection. It must not receive a pad-down and emit the generated chord notes
itself.

---

## 1. Target Behavior

Chord mode is an explicit controller mode:

- Press Chord from Normal/Plugin/Song/etc. -> enter Chord.
- Press Chord while already in Chord -> exit to the previous/base mode.
- Press Scale while in Chord -> switch directly to Scale.
- Press another explicit mode -> exit Chord and activate that destination.

Core invariant:

```text
Chord screen visible <=> Chord mode active
```

Temporary overlays may obscure the Chord page, but they do not exit or suspend Chord mode.

Examples of temporary overlays:

- encoder parameter/value popup;
- notification/status message;
- loading message;
- error message.

When the overlay dismisses, the screen should resolve to the active mode at that moment, not to a page
captured when the overlay was created.

---

## 2. Why a Rack

The factory data gives exact 16-pad chord voicings in `Famous.chords` and `Simple.chords`. A one-to-one
pad translation cannot express one pad triggering three or four notes. Python-generated notes would add
scheduling jitter because Remote Scripts are not the realtime MIDI engine.

Therefore Chord mode should use a Live MIDI Effect Rack:

```text
Motion pad note
-> static pad translation / identity chord-pad layout
-> [M32] Chord Engine MIDI Effect Rack
-> instrument
```

Live's MIDI effects generate the actual chord notes. Python only programs the Rack on selection/key
changes.

---

## 3. Rack Shape

Save a complete engine preset as an `.adg` MIDI Effect Rack:

```text
[M32] Chord Engine
|
+-- [M32] 16 Pad Control
|   |
|   +-- Chain: [M32] Pad 01
|   |   +-- [M32] Carrier Pitch
|   |   +-- [M32] Chord
|   |
|   +-- Chain: [M32] Pad 02
|   |   +-- [M32] Carrier Pitch
|   |   +-- [M32] Chord
|   |
|   ...
|   |
|   +-- Chain: [M32] Pad 16
|       +-- [M32] Carrier Pitch
|       +-- [M32] Chord
|
+-- [M32] Global Key Pitch
```

The top-level device is a MIDI Effect Rack. The instrument remains after it:

```text
[M32] Chord Engine -> Instrument
```

The 16 pad chains are key-zoned to the fixed chord-pad trigger notes:

```text
Pad 01 chain -> note 36 only
Pad 02 chain -> note 37 only
...
Pad 16 chain -> note 51 only
```

The chain zones never change. This permanently separates physical pad identity from the musical notes
being generated.

---

## 4. Chord Pad Layout

Chord mode uses only the bottom lane:

- bottom lane notes `36-51`: 16 active chord pads;
- top lane notes `52-67`: dead/consumed, unlit.

This is important for the current script. `Motion_Keyboard` already translates pads globally for the
Keys layout. Chord mode must explicitly take over pad behavior so the bottom row is routed as identity
notes `36-51`, and the top row is consumed without leaking raw notes.

Do not let the normal keyboard translation remain active during Chord mode. If it remains active, the
Rack will receive translated piano notes instead of fixed pad identity notes, and key-zoned chains will
not behave predictably.

---

## 5. Source Data

The authoritative pad voicings are:

- `Resources/From Studio Pro/Famous.chords`
- `Resources/From Studio Pro/Simple.chords`

These files already contain explicit `pitches` arrays for every selectable 16-pad definition. The
Remote Script should not derive Roman numerals, harmony, inversions, scale spelling, or voice leading.
It should only look up exact pad definitions.

`Famous.chords` rows represent four progression chords, four voicings each:

```text
Pads 01-04 -> progression chord 1, voicing rotations
Pads 05-08 -> progression chord 2, voicing rotations
Pads 09-12 -> progression chord 3, voicing rotations
Pads 13-16 -> progression chord 4, voicing rotations
```

`Simple.chords` is the same 16-row table shape after lookup.

---

## 6. Offline Compiler

Create an offline compiler when Phase 11 begins:

```text
tools/compile_motion_chords.py
```

Inputs:

- `Famous.chords`
- `Simple.chords`

Output:

- generated Python module, likely `motion_chords_compiled.py`;
- or JSON if import size/readability becomes a concern.

A generated Python module is probably simplest for a Remote Script.

Compiler responsibilities:

- verify every selectable definition has exactly 16 pad arrays;
- retain original source notes for debugging;
- sort and deduplicate each pad's notes;
- choose a carrier note for the Chord device;
- convert every other note into shifts relative to that carrier;
- verify note count fits Live's Chord device;
- verify carrier Pitch and Chord shift values fit Live's actual parameter ranges;
- emit a validation report with min/max pitch shifts, min/max chord shifts, and unsupported rows;
- store display metadata such as category, group, and progression name.

---

## 7. Carrier Note Selection

Do not blindly use the lowest note as the Chord-device input.

The original plan used:

```text
anchor = lowest note
shifts = all other notes above anchor
```

That fails for several `Famous.chords` voicings if Live's Chord shifts are limited to `-36..+36`.
Some voicings are open enough that the highest note is `+37`, `+38`, or `+39` above the lowest note.

Example:

```text
source notes: [77, 72, 68, 38]
lowest note: 38
offsets from lowest: +30, +34, +39
```

If the carrier is `38`, a `+39` Chord shift is required. Instead, choose a source note that keeps all
relative shifts inside Live's range:

```text
desired notes: [38, 68, 72, 77]
carrier: 68
Chord shifts: -30, +4, +9
```

The compiler should store both:

- `bass`: the lowest desired note, useful for display/debug;
- `carrier`: the note sent into the Chord device;
- `shifts`: all other desired notes relative to `carrier`.

Suggested compiled row:

```python
PadDefinition(
    source_notes=(77, 72, 68, 38),
    bass=38,
    carrier=68,
    shifts=(-30, 4, 9),
    chord_group=2,
    voicing=3,
)
```

Carrier selection rule:

1. Sort and deduplicate the desired notes.
2. For each desired note as candidate carrier, compute `other_note - carrier`.
3. Keep candidates where every shift is inside Live's Chord shift range.
4. Prefer the candidate closest to the bass if several work, unless testing shows another choice gives
   cleaner device behavior.
5. Fail the row at compile time if no carrier works.

Because Live's Chord device allows `-36..+36`, the known `Famous.chords` wide rows should be
representable with carrier selection rather than lowest-note anchoring.

---

## 8. Per-Pad Programming

Each pad chain has:

- one Pitch device to move the fixed physical trigger note to the selected carrier;
- one Chord device to add the remaining notes relative to that carrier.

For pad 12:

```text
physical trigger note: 47
desired notes: [38, 68, 72, 77]
carrier: 68
Pitch shift: 68 - 47 = +21
Chord shifts: -30, +4, +9
```

The Chord device should produce the carrier note plus the shifted notes, yielding the original voicing.

Unused Chord shift slots must be neutralized so they do not produce extra unison notes. Prefer disabling
unused slots if Live exposes an on/off parameter per slot. If not, verify the safest neutral value by
testing the actual Chord device behavior.

---

## 9. Global Key Transposition

Store progressions once in the source/reference key. A single global Pitch device after all 16 chains
sets the selected key:

```text
per-pad Carrier Pitch -> per-pad Chord -> Global Key Pitch
```

Initial v1 key offsets:

```text
C  = 0
C# = +1
D  = +2
D# = +3
E  = +4
F  = +5
F# = +6
G  = +7
G# = +8
A  = +9
A# = +10
B  = +11
```

Changing key should require one Live parameter write. It should not rewrite the 16 pad programs.

A later Studio Pro comparison can decide whether signed offsets are closer:

```text
G  = -5
G# = -4
A  = -3
A# = -2
B  = -1
```

---

## 10. Chord Mode State

Controller state should be independent of the Rack:

```python
@dataclass
class ChordModeState:
    category: str = "Famous"
    group: str = "Major"
    definition: str = "I - V - vi - IV"
    key_index: int = 0
    selected_menu_field: int = 0
    scroll_position: int = 0
```

Likely menu dimensions:

- category: `Famous` / `Simple`;
- group: `Major`, `Minor`, `H. Min`, `N. Min`, etc.;
- definition: progression or chord type;
- key: `C-B`.

After lookup, Rack programming should not care whether the source was `Famous` or `Simple`.

---

## 11. Rack Programmer

All direct interaction with Live devices should be isolated:

```python
class MotionChordRackProgrammer:
    def find_engine(self, track): ...
    def validate_engine(self, engine): ...
    def program_progression(self, engine, progression): ...
    def set_key(self, engine, key_offset): ...
    def set_enabled(self, engine, enabled): ...
    def reset(self, engine): ...
```

Automatic insertion is intentionally not part of the first proof. Start by detecting and driving an
existing Rack. Add preset insertion only after validation/programming is proven.

Reason: Ableton v3 does not provide a framework-level device insertion API. Raw browser/LOM loading is
asynchronous, changes the user's set, can affect undo history, and needs careful selected-track
targeting.

---

## 12. Rack Validation

Validation should verify:

- exact top-level Rack identity/name;
- one nested 16-pad Rack;
- exactly 16 pad chains;
- fixed, non-overlapping key zones;
- one Pitch device per pad chain;
- one Chord device per pad chain;
- one Global Key Pitch device after the 16-pad Rack;
- required parameters are accessible by stable name or validated index;
- parameter ranges match compiler assumptions;
- the Rack is on the expected track.

Run validation:

- when entering Chord mode on a track for the first time;
- after inserting/loading the engine;
- whenever a cached reference becomes invalid;
- when the selected track's device list changes.

Do not validate on pad press.

---

## 13. Cached References

After validation, cache:

- top-level Rack;
- 16 carrier Pitch devices;
- 16 Chord devices;
- Global Key Pitch device.

Invalidate when:

- selected track changes;
- the device list changes;
- the Rack is deleted;
- the Remote Script reloads;
- a Live Set is loaded;
- object validity checks fail.

Before a programming transaction, verify cached Live objects are still valid.

---

## 14. Entry Sequence

When Chord is pressed outside Chord mode:

1. Begin transition from current mode.
2. Cancel display overlay timers.
3. Exit/deactivate the previous musical mode.
4. Set active musical mode to Chord.
5. Show the persistent Chord page immediately.
6. Bind Chord menu encoder/button assignments.
7. Take over pad layout: bottom row identity notes, top row dead.
8. Paint Chord pad LEDs.
9. Find and validate the Chord Engine Rack on the selected eligible MIDI/instrument track.
10. Resolve the selected compiled progression.
11. Program all 16 pad chains.
12. Set Global Key Pitch.
13. Enable the Rack.
14. Mark the Chord engine ready and allow pad performance.

If the Rack is missing in the first implementation, keep the Chord page visible but show a clear
error/status and keep chord pad performance disabled.

---

## 15. Exit Sequence

Chord mode exits when:

- Chord is pressed again;
- Scale is pressed;
- another explicit mode is selected;
- a dedicated Back/Exit action is used.

Exit sequence:

1. Cancel temporary overlay return timers.
2. Clear parameter/status overlays.
3. Stop accepting new chord-pad interaction.
4. Handle held pads safely.
5. Disable the Chord Engine Rack when safe.
6. Release Chord-specific menu controls.
7. Clear or hand off Chord-specific pad LEDs.
8. Restore destination pad mapping.
9. Activate destination mode.
10. Show the destination mode's persistent page.

When switching directly to Scale, do not draw an intermediate Normal page.

---

## 16. Held-Note Safety

Disabling a Rack while generated notes are sounding must be tested.

Preferred first policy:

- defer Rack disable and progression reprogramming until all chord pads are released;
- store `pending_mode` or `pending_program` while pads are held;
- complete the transition/programming after the final note-off.

Tests required:

- hold one chord pad, exit Chord;
- hold several chord pads, exit Chord;
- switch directly from Chord to Scale while holding a pad;
- change progression while holding a pad;
- hold sustain pedal while exiting;
- delete or disable the Rack while notes are held;
- disconnect/reload the script while notes are held.

Immediate disable may be acceptable only if hardware testing proves Live sends clean note-offs for every
generated note in the relevant cases.

---

## 17. Progression Changes

When the user scrolls to another progression/type:

```text
resolve compiled definition
-> prepare all 16 PadProgram records
-> validate all ranges
-> wait for held pads to release, if needed
-> temporarily disable Rack, if testing proves this is safe
-> write all 16 carrier Pitch devices
-> write all 16 Chord devices
-> re-enable Rack
-> update display and LEDs
```

Prepare the whole transaction before touching Live. Avoid partially programming the Rack while it is
playable.

---

## 18. Key Changes

Changing key is independent of progression selection:

```text
set Global Key Pitch
-> update display
```

Do not reprogram the 16 pad chains.

---

## 19. Pad LEDs

LEDs represent physical pad identity and progression layout, not generated pitch.

Suggested layout:

```text
Pads 01-04 -> progression chord 1
Pads 05-08 -> progression chord 2
Pads 09-12 -> progression chord 3
Pads 13-16 -> progression chord 4
Top row    -> off
```

The four pads in each group represent voicing/register variations.

Pressed pad overlay:

```text
base progression color -> white while held -> restore base color on release
```

Generated chord notes must not drive LED feedback. Shared pitches between voicings could otherwise
light the wrong physical pad.

---

## 20. Display Model

Chord mode needs a persistent Template 1 Menu view. The existing `NotificationView` already borrows
Template 1 for transient two-field overlays, so the eventual Menu view and Notification view must
coordinate ownership carefully.

Recommended display priority:

1. critical error;
2. loading/status notification;
3. encoder parameter popup;
4. Chord persistent page;
5. current base mode page.

The overlay restore callback should call something like:

```python
restore_highest_priority_page_for_current_state()
```

It should not store a fixed return page.

---

## 21. Encoder Popup Behavior

Encoders may continue controlling Live parameters while Chord mode is active.

On touch:

- cancel any pending overlay-return timer;
- show parameter name/value popup;
- keep Chord mode active.

While turning:

- update the parameter;
- refresh popup value immediately;
- keep popup visible.

On release:

- schedule restoration after about one second.

If another encoder is touched:

- cancel previous timer;
- replace popup contents.

When the timer expires, restore the highest-priority page for the mode active at that moment.

---

## 22. Track-Switch Behavior

While Chord mode is active, selecting another track should trigger a controlled engine transition:

1. Stop chord pad input temporarily.
2. Disable the previous track's engine when safe.
3. Capture the new selected track.
4. Validate that it is eligible.
5. Find and validate its Chord Engine Rack.
6. Program the current selected progression.
7. Set current key.
8. Enable the Rack.
9. Resume chord input.

The Chord screen stays visible. If the new track is ineligible or has no engine in the no-auto-insert
implementation, show a clear error and keep performance disabled.

---

## 23. Failure Handling

Chord mode must not partially activate if the Rack cannot be used.

Potential failures:

- selected track is not MIDI-capable;
- selected track has no instrument;
- Chord Engine Rack not found;
- preset cannot be found or loaded, once auto-insertion exists;
- inserted Rack appears on the wrong track;
- Rack structure malformed;
- expected chain/device missing;
- parameter name/index cannot be resolved;
- parameter range unsupported;
- duplicate engines found;
- cached Live object invalid.

On failure:

- keep the Chord page visible;
- show a clear error;
- keep chord pad performance disabled;
- do not leave a partially programmed Rack active.

Example messages:

```text
Select MIDI Track
Chord Engine Missing
Invalid Chord Rack
Unsupported Voicing
Multiple Engines
```

---

## 24. Automatic Rack Insertion

Automatic insertion is useful, but should be a later phase.

When added:

1. Capture `target_track = song.view.selected_track`.
2. Validate it is eligible before loading.
3. Ensure it is still selected immediately before invoking browser/device load.
4. Request preset load.
5. Schedule a follow-up check; insertion is asynchronous.
6. Search the captured target track, not merely the currently selected track.
7. Validate the inserted Rack.
8. Program progression/key.
9. Enable engine.

Insert only once per track. On later Chord entries, reuse the existing Rack.

---

## 25. V1 Boundary

Recommended v1:

- explicit Chord entry and exit;
- persistent Chord screen;
- Chord pad takeover: bottom row active, top row dead;
- manual Rack requirement with detection/validation;
- Rack reuse and enable/disable;
- compiled `Famous` and `Simple` chord library;
- carrier-note compiler selection with range validation;
- all 12 keys through one Global Key Pitch;
- exact 16 Motion voicings where validation passes;
- pad lighting and held-pad overlay;
- safe mode transitions;
- error page/status when engine is unavailable.

Defer:

- automatic `.adg` insertion;
- arbitrary Rack rebuilding;
- user-created chord files;
- editing progression notes from the controller;
- matching Studio Pro's register behavior for signed key offsets;
- continued chord playing after the Chord screen exits.

---

## 26. Implementation Phases

### Phase 1 — Manual Rack Proof

Build the Rack manually and program one `Famous` progression by hand.

Confirm:

- pad zones are correct;
- top row is dead;
- every voicing sounds correct;
- known wide voicings work through carrier-note selection;
- note-offs are clean;
- sustain behaves correctly;
- Global Key transposes the complete progression;
- no chain overlap exists.

### Phase 2 — Compiler Report

Implement the offline compiler/report before script integration.

Report:

- total definitions;
- definitions with exactly 16 rows;
- max unique note count;
- carrier Pitch min/max;
- Chord shift min/max;
- unsupported rows, if any;
- examples of widest voicings.

### Phase 3 — Rack Detection and Programming

Implement:

- Rack search;
- validation;
- cached device references;
- writing one carrier Pitch parameter;
- writing one Chord device;
- writing all 16 chains;
- setting Global Key.

Use one hard-coded progression initially.

### Phase 4 — Chord Mode Lifecycle

Implement:

- Chord button entry;
- persistent Chord page;
- pad layout takeover;
- Rack enable;
- Chord button exit;
- Rack disable;
- direct Chord-to-Scale transition behavior.

### Phase 5 — Chord Menu

Implement:

- category;
- group;
- progression/type;
- key;
- scrolling;
- screen updates;
- transactional Rack updates.

### Phase 6 — Display Overlays

Implement or integrate:

- encoder touch popup;
- live value updates;
- release timer;
- correct restoration after mode changes;
- replacement when another encoder is touched.

### Phase 7 — Held-Note and Transition Safety

Test and finalize:

- exit while pads are held;
- progression change while pads are held;
- track change while pads are held;
- sustain pedal;
- controller disconnect;
- Rack deletion.

### Phase 8 — Automatic Preset Insertion

Only after the above works reliably:

- saved `.adg` lookup;
- selected-track targeting;
- asynchronous insertion detection;
- post-load validation;
- first-entry programming.

---

## 27. Final Flow

Entering Chord mode:

```text
Press Chord
-> active mode becomes Chord
-> Chord page appears
-> chord pad layout takes over
-> find/validate Chord Engine
-> load selected progression from compiled table
-> program 16 Carrier Pitch devices
-> program 16 Chord devices
-> set Global Key Pitch
-> enable engine
-> activate chord pads
```

Changing progression:

```text
Turn progression selector
-> resolve new 16-pad definition
-> prepare and validate PadProgram records
-> defer if pads are held
-> program 16 chain Pitch/Chord devices transactionally
-> update screen and LEDs
```

Changing key:

```text
Turn key selector
-> change Global Key Pitch
-> update screen
```

Exiting Chord:

```text
Press Chord again or select another mode
-> stop new chord input
-> wait for held pads if required
-> disable Chord Engine
-> release chord pad layout
-> activate destination mode
-> show destination page
```

This keeps responsibilities clean:

```text
Motion Remote Script:
  mode state
  menu state
  display and LEDs
  progression lookup
  Rack programming

Ableton MIDI Rack:
  fixed pad routing
  carrier transposition
  chord generation
  global key transposition

Instrument:
  sound generation
```
