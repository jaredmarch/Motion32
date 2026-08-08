# Motion 32 → Ableton Live — Build Roadmap & Working Method

**Status (2026-08-03): Phases 0-8 and Phase 10 are done.** Song, Plugin, **Mix** and **Scale** modes
are live, with the screen, encoder halos, wheel, per-mode soft buttons, the pads as a playable
keyboard, Octave ±, A–H banking and clean teardown all running on hardware. Phase 7c (meters) is confirmed on hardware too, and **7d — the Sends page — joins them.** **Phase 8
(Shift pad overlay)** and **Phase 10 (Scale mode)** are both built; Scale is confirmed on hardware,
the Shift overlay was confirmed on 2026-08-08.

**Agreed build order (user, 2026-07-25):** colour system → pads → A–H → Mix mode → shift pad overlay →
touch strips → Scale → Chord. That is Phases 4-11 below, numbered to match so the plan reads top to
bottom. **Phase 4's conversion layer is done** (`palette.py`); what remains of it is applying the colours,
which lands naturally with Phases 5-7. **Phases 7 (Mix, now with Sends), 8 (Shift pad overlay) and 10 (Scale) are all built** (2026-08-03).
The agreed order has therefore been run out of sequence — Scale was taken before the touch strips at
the user's request. What remains of it is **touch strips (Phase 9)**, which also carry the one known
defect in shipped behaviour, and **Chord (Phase 11)**.

**Nothing on the roadmap is blocked.** The pad-note question — the last blocker — was closed by source
rather than capture (`Motion32_Scale_and_Chord_Engine.md`). Session mode is consequently unblocked but
sits unsequenced in §3b, outside the agreed run. Scale and Chord are deliberately parked as Phases
10-11, the last features to integrate. §2 is the current-state snapshot. This doc is the plan of record.

---

## 0. Working method (the discipline — read first)

1. **One feature at a time.** Define expected behavior + exact wire I/O → implement minimal →
   test on hardware and read the MIDI log → confirm stable → only then move on.
2. **Every mapping is grounded in a verified capture**, not the spec's `[INF]` assumptions. The
   handshake spec tags several controls `[INF]` (inferred) — those must be confirmed against real
   device→host input before we bind them.
3. **One owner per screen element and per LED.** No element is written by two code paths. This is
   the rule the current display broke (manual repaint + leftover display-line elements → label flph).
4. **Framework idioms over hand-rolled loops.** Use the `ableton.v3` Content/View display system,
   Components, and `create_mappings` the way the factory Atom SQ does. Only hand-roll where the
   Motion genuinely exceeds the framework (value/color screen attrs, 4 templates).
5. **Confirmed reference vocabulary** (extracted from the factory `ATOMSQ` bytecode) is the source
   of truth for control/component names — see Appendix A.

---

## 1. How data flows (mental model)

Remote scripts run **in-process inside Live** and use the **Live Object Model (LOM)** Python API.
**Ableton never sends us SysEx.** Two paths:

- **Input (hardware → Live):** device sends CC/notes → framework `Element` → mapped `Component`
  sets LOM state (`parameter.value`, `track.mute`, fires clips, …).
- **Feedback (Live → hardware):** we attach **listeners** to LOM objects
  (`param.add_value_listener`, property observers). On change we **emit** CC/SysEx to the device.
  Event-driven, not polling.
- **Meters** are the exception — Live doesn't push meter deltas efficiently, so VU is **polled on a
  rate-limited timer**.

Implication: "see data coming from Ableton when I turn a knob" = our script's **outgoing** screen
SysEx reflecting the new value. There is no inbound value packet.

---

## 2. Current state (snapshot — 2026-08-03)

> This is a *state* section, not a changelog. The chronology of every bug and fix lives in
> `Motion32_Implementation_Notes.md`; this says only what is true right now.

> **2026-08-03 — a long session: audit, fixes, then three features.** Three missing skin namespaces,
> a new LED colour contract, five audit defects, the **Mix meters (7c)**, the **Shift pad overlay
> (8)**, **Scale mode (10)** and the **Sends page (7d)**. Five hardware runs, each of which found
> something. Full record in `Motion32_Ableton_Build_Handoff.md` §7; the durable lessons are
> `Motion32_Implementation_Notes.md` **§6b-34 … §6b-37**.
>
> ✅ Confirmed on hardware: the meters, the volume reveal, Scale mode re-laying the pads, and the
> **Shift pad overlay** (2026-08-08, incidentally — it turned up inside a touch-strip capture).
> ⚠️ Not yet seen: the LED colour contract, and the Sends page after its three fixes.
>
> **The two sessions before that were research**, and both changed what the plan should be rather
> than what the script does:
>
> - **Firmware (§6b-33).** The device's control mapping is fixed at manufacture — CC numbers are
>   `movs` immediates, the config selector has one boot-time writer, and exactly two variants exist
>   (Motion 32 / Motion 16). No handshake can repoint a control. This closes a line of enquiry rather
>   than opening one: stop looking for a device-side escape hatch.
> - **Pitch bend (§5.3b of the Pads/Strips doc).** Live's framework *does* support pitch bend —
>   `MIDI_PB_TYPE`, `forward_midi_pitchbend`, `map_midi_pitchbend_with_feedback_map`. The previous
>   "final" verdict that strip 2 was hopeless was partly wrong, and **Phase 9 below has been rewritten
>   accordingly**.

**The script loads and runs on hardware** (Live 12, firmware 1.0.6, DAW Mode Off, `Motion 32 Main`).
**26 modules, 9.3k lines** (6.4k excluding blanks and comments — this project carries its reasoning
in the source, so the two counts differ a lot), plus an **8.5k-line** `tests/test_screen.py` —
**169 test groups, 3999 assertions, no Live and no hardware required** (`pip install xdis` is a
prerequisite; the suite fails without it rather than silently skipping the framework-derived guards).

### Working, verified on hardware

| Area | State |
|---|---|
| Handshake | Native mode via `hello_messages = (NATIVE_ON, IDENTITY_REQUEST)` + manual reply parse; firmware read from fixed offsets 11/12/13 |
| Teardown | LEDs to state 0 + white, screen to empty/white/visible, then `8F 00 00` — matched to a Studio Pro shutdown capture |
| Transport | Play/Stop/Record/Tap with source-accurate colours; Shift+Play/Stop/Record/Tap = Loop/Undo/Capture/Metronome |
| Modes | **Song** (T3), **Plugin** (T0), **Mix** (T2/T0) and **Scale** (T1) as a strict radio; **Control** returns from Scale to the previous mode. Only **Edit** is deliberately unbound |
| Screen | Cached, diffed renderer over all four templates; suspends during the device's Global Settings screen and fully redraws on close |
| Encoders | 8 relative encoders (`LinearSignedBit`), Shift as fine modifier, capacitive touch reveals values |
| Halos | Ours exclusively — see §LED ownership below. Purple in Song, **the owning track's colour in Plugin**, the eight track colours in Mix, white on touch, dark when unassigned |
| Wheel | Scrolls parameter banks in Plugin mode; click steps devices with wraparound; **pages Mix between Volume, Pan and the Sends pages**; **scrolls the scale list** in Scale mode; halo lit for the whole of Plugin, Mix and Scale |
| Soft buttons | All 8 assignable **per mode**. Song uses 6; Plugin claims none yet |
| Song mode | Session/Arrangement header, selected-track bar, 8 named encoders incl. cue volume, Loop + Back-to-Arrangement, Solo/Mute on the focused track |
| Plugin mode | `Track \| Device` header, bank name on a grey strip, 8 device parameters, opens Live's Detail view, Preset Up/Down steps devices |
| Pads | Piano ("Keys") layout lit from the track colour, playable through note translation, held pads flash green |
| Octave ± | ±3 octaves, two-channel LED model, `Octave` on the notification bar |
| A–H banking | Radio of eight resting on `E`, **one scale degree per step**; the keybed slides and the gaps move with it |
| Mix mode | Three pages — Volume, Pan and **Sends**. Template 2's eight strips off the **Mixer component** (so the view follows the session ring); L/R pages the ring by 8; encoder cap-touch selects the strip so Solo/Mute follow it; the 8 LCD buttons arm the 8 strips. Page 2 is **Pan** on Template 0's arcs, reached by turning the wheel, and the pages wrap. ✅ **Level-banded meters at 10 Hz, confirmed on hardware 2026-08-03** (§7c). Encoder touch also shows the strip's volume on its label while held. **Sends** is a (track × send) encoder grid whose page count comes from the set (§7d) |
| Shift pads | Hold Shift and the bottom lane is a 16-slot edit layer (6 filled); the top lane is dark and consumed. `ComboElement` priority means no pad both commands and plays |
| Scale mode | Template 1 list, wheel-scrolled, `Main`/`Modes`/`Key` + a single `Guide`/`Locked` toggle. Locked collapses the pads to one lane of the scale; Guide keeps the piano and dims what is out of scale. Writes root + scale back to Live |
| Notification bar | Generic `notify(title, value)` on Template 1 for ~1 s, outranking every mode. Octave and A–H banking are the two callers |

### The two findings that shape everything else

**1. The framework source is in the repo** at `Motion32/Resources/control_surface/` (`.pyc`,
decompile with `xdis`). It is the **first stop for any framework question**, ahead of the Atom SQ
scripts. It has already pinned `DeviceComponent.parameters` as a `listenable_property` (which
unblocked banking), proved `create_skin` merges over the default (which unblocked
`Device_Navigation`), and caught a pre-hardware bug where `parameters` yields `ParameterInfo`
wrappers rather than parameters.

**2. Unknown `Layer` names fail silently.** Binding `prev_button` to a component that has no such
control produces no error, no log line, and no behaviour. This makes the offline test suite
load-bearing rather than optional: it checks every mapping name against the real component classes.

### LED ownership (the one design rule that isn't obvious)

An encoder halo has **no address of its own** — it is the encoder's own CC. So the framework's element
writes land on the light, via two paths: parameter feedback (a flag) and element reset (not a flag;
`install_connections()` calls `reset()`, `reset_state()` sends the off value, and this fires on every
layer grab). The fix is `MotionEncoderElement`, which drops the element's outgoing writes so `leds.py`
is the only writer. **Do not re-introduce timer-based re-asserting** — full reasoning in
`Motion32_Implementation_Notes.md` §6b-10.

Consequence: a halo cannot safely carry transient state. Halos are mode-level indicators.

### Not started

**Edit mode**, the touch strips, Scale/Chord menus, Session mode, and the Template 1 Menu list view.
The **Shift pad overlay shipped 2026-08-03** with six of sixteen slots filled. Their elements exist; a mode button with no matching mode binds a
control the framework never created, which is why the unused ones are left unbound rather than
half-wired.

**Mix mode moved off this list on 2026-07-29**, Phase 7b on 2026-07-31, the **meters (7c)** and the
**Sends page (7d)** on 2026-08-03 — Mix mode is complete. The meters are confirmed on hardware; the
Sends page is confirmed only *before* its three fixes, so crossing modes into and out of it is still
an open hardware check.

---

## 3. Phased plan (each phase is test-gated)

### Phase 0 — Authoritative control-surface definition  ✅ DONE
The control surface is **already fully defined** by the reverse-engineering: every control's
send/receive message is in the factory `Motion 32.surface.xml`, now consolidated and cross-checked
against `midi.py` (all match) in **`Motion32_Control_Surface_Definition.md`**. No hardware capture
is needed for the control-identity map. (An earlier draft of this plan wrongly proposed a capture
pass — corrected.) Only *behavioral* items remain for later capture (encoder accel, pad musical
notes, aftertouch); none block wiring.

### Phase 1 — Stable transport + navigation (no screen)  ✅ DONE
Temporarily disable custom screen writes. Bind, verify, and lock one control at a time using the
Phase 0 map and the confirmed factory control names (Appendix A): Play, Stop, Record, Loop
(shift+Play), Metronome, then arrows → track/scene nav. Gate: each button does exactly one correct
thing, confirmed in the log.

> Both prerequisites for Phase 2 are met: the identity firmware offsets are fixed
> (`Motion32_Implementation_Notes.md` §1a), and the renderer was built on
> `Motion32_Screen_Style_Spec.md` from the outset — character budgets and `compactify` live in
> `formatting.py` rather than being retrofitted across every write site.

### Phase 2 — Screen engine, rebuilt correctly  ✅ DONE (gate passed on hardware)
Re-render **only on real state change**; one owner per element; drive the text/value/color/visibility
primitives from a diffed content snapshot, not a loop. Gate: title + 8 encoder labels stable while
turning knobs; no reverts, no collisions.

**How it came out.** The framework's own display system is line-oriented (`display_line`,
`Justification`, `Text(max_width=…)`) and does not model per-element colour/value/visibility across 4
templates, so the renderer is hand-rolled — which §0.4 explicitly allows "where the Motion genuinely
exceeds the framework". The framework's *discipline* is kept: an immutable content snapshot, equality
as the change test, and a diff before anything reaches the wire.

Shipped structure:

| Module | Responsibility |
|---|---|
| `screen.py` | Named addresses per template + factory palette. Callers never write raw `(zone, element)` |
| `formatting.py` | `compactify` + the per-element character budgets |
| `display.py` | `ScreenModel` (desired/sent diff, suspend, invalidate, batched flush, teardown blank), `MainView` (Template 0) and `ParamsView` (Template 3) |
| `leds.py` | The same desired/sent diff for LED addresses the framework must not touch |
| `runtime.py` | Owner-scoped module state, so a script reload can't have the old instance blank the new one's screen |
| `screen_component.py` | Content source: follows the appointed device and its parameter values |
| `parameters.py` | Resolves which 8 parameters the encoders are actually wired to |

Two mechanisms worth carrying into Phases 3-8:

- **Desired vs sent, not one cache.** `flush()` sends the difference. A redundant re-render is free,
  and `invalidate()` (clear "sent") gives a correct full repaint after connect and after the device's
  Global Settings screen wipes the display. Reset `MainView.forget()` at the same time or the view
  short-circuits on an unchanged snapshot and nothing is redrawn.
- **Address validation in CI.** `tests/test_screen.py` checks every
  `(template, zone, element, attr)` the renderer emits against the 433 handlers in
  `Motion32_Screen_Template_Map.csv`. An address typo or an attribute an element doesn't accept fails
  offline instead of looking like "nothing happened" on hardware. Every new view should extend it.
- **Flush unconditionally.** An early version flushed only when the content snapshot changed.
  Switching mode away and back leaves the snapshot identical, so the queued *template select* never
  went out and the device stayed on the other template. The diff already makes a redundant flush
  free, so there is no reason to gate it.

**Also true of Template 3 (Song).** It was identified from a photo of Studio Pro and confirmed on
hardware: each tile has a separate label *and* value element, so both stay on screen and no
reveal-on-touch timeout is needed. It carries **no bar/arc attribute at all** — text only.

### Phase 3 — Plugin view (the flagship)
> **Already landed with Phase 2**, once the framework source made them safe: 8 encoders → device
> parameters with label + halo per tile; **param banking** on Left/Right; **device tabbing** on
> Up/Down; the centre area showing Live's real bank name. Labels cannot desync because the screen
> listens to `DeviceComponent.parameters` (listenable), which fires on both device and bank change.
> Remaining for this phase: **lock** (`device_lock_button`), device on/off
> (`device_on_off_button`), bank *select* buttons (`set_bank_select_buttons`, e.g. on the A-H bank
> buttons), and a bank "x of y" readout if wanted.

- 8 encoders → focused device params; screen shows label + value-fill + halo per tile. ✅
- **Param banks:** tab across a device's parameter pages. ✅ — on the **big wheel** as
  `bank_scroll_encoder`, plus Up/Down buttons. Bank-select grid still to do.
- **Device tabbing:** move focus across multiple devices on a track. ✅ — note the control names are
  `scroll_up_button`/`scroll_down_button`, because `Device_Navigation` extends `ScrollComponent`.
  `prev_button`/`next_button` do not exist and bind **silently**.
- **Lock** focus to a device (`device_lock_button`).
- Gate: values track live (mouse + encoder), banks/devices switch cleanly, labels never desync. ✅

> **Encoder feel, settled.** `quantized_parameter_sensitivity = 1.0` on the Specification. The
> framework default is **0.1**, which is why a toggle or enum took ~10 detents to advance one step.
> This was never an encoder-acceleration problem, and acceleration remains uncaptured.

> **Known framework crash, not ours.** `banking_util._get_parameters_for_bank_index` raises
> `IndexError` for a Max for Live device that declares bank indices beyond its own parameter list
> (`[device.parameters[i] for i in device.get_bank_parameters(n)]`). Entirely framework code; it
> surfaces more often now that Left/Right appoints devices. Nothing to fix from our side.

**Follow the factory Control-Link model here** — it's now fully documented in
`Motion32_ControlLink_and_User_Mode.md`. Specifically: a page is a *sparse dict* of 8 (an unassigned
knob is legal and renders grey, not stale); the active page is **persisted per device**; the paging
readout is `title` + `n / m`; and the **touch strip is a 9th assignable target per page** — a
Motion-only capability the Atom SQ never had, and a strong v3 candidate. Live gives us both halves of
Fender's `pagingMode` for free (curated device banks ≈ user pages, default ordering ≈ Auto-Fill).

> **Build order set by the user, 2026-07-25.** Colour system → pads → A–H → Mix mode → shift pad
> overlay → touch strips → Scale → Chord. Phases 4-11 below are in that order and the numbering follows
> it, so the plan reads top to bottom. Session mode (formerly Phase 6) is unblocked but unscheduled —
> it now sits in §3b as an unsequenced item rather than interrupting the agreed run.

### Phase 4 — Colour system (device ⇄ Ableton parity)  ✅ **DONE (conversion layer)**
Stop using the Atom SQ approximations. **The factory palette is recorded** with 7-bit conversions in
`Motion32_Screen_Style_Spec.md` §3 — start from those values for non-Live UI states rather than
inventing them, and adopt the two factory conventions: white = active/assigned, `#BBBFC3` grey =
present-but-unassigned; `#4fd3ff` cyan = global assignment, `#fcca03` amber = focus assignment.

**The requirement that makes this first, in the user's words: translate Live's colours into device
colours without being bound to a pre-defined colour map.** Today `colors.py` has only hand-picked named
constants (`Rgb.BLUE`, `Rgb.YELLOW`, …) and *no* LOM conversion — nothing turns a real
`track.color` / `clip.color` / `scene.color` (`0xRRGGBB` ints) into 7-bit RGB. Pads want clip colours,
Mix wants track colours, A–H wants bank state. Build the conversion once here or hand-roll it three
times and refactor.

- `rgb7 = ((c>>16)&0xFF)>>1, ((c>>8)&0xFF)>>1, (c&0xFF)>>1` from the object's real `.color`.
- **One** conversion layer used by *both* screen colours and LED/halo/pad RGB, so the device agrees
  with the laptop screen — `colors.py` exposing `screen_rgb(obj)` and a LED `ComplexColor` builder from
  the same source (§4.4).
- Keep named colours only for non-Live UI states (transport, mode focus, shift).
- Gate: track/clip colours on the device visibly match Live, and an arbitrary user-chosen colour works
  without being added to any table.

### Phase 5 — Pads: lit and responding  ✅ **DONE — lit, playable, and flashing on press**
**A foundation phase, added 2026-07-25.** Pads were previously buried inside Session mode, which was
the wrong shape: they are a prerequisite for Session, the Shift overlay *and* Scale/Chord.

Addresses are settled and need no discovery — lane 0 = notes 36–51, lane 1 = 52–67, the same address
serving as both LED and note, with `midi.py` already defining `PAD_NOTES` and `leds.py` already being a
generic address-array class. See `Motion32_Pads_Banking_and_Strips.md` §1.

- Declare the pad elements; own their LEDs (state `0x90`, RGB `0x91`/`0x92`/`0x93`; Off/On/Blink/Pulse
  = `0x00`/`0x7F`/`0x01`/`0x02`).
- Get them lit from the Phase 4 colour layer and confirm note in/out, **without yet committing to a
  mode** — this phase ends with working, addressable, correctly-coloured pads, not with a feature.
- Respect the Keys layout: some top-lane pads are deliberately dark to preserve the white/black key
  relationship. A renderer that assumes 32 live pads is wrong (§2 of that doc).
- Gate: every pad lights in the intended colour, every pad sends the expected note, and teardown
  releases all 32 to the documented reset state.

**Delivered beyond the original gate** (2026-07-25/26): the pads are a **playable keyboard**
(`keyboard.py`, a `PlayableComponent`) in the piano layout decoded from a Studio Pro capture, they
**flash green from note-on to note-off**, the four gap pads are silent and dark (claimed on
`DEAD_PAD_CHANNEL = 15` so they cannot collide with a transposed pitch), and **Octave ± is wired**
with the factory's two-channel LED model. See `Motion32_Implementation_Notes.md` §6b-16…§6b-26.

### Phase 6 — A–H buttons: pad banking  ✅ **DONE**

> **Landed 2026-07-29, running on hardware.** A strict radio of eight resting on `E`, **one scale
> degree per step** — the factory only ever shifts the bottom row, so a press slides the keybed by
> one bottom-row pad (see §3 of `Motion32_Pads_Banking_and_Strips.md`). Announces `Root` / signed
> offset. Octave and the bank are the two *separate* arguments to `pad_pitches`, not one term: the
> octave transposes rigidly, the bank slides the window and moves the gaps. The screen component's
> duplicate `_pad_root_offset` is **gone** — the keyboard reports the roles it derives from its own
> pitch list, so the lights and the notes cannot disagree. Full write-up in
> `Motion32_Implementation_Notes.md` §6b-29, including why the wrong unit presented as an LED bug.

**Decision (user, 2026-07-25): follow the factory Keys-mode role — A–H is *pad banking*, resting on
`E`.** It shifts the pads' musical root along the piano; F/G/H move the root right, D/C/B/A move it
left, and E rests in the middle so there is room in both directions. This **supersedes** the earlier
Phase 3 suggestion that A–H might carry `set_bank_select_buttons` for device *parameter* banks — the
two roles are mutually exclusive and the factory role is the one the hardware is labelled for.
Parameter banking stays on the wheel and Left/Right, where it already works.

Full behaviour, including the two other context-dependent roles (Drum Blocks selects banks two at a
time; 16-Velocity selects the note bank) is in `Motion32_Pads_Banking_and_Strips.md` §3.

- Wire A–H (CC `0x00`–`0x07`) with LED state reflecting the selected bank.
- ~~Octave ± (CC `0x40`/`0x41`)~~ **✅ already done in Phase 5.** ±12 semitones globally, limit ±3
  octaves, dim blue at rest and dim white when *that direction* is engaged, with a 1 s notification
  bar. What remains for A–H is the *bank* half.
- Gate: `E` on load with Pad 1 at the root; moving the bank shifts the pads and the lit button follows;
  octave offset is visible on the buttons. **Confirmed on hardware 2026-07-29.**

### Phase 7 — Mix mode  ✅ **DONE — meters built 2026-08-03, see 7c**

> **Phase 7b — Pan page on the wheel — built 2026-07-30, confirmed on hardware 2026-07-31.** Mix mode has two
> pages: Volume on Template 2's faders and **Pan on Template 0's eight arcs** (Template 2 has no
> pan element). The big wheel pages between them and **wraps**. `Mix_Pages` is a nested modes
> component declared `"enable": False` and enabled only by Mix mode — the general recipe for a
> nested mode set, written up in `Motion32_Implementation_Notes.md` §6b-31.

> **Landed 2026-07-29:** `display.MixerView` renders Template 2
> — eight strips with number, name on the track colour, and a volume fader — fed by the **Mixer
> component** so the view follows the session ring. `mix` is a real mode on the Mix button, with the
> eight encoders on `volume_controls`. The 16 meter elements are **claimed and hidden**.
> **Second pass, same day:** Left/Right now pages the ring via `Session_Navigation` (it was
> wrongly on `View_Control`), cap-touch focus is **the track selection** so Solo/Mute follow it,
> the halos take the eight track colours, and the LCD soft buttons are the eight **arm** buttons.
> **Confirmed on hardware 2026-07-30**, and the meters (§7c) on 2026-08-03. ⚠️ The **Sends page**
> (§7d) has not been re-tested since its three fixes — specifically crossing Mix → Sends → Plugin.
> See `Motion32_Implementation_Notes.md` §6b-30, §6b-31 and §6b-34.

The largest phase in this run: it needs a **third screen view**. `display.py` had `MainView` (T0) and
`ParamsView` (T3) only — Template 2 had an address class in `screen.py` but no renderer — plus meters,
which are the one thing in the whole design that must be **polled** rather than event-driven.

8-channel strip on the Mixer template: volume/pan/sends on encoders, mute/solo/arm, meters, session-ring
border.

**Focus model — a deliberate divergence from the factory (user decision, 2026-07-25).** Studio Pro uses
`screenButtonsMode = MixerChannelSelect`: the soft buttons select the channel, and holding Solo/Mute
plus a soft button does per-channel solo/mute. **We instead focus the channel by encoder capacitive
touch** (CC `0x70`–`0x77`), so Solo and Mute act on the last-touched channel strip. The roadmap already
anticipated cap-touch as a focus mechanism (§4.3), and `Target_Channel_Strip` — already wired for global
solo/mute — is the component that makes it work.

> ⚠️ **The focus must persist, not time out.** This is the explicit difference from the Plugin screen's
> reveal-on-touch, which reverts after `ACTIVE_PARAMETER_TIMEOUT` (0.75 s). A *focus* is a selection and
> must survive until another encoder is touched; only the on-screen *value* readout should time out.
> Do not reuse the Plugin-mode timeout task for this — it is the same event source with opposite
> semantics, which is exactly the kind of reuse that produces a subtle bug.

- Gate: ring follows selection; the focused strip is unambiguous on screen and in the LEDs; Solo/Mute
  hit the focused channel; focus survives an idle period; meters smooth and rate-limited.

#### 7c. Meters — ✅ **DONE — confirmed on hardware 2026-08-03**

> **What shipped.** `MixerStrip` carries `meter_left` / `meter_right` / `metered`; `MixerView`
> renders them (and `paint_chrome` no longer touches those addresses — one owner);
> `screen_component` polls at `METER_INTERVAL = 0.1` through `task.loop`, gated on Mix mode **and**
> the Volume page, killed on teardown. `_track_meters()` reads `output_meter_left`/`_right` and
> `has_audio_output`. Colour is banded green/amber/red via `display.meter_colour()`.
>
> **Two decisions taken at build time (user, 2026-08-03):**
>
> - **Level-based colour**, not the track colour and not left unset. ⚠️ The thresholds
>   `METER_AMBER_AT = 0.76` / `METER_RED_AT = 0.92` are **inferred from where Live draws its own
>   amber and red** and have not been checked against hardware — Live's value is its normalised
>   display scale, neither dB nor linear amplitude. Two named constants so the correction is one
>   line.
> - **Banded, not a gradient, and this is load-bearing.** A screen element takes one colour and one
>   value, so a continuously varying colour must be re-sent every frame — 16 extra messages per
>   frame, doubling meter traffic from the factory's 160/s to 320/s. Quantised, the colour only
>   becomes a *different* payload at a crossing, so the diff drops it on nearly every frame. Do not
>   "improve" this into a ramp.
>
> ⚠️ **A screen colour is one SysEx with an R G B payload, not three messages.** That is the LED
> model, and conflating the two put this doc's first traffic estimate out by a factor of three.
>
> The three open questions below are unchanged and are now **hardware questions** — the run-through
> is item 5 of `README.md`'s "What to try".

**The captured factory model** `[CAP 2026-07-31]`

A Studio Pro capture settles how meters actually work, which is what the deferral was waiting on.
Each update is an ordinary Template 2 screen write — no special meter message exists:

```
F0 08 26 21 | 02 02 07 02 | 3D | F7      template 2, zone 2, element 7, attr 2 (value)
                    │  │                  element 07 = METER_LEFT, 08 = METER_RIGHT
                    └──                   zone N -> strip index N-1
```

Four observations, each of which decides a design question:

1. **10 Hz.** Frame intervals run 96–117 ms. That is the factory's own rate, so it is sufficient by
   demonstration rather than by guess. Eight strips = 16 messages per frame, 160/s, ~1.6 kB/s.
2. **All four messages of a frame share one millisecond** — sent as a batch, not trickled.
3. **The host does the ballistics.** Note-off at `10.380`, meter still decaying at `16.461` — six
   seconds later, smoothly (`3D 3A 37 33 30 2C 29 25 22 1F …`). The device renders whatever number
   it is handed and does no decay of its own.
4. **The factory does not diff** — strip 1 repeats `04` across five consecutive frames. Our
   `ScreenModel` desired/sent diff would suppress those, so we would send *less* than Studio Pro for
   an identical result.

**Ableton side.** `Track` exposes six meter properties, read-only and normalised 0.0–1.0:
`output_meter_left` / `output_meter_right` (smoothed momentary peak — the pair we want),
`output_meter_level` (held peak, 1 s hold), and the three `input_*` equivalents.
⚠️ Meters live on **`Track` only** — not `MixerDevice`, not `Chain`. And the framework has **no**
meter support to build on; a grep that appears to find `meterComponent` / `meterBank` /
`meter_provider` is matching inside *para·meter*. This component is ours to write.

**Sketch.** A `task.loop` at 100 ms over the session ring's eight tracks, writing
`round(track.output_meter_left * 127)` into the existing `ScreenModel` diff, exactly like any other
element. Live has already done the smoothing, so no ballistics code is needed — which is the whole
reason this is cheap. Polling, not listeners: the properties are observable, but they fire far faster
than 10 Hz and would flood the diff for no visible gain.

🔑 **Meters can be switched off per strip.** The CSV carries `METER_LEFT_VISIBLE` /
`METER_RIGHT_VISIBLE` alongside the value, so a strip can render with **no meter at all** rather than
a dead one. That matters because a MIDI track with no instrument has `has_audio_output == False` and
will read 0.0 forever — eight strips where three sit permanently empty reads as a bug. Hiding those
two elements is the honest rendering, and it is also the answer for return/master strips if the ring
ever shows them.

Three things to confirm before building:

- Does the 0.0–1.0 value map linearly onto the device's meter rendering? Live's number is its own
  normalised display value, not dB. Compare against Live's on-screen meter for the same signal.
- Do meters keep updating when Live is in the background or the track is off-screen? If not, they
  freeze mid-decay on app switch and need a zeroing path.
- Do the `*_VISIBLE` attributes need setting once on Mix-mode entry, or on every template load?

- Gate: meters track Live's own within a strip's width; no meter on a track that cannot produce
  audio; no added latency to encoder or pad handling while the loop runs; the loop stops when Mix
  mode is not active.

#### 7d. Sends — the (track × send) grid  ✅ **BUILT 2026-08-03**

The eight encoders as columns of tracks and rows of sends, so encoder 1 and 5 are send A and B of the
same track. The page count is derived from the set — sends taken in pairs, a leftover odd send given
its own page of one row × eight tracks, so **no encoder is ever dead**. `sends.py`.

⚠️ **One mode, several wheel steps.** A `ModesComponent`'s mode list is fixed at mapping time and the
page count is a fact about the user's set, so `mixpages.py` expands the single `sends` mode.

⚠️ **Three hardware bugs from one root**, all of them duties the framework discharges silently for
Volume and Pan: follow the ring, resolve which track an encoder means, and release the parameters on
disable. The third stopped **Plugin mode** binding its device. **§6b-34** — the most transferable
lesson of the session.

### Phase 8 — Shift pad overlay  ✅ **BUILT 2026-08-03 — confirmed on hardware 2026-08-08**

The bottom lane (notes 36–51) becomes a 16-slot edit layer while Shift is held; the top lane goes
dark and silent. `commands.py`.

**Six slots filled, ten grey — and the shortfall is now settled rather than suspected.** A grep for
`split`, `consolidate`, `join`, `freeze` and `flatten` across all twelve LOM reference files finds
nothing, so **Split** and **Merge/Consolidate** are confirmed impossible, and **Insert Pattern / New
Variation / Duplicate Variation** are Studio One concepts Live has no equivalent of. Copy/Paste are
*deferred, not impossible*: `ClipboardComponent` needs a source object tapped on a clip grid, so they
arrive with Session mode.

| Slot | 1 | 2 | 3 | 4 | 5 | 6 | 7–16 |
|---|---|---|---|---|---|---|---|
| | Undo | Redo | Dup | Delete | Quant | Double | grey |

🔑 **The mechanism is `ComboElement.priority_increment = 0.5`** — a *bound* Shift-modified pad
outranks the keyboard binding and takes the press, so no pad both commands and plays. ⚠️ An
*unbound* one claims nothing, which is why the top lane is bound to a `BackgroundComponent` to be
consumed rather than simply left alone.

⚠️ **`Clip_Actions` is deliberately not bound to the pads** despite implementing four of these
commands with availability LEDs: it would take LED ownership of four pad addresses and leave
twenty-eight with `PadLeds`. See `commands.py`.

- Gate: each command verified individually on hardware; unmapped slots visibly grey, not
  dead-but-lit; no pad plays a note while Shift is held.

### Phase 9 — Touch strips
Two strips, and they are richer than we had recorded — **touch and position are separate streams**, so
gestures the factory cannot express are available to us. Full reference:
`Motion32_Pads_Banking_and_Strips.md` §5.

- Position = **14-bit pitch bend message carrying ~10 bits of signal**, strip 1 on channel 0,
  strip 2 on channel 1. Values are quantised to multiples of 16 — 1024 steps, not 16384. Confirmed
  on the wire and by the firmware's 10-bit ADC (`Motion32_Pads_Banking_and_Strips.md` §5.1c).
- Touch = **CC `0x7A`/`0x7B`** — the contact sensor, *not* a physical button as the control-surface
  definition previously claimed.
- 🔑 **Return-to-centre is the host's job — in native mode.** Confirmed twice: the strip's last value
  is wherever the finger left it. ⚠️ The device *does* self-centre in **stand-alone** mode; that is a
  property of the state, not of the hardware (§6b-38).
- Shift + touch a strip toggles the secondary identity (Pitch↔Expression, Mod↔Breath) — free, since it
  rides the touch event we already receive, and free of device cooperation since **Shift changes
  nothing on the wire** (so the choice of target is entirely ours).
- 9 LEDs per strip (`0x37`–`0x3F` / `0x70`–`0x78`), colour-only, bipolar for pitch and fill for the
  rest.

⚠️ **Scope corrected 2026-07-31. Read `Motion32_Pads_Banking_and_Strips.md` §5.3b before writing any
code** — three of the bullets above are not reachable as originally written.

- **"Mod wheel" is out *for the script*.** A Remote Script cannot emit CC 1 into Live, and
  `_translate_message` has no pitch-bend branch (verified in bytecode). Name any mode we build for
  what it actually drives; calling one "Breath" is a lie that will confuse a later reader.

  ✅ **But the mod wheel is reachable — via a device, decided 2026-08-08.** A Max for Live effect
  using `[midiselect]` → `[ctlout]` converts strip 2's channel-1 pitch bend into **CC 1** and passes
  strip 1's channel-0 bend through untouched, because `midiselect` forwards everything it did not
  select. Real CC 1 into the VST's own hook, and the double bend gone, from one device.

  ⚠️ **This inverts the strip-2 fix below.** The converter can only convert what reaches it, so
  strip 2 must stay **un-consumed** — and the double bend therefore persists on any track without the
  device. The device *is* the fix. See `Motion32_Pads_Banking_and_Strips.md` §5.1b for the full
  decision, the candidate devices and the rejected conditional variant.

  **The script never inserts a device unprompted** (user, 2026-08-08). Insertion is a deliberate
  action — `track.insert_device(name, 0)` (Live 12.3+) or `browser.load_item()` over
  `browser.midi_effects` — on a soft button or one of the ten empty Shift pads.
- **The secondaries are not on the wire** — confirmed by capture twice, shifted and unshifted streams
  byte-identical. Expression and Breath exist only as host-side reinterpretations of the same
  pitch-bend stream. The Shift *button* is ours, so the toggle is still implementable — but only over
  targets we own.
- **The no-Python-latency gate collides with the LED bars.** `PitchBendFeedbackRule` sends pitch bend
  back to the device; the LED bars are CC addresses. Engine mapping therefore cannot light them, and
  lighting them requires the value in Python. §5.3b has the map-vs-forward table and the cheap
  hardware test that decides it. **Resolve that test before committing to a design.**
- ⚠️ **First gate, cheapest and untested: can we even see the contact sensor?** `0x7A`/`0x7B` are the
  reserved MIDI **channel-mode** numbers (Local Control, All Notes Off), and the device sends `127`
  for All Notes Off, which is out of spec. If Live filters channel-mode messages before the script,
  the touch event never arrives and every gesture design above collapses. Declare one element and log
  it before designing anything on top of it.
- ⚠️ **Strip 2's forwarding is now a decision, not a default** — see the mod-wheel entry above.
  `ScriptForwarding.exclusive` — that is what
  stops its channel-1 pitch bend reaching the armed track and fighting strip 1. Today, undeclared, it
  double-bends the instrument. Strip 1 stays `non_consuming`.
- ⚠️ A hand-rolled branch in `receive_midi()` **will not fire** — Live forwards only what an element
  registered. The strips must be declared elements.

- Gate: pitch returns to centre on release; strip 2 no longer reaches the armed track; strip 2 drives
  its bound parameter; LED bars track the finger *or* the decision to drop them is recorded with its
  reason; strip 1's existing pitch bend still works.

### Phase 10 — Scale mode  ✅ **BUILT 2026-08-03 — confirmed on hardware**

Taken out of sequence at the user's request. `scales.py` (the framework-free engine), `menu.py` (the
Template 1 list, now general enough for Chord and browser navigation) and `scalemode.py` (state, soft
buttons, wheel, and the Control button that returns).

The factory's soft-button designation came from `Motion32_State_Trace_Table.md` §Scale `[SRC]` —
*"wheel selects scale/key; soft buttons pick Main/Modes/Key + Guide/Lock"* — with `Guide`/`Lock`
defined by the user as the two states of one pad layout. Full write-up in
`Motion32_Ableton_Build_Handoff.md` §7; the three hardware bugs are §6b-35 and §6b-36.

⚠️ **§5.6's Template 1 collision is now settled.** The scale menu and the notification bar share the
template; they are never both active, each claims every element on the way in, and the incoming view
`forget()`s so an unchanged snapshot cannot strand it. The bar is suppressed entirely while the menu
is up.

### Phase 11 — Chord mode  ⏸️ deferred
Still the last feature. Its menu view now exists, and the two triads it needs are already in
`scales.SCALES` — kept there deliberately when they were dropped from the Scale menu. Detail, with confidence tags separating established fact from
untested speculation, is in **`Motion32_Scale_and_Chord_Engine.md`** §5; the six `[VERIFY]` questions in
§5.4 are the place to start when they come off the shelf.

**The one rule that must survive the deferral:** *no Python in the pad→note path.*

---

### Unsequenced — Session mode
Formerly Phase 6, and **no longer blocked** (pads send fixed notes 36–67, closed by source rather than
capture). Left unsequenced because the user's agreed run above does not include it; it becomes cheap
once Phases 4-6 land, since it needs exactly the pad LEDs, colour translation and banking they deliver.
Clip grid on pads with RGB clip colours, clip launch/stop, scene launch, session-ring navigation,
overview. Gate: launching/stopping and colours correct; nav matches the ring.

### Unsequenced — notifications, polish
**On-screen notification overlays: ✅ done (2026-07-26).** A generic title/value bar on
Template 1, up for 1 s, outranking both modes while shown — `notification.py`, and
`Motion32_Implementation_Notes.md` §6b-25 for why it costs two messages where the factory
spends sixty-five. Octave is the first caller; **A-H banking is the obvious second**, and
Studio Pro does *not* show a bar for it, so that one is ours to add. Scale/root and tempo
nudge want the same two fields.

Still open here: feedback-suspend gate hardening; teardown hardening.


## 4. Feature design notes (drill-downs)

### 4.1 Plugin view
Content per encoder tile = {label, value(0–127), color, visible}. Source = the device parameters the
`Device` component currently banks. Listeners on each mapped param → update only that tile. Title =
device name (own element/zone, never shared with soft-button label zones — the current collision is
title zone vs. header button-label zones overlapping; separate them explicitly).

### 4.2 Param & device tabbing
- Within a device: `Device` component param banks; page via bank buttons or soft L/R; show "x/y".
- Across devices: `Device_Navigation` prev/next; optional lock. Screen title reflects current device.

### 4.3 Mixer + focus indication
Ring-wide `volume_controls`/`pan_controls`/`send_controls`; `mute_buttons`/`solo_buttons`/
`arm_buttons`. Focused-track cues: light the soft button(s) for the focused strip; use encoder cap
touch to re-focus. `target_track_*` controls drive the "currently focused track" dynamic binds.

### 4.4 Color translation
`rgb7 = ((c>>16)&0xFF)>>1, ((c>>8)&0xFF)>>1, (c&0xFF)>>1` from the object's real `.color`. Single
module `colors.py` exposes both `screen_rgb(obj)` and LED `ComplexColor` builders from the same
source so screen and LEDs agree. Reserve named colors only for non-track UI (play=green, rec=red,
mode-focus=white, shift=magenta).

### 4.5 Session mode
~~Blocked on pad capture.~~ Unblocked — pads are fixed notes 36–67. Design: pads = clip slots of the
ring; color = clip.color; states stopped/triggered/playing/recording via pad LED value
(0x00/blink 0x01/pulse 0x02) + RGB. Scene launch on a dedicated control; nav moves the ring.

### 4.6 Shift command → Ableton mapping (research table)
Remote scripts **cannot inject OS keystrokes**, so each command must resolve to a LOM call. Status:
- Undo/Redo → `song.undo()/redo()` ✓
- Duplicate (scene/track) → `song.duplicate_scene/track` ✓ ; clip duplicate ✓
- Delete → `song.delete_track/scene`, `clip_slot.delete_clip` ✓
- Quantize → `clip.quantize(...)` ✓
- Metronome / Loop / Tap → `song.metronome`, `song.loop`, `song.tap_tempo()` ✓
- **Split (Cmd+E)** / **Merge=Consolidate** → arrangement edits; **not exposed in the LOM** →
  research needed (likely not doable without a user-side Live key mapping; may have to drop or find
  an API path). Flag, don't assume.
- Grid prev/next, floating windows, insert part, patterns/variations → mostly device/clip-view
  specific; research per item.
Rule: implement the ✓ items first; keep a live list of the unknowns and confirm each before wiring.

---

## 5. Consolidated captures still needed (hardware)
1. ~~**Every control's device→host message**~~ — **CLOSED by Phase 0** (machine-extracted from the
   factory surface XML into `Motion32_Control_Surface_Definition.md`; no capture needed).
2. Encoder acceleration / Fine behavior under Encoder Curve.
3. Aftertouch format (channel vs poly).
4. ~~Pad musical-note output across Keys/Blocks/octave/scale/chord~~ — **CLOSED BY SOURCE
   (2026-07-25).** There is no per-Octave/per-bank transform on the device to capture: in native mode
   the pads send **one fixed note per pad** (36–51 / 52–67, straight from the surface XML) and every
   musical transform is host-side. **Session mode is unblocked.** See
   `Motion32_Scale_and_Chord_Engine.md` §2 and gap analysis §2.4. A one-minute corroborating capture
   (Octave-up, hit a pad, confirm the note is unchanged) is worth doing but blocks nothing.
5. ~~Whether screen/LED SysEx is accepted before vs. after the identity handshake~~ — **CLOSED.**
   Screen SysEx is accepted in the pre-native half-state, which is exactly what masked the handshake
   bug (`Motion32_Implementation_Notes.md` §1). Our order is native-on → identity → draw regardless.
6. Feedback-suspend gate (`F0 08 26 22`) timing — partly closed: the gate is handled and the screen
   suspends and fully redraws correctly on hardware. Only the device's own timing is uncharacterised.
7. ~~Touch-strip contact sensors at CC `0x7A`/`0x7B`~~ — **CLOSED by capture** (2026-07-30, re-confirmed
   2026-08-08). Not physical buttons: they are the strips' contact detect, a **separate stream from
   position**, and they bracket every gesture. Down `0x7F` / up `0x00` on both strips, confirmed. **No
   position update is sent on release** in native mode — the value sticks where the finger left it.
   Position is a 14-bit pitch-bend message carrying a ~10-bit signal (§5.1c).
   **Still open:** the Expression/Breath LED colour (the manual says green, the palette constant says
   orange), and — new, untested, and gating everything else — **whether Live even delivers `0x7A`/`0x7B`
   to a script**, since they are the reserved channel-mode numbers. See Phase 9.
8. ~~LED addressing and resting colours~~ — **CLOSED by a Studio Pro project-load capture**
   (2026-07-25). Every LED address decoded against `midi.py` with no unknowns: halos `0x0E`-`0x15`
   and wheel `0x1D` at state 127 / `(0,52,102)`; key LEDs on notes 36-67 with RGB on
   `0x91`/`0x92`/`0x93`; transport resting colours confirmed. See
   `Motion32_Implementation_Notes.md` §6b-11.
9. ~~Whether Studio Pro's Scale/Chord buttons trigger on-device menus or host-drawn ones~~ —
   **CLOSED: host-drawn.** The Chord press arrives as plain `B0 22 7F` and Studio Pro writes the
   entire Template 1 menu itself. There is no on-device UI to hand control back to.
   See `Motion32_Implementation_Notes.md` §6b-12.

**Still genuinely blocking something: nothing.** #4 was the last one and it is closed by source.
Everything remaining on this list is polish or characterisation.

---

## Appendix A — Confirmed framework vocabulary (from factory ATOMSQ bytecode)

Components: `Modifier_Background`, `Undo_Redo`, `Session_Navigation`, `View_Control`,
`View_Based_Recording`, `Transport`, `Mixer`, `Session`, `Lower_Pad_Modes`, `Device`,
`View_Toggle`, `Launch_And_Stop`, `Device_Navigation`, `Translating_Background`, `Main_Modes`.

Transport controls (confirmed used): `play_button`, `stop_button`, `loop_button`,
`metronome_button`, `capture_midi_button`, `arrangement_position_encoder`, `tempo_coarse_encoder`,
`prev_cue_button`, `next_cue_button`.

View_Control: `next_track_button`, `prev_track_button`, `next_scene_button`, `prev_scene_button`.
Session_Navigation: `up_button`, `down_button`. Device: `parameter_controls`. **Device_Navigation:
~~`prev_button`, `next_button`~~ → `scroll_up_button`, `scroll_down_button`** (⚠️ corrected
2026-07-25: the component extends `ScrollComponent` and has no prev/next; the old names bound
**silently** and device navigation simply never worked — see
`Motion32_Implementation_Notes.md` §6b-7). View_Toggle: `main_view_toggle_button`, `browser_view_toggle_button`,
`detail_view_toggle_button`, `clip_view_toggle_button`. Mixer (target): `target_track_volume_control`,
`target_track_pan_control`, `target_track_send_controls`, `target_track_solo_button`,
`target_track_mute_button`, `target_track_arm_button`, `crossfader_control`.
Display: framework `Content` + `View` + `CompoundView`/`NotificationView`; the factory reads
`state.target_track` and `state.device` and writes via display-line elements
(`track_name_display.display_message`, `button_label_display_{i}`).

> Note: absence from this list ≠ invalid (it only shows what the factory *used*). Presence = valid…
> **except where the framework has since changed.** This appendix was derived from Atom SQ bytecode,
> not from Live 12's framework, and at least one entry was wrong in a way that failed silently. The
> authority is `Motion32/Resources/control_surface/` — and `test_every_mapped_control_name_exists`
> now checks every mapping against it, so a stale name here fails offline instead of on hardware.
