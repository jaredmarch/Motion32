# Motion 32 — Ableton Remote Script Structure (modeled on the Atom SQ script)

> ⚠️ **Historical design document — largely superseded by the code.** This was the pre-build
> blueprint. The script now has **20 modules**, not the 9 proposed here, and several decisions below
> were overtaken by hardware findings. Any module count in this file describes the *Atom SQ* or the
> original proposal, never the current script. For current structure read
> `Motion32_Ableton_Build_Handoff.md` §2, then the code.

The `ATOMSQ.zip` in this folder is the **PreSonus Atom SQ's official Ableton Live remote script**, compiled
for **Live 12 / Python 3.11**, built on Ableton's modern **`ableton.v3.control_surface`** framework. The
Motion 32 is the Atom SQ's successor and clearly retains its design, so this script is a near‑drop‑in
structural template. This document maps its architecture onto the Motion 32 using the constants we've already
documented.

Decompiled from bytecode (structure + constants recovered via `xdis`; exact method bodies not fully
reconstructed). Everything below is **[SRC]** from the Atom SQ `.pyc` unless noted.

> ## Guiding principle — "what" vs "how", and don't be captive to the Atom SQ
>
> The Atom SQ is a **precursor** device. Its scripts are useful for exactly one thing: **HOW** to express a
> Motion 32 client in Ableton's `ableton.v3` framework — the idioms, the `Specification`, elements/mappings/
> skin/display wiring, the native-mode/identity hooks. They are **not** authoritative for **WHAT** the Motion
> 32 should do.
>
> - **WHAT the device should do** comes from Motion 32's *own* capabilities and our reverse-engineering
>   (`Motion32_Native_Host_Architecture.md`, `Motion32_State_Trace_Table.md`, the handshake spec, the
>   181-element screen map). Stay grounded there.
> - **HOW to implement it in Live** is what we borrow from the Atom SQ factory script.
>
> Where the Motion 32 has capabilities the Atom SQ lacks — the **4-template / 181-element screen**, **8 LCD
> soft buttons**, **encoder halos**, **32 pads**, **two touch strips**, **Scale/Chord engines**, richer
> mode set — we should design **beyond the Atom SQ mold**. Ideas that don't fit the old script are
> **encouraged**. The target is the **highest functionality the Motion 32 hardware allows**, and for it to
> feel **as deeply integrated into Ableton as it is into Studio Pro** — not merely a port of a precursor's
> script. Use the Atom SQ for mechanics; let Motion 32's hardware define the ambition.

---

## 1. The headline: our RE findings are native framework features

Every low‑level thing we reverse‑engineered has a **direct hook** in `ableton.v3`. The Atom SQ script shows
exactly where each plugs in — so we barely have to hand‑roll the protocol.

| Our Motion 32 finding | Atom SQ / `ableton.v3` mechanism |
|---|---|
| Native‑mode enable `8F 00 7F` / disable `8F 00 00` | `Specification.hello_messages` / `goodbye_messages` (Atom SQ: `NATIVE_MODE_ON_MESSAGE = (0x8F,0x00,0x01)`, `OFF = (0x8F,0x00,0x00)`) — framework sends them on connect/disconnect |
| Identity handshake (firmware ≥ 1003) | ⚠️ **CORRECTED (see `Motion32_Implementation_Notes.md` §1):** `identity_response_id_bytes` does NOT work for the Motion — its reply id bytes are non-contiguous (`08 00 00 26`), the framework match never fires, and the device stays pre-native. Put `IDENTITY_REQUEST` in `hello_messages` and parse the reply manually in `receive_midi`; do not rely on `on_identified`. |
| Relative encoders, sign‑bit at 0x40 | `MapMode.LinearSignedBit` on `add_encoder` — the exact decode, built in |
| RGB as 3 messages on channels 1/2/3 | `colors.create_color` → `ComplexColor([ColorPart(ch=RED_MIDI_CHANNEL=1), GREEN=2, BLUE=3])` |
| Blink / pulse LED values | `colors.BLINK_VALUE` / `PULSE_VALUE` |
| Screen text via `F0 08 26 21 …` | `elements.add_sysex_display_line(header=DISPLAY_HEADER)` + `display.py` `DisplaySpecification` |
| Touch‑strip LED bar | `touch_strip.TouchStripElement` (maps a param → `map_value_to_led_states` → per‑LED `send_value`) |
| Ports (Main vs Control) | `get_capabilities()` → `inport`/`outport` with flags `NOTES_CC, SCRIPT, REMOTE, SYNC` |

**Implication:** most of the "protocol" work becomes *configuration* of a `ControlSurfaceSpecification`, not
custom MIDI plumbing. We supply Motion 32's constants (which we've documented) into the same slots.

---

## 2. Module layout (copy this structure)

The Atom SQ script is 9 modules. Proposed Motion 32 equivalents:

| Atom SQ module | Role | Motion 32 changes |
|---|---|---|
| `__init__.py` | `ControlSurface` subclass + `ControlSurfaceSpecification`, `get_capabilities()`, `create_instance()` | Swap vendor/product IDs, port names (`Motion 32 Main`), native‑mode bytes (`0x8F 00 7F`), identity bytes (`08 26`) |
| `midi.py` | All MIDI/SysEx constants | Replace with our documented values (§4) |
| `elements.py` | `ElementsBase` — declare every physical control + its CC/note | Use our full control map (handshake spec §2); 32 pads vs Atom SQ's grid; 8 encoders CC 0x0E–15; 2 touch strips; 8 LCD buttons; screen SysEx lines |
| `skin.py` | Declarative LED color skin (per component/state → color) | Reuse nearly as‑is; add Motion pad/encoder‑halo states |
| `colors.py` | `Rgb` palette + `ComplexColor` 3‑channel builder + Live‑color map | Reuse almost verbatim |
| `display.py` | `DisplaySpecification`: `Content` dataclass, `View`, notifications, `protocol` | **Biggest expansion** — Motion has 4 templates & many zones vs Atom SQ's simple lines (see §5) |
| `touch_strip.py` | `TouchStripElement` with LED feedback | Two strips; our LED addresses (0x37–3F / 0x70–78); pitch‑bend transport |
| `launch_and_stop.py` | Session clip launch/stop component | Reuse as‑is |
| `mappings.py` | `create_mappings()` — declarative modes → components → controls | Adapt to Motion's **Control Focus** buttons (Song/Plugin/Edit/**Mix**) plus its **Mode** buttons (Add/Scale/Chord/Control) and the **User** screen mode (§3) |

---

## 3. Modes: how the state chart becomes declarative

The Atom SQ expresses its mode system **declaratively** in `create_mappings()` — this is the Ableton‑native
replacement for hand‑coding our 14‑layer chart. Recovered top‑level structure (Atom SQ):

- **`Main_Modes`** (the control‑focus selector) — Atom SQ buttons `song_button / instrument_button /
  editor_button / user_button` select modes `song / instrument / editor / user`, with a `default_behaviour`.
  This is the structural analog of **Motion's four Control Focus buttons: Song / Plugin / Edit / Mix**
  (our control‑focus layer 4). Note the sets are **not** a 1:1 rename — Atom SQ's *instrument* ≈ Motion's
  *Plugin*, and Atom SQ's 4th mode is *user* whereas Motion's 4th Control‑Focus is **Mix**. Motion's *User*
  is a separate **screen mode** (layer 5, with Add/Scale/Chord/Control), not a Control‑Focus button.
- **`Device`** — Atom SQ's mode buttons → `encoders` → `parameter_controls` (the 8 encoders drive device params).
- **`Mixer`**, **`Session`** (pads → clip launch / track select / stop), **`Transport`** (play/stop/record/loop/click/tempo/cue nav), **`View_Toggle`** (bank A/B/D/H → session/browser/detail/clip views), **`View_Control`**, **`Device_Navigation`**, **`Launch_And_Stop`**, **`Lower_Pad_Modes`** (enable/cycle/select/stop), **`Modifier_Background`** (shift), **`Translating_Background`**, and a **touch‑strip** mapping (target track volume/pan/sends/solo/mute/arm/crossfader).

Framework primitives used: `Modes`, `LatchingBehaviour`, modifier buttons (shift), component mappings. The
framework handles mode layering, LED feedback, and takeover — so we **do not** re‑implement the supervisor/queue
by hand; we express the layers as modes and let the framework compose them. (This validates the architecture
doc's "adapt, don't copy the 14 layers" guidance.)

> Motion‑specific adaptation: map Motion's **Plugin** button → a Device mode, **Mix** → Mixer, **Song** →
> a transport/song params mode, **Edit** → a device/clip edit mode, **Scale/Chord** → *leave the pads passing
> through in v1* (local firmware engine; see gap analysis §12), **User** → user‑commands mode.

> **Shift layer (don't overlook it — see handshake spec §2.2).** Shift (`shiftButton`, CC 0x1F) is a
> **non‑latching modifier**; while held it reassigns controls: transport → Undo/Loop/Retro/Click,
> **Control → User mode**, Plugin → close editor, nav → Extend, wheel‑push → Replace, touch strips →
> Expression/Breath, and the **pad bottom lane becomes a 16‑command edit overlay** (Copy/Paste/Duplicate/
> Delete/Quantize/Split/Merge/Double/Redo/grid/windows/parts/patterns/variations). Mirror the Atom SQ pattern:
> declare a **Modifier** (its `Modifier_Background` / shift) and `_with_shift` control variants, plus a
> Shift‑held pad command mode. The Atom SQ `mappings.py` already shows `stop_button_with_shift`,
> `play_button_with_shift`, `record_button_with_shift`, `display_*_with_shift`, etc.

---

## 4. Motion 32 `midi.py` (fill these with our documented values)

Atom SQ's constants (for reference) vs Motion 32's (from `Motion32_Handshake_and_SysEx_Spec.md`):

```python
# --- Motion 32 midi.py (proposed) ---
NATIVE_MODE_ON_MESSAGE  = (0x8F, 0x00, 0x7F)   # Atom SQ used 0x01; Motion uses 0x7F
NATIVE_MODE_OFF_MESSAGE = (0x8F, 0x00, 0x00)

SYSEX_START_BYTE = 0xF0
SYSEX_END_BYTE   = 0xF7
MANUFACTURER_ID  = (0x08,)                       # Fender
DEVICE_ID        = 0x26                           # Motion 32 (Motion 16 = 0x24)
SYSEX_HEADER     = (0xF0, 0x08, 0x26)

# message ids (device-facing)
MSG_SCREEN_TEMPLATE = 0x20     # F0 08 26 20 <template> F7
MSG_SCREEN_UPDATE   = 0x21     # F0 08 26 21 <template><zone><element><attr>[data] F7
MSG_GLOBAL_STATE    = 0x22     # device->host feedback gate

# screen element attributes
ATTR_TEXT, ATTR_COLOR, ATTR_VALUE, ATTR_VISIBLE, ATTR_FONT = 0x00, 0x01, 0x02, 0x03, 0x04

# RGB (3 messages, channels 1/2/3), LED states
RED_MIDI_CHANNEL, GREEN_MIDI_CHANNEL, BLUE_MIDI_CHANNEL = 1, 2, 3
LED_OFF, LED_DIM, LED_ON, LED_BLINK, LED_PULSE = 0, 63, 127, 0x01, 0x02

# identity (handshake)
# ⚠️ DO NOT USE identity_response_id_bytes — see Motion32_Implementation_Notes.md §1.
# The Motion's reply id bytes are non-contiguous (08 00 00 26) so the framework match never fires.
IDENTITY_REQUEST_MESSAGE = (0xF0, 0x7E, 0x7F, 0x06, 0x01, 0xF7)  # goes in hello_messages
REQUIRED_FIRMWARE = 1003
# Firmware bytes in the reply, at FIXED offsets from the leading F0 (Fender mfr id is 1 byte):
#   major = msg[11], minor = msg[12], patch = msg[13]      (build byte is unreliable — ignore it)
#   decode is BCD-style: int(f"{byte:x}")   -> 0x10 means 10, not 16
#   version = major * 1000 + int(f"{minor}{patch}")        -> 1.0.6 => 1006
FIRMWARE_MAJOR_INDEX, FIRMWARE_MINOR_INDEX, FIRMWARE_PATCH_INDEX = 11, 12, 13

# text limits (every string is compactified to fit — see Motion32_Screen_Style_Spec.md)
MAXCHARS_ENCODER_LABEL, MAXCHARS_MIXER_CHANNEL = 7, 8
MAXCHARS_HEADER_TITLE, MAXCHARS_MENU_BUTTON, MAXCHARS_PARAMS_VALUE = 13, 16, 7

# touch-strip buttons (found in the surface XML 2026-07-24)
CC_TOUCHSTRIP_1_BUTTON, CC_TOUCHSTRIP_2_BUTTON = 0x7A, 0x7B
```

`get_capabilities()`: set Fender's USB **vendor_id**, the Motion 32 **product_id**, `model_name="Motion 32"`,
and the two ports — bind the script to **`Motion 32 Main`** (native), leaving `Motion 32 Control` for the
optional Mackie path. (Atom SQ used `vendor_id=6479 (PreSonus 0x194F)`, `product_ids=522`, `model_name='ATM SQ'`.)

---

## 5. Where Motion 32 diverges from Atom SQ (plan for it)

1. **Screen is far richer.** Atom SQ's `display.py` writes simple text lines; Motion has **4 templates, 181
   addressable elements** (see screen map). Our `display.py` needs a `DisplaySpecification` that selects a
   template (`MSG_SCREEN_TEMPLATE`) and populates zones/elements (`MSG_SCREEN_UPDATE`) per mode — model the
   `Content`/`View` dataclasses on the Atom SQ ones but expand to template/zone/element addressing.
2. **Encoder‑halo RGB + pad RGB** — Atom SQ maps pad/button colors via the skin; extend the skin to encoder
   halos (Control‑Link colors) and 32 pad LEDs.
3. **Scale/Chord/Keys‑Blocks are local firmware engines.** In v1, do **not** remap pad notes — pass them
   through (gap analysis §12). Revisit after the pad‑mode‑sync capture.
4. **Feedback volume** — a full template repaint is many packets; use the framework's caching + add a
   rate‑limited path for mixer meters (architecture doc §4).

---

## 5b. The `ATOMSQ Plus` add-on — a *supplementary* "custom actions in User mode" example [SRC: working .py]

> **Authority hierarchy — read this first.** The **factory** behavior is the "most correct" reference:
> (1) the **Atom SQ factory Ableton script** (`ATOMSQ.zip`) is the authoritative *structural* model for our
> Motion 32 script, and (2) Motion 32's **own factory native protocol** (reverse-engineered from the Studio
> One integration) is authoritative for device behavior. The `ATOMSQ Plus` add-on below is a **WIP,
> human-written hack** — genuinely useful for *ideas* about layering custom actions, but **not** the primary
> blueprint. Where Plus and the factory disagree, follow the factory. Treat Plus as inspiration, not canon.

`CustomAtomSQ Plus.zip` is a **working** add-on (source, not bytecode) that keeps factory behavior and adds
custom actions by owning **User mode**. Useful patterns worth borrowing (with the caveat above):

- **Extend, don't replace.** `ATOMSQPlus(ControlSurface)` reuses the factory `Specification` + modules
  verbatim; `create_mappings` wires the *factory* modes (song/instrument/editor) to real Live components
  (`Mixer`, `Device`, `Session`, `Transport`, `Device_Navigation`, `View_Toggle`, `Launch_And_Stop`).
  **`mappings.py` is a goldmine** of exactly how to bind each Live component to hardware controls.
- **User mode = the custom seam.** In `mappings.py`, `user=` binds **only** `Translating_Background`
  encoders (a channel-10 passthrough) and deliberately leaves the display L/R buttons free. A custom
  `UserPagesComponent` (instantiated in `setup()`) then owns the soft buttons + page nav. `_on_main_modes_changed`
  enables that component **only when** `mode == "user"`, so factory modes are untouched.
- **`UserPagesComponent` = paginated custom actions.** A `pages` list is the source of truth; each page =
  `{name, button_labels(6), actions(6 callables)}`. Soft buttons light + run the action; L/R buttons page.
  Actions call the Live API directly (`song.tempo`, view toggles, `set_or_delete_cue`, `jump_to_*_cue`,
  `scene.fire`, `stop_all_clips`, `metronome`, `tap_tempo`, back-to-arrangement). Trivial to graft new actions.
- **Display takeover per mode.** `display.py` uses the framework `DisplaySpecification` + a `Content`
  dataclass + `protocol()`; in user mode it *takes over* the screen (custom SysEx for title/BPM/page indicator
  + soft-button labels), and in factory modes restores default track/device text via `BUTTON_LABELS_MAP`.
- **Repurposing a control globally.** `PitchBendTempoControl` binds the pitch-bend (touch strip) to BPM ±
  with a return-to-center debounce — a clean template for global custom control behavior.
- **Handshake confirmations (match our RE):** `hello_messages=(NATIVE_MODE_ON_MESSAGE,)` /
  `goodbye_messages=(NATIVE_MODE_OFF_MESSAGE,)` (plus a manual `_send_midi` on setup); `on_identified` →
  `schedule_message(1, self._update_firmware)`; `MapMode.LinearSignedBit` encoders;
  `add_modified_control(ctrl, modifier=shift)` for `_with_shift`; display SysEx `F0 00 01 06 22 12 <field>
  <r> <g> <b> <align> <ascii…> F7` (Atom SQ) — our Motion equivalent is `F0 08 26 21 <t><z><e><attr>…`.

### Applying it to Motion 32 — one crucial difference
The Atom SQ Plus builds **on top of the existing factory Ableton script**. **Motion 32 has no factory Ableton
script** — building it (modeled on `ATOMSQ.zip`) *is* our project. So we don't "add on"; we build the factory
equivalent and can bake the UserPages pattern in from day one. Concretely:
- Motion's **User** mode is reached via **Shift+Control** (no dedicated User button) — our `Main_Modes` ties
  to Motion's Song/Plugin/Edit/Mix CCs; treat Shift+Control → a `user` mode the same way.
  **The factory User-mode model is now fully documented** (named pages of 8 commands on the LCD soft
  buttons, with paging independent of the encoders') — see `Motion32_ControlLink_and_User_Mode.md` §4.
  The UserPages pattern below and Fender's own model agree, so build to Fender's shape.
- Motion has **8 LCD soft buttons** (vs Atom SQ's 6) → more actions per page; use the wheel/nav for paging.
  The factory splits them **top row = 0–3, bottom row = 4–7**, matching Template 0's header/footer label
  zones — keep that correspondence or the labels will read wrong.
- Motion's **4-template, 181-element screen** makes far richer custom pages than Atom SQ's flat fields.
- WIP caveats to clean up when porting: heavy `try/except` guards, a hardcoded scene-color constant, and
  mixed display paths (framework `protocol` vs direct `_send_display_sysex`) — fine for a WIP, tidy for v1.

---

## 6. Recommended first vertical slice (matches the agreed milestone)
Build the smallest end‑to‑end script, reusing Atom SQ modules where possible:
1. `__init__.py` + `midi.py` + minimal `elements.py`: connect → `hello_messages` (native mode) → identity → `on_identified`.
2. Render one test screen line (`add_sysex_display_line`) to prove the display path.
3. `mappings.py`: a `Main_Modes` with **Plugin → Device** and **Mix → Mixer**; wheel pages banks/tracks.
4. One encoder (`LinearSignedBit`) → one Live device parameter; halo + screen value reflect it (skin + display).
5. Unload → `goodbye_messages` (native‑mode exit).

That slice exercises port routing, handshake, `LinearSignedBit` parsing, template switching, screen SysEx,
Live parameter control, skin/color feedback, and teardown — then expand modes around proven behavior.

---

## 7. Practical note on obtaining the framework
The `ableton.v3.control_surface` framework ships **inside Live 12** (`MIDI Remote Scripts/`). The Atom SQ
script imports it; our Motion 32 script will too. Develop against a Live 12 install; the Atom SQ folder is the
working reference for every import and idiom we need.
