# Motion 32 — Implementation Notes (hard-won, from building the live script)

Practical knowledge discovered while getting the Ableton script actually running on hardware
(firmware 1.0.6, DAW Mode Off). Where this contradicts the older design docs, **this file wins** —
it's from real device behavior. Current build = rebased on the clean bootstrap structure; **handshake,
transport input, and transport LED feedback are working.**

---

## 1. The identity-handshake gotcha (the big one)

**Do NOT use `Specification.identity_response_id_bytes` for the Motion.** The Motion's Universal
Identity Reply is:

```
F0 7E 7F 06 02  08 00 00 26  00 00 01 00 06  F7
                 ^^ Fender    ^^ device/fw
```

The Fender id `08` and device id `26` are **non-contiguous** (`08 00 00 26`). The framework's
`identity_response_id_bytes` match expects the id bytes contiguous, so it never matches → the
framework treats the device as *not identified* → the Motion stays in a **pre-native button state**.

**Symptom of the pre-native state:** transport buttons emit `0x66/0x67/0x68/0x69` instead of the
native `0x6F/0x6D/0x6B/0x69`. (This wasted a lot of time — we briefly "corrected" `midi.py` to the
`0x66` values, which was wrong.) The **screen SysEx still works** in this half-state, which masks
the problem.

**The fix (matches what Studio Pro actually does):**
```python
hello_messages = (NATIVE_MODE_ON_MESSAGE, IDENTITY_REQUEST_MESSAGE)  # 8F 00 7F, then F0 7E 7F 06 01 F7
goodbye_messages = (NATIVE_MODE_OFF_MESSAGE,)
# do NOT set identity_response_id_bytes
```
Parse the reply yourself in `receive_midi` (see `protocol.py` `parse_identity_reply`). Once the
device gets the native-on + identity request this way, it fully enters native mode and transport
emits the correct `0x6F` etc.

> Corrects: `Motion32_Ableton_Build_Handoff.md` §4 and `Motion32_Ableton_Script_Structure.md` §1/§4,
> which recommend `identity_response_id_bytes` + `on_identified`. That path does not work here.

### 1a. The firmware bytes are at **fixed offsets** — and `protocol.py` currently gets them wrong

Settled from `Motion32MidiDevice.js` (`IdentityReplyMessage`), which is authoritative:

```js
getFirmwareMajor(data, mfrId) { return parseInt(data[10 + mfrId.length].toString(16)); }
getFirmwareMinor(data, mfrId) { return parseInt(data[11 + mfrId.length].toString(16)); }
getFirmwarePatch(data, mfrId) { return parseInt(data[12 + mfrId.length].toString(16)); }
getFirmwareBuild(data, mfrId) { return parseInt(data[13 + mfrId.length].toString(16)); }
// kFenderManufacturerSysExId = [0x08]  ->  mfrId.length == 1
```

`data` **includes** the leading `0xF0` (the same function checks `data[3] == 0x06 && data[4] == 0x02`).
So with Fender's 1-byte manufacturer ID the absolute offsets are:

| Field | Offset | Value in our capture |
|---|---|---|
| major | `data[11]` | `0x01` |
| minor | `data[12]` | `0x00` |
| patch | `data[13]` | `0x06` |
| build | `data[14]` | `0xF7` ← **this is the SysEx terminator** |

```
F0 7E 7F 06 02 08 00 00 26 00 00 01 00 06 F7
 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
                              ^maj ^min ^pat ^"build"
```

Two consequences:

1. **Ignore the build byte.** Our 15-byte reply has `0xF7` at `data[14]`, so Fender's own build read
   lands on the terminator (`parseInt("f7")` → `NaN` in JS). Build is not used in the version gate, so
   this is harmless — but don't log it as if it were real.
2. 🐛 **`protocol.py` has a live bug.** `parse_identity_reply` reads firmware from `payload[-4:]`, i.e.
   `message[10:14]` = `00 01 00 06` → it reports firmware **0.1.0** and computes a version code of
   **10**, which is `< 1003` and therefore emits a spurious "firmware older than the supported minimum"
   warning on every load. Fix: read absolute `message[11]`, `[12]`, `[13]`; drop the build field.
   (§6 below previously claimed firmware 1.0.6 was being logged correctly — that was written from the
   earlier build. Re-check `Log.txt` after the fix.)

Also note the decode is **BCD-style, not binary**: `parseInt(byte.toString(16))`. In Python that is
`int(f"{byte:x}")`, so `0x10` decodes to **10**, not 16. And the version rule
(`major*1000 + int(f"{minor}{patch}")`) is a string concatenation of minor and patch — 1.0.6 → `1006`;
required minimum is `1003` (`$MOTIONSHARED_REQUIREDFIRMWAREVERSION`).

---

## 2. Native transport CCs are the surface.xml values (confirmed)

Verified by an official Studio Pro MIDI capture (DAW Off): pressing Stop/Play/Record/Tap emits
`0x6F / 0x6D / 0x6B / 0x69` — exactly `Motion 32.surface.xml`. The surface XML **is** reliable for
input in true native mode; the `0x66-0x69` we saw was purely the pre-native handshake bug above.
DAW Mode (Logic/Ableton/Cubase) is a *separate* MCU-style profile — keep it **Off**.

---

## 3. LED feedback — colors + brightness (from Motion32Component.js)

Each button LED takes **two things**: a state byte on the base channel and an RGB triple.
- State (status `0xB0 <cc> <v>`): `kOn = 127`, `kDimmed = 63`, `kOff = 0`.
- RGB (status `0xB1/0xB2/0xB3 <cc> <r|g|b>`, 0-127 each).
- The intended resting brightness for "inactive but present" is **63 (dim)**, not 0
  (`configureLEDHelperParams` sets the off-state to `kDimmed`). So buttons sit dim at rest, full
  when active.

Source colors (`MotionSharedColors` / `Motion32Colors`):
`kButtonDefault #0069CC` (blue), `kRecordActive` red, `kStopActive` orange, `kModifierKey` magenta,
`kButtonSelected` / alt / flash white, `kChannelSolo` yellow, `kChannelMute` red,
`kControlLinkGlobalAssigned #4fd3ff`, `kControlLinkFocusAssigned #fcca03`.

**In ableton.v3 terms:** the button element must be `is_rgb=True`, and the skin color a
`ComplexColor` with one `ColorPart` per RGB channel (1/2/3) plus a channel-less `ColorPart` for the
state byte. State-only `BasicColors` render dim/colorless. `pressed_color` on a `ButtonControl`
gives the "flash white on press." Setting `control.color` at runtime reflects dim↔full state.

Implemented transport behavior: Play dim-green→full-green; Record dim-red→full-red; Stop steady
orange + white flash; Tap steady blue + white flash; Shift magenta.

**Confirmed against a Studio Pro project-load capture (2026-07-25).** The resting colours it
actually sends are exactly what we chose, so this is no longer inference from the JS:

| Control | CC | State | RGB (7-bit) | ≈ Hex |
|---|---|---|---|---|
| Play | `0x6D` | 63 dim | `(0, 64, 0)` | green |
| Record | `0x6B` | 63 dim | `(127, 0, 0)` | red |
| Stop | `0x6F` | 127 on | `(127, 82, 0)` | orange |
| Shift | `0x1F` | 63 dim | `(127, 0, 127)` | magenta |
| Control | `0x23` | 127 on | `(127, 127, 127)` | white |

> This **corrects** the previous parenthetical here, which said Play's green was our choice and
> that the source default was blue. Studio Pro sends dim green at rest. Also note Play and Record
> sit **dim** while Stop sits **full** — the "inactive but present = dim" rule applies to the
> controls whose function is currently inactive, not to every idle button.

---

## 4. ableton.v3 framework API gotchas (all cost a failed load)

- **Never pass `channel=` to the matrix element helpers.** `add_matrix` (and therefore
  `add_encoder_matrix` / `add_button_matrix`) supplies `channel` to `create_encoder` /
  `create_button` itself, so an explicit one is a duplicate:
  ```
  TypeError: ableton.v3.control_surface.elements_base.create_encoder()
             got multiple values for keyword argument 'channel'
  ```
  This aborts `_create_elements` and the whole script fails to load. Confirmed on hardware
  2026-07-25 (Live 12, `elements_base.py` line 435). The **singular** `add_encoder` /
  `add_button` / `add_modifier_button` **do** accept `channel` — the conflict is specific to the
  matrix helpers. The factory Atom SQ omits it: `add_encoder_matrix([[...]], "Encoders",
  map_mode=MapMode.LinearSignedBit, sensitivity_modifier=self.shift_button)`. The Motion is on
  MIDI channel 1 (0-based 0), which is the default anyway. Regression-guarded by
  `tests/test_screen.py::test_matrix_helpers_are_not_passed_channel` (an AST check — a regex
  version false-positived on the warning comment).
- **Never shadow a `Component` attribute in a subclass.** From `component.pyc`:
  ```python
  def __init__(self, name='', parent=None, register_component=..., song=None,
               layer=None, is_enabled=True, is_private=...):
      self.name = name; self.is_private = is_private; self._parent = parent
      self._explicit_is_enabled = is_enabled; self._recursive_is_enabled = True
      self._is_enabled = ...; self._song = song; self._layer = layer
      self._child_components = ...; self._has_task_group = False
      self._initializing_children = ...
      if self._parent:
          with self._initializing_children():
              self._parent.add_children(self)
  ```
  plus properties `application`, `song`, `parent`, `is_root`, `layer`, `canonical_parent`,
  `num_layers`, `any_clipboard_has_content`, `_tasks`. Defining any of those on a subclass breaks the
  base class. A read-only `_song` property produced
  `AttributeError: property '_song' of 'MotionScreenComponent' object has no setter` and the
  component failed to build (confirmed on hardware 2026-07-25). `Component.song` simply returns
  `self._song`, so use `self.song` — don't invent an accessor with a reserved name.
  Regression-guarded by `test_components_do_not_shadow_framework_attributes`.
- **Do not pass `parent=<the ControlSurface>` to a component.** When `parent` is truthy,
  `Component.__init__` calls `self._parent.add_children(self)`, and a `ControlSurface` is not a
  `Component`. (Moot once you register via `component_map` as above — the framework constructs it
  correctly. Recorded because the Atom SQ Plus add-on *appears* to pass `parent=self`: it consumes the
  argument in its own `__init__` and never forwards it, so the framework receives `parent=None` and
  the branch is never taken. Easy to misread as "passing parent works".)
- **A `control_list` event handler takes `(self, control)` — the index is `control.index`.**
  Not `(self, index, control)`: that is the **2D `control_matrix`** shape, and mixing them up raises
  `TypeError: ... missing 1 required positional argument` on the first press. Confirmed against the
  framework's own `ActiveParameterComponent.touch_controls` and
  `SessionComponent.stop_track_clip_buttons`, both of which read `button.index`. A plain
  `ButtonControl` handler takes `(self, value)`. Guarded by
  `test_control_handlers_have_the_framework_arity`.
  > Worth knowing: `ActiveParameterComponent` implements *this exact feature* — reveal a parameter on
  > touch, clear it after a timeout — with `task.sequence(task.wait(self._timeout),
  > task.run(partial(self._on_touch_control_release, button.index)))`. If we ever want the framework
  > to own the behaviour instead of our screen component, that component is the drop-in.
- **`Component.application`, `song`, `parent`, `layer`, `is_root` and `_tasks` are PROPERTIES.**
  Calling one raises at runtime — `self.application()` gives
  `TypeError: 'Application' object is not callable`, which reached hardware. But `is_enabled()`,
  `disconnect()`, `set_enabled()` and `add_children()` genuinely *are* methods, so the distinction
  cannot be guessed from the name. Guarded by `test_framework_properties_are_never_called`, which
  derives the property list from the class-body bytecode (a decorator loaded immediately before a
  `STORE_NAME`) rather than from memory.
- **Give every `@listens` handler `*a`.** The handler is called with whatever the notifier passes, and
  that differs per property: `notify_parameters()` passes nothing, while `selected_mode` passes the new
  mode. A handler declared `def _on_selected_mode_changed(self)` raised
  `TypeError: takes 1 positional argument but 2 were given` the moment a mode button was pressed —
  inside a Live callback, so it surfaced as a `RemoteScriptError` wall rather than a clean failure.
  `*a` is correct for both shapes. Guarded by `test_listens_handlers_tolerate_a_payload`.
- ControlSurface method is **`_send_midi`**, not `send_midi`.
- There is **no `log_message`** — use the stdlib `logging` module; Live routes it to `Log.txt`.
- Skin values must be **Color objects** (have `.draw()`), never raw ints — `'int' object has no
  attribute draw'`.
- An element name that normalizes to an `add_*` method shadows it: **`"Add_Button"` breaks
  `add_button()`** → use `"Add_Mode_Button"`.
- The Remote Scripts **folder name cannot contain spaces** (`import Motion 32` is a SyntaxError) →
  `Motion32`.
- Overriding a built-in component name in `component_map` (e.g. `"Transport"`) works.
- USB IDs: Fender vendor **7896** (0x1ED8), Motion 32 product **513** (0x0201) — enables auto-load.

---

## 5. Clean teardown — exact values, from a full shutdown capture

On exit Studio Pro **releases every LED and screen element, then** sends `8F 00 00` last. The
ordering was recorded here from the start and is correct; a 2026-07-25 MIDI capture of a full
shutdown pinned down the **values**, which matter more than the ordering.

> ⚠️ Note on provenance: `Motion32MidiDevice.js` `onExit()` appears to send `8F 00 00` *first* and
> then call `super.onExit()`. Reading only that function suggests no reset happens at all — a
> conclusion this doc briefly adopted and the capture disproves. The resets come from the base
> class's handler teardown, which runs **before** `onExit`. **Trust the capture over a partial
> read of the JS.**

### 5.1 LEDs — state off, colour WHITE (not black)
Four messages per address:

| Channel | Status | Value |
|---|---|---|
| 1 | `0xB0` state | `0` |
| 2 | `0xB1` red | `127` |
| 3 | `0xB2` green | `127` |
| 4 | `0xB3` blue | `127` |

Pads get the same, with the **state written twice** per note (the state and animation handlers
both release the same address). Colour-only handlers — the touch-strip LEDs — receive channels
2/3/4 with no channel-1 state byte.

Addresses seen in the capture: all bank buttons `0x00`–`0x07`, encoders `0x0E`–`0x15`, wheel
`0x1D`, Shift `0x1F`, LCD buttons, **touch-strip 1 LEDs `0x37`–`0x3F`**, mode/octave/solo/mute
`0x40`–`0x4B`, nav `0x57`/`0x59`/`0x5A`/`0x66`, transport `0x69`/`0x6B`/`0x6D`/`0x6F`,
**touch-strip 2 LEDs `0x70`–`0x78`** (which covers the wheel-push address).

### 5.2 Screen — empty, white, VISIBLE, regular font
Per element, e.g. `F0 08 26 21 01 03 01 …`:

| attr | Value | Meaning |
|---|---|---|
| `0x00` text | *no data bytes* | empty string |
| `0x01` colour | `7F 7F 7F` | white |
| `0x03` visible | `01` | **shown** |
| `0x04` font | `00` | regular |

No `attr 0x02` (value) writes, and **no template-select** at the end. Only the elements the host's
handlers owned are touched (templates 0, 1 and 3 in the captured session; template 2 was unused).

🐛 **This is what caused a real bug.** Our teardown blanked to *black* and *`visible=0`*, which
left the Motion's screen dark after unload — its standalone UI draws into the same persistent
screen elements and inherited hidden-and-black from us. Releasing to empty-but-visible white fixes
it. Constants live in `midi.py` as `RESET_*`; regression-tested by
`test_teardown_matches_the_factory_release_state`.

---

## 6. Current build state

> For the authoritative snapshot see `Motion32_Build_Roadmap.md` §2. This section keeps only the
> module inventory; §6a onwards is the chronological record of what was learned building each piece,
> which is the part worth reading before touching the code.

20 modules: `__init__.py`, `midi.py`, `protocol.py`, `elements.py`, `mappings.py`, `skin.py`,
`colors.py`, `palette.py`, `screen.py`, `formatting.py`, `display.py`, `notification.py`,
`screen_component.py`, `parameters.py`, `leds.py`, `pads.py`, `keyboard.py`, `wheel.py`,
`transport.py`, `runtime.py` — plus `tests/test_screen.py`.

**Phases 0-3 are done and running on hardware:** handshake/native mode, identity parse (offsets fixed
— §1a), clean teardown, transport with Shift variants, Song mode on Template 3, Plugin mode on
Template 0, 8 encoders with halos, the big wheel, per-mode soft buttons, parameter banking and device
navigation.

**Not started:** Edit mode, Mix mode (Template 2), the menu *list* view (Template 1) that Scale/Chord
and browser navigation both need, A–H pad banking, touch strips, the Shift pad-command layer, Session
mode.

Pads, the playable keyboard, Octave ± and the notification bar are **done** — §6b-16…§6b-26.
Template 1 is already partly claimed by the notification bar, so a future menu list view has to
settle ownership of those elements with it rather than assume the template is free.

### 6a. Framework facts learned while building Phase 2

- **`component_map` DOES register brand-new components** — an earlier note here said the opposite and
  was wrong. `ComponentMap._create_component_map` builds the built-ins and then ends with
  `self.update(specification.component_map)`, so a new key like `"Motion_Screen"` sits alongside them.
  `ComponentMap.__getitem__` instantiates lazily (`factory(is_enabled=False)`) **inside the surface's
  dependency guard**, which is what supplies `self.song` and, crucially, the injected
  `parent_task_group` behind `self._tasks`. A hand-built component gets neither — `self._tasks` fails
  outright, so timers are impossible. **Always register; never hand-build.**
- **The mapping engine decides what a `create_mappings` key means** (`control_surface_mapping.pyc`
  `setup()`): keys that name something in `component_map` become that component with a `Layer` built
  from the entry; **every remaining key becomes a `ModesComponent`.** That is how `Main_Modes` exists
  without being a built-in. Inside a modes section, a **string** value binds a mode button
  (`plugin_button="plugin_button"`), a **dict** defines a mode, and a mode may hold `modes=[…]` to
  enable several components at once. `add_mode` creates the `<name>_button` control per mode, so a
  declared mode button with no matching mode binds a control that was never created.
- Verified-good element signatures, from the readable Atom SQ Plus source and the factory bytecode:
  `add_encoder(cc, "Name", map_mode=MapMode.LinearSignedBit)`,
  `add_encoder_matrix([[ccs]], "Encoders", map_mode=..., sensitivity_modifier=self.shift_button)`,
  `add_button(cc, "Name", is_rgb=True, msg_type=...)`, `add_modified_control(control, modifier)`.
- Verified-good `create_mappings` keys: `"Device"` accepts `parameter_controls`, `prev_bank_button`,
  `next_bank_button`, `device_lock_button`, `device_on_off_button`; `"Device_Navigation"` accepts
  `prev_button` / `next_button`.
- **Output ordering trap.** Components are constructed during `ControlSurface.__init__()`, but
  `_send_midi` isn't usable that early. The screen model therefore starts **suspended** and is
  released in `setup()`. Without that, the first paint is silently dropped *and* the cache records it
  as sent — a screen that stays blank with nothing pending.
- The screen cache needs **both** halves reset together: `ScreenModel.invalidate()` (forget what the
  device has) and `MainView.forget()` (forget the last content snapshot). Doing only the first leaves
  the view short-circuiting on an unchanged snapshot, so nothing is redrawn.

### 6b-1. ~~Open question~~ RESOLVED — the framework source is now in the repo

`control_surface/` (Live 12's `ableton/v3/control_surface/`, as `.pyc`) is now in
`Motion32/Resources/`, and `xdis` decompiles it. **This should be the first stop for any future
framework question** — it turned three guesses into facts and found a bug that hardware testing would
have shown only as "all the halos read zero".

**`DeviceComponent` (`components/device.pyc`) — pinned:**

| Fact | Consequence for us |
|---|---|
| `parameters` property → `self._provided_parameters` | This is the accessor. The earlier probe chain is deleted. |
| `parameters` is a **`listenable_property`**; `_update_parameters()` calls `self.notify_parameters()` | A **public change signal.** `@listens("parameters")` with the Device component as subject fires on device change *and* bank change — which is what makes banking safe to map (see §6a). |
| The list holds **`ParameterInfo`**, not raw parameters — `ParameterInfo(parameter=…, name=…)`, from `parameter_info.pyc` | 🐛 **Bug caught before hardware.** Reading `.min`/`.max`/`.value` off a `ParameterInfo` raises `AttributeError`, so every encoder halo would have rendered 0 while the labels looked fine. Label comes from `info.name`, value from `info.parameter`. |
| `info.name` vs `parameter.name` | Prefer `info.name`: Live's curated bank definitions rename parameters per bank, and the info object carries the bank-specific label. Using `parameter.name` would silently show the wrong text on banked devices. |
| `bank_name` / `bank_index` properties | The screen can show Live's **real** bank name ("Filter", "Envelope") instead of a synthetic "n/m" counter. |
| `__getattr__` forwards any `set_*` containing `"bank"` to `_bank_navigation_component` | Explains why `prev_bank_button` / `next_bank_button` are valid keys under `component="Device"` even though they live on `DeviceBankNavigationComponent`. |

**`create_skin` (`default_skin.pyc`) — pinned:** it builds `[default_skin, our_skin, colors]` and
calls `merge_skins(*skins)`. **Our partial `Skin` merges *over* the framework defaults**, so missing
keys fall back rather than failing. That removes the "unknown skin key" hazard that was holding back
`Device_Navigation`. Verified present in `DefaultColors`: `Device.{On,Off,FoldOn,FoldOff,LockOn,
LockOff,Navigation,NavigationPressed}` and `Device.Bank.{Selected,NotSelected,Navigation,
NavigationPressed}`. The full default skin also lists `Transport`, `Mixer`, `Session`, `ViewControl`,
`ViewToggle`, `Recording`, `UndoRedo`, `ClipActions`, `DrumGroup`, `NoteEditor`, `LoopSelector`,
`Clipboard`, `TargetTrack`, `Translation` — worth consulting before hand-defining colours in later
phases.

Consequently **banking and device navigation are now mapped** (Left/Right = parameter bank, Up/Down =
device focus), and the one-shot introspection probe has been removed.

### 6b-2. Hardware findings from the first working screen (2026-07-25)

The screen loaded and drew titles and parameter names correctly. Three things came out of it.

1. **The device view belongs on the Plugin button, not on all the time.** Now implemented as a
   `Main_Modes` modes component: `song` (default) and `plugin`. The encoders are mapped **only inside
   plugin mode**, so they cannot move parameters while another view is on screen. Nav buttons are
   per-mode too — song: track/scene navigation; plugin: bank (left/right) and device tabbing
   (up/down). Edit and Mix remain deliberately unmapped: a declared mode button with no matching mode
   binds a control the framework never created, and those views are not designed yet.
2. **Parameter values were missing.** Template 0's encoder tile has exactly **one** text element
   (element 2), so name and value must share it — which is precisely why the factory shows the name at
   rest, the value while an encoder is touched or turning, then reverts. The surface XML confirms this:
   both `titleParam` and `valueParam` are written to `MOTION32_SCREEN_MAIN_ENCODER_LABEL_CC_ENC`
   (lines 2142-2143). Implemented with the framework's own timeout,
   `ACTIVE_PARAMETER_TIMEOUT = 0.75 s` (`control_surface/consts.pyc`), via `self._tasks` +
   `task.sequence(task.wait(…), task.run(…))` — the same shape as the framework's
   `ActiveParameterComponent`. Touch reveals and holds; release starts the timeout; a value change
   from anywhere (encoder, mouse, automation) also reveals and times out. The value is drawn in
   `VALUE_TRIGGERED` blue to distinguish it from the name.
   > ⚠️ **Deliberate divergence from the factory.** Fender pipes values through `compactify` too, but
   > compactify's first step strips hyphens — so `-12.5 dB` renders as `12.5 dB`, silently flipping
   > the sign. We use `truncate_value()` for values instead (drop the unit, then hard-trim:
   > `-12.5 dB` → `-12.5`). `compactify` remains correct for *names*.
3. **`Got unknown sysex message` warnings** were the framework logging our own identity reply. We parse
   it in `receive_midi` and were then still forwarding it to `super()`; since we deliberately avoid
   `identity_response_id_bytes`, nothing there can match it. `MotionProtocol.handle_incoming` now
   returns a bool and consumed messages are not forwarded. (The warning also independently confirmed
   the reply bytes: `F0 7E 7F 06 02 08 00 00 26 00 00 01 00 06 F7` — firmware 1.0.6 exactly as
   documented in §1a.)

### 6b-3. Modes, and the transport refactor they forced (2026-07-25)

**Mode model chosen.** Song and Plugin as a **radio** (`ImmediateBehaviour`) with Song as the base,
plus `ToggleBehaviour` on Plugin so re-pressing it drops back to Song. This gives the
"toggle in and out" feel *without* a fifth invisible state: exactly one mode button is lit at all
times, so the hardware always says where you are. This also matches the factory decomposition — the
RE shows control-focus (layer 4, Song/Plugin/Edit/Mix) is a strict radio with **no** base, while the
toggling overlays are layer 5 (Add/Scale/Chord/Control/User) on their own buttons.

Available behaviours (`mode/behaviour.pyc` + `mode/__init__.pyc`): `ImmediateBehaviour`,
`LatchingBehaviour`, `MomentaryBehaviour`, `ToggleBehaviour`, `ReenterBehaviourMixin` /
`make_reenter_behaviour`. There is **no** `CancellableBehaviour` (that was v2); `ToggleBehaviour` is
its analogue.

**Session ↔ Arrangement is a view toggle, not a mode.** Bound to **Shift+Song** via
`View_Toggle.main_view_toggle_button`. Keeping it out of the mode system means what the Motion's
screen shows stays independent of which Live window is open — you can have the device screen up while
looking at Arrangement.

**The transport had to be refactored.** `MotionTransportComponent` *replaced* the framework's
`TransportComponent` and re-implemented four buttons against the Live API. That left it with none of
the framework's encoders — and Song mode needs exactly those:
`arrangement_position_encoder`, `loop_start_encoder`, `loop_length_encoder`, `tempo_coarse_encoder`,
`tempo_fine_encoder`, `cue_encoder` (plus `ZoomComponent`'s `horizontal_zoom_encoder` /
`vertical_zoom_encoder`). It now **subclasses** `TransportComponent` and keeps only `record_button`,
which the framework genuinely lacks (Live's record lives in `Recording` /
`View_Based_Recording`, which are shaped around record *modes*). Undo moved to the `Undo_Redo`
component. Play/Stop/Tap/Loop/Metronome/Capture now come from the framework.

Two consequences to remember:

- **Skin keys must match what the framework asks for.** `TransportComponent` requests
  `Transport.PlayOn/PlayOff/StopOn/StopOff/StopPressed/LoopOn/LoopOff/MetronomeOn/MetronomeOff/`
  `TapTempo/TapTempoPressed/CanCaptureMidi/…`. Our old skin defined `Transport.Stop` and
  `Transport.Tap`, which nothing reads — they silently fell back to the framework default. Renamed.
- **`{name}_raw[i]` addresses one element of a matrix.** `ElementsBase.add_matrix` calls
  `_add_raw_elements`, which creates `"{}_raw".format(name)`. So `encoders_raw[0]`…`[7]` bind
  individual encoders, which is how Song mode splits the eight across Transport and Zoom while
  Plugin mode binds the whole `encoders` matrix to `Device.parameter_controls`.

**A guard I had to relax.** An earlier test forbade a component appearing both globally and inside a
mode. That is wrong — the factory scripts bind global `Transport` buttons *and* per-mode `Transport`
encoders, and so do we. The real invariant is about **elements**: no element may be bound twice in
layers that are live simultaneously (global + any one mode), and reuse across two different modes is
fine because they are mutually exclusive. The test now checks that instead.

### 6b-4. The offline-test blind spot (2026-07-25)

Two errors reached hardware in one release, and both were the *same* structural gap rather than two
unrelated slips:

1. `_get_song()` was deleted during the move to framework registration (which supplies `self.song`),
   but `_song_content()` still called it → `AttributeError` on every render.
2. `_on_selected_mode_changed(self)` didn't accept the payload `selected_mode` passes → `TypeError`
   the moment a mode button was pressed.

**Why the suite missed them.** `test_screen.py` deliberately covers only the framework-free modules —
`display`, `screen`, `formatting`, `protocol`, `parameters`, `midi` — because those are the ones it can
import. `screen_component.py` and `transport.py` import `ableton.v3`, so they were never *executed*
offline, and nothing checked them beyond `py_compile` (which happily accepts a call to a method that
doesn't exist).

**The fix is static analysis, not more stubbing.** Two new checks:

- `test_no_self_reference_is_undefined` resolves every `self.X` in our `Component` subclasses against
  the names defined in the class **plus the real framework members**, extracted from
  `Resources/control_surface/component.pyc` and `components/transport.pyc` (105 names resolved; falls
  back to a small hardcoded set if the framework copy is absent). This catches a deleted or renamed
  method immediately.
- `test_listens_handlers_tolerate_a_payload` enforces `*a` on every `@listens` handler.

A third followed on the next run: the encoder-touch handler was declared `(self, index, control)`
(the `control_matrix` shape) instead of `(self, control)`, so the first touch raised `TypeError`. Guard
added: `test_control_handlers_have_the_framework_arity`.

All three were verified by reintroducing the original bug and confirming the test fails. The general
lesson: **for the framework-importing modules, offline checks have to be structural** — the suite
cannot execute them, so it must reason about them instead. What that now covers automatically:

| Guard | Catches |
|---|---|
| `test_no_self_reference_is_undefined` | a deleted/renamed `self.` helper (resolves against the class + 105 real framework names) |
| `test_listens_handlers_tolerate_a_payload` | `@listens` handler arity |
| `test_control_handlers_have_the_framework_arity` | `control_list` vs `control_matrix` vs plain control handler shapes |
| `test_components_do_not_shadow_framework_attributes` | shadowing `_song`, `_parent`, `song`, `name`, … |
| `test_matrix_helpers_are_not_passed_channel` | `channel=` on a matrix element helper |

**The pattern behind all of it:** every one of these failures was an *API shape* assumed rather than
read, in a module the test suite cannot execute. When touching those two files, the order is: find the
same construct in `Resources/control_surface/`, copy its shape, then add a structural guard.

### 6b-5. The script-reload race — module state and hardware teardown (2026-07-25)

Symptom: after the mode work, the screen went **completely blank with nothing in the log**, while the
encoders and mode switching worked fine. Two distinct bugs of the same shape, both invisible:

**Live constructs the replacement `ControlSurface` *before* disconnecting the old one.** Every script
reload — re-selecting the control surface, or editing a file — therefore runs, in order:
new `__init__` → new `setup` → **old `disconnect`**. Two consequences:

1. **Module-level state gets wiped by the wrong instance.** `runtime.py` holds the screen model for
   components to read (they cannot be handed constructor arguments). The old instance's `disconnect()`
   called an unscoped `runtime.clear()`, deleting the *new* instance's references. Every later redraw
   then found no model and returned silently. `publish`/`clear` are now keyed by owner, and
   `clear(owner)` is a no-op — returning False — when a newer instance has taken over.
2. **Worse: the old instance resets hardware the new one already drew on.** Our teardown deliberately
   clears every LED and blanks the screen before the native-mode goodbye (§5). Run *after* the new
   instance has painted, that blanks a live screen. `disconnect()` now uses `runtime.clear(self)`'s
   return value as the ownership test and skips the hardware reset entirely when superseded.

> **General rule for remote scripts:** any module-level state must be owner-scoped, and any teardown
> that touches the hardware must first ask "am I still the live instance?". Neither failure produces an
> exception, so neither shows up in a log.

**And a process failure worth recording.** The guards added for robustness — `try/except` around render,
content, flush and `_send_midi`, plus an early `return` when the model was missing — were written to
keep a bad frame from wedging the surface. They also made this class of bug undiagnosable: several
logged nothing at all, and `_send_midi` failures were logged only once. Diagnostics added: `flush()`
reports how many messages it sent (and says so when suppressed by the suspend gate), `full_redraw` logs
mode/suspended/pending, `_render` distinguishes a content failure from a render failure from a flush
failure, a missing model/view is now a **warning** rather than a silent return, and dropped `_send_midi`
calls log the first three with tracebacks. **A guard that swallows must still say that it swallowed.**

### 6b-6. Making the screen feel live (2026-07-25)

With the reload race fixed, Song mode drew correctly and revealed values on touch. Three follow-ups,
all the same underlying mistake: **content read at render time with nothing to trigger the render.**

1. **Values updated in batches, not smoothly.** The Song-mode readouts come from song properties, but
   the only things causing a render were touch events, device-parameter listeners and mode changes — so
   a value refreshed whenever something *unrelated* happened. Fixed two ways:
   - **Listeners** for `tempo`, `loop_start`, `loop_length`, `signature_numerator`.
   - **A 20 Hz live refresh while a value is actually on screen.** Arrangement position, zoom and cue
     have no single property to subscribe to — they are driven by the framework's Transport/Zoom
     components mutating Live, and `current_song_time` fires far too often to listen to. So while any
     tile is revealing a value, re-read on a repeating `self._tasks` timer and stop when the last value
     times out. The `ScreenModel` diff makes this cheap: an unchanged value sends **nothing**, so wire
     traffic only happens while a number is genuinely moving.
2. **The track name lagged.** No listener on `song.view.selected_track`, and none on the selected
   track's `name`. Both added — note they are *different* events (selecting another track vs renaming
   the current one) and Song mode's title depends on both.
3. **Plugin mode "showed nothing".** It was rendering fine — the log showed repeated 36-message
   flushes on each mode toggle — but on a fresh Live set with no devices, `_device_content()` produced
   `title=""`, `centre="No device selected"` and eight empty tile labels. **An empty screen is
   indistinguishable from a broken one.** It now shows the focused track's name as the title, states
   "No device selected", and labels every tile `-` so the layout still reads as a device view. The
   device lookup also falls back to `song.appointed_device` when the Device component reports none
   (it does not report one until its layer has been granted, which is exactly the first render after
   switching into Plugin mode).

**Diagnostics lesson, part two.** The flush log added in §6b-5 logged *every* flush, which was fine for
a static screen and would have flooded Log.txt at 20 Hz. It now only reports flushes of ≥10 messages —
the full repaints, which are the interesting events — and the suspend-gate suppression. Instrumentation
has to survive the traffic it is meant to observe.

### 6b-7. Silent binding failures, and a late-binding rule (2026-07-25)

**An unknown control name in a `Layer` fails silently.** No exception, no log line — the button
simply never does anything. `Device_Navigation` was mapped with `prev_button`/`next_button` for
several rounds; it extends `ScrollComponent`, whose controls are
**`scroll_up_button` / `scroll_down_button`**, so device navigation was quietly absent the whole
time. (`Motion32_Build_Roadmap.md` Appendix A lists `prev_button`/`next_button` for this component;
that came from Atom SQ bytecode and is wrong for Live 12's framework — corrected there.)

Now guarded by `test_every_mapped_control_name_exists`, which resolves every mapped control name
against the target component's real names, extracted from the framework `.pyc`. Two subtleties the
guard has to encode:

- **Bases must be listed explicitly** — class inheritance is not recoverable from bytecode, so
  `Device_Navigation` is checked against `device_navigation.pyc` *plus* `scroll.pyc`, and `Device`
  against `device.pyc` plus `device_parameters.pyc` and `device_bank_navigation.pyc` (it forwards
  `set_*bank*` and `set_parameter_controls` to those sub-components).
- **Background components are wildcards.** `BackgroundComponent.__getattr__` synthesises
  `set_<anything>`, which is the point of a background — it grabs arbitrary elements so they don't
  leak into other layers. `Modifier_Background` and `Translating_Background` accept any name and are
  skipped.

**The late-binding rule.** The screen showed a device title and bank name but *no parameters*, and
bank changes never repainted. Cause: the framework constructs components **during**
`ControlSurface.setup()`, but the surface binds the Device component to the `ParameterSource`
*after* `super().setup()` returns. The screen component's `__init__` therefore saw
`source.component is None`, silently skipped subscribing to `parameters`, and froze `_entries` at
eight empty slots forever. Title and bank name still worked because those are read fresh at render
time — which is exactly why the failure looked partial and confusing.

> **Rule: anything handed to a framework-built component after `super().setup()` needs an explicit
> late-binding hook that both subscribes and re-reads state.** This is the third bug from this
> ordering (see also §6a on `_send_midi` before setup, and §6b-5 on the reload race). The hook here
> is `bind_parameter_source()`, called from `setup()` right after `bind_device_component()`, and it
> warns if there is still no Device component to follow.

### 6b-8. Template 3 identified; Song mode moved to it (2026-07-25)

A photograph of Studio Pro's Song mode **confirmed Template 3** as the factory's Song/Timeline view,
closing a standing `[INF]` in the screen map. Details and the evidence are in
`Motion32_Screen_Template_Map.md`; the consequences for the build:

**The screen widget vocabulary is fixed and small.** Five attributes exist protocol-wide — text,
colour, value, visible, font — across all 433 handlers. There are exactly two screen messages
(`0x20` select, `0x21` update) and **no image path**. The firmware is LVGL and contains `lv_label`,
`lv_bar` and `lv_arc`, but **not** `lv_img` or `lv_canvas`, so bitmaps are impossible on this device,
not merely unsupported by the protocol. What "widgets" we have are the 181 pre-instantiated elements:

| Template | Text | Graphical |
|---|---|---|
| 0 Main | title (13, bold), **1 label per tile (7)**, centre text, 8 soft-button labels | **8 encoder arcs** (`value`) |
| 1 Menu | title, **2 × 6 rows** (colour + bold each), 4+4 button labels | none |
| 2 Mixer | channel number + name ×8 | **fader, mute, solo, meter L/R** ×8 + colour swatch |
| 3 Params | title, **label + value per tile ×8**, centre bar, 4+4 button labels | **none — text only** |

**Song mode now renders on Template 3** (`display.ParamsView`), Plugin mode stays on Template 0
(`MainView`). The trade is deliberate: Template 3 shows a full parameter name *and* its value
simultaneously, which is what tempo/position/loop readouts want; Template 0 keeps the encoder arcs,
which suit a device parameter better than a number. Reveal-on-touch therefore only applies to Plugin
mode now — it existed solely because Template 0 has one text element per tile.

Layout follows the factory: header = which Live view is up (`application().view.is_view_visible`),
grey centre bar = selected track, tiles = full encoder name + live value.

**Two views, one `ScreenModel`.** Cache keys already include the template, so both templates' state
coexists and only `select_template` changes on a mode switch. Returning to an unchanged template
costs **exactly one message** (regression-tested). Two things this requires:
`full_redraw` must call `forget()` on **both** views — the cache was cleared for every template, so a
later switch would otherwise short-circuit on an unchanged snapshot and draw nothing — and the
component tracks `_active_view` so `activate()` runs on change rather than every render.

### 6b-9. Song mode fleshed out (2026-07-25)

Three bugs and a batch of content, all after the Template 3 move:

- **Session/Arrangement lagged.** The header read `is_view_visible()` at render time with nothing
  listening for the view changing. Now subscribed to `application.view` `focused_document_view`.
- **Returning to Song didn't redraw.** `_render` only flushed when the *content* changed — but
  switching away and back leaves content identical, so `render()` short-circuits while `activate()`
  has already queued a **template select** that then never went out. The flush is now
  unconditional; the diff makes it free, and it removes the whole "forgot to flush" class.
  Guarded by `test_render_flushes_unconditionally`, which fails if the flush is ever made
  conditional on `changed`.
- **Mode buttons behaved as mutual toggles.** `ToggleBehaviour` on Plugin meant a second press fell
  back to Song. Fine with two modes; with four peers "toggle off" has no defined destination. Now a
  strict radio, guarded by a test that rejects any per-mode `behaviour` override so Edit and Mix
  cannot reintroduce it.

Song mode now also carries: two-line hints on encoders whose value isn't a number (Cue → "Prev/Next",
zoom → "In/Out"); **cue volume** (`Mixer.prehear_volume_control`) on encoder 8; the four soft buttons
under the screen (view toggle, browser, cue marker, Clip/Device) labelled on screen and lit blue; and
**Solo/Mute on the focused track** via `Target_Channel_Strip` (which extends `ChannelStripComponent`
— that is where `solo_button`/`mute_button` come from).

`SONG_ENCODERS` now carries `(control, label, owning component)` so the per-component layers are
derived rather than hand-maintained, and a test checks every declared owner actually gets a layer.

**One measurement worth keeping:** Fender declares `PARAMS_VALUE_MAXCHARS = 7`, but its own Song
screen renders "Timeline" (8) in that element — so the constant is its numeric-compaction target,
not a device limit. We use 9 on the value line so a two-word hint fits.

### 6b-10. LED ownership on shared addresses (2026-07-25)

The encoder halos took three attempts because **two different framework mechanisms write to the same
CC the halo lives on** — the halo has no address of its own (`Motion32_Control_Surface_Definition.md`
§2.5). Both had to be dealt with:

1. **Parameter feedback.** `EncoderElement` sends the mapped parameter's value on its own CC.
   `EncoderElement.__init__` takes an explicit **`is_feedback_enabled`** flag; passing `False` for the
   encoder matrix and the wheel stops it.
2. **Element reset.** `EncoderElement.install_connections()` calls `reset()`, and `reset_state()` sends
   the element's *off* value. This fires whenever a **layer is granted or released** — i.e. on every
   mode change — and `is_feedback_enabled` does not cover it. Our refresh ran before the framework's
   reset and therefore lost the race: the halos lit in the right colour and immediately went dim.

**The diagnostic that identified it:** encoder 8 kept its colour while 1-7 went dark. Encoder 8 is the
only one bound to a **`MappedControl`** (cue volume), whose reset re-sends the parameter value; 1-7 are
**`StepEncoderControl`s**, whose reset sends zero. A per-control-type difference pointed straight at
element reset rather than at our own code.

**The fix: take the address, don't race for it.** `elements.py` defines `MotionEncoderElement`, an
`EncoderElement` subclass that drops its outgoing writes (`send_value` and `send_midi` — the send path
differs between the reset and feedback routes, and the base is bytecode). Input behaviour and internal
bookkeeping are untouched: `reset()` and `reset_state()` still run, so sensitivity state stays correct,
they just cannot reach the light. `leds.py` becomes the only writer of those addresses.

Wiring it in has one trap, and ⚠️ **this paragraph got it wrong until 2026-07-25** — the correction
cost a failed script load, so read it carefully.

**No matrix *wrapper* accepts `element_factory`.** `add_encoder_matrix` and `add_button_matrix` both
hard-code it and forward it to `add_matrix` as a keyword — decompiling `elements_base.pyc` shows both
carrying the const tuple `('channels', 'element_factory')`, which is exactly the set of kwargs they
pass on. Supplying our own is therefore a duplicate:

```
TypeError: ElementsBase.add_matrix() got multiple values for keyword argument 'element_factory'
```

…and the whole script fails to load. **This is the same trap as `channel=` (§4), one level up**: the
wrapper supplies the argument, so the caller must not.

Only the generic **`add_matrix`** and **`add_element`** take a factory. So:

* the encoder matrix goes through **`add_matrix(..., element_factory=create_motion_encoder)`**;
* the wheel goes through **`add_element(name, factory, …)`**, because the singular `add_encoder` also
  hard-codes the stock factory and silently ignores an override. Missing *that* is why the wheel
  stayed the worst offender after the encoders were fixed.

> 🐛 **How this survived a green test run.** The offline guard asserted
> "`add_encoder_matrix` must pass `element_factory`" — it encoded the wrong belief and then *enforced*
> it, so the suite stayed at 0 failures while Live could not construct the elements at all. A
> structural guard is only as good as the framework reading behind it; this one was written from the
> same wrong assumption as the code it checked. The replacement,
> `test_matrix_wrappers_reject_a_factory`, checks the framework's actual rule (no `element_factory`
> **or** `channel` on either wrapper) rather than our habit, and was verified by reintroducing the
> exact failing call.

> **The rejected fix, recorded so it isn't retried.** The first two attempts re-asserted the LEDs on a
> 150 ms timer after each mode change, with a 2 s heartbeat as a backstop, invalidating the LED cache
> first so the writes weren't diffed away. It half-worked and should not come back: it flickers
> visibly, it costs ~36 messages per beat forever, and anything without an event to hook wins until
> the next beat — turning and clicking the wheel kept knocking its light out. A shared address is an
> ownership problem, not a timing problem. Chasing it as a timing problem cost three rounds.

Regression-tested in `test_encoder_elements_never_write_to_their_own_cc` (the subclass exists, both
send hooks are overridden, the matrix passes `element_factory`, and the wheel is *not* built by
`add_encoder`) — each assertion verified by reintroducing the bug.

**Corollary for LED design generally.** Because the halo is the encoder's own address, a halo cannot
carry transient state safely. The wheel originally went white while pressed; every one of those
transitions was a chance to be left dark, which is what "goes out depending on what it's interacting
with" was. Halos are now **mode-level indicators**: the wheel is lit for the whole of Plugin mode and
dark otherwise, and nothing about using it changes the light. Encoder halos still take a white touch
highlight because capacitive touch is a clean paired press/release from the device, but the same
caution applies to anything new.

### 6b-11. LED addresses verified by hardware capture (2026-07-25)

A Studio Pro project-load capture was decoded byte-for-byte against `midi.py`. **Every address in
our table matched, with no unknowns**, which retires the last of the guesswork on LED addressing:

* **Encoder halos** `0x0E`-`0x15` — all eight set to state **127** and RGB `(0, 52, 102)`
  = `#0069CC`, the factory blue. Confirms both the shared-address model and the value range.
* **Wheel halo** `0x1D` — state **127**, same blue. Identical treatment to the halos.
* **Key LEDs** — notes **36-67** (32 keys, matching `PAD_NOTES`), state on `0x90` and RGB on
  `0x91`/`0x92`/`0x93`, exactly as `Motion32_Handshake_and_SysEx_Spec.md` §Pads claimed. The Chord
  capture shows them carrying a per-key **gradient** (`(0,52,102)`, `(0,37,72)`, `(0,22,43)`,
  `(0,10,19)`…), i.e. brightness falling off across the keybed rather than one flat colour.

Two behavioural facts fall out of the same capture:

1. **Studio Pro never writes state 0 to a halo.** Not once in the burst. Its halos are lit or
   the whole surface is being torn down. This is the strongest argument for the ownership model
   in §6b-10: on this device a dark halo is an exceptional state, not a resting one.
2. **Studio Pro lights the wheel in Song mode too**, even though that template's burst
   (`F0 08 26 20 03 F7` — template 3) gives the wheel nothing to do. We deliberately diverge and
   leave it dark in Song mode: an unlit control that does nothing is honest feedback. Worth
   revisiting if Song mode ever claims the wheel (browser navigation was the candidate).

### 6b-12. The Scale/Chord menus are drawn by the host, not the device (2026-07-25)

This settles the open question about how Studio Pro's Scale and Chord buttons work.

Pressing **Chord** (CC `0x22`) produces *inbound* `B0 22 7F` and then **the host does all the
work**: it blanks the Template 3 elements, writes a full Template 1 menu — `"Progressions"`,
`"Major"`, `"Minor"`, `"Key"`, `"Simple"`, and six progression rows (`"I - V - vi - IV"`,
`"I - IV - vi - V"`, `"I - vi - iii - V"`, …) — repaints the key LEDs, and only then selects the
template with `F0 08 26 20 01 F7`.

So the device is **not** running its own Chord UI while in native mode. The button is an ordinary
input; the menu is host-drawn. Consequences for us:

* Those buttons being dark and inactive in our script is *correct* until we implement the menus.
  There is no "hand it back to the device" option to switch on.
* Integrating Scale/Chord means building a Template 1 `MenuView` (2×6 list) plus the note logic —
  the progression strings in the capture match the `Famous.chords` / `Simple.chords` files already
  catalogued in `Motion32_Source_Inventory.md`, so the *content* is in hand.
* The gradient key-LED writes in the same burst are how Studio Pro shows the chord/scale on the
  keybed, so a faithful implementation has a documented reference to copy.

### 6b-13. The guard that reported success while testing nothing (2026-07-25)

Chasing an assertion-count discrepancy between the docs (1885) and an actual run (1849) turned up
something worse than stale documentation: **`tests/test_screen.py` silently disabled its own strongest
guard on any machine without `xdis`, and still printed "0 failures".**

The whole 36-assertion gap was one test. `test_every_mapped_control_name_exists` fell from 39
assertions to 3, because:

* `_control_names_from_pyc` returns `None` on `ImportError: xdis`;
* `check_section` saw `allowed is None` and returned **with no message** — while the neighbouring
  "empty set" branch did print a warning, so the silent path was the one nobody noticed;
* the backstop `check(checked >= 6, …)` counted sections **visited**, not sections **validated**.
  `checked` was incremented outside `check_section`, so it happily passed at 6+ while every single
  section had been skipped.

**Verified by reintroducing the original bug** — `prev_button`/`next_button` on `Device_Navigation`,
the exact mapping that hid for several rounds (§6b-7):

| Environment | Result |
|---|---|
| bug present, **no** `xdis` | `1849 assertions, 0 failures` — **clean pass** |
| bug present, `xdis` installed | `1885 assertions, 2 failures` — caught |

**The fix.** `check_section` now returns whether it really resolved anything, `checked` counts only
validated sections, and every skip is collected and reported as a **failure** naming the mappings that
went unchecked plus the remedy (`pip install xdis`). A missing `Resources/control_surface` is likewise
a failure rather than an early `return`. `main()` now ends in an explicit `PASSED` / `FAILED` line.
Suite total is **1887** assertions (the two additions are the framework-directory check and the
not-skipped check). All three states re-verified afterwards: clean+xdis passes, clean without xdis
fails loudly and names all seven unchecked mappings, and the reintroduced bug is still caught.

Two things worth carrying forward:

1. **`xdis` is a hard dependency of the test suite, not an optional nicety.** Treat a low assertion
   count as a red flag in its own right — it means guards did not run.
2. **§5's rule needs a second half.** "Reintroduce the bug and watch the test fail" is necessary but
   not sufficient; the bug must also be reintroduced in a *degraded* environment. Every check here
   had been verified once, on a machine that happened to have `xdis` — which is precisely why the
   degradation went unnoticed. This is the same shape as the §6b-5 lesson (**a guard that swallows
   must still say that it swallowed**), one level up: it was the *test harness* doing the swallowing.

### 6b-14. Scale and Chord are host-side — the assumption that cost us the pad-note gap (2026-07-25)

Four folders in `From Studio Pro/` (`Musical Scales/`, `Chorder/`, `Chords/`, `Chord Sounds/`) had
never been cited by any doc, and were missed entirely by the 2026-07-24 source audit. Mining them
settled the project's last blocking question and corrected a guiding principle. **Full write-up in
`Motion32_Scale_and_Chord_Engine.md`;** the short version and the lesson belong here.

**The finding.** In native host mode the Motion's pads send **one fixed note per pad** (36–51 / 52–67)
and *Studio One* applies scale, chord, octave, root and range — via its own `PadSectionComponent`
(`setScale`, `setCurrentOctave`, `setRootOffset`, …) and a chord table it imports at init with
`padSection.chordTriggerModeSettings.importChordProgressions(famousChordsUrl, "Famous")`. The SDK is
explicit that the scale engine is host C++: *"Musical scales supported by
`PadSectionComponent::setScale()`. Keep in sync with host `musicalscales.h`."* The surface XML declares
each pad at a fixed `address="$padIndex+36"`, and `Music.symbolicPitchToPadIndex()` exists precisely so
the host can recover *which pad* from an incoming note.

**Why we believed otherwise, which is the interesting part.** The device genuinely *has* a Scale and
Chord engine, with these same scales and these same progressions, and it genuinely uses them —
stand-alone. The inference that native mode therefore invoked the same firmware assets was reasonable
and wrong. Native mode doesn't share the engine; the host replaces it. **Shared *assets* are not
evidence of a shared *code path*.**

Two supporting mistakes are worth naming:

1. **The 36–86 "evidence" was circular.** The claim that pad output escapes the LED range came from the
   pitch range inside `Famous.chords` — which is the *host's* voicing library. That range is exactly
   what host-side generation predicts. `Motion32_Source_Inventory.md` had already flagged the caveat
   ("the host's chord library, not a dump of the device's engine"); nobody followed the thread.
2. **The audit's completeness claim outran its method.** It concluded "nothing substantial is left
   unmined" after walking the files *named by the manifest* plus the loose files beside them. It never
   enumerated the package's subdirectories, so four folders no manifest attribute points at were
   invisible. Enumerate the tree, not the manifest — and don't state completeness more strongly than
   the enumeration supports.

**What it unblocks.** The pad musical-note capture — carried as the single genuinely blocking item
since the start, and the reason Session mode was deferred — is closed by source. There was never a
firmware transform to capture.

**What it obliges.** Note generation is ours, which makes latency our problem. The framework's note
translation (`PlayableComponent._note_translation_for_button` → element `identifier`/`channel`) is a
**static 1:1 remap** recomputed only on change, so a scale layout costs nothing at play time. A chord
cannot be expressed that way, and generating notes in Python would put our thread — serviced on a
timer, not per MIDI event — directly in the pad→note path. Design consequences and the rejected option
are in `Motion32_Scale_and_Chord_Engine.md` §5.

> Still to read before building: `_set_pad_translations` is called in `drum_group.pyc` but defined in
> `_Framework.ControlSurface`, which is **not** in our `Resources/control_surface/` copy — and
> `_can_set_pad_translations` gates on a 4×4 matrix while the Motion has two lanes of 16. Read the real
> implementation from the Live install first. Same rule as §6c.

### 6b-15. Song mode's centre bar takes the track colour — and a stale-bytecode trap (2026-07-25)

Phase 4's colour layer (`palette.py`) landed with its first consumer: the Template 3 centre bar now
carries the **selected track's real `0x00rrggbb`**, converted rather than looked up, so any colour the
user picks renders. Two details worth keeping:

* **Text colour is derived from the background.** Live's track colours include very light ones, and
  fixed white text on pale yellow is unreadable *while failing silently* — the element is drawn, it
  just cannot be seen. `palette.text_on()` picks black or white by Rec. 601 luma, so a saturated blue
  counts as dark and a mid green counts as light. A raw channel sum would get pure blue wrong.
* **The bar's background moved out of `paint_chrome` into `render`.** It is dynamic now, so leaving
  the chrome write in place would have been two code paths to one element — and they would have
  fought on every mode switch. Guarded by `test_centre_bar_has_one_owner`.

🐛 **The trap, which cost more time than the feature.** While verifying a guard by sabotaging
`_LUMA`, the suite reported failures that did not match the source on disk — the source was already
correct. Cause: **CPython validates cached bytecode on the source's `(mtime, size)` pair**, mtime has
one-second resolution, and `(299, 587, 114)` and `(333, 333, 333)` are *both exactly 15 characters*.
Edit, compile, restore — all inside one second, with the size unchanged — and the `.pyc` validation
key still matched, so a stale `__pycache__` entry shadowed the real file.

This is not exotic: a fast edit/test loop over a framework-free module is exactly the condition, and
the failure mode is a **confident pass against code that is no longer on disk** — which would quietly
undermine the whole "the offline suite is load-bearing" premise.

Fixed in `tests/test_screen.py`: `sys.dont_write_bytecode = True`, plus an `_AlwaysCompile`
`SourceFileLoader` subclass whose `get_code` compiles from source every time. Verified by recreating
the collision deliberately — writing a sabotaged `.pyc` whose `(mtime, size)` key provably matches the
restored source — and confirming the suite still reads the real file.

> **General rule:** any test harness that loads modules by path must compile from source. Trusting
> `.pyc` invalidation is trusting a one-second clock and a byte count.

### 6b-16. Two predicates, one decision — the view/content mismatch (2026-07-25)

Adding `centre_background` to `ParamsContent` produced `AttributeError: 'MainContent' object has no
attribute 'centre_background'` on every render **during setup**, logged three times before the screen
settled and drew correctly. The new field was not the bug; it *exposed* one.

**Which mode's screen we draw was decided in two places, with different tests:**

```python
def _view_for_mode(self):      # dispatches on self._mode alone
    if self._mode == PLUGIN_MODE: return runtime.main_view()
    return runtime.params_view()

def _content(self):            # ...and ALSO on self._modes
    if self._modes is not None and self._mode != PLUGIN_MODE: return self._song_content()
    return self._device_content()
```

`_mode` is a property returning `self._modes.selected_mode or ""`, so **before the modes component is
bound it is `""`**. The view then chose Params (Template 3) while the content fell through to
`_device_content()` — Main content into the Params view, on every render until modes bound.

**Why it had never been noticed:** `MainContent` and `ParamsContent` share the field names `title`,
`centre`, `tiles` and `soft_labels`. Duck typing meant the wrong pairing rendered a *plausible* screen
rather than failing. It only became visible when one dataclass grew a field the other lacked.

Two fixes, because either alone leaves the hazard:

1. **One predicate.** `_showing_plugin()` is now the single test, called by both `_content()` and
   `_view_for_mode()`. Guarded by `test_view_and_content_use_one_predicate`, which also rejects any
   re-test of `self._modes` in either function.
   *(The same rule was applied immediately afterwards to the Plugin header: its colour and its text
   both come from `_plugin_header_track()`, so the bar cannot name one track while wearing another's
   colour.)*
2. **Views reject foreign content.** `MainView.render` and `ParamsView.render` raise `TypeError` on the
   wrong dataclass. Guarded by `test_views_reject_the_other_templates_content` — removing the check
   reproduces the original `AttributeError` exactly.

> **The general lesson, and it is not really about screens:** when two code paths must agree, do not
> write the agreement twice. Derive both from one expression. Structural similarity between the two
> content types is what let the disagreement stay invisible for so long — *the more alike two things
> are, the less a wrong pairing will announce itself.*

### 6b-17. Track colour on both headers (2026-07-25)

The colour layer now drives two elements, and the rule that decides *which* element is worth stating:
**in each mode, the thing that names the track wears the track's colour.**

| Mode | Element | Colour | Why |
|---|---|---|---|
| Song (T3) | centre bar, zone 7 | selected track | it names the track; the header names the Live *view* ("Session"/"Arrangement") so it keeps the factory blue |
| Plugin (T0) | header bar, zone 1 | the device's owning track | the header is `Track \| Device`; the grey bank strip keeps `#303336` |

Three things this forced, each of which would have been a bug:

* **Text contrast is derived, not fixed.** `palette.text_on()` picks black or white by Rec. 601 luma.
  Live's track colours include pale ones, and fixed white text on them is unreadable *while failing
  silently*. Orange `#FF6600` lands at luma 67 of 127 — above the midpoint — so it correctly takes
  **dark** text; the factory blue `#0069CC` is 42 and keeps light text. A raw channel sum would get
  blue wrong.
* **Both dynamic elements moved out of `paint_chrome` into `render`.** Chrome is for what is static;
  leaving the old write in place would have been two owners for one element, fighting on every mode
  switch. Note this applies to `MainView` only — `ParamsView.paint_chrome` still owns *its* header
  background, correctly, because Song's header is not track-coloured.
* **`live_rgb7` had to survive a dead Live object.** A deleted object raises `RuntimeError` on
  *attribute access*, not merely on use, so guarding only the `int()` conversion is insufficient —
  the `getattr` itself throws, and an exception inside a Live listener wedges the render.

> A test-writing note worth keeping: two of the assertions here failed on first run because *the test*
> was wrong, not the code — one asserted light text on orange (it is bright enough to need dark), and
> one forbade `HEADER_BACKGROUND` in **every** `paint_chrome` rather than only `MainView`'s. Both were
> checked against the real luma numbers and the real class structure before being changed. When a new
> guard fails, establish which side is wrong before "fixing" anything.

### 6b-18. Pads: lit, and the ownership call that shapes Session mode (2026-07-25)

Phase 5. The pads are now declared, owned and lit; nothing binds them to a mode yet, which is the
whole point of a foundation phase.

**Pads are the only LED group on this device that is not CC-addressed.** State on `0x90`, colour on
`0x91`/`0x92`/`0x93`, against notes 36-67. `leds.py` grew a `LedGroup` base whose status bytes are a
parameter, so halos (`0xB0`-`0xB3`) and pads share one cache/diff implementation instead of two.
`PadLeds` also writes the **state byte twice** on release — the factory's state and animation
handlers both own the address and both release it, and the shutdown capture shows both (§5.1).

**The ownership decision, which matters more than the code.** A pad's LED address *is* its note
address — the same shared-address property that cost three attempts on the encoder halos (§6b-10).
It would have been consistent to reach for the same fix and suppress the element's writes. **That
would have been wrong**, and the difference is worth stating precisely:

* for an **encoder**, the framework wrote *parameter values* to a light — meaningless data, so
  suppression was right;
* for a **pad**, the framework writes *colour and state* — exactly what the light is for. Suppressing
  it would make it impossible for `SessionComponent` to ever light a clip.

So the pads are declared as ordinary `MIDI_NOTE_TYPE` buttons with `is_rgb=True`, and the rule is
**per-pad rather than per-address**: while no component has bound them, `leds.PadLeds` is the only
writer; when Session binds them, the framework becomes the writer for those pads and `PadLeds` must
yield. One owner at a time either way — this is the one-owner rule applied dynamically.

**A framework fact worth recording, because it was an inference until it was checked.** `is_rgb` on a
NOTE-type element lands on the *pad* RGB addresses, not the button ones. `ComplexColor.draw` calls
`interface.send_value(part.value, channel=part.channel)`, and the element adds that channel to **its
own** message type — so `ColorPart(channel=1)` on a note element is `0x90 + 1 = 0x91`. `[DERIVED]`:
`draw` is read from `elements/color.pyc`, but the final status arithmetic lives in v2's
`InputControlElement`, which is not in our framework copy. Confirm on hardware when Session lights a
clip.

**Resting appearance.** All 32 pads sit at the **focused track's own colour**, dim — the factory's
"present but inactive" model, where the state byte carries brightness (0/63/127) and the RGB triple
carries hue. The keybed therefore tells you which track you are playing into without any mode
claiming the pads.

🐛 **One bug caught while wiring it.** Selecting another track and *recolouring the current one* are
different events, and the colour listener only called `_render()` — which does not touch LEDs. A
recolour would have left the keybed on the previous colour indefinitely. Both track listeners now go
through `_track_appearance_listener`, which repaints pads and screen together; the LED diff makes the
redundant half free, so a rename queues 32 identical colours and sends nothing. Same shape as the
§6b-6 "content read at render time with nothing to trigger the render" family.

### 6b-19. Why nothing lit: pads have no dim state — and the Keys layout, decoded (2026-07-25)

Phase 5 shipped and **not one pad lit**. Two findings, both from a Studio Pro track-change capture.

#### The bug

We sent `0x90 <note> 0x3F` — `LED_DIM`. **63 is not a valid pad state.** A pad's state byte accepts
`0x00` Off, `0x7F` On, `0x01` Blink, `0x02` Pulse, and nothing else. The dim/full/off model with 63 in
the middle belongs to **button** LEDs on `0xB0`; pads are a different address space *and a different
vocabulary*, and the two had been silently conflated.

The consequence generalises: **a pad's brightness has to come from its colour, not its state.** That is
precisely why the factory updates a lit pad with colour-only writes, and why `palette.dim()` exists.
`midi.py` now carries `PAD_STATES` with a warning next to `LED_DIM`, and
`test_pads_never_get_the_dim_state_byte` fails if `LED_DIM` ever reaches `_refresh_pad_leds` again.

A second, smaller finding from the same burst: Studio Pro sends **channels 2/3/4 only** when a lit
pad's colour changes — no state byte. `LedGroup.flush` now diffs state and colour separately, so an
unchanged state is not re-sent with every recolour.

#### The layout — the pads are a piano, not a grid

The capture tinted three pads with the track colour and zeroed four others. Both sets are fully
explained by a **two-lane piano**:

* **Bottom lane, notes 36-51** — 16 *white* keys: C D E F G A B C D E F G A B C D.
* **Top lane, notes 52-67** — the *black* key above each white key, **dark where none exists**
  (above E and above B).

| | Predicted | Capture |
|---|---|---|
| Roots (white index % 7 == 0) | 36, 43, 50 | C1, G1, D2 — the three tinted pads ✓ |
| Absent black keys (white index % 7 ∈ {2, 6}) | 54, 58, 61, 65 | F#2, A#2, C#3, F3 — the four zeroed pads ✓ |
| Lit total | 28 | 28 ✓ |

**Appearance: root pads take the track colour, every other key is white, the four gaps are dark.**
That is more informative than the flat colour wall we had planned, and it is what the hardware
already expects.

The layout lives in `pads.py` (framework-free, so the suite executes it) and is parameterised by
`root_offset` in **scale degrees** — which is exactly what the A-H buttons move, so Phase 6 is now a
matter of driving one integer. The missing black keys are a property of the keyboard, not of the root,
so they must not move when the root does; there is a test for that across all eight offsets.

> **Method note.** The octave convention nearly cost an hour: this MIDI monitor labels middle C as
> **C3**, so `C1 = 36`. Decoding with the other common convention put every prediction off by twelve
> and made a correct hypothesis look wrong. When a capture's note *names* disagree with your model,
> check the naming convention before abandoning the model.

### 6b-20. The pads as a keyboard — translation, and two LED paths that disagreed (2026-07-25)

Three hardware complaints, two causes.

#### 1. The keybed stayed dark until a mode switch

`full_redraw` — the path taken on connect, on `refresh_state` and after Global Settings closes —
named `self._encoder_leds` explicitly and refreshed only the halos. The pads had been wired into
`_reassert_leds`, the *mode-change* path, and into nothing else. So the pads were painted the first
time a mode changed and never before.

**A hand-listed set of groups is exactly what goes stale when a group is added.** Both paths now go
through `_led_groups()` / `_invalidate_led_groups()` / `_refresh_all_leds()`, and
`test_every_led_path_covers_every_group` fails if either path names a group directly *or* if a
fourth group is added without extending the list.

#### 2 & 3. The pads played chromatically and could not play a track — one cause

Declaring an element makes Live route that message to the **control surface** rather than the track.
The pads therefore showed up in Live's Key/MIDI indicator (mappable) but made no sound, and they
played their own fixed notes 36-67 rather than a piano layout. Both symptoms are the same missing
mechanism: **note translation**.

`keyboard.MotionKeyboardComponent` extends the framework's `PlayableComponent`, whose contract we
read out of `components/playable.pyc` rather than guessing:

* `_note_translation_for_button(button)` → `(identifier, channel)`, written onto the element by
  `_set_button_control_properties`. Live's MIDI map then rewrites the note **in the engine** and
  forwards it to the track.
* `_button_should_be_enabled(button)` is literally `isinstance(identifier, int) and identifier < 128`
  — so **returning a non-int identifier disables the pad**. The four gap pads (where a piano has no
  black key) return `None` and are genuinely dead rather than playing a note off the keyboard.

**This costs no latency**, which is the §5.0 constraint from `Motion32_Scale_and_Chord_Engine.md`:
the translation is a static per-pad remap recomputed only when the root or octave changes, never per
note. Python is not in the pad→note path, and there is a guard that fails if the setters stop
early-returning.

#### Two framework details that would have been silent bugs

* **`button.coordinate` is `(y, x)` — row first.** Verified from the bytecode of
  `DrumGroupComponent._button_coordinates_to_pad_index`, which opens `y, x = coordinates`. Unpacking
  it the other way *transposes the keyboard* — a plausible-looking wrong layout, not a crash.
  (The drum group also inverts y because drum racks number bottom-up; that is drum-specific and our
  lanes need no inversion.) Guarded.
* **`PlayableComponent._update_button_color` is an empty hook**, and we deliberately do **not**
  override it. That is what keeps `leds.PadLeds` the sole writer of the pad addresses. Overriding it
  would put the framework and `PadLeds` on the same address — the encoder-halo two-writer problem
  again (§6b-10). A test fails if anyone adds the override without moving ownership in the same
  change.

> The through-line with §6b-16 and the LED-path bug above: **when two things must agree, do not write
> the agreement twice.** One `_led_groups()`, one `_showing_plugin()`, one `_plugin_header_track()`,
> one owner per address.

### 6b-21. `None` means ENABLED — the dead pads that kept playing (2026-07-25)

The four gap pads were unlit but still sounded. The cause is a piece of framework semantics that
reads backwards, and §6b-20 above had it exactly wrong until this was disassembled properly.

`PlayableComponent._button_should_be_enabled`, from the bytecode:

```python
identifier, _ = self._note_translation_for_button(button)
return identifier is None or (isinstance(identifier, int) and identifier < 128)
```

**`identifier is None` short-circuits to `True`.** It does not mean "no note, disable this pad" —
it means *"no translation needed, leave this button as it is"*. So returning `None` for the gap pads
left them **enabled and untranslated**, and an enabled-but-untranslated element passes its own raw
note straight through to the track. Unlit, and audible.

The only value that yields `False` is an **int at or above 128** — deliberately outside MIDI's 7-bit
note range. `keyboard.DEAD_PAD_IDENTIFIER = 128`, and a guard fails if it is ever `None` or below 128,
or if the translation returns a `None` identifier again.

> **The method failure, not the code failure.** §6b-20 recorded the rule as *"a non-int identifier
> disables the pad"* — inferred from the `co_names` tuple `('_note_translation_for_button',
> 'isinstance', 'int')` and the const `128`, which is consistent with the truth but does not imply it.
> The `is None` branch is invisible in a names/consts summary; it only appears in the jump structure.
> **Reading a function's *names* is not reading the function.** Disassemble the branches when the
> semantics matter.

Two features landed in the same pass:

* **Held pads flash green.** `matrix_always_listenable=True` keeps the matrix *playable and*
  listenable, so notes still reach the track and we additionally see press/release. The keyboard does
  **not** paint them — it reports the held set and the screen component repaints, because `PadLeds`
  is the single writer of those addresses. `Palette.PAD_PLAYED` is the colour.
* **Octave +/- wired** (CC `0x40`/`0x41`) on the keyboard component, since transposition changes the
  translation the keyboard owns. Clamped to ±3 octaves so every pad stays inside 0-127, and the
  recompute still happens only on change — never per note.

### 6b-22. Playable pads: the framework takes them over the moment you press one (2026-07-25)

Desired behaviour is as simple as it gets: **note-on → green, note-off → back to the previous
colour.** Getting there took two wrong turns, and the second one is a genuine framework trap.

#### The trap: `PlayableComponent` steals the pads while one is held

`_update_control_from_script`, from the bytecode:

```python
takeover_pads = self._takeover_pads or len(self.pressed_pads) > 0
mode = PlayableControl.Mode.listenable if takeover_pads else self._default_playable_mode
for button in self.matrix:
    button.set_mode(mode)
```

**The moment any pad goes down, the entire matrix flips to `listenable` — which consumes notes
instead of passing them.** That is correct for a drum rack, where holding a pad is meant to take
the grid over for selection. It is completely wrong for a keyboard, and it produced exactly two
symptoms: the note that lit a pad was **swallowed**, and a second press of the same pad behaved
differently from the first because the mode had changed underneath it.

⚠️ **`matrix_always_listenable=True` does not prevent this.** It only sets
`_default_playable_mode`; the takeover overrides the default. That flag was the thing that looked
like the answer and was not.

Fix: override `_update_control_from_script` to hold the mode constant at
`playable_and_listenable`. We never take the pads over, so nothing should ever make them stop
playing. Guarded by `test_pads_are_never_taken_over_from_the_player`, which fails if the override
is missing *or* if it reintroduces a dependency on `pressed_pads` / `_takeover_pads`.

#### The first wrong turn, recorded because the reasoning was the problem

Before finding the takeover, the symptom was "green on press, green for a while afterwards", and
the fix attempted was defensive ordering: run our LED bookkeeping before `super()` and wrap the
base call in a `try`. That was **treating a design mismatch as a robustness problem** — the same
error as the timer-based halo re-asserting in §6b-10, where a race was the wrong diagnosis for an
ownership problem. The ordering itself is harmless and is kept (the light should not depend on the
base class's `pressed_pads` handling succeeding), but the wrapper and its guard were removed:
scaffolding built around a misdiagnosis outlives the misdiagnosis and misleads the next reader.

> **The lesson that keeps recurring in this file:** when the framework fights you, the question is
> *what is this API for* — not *how do I harden against it*. `PlayableComponent` is built for drum
> racks; its takeover behaviour is a feature there and a defect here. Read the mechanism, then
> decide whether to use it, override it, or not inherit from it at all.

**The firmware was checked too, and it is not involved.** `motionupgrade.bin` was searched for local
pad-LED or note-echo logic; there is none. The only pad-adjacent strings are Global-Settings labels
(`Velocity`, `Pressure`, `Pressure Feel`), the note-name table the device renders in its own UI, and
LVGL/Pico-SDK internals. That is exactly what the host-rendered model predicts — **the device will
never light a pad on its own, so every bit of press feedback is ours to send.** Recorded in
`Motion32_Source_Inventory.md` so it is not re-checked a third time.

### 6b-23. Two collisions, one symptom set — and the root-offset maths (2026-07-25)

Reported: dead pads sounding after an octave change, dead pads lighting *a different* pad, and some
lit pads not turning green. Three symptoms, and they share a cause — **note 54, 58, 61 and 65 are
both the dead pads' own addresses and other pads' translation targets.**

#### The collision

`PlayableComponent._update_note_translations` only assigns properties to buttons it *enables*:

```python
for button in self.matrix:
    if self._button_should_be_enabled(button):
        self._set_button_control_properties(button)
        button.enabled = True
    else:
        button.enabled = False
```

A disabled pad therefore never gets an identifier and **keeps its declared raw note**. Ours are
54/58/61/65 — real notes, and also translation targets for other pads. Measured overlap:

| Octave | Dead-pad notes that are also a live translation target |
|---|---|
| −12 | none |
| 0 | 54, 58, 61 |
| +12 | 54, 58, 61, 65 |
| +24 | 61, 65 |

That is exactly why it looked octave-dependent, and why the default felt *mostly* right.

#### 🔑 The actual mechanism, and the four attempts it took

**A control is keyed by `(identifier, channel)`, and the framework matches an incoming note
against that key.** Everything follows from that one sentence.

The transposition works: a real pad is given its layout pitch, so the keyboard genuinely plays a
piano. The problem was only ever the four gaps, and each attempt failed for its own reason:

| Dead-pad identifier | Result |
|---|---|
| `None` | enabled **and** untranslated — the raw note passes straight through |
| int ≥ 128 | *disables* the pad, and a disabled element is **released**, so its raw note floats loose |
| its own note, keyboard channel | **collides** with whichever real pad is transposed to that number |
| its own note, **its own channel** | claimed, unique, silenced by mode ✅ |

The collision is measurable: 54, 58, 61 and 65 are every one of them a live translation target at
some reachable octave. A capture confirmed it three times over —

| Pressed (physical) | Control that fired | That control's pitch | LED written |
|---|---|---|---|
| 54 | 26 | **54** | 62 |
| 58 | 28 | **58** | 64 |
| 61 | 30 | **61** | 66 |

**Fix:** dead pads keep their own note but on `DEAD_PAD_CHANNEL`, which makes the key unique, and
`_update_control_from_script` gives *them* `PlayableControl.Mode.listenable` while every other pad
gets `playable_and_listenable`. Listenable consumes the note and passes nothing on. `_note_held`
ignores them so they cannot light.

> 🐛 **A wrong turn worth recording, because the reasoning looked sound.** Reading the capture as
> "identifier is the note a control *matches*, not a transposition", I concluded the piano layout
> had never worked and removed it. **Both halves are true at once** — the identifier transposes
> the outgoing note *and* becomes part of the control's match key — and the user had a working
> piano keyboard the whole time. Reverted immediately.
>
> The lesson is about evidence, not the API: the capture only ever showed **dead** pads
> misbehaving. Concluding from it that *every* pad was scrambled extrapolated far past the
> observation, and it took a "no, that part works" to catch. **When a capture shows one class of
> input failing, that is evidence about that class — not licence to condemn the mechanism.**

#### The root-offset maths was broken in both directions

Spotted while investigating. The old expression mixed `% 7` and `// 7` across different terms:

```python
white = white_key_semitone(index) - white_key_semitone(root_offset % 7)
base = 36 + white + octave_semitones + 12 * (root_offset // 7)
```

Python floors toward negative infinity (`-1 % 7 == 6`, `-1 // 7 == -1`), so offset −1 subtracted
B's semitone *and* an octave: pad 1 landed on note **13** instead of 35. Positive offsets were wrong
too — +1 gave **34** where it should give 38, moving the root the *wrong way*.

Replaced with a single `divmod`-based helper, so pad `i` is simply white key `i + root_offset`
measured from C at note 36. Verified across offsets −3…+3 × octaves −2…+2: no duplicate pitches,
the white lane always ascends, and roles and pitches always agree about which pads are dead.

**And one modelling correction that came with it.** An earlier test asserted the dead pads never
move. That was wrong: sliding the window along a piano changes which positions have a black key
above them, so the gaps follow `(index + root_offset) % 7`. What does *not* move is the root tint —
the manual is explicit that Pad 1 is the root, so the tint stays on `index % 7 == 0` and the offset
changes which *pitch* pad 1 plays. At offset 0 both reduce to the capture-verified layout.

> ⚠️ **The second half of that paragraph is wrong, corrected 2026-07-29 — see §6b-29 item 7.** The
> tint *does* move. It marks the pads playing the **root pitch class**, not a fixed set of pad
> positions, so it slides with the window exactly as the gaps do. The manual's "Bank E will be
> selected and Pad 1 will be assigned to the root note" describes the **default**, not a rule: at
> bank E the window starts on C, so the two readings pick the same three pads and the
> capture — taken at rest — could not tell them apart. Left in place rather than rewritten, because
> the mistake is instructive: this paragraph is a confident modelling claim built on a capture of a
> single state, in the one state where the ambiguity is invisible.

### 6b-24. Making the pad layout survive A-H and scales (2026-07-25)

Asked whether the keyboard would still be correct once A-H banking moves the pads and non-diatonic
scales change the whole/half-step pattern. It would not have been, for one specific reason.

**Two passes set two different things, and only one was refreshed.**

* `_update_note_translations()` → each pad's **identifier** and `enabled`
* `_update_control_from_script()` → each pad's **mode**, which is the only thing that makes a dead
  pad silent

`_recompute()` called just the first. So a pad that *became* dead kept `playable_and_listenable`
and would still sound, and one that became alive kept `listenable` and would stay mute. **This was
invisible only because nothing yet moves the gaps** — an octave shift transposes every pad equally
and leaves deadness untouched. A-H banking and any non-diatonic scale both move it, so the bug was
scheduled to appear exactly when this work continues. Fixed: `_recompute` calls both, and a guard
fails if either is dropped or if a setter bypasses `_recompute`.

**Deadness now has one source.** `pad_roles` derives it from `pad_pitches` instead of re-testing
`(index + root_offset) % 7` itself. Two opinions about which pads are dead is the §6b-16 failure,
and it gets sharper with scales: a pentatonic layout has a different number of gaps in different
places, so a second computation *will* disagree — silently, as a pad that looks dead but plays.

**What generalises and what does not** is written up in `Motion32_Scale_and_Chord_Engine.md` §5.3b.
Short version: the *keyboard component* is scale-ready, because everything it does is derived from
"pitch or `None`" per pad. `pads.py` is not — `WHITE_KEY_SEMITONES`, `% 7` and
`NO_BLACK_KEY_ABOVE` are diatonic assumptions, and Phase 10 needs a function taking a **scale mask**
rather than an extra argument bolted onto these.

> **The invariant to keep through every later phase:** the layout module answers *pitch or None*
> per pad, and silence, darkness, translation and press feedback are all **derived** from that one
> answer. The moment something forms a second opinion about which pads are playable, the two
> opinions drift and the symptom is a pad that looks one way and behaves another.

### 6c. Method note
Both the `channel=` failed load (§4) and the `ParameterInfo` bug had the same root cause: reasoning
about the framework from naming and from a third-party script instead of from its own source. The
source is small, decompilable, and now sitting in `Resources/control_surface/`. Read it first.

---

## 7. PreSonus/Fender SDK scaffolding (`From Studio Pro/sdk/`, 5 .js files)

These are the **generic Control Surface SDK** base classes (© 2020 PreSonus) that the Motion scripts
extend — the Studio One analog of Ableton's `ableton.v3` framework. No Motion-specific wire formats
here (those stay in `Motion32MidiDevice.js`), but they confirm architecture and add:

- **Pad → note base mapping** (`musicprotocol.js`): `padIndexToSymbolicPitch = (kPitchC1 + padIndex)
  % 128`, with **`kPitchC1 = 36`** (`kPitchC0 = 24`). So the un-transformed pad grid is chromatic
  from C1=36; Scale / Chord / Octave transform on top of that. `kMinVelocity = 1/127` (0 = note-off).
  → This is the anchor for the still-open "pad musical-note output" gap; a capture only needs to show
  how each Scale/Chord/Octave setting offsets from this base.
- **Scale engine list** (`musicprotocol.js` `MusicalScaleID`): 0 Chromatic, 1 Major, 2 Melodic Minor,
  3 Harmonic Minor, 4 Natural Minor, 5 Major Pentatonic, 6 Minor Pentatonic, 7 Blues, 8 Dorian,
  9 Phrygian, 10 Lydian, 11 Mixolydian, 12 Locrian, 13 Major Triad, 14 Minor Triad. Root symbols in
  `kKeySymbols`. Needed when we integrate Scale mode.
- **Pad LED animation codes** (`controlsurfacedevice.js` `PadSectionPadAnimation`): none 0 / blink 1 /
  pulse 2 — confirms the pad-state animation values in the handshake spec.
- **ControlValue flags** (`controlsurfacedevice.js`): `kBipolar = 256`, `kDisabled = 512`. Value-bars
  fill center-out when bipolar (pan, encoder halos) and show off when disabled — informs encoder/mixer
  value rendering.
- **Touch-strip event model** (`controlsurfacedevice.js`): the base device exposes
  `sendPitchBendToHost / sendModulationToHost / sendExpressionToHost / sendBreathControlToHost /
  sendSustainToHost`. Confirms the strips emit raw pitch-bend and the *script* decides the musical
  meaning; for Ableton these become our per-strip mapping targets (pitch/mod/expression/breath).
- **Handler architecture** (`controlsurfacedevice.js`): `ControlHandler` (sendValue/updateValue/
  receiveMidi/receiveSysex) + `ControlSurfaceDevice` (`onMidiOutConnected` = where the Motion sends
  its native-mode handshake, `onMidiEvent`/`onSysexEvent` dispatch). Studio One analog of our
  hello_messages + receive_midi.

`controlsurfacecomponent.js` is the Studio One host API (ChannelType, PropertyID, banks, sends,
inserts, editors) — reference-only for us since the Ableton build uses Live's LOM, but it maps out
what a full integration eventually touches.

---

### §6b-25 The notification bar is Template 1, and the diff makes it nearly free

**What the factory does.** A Studio Pro capture of two Octave presses (2026-07-26) shows the
complete transaction: paint Template 1, show it, wait, **restore every element it touched to
its default**, **repaint all of Template 3**, switch back. About 65 messages per press.

The surprise is that the "popup" is not a fifth template. It is the **Menu** template with its
title, its four footer labels and its footer divider taken away, leaving two bold texts on the
header bar — `"Octave"` in header slot 0 and `"+1"` in slot 2, with slot 1 empty between them so
it reads as *label … value*. Every address involved was already named in `screen.py`.

**What we do instead, and why it is safe.** Studio Pro's renderer does not diff, so it rebuilds
unconditionally. Ours does. The bar's chrome is identical on every showing, so:

| | Studio Pro | Us |
|---|---|---|
| First showing | ~15 messages | ~15 |
| Every later showing | ~15 | **2** (the value text + the template select) |
| Dismissing | ~50 (full repaint of the base template) | **1** (the template select) |

Skipping the repaint depends on the device keeping each template's element state while a
*different* template is displayed. That is not an assumption: **the Song ↔ Plugin mode switch
already relies on it and works on hardware** — `_render()` selects the template and lets the
diff decide, and neither view repaints on the way back.

**The trap this had to avoid.** The overlay writes through `ScreenModel` like everything else.
Poking Template 1's elements directly would leave `_sent` describing a device state that does
not exist, and the first real Menu view would then render wrong with nothing in the log — the
same shape as the halo bug, one layer up.

**Three layers now, one predicate each.** `_showing_notification()` joins `_showing_plugin()`,
and **both `_view_for_mode()` and `_content()` consult them in the same order**. The suite
asserts the order, not just the presence: if one function checked the bar first and the other
checked it second, a notification raised in Plugin mode would draw Plugin content onto
Template 1. That is exactly the §6b-16 failure repeated at the next level up, so it is guarded
rather than remembered.

The bar is cancelled by a mode change (you asked for a different screen; you get it now) and by
`disconnect()`. Re-notifying **restarts** the timer rather than queueing, so holding Octave Up
keeps one bar alive showing the running value.

⚠️ **Nothing on the pad path may call `notify()`.** Press → note must stay free of Python.

**🐛 First hardware run: an unwritten element is not a blank one.** The bar worked, but the
device drew its own placeholders straight through it — `MenuItem0`…`MenuItem5`, **twice**, from
the twelve `TEXT_ROW` elements in zones 3 and 4 that `paint_chrome` never touched. The firmware
ships those strings *in the elements*; leaving an element alone displays whatever the factory
put there.

Studio Pro does not clear them either, which is why the capture gave no hint: by the time it
raises a bar it has already used the Menu template for real and left it clean. We arrived at
Template 1 for the first time ever, in its shipped state.

The general rule, and it applies to every template: **claim every element or inherit the
factory's.** Painting only what you mean to show is not enough.

Every existing test passed while this was broken, because each asserted that the elements we
had *thought about* were right. `test_the_bar_claims_every_element_on_its_template` asks the
opposite question — is there anything on this template we did not think about? — and derives
the element list from `Motion32_Screen_Template_Map.csv` rather than from memory, so the next
view on any template gets the same guard for nothing.

### §6b-26 The octave buttons carry two meanings on one LED

State byte = press feedback (63 rest / 127 held). RGB = whether *that direction* is engaged
(blue rest / white engaged). Proven by the second press in the same capture: Octave **Down**'s
press wrote only its own state byte, and simultaneously rewrote **Up**'s RGB back to blue
because the offset had returned to 0.

Implemented with `ButtonControl`'s `on_color` and the `is_on` setter — both read out of
`control_surface/controls/button.pyc` before use (`__init__(self, color, on_color, *a)`,
`_send_button_color` picks `on_color if is_on else color`, and the `is_on` setter calls
`_send_current_color()` so assignment repaints). `update()` re-asserts after a layer grab,
because layer grabs reset button elements — the same reason the halos needed re-asserting.

Rest reads **`0`** on the bar, not `+0`: the capture sends the single byte `0x30`.

### §6b-27 Wheel push is input-only because CC 0x78 is strip LED output

Hardware capture confirms the main wheel's native input split:

- Wheel turn right/left: CC 29 (`0x1D`) with values `1` and `65`.
- Wheel click down/up: CC 120 (`0x78`) with values `127` and `0`. MIDI Monitor labels CC 120
  as "All Sound Off", but the native surface definition names it `wheelPush`.

That does **not** mean the script can safely light the wheel push at `0x78`. Fender's sources use
direction-overloaded addresses here: `wheelPush` is receive-only at `#78`, while touch-strip 2's
nine LED outputs are `0x70` through `0x78`. `Motion32MidiDevice.js` sends those strip LED states
as outbound CCs, so an outbound `B0 78 <value>` belongs to touch-strip 2 LED 9, not to the wheel
push.

The wheel's visible feedback belongs on the wheel LED/halo address at `0x1D`, and should indicate
that the wheel is actively mapped to a control. The click itself is menu/screen input; the screen
will show the result of the click, so there is no planned press feedback on `0x78`.

Implemented in code by building `Wheel_Push_Button` with `MotionInputOnlyButtonElement`, which keeps
normal input behavior but suppresses all outgoing `send_value` / `send_midi` writes. `wheel.py` uses
a plain feedbackless `ButtonControl()` for the press, and `skin.py` no longer defines wheel push
colors. `test_wheel_push_is_input_only` guards the collision before touch-strip LED work starts.


### §6b-28 Suspending your writers does not mute the framework (2026-07-29)

§6b-5 established the script-reload race and fixed the half of it we could see: Live constructs the
replacement `ControlSurface` **before** disconnecting the old one, so `runtime` is owner-scoped and
the outgoing instance skips its LED/screen reset. That handled everything routed through
`MotionProtocol`, `ScreenModel` and `LedGroup`.

It did not handle the framework. Disassembling `control_surface.pyc`:

```
disconnect            -> _send_specification_messages(messages_name="goodbye_messages")
_send_specification_messages -> for msg in getattr(self.specification, messages_name) or []:
                                    self._send_midi(msg)
```

`self._send_midi` **directly** — no protocol, no model, no suspend flag anywhere on that path. Both
branches of `disconnect` do it; `send_goodbye_messages_last` only decides whether it runs before or
after `super().disconnect()`. So the real reload order was:

```
new instance sends 8F 00 7F  ->  old instance disconnects  ->  old instance sends 8F 00 00
```

The device leaves native mode while the new instance believes it is in — which is indistinguishable
from §1's pre-native half-state: the screen and LEDs keep working, and only the transport CCs give
it away (`0x66`-`0x69` instead of `0x6F`). Intermittent, reload-only, and it looked nothing like a
teardown bug.

**The rule this generalises to: a suspend flag protects the writer that reads it, and nothing else.**
If a framework path can reach the wire without passing through your abstraction, the only place to
stop it is the wire. `Motion32` now overrides `_send_midi` and returns `True` (framework for
"handled") while `self._midi_muted` is set. That is broader than neutralising `goodbye_messages`
would have been, and deliberately so — it also covers element resets and any framework write not yet
enumerated. The flag is initialised on the first line of `__init__`, before `_build_screen()` and
`super().__init__()`, because the override is live from the moment the object exists.

**The test lesson is the sharper one.** `test_teardown_is_skipped_when_superseded` was passing
throughout. It checked that `_clear_all_leds` sat inside the ownership guard — which was true, and
which had nothing to do with what actually went on the wire. A guard phrased over *the calls we
remembered to make* cannot see a path we did not know about; a guard phrased over *bytes emitted*
can. `test_a_superseded_teardown_emits_zero_bytes` lifts the teardown methods out by AST, re-compiles
them as a class body (so zero-argument `super()` gets its `__class__` cell and the base is really
reached), and reproduces the framework goodbye path in the stand-in — because stubbing that path out
would have stubbed out the bug. It opens with a positive control: a *current* instance must still
emit `8F 00 00`, or "zero bytes" proves nothing. Verified by reintroducing both failure modes.

---

### §6b-29 A–H banking, and retiring the second copy of the layout (2026-07-29)

Phase 6. Three things are worth carrying forward.

**1. The step is a semitone, and that made the maths simpler, not harder.** `[MAN]` describes the
Keys-mode role as "moves the musical root note left/right along the piano", and the firmware's
`bankMode` for Keys is `KeyboardRange` — the fine granularity, as against the `KeyboardBanks16/32`
that Drum Blocks pages with. So one A–H step is **one semitone** (user decision), which makes the
root shift the *same kind of operation as Octave*: a rigid transposition of the whole layout. They
sum into one semitone term in `pad_pitches`, and the gaps do not move.

That is a real distinction from `root_offset`, which moves the window in **white-key degrees** and
therefore *does* move the gaps (§6b-23). Both now exist in `keyboard.py` and they are not
interchangeable — `set_bank` is chromatic, `set_root_offset` is diatonic and is the Phase 10 seam,
where a semitone nudge would land between a scale's pitches. `pads.bank_step()` returns a unitless
−4…+3 precisely so the same eight buttons can mean "one degree" in Scale mode without a second
control or a mode-dependent handler.

**2. The bug the handoff predicted, and the shape of the fix.** The handoff's Phase 6 entry warned:
*"a future A–H implementation must drive the keyboard's root offset and the pad-LED root offset from
the same value, or the lights and the notes will disagree."* The screen component did keep its own
`_pad_root_offset` and call `pad_roles()` with it.

Keeping two copies in step is the obvious fix and the wrong one. **The copy is now gone.** The
keyboard already computes `self._pitches` — the list it builds the note translation from — and
`pads.roles_for_pitches()` derives the roles from *that list*, which the keyboard reports through a
listener, the same shape as `set_held_listener`. So the lights and the notes are not computed from
the same inputs; they are computed from the same object. That is the strongest available form of
§6b-24's invariant, and it removes the failure mode rather than guarding it.

**3. A latent disagreement that A–H would have exposed.** `pad_roles` hard-coded `0` for the
transposition, on the reasoning that a rigid shift cannot change which positions have a black key
above them. That reasoning is correct and the code was still wrong: a rigid shift *can* push a pad
off the end of MIDI, and `pad_pitches` calls such a pad dead. With Octave alone the layout could not
reach the edge — ±3 octaves over a ~2½-octave span stays inside 0–127 — so the two never disagreed
and the test suite never saw it. A–H adds four more semitones downward, and bank **A** at octave
**−3** puts pad 1 on note **−4**. The symptom would have been a lit pad that plays nothing.

> **The generalisation.** "This input can't affect that output" is a claim about the *interior* of
> the range. `_in_range` is a second thing the offsets feed, and it does not care which offset moved.
> An argument that a parameter is irrelevant should be checked at the boundaries before it becomes a
> hard-coded zero.

**4. What the first hardware run corrected (2026-07-29).**

*The notification bar's fields are soft-button labels, not free text.* The title read
`Root Shifted` and ran off the left edge of the screen. The four fields are
`MENU_HEADER_BUT_TEXT[0..3]`, each anchored over its **physical button** across the screen width,
and the title sits in slot 0 — the leftmost. So the usable width is about one button, **6-7
characters**, while `MAXCHARS_MENU_BUTTON = 16` is what the *element* accepts. Those are different
numbers and only one of them is on screen. Title is now `Root`; `Octave` is 6 and has always fitted.

*A bottom-lane pad is never legitimately dead* (user, 2026-07-29), and that is a stronger statement
than the code was making. The gaps are **missing black keys**, and black keys only exist on the top
lane; the bottom lane is sixteen white keys, all real notes, and the root lives there. So a dark
bottom-lane pad is a *range* failure, never a layout feature. `pads.safe_semitone_range()` now
derives the transposition window from the layout itself and `keyboard._octave_limits()` combines it
with the current bank, which makes the invariant true by construction rather than by remembering
that ±3 octaves happened to fit. At bank `A` the octave floor is **-2**, not -3; and selecting a low
bank while the octave is already floored pulls the octave up, because **the bank is an explicit
selection and the octave is a range control** — pressing `A` must give you `A`.

> **The method failure, and it is the important part of this entry.** A–H shipped with AST-only
> guards: *the handler calls `_select_bank`*, *`set_bank` clamps*, *`_recompute` is called*. All
> true, all passing, and the feature still did not do the job on hardware. **Structure is not
> behaviour.** An AST guard can prove a call exists; it cannot prove the number that comes out the
> other end is right. The suite now imports `keyboard.py` for real against a `PlayableComponent`
> stand-in (`_load_keyboard`) and presses the buttons, so "pad 1 plays 37 at bank F" is an assertion
> rather than an inference. That is the same move `test_a_superseded_teardown_emits_zero_bytes` made
> for the goodbye path a few hours earlier, and it should have been the default here.

**5. Runtime identifier changes do reach Live.** Briefly suspected otherwise: `PlayableComponent`
transposes by plain `button.identifier = …` assignment, and whether that gets Live's MIDI map rebuilt
lives in `ableton.v2`, which is not vendored. Hardware says it does — no
`request_rebuild_midi_map()` call is needed, and the same answer covers Octave ±, which shares
`_recompute`. The layout log line stays; it is what made the question answerable and it will be
wanted again for the Scale layouts.

**6. The step is a scale degree, not a semitone — and the wrong unit showed up as an LED bug.**

The first build made A–H a **semitone** shift, reasoning from the manual's chromatic-sounding "moves
the musical root note left/right along the piano" plus `bankMode = KeyboardRange`. Those rule out the
coarse options but say nothing about what the fine step is. Factory behaviour does: **A–H only ever
shifts the bottom row**, so one press slides the keybed by exactly one bottom-row pad. Pad 1 takes
over what pad 2 was playing. That is a degree. It holds in Scale mode too — ⚠️ **and both rows are
lit there**, which corrects `Motion32_Pads_Banking_and_Strips.md` §2b's "top lane all dead".

> **The diagnostic is the part worth keeping.** The reported symptom was *"the notes shift but the 32
> pad LEDs never redraw"*, which reads like a rendering bug — a missed listener, a stale cache, an
> early return in the diff. It was none of those. A semitone shift transposes the layout **rigidly**:
> every pad moves by the same amount and *no pad changes role*, so `pad_roles` returned a list
> identical to the previous one, `set_pad_roles` correctly declined to repaint, and there was
> genuinely nothing to draw. The LEDs were right; the unit was wrong.
>
> **A diff that correctly reports "no change" is evidence about the model, not the renderer.** When
> the display is idle and the model says nothing moved, check whether the thing you changed *should*
> have moved anything before going looking in the renderer. Fixing the unit fixed the lights as a
> side effect, and no LED code was touched.

**7. The bottom row stayed fixed, and it was the same class of mistake one level down.** With the
degree shift in, the top lane's gaps moved correctly and the bottom lane's tint did not. The two rows
were in **different reference frames**: the gaps came from `(index + root_offset) % 7` via the
pitches, while the tint was pinned to `index % 7` — the pad's own position, independent of the
window.

That came from reading the manual's *"Bank E will be selected and Pad 1 will be assigned to the root
note"* as a rule — pad 1 *is* the root — when it is a description of the **default**. At bank E the
window starts on C, so "pad 1, 8 and 15" and "the pads playing C" are the same three pads. They agree
at bank E and nowhere else, and the Studio Pro capture that verified this layout was taken at rest,
so nothing available could tell the two rules apart. §6b-23 recorded the wrong one confidently, and
the test suite asserted it: *"the tint does not move with the offset"*.

The tint marks the **root pitch class** — the C's, the landmark you orient by on a piano — so it
slides across the keybed as the window moves. `roles_for_pitches` now derives it from `pitch % 12`,
which puts both rows in one frame and keeps the function a pure function of the pitch list.
`ROOT_PITCH_CLASS` is a parameter so Phase 10 can tint a scale's tonic.

> **Two lessons, and the second is the sharper one.**
>
> *A capture of one state cannot distinguish two rules that agree in that state.* Everything about
> this layout was verified at bank E, which is exactly where the ambiguity hides. When a capture is
> taken at a default, the default is the one place its evidence is weakest — for anything the
> defaults make coincide, the capture is silent, however detailed it is.
>
> *And "half the thing updates" is a frame mismatch until proven otherwise.* Two rows of one
> keyboard, one moving and one not, is not a missed listener — it is two computations that disagree
> about what they are indexed by. The same shape as §6b-16 and §6b-24, at a smaller scale: the fix is
> always to delete a frame, never to synchronise two.

Mechanically: Octave and A–H are now the two *separate* arguments to `pad_pitches`, not one summed
term. Octave is the semitone argument (rigid, gaps stay put); the bank feeds the degree argument
(slides the window, gaps move). `keyboard.root_offset` is the single degree number — a programmatic
base plus wherever A–H sits — so the pitches and the roles can never be handed different windows.
Eight banks over a seven-degree cycle give exactly seven distinct gap patterns, A and H sharing one
because they are an octave apart; the suite asserts that, and asserts adjacent banks always differ,
which is the property that makes the keybed visibly follow.

**On not using `control_list` for the eight buttons.** `control_list(ButtonControl, 8, color=…)`
forwards its kwargs to a `ControlList` in `ableton.v2.control_surface.control`, which is **not** in
`Resources/control_surface/` — v3 only. Whether it passes colours down to each element cannot be
read, and the failure mode if it does not is silent: `_send_button_color` falls through to `color`
whenever `on_color` is None, so every bank button would light the framework default and `is_on`
would do nothing. Eight explicit `ButtonControl`s use only the two-argument form verified from
`controls/button.pyc` and already running for Octave, and it happens to be the factory Atom SQ's own
idiom — its bank buttons are individually named too. §6c's rule applies: read it or don't build on
it. If v2 lands in the repo, a `control_list` is the obvious simplification.

### §6b-30 Mix mode, part one: Template 2 and what the map does not have (2026-07-29)

Phase 7's first half — the renderer and the eight volume strips. Four findings.

**1. Template 2 is not shaped like the other three.** It has **no header or title zone at all**:
zone 0 is the background and zones 1-8 are the strips, nine elements each. Every other template
we draw has somewhere to put a mode name or a global readout; this one does not, so anything
global has to go on the notification bar.

There is also **no pan element**. The strip vocabulary is number / fader / mute / solo / label /
two meters, full stop. Pan can be bound to an encoder but cannot be *shown*, which quietly rules
out the "volume and pan side by side" layout the roadmap sketched.

And `MIXER_CHANNEL_LABEL` has `text` but **no `visible`** — the only text element on this device
that cannot be hidden. An unassigned strip is blanked by writing an empty string, not by hiding.
Writing `visible` to it would be an address the device does not implement, which is the silent
no-op class `test_every_address_is_real` exists to catch.

**2. Nobody drives the Motion's meters — including Fender.** `Motion32Component.js` and
`Motion32MidiDevice.js` contain **no meter handling at all**, despite the firmware exposing
`MIXER_CHANNEL_METER_LEFT/RIGHT` for all eight strips with `value`, `visible` and `color`. Live's
v3 framework has no meter support either, and neither does the factory Atom SQ script. So there is
no capture to match and no cadence to copy: this is genuinely new ground.

Meters are deferred by decision (user, 2026-07-29), **but the elements are still claimed** —
zeroed and hidden — because §6b-25 applies with full force to sixteen elements nobody writes.
When they land they need a **polled** source; the right idiom is `task.loop`, from the framework's
own `ScrollComponent._make_scroll_task`, rather than the self-rescheduling
`task.sequence(wait, run)` chain in `screen_component`. Ours is fine for a readout that is usually
idle; a continuous meter should be one task object that gets killed on mode exit.

**3. `volume_controls` is plural, and a static allowlist cannot see why.** `MixerComponent` has no
attribute of that name. `__getattr__` catches anything starting with `set` and returns
`partial(self._set_strip_controls, name[4:-1])` — dropping `set_` **and the trailing `s`** — then
`_set_strip_controls` does `getattr(strip, name)` on each channel strip. So the mixer-wide spelling
of a per-strip control is its plural.

I initially concluded the roadmap's §4.3 names were wrong, because they are absent from the class
body. They are not wrong; the allowlist just cannot model `__getattr__`. Worth stating as a rule:
**a name-resolution guard is only as good as its model of attribute lookup**, and this codebase has
two components that forward (`Device` via sub-components, `Mixer` via pluralisation). The guard now
encodes the pluralisation rule explicitly rather than either rejecting valid names or being relaxed
into uselessness. Unusually, a typo here is *loud* — `getattr(strip, "volumes_control")` raises at
bind time — which is the opposite of the normal Layer behaviour and worth knowing.

**4. Three layers became four, and the ordered-predicate rule stopped scaling.** §6b-16's fix for
"view and content disagree" was to give both functions the same two predicates and require the same
call order, guarded by a test. That is a rule a reader maintains. At four layers it was going to
rot, so both now index dicts — `_VIEWS` and `_CONTENT` — by a single key from `_screen_layer()`.
Disagreement is structurally impossible rather than tested for, and the guard checks that the two
tables carry the same keys.

> ⚠️ **The method is `_screen_layer`, not `_layer`.** `Component.__init__` assigns `self._layer`,
> and shadowing it fails the build outright. The reserved-name guard caught this immediately, which
> is the second time that list has paid for itself.

**5. Second pass, from the first hardware run.** Four reports, and the first three were one bug.

*Left/Right moved Live's selection, not the ring.* Bound to `View_Control.prev/next_track_button`,
which steps the **selected track** by one and never touches the session ring. Three symptoms from
one wrong component: the eight strips stayed put, only one track looked highlighted (the selection,
not the ring), and Solo/Mute — which follow the *target* track, i.e. the selected one — crawled
along with it instead of following the strip you touched. It is `Session_Navigation`, and
specifically its **page** buttons; the plain `left_button`/`right_button` scroll by one, which is
the behaviour that was already wrong.

> **Worth generalising:** "three things are broken" was one binding. Before treating co-occurring
> symptoms as separate bugs, check whether they share an input — here, all three read the selected
> track, directly or through `Target_Channel_Strip`.

*Focus is the selection, which dissolves the roadmap's trap rather than managing it.* Phase 7's
design note warned that cap-touch focus must **persist** and must not reuse Plugin mode's
`ACTIVE_PARAMETER_TIMEOUT` — "the same event source with opposite semantics". Touching an encoder
now **selects that strip's track**: `Target_Channel_Strip` already follows the target track, so
Solo/Mute come free; a selection persists by definition, so there is no timeout to get wrong; and
the on-screen mark is *derived* from the selection in `_mixer_content` rather than stored, so there
is no second copy to drift. Cheaper than the design, and strictly better — Live's own highlight now
agrees with the screen.

*Arm on the soft buttons* forced the eight LCD buttons from eight `add_button`s into one
`add_button_matrix`, because a plural control (`arm_buttons`) needs something iterable. Declaring
both shapes would put **two elements on each CC**, which is the shared-address trap from §6b-10;
Song mode instead binds them singly through `soft_buttons_raw[i]`, the `_add_raw_elements` idiom the
encoders already use. The LED is Live's: `MixerComponent._update_arm_button` listens to `track.arm`,
so arming with the mouse lights the button and nothing here is a script-side toggle.

*And one shape error the guards caught before hardware did:* arm and volume initially went in as
**two `Mixer` sections in one mode**. A component's `layer` is a single object, so the second would
have silently replaced the first — the exact reason `SONG_EXTRA_BINDINGS` merges per component. The
mapping-name guard failed on it immediately.

> 🐛 **A third dead assertion, and the fix is now general.** The halo guard checked that
> `_refresh_encoder_leds` mentioned `MIX_MODE`, `live_rgb7` and `_strip_track`. Disabling the branch
> with `elif False:` leaves every one of those names in place, so all three passed while the feature
> was switched off. That is the same failure as the A–H AST guards and the unfalsifiable lane check,
> three times in one project. There is now a **project-wide** guard —
> `test_no_branch_in_the_script_is_disabled_by_a_constant` — because `if False:` is precisely how
> bugs get simulated when verifying guards, and it must never be able to survive a green run.

**6. The stale screen, for the third time — and now guarded generically.** Mix mode drew the right
thing but only after something unrelated fired: turning an encoder moved the volume in Live and the
fader did not follow, and paging the ring moved the tracks without repainting. Touching another
encoder looked like a fix, because a touch selects a track and the *selection* has a listener.

Nothing in this component listened to a mixer strip. The value listeners it had (`_value_slots`) are
for **device parameters** — Plugin mode — and the track listeners (`_track_slots`) follow only the
*selected* track's name and colour. So Mix mode had no event of its own at all.

Now: per strip, `mixer_device.volume` (the fader), `mute`, `solo`, `name`, `color`; plus the session
ring's `offset` and `tracks`. The ring handlers also **re-point** the per-track listeners, because
paging moves the tracks out from under the strips — a listener on the old track is worse than none,
since it fires for something no longer on screen.

Getting at the ring took one non-obvious step: it is **not** in `component_map`.
`ControlSurface._create_session_ring` builds it and stores `self._session_ring`, and it is the object
carrying `offset` — `MixerComponent` listens to `offset` on its *provider*, which is the ring
(`mixer.pyc.__init__` sets `self._provider.subject`). `SessionRingComponent` declares `offset` and
`tracks` as `listenable_property`.

> **This is the third instance of one bug** — "the track name updates sometime later" (§6b-6),
> "bank changes never repainted" (§6b-7), and now the mixer strips. The rule is stated in each
> place and was still missed, which means restating it is not the fix. **Every fact on screen needs
> an event, and a new content field is where that gets forgotten.** So the guard is now derived from
> `MixerStrip`'s own dataclass fields: each field must either name the listener that keeps it fresh
> or be explicitly recorded as unable to go stale, and an unclassified field fails the suite. Adding
> a field to the content and forgetting to listen for it is no longer possible to ship. That is the
> shape every one of these guards should take — keyed off the thing that changes, not off a list
> someone maintains.

### §6b-31 How mode handoff of a physical control actually works (2026-07-29)

Written up because I got it wrong twice in one debugging session, and because every remaining
phase depends on it — Plugin-mode soft buttons, the Shift pad overlay, Scale and Chord all want
controls that another mode already claims. **v2 is now vendored at `Resources/v2/`, which is what
made this readable.**

**Two kinds of layer.** From `control_surface_mapping.pyc`:

| Where the mapping is | What is built | Lifetime |
|---|---|---|
| Top level (`"Transport": {...}`) | `component.layer = Layer(**mappings)`, then `set_enabled(True)` | permanent |
| Inside a mode's `modes` list | `EnablingAddLayerMode(component=..., layer=Layer(**mappings))` | **added** on enter, removed on leave |

The mode part *adds* a layer; it does not replace the permanent one. That is why the global
transport buttons keep working in every mode while Song mode simultaneously gives `Transport` six
more controls.

**Ownership is a stack, not a lock.** `ControlElement._resource_type` is `StackingResource`
(`v2/control_surface/control_element.pyc`), and from `v2/control_surface/resource.pyc`:

* `grab(client, priority)` removes then re-adds the client with its priority, recomputes
  `_actual_owners()`, and **always returns `True`**. There is no "grab failed".
* `release(client)` removes it, recomputes the owner set, and calls `_on_received_set(new_owners)`
  — which **hands the control back to whoever held it before**, automatically.
* `PrioritizedResource._actual_owners` filters clients to those at `max_priority`, so equal
  priorities coexist and a higher priority wins outright.

So the handoff needs no bookkeeping from us: mode A grabs, mode B stacks on top, mode B leaves and
A gets it back. `Layer(priority=N)` is the knob for a claim that must outrank another while both
are held — a Shift overlay over an active mode is the case that will want it. Ordinary
mutually-exclusive modes should not set a priority at all.

**A matrix is not a special case.** `ButtonMatrixElement` is a `CompoundElement`; when a layer
grabs it, `_grab_nested_control_elements` grabs each nested element *for the matrix as client* at
the layer's priority. And `__iter__` flattens — `product(range(height), range(width))` over
`get_button(j, i)` — so a 1x8 matrix yields eight buttons and `MixerComponent._set_strip_controls`
zips them one per strip. Splitting a matrix grab in one mode against raw element grabs in another
is therefore fine.

> **The two mistakes, because the method matters more than the conclusion.**
>
> 1. I claimed matrix-vs-raw could not be shared across modes. That contradicts the whole purpose
>    of the mode system, and the user said so from experience before I had read the resource code.
>    **When a hypothesis requires a framework to not do the thing it exists to do, read the
>    framework.**
> 2. I built that hypothesis on `identifier=None` in a diagnostic — but v2's
>    `InputControlElement` has **no `identifier` attribute**; it exposes `message_identifier` and
>    `original_identifier` as properties. The column was always going to read `None`. The log had
>    *already* shown `arm_element=ButtonElement` on all eight strips, i.e. the binding was fine,
>    and I read past it because a broken column agreed with a theory.
>
> **A diagnostic that reads a non-existent attribute is worse than no diagnostic**, because it
> returns a plausible value. Probe fields should be verified against the source that defines them,
> the same as any other API use — §6c applies to instrumentation too.
>
> Also: the first version of that probe was capped at three dumps and all three fired within
> twenty seconds of load, before the tracks under test existed. **Diagnostics should log on state
> *change*, not on a counter** — a counter is a way of guaranteeing you miss the thing you added it
> for.

**Resolved: there was no bug.** The tracks that would not arm were **audio tracks with no input
selected** — an audio interface had just been connected and its input was unset, so Live refused to
arm them. The mouse could not arm them either. Every layer of the script was correct throughout:
eight distinct `ButtonElement`s (confirmed by their `id()`s), `stack=2` with a single
`NestedElementClient` owner on all eight (the matrix winning over the `Modifier_Background` layer,
which grabs every element at low priority — **uniform, therefore healthy**), and
`arm_enabled=True` on every armable strip.

> **The tell was in the data from the first run and I did not see it.** The track names carry their
> type: run one was `1-MIDI`, `2-MIDI`, `3-Audio`, `4-Audio` and arm worked on 1 and 2 — *the two
> MIDI tracks*. I read "1 and 2" as "the first two buttons" and went looking for an ownership
> pattern, because I had already decided the shape of the answer. The user's observation that
> **placement did not matter across pagination** is what finally separated "the button" from "the
> track", and that distinction was available in the very first log.
>
> **`can_be_armed` does not mean "Live will arm this".** It reports track *type* — not a group, not
> a return — so it reads `True` on an audio track that has no input and cannot be armed. Anything
> that looks like "the script cannot arm this track" should be checked with the mouse first.

**Reverted with it:** a speculative `strip.update()` pass over all eight strips on every Mix render,
added on the theory that `_set_strip_controls` omitting `strip.update()` (where `set_send_controls`
includes it) left `arm_button.enabled` stale. That asymmetry in the framework **is real** and is
recorded here so nobody re-derives it, but it is not harmful and calling `update()` eight times per
render is real cost on the path that runs on every volume change. Also reverted: the per-strip
diagnostic, which had served its purpose.

**Kept:** everything else from that pass, because all of it was a genuine fix or a requested
feature — `Session_Navigation` page buttons for the ring, cap-touch focus via track selection,
per-track halo colours, arm on the LCD buttons, and the soft-button matrix conversion.

### §6b-32 Phase 7b, and the fourth stale-screen omission (2026-07-30)

The Pan page landed with **no listener on `panning`** — the arcs only moved when an unrelated event
forced a render. That is the *fourth* instance of one bug in this project (§6b-6, §6b-7, the mixer
strips in §6b-30, now the pan arcs), and the interesting part is that §6b-30's guard was supposed to
prevent exactly this and could not see it: it derives its checklist from **`MixerStrip`'s dataclass
fields**, and the Pan page does not use `MixerStrip` — it builds `MainContent`. A guard keyed off one
content class is blind to a second one.

> **The lesson is about the shape of the guard, not the listener.** "Derive the checklist from the
> thing that changes" was right, but I derived it from *a* thing that changes and then added a second
> one. The table is now per **page**, and the pan entry is checked against what
> `_mixer_pan_content` actually reads.

**Three dead assertions in one verification pass**, all found by reintroducing the bug:

* `"panning" in rebind_dump` passed with the subscription deleted — the *variable* survives when the
  call does not. Now asserts `_add_mixer_listener` is called **with `panning` as its subject**.
* Nothing checked that `_mixer_pan_content` *passes* `centre_background`; `MainView` supporting it
  proves nothing. Now asserts the keyword is present in the `MainContent(...)` call.
* Earlier in the session the halo guard survived `elif False:`. That one produced the project-wide
  `test_no_branch_in_the_script_is_disabled_by_a_constant`.

Three in one session is a pattern: **a substring or "does the code mention X" check is not a guard.**
Assert the call, the argument, or the resulting bytes.

**Two screen findings worth keeping.**

*Focus and reveal are per **page**, not per mode.* Mix's cap-touch focus used to `return` before the
value reveal for the whole of Mix mode. Correct for Volume — Template 2 shows the fader permanently,
so there is nothing to uncover — and wrong for Pan, where Template 0 gives one text element per tile
and the value shares it with the name. The Volume page still skips the timeout (a selection does not
expire); the Pan page falls through and gets it, like Plugin mode.

*The arc cannot be bipolar.* `MAIN_ENCODER_ENCODER[n]` takes a single 0-127 `value`, `color` and
`visible` — **no fill-mode attribute** — so the firmware fills from one end and a centred pan reads
as a half-filled arc. There is no host-side lever. Worth contrasting with the **touch strips**, where
the firmware *does* expose bipolar and fill modes (`Motion32_Pads_Banking_and_Strips.md` §5.4): the
device is inconsistent about this, so check the template map per element rather than assuming. What
does work is the text — Live formats a pan as `50L` / `C` / `50R` via `str(parameter)`, so the
bipolar reading comes free from `format_parameter_value` once the value is actually shown.

*And one element that gained a colour we were not using.* `MAIN_TEXT` (the centre strip) has
`text`, `color` and `visible`, and `MAIN_TEXT_BACKGROUND` has `color` — so the Pan page marks focus
on the centre label the same way the header does. That moved `CENTRE_BACKGROUND` out of
`paint_chrome` into `render`, because two writers on one element is what the one-owner rule forbids;
a guard now asserts the chrome no longer touches it.

---

### §6b-33 The firmware deep-dive: the device cannot be reconfigured (2026-07-30)

**The question.** Whether native mode has more than one configuration, whether a handshake variation
could select one, and whether any physical control can be repointed by the host. Answer: **no to all
three, and the reasons are structural rather than incidental.** Ghidra headless, payload import.

⚠️ **Two imports exist and they are NOT interchangeable.** `Motion32Firmware` ←
`motion32_fw_payload_0x1000.bin` (the extracted payload) and `Motion32FirmwareFull` ←
`motionupgrade.bin`. **Every address in `NativeMode_USB_EventStream_Report.md` is a payload
address.** A probe run against the full image resolves none of them — `0x9664` there decodes as
`bx lr` / `push` / `pop`. One full session was spent analysing that garbage before the mismatch was
spotted. The payload's image base is **0**, so a program address is also a raw file offset, which
means much of this is checkable with `python3` and no Ghidra at all.

**Four independent pieces of evidence that the mapping is baked in:**

1. **The CC numbers are immediate operands.** The whole emitter cluster (`0x00000ee0`–`0x000010a0`)
   builds exactly one status byte — `0xB0`, CC — and the controller numbers are literal
   instructions: `movs r1,#0x14` / `#0x15` / `#0x16` / `#0x36`. Nothing reads them from a table.
   **This alone is decisive**: no command can repoint a control whose CC number is a `movs` operand.
2. **The config selector is `return DAT_20004291`** (`FUN_00000e50`), written by exactly one
   function — `FUN_00000e5c`, on the boot path. No runtime write, no host reachability.
3. **The control-id table at `0x9664` is in flash rodata.** Not writable at runtime.
4. **The counts** `0x200045ca` (absolute) / `0x200045cc` (relative) are SRAM but have a single
   writer, `FUN_000016f4`, at boot.

**Exactly two variants exist, and it is provable from data.** Scanning every `F0 08` in the image
gives 42 hits; 40 have a third byte ≥ `0xF0` and are Thumb-2 branch encodings. Only two are real
headers, and they sit adjacent as a 2-entry array:

```
0x95f4:  f0 08 26 05     Motion 32
0x95f8:  f0 08 24 05     Motion 16
0x9664:  00 03 05 07 01 02 04 06 08 | 02 08 06 05 01 00 07 04 03 | ff ff
```

Two prefixes, two 9-byte control-id rows, `ff ff` terminator, no third entry anywhere.
`FUN_000016f4` sets `{rel 8, abs 2}` for config 0 and `{rel 9, abs 1}` for config 1;
`FUN_00001030` picks the outbound SysEx prefix from the same selector.

**The decoded control model:**

```c
FUN_0000140c   encoder scan, 9 unrolled slots gated by rel count
               delta = (char)cur[i] - (char)last[i];      // cur at 0x20004538 + i*0x10
               FUN_00000fb0((&DAT_00009664)[cfg*9 + i], delta);

FUN_00000fb0   if (cache != id) { cache = id; push(ring, (id - 0x50) & 0xff); }   // running status
               push(ring, 0x15); push(ring, delta + 0x40);

FUN_00001288   absolute scan, `abs` channels, 10-bit ADC, hysteresis 12 (tightening to 2
               below 0xc / above 0x3f4) -> FUN_00000eec(ch, value)
FUN_00000eec   -> CC 0x16 (MSB) + CC 0x36 (LSB): a 14-bit CC pair
```

`FUN_00004df4` reads GPIO `0x40040800` with `& 3 >> 1` — a 2-bit quadrature read — confirming the
`0x95fc` pairs are encoder pin configs and that "rel count" is literally the encoder count.

⚠️ **An unresolved discrepancy — do not build on either reading until it is settled.** The firmware
emits **CC `0x15` with the channel varying** per encoder (`0xB0`–`0xB8`, order `{0,3,5,7,1,2,4,6}`).
`midi.py` uses `CC_ENCODERS = range(0x0E, 0x16)` — **CC varying, channel fixed at 0** — and that
works in native mode. Same two numbers, opposite axes. Either this ring feeds the *control* port
rather than the main one, or a translation stage sits downstream. `FUN_00002a14` selects between two
USB endpoint descriptor sets at boot (`0x97e4` = endpoints 0–3, `0x9874` = endpoints 4–7), which
makes the two-port explanation plausible. **Cheapest resolution: open the `Motion 32 Control` port in
a MIDI monitor and turn encoder 1.**

⚠️ **Methodology correction worth keeping.** A literal-pool scan for the queue addresses returned
zero hits, and I wrote in the report that the anchors were stale. **That was wrong.** The core is
ARMv7-M, which builds 32-bit constants with MOVW/MOVT immediate pairs — `44 f2 84 00` =
`MOVW r0,#0x4084`, `c2 f2 00 00` = `MOVT r0,#0x2000` — so the address never exists as bytes anywhere
and neither `getReferencesTo` nor a byte scan can find it. Searching for the **MOVW encoding**
instead finds `0x20004084` at 17 sites and `0x200040a0` at 3. Both anchors are real. *A null result
from a search method is evidence about the method until the method is validated.*

**Probes, all in `Resources/FirmwareAnalysis/`:** `Motion32HostConfigProbe.java` (+
`run_host_config_probe.sh`, runs both programs), `Motion32CommandVocabProbe.java` (+
`run_command_vocab_probe.sh`), `Motion32EmitterProbe.java` (+ `run_emitter_probe.sh`, **payload
only, deliberately**). Still unexamined: `FUN_000010a4`, the real inbound parser —
`FUN_00002ab8` is just `return 0x200040a0` and `FUN_000010a4` is its only caller. Worth a look to
bound the command vocabulary, but per evidence 1 it cannot change the answer above.

---

## 8. Source audit — what the 2026-07-24 pass added

Three source files that no doc had cited turned out to matter. Full provenance record in
**`Motion32_Source_Inventory.md`**; the substance landed in two new docs:

- **`Motion 32.surfacedata`** (the manifest's `hostDataFile`) is the **Control-Link assignment
  database** — 121 pages of 8 encoder assignments across ~90 plugins, the 3 factory **User command
  pages**, the touch strip as a per-page assignable target, and `Channel`/`Macro Controls` pseudo-devices.
  Plus `skin/skin.xml`, which reveals the **Auto-Fill** paging mode and confirms LCD buttons 0–3 = top
  row / 4–7 = bottom row. → **`Motion32_ControlLink_and_User_Mode.md`**
- **Text limits and the label-abbreviation algorithm** (`StringFormatter.compactify`) plus the complete
  factory colour palette, which we had only partially recorded. Every factory string is length-capped
  (encoder labels **7 chars**). → **`Motion32_Screen_Style_Spec.md`**
- **`From Universal Control/`** describes the **stand-alone (non-native) MIDI scene** — absolute encoder
  CCs 16–19/80–83, pads on notes 80–111 channel 10, soft buttons CC 106–113. Not our protocol, but a
  third diagnostic signature: if a capture looks like *that*, the device is in the stand-alone scene,
  not native mode and not the pre-native half-state.

New wire facts folded into `Motion32_Control_Surface_Definition.md`: `touchStripButton[0]` = CC `0x7A`,
`touchStripButton[1]` = CC `0x7B`; the `lcdUserButton[0..7]` / `menuList*` virtual controls; encoder
**halo LEDs live at the encoder's own CC** (`0x0E`–`0x15`); and a direction-dependent address-overlap
table to check before writing `elements.py`.

---

### §6b-34 Taking a mapping into your own hands inherits the whole lifecycle (2026-08-03)

**Three hardware bugs in one component, all from the same root.** Mix mode's Sends page maps the
eight encoders onto (track × send) pairs itself, because the framework's `set_send_controls` maps
`controls[x]` onto `_channel_strips[x]` and a four-wide matrix therefore reaches strips 0-3 and
leaves half the ring unreachable. That decision was right. What was missed is everything the
framework had been doing *around* the mapping for Volume and Pan:

| Symptom on hardware | Missing duty | What the framework does |
|---|---|---|
| Turning an encoder did nothing after Left/Right | follow the ring | `MixerComponent.__init__` subscribes to `__on_offset_changed` on its provider and re-connects |
| Touch focused one track, the knob moved another's send | resolve "which track is this encoder" per page | on Volume/Pan encoder N *is* strip N, so the question never arose |
| **Plugin mode stopped binding its device** | release on disable | `ChannelStripComponent.update()` is `_connect_parameters()` / `_disconnect_parameters()` |

The third is the worst, because the damage lands somewhere else entirely: the encoders kept
`mapped_parameter` pointing at send parameters after the page left, so the Device component could
not take the elements and Plugin mode looked broken. Nothing about the symptom pointed at Sends.

> 🔑 **The rule: a component that maps parameters owns the whole lifecycle** — point them, follow
> whatever moves under them, resolve what each control *means*, and let go when it is not showing.
> Implementing only "point them" is the natural mistake, because it is the only part that feels
> like the feature.

⚠️ **The corollary for testing.** All three bugs live on the axis of *crossing* modes and pages, and
none of them is visible while you stay put. A mode that works in isolation is not tested.

### §6b-35 A layout that depends on state must be regenerated, not captured (2026-08-03)

Scale mode's first version handed the keyboard a finished pitch list. `_recompute()` then re-used
that frozen list, so A–H banking moved `root_offset` and the pitches never moved with it.

Three symptoms, one cause, and the middle one is the tell:

* the pitch did not shift;
* the LEDs did not shift **on the bank press**;
* the LEDs *did* shift after the next pad press.

That last one exposed a second fault. There was a separate Scale pad painter that regenerated
`scales.locked_pitches` independently, so on a bank press the roles were unchanged (frozen list)
and the repaint was skipped, while a pad press ran the painter and recomputed from the *current*
offset. **Lights moving while notes do not is the second-opinion failure of §5.3b**, and here it
actively hid the real bug rather than causing it.

The fix is both halves: the keyboard takes a **layout provider** it calls on every `_recompute()`
with the current offsets, and Scale mode has **no painter of its own** — it reports roles through
`keyboard.pad_roles` and the one keyboard painter draws them.

> Same shape as `_pad_root_offset` (§6b-24) and the Mix focus: **two copies of a derived fact will
> diverge, and the copy that is easier to refresh will make the other look correct.**

### §6b-36 Two views on one template: `activate()` is not enough (2026-08-03)

Scale mode's menu and the notification bar both draw **Template 1** — the collision the roadmap
flagged in §5.6 and left for whoever needed it first.

They coexist because they are never both active and each claims every element on the way in
(§6b-25). What did *not* work was returning: the bar hides the twelve menu rows to draw itself, and
coming back found **identical** content, so `render()` short-circuited and the rows were never
re-shown. `activate()` paints chrome; row *visibility* is set in `render()`.

This is the trap the roadmap already names for `MainView` — *"reset `forget()` at the same time or
the view short-circuits on an unchanged snapshot and nothing is redrawn"* — and sharing a template
is what finally made it reachable. `_render()` now calls `forget()` on a view as it becomes active.
Free in practice: the model's diff still sends only the difference.

**Consequence for the bar.** `notify()` is suppressed while the scale menu is up. Octave and A–H
still announce themselves everywhere else, but in Scale mode the bar would wipe the list being
scrolled, once per detent — and the menu already shows the state permanently.

### §6b-37 Three ways a substring guard is wrong (2026-08-03)

The suite's rule is to match **structure**, not source text. `_exec_module_function` exists for
exactly this, and its docstring already recorded one failure mode. In a single session three more
appeared, so here they are together:

| Guard | Failure | Fix |
|---|---|---|
| `"sends.bind_session_ring" in surface` | **too weak** — the explanatory *comment* above the call contains the same text, so deleting the call still passed | walk `_bind_screen_sources` for an `ast.Call` whose receiver is `sends` |
| a test that re-implemented `page_table`'s arithmetic | **too weak** — it verified its own maths; reintroducing the bug did not fail it | move the rule to module level and `_exec_module_function` it |
| `"_strip_track" not in ast.dump(selector)` | **too strong** — the function's own name, `_select_strip_track`, contains that substring, so it could never pass | collect `ast.Call` attribute names and test membership |

> ⚠️ The middle one is the dangerous one: a guard that re-derives the rule it is checking will
> agree with itself for ever. **Execute the real function or compare against the real structure —
> never restate the logic in the test.** §5's discipline (reintroduce the bug and watch it fail) is
> what caught all three, and it caught the *guards* rather than the code each time.

---

### §6b-38 Check the docs before re-deriving them, and name which state a fact belongs to (2026-08-08)

A session spent three exchanges re-deriving facts that §5.1b of `Motion32_Pads_Banking_and_Strips.md`
had recorded on **2026-07-30**: that native mode emits pitch bend and nothing else, that `0x7A`/`0x7B`
bracket each gesture as contact sensors, and that Shift changes nothing on the wire. A fresh capture
re-confirmed all of it. Nothing was wrong; the work was redundant.

**The trigger was a false negative in my own search.** Looking for whether the strips had been
captured in native mode, I searched for the *claims* (`"Mod wheel" is out`, `cannot emit CC 1`) and
found them in the roadmap — a **summary** — and treated the summary as the whole record. §5.1b, the
primary source three files away, had already answered the question the summary left open.

> 🔑 **When a doc restates a conclusion, find the doc that *earned* it.** Roadmaps and READMEs
> compress; they drop the capture that settled the thing. `grep` for the conclusion finds the
> compression. Search for the **evidence** — `[CAP`, `[SRC`, a date stamp, a hex address — and read
> the section around it before deciding something is unknown.

**Second, and more general: every strip fact is state-relative, and the docs are only safe because
they say so.** There are three states, and the same physical gesture produces different MIDI in each:

| | Stand-alone | Pre-native half-state | Native mode |
|---|---|---|---|
| Strips send | Pitch/Mod/Expression/Breath, ch 0 | — | **pitch bend only**, ch 0 / ch 1 |
| Shift secondary | **on the device** | — | **not on the wire** |
| Return to centre | **device does it** | — | **nobody does it** |
| Screen | ignores our SysEx | works | works |

I asserted "the device does return-to-centre itself" from a stand-alone capture, as though it were a
property of the device. It is a property of *stand-alone mode*. §5.1b avoids this trap by opening with
"every claim in §5.2/§5.3 below is a *native-mode* claim" — a habit worth copying: **a wire fact
without its state is not a fact.**

**Third — the one genuinely new thing that session produced came from cross-checking two methods, not
from one more capture.** Every strip value on the wire is a multiple of 16, so the 14-bit pitch-bend
field carries 1024 steps. The firmware disassembly had independently found a **10-bit ADC** (§6b-33,
`FUN_00001288`). Neither observation is remarkable alone; together they turn "14-bit" — stated in five
places — into a precise and actionable claim. **Agreement between wire and bytecode is worth more than
a third capture of either.**

> ⚠️ The corollary for `[SRC]`-derived conclusions: "the device cannot do X" is nearly always
> "the device does not do X *in the state I looked at*". Studio Pro's JS shows the **host** generating
> mod and expression, which is true, and says nothing about what the device does when no host is
> listening. Reading a capability out of a host's source proves what the host does, not what the
> device lacks.
