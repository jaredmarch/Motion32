# Motion 32 — Complete Control-Surface Definition (authoritative)

**This is the single source of truth for what every control sends and receives.** It is generated
directly from the Studio One integration surface file `From Studio Pro/Motion 32.surface.xml`
(the device's own factory definition) and cross-checked against the build's `midi.py` — **all
values match**. Where the summarized `Motion32_Handshake_and_SysEx_Spec.md` and this file agree,
either can be cited; where they differ, **this file wins** (it is machine-extracted from the XML).

Confidence: everything below is `[SRC]` (directly in the surface XML) unless marked `[INF]`.
Behavioral details that still need a hardware pass (encoder acceleration, pad *musical* note output,
aftertouch format) are **not** control-identity questions and are tracked separately in the gap
analysis — the control identities themselves are fully defined here.

All channel-voice messages are on **MIDI channel 1 (status `0xB0`)** unless noted. Buttons are
momentary: **press = `0x7F`, release = `0x00`**.

---

## 1. Identity & handshake (ref: spec §0–1)
- Manufacturer `0x08` (Fender), device `0x26` (Motion 32). SysEx frame `F0 08 26 <msgId> … F7`.
- USB: vendor `7896` (0x1ED8), product `513` (0x0201) — captured via `ioreg`.
- Native mode ON = `8F 00 7F`, OFF = `8F 00 00`. Identity req `F0 7E 7F 06 01 F7`; reply carries
  firmware (require ≥ 1003). Feedback-suspend gate: device→host `F0 08 26 22 <0x01|0x00> F7`.

---

## 2. Input map — device → host (55 controls)

### 2.1 Encoders & wheel (relative, sign-bit at 0x40)
XML `type="relative"`. Decode: `v<0x40 → +v`, `v≥0x40 → -(v-0x40)`.

| Control | CC | | Control | CC |
|---|---|---|---|---|
| knob[0]…knob[7] | `0x0E`–`0x15` | | wheel (screen) | `0x1D` |
| knobTouch[0]…[7] (cap. touch, button) | `0x70`–`0x77` | | wheelPush (button) | `0x78` |

### 2.2 Buttons
| Control | CC | | Control | CC |
|---|---|---|---|---|
| bankButton[0]…[7] (A–H) | `0x00`–`0x07` | | lcdButton[0]…[7] (soft) | `0x24`–`0x2B` |
| shiftButton | `0x1F` | | addButton | `0x20` |
| scaleButton | `0x21` | | chordButton | `0x22` |
| controlButton | `0x23` | | presetUpButton | `0x2C` |
| presetDownButton | `0x2D` | | octaveUpButton | `0x40` |
| octaveDownButton | `0x41` | | fineButton (labeled "16") | `0x42` |
| fixedButton | `0x43` | | padsButton (Keys/Blocks) | `0x44` |
| launchButton | `0x45` | | songButton | `0x46` |
| pluginButton | `0x47` | | editButton | `0x48` |
| mixButton | `0x49` | | soloButton | `0x4A` |
| muteButton | `0x4B` | | navigationUpButton | `0x57` |
| navigationDownButton | `0x59` | | navigationLeftButton | `0x5A` |
| navigationRightButton | `0x66` | | tapButton | `0x69` |
| recordButton | `0x6B` | | playButton | `0x6D` |
| stopButton | `0x6F` | | | |

> Note the non-obvious nav spacing: Up `0x57`, Down `0x59`, Left `0x5A`, Right `0x66` (NOT
> contiguous). And transport: Tap `0x69`, Rec `0x6B`, Play `0x6D`, Stop `0x6F` (every other CC).

#### 2.2.1 Touch-strip **contact sensors** at `0x7A` / `0x7B` [SRC]

⚠️ **Corrected 2026-07-25.** This section previously called these "touch-strip **buttons**" and stated
that "each touch strip has a **physical button**." That is wrong, and it caused the strips to be
modelled as position-only. `touchStripButton[0]`/`[1]` is the strip's **touch/contact detect** — finger
down and finger up — which means **touch and position are two independent streams**:

| Control | CC | Meaning |
|---|---|---|
| `touchStripButton[0]` | `0x7A` (122) | strip 1 contact: down `0x7F` / up `0x00` |
| `touchStripButton[1]` | `0x7B` (123) | strip 2 contact |

Proof is in `Motion32Component.js` `onReceive_touchStripButton`, which uses `ifPressBegin` for the
Shift secondary-identity toggle and `ifPressEnd` to reset pitch bend to centre. Full behaviour, and the
fact that **return-to-centre is host-side and therefore ours to implement**, is in
`Motion32_Pads_Banking_and_Strips.md` §5.

⚠️ Both addresses are **shared with host→device strip-LED writes** (`touchStripMultiLEDBipolar[n]` and
`touchStripMultiLEDFill[n]` are declared at the same `0x7A`/`0x7B`). Direction disambiguates: inbound
`0x7A/0x7B` = a strip button press; outbound = a strip LED bar write.

#### 2.2.2 Virtual controls — no MIDI message at all [SRC]
These are declared as `<Control>` with **no `<MidiMessage>` and no `<Handler>`**. They are host-side
identities, not wire addresses. Binding them to a CC would be a mistake:

| Control | Purpose |
|---|---|
| `screenTemplateSwitch` | drives the template SysEx `F0 08 26 20`, not a CC (already noted in the spec) |
| `lcdUserButton[0]`–`[7]` | titled **"User 1"–"User 8"** — the User-mode identity of the *same physical* LCD buttons (`0x24`–`0x2B`). See `Motion32_ControlLink_and_User_Mode.md` §4 |
| `touchStrip[0]` / `touchStrip[1]` | the strips themselves. **Their pitch-bend behaviour is not in the surface XML** — it comes from the native `JSKeyboardDevice` layer / `Motion32MidiDevice.js`. See §2.4 |
| `pitchBend` / `modulation` / `expression` / `breathControl` `EventGenerator` | host→DAW event emitters, not device controls |
| `knobTouchEnabler[$knobIndex]` | enables/disables cap-touch reporting per encoder |
| `menuListItems`, `menuListTextColor`, `menuListSelectionColor` | a higher-level list API for Template 1 (Menu) — the host can push a whole list rather than addressing rows one at a time |

### 2.3 Pads (NoteTrigger)
Two lanes of 16 at notes **36–51** (lane 0) and **52–67** (lane 1), declared as
`address="$padIndex+36"` / `+52`. These are **both** the LED/feedback address and the note the pad
actually sends — in native mode there is no firmware transform, and Keys/Blocks, Octave, range, Scale
and Chord are all host-side. `[SRC]`

> ⚠️ **Corrected 2026-07-25.** This entry previously carried an `[INF]` claim that the emitted note was
> firmware-generated and could fall outside 36–67, needing a capture before Session/keyboard mapping.
> That was wrong and it blocked Session mode unnecessarily. See
> `Motion32_Scale_and_Chord_Engine.md` §2.

### 2.4 Touch strips
Two strips report raw **pitch-bend position**, strip 1 on **channel 0**, strip 2 on **channel 1**
(14-bit message, ~10-bit signal — see `Motion32_Pads_Banking_and_Strips.md` §5.1c). Musical meaning
(pitch/mod/expression/breath) is decided host-side.

> **Provenance correction:** this claim is **not** `[SRC]` from the surface XML — `touchStrip[0]`/`[1]`
> are declared there with no `<MidiMessage>`. The pitch-bend format comes from the device's native
> `JSKeyboardDevice` layer and `Motion32MidiDevice.js`, corroborated by capture. Treat as **[SRC-JS]/[CAP]**.
> Universal Control's `motion32.devicelayout` names them `touchstrippitch` and `touchstripmod`,
> confirming strip 1 = pitch / strip 2 = mod as the default identities.

### 2.5 Address overlaps — read this before writing `elements.py`
Several CCs carry different meanings by **direction**. The framework will happily let you collide these.

| CC | Device → host (input) | Host → device (feedback) |
|---|---|---|
| `0x0E`–`0x15` | encoders 1–8 (relative) | **encoder halo** state + RGB (`knobLED[n]` address = `knobIndex + 14`) |
| `0x70`–`0x77` | encoder cap-touch 1–8 | **touch-strip 2 LEDs 1–8** (`ledIndex + 112`) |
| `0x78` | wheel push | **touch-strip 2 LED 9** |
| `0x7A` / `0x7B` | touch-strip 1 / 2 **button** | touch-strip 1 / 2 LED-bar mode write |
| `0x37`–`0x3F` | — | touch-strip 1 LEDs 1–9 (`ledIndex + 55`) |
| `0x44` | `padsButton` (Keys/Blocks) | `padsButton` LED state + RGB |

Note in particular that the **encoder halos have no address of their own** — they are written at the
encoder's own CC. And every one of the 8 encoders' halos is therefore reachable without a new constant.

---

## 3. Feedback map — host → device

**Every button carries BOTH a state-LED handler and an RGB color handler at the same address.** To
light a control fully you send its state *and* its color.

### 3.1 Button state LED  `0xB0 <addr> <state>`
`state`: Off `0`, Dim `63` (`0x3F`), On `127` (`0x7F`). `addr` = the control's own CC (§2.2).
Constants are `$MOTIONSHARED_BUTTONLEDSTATE_OFF/DIMMED/ON` = `0 / 63 / 127`.

Handler census in the surface XML (pre-`foreach` expansion): **45 `ButtonStateLEDHandler`** and
**47 `ButtonColorLEDHandler`** declarations, plus `PadStateLEDHandler`, `PadAnimationLEDHandler` and
`PadColorLEDHandler` (×2 each, one per pad lane, each expanded ×16 by `foreach`). Practically: every
button and every encoder halo has both a state and a colour handler at its own address.

### 3.2 RGB color  (three messages)  `0xB1 <addr> <R>` · `0xB2 <addr> <G>` · `0xB3 <addr> <B>`
Low status nibble selects component (1=R,2=G,3=B), each 0–127. `addr` = the control's CC. Present
for: all buttons, `knobLEDColor[0..7]` (encoder **halos**), `lcdButtonLEDColor[0..7]`, transport,
nav, mode/focus buttons — i.e. essentially every LED.

### 3.3 Pads
- State: `0x90 <note> <value>` — Off `0x00`, On `0x7F`, Blink `0x01`, Pulse `0x02`
  (`PadStateLEDHandler` + `PadAnimationLEDHandler`).
- Color: `0x91/0x92/0x93 <note> <R/G/B>` (`PadColorLEDHandler`).

### 3.4 Touch-strip LEDs (9 per strip)
Strip 1 = CC `0x37`–`0x3F`, strip 2 = CC `0x70`–`0x78` (0 off … 127 on). Bipolar (from center) or
fill (from bottom) host-side.

---

## 4. Screen (host-driven) — ref: `Motion32_Screen_Template_Map.md/.csv`
Select template: `F0 08 26 20 <templateId> F7`  (0=Main, 1=Menu, 2=Mixer, 3=Params).
Update element: `F0 08 26 21 <template> <zone> <element> <attr> <data…> F7`
(`attr`: 00 text ASCII · 01 color R G B · 02 value 0–127 · 03 visible 0/1 · 04 font 0/1).
The XML's screen color controls (`MOTION32_SCREEN_*_COLOR`, `_BACKGROUND`, `_VALUE`, `_LABEL`) map
1:1 onto the 181 addressable elements in the screen map — that file remains the element address list.

**Verified:** the CSV contains exactly 433 rows over 181 unique `(template, zone, element)` addresses
(attrs: 141 color, 132 visible, 81 text, 48 value, 31 font), matching the claims in both docs.

**Text is length-limited and abbreviated.** Every string the factory sends passes through
`formatFunction_compactify(<limit>)` — encoder labels 7 chars, mixer channel labels 8, header titles 13,
menu button text 16. Limits, the algorithm (ported to Python) and the full colour palette are in
**`Motion32_Screen_Style_Spec.md`**.

---

## 5. What this settles
- The **control-identity map is complete and verified** against the device's own factory surface
  file. No hardware capture is required to build correct mappings.
- Therefore any wrong on-device behavior (e.g. transport doing navigation) is a **wiring bug in the
  Ableton `mappings.py`** (which Live function a correct element is bound to), fixed and tested one
  control at a time — not a definition gap.
- Remaining hardware captures are **behavioral** only: encoder acceleration/Fine, pad musical-note
  output, aftertouch format, and feedback timing. None block transport/mixer/plugin wiring.
