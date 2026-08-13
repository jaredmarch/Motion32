# Motion 32 — Pads, A–H banking, Octave, and the touch strips

**Why this file exists.** The next three roadmap phases (pads → A–H → … → touch strips) all need
device behaviour that was scattered across the manual, the surface XML and the Studio One component,
and in two places was recorded **wrong**. This is the reference for that block of work.

Sources: `OM_2777100104_Motion-32_EN.pdf` (owner's manual), `UM_…Studio-Pro-Integration_EN.pdf`,
`Motion 32.surface.xml`, `Motion32Component.js`, `Motion32MidiDevice.js`. Tags as elsewhere:
**[SRC]** from source/XML, **[MAN]** from the manuals, **[CAP]** from a capture, **[INF]** inferred.

---

## 1. Pads — addressing (recap)

Fixed notes, one per pad, in **both** directions: lane 0 = **36–51**, lane 1 = **52–67**. The same
address is the LED address and the note the pad sends. There is no firmware transform in native mode —
Keys/Blocks, Octave, A–H range, Scale and Chord are all applied host-side. Full evidence in
**`Motion32_Scale_and_Chord_Engine.md`** §2. LED state on `0x90`, RGB on `0x91`/`0x92`/`0x93`; state
values Off `0x00` / On `0x7F` / Blink `0x01` / Pulse `0x02`. `[SRC]`

**What this means for "pads lit and responding":** the addresses are known and stable, `leds.py` is
already a generic address-array class that takes `PAD_NOTES` as-is, and `midi.py` already defines
`PAD_NOTES = range(36, 68)`. The work is declaring the elements and deciding what they do — not
discovering anything.

## 1b. The Keys layout, decoded from a capture `[CAP]`

A Studio Pro track-change burst settles the exact geometry, and `pads.py` implements it:

* **Bottom lane, notes 36-51** — 16 **white** keys (C D E F G A B C D E F G A B C D).
* **Top lane, notes 52-67** — the **black** key above each white key, **dark where none exists**
  (above E and above B) → notes **54, 58, 61, 65**.
* **Root pads** (white index % 7 == 0) → notes **36, 43, 50**, drawn in the **track's colour**;
  every other key is **white**; the four gaps are **off**. 28 of 32 lit.

Two protocol facts from the same burst:

1. A lit pad's colour update is **channels 2/3/4 only** — `0x91`/`0x92`/`0x93`, no `0x90` state byte.
2. **Pads have no dim state.** The state byte takes only Off `0x00` / On `0x7F` / Blink `0x01` /
   Pulse `0x02`; `0x3F` (the *button* dim value) lights nothing. Pad brightness comes from the RGB
   triple. See `Motion32_Implementation_Notes.md` §6b-19.

> Note on reading captures of this device: the MIDI monitor used here labels middle C as **C3**, so
> **C1 = 36**. The other common convention shifts every note by an octave and will make a correct
> layout hypothesis look wrong.

## 2. Pad layouts — Keys vs Blocks `[MAN]`

- **Keys (default)** — piano layout: white keys on the bottom lane, black keys on the top lane.
  *Some top-lane pads are deliberately off* to preserve the white/black relationship. Any renderer
  that assumes 32 live pads will be wrong here.
- **Blocks** — a left/right split drum-bank layout: left-side pads are one bank, right-side pads the
  next (e.g. Bank A left, Bank B right).

Host-side these are `PadSectionLayout`: `kKeyboard = 0`, `kContinuous = 1`, `kScale = 2` `[SRC]`.

## 2b. Scale and Chord pad layouts `[MAN — user, 2026-07-25]`

Both abandon the two-lane piano entirely:

| Mode | Top lane | Bottom lane |
|---|---|---|
| **Scale** | ⚠️ **both rows are lit** — see §3's 2026-07-29 note; this row said "all 16 dead" and the user has since observed otherwise on the factory | the scale's pitches, 16 consecutive degrees, tonics in the special colour |
| **Chord** | **all 16 dead** | **4 groups of 4** — root position + 3 voicings, per chord of a four-chord progression |

Two consequences worth carrying:

* A scale layout is strictly ascending on one lane, so **no two pads can share a pitch** — the
  collision that dominates the two-lane piano cannot occur. Verified across all 15 scales ×
  roots -3…+3 × octaves -2…+2.
* The chord layout is exactly the shape of `Famous.chords`: **16 rows = 4 chords × 4 voicings**,
  each group sharing one pitch-class set over a held pedal bass. Confirmed against the file.

Full detail and the Live design consequences: `Motion32_Scale_and_Chord_Engine.md` §5.3c.

## 3. A–H buttons — three context-dependent roles `[MAN]`

**This is the single most important thing to get right about A–H: what they do depends on the pad
mode.** CC `0x00`–`0x07`.

| Pad context | What A–H does | Default |
|---|---|---|
| **Keys** (also **Scale** and **Simple chord**) | Moves the **musical root note** left/right along the piano. F, G, H move the root right; D, C, B, A move it left | **E** — and Pad 1 is the root note |
| **Drum Blocks** | Selects which drum banks the pads show. **Banks are shown two at a time**: the pressed button becomes the left bank and the next in sequence follows on the right | — |
| **16-Velocity** | Selects the bank in which a note is "selected"; the top lane becomes Bank A (1–16) | **A** |

> **Decision (2026-07-25): we follow the factory Keys-mode role — A–H is pad banking, resting on E.**
> This supersedes the earlier suggestion in `Motion32_Build_Roadmap.md` Phase 3 that A–H might carry
> `set_bank_select_buttons` for *device parameter* banks. It cannot be both without a mode split, and
> the factory role is the one the hardware is labelled and lit for. Parameter banking stays on the
> wheel and Left/Right, where it already works.
>
> **Decision (user, 2026-07-29, corrected against factory behaviour): one step is one *scale
> degree* — one pad along the bottom row — in every layout.** The granularity question the table
> above leaves open, and it took two attempts.
>
> It shipped first as **one semitone**, reasoning from "moves the musical root note left/right along
> the piano" (chromatic-sounding) plus `bankMode = KeyboardRange` (fine-grained, as against the
> `KeyboardBanks16/32` that Drum Blocks pages with). Both readings rule out the *coarse* options — a
> whole 16-pad page per button spans ~18 octaves across A–H, and a whole octave per button just
> duplicates Octave ± — but neither says what the fine step actually is.
>
> **Watching the factory settles it: A–H only ever shifts the bottom row.** One press slides the
> keybed by exactly one bottom-row pad, so pad 1 takes over what pad 2 was playing. That is a degree.
> ⚠️ And it holds **in Scale mode too, even though both rows are lit there** — which also corrects
> §2b below, where Scale mode is recorded as leaving the top lane entirely dead.
>
> ⚠️ **A semitone shift and a degree shift are different transforms, and the difference is
> visible.** A semitone shift moves the whole shape rigidly, so no pad changes role and the keybed
> has nothing to redraw — which is exactly how the wrong unit announced itself on hardware: the notes
> moved and the 32 pad LEDs sat still. A degree shift slides the window, so which positions have a
> black key above them changes and **the gaps move with it**. Eight banks over a seven-degree cycle
> give seven distinct gap patterns; A and H are an octave apart and share one.
>
> In code, `pads.bank_step()` returns the **unitless** −4…+3 and `keyboard.DEGREES_PER_BANK_STEP` is
> the conversion, so one radio serves both layouts without a mode-dependent handler.

**Why E is the right default** and not A: it leaves four banks of room downward (D, C, B, A) and three
upward (F, G, H), so the root can move either way from rest. A resting bank at one end would make half
the buttons dead until you moved.

`bankMode` host-side takes `None / KeyboardRange / KeyboardBanks16 / KeyboardBanks32 /
ControlLinkPaging / Launcher / SimpleChordRange` `[SRC]` — note **KeyboardRange** (shift the root)
versus **KeyboardBanks16/32** (page whole banks) are different granularities, matching the
Keys-vs-Blocks split above.

## 4. Octave Up / Down — decoded from a capture `[CAP]`

CC `0x40` (Up) / `0x41` (Down). Transposes **all** pads by 12 semitones, **globally, regardless
of layout** (Keys or Blocks), and also affects some Scale and Chord modes. `[MAN]`

A Studio Pro capture of two consecutive presses (2026-07-26) settles the LED model, and it is
**two independent channels of meaning on one button**:

| | Carries | Values |
|---|---|---|
| **State byte** (`0xB0`) | physical press feedback | `63` at rest, `127` while held |
| **RGB** (`0xB1`-`0xB3`) | whether *this direction* is engaged | blue `#0069CC` at rest, **white** when engaged |

The evidence for the split is clean. Pressing Octave **Down** wrote `Portamento 127` — Down's
own state byte — and in the same breath wrote **Up's** RGB back to blue, because the offset had
just returned to 0. Down's colour was never touched by its own press. So:

* pressing a button changes only its brightness, never its hue;
* the hue is a readout of shared state, and each button shows its own direction.

**Directional, not "non-zero"** `[INF]`: at +1 the host wrote *Up* white and never wrote Down at
all. Had the rule been "either button lights whenever the offset is non-zero", Down would have
been written too. We have not seen a negative offset on the wire, so the mirror image is
inferred — a capture of Octave Down from rest would confirm it.

Implemented in `keyboard.py` via `ButtonControl`'s `on_color` plus the `is_on` setter (both
verified by disassembling `control_surface/controls/button.pyc`: `_send_button_color` picks
`on_color if is_on else color`, and the setter calls `_send_current_color()`).

One deliberate divergence, recorded in `skin.py`: the factory holds the hue on press and only
brightens, so a *disengaged* button pressed would flash full blue. `ButtonControl` has a single
`pressed_color`, and white is right for the other three cases, so a disengaged press flashes
white for ~100 ms instead.

### 4b. The notification bar

Pressing either button **temporarily shows the change on screen**, then returns to the previous
screen. The capture shows exactly how, and it is not a fifth template: it is **Template 1 (Menu)
stripped to two bold texts on the header bar**. Full byte-level detail, and the ways our
implementation deliberately differs, are in `notification.py` and
`Motion32_Implementation_Notes.md` §6b-25.

Dwell measured **995 ms** then **848 ms** across the two presses, so the factory's timer is
coarse rather than exact; we use a round **1 s**.

Text is `"Octave"` and the signed offset — and rest reads **`0`**, not `+0` (the capture sends
the single byte `0x30`).

Interaction to respect: in **Chord mode (famous progressions)** the Octave buttons are *not available*
`[MAN]`. Grey them rather than leaving them lit and inert.

---

## 5. The touch strips — corrected, and better than we recorded

### 5.1 ⚠️ Two errors in the existing docs

1. **`touchStripButton[0]`/`[1]` (CC `0x7A`/`0x7B`) is not a "physical button".** It is the strip's
   **touch/contact sensor** — finger down sends `0x7F`, finger up sends `0x00`.
   `Motion32_Control_Surface_Definition.md` §2.2.1 described it as a physical button ("Each touch
   strip has a **physical button**"); that framing is wrong and led to the strips being modelled as
   position-only.
2. **Touch and position *are* separable.** They arrive as two independent streams. This was the open
   question; the answer is yes.

### 5.1b ⚠️ **Native mode changes what the strips send** `[CAP 2026-07-30]`

**This is the most important thing in §5 and it was not recorded.** The strips behave completely
differently depending on whether native host mode is active, and every claim in §5.2/§5.3 below is a
*native-mode* claim.

**Native mode OFF** (device standalone, DAW Mode off) — the device resolves all four identities
itself, on channel 1:

```
Pitch Wheel  1   32 / -176 / 0        <- strip 1, and it RETURNS TO 0 ON RELEASE BY ITSELF
Control 1  Modulation Wheel   53..41  <- strip 2          (CC 1)
Control 1  Expression         35..37  <- Shift + strip 1  (CC 11)
Control 1  Breath Control     46..40  <- Shift + strip 2  (CC 2)
```

So the Shift toggle **and** the pitch re-centre are done **on the device**. This answers §5.6's open
question 2 for standalone mode: yes, strip 1 emits a final centre value on release.

**Native mode ON** — the device sends **pitch bend only** (strip 1 ch 0, strip 2 ch 1) plus the
contact sensor, and the host owns everything else. The chain in Studio Pro is:

1. `PitchBendHandler` — `addReceiveHandler`, receive-only, one per strip.
2. The host stores the normalized value in `pitchBendValue` / `modulationValue` / `expressionValue` /
   `breathControlValue`, chosen by the **host-side** `touchStripMode[n]` param
   (`paramList.addInteger(0, 7, …)` — nothing is sent to the device).
3. Those params feed `*EventGenerator` controls whose handlers call
   **`sendPitchBendToHost` / `sendModulationToHost` / `sendExpressionToHost` /
   `sendBreathControlToHost`** — Studio One **generating a MIDI event into its own track input**.

> 🔑 **Step 3 is the facility Live does not have.** A Live Remote Script's only outbound API is
> `c_instance.send_midi`, which goes to the *controller*. The translation calls
> (`set_cc_translation`, `set_note_translation`, `set_pad_translation`) rewrite **incoming** messages
> and cannot manufacture one or change its type. So in native mode we can drive Live **parameters**
> from the strips — `Live.MidiMap.map_midi_pitchbend_with_feedback_map` and `PitchBendFeedbackRule`
> both exist — but we cannot deliver pitch bend, mod, expression or breath to the armed instrument,
> and we cannot re-centre a bend that has already reached it.
>
> ⚠️ **Therefore §5.3's "the return-to-centre is host-side, so we must implement it" is only half
> right.** It is host-side in native mode, and we *cannot* implement it for the instrument path. It
> is achievable only for a strip mapped to a Live parameter, where we own the value.

**`touchStripBypass` is not an escape hatch.** It is set true while **Shift is held** and false on
release (`onReceive_shiftButton`), so the strip stops driving the host value during the Shift+touch
gesture and toggling the identity does not also move the value. It does not hand control back to the
device.

**Settled by capture, 2026-07-30, script loaded and native mode active.** ⚠️ **Native mode emits
pitch bend and nothing else. Shift changes nothing the strips send.**

```
Control 1 Local Control On/Off 127   <- strip 1 contact DOWN   (CC 122 = 0x7A)
Pitch Wheel 1  -8048 … -768                                    (channel 0)
Pitch Wheel 1  -976                  <- last value before release
Control 1 Local Control On/Off 0     <- strip 1 contact UP  — NO centre value

Control 1 All Notes Off 127          <- strip 2 contact DOWN   (CC 123 = 0x7B)
Pitch Wheel 2  -7792 … +3632                                   (channel 1)
Control 1 All Notes Off 0            <- strip 2 contact UP

Control 1 Controller 31 127          <- SHIFT DOWN             (CC 31 = 0x1F)
Pitch Wheel 1  …                     <- Shift + strip 1: STILL PITCH BEND, not CC 11
Pitch Wheel 2  …                     <- Shift + strip 2: STILL PITCH BEND, not CC 2
Control 1 Controller 31 0            <- SHIFT UP
```

⚠️ **MIDI Monitor renames these CCs and it is badly misleading here.** `0x7A` (122) prints as
"Local Control On/Off" and `0x7B` (123) as "All Notes Off" — they are the strip contact sensors, and
`0x1F` (31) prints as "Controller 31" and is Shift. Same trap as `0x78`/"All Sound Off" for the wheel
push (§6b-27).

**Consequences, all confirmed rather than inferred:**

1. §5.6's open question 1 is **answered**: strip 1's contact is `127` down / `0` up, like strip 2.
2. **No self-centre in native mode.** Strip 1's final value is wherever the finger left it.
3. **The Shift secondaries are not on the wire at all.** Expression and Breath exist only as
   host-side reinterpretations of the same pitch-bend stream. We receive the Shift *button*
   (`0x1F`, already our modifier), so we can implement the toggle — but only for targets we own.
4. **Strip 1 already works as pitch bend into the armed instrument**, because we do not consume it.
   Strip 2 does too — as a *second* pitch bend on channel 2, which is why it is not a mod wheel.

### 5.1c ✅ Re-confirmed independently, plus one new wire fact `[CAP 2026-08-08]`

A second capture, taken a week later on a different Live session, reproduces §5.1b exactly: contact
sensor down, pitch bend only, contact sensor up, no centre value, and Shift changing nothing. **§5.1b
needed no correction.** Two things it did add:

**1. 🔑 The strips carry ~10 bits, not 14 — and the firmware already told us so.**

Every value in the capture is a multiple of 16: `-1632, -1536, -1408, -1136, -880, -608, -400, -176,
80, 288, 560, 784, …`. The low four bits are always zero, so the 14-bit pitch-bend field is a
**1024-step value shifted left by four**.

This is a **cross-confirmation, not a new guess.** The firmware disassembly independently found
`FUN_00001288 — absolute scan, abs channels, **10-bit ADC**, hysteresis 12`
(`Motion32_Implementation_Notes.md` §6b-33). Wire observation and bytecode agree: 10 bits at the
sensor, transported in a 14-bit envelope.

⚠️ **Every "14-bit" claim about the strips in these docs is true about the message and misleading
about the signal.** Do not build LED bars, parameter scaling or dead-zones assuming 16384 distinct
positions — there are 1024, and the hysteresis means fewer in practice.

**2. Foreign SysEx is silently ignored** `[CAP 2026-08-08]`. Live's factory **Atom SQ** script was
loaded against the Motion as an experiment. It sends PreSonus SysEx (`F0 00 01 06 22 …`, manufacturer
`00 01 06`, device `22`); the Motion's protocol is Fender (`F0 08 26 …`, manufacturer `08`, device
`26`). Every message — including the `12` display writes — was discarded with no screen response and
no error. There is no latent Atom-SQ display compatibility to exploit, and a foreign script cannot
put the device into a state we would have to defend against.

That run also re-captured the **stand-alone** strip behaviour of §5.1b (Mod/Expression/Breath/pitch
bend, self-centring), from a completely different host script — so the three-state model in §5.1b is
now confirmed from two directions.

**And there is no device-side escape either** `[MAN 2026-07-30]`. The owner's manual's Global
Settings list is complete and contains **no touch-strip option**: Screen, LEDs, DAW Mode, Pressure,
Pressure Feel, Pad Curve, Encoder Curve, Reset Settings, Current Firmware. So the device cannot be
told to keep its standalone strip behaviour while native mode is active.

> 🔑 **Conclusion: "strip 2 = Mod Wheel" is not achievable *by the script*.** The device sends pitch
> bend in native mode, Live's translation API has no pitch-bend branch, a Remote Script has no way to
> emit a CC into Live, and the device has no setting.
>
> ✅ **Refined 2026-08-08 — it *is* achievable, just not by us.** A Max for Live MIDI effect can do
> what the script structurally cannot. The Max idiom is `[midiselect]` → `[ctlout]`, and the load-
> bearing detail is that **`midiselect` passes everything it did not select straight through**. So one
> device placed first in the chain can:
>
> - grab pitch bend on **channel 1** (strip 2) and re-emit it as **CC 1**
> - pass pitch bend on **channel 0** (strip 1) through untouched
>
> That is a real mod wheel into the VST's own hook, *and* it removes the two-pitch-benders defect, from
> one device. The two problems turn out to have one solution.
>
> ⚠️ **But it inverts the fix.** The converter can only convert what reaches it, so the script must
> **leave strip 2 un-consumed** — meaning on any track *without* the device, the double bend remains.
> You cannot have the mod wheel and the automatic fix at once; the device *is* the fix. A conditional
> version (consume strip 2 unless the converter is visible in `track.devices`) is possible and
> deliberately not built — it is stateful and fragile, and the simple version should be lived with
> first.
>
> **Decision (user, 2026-08-08): the mod wheel comes from the converter, and the script never inserts
> a device unprompted.** Insertion is a deliberate user action only — `track.insert_device(name, 0)`
> (Live 12.3+) or `browser.load_item()` walking `browser.midi_effects`, bound to a soft button or one
> of the ten empty Shift pads. Nothing automatic, nothing on load, nothing in undo history the user
> did not ask for.
>
> Candidate devices, none of which is likely to do the *channel split* off the shelf:
> [Pitch Bend and Mod Wheel](https://maxforlive.com/library/device/5144/pitch-bend-and-mod-wheel),
> [iBend and iMod](https://maxforlive.com/library/device/2235/ibend-and-imod-pitchbend-modwheel-replacement),
> and the patch outline in the
> [Cycling '74 thread](https://cycling74.com/forums/converting-midi-data-question-pitch-bend-to-cc).
> Stock precedent that Live generates CC 1 internally: its **Slide to Mod** MPE option.
>
> ⚠️ **Corrected 2026-07-31 — this block used to say "and it is final", and part of its reasoning was
> wrong.** What survives: we cannot *emit* CC 1 into Live, and `_translate_message` has no pitch-bend
> branch (verified in bytecode — it handles only `MIDI_CC_TYPE` and `MIDI_NOTE_TYPE`), so a
> translation-based mod wheel is genuinely impossible. What was **false**: the implication that the
> framework cannot deal with pitch bend at all. It has full first-class support —
> `MIDI_PB_TYPE`, `Live.MidiMap.forward_midi_pitchbend`, and
> `map_midi_pitchbend_with_feedback_map`. So we *can* receive it, consume it, and map it to a
> parameter. See §5.3b, which is where the real design decision now lives.
>
> ⚠️ **And leaving strip 2 alone is worse than binding it.** Undeclared, its pitch bend on channel 1
> reaches the armed track and *fights strip 1* — two pitch benders on one instrument. Consuming it is
> a fix in itself, whatever we then point it at.

**The manual also gives the exact LED behaviour** `[MAN]`, which is the spec for §5.4 when the bars
get built:

| Strip | Rest | Movement | Release |
|---|---|---|---|
| 1 — pitch | **centre LED** | follows the finger up/down from centre; jumps to a touch | returns to centre |
| 2 — mod | **bottom LED** | fills upward; jumps to a touch above the bottom | **holds** |
| Shift secondaries | bottom LED | fills upward | holds |

⚠️ **§5.6 open question 3 is answered: the manual says the secondaries turn the LEDs GREEN**
("The LEDs will change to green, reflecting the active parameters' position"). The palette constant
`kTouchStripSecondary` says `orange`. The manual describes the **standalone** device; the constant is
Studio Pro's. In native mode the colour is ours to choose, so this is a preference rather than a
conflict — but the manual is the factory's own documented intent.

⚠️ **So if we declare the strips to read position for the LED bars, it must be with
`ScriptForwarding.non_consuming`** (`v2/control_surface/input_control_element.pyc`:
`script_wants_forwarding` returns true for `exclusive` *or* `non_consuming`). Consuming the stream
would break strip 1's working pitch bend.

### 5.2 What the strips actually send `[SRC]` — ⚠️ **native mode only; see §5.1b**

| Stream | Message | Notes |
|---|---|---|
| **Position** | **Pitch bend, 14-bit message / ~10-bit signal** (§5.1c) — strip 1 on **channel 0**, strip 2 on **channel 1** | `PitchBendHandler.normalize(d1, d2) = (d1 \| (d2 << 7))` over `0…16383` → `0.0…1.0` |
| **Touch** | CC `0x7A` (strip 1) / `0x7B` (strip 2), `0x7F` down / `0x00` up | The contact sensor. Same address carries the strip LED-bar mode host→device — direction disambiguates |

`touchStrip[0]`/`[1]` are declared in the surface XML with `options="receive"` and **no
`<MidiMessage>`** — the pitch-bend stream comes from the device's native `JSKeyboardDevice` layer, not
the XML. That is why the XML alone made them look position-only.

Hardware capture, strip 2, 2026-07-27 `[CAP]`: sliding along the strip produced `CC 0x7B` down
(`0x7F`), then a dense **Pitch Wheel channel 2** stream from about `-8192` to `+8160`, then `CC 0x7B`
up (`0x00`). MIDI Monitor labels `0x7B` as **All Notes Off**, but in Motion native mode it is the
strip-2 contact sensor. This confirms both that touch and position are separate and that strip 2's
position stream is zero-based channel 1 / displayed channel 2.

### 5.3 Behaviour, and who implements it

| | Strip 1 | Strip 2 |
|---|---|---|
| Default identity | **Pitch Bend** | **Mod Wheel** |
| Rest position | **Centre** | **Bottom** |
| On release | **Returns to centre** | **Holds last position** |
| Shift secondary | **Expression** | **Breath** — both rest at bottom and hold |

**Jump-to-touch is intended, not a defect.** The manual documents it as a feature for every mode:
*"Jump to a new pitch position by touching a point above or below centre (the LEDs will jump to your
finger)."* There is no pickup/takeover in the factory behaviour. `[MAN]`

🔑 **The return-to-centre is host-side, not device-side** — *in native mode*. ⚠️ **And it is not
implementable in Live for the instrument path; see §5.1b.** In `Motion32Component.js`:

```js
onReceive_touchStripButton(touchStripIndex, state) {
    ButtonEvent.ifPressBegin(state, () => { /* Shift held → toggle the strip's secondary identity */ });
    ButtonEvent.ifPressEnd(state, () => {
        if (touchStripIndex === 0 && this.isTouchStrip0Mode(kPitchBend))
            this.touchStripHelper.resetPitchBendValue();      // → 0.5
    });
}
```

So **if we do not implement it, pitch bend will stick wherever the finger left it.** This is the
single most important implementation note in this file. Defaults: pitch `0.5`, mod / expression /
breath `0.0` `[SRC]`.

The same handler shows how the secondary identities are reached: **Shift held + touch a strip**
toggles Pitch↔Expression / Mod↔Breath on *press begin*. That matches the manual's "hold Shift, tap a
touch strip," and it means the Shift+strip gesture costs us nothing extra — it is the touch event we
are already receiving.

**A mode the factory defines but does not use:** `PitchBendHandler` supports `kModeDefault`,
`kModeSnapCenter` (snaps to exactly `0.5` within ±0.05) and `kModeMenu`. Studio Pro sets **both strips
to `kModeDefault`** — it relies on the host reset above rather than snapping. Worth knowing that
snap-to-centre exists as a cheap fix if the hardware's own centre proves noisy.

### 5.3b 🔑 The actual design decision: map, or forward? `[FRAMEWORK 2026-07-31]`

Everything above says what the strips *send*. This says what we can *do* with it, read out of
`v2/control_surface/` bytecode rather than guessed. **This is where Phase 9 starts.**

**The framework has full pitch-bend support.** Both installers branch on `MIDI_PB_TYPE`:

```
_install_forwarding(self, midi_map_handle, control, forwarding_type)
    MIDI_PB_TYPE -> Live.MidiMap.forward_midi_pitchbend(handle, channel)
    local `should_consume_event` is derived from forwarding_type

_install_mapping(self, midi_map_handle, control, parameter, feedback_delay, feedback_map)
    MIDI_PB_TYPE -> Live.MidiMap.map_midi_pitchbend_with_feedback_map(...)
                    PitchBendFeedbackRule(value_pair_map, channel, delay_in_ms, enabled)
                    also passes message_map_mode, needs_takeover, mapping_sensitivity
```

`ScriptForwarding` has exactly **three** members: `none`, `exclusive`, `non_consuming`.

⚠️ **A hand-rolled branch in `receive_midi()` will never fire.** Live only forwards messages that an
element registered — `build_midi_map` fills `_forwarding_registry` from declared elements. With no
pitch-bend element declared, the bytes never reach the script. SysEx works today only because it is
special-cased. So the strips must be **declared elements**, not intercepted bytes.

🔑 **`PitchBendFeedbackRule` cannot drive the strip LED bars.** Feedback through that rule sends
*pitch bend* back to the device, but the LED bars are **CC** addresses (§5.4: `0x37`–`0x3F` /
`0x70`–`0x78`). Wrong message type, wrong address space. No configuration of the rule fixes this.

That forces a fork:

| | Map (`_install_mapping`) | Forward (`_install_forwarding`) |
|---|---|---|
| Parameter control | engine-side, with `needs_takeover` + `mapping_sensitivity` | we set `parameter.value` in Python |
| Script sees the value | **no** | yes |
| LED bar possible | **no** | yes |
| Latency | none added | Python in the position path — ⚠️ violates the Phase 9 gate |
| Takeover | free | we implement it, and an absolute strip needs it |

**They may be combinable, and this is the open question.**
`install_connections(self, install_translation, install_mapping, install_forwarding)` hands the
element all three callbacks and lets it choose, and `_is_mapped` / `_is_being_forwarded` are tracked
as **independent** flags — so mapped-and-forwarded is structurally legal. What is *not* knowable
statically is whether the engine still delivers a copy to the script after consuming a message for a
mapped parameter.

> **Hardware test that settles it, and it is cheap.** Declare strip 2 as `MIDI_PB_TYPE`, channel 1,
> `ScriptForwarding.exclusive`, with a value listener that only logs; map it to a device parameter at
> the same time. If the log fills *and* the parameter moves, both paths work — take the LED bar and
> engine takeover together. If the parameter moves and the log stays empty, pick one; prefer
> forwarding, because the LED bar is what makes the strip feel like the factory.

### ✅ RUN, 2026-08-10 — the answers

**1. Declaring a pitch-bend element CONSUMES it.** Strip 2 stopped reaching the armed instrument
the moment it was declared. The two-pitch-benders defect is fixed, and it is fixable in the script
rather than structurally.

This was not predictable from the source. `_install_forwarding` passes `should_consume_event` to
`forward_midi_cc` as a fifth argument but calls `forward_midi_pitchbend` with three and no flag
(`CALL 5` versus `CALL 3` in the bytecode), so the script cannot *request* consumption. Live
consumes forwarded pitch bend **inherently**. Only hardware could have told us.

**2. Forwarding must be installed at construction, not in `setup()`.** The first attempt produced a
strip that was consumed *and* silent — no values reached the listener. Cause: `script_forwarding` is
a property whose setter calls `_request_rebuild`, and `setup()` runs after the first
`build_midi_map`. Assigning it in `elements.py` during construction fixed it immediately.

**3. `script_forwarding` is not a constructor kwarg.** `InputControlElement.__init__` names exactly
`msg_type, channel, identifier, sysex_identifier, request_rebuild_midi_map,
send_should_depend_on_forwarding, is_feedback_enabled`. Anything else falls through `**k` to
`object.__init__` and the script fails to load with `TypeError: object.__init__() takes exactly one
argument`. Cost one failed load.

**4. The signal is ~10-bit, confirmed.** Every value in the capture is a multiple of 16 — `11040`,
`10656`, `9792`, `576`, `12976`. §5.1c was right.

**5. 🐛 The contact sensor cannot be consumed, and it stops notes.** CC `0x7B` is **CC 123, All
Notes Off**. We have never received one event from that element, while strip 1's sensor (CC `0x7A`
= 122) forwards cleanly and the wheel push (CC 120) has always worked — so Live is special-casing
All Notes Off upstream of script forwarding. `ScriptForwarding.exclusive` does not help. MIDI
Monitor shows it plainly:
>
> ```
> From Motion 32 Main  Control 1  All Notes Off  0
> ```
>
> The LED bar does not need it — position onset is enough to know the finger arrived.

**6. The trade-off this creates.** Because declaring consumes, **reading a strip's position and
letting it play the instrument are mutually exclusive**. Strip 1 therefore gets no LED bar; its
working pitch bend is worth more. Untested: whether `non_consuming` behaves differently for pitch
bend. The bytecode says it cannot, since neither type reaches Live for PB, but it is five minutes to
confirm.

Two further notes:

- `script_wants_forwarding` returns true for `exclusive`/`non_consuming` **or** when
  `_input_signal_listener_count` is non-zero. Attaching any value listener silently installs
  forwarding — which is the cheapest way to run the test above, and also an easy way to install
  forwarding by accident.
- **Strip 2 must be `exclusive` regardless of the outcome.** Consumption is decided purely by the
  forwarding type, and consuming it is what stops its channel-1 pitch bend reaching the armed track
  and fighting strip 1. Strip 1 must stay `non_consuming` or its working pitch bend breaks.

### 5.4 Strip LEDs `[SRC]`

Nine per strip. Strip 1 = CC `0x37`–`0x3F`, strip 2 = CC `0x70`–`0x78`. **Colour-only handlers** — the
shutdown capture shows channels 2/3/4 with no channel-1 state byte
(`Motion32_Implementation_Notes.md` §5.1). Index mapping is
`round((ledCount - 1) * normalizedValue)`, and the factory drives them through a dirty-flag cache
identical in shape to our `leds.py`. Two fill styles exist host-side: **bipolar** (from centre — pitch)
and **fill** (from bottom — mod/expression/breath), written at the strip's own `0x7A`/`0x7B` address.

Colours: `TOUCHSTRIPPRIMARY` `#0069CC` blue, `TOUCHSTRIPSECONDARY` orange `[SRC]` — though the manual
says the LEDs *"change to green"* for the Expression/Breath secondaries `[MAN]`, and the Studio Pro
integration manual says both illuminate blue for primary. **Unresolved: confirm the secondary colour on
hardware** before hard-coding it.

⚠️ **Strip 2's LED range collides with encoder cap-touch on input** (`0x70`–`0x77` = encoder touch
device→host, strip-2 LEDs host→device; `0x78` = wheel push in, strip-2 LED 9 out). Direction
disambiguates and `midi.py` already records this, but the framework will not warn you.

### 5.5 What separable touch buys us that the factory does not do

Because touch-down and position are independent events, we can implement behaviour the factory has no
mechanism for:

- **Takeover / pickup.** Ignore position until the finger has *moved* past the current value, killing
  the jump. The factory cannot do this cleanly; we can, because we know when contact began.
- **Touch-only gestures** — tap without slide as a discrete action, which is exactly how the
  Shift+tap secondary toggle already works.
- **Honest LED state.** Light the strip differently while it is actually being touched.

> **Latency note.** The strips are an expressive, real-time control, so the rule from
> `Motion32_Scale_and_Chord_Engine.md` §5.0 applies here too: **the position stream must not be routed
> through Python.** Pitch bend on channel 0 already reaches the track natively. Anything we add —
> takeover, re-identification as mod/expression — needs the same scrutiny as the pad note path, and
> the same answer if we cannot do it in the MIDI layer: do not do it on the play path. The
> return-to-centre reset is a *release* action, not a per-sample one, so it is safe.

### 5.6 Still to confirm on hardware

1. The exact touch-down/up values on **strip 1** `0x7A` (expected `0x7F`/`0x00`, now confirmed for
   strip 2 only).
2. ~~Whether **strip 1** sends any position update on release~~ — **answered for standalone mode
   (§5.1b): it sends `0`.** Still unknown in native mode.
3. **The one that matters: does native mode also emit CC 1 / CC 11 / CC 2, or pitch bend only?**
   §5.1b explains why the answer decides whether the factory identities are reachable at all.
3. ~~The Expression/Breath LED colour~~ — **the manual says GREEN** (§5.1b). The palette constant
   says orange; the manual describes the standalone device and Studio Pro's constant is its own
   choice, so in native mode this is ours to pick.
