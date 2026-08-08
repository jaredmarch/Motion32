# Motion 32 — Host-Integration Handshake & SysEx Specification (Scenario 2)

Authoritative source: the Studio One integration scripts `Motion32MidiDevice.js` and
`Motion 32.surface.xml`, corroborated by disassembly of the device firmware `motionupgrade.bin`
and by hardware MIDI captures. This document describes the **integrated / host protocol** the Motion
enters after a DAW handshake — the mode we intend Ableton to drive. The plain "dumb MIDI" scene is
deliberately out of scope.

**Confidence tags** used throughout:
- **[SRC]** directly specified by the Studio One source / surface XML.
- **[CAP]** observed in hardware MIDI captures.
- **[INF]** inferred from firmware or behavior; not yet verified.

---

## 0. Identity constants

| Item | Value | Source |
|---|---|---|
| Fender SysEx manufacturer ID | `0x08` | JS `kFenderManufacturerSysExId`; firmware header table |
| Device ID — **Motion 32** | `0x26` | JS `Motion32MidiDevice.kDeviceId`; firmware `F0 08 26` |
| Device ID — Motion 16 | `0x24` | firmware `F0 08 24` (shared image) |
| Required firmware | ≥ `1003` | JS `kRequiredFirmwareVersion`. Version computed **verbatim** as `major*1000 + Number(\`${minor}${patch}\`)` — i.e. `major*1000` plus the *string concatenation* of minor and patch parsed as a number. For 1.0.3 → `1000 + Number("03")` = `1003`. (Note: this differs from `minor*100+patch` for two-digit minors, e.g. 1.2.3 → `1023`, not `1203`.) |
| Ships firmware | v1.0.6, build `20260630-182229` | `motionupgrade.bin` header |
| MCU / board | Raspberry Pi **RP2040** (dual Cortex‑M0+), LVGL UI | firmware build path `prj_061_beep2/…/beep2_RP2040_01.c` |

All device-facing SysEx is framed `F0 08 26 <messageId> … F7`. All values are 7‑bit (0–127).

### Ports
`Motion 32.device` detector ports: **`Motion 32`** and **`Motion 32 Main`**. A **second MIDI port**
additionally presents as a **Mackie Control** surface when the on-device *Global Settings → DAW Mode*
is set. Firmware confirms DAW Mode options: **Off / Logic / Ableton / Cubase** — i.e. Ableton already
has a built-in (transport/MCU-level) profile, separate from the deep integration described here.

---

## 1. Connection handshake (the mode switch)

This is the sequence that flips the Motion out of plain-MIDI behavior into the integrated control set.

**On host MIDI-out connect (`onMidiOutConnected(true)`):**
1. Host → device: **`8F 00 7F`** — NoteOff, channel 16, note 0, velocity 127. *This is the "enter host / integrated mode" signal.* (Predecessor Atom SQ used the same channel-16 note-off pattern.)
2. Host invalidates and re-sends all cached LED/screen state (full redraw).
3. Host → device: **Identity Request** `F0 7E 7F 06 01 F7` (universal, non-Fender).
4. Device → host: **Identity Reply** `F0 7E 7F 06 02 …`. The four **firmware version bytes** (major, minor, patch, build) are read at data indices `10 + mfrIdLen`, `11 + mfrIdLen`, `12 + mfrIdLen`, `13 + mfrIdLen`. With the 1-byte Fender manufacturer ID (`mfrIdLen = 1`) these are absolute byte offsets **11, 12, 13, 14** in the reply, counting from the leading `F0`. The JS reads each via `parseInt(byte.toString(16))` (a BCD-style decode — `0x10` → 10, not 16). Host computes the version per §0 and refuses integration if `< 1003`. Offsets shift if a 3-byte manufacturer ID form is ever used — key off `mfrIdLen`, not the absolute index.

   > ⚠️ **Do not compute these offsets from the end of the message.** Our observed reply is 15 bytes
   > (`F0 7E 7F 06 02 08 00 00 26 00 00 01 00 06 F7`), so major/minor/patch land on `01 00 06` = 1.0.6
   > but the *build* read at index 14 lands on the `F7` terminator. Build is unused by the version gate;
   > ignore it. Reading the last four data bytes instead yields a bogus "0.1.0" / version 10. See
   > `Motion32_Implementation_Notes.md` §1a — this is a live bug in the build's `protocol.py`.

**On host exit / disconnect (`onExit`):**
- Host → device: **`8F 00 00`** — NoteOff ch16, note 0, velocity 0. Leaves host mode.

**Device-initiated feedback gating:**
- Device → host: **`F0 08 26 22 <state> F7`** (Global Setting State). `state = 0x01` means the user opened the on-device Global Settings screen — host must **suspend** all screen/LED SysEx while active. When it returns `0x00`, host re-invalidates and redraws everything.

> For an Ableton script: emit `8F 00 7F` on connect and the identity request; parse the identity reply for firmware; watch for `F0 08 26 22` to pause/resume feedback; emit `8F 00 00` on unload.

---

## 2. Device → host (controls, integrated mode)

All on MIDI channel 1 (status `0xB0`) unless noted. Momentary buttons send `0x7F` press / `0x00` release.

| Control | Message | Notes |
|---|---|---|
| Encoders 1–8 | CC `0x0E`–`0x15` | **Relative** (XML: `signed plain`). Sign-bit at 0x40, NOT two's-complement. See §2.1. |
| Encoder touch 1–8 | CC `0x70`–`0x77` (112–119) | capacitive touch on/off |
| Screen wheel | CC `0x1D` | relative signed |
| Wheel push | CC `0x78` | button |
| Bank buttons A–H | CC `0x00`–`0x07` | |
| LCD soft buttons 1–8 | CC `0x24`–`0x2B` | |
| Preset Up / Down | CC `0x2C` / `0x2D` | |
| Shift / Add / Scale / Chord / Control | CC `0x1F` / `0x20` / `0x21` / `0x22` / `0x23` | |
| Octave Up / Down | CC `0x40` / `0x41` | |
| **16‑Velocity** | CC `0x42` | Physical/manual label "16"; XML internal symbol is `fineButton`. Same control. [SRC]/[CAP] |
| Fixed | CC `0x43` | |
| **Pads (Keys/Blocks toggle)** | CC `0x44` | `padsButton` — device→host press `0x7F`/release `0x00`; host→device LED state + RGB at `0x44`. [SRC]/[CAP] |
| Launch | CC `0x45` | |
| Song / Plugin / Edit / Mix | CC `0x46` / `0x47` / `0x48` / `0x49` | control-focus buttons |
| Solo / Mute | CC `0x4A` / `0x4B` | |
| Nav Up / Down / Left / Right | CC `0x57` / `0x59` / `0x5A` / `0x66` | |
| Tap / Record / Play / Stop | CC `0x69` / `0x6B` / `0x6D` / `0x6F` | transport |
| Pads — lane 0 (16) | Note On/Off `36`–`51` | velocity + aftertouch |
| Pads — lane 1 (16) | Note On/Off `52`–`67` | velocity + aftertouch |
| Touch strip 1 | **Pitch Bend, channel 0** | 14-bit message, **~10-bit signal** (values are multiples of 16). [SRC-JS]/[CAP] — *not* in the surface XML |
| Touch strip 2 | **Pitch Bend, channel 1** | 14-bit message, **~10-bit signal**. [SRC-JS]/[CAP] |
| **Touch-strip 1 contact** | CC `0x7A` (122) | `touchStripButton[0]` — the strip's **touch sensor**, not a physical button. Down `0x7F` / up `0x00`. Independent of the position stream. [SRC] |
| **Touch-strip 2 contact** | CC `0x7B` (123) | `touchStripButton[1]`. Same. See `Motion32_Pads_Banking_and_Strips.md` §5 |

### 2.1 Relative encoder decoding [CAP]
The XML labels encoders `signed plain`. Captures show **sign-magnitude with the sign bit at 0x40**, not
7-bit two's-complement (which would encode −1 as `0x7F`). Observed: `0x01` = +1 CW, `0x41` = −1 CCW.

```python
def decode_relative(v):
    if v == 0:      return 0
    if v < 0x40:    return v            # 0x01→+1, 0x02→+2, …
    return -(v - 0x40)                  # 0x41→-1, 0x42→-2, …
```
Still to verify: acceleration / larger deltas under different **Encoder Curve** settings, and whether the
**Fine** modifier changes the wire value or is device-side only. [INF]

### 2.2 Shift layer — secondary functions [SRC]
**Shift** (`shiftButton`, CC `0x1F`) is a **non-latching modifier** (`shiftModifier` param; LED goes
**magenta** while held). It does not send its own action — while held it *reassigns* other controls. On the
wire the modified controls still send their **same CC/note** (§2); the reinterpretation is host-side. All of
the following are confirmed in `Motion32Component.js` / `Motion 32.surface.xml` (transport also in the manual):

| While Shift held… | Control | Secondary function |
|---|---|---|
| **Pads → Command layer** | the pad grid (padMode=Commands, pads turn white) | 16 edit commands on pad indices 0–15 (the **bottom lane**, notes 36–51): Copy, Paste, Duplicate, Delete, Quantize, Prev-grid, Next-grid, Toggle Floating Windows, Insert Instrument Part, Split, Merge, Double, Insert Pattern, New Variation, Duplicate Variation, Redo |
| Transport | Stop (`0x6F`) | **Undo** |
| Transport | Play (`0x6D`) | **Toggle Loop / Cycle** |
| Transport | Record (`0x6B`) | **Retrospective Record** |
| Transport | Tap (`0x69`) | **Metronome / Click** toggle |
| Mode | Control (`0x23`) | enter **User** screen mode (vs Control) — *this is how User mode is reached* |
| Mode | Plugin (`0x47`) | **close** the device editor (vs plugin focus) |
| Touch strip 1 | strip-1 button | toggle **Pitch Bend ↔ Expression** |
| Touch strip 2 | strip-2 button | toggle **Mod Wheel ↔ Breath** |
| Navigation | arrows (`0x57/59/5A/66`) | **Extend** selection mode (vs move) |
| Add menu | Wheel push (`0x78`) | **Replace** selected item (vs Load) |

> For an Ableton client: model Shift as a **modifier button** and provide `_with_shift` variants for the
> transport, Control/Plugin, nav, and wheel-push controls, plus a **Shift-held pad "command" mode**. The Atom
> SQ script does exactly this (its `mappings.py` has `stop_button_with_shift → Undo_Redo`,
> `play_button_with_shift`, `record_button_with_shift`, etc.).

**Important — touch strips:** in integrated mode both strips report raw **pitch-bend position on two
separate channels (0 and 1)**. The *musical meaning* (pitch bend / mod / expression / breath, incl. the
Shift secondary) is decided host-side and re-emitted to the DAW by the script's event generators
(`sendPitchBendToHost`, `sendModulationToHost`, `sendExpressionToHost`, `sendBreathControlToHost`).
The strip snap-to-center behavior (pitch mode) is also a host-side option.

**Pad addressing — one namespace, not two.** ⚠️ **Corrected 2026-07-25.** This section previously
claimed the played note was firmware-generated and could fall outside 36–67. In **native mode** that is
wrong:
- **Pad LED / feedback address:** fixed notes **36–67** (lane 0 = 36–51, lane 1 = 52–67). [SRC]
- **Pad note output:** the *same* fixed addresses. The surface XML declares each pad as
  `<MidiMessage status="NoteTrigger" address="$padIndex+36" options="through"/>` — no transform. The SDK
  calls this the pad's **symbolic pitch** and supplies `symbolicPitchToPadIndex()` so the host can
  recover which pad was pressed. Keys/Blocks, A–H range, Octave, Scale and Chord are all applied
  **host-side**. [SRC]

  The old `[INF]` claim came from the 36–86 range inside `Famous.chords`, which is the *host's* voicing
  library. Full evidence in `Motion32_Scale_and_Chord_Engine.md` §2.
  (The **stand-alone** scene is different — pads there are notes 80–111 on channel 10; see
  `Motion32_Source_Inventory.md` §4.2.)

`screenTemplateSwitch` is a **virtual control with no MIDI message** (surface XML: `options="transmit"`, no `<MidiMessage>`); it drives the template-change SysEx of §4, not a CC. Template selection is done **only** via `F0 08 26 20 <template> F7`. [SRC]

---

## 3. Host → device (LED / color feedback, integrated mode)

### 3.1 Button state LEDs
`0xB0 <addr> <state>` where `<addr>` = the button's CC address (table above) and
`<state>`: **Off = 0**, **Dimmed = 63 (`0x3F`)**, **On = 127 (`0x7F`)**.

### 3.2 RGB color (buttons & encoder halos & pads)
RGB is sent as **three separate messages**, one per channel component, using the low status nibble as a
component selector (1=R, 2=G, 3=B), each component 0–127:

- **Button / encoder halo color:** base status `0xB0` → `0xB1 <id> <R>`, `0xB2 <id> <G>`, `0xB3 <id> <B>`.
- **Pad color:** base status `0x90` (Note On) → `0x91 <note> <R>`, `0x92 <note> <G>`, `0x93 <note> <B>`.

`<id>` for buttons = the button CC address; for pads = the pad note (36–67).

> Fender's internal color-code packing (from JS `RgbColor`): `code = (R<<1)|(G<<9)|(B<<17)|(A<<24)`, each channel 7-bit. You don't need this on the wire — just send the three R/G/B messages.

### 3.3 Pad state LEDs
`0x90 <note> <value>` — `value`: **Off = 0x00**, **On = 0x7F**, **Blink = 0x01**, **Pulse = 0x02**.

### 3.4 Touch-strip LEDs (9 per strip)
Per-LED CC writes: **Strip 1 LEDs = CC `0x37`–`0x3F`**, **Strip 2 LEDs = CC `0x70`–`0x78`**
(`kLEDAddressStart0 = 0x37`, `kLEDAddressStart1 = 0x70`, 9 LEDs each; 0 = off, 127 = on).
Two fill modes exist host-side: *bipolar* (fills from center, default value 0.5) and *fill* (from bottom).
The mode itself is written at the strip's button address (`0x7A`/`0x7B`).

> ⚠️ **Strip 2's LED range collides with encoder cap-touch on input.** `0x70`–`0x77` is *encoder touch
> 1–8* device→host and *strip-2 LEDs 1–8* host→device; `0x78` is *wheel push* in and *strip-2 LED 9* out.
> Direction disambiguates, but the framework won't warn you. Full overlap table in
> `Motion32_Control_Surface_Definition.md` §2.5.

### 3.5 Shutdown
On exit the host also sends `0x8F 0x00 0x00` (see §1).

---

## 4. Screen protocol (host-driven display)

The 4 screen templates are numbered: **0 = Main, 1 = Menu, 2 = Mixer, 3 = Params.**

**Select active template:** `F0 08 26 20 <templateId> F7`.

**Update a screen element:** `F0 08 26 21 <templateId> <zoneId> <elementId> <attr> <data…> F7`

| `attr` | Meaning | `data` |
|---|---|---|
| `0x00` | Text | ASCII bytes |
| `0x01` | Color | `<R> <G> <B>` (7-bit each) |
| `0x02` | Value | `<v>` = normalized × 127 (fader/meter/knob fill) |
| `0x03` | Visibility | `0` hidden / `1` shown |
| `0x04` | Font style | `0` regular / `1` bold |

The full zone/element map for every template is in the companion file
**`Motion32_Screen_Template_Map.md`**. *Which* template + content page is active at any moment is not a
protocol matter — it's decided by the host-side state machine documented in
**`Motion32_Native_Host_Architecture.md`** (the merged state's `screenTemplate` + `pageIndex` attributes).
This spec covers the wire format; the architecture doc covers when to send what.

---

## 5. Confirmation status
**Already confirmed by captures [CAP]:**
- Button **press = `0x7F`, release = `0x00`** (verified on Pads, Plugin, encoder touch, and others).
- Encoder **direction/format**: `0x01` = +1 CW, `0x41` = −1 CCW (sign-bit — see §2.1).
- Native-mode entry/exit (`8F 00 7F` / `8F 00 00`) and the startup ordering.

**Still needs live confirmation [INF]:**
- Encoder **acceleration / larger deltas** under different Encoder Curve settings; whether **Fine** alters the wire value.
- Whether the device **rejects screen/LED SysEx before** the `8F 00 7F` + identity handshake, or feedback free-runs. (Not required to *start* a script, but determines init robustness.)
- **Aftertouch**: channel vs poly (global "Pressure" setting) and default; "Pressure Feel" Drum/Piano curve effect.
- Exact **pad musical-note ranges** produced by each Keys/Blocks/range/octave/scale/chord combination.
- The relationship between this deep integration and the separate **DAW-Mode MCU** profile on the second port — can both run at once, and which port carries what? (Genuinely unknown.)
