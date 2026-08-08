# Motion 32 → Ableton Live: Build Handoff

**Purpose:** everything a new session needs to pick this up cold. The reverse-engineering is done and
**a working script is running on hardware** — this hands off where it stands, the rules that keep it
working, and what to do next.

**Last verified in sync with the code: 2026-08-03.** **26 modules, 9.3k lines** (6.4k excluding
blanks and comments), **169 test groups / 3999 assertions** passing.

**Four modes now:** Song, Plugin, **Mix** (Volume / Pan / **Sends**) and **Scale**. Plus the pads as
a keyboard, Octave, A–H banking, the notification bar, the **Shift pad overlay** and the
**Mix meters**.

**2026-08-03 was a long session: an audit, then fixes, then three features.** In order — a full
code audit against the docs; the Mix **meters** (Phase 7c); the **Shift pad overlay** (Phase 8);
**Scale mode** (Phase 10); and Mix mode's **Sends** page. Five hardware runs during it, each of
which found something. Full record in §7; the durable lessons are in
`Motion32_Implementation_Notes.md` **§6b-34 … §6b-37**.

The two research sessions before it both overturned things the docs asserted:

- **The firmware cannot be reconfigured by a host.** Settled, with four independent lines of
  evidence, in `Motion32_Implementation_Notes.md` **§6b-33**. Exactly two variants exist (Motion 32 /
  Motion 16), selected at boot from a product byte. Native mode grants an *output* surface (screen,
  LEDs, settings); it does not remap inputs.
- **Live's framework does support pitch bend**, contradicting the "final" conclusion previously in
  `Motion32_Pads_Banking_and_Strips.md` §5. That reopens Phase 9 as a real design choice — see the
  new **§5.3b**.

⚠️ **Unfixed defects in shipped behaviour:** strip 2 is undeclared and double-bends the armed
instrument (§8), and Song encoder 4 is labelled `Loop End` while showing the loop's *length*
formatted as a position (§7).

✅ **Confirmed on hardware 2026-08-03:** the Mix **meters** (levels, decay, and the green/amber/red
banding all read correctly against Live's own; the run also settled that `METER_LEFT_BACKGROUND`
colours the **bar**, not the trough, so the inferred thresholds stand), and **Scale mode** re-laying
the pads once its three bugs were fixed.

⚠️ **Not yet seen on hardware:**

1. **The colour contract** — Shift purple, Loop and Metronome yellow, Mute yellow-when-audible /
   red-when-muted, Plugin halos following the owning track, and the three skin-key fixes that make
   Shift, Mix Left/Right and Shift+Stop light at all. Table in `README.md`.
2. **The Shift pad overlay (Phase 8) — half confirmed.** The 2026-08-08 capture proves it *paints*
   correctly. ⚠️ It captured **outbound** MIDI only, so the load-bearing check is still outstanding:
   **no pad may play a note** while Shift is held. That is `ComboElement` priority doing its job, and
   the top lane only stays silent because it is bound to a background rather than left unbound.
   Neither is visible in an outbound log — it needs ears, or an inbound capture.
3. **The Sends page** after its three fixes, and specifically **crossing modes**: Mix → Sends →
   Plugin → Song and back. All three Sends bugs lived on that axis and none was visible while
   staying put (§6b-34).

> **Read this section first if you read nothing else.**
>
> 1. The script lives at `~/Music/Ableton/User Library/Remote Scripts/Motion32/` and **works today** on
>    Live 12 with firmware 1.0.6, DAW Mode **Off**, on the `Motion 32 Main` port.
>    The superseded-instance reload bug is **fixed and confirmed on hardware (2026-07-29)** — see §7
>    for the mechanism, which is worth knowing before debugging any "reload made it weird" symptom.
>    A–H banking and **all of Mix mode, meters included**, are confirmed on hardware.
>    ⚠️ **If a track will not arm, check its input first** — Live silently refuses to arm an audio
>    track with no input selected, and `can_be_armed` still reads `True`. That cost a long detour;
>    see §6b-31.
> 2. `Motion32_Implementation_Notes.md` **wins over every other doc**, including this one. It is
>    written from real hardware behaviour; the design docs were written before the code existed.
> 3. **Live's framework source is in the repo** at `Motion32/Resources/control_surface/` as `.pyc`.
>    Decompile with `xdis`. Read it *before* writing anything that touches the framework — three
>    separate load failures came from inventing an API instead of reading the one that exists.
> 4. **Run `python3 tests/test_screen.py` before and after every change.** 3999 assertions, no Live
>    and no hardware needed. It is load-bearing, not decorative — see §5.
>    **`pip install xdis` first** — without it the suite cannot read the framework `.pyc` and now
>    *fails* rather than quietly skipping its strongest guard (§5).
> 5. **Standing instruction from the user:** *whenever a bug is fixed or the script changes, and that
>    change has a callback to the documentation, the docs must be brought back in sync with how the
>    script actually behaves in the real Ableton Live environment.* Docs are part of the deliverable.

---

## 1. The goal (unchanged)

A **native Ableton Live 12 control-surface script** for the **Fender Motion 32** that makes the
controller feel as deeply integrated into Ableton as it is into Fender Studio Pro — full use of the
screen, encoders, pads, touch strips and LEDs. Not a generic MIDI map.

Native protocol on the **`Motion 32 Main`** port. The DAW-Mode Mackie profile on the `Motion 32
Control` port is a commodity fallback and is deliberately unused; DAW Mode stays **Off**.

### Guiding principles

1. **WHAT vs HOW.** *What* the Motion should do comes from the device's own capabilities and the RE
   docs. *How* to implement it comes from `ableton.v3.control_surface`. Never let either dictate the
   other.
2. **Factory-first, then exceed it.** Faithful parity first; then push into Motion-only territory.
3. **Don't be captive to the Atom SQ.** It is a precursor, not a target. The Motion is richer
   (4-template/181-element screen, 8 soft buttons, encoder halos, 32 pads, 2 touch strips).
4. **Respect the device's local engines — but know which ones actually run in native mode.**
   Global Settings, Encoder Curve, Pressure and the stand-alone scene are the device's. **Scale and
   Chord are not.** ⚠️ *Corrected 2026-07-25:* this principle used to read "note *generation* runs
   on-device; don't reimplement the musical engine." That is false for native mode — Studio One
   generates the notes, and the pads only ever send a fixed note per pad (36–67). Reimplementing the
   musical engine is exactly what a native client does. See
   `Motion32_Scale_and_Chord_Engine.md`.
5. **The device is host-rendered.** It sends control events and renders whatever we push. We own the
   state model, screen content and feedback — cache it and redraw coherently.

---

## 2. Where the code is and what each module does

`~/Music/Ableton/User Library/Remote Scripts/Motion32/` — **26 modules, 9.3k lines** (6.4k excluding
blanks and comments; this project deliberately carries its reasoning in the source, so the two counts
are far apart), plus an **8.5k-line** test suite.

| Module | Responsibility |
|---|---|
| `__init__.py` | `ControlSurface` + `Specification`, handshake, redraw lifecycle, teardown, and the `setup()` late-binding order |
| `midi.py` | Every CC/note/status constant, plus the teardown reset values |
| `protocol.py` | SysEx framing, identity-reply parsing, the Global-Settings suspend gate |
| `pads.py` | The Keys layout — which pad is which key, and the four that are not keys at all |
| `keyboard.py` | The pads as a playable keyboard: note translation, Octave ±, and the A–H bank radio. **Single source of the layout** — it reports the pad roles the LEDs are painted from |
| `elements.py` | Physical controls — **including `MotionEncoderElement`, which is why the halos work** |
| `mappings.py` | `create_mappings`: global bindings + the `Main_Modes` radio + per-mode layers |
| `palette.py` | The single colour conversion layer — `rgb7`, `live_rgb7`, `text_on`, `dim`. Screen and LED colour both come from here so they cannot drift |
| `colors.py` | `ComplexColor` construction (RGB parts + state byte) and the named `Rgb` palette, memoised |
| `skin.py` | Skin entries per framework component (framework `BasicColors` render colourless here) |
| `screen.py` | Named screen addresses per template + the factory palette |
| `formatting.py` | `compactify` (ported from Fender's JS) + per-element character budgets |
| `display.py` | `ScreenModel` (desired/sent diff, suspend, invalidate), `MainView` (T0), `MixerView` (T2), `ParamsView` (T3) |
| `notification.py` | The transient title/value bar on Template 1 — a third view that outranks both modes for ~1 s |
| `screen_component.py` | The content source — decides *what* is on screen and when it changes |
| `parameters.py` | Resolves which 8 parameters the encoders are actually wired to |
| `leds.py` | The same desired/sent diff for LED addresses |
| `wheel.py` | The big wheel's push: next device with wraparound |
| `sends.py` | Mix mode's **Sends** page — the (track × send) encoder grid and its derived page count |
| `scales.py` | The **15-scale table** and both Scale layouts. Framework-free, so the suite executes it |
| `scalemode.py` | Scale mode's state, soft buttons and wheel; plus the **Control** button that returns to the previous mode |
| `menu.py` | The Template 1 **list view** — shared with the notification bar |
| `commands.py` | The **Shift pad overlay** — six edit commands on the bottom lane, plus the `Modifier_Background` subclass that reports Shift-down so the keybed can repaint |
| `mixpages.py` | The big wheel *turning* pages Mix mode between Volume and Pan. Ours because no framework component switches modes from an encoder |
| `transport.py` | Subclasses the framework `TransportComponent`; adds record, loop-toggle, back-to-arrangement |
| `runtime.py` | Owner-scoped module state so a reload can't have the old instance blank the new one's screen |
| `tests/test_screen.py` | The offline suite |

Docs live in `Motion32/Resources/` so the script folder is self-contained. **That is now the only
copy** — the separate `Motion 32 resources` project folder was from an earlier run and is retired
(2026-07-25). There is nothing left to mirror; edit `Motion32/Resources/` directly.

---

## 3. What works right now (verified on hardware)

| Area | State |
|---|---|
| Handshake | `hello_messages = (NATIVE_ON, IDENTITY_REQUEST)` + manual reply parse; firmware from fixed offsets 11/12/13 |
| Teardown | LEDs to state 0 + **white**, screen to empty/white/visible, then `8F 00 00` — matched to a shutdown capture |
| Transport | Play/Stop/Record/Tap with capture-accurate colours; Shift+Play/Stop/Record/Tap = Loop/Undo/Capture/Metronome |
| Modes | **Song** (T3), **Plugin** (T0), **Mix** (T2/T0) and **Scale** (T1), strict radio. **Control** returns from Scale to the previous mode. Only **Edit** is deliberately unbound |
| Screen | Cached diffed renderer; suspends during the device's Global Settings screen and fully redraws on close |
| Encoders | 8 relative (`LinearSignedBit`), Shift as fine modifier, capacitive touch reveals values |
| Halos | Purple in Song, **the owning track's colour in Plugin**, the eight track colours in Mix, white on touch, dark when unassigned |
| Wheel | Bank scroll in Plugin mode; click steps devices with wraparound; **turning pages Mix Volume/Pan**; halo lit in Plugin and Mix |
| Soft buttons | All 8 assignable **per mode**. Song uses 6; Plugin claims none yet |
| Song mode | Session/Arrangement header, selected-track bar, 8 named encoders incl. cue volume, Loop, Back-to-Arrangement, Solo/Mute on the focused track |
| Plugin mode | `Track \| Device` header, bank name on a grey strip, 8 device parameters, opens Live's Detail view, Preset Up/Down steps devices |
| **Pads** | Lit from the track's colour in the piano ("Keys") layout decoded from a capture — root pads tinted, keys white, the four gaps dark |
| **Keyboard** | Pads play an armed track through `PlayableComponent` note translation. **No Python in the pad→note path.** Held pads flash green from note-on to note-off |
| **Dead pads** | The four gaps are claimed on `DEAD_PAD_CHANNEL = 15`, so they are silent *and* cannot collide with a real pad's transposed pitch |
| **Octave ±** | ±3 octaves. Dim blue at rest, dim white when *that direction* is engaged, full while held — the factory's two-channel LED model |
| **Mix mode** | Template 2: 8 strips (number, name on the track colour, volume fader) off the **Mixer component** so the view follows the session ring. L/R pages the ring by 8; encoder cap-touch selects the strip so Solo/Mute follow it **and replaces its label with the volume while held**; halos take the 8 track colours; the LCD buttons are the 8 arm buttons; **level-banded meters at 10 Hz** (§7c) |
| **A–H banking** | Strict radio of eight resting on **E**, one **scale degree** per step (−4…+3) — the keybed slides by whole bottom-row pads, so the gaps move and the keybed redraws. Dim blue / dim white, exactly one lit. Announces `Root` / signed offset. Clamps the octave so no bottom-lane pad can leave MIDI |
| **Notification bar** | Generic `notify(title, value)` on Template 1 for 1 s, outranking both modes. Octave is the first caller |
| **Shift pads** | Hold Shift and the bottom lane is a 16-slot edit layer — Undo, Redo, Dup, Delete, Quant, Double; ten slots grey. Top lane dark and consumed. `ComboElement` priority means no pad both commands and plays |
| **Scale mode** | Template 1 list, wheel-scrolled; `Main`/`Modes`/`Key` categories and a single `Guide`/`Locked` toggle. Pads collapse to one lane of the scale (Locked) or stay chromatic with the scale lit (Guide). Writes root + scale back to Live |
| **Sends page** | The eight encoders as a (track × send) grid, paged from the set's own track and return counts. Halos wear the slot's track colour |
| **Wheel push** | Input-only at CC `0x78` — that address is touch-strip 2 LED 9 outbound, so it must never become writable |

**Not started:** **Edit** mode, the touch strips (Phase 9), **Chord** mode (Phase 11) and Session
mode. Their *elements* exist but are unbound on purpose — a mode button with no matching mode binds
a control the framework never created.

**Complete:** Mix mode (Volume / Pan / Sends / meters), the Shift pad overlay, and Scale mode.

---

## 4. The six things that will bite a new session

These each cost a failed load or a long debug. All are in `Motion32_Implementation_Notes.md` §4 and
§6b in full.

1. **`identity_response_id_bytes` does not work on this device.** The reply's id bytes are
   non-contiguous (`08 00 00 26`), the framework's match never fires, and the device sits in a
   *pre-native* half-state where the screen still works but transport emits `0x66-0x69` instead of
   `0x6F`. Working screen output is **not** proof of native mode — check the transport CCs. (§1)
2. **Unknown `Layer` control names fail silently.** No error, no log, no behaviour. `Device_Navigation`
   has `scroll_up_button`/`scroll_down_button`, *not* `prev_button`/`next_button`. This is why the
   test suite checks every mapping name against the real component classes. (§6b-6)
3. **Never pass `channel=` to a matrix helper.** `add_matrix` supplies it, so it's a duplicate and the
   whole script fails to load. The singular `add_encoder`/`add_button` *do* accept it. (§4)
4. **Never shadow a `Component` attribute.** `Component.__init__` assigns `self._song`, `self._parent`,
   `self.name`, `self._layer` and more. A read-only `_song` property fails the build outright. (§4)
5. **An encoder halo has no address of its own — it is the encoder's CC.** So framework element writes
   land on the light. `MotionEncoderElement` drops the element's outgoing writes so `leds.py` owns the
   address. **Do not replace this with timer-based re-asserting** — that was tried twice and is worse.
   (§6b-10)

6. **An unwritten screen element is not a blank one — it shows whatever the firmware shipped in it.**
   The notification bar's first hardware run drew the device's own `MenuItem0`…`MenuItem5`
   placeholders straight through it, from twelve Template 1 elements the renderer had not claimed.
   **Every view must claim every element on its template.** The suite derives that list from
   `Motion32_Screen_Template_Map.csv`, so it is checked rather than remembered. (§6b-25)

Two more worth knowing: `quantized_parameter_sensitivity = 1.0` on the Specification (the framework
default 0.1 is why enums took ten detents per step), and `application` is a *property*, not a method.

---

## 5. Why the tests matter here more than usual

`tests/test_screen.py` runs with no Live and no hardware by loading the framework-free modules under a
synthetic package and parsing the rest with `ast`. That second half is the important part: the modules
that *can't* be imported offline are still checked structurally.

It catches, offline, things that on hardware look like "nothing happened":

- every `(template, zone, element, attribute)` the renderer emits, against the 433 handlers in
  `Motion32_Screen_Template_Map.csv`;
- every `self.X` a component references, against what the class and framework actually provide;
- every mapping control name, against the real component classes (the silent-binding trap);
- control-handler arity, `@listens` signatures, matrix `channel=`, framework properties called as
  methods, reload ownership, teardown reset values, and the LED ownership wiring.

**`xdis` is a hard dependency of the suite, not an optional extra.** The guards above that resolve
names against the real framework read Live's `.pyc` through it. Without it installed the suite used to
drop 36 assertions — the *entire* `test_every_mapped_control_name_exists` body — and still print
"0 failures". The historical `prev_button`/`next_button` bug passed clean in that state. It now fails
and names every mapping it could not check. **A green run on a machine without `xdis` was the most
misleading output this project could produce; that is fixed, but it is worth knowing why.**

**Discipline that has paid off every time:** after adding a guard, reintroduce the bug and watch the
test fail. An assertion that has never failed hasn't been shown to test anything. The corollary,
learned the hard way here: **also check the guard still fails in a degraded environment.** A backstop
that counts sections *visited* rather than *validated* passes while testing nothing.

---

## 6. Reference library (this folder)

| Doc | What it gives the build |
|---|---|
| `Motion32_Implementation_Notes.md` | ⭐ **Hard-won hardware truth — wins over every other doc.** Handshake, identity offsets, LED model, framework traps, per-feature build notes (§6b-1…6b-12) |
| `Motion32_Build_Roadmap.md` | ⭐ Plan of record + working method. §2 is the current-state snapshot |
| `Motion32_Control_Surface_Definition.md` | ⭐ Authoritative control map, machine-extracted from the factory surface XML — every CC/note, LED/RGB address, and the direction-dependent address overlaps |
| `Motion32_Handshake_and_SysEx_Spec.md` | Wire protocol: handshake, control→MIDI map, encoder sign-bit, RGB/LED, screen SysEx, Shift layer (§2.2) |
| `Motion32_Screen_Template_Map.md` + `.csv` | Every template/zone/element — 181 addressable elements, 433 attribute handlers. The CSV is what the tests validate against |
| `Motion32_Screen_Style_Spec.md` | How the screen should look: character limits, the `compactify` algorithm, the full 7-bit palette |
| `Motion32_Native_Host_Architecture.md` | Host-side state model, redraw/commit lifecycle, ownership split |
| `Motion32_State_Trace_Table.md` | Per-state trace: attributes → device I/O → interpretation → screen/LED |
| `Motion32_ControlLink_and_User_Mode.md` | How encoders get assignments: Control-Link pages, Auto-Fill, the User command-page model |
| `Motion32_Pads_Banking_and_Strips.md` | ⭐ Pads, A–H banking (rests on `E`), Octave, and the touch strips — the reference for the next three phases |
| `Motion32_Scale_and_Chord_Engine.md` | ⭐ **Who generates the notes** (the host, not the firmware), the complete 15-scale table, and the Live design — including why Scale is free and Chord is not |
| `Motion32_Ableton_Script_Structure.md` | The original build blueprint. Largely superseded by the code — read the code first |
| `Motion32_Gap_Analysis.md` | What's proven vs. still needs a capture. §1b lists what recent captures closed |
| `Motion32_Chord_Mode_Implementation_Guide.md` | ⭐ Phase 11 plan of record: the 16-chain Rack, and **carrier-note selection** — 7 of 624 `Famous.chords` rows span >36 semitones, so lowest-note anchoring exceeds Live's Chord range |
| `Motion32_StudioPro_SendMidi_Handler_Inventory.md` | Every Studio Pro output handler, catalogued |
| `Motion32_Code_Audit_2026-07-27.md` | Per-file audit against the docs. Its High finding is **fixed**; its four Low cleanups are **still open** — see §7. Superseded as a snapshot by the 2026-08-03 pass recorded in §7 |
| `FirmwareAnalysis/` | Ghidra projects + 18 probe scripts. ⚠️ **Two imports, not interchangeable — see below.** Start with `NativeMode_USB_EventStream_Report.md`, then §6b-33 of the Implementation Notes for the 2026-07-30 conclusions; the rest are raw probe dumps |
| `AbletonLOM/references/*.md` | Ableton **Live Object Model** reference, 12 files, Live 12.3. Installed 2026-07-31 alongside the `ableton-lom` skill — see §6b below |
| `Motion32_Source_Inventory.md` | Provenance: every primary source, what was extracted, what's unmined (answer: nothing substantial) |
| `ATOMSQ.zip` | Atom SQ **factory** script — the *how* idiom reference |
| `CustomAtomSQ Plus.zip` | WIP third-party add-on — ideas only, not canon |

**Precedence when docs disagree:** `Motion32_Implementation_Notes.md` (real hardware) →
`Motion32/Resources/control_surface/` (Live's actual framework) →
`Motion32_Control_Surface_Definition.md` (machine-extracted) → everything else.

### 6b. Tooling a new instance should know it has

**The `ableton-lom` skill is installed** (added 2026-07-31, from
[mikecfisher/ableton-lom-skill](https://github.com/mikecfisher/ableton-lom-skill), MIT). Its
`SKILL.md` carries the LOM object hierarchy, property access modes, the main-thread rule and common
patterns; the twelve detailed per-object references are cloned into
**`Resources/AbletonLOM/references/`** — `song.md`, `track.md`, `clip.md`, `device.md`,
`specialized-devices.md`, `rack.md`, `session.md`, `views.md`, `browser.md`, `control-surface.md`,
`grooves-tuning.md`, `lom-coverage.md`.

> **Use it by `Read`ing the matching reference file, not from memory.** The LOM has many non-obvious
> access modes and observability flags, and a wrong guess produces a script that fails *silently*.
> If the directory is missing, re-clone it:
>
> ```
> git clone https://github.com/mikecfisher/ableton-lom-skill.git \
>   "$HOME/Music/Ableton/User Library/Remote Scripts/Motion32/Resources/AbletonLOM"
> ```
>
> ⚠️ Note the division of labour, because it is easy to reach for the wrong one: the LOM references
> describe **Live's object model** (what a Track or DeviceParameter exposes). They do **not** describe
> `ableton.v3.control_surface` — for framework mechanics (elements, layers, modes, forwarding,
> mapping) the `.pyc` in `Resources/control_surface/` and `Resources/v2/` is still the only source of
> truth, read with `xdis`.

**Firmware probes.** ⚠️ There are two Ghidra programs and they are **not** interchangeable:

| Project | Program | Notes |
|---|---|---|
| `Motion32Firmware` | `motion32_fw_payload_0x1000.bin` | **The one every documented address belongs to.** Image base 0, so a program address is also a raw file offset |
| `Motion32FirmwareFull` | `motionupgrade.bin` | Comparison only. Payload anchors resolve to garbage here |

Runners: `run_host_config_probe.sh` (both programs), `run_command_vocab_probe.sh` (both),
`run_emitter_probe.sh` (**payload only, deliberately**). Because the payload base is 0, many
questions are answerable with `python3` against the `.bin` directly and no Ghidra at all — that is
how the two-variant proof in §6b-33 was done.

---

## 7. Open items

> **This section is chronological within 2026-08-03**, and the ✅ entries are kept rather than
> deleted because the reasoning is the useful part.
>
> The session opened with an **audit** of all 21 modules as they then stood, against the framework
> `.pyc` and against these docs. Most of what it found was fixed the same day. Three features were
> then built — the Mix meters, the Shift pad overlay, Scale mode and the Sends page — taking the
> script to 26 modules.
>
> **Still open:** the `Loop End` label (below) and the strip-2 double bend (§8).

### ✅ Fixed 2026-08-03 (was Medium): missing skin keys — three namespaces the framework asks for

**How a missing skin key actually fails.** `Skin.__getitem__` in `skin.pyc`:

```python
if key not in self.colors:
    if key.lower().endswith(ON_SUFFIXES):   # ('enabled', 'on', 'pressed', 'selected')
        return BasicColors.ON
    return BasicColors.OFF
```

No raise, no log. A `BasicColors` is a state byte with **no RGB triple**, which renders colourless on
this device. And note the asymmetry, because it is what hid all three of these: the `On`/`Pressed`
half still lights (wearing whatever RGB the address last held), while its resting partner writes
state 0 and goes **dark**. The symptom reads as "this button only works while I hold it", which
nobody files as a bug.

| Skin key | Asked for by | Bound to | Was |
|---|---|---|---|
| `Session.Navigation` / `…Pressed` | `Session_Navigation` | Mix mode Left/Right | **dark for the whole of Phase 7** |
| `UndoRedo.Undo` / `…Pressed` | `Undo_Redo` | Shift+Stop | dark under Shift |
| `ModifierBackground.Shift` / `…Pressed` | `Modifier_Background` | Shift | dark at rest, colourless when held |

⚠️ **The Shift one is the instructive case.** `skin.py` had carried `class Modifier: On/Off` since
the first commit — a namespace **nothing in the framework ever asks for**. The real keys are built at
runtime from the component's own name:

```python
# ModifierBackgroundComponent._setup_control_state
base = self.name.title().replace("_", "")   # "Modifier_Background" -> "ModifierBackground"
ctrl = name.title().replace("_", "")        # "shift"              -> "Shift"
control_state.color         = "{}.{}".format(base, ctrl)
control_state.pressed_color = "{}.{}Pressed".format(base, ctrl)
```

So it cannot be found by grepping the framework for skin-key literals, which is how the other two
were found. `ScrollComponent`'s `"{}Pressed"` is the only other computed one. Both are written down
in `skin.py`'s module docstring.

**Corrected finding:** the audit also listed `Mixer.ImplicitArmOn` as missing. **It is not a bug.**
It is wrapped in an `OptionalSkinEntry(name=…, fallback_name='Mixer.ArmOn')` and
`Skin._from_wrapper` follows the fallback when the preferred name is undeclared — so an implicitly
armed track already gets our red. It is now on `SKIN_KEYS_DELIBERATELY_ABSENT` in the suite, with a
guard that fails if anyone *does* declare it.

**The guards.** Two, because neither is sufficient alone:

- `test_every_skin_namespace_a_bound_component_uses_is_declared` — fully **derived** from
  `create_mappings()` plus the skin-key literals in each bound component's `.pyc`, so it needs no
  maintenance and catches the next forgotten namespace on its own.
- `test_bound_controls_have_a_real_skin_colour` — an explicit `REQUIRED_SKIN_KEYS` table pinning the
  exact keys per mapped control, because **nothing in the bytecode links a control name to its skin
  keys**. Kept honest from both ends: a row naming a control we no longer map fails too.
- `test_the_shift_skin_key_is_the_computed_one` recomputes the derivation rather than hardcoding
  its answer.

Verified by deleting `class Session` (5 failures) and by renaming `ModifierBackground` back to
`Modifier` (6 failures).

### ✅ Done 2026-08-03 (Phase 7c): Mix-mode meters — **confirmed on hardware**

The last deferred piece of Mix mode, built on the `[CAP 2026-07-31]` capture. Full design in
`Motion32_Build_Roadmap.md` §7c; what a new session needs to know:

**It is the only polled thing in this script, and that is the interesting part.** Every other fact
on screen has an event, on the rule that produced three stale-screen bugs when it was broken. Meters
are the exception for the *opposite* of the usual reason — `output_meter_left` **is** observable, but
it fires far faster than any rate the screen can use, so a listener would flood the diff to produce
a picture no better than 10 Hz gives.

- `task.loop(task.wait(METER_INTERVAL), task.run(self._poll_meters))` — the framework's own
  repeating idiom, deliberately **not** the self-rescheduling chain `_schedule_live_refresh` uses. A
  chain that misses one hop simply ends, which for a 0.75 s timeout is fine and for a meter loop
  means a bar frozen for the rest of the session.
- Gated on **Mix mode AND the Volume page** — the Pan page draws Template 0, which has no meter
  element at all. `_poll_meters` re-checks the gate because a page change can race a frame.
- `_poll_meters` just calls `_render()`. Routing meters through the ordinary path means they are
  diffed, suspended during Global Settings, and address-validated like every other element; a
  private write path would have to reimplement all four.
- Killed in `disconnect()` with `_kill_task`, **not** `_stop_meters` — the latter renders, and
  rendering during teardown is how a superseded instance writes to a device it no longer owns.

**Two design decisions worth not re-litigating:**

1. **Banded colour, not a gradient.** A screen element takes one colour and one value, so a
   continuously varying colour must be re-sent every frame — 16 extra messages per frame, doubling
   meter traffic from the factory's 160/s to 320/s. Quantised to three bands, the colour only becomes
   a *different* payload at a crossing, so the diff drops it on nearly every frame.
   `test_a_steady_meter_costs_nothing_between_band_crossings` pins this.
   ⚠️ **A screen colour is one SysEx with an R G B payload, not three messages** — that is the LED
   model. Conflating them put the first version of this estimate out by a factor of three.
2. **No ballistics code, anywhere.** Live's `output_meter_left`/`_right` are already smoothed; the
   capture shows Studio Pro's host decaying a meter for six seconds after a note-off while the device
   just renders numbers. If a bar ever snaps to zero instead of falling, we are reading the wrong
   property — not missing a decay implementation.

**What the hardware run settled (2026-08-03):**

- ✅ **The colour attribute paints the bar, not the trough.** This was the real risk and the map
  could not answer it: `METER_LEFT_BACKGROUND` is the only `_BACKGROUND` among all 181 elements that
  shares an element with a `value`, and everywhere else that suffix means a fill *behind* the
  content. Had it been the trough, the banding would have coloured the empty space above the signal
  — an inverted meter, worse than no colour at all.
- ✅ **0.0–1.0 maps onto the bar as expected**, and the bands change where Live's own meters do. The
  inferred thresholds stand unmodified.
- ⚠️ **Still unanswered:** do meters keep updating with Live in the background? If they freeze
  mid-decay on an app switch they need a zeroing path. Not seen either way yet.

**A deliberate divergence from the factory, recorded because it will look like an oversight.**
Studio Pro colours each meter with its **track's fill colour**; we colour by signal level. The track
is already identified three other ways on this screen — the name swatch, the encoder halo and the
selection blue — so spending the meter's colour on identity as well would say nothing new, whereas
level is information the screen carries nowhere else. `meter_colour()` is one function if it ever
reads better the factory way.

### ✅ Added 2026-08-03: the Volume page reveals the level on the strip label

Touching an encoder in Mix mode already selected the strip (the focus model). It now **also replaces
that strip's track name with its volume** (`-6.0 dB`) for as long as the touch lasts, and the name
returns **the instant you let go**.

⚠️ **No timeout, and that is the point.** Plugin mode and the Pan page both revert after the
framework's `ACTIVE_PARAMETER_TIMEOUT` (0.75 s), because there the value is uncovered by a touch that
may never be followed by a turn and needs a moment to be read. On the Volume page the fader is on
screen permanently, so the number is a precision aid while your finger is down; holding it after
release would hide the track name for nothing. **The distinction is per page, not per mode** — the
same lesson that made the Pan page silent on touch when it was got wrong the other way round.

🔑 **`MixerStrip.show_value` is derived from `_touch_held`, not stored.** "Is the finger down" is
exactly the question the reveal asks, so there is no flag to clear and no timeout to miss — which is
what makes "no timeout" safe rather than merely untested. It deliberately does **not** reuse
`_showing_value`, which carries the 0.75 s revert: that is the roadmap's standing warning about one
event source with two opposite meanings, and it is the third time that warning has earned its place.
The *focus* is still the track selection and still persists, untouched by any of this.

The value goes through `truncate_value()`, never `compactify()` — compactify strips hyphens and
would render every attenuation on the mixer as a boost.

🐛 **Fixed the same day, from hardware: the mixer dropped `dB` on every level below -10.**
`truncate_value` shortened by keeping only the leading token, so at the label's 8-character budget
`-6.00 dB` (8) survived intact while `-12.00 dB` (9) became `-12.00`. A column where the unit comes
and goes with the value reads as a bug, and `-70.00` alone is ambiguous. It now tightens in the
order a person would — spare decimals, then the space, then more decimals, and only then the unit:

    -12.00 dB  -> -12.00dB      -12.345 dB -> -12.35dB
    -100.00 dB -> -100.0dB      -6.00 dB   -> -6.00 dB  (fits, untouched)

⚠️ **Capping the decimals would not have fixed it**, which is the trap worth recording: Live already
sends two, so `-12.00 dB` is over by exactly the space. The obvious fix passes a naive test and
ships the bug — `test_a_value_keeps_its_unit_before_it_keeps_its_precision` fails on it deliberately.
The change applies to the Plugin and Pan tiles too (7 chars), where it is a strict improvement:
`-6.00 dB` was `-6.00`, and is now `-6.00dB`.

**New guard vocabulary.** `MIXER_STRIP_LISTENERS` in the suite now carries **four** freshness
contracts, and they are not interchangeable:

| Classification | Means | Obligation it carries |
|---|---|---|
| a listener name | Live tells us | the listener is really subscribed in `_rebind_mixer_strips` |
| `None` | cannot change | none |
| `POLLED` | a timer re-reads it | the loop exists, is gated, and is killed on teardown |
| `CONTROL_DRIVEN` | our own handler changes it | **every** handler that mutates it repaints in the same breath |

The last one is the newest and the most easily got wrong: a touch handler that updates state and
forgets to render leaves the screen permanently a frame behind the hardware, which is the
stale-screen bug wearing a different hat. Collapsing any of these into `None` would let a genuinely
event-driven field through unguarded.

### ✅ Built 2026-08-03 (Phase 8): the Shift pad overlay — **confirmed on hardware 2026-08-08**

> **The confirmation was incidental.** It appears inside a capture taken to settle a touch-strip
> question, which is the useful part: nobody was testing the overlay, so nothing was staged for it.
> On `CC 31 = 127` the script paints `C1`–`F1` (the six commands — already-correct colours diffed
> out, exactly as the renderer should), ten grey pads at `F#1`–`D#2` velocity 93/95/97, and Note Offs
> across `E2`–`G3` taking the top lane dark. On `CC 31 = 0` it restores. Six commands, ten grey, dead
> top lane — the design as specified.

Hold Shift and the bottom lane becomes a 16-slot edit layer; the top lane goes dark and silent.
`commands.py` (the 22nd module). Six slots filled: **Undo, Redo, Dup, Delete, Quant, Double.**

**Why six and not sixteen — now settled rather than suspected.** A grep for `split`, `consolidate`,
`join`, `freeze` and `flatten` across all twelve LOM reference files finds **nothing**, so the
roadmap's long-standing flag on Split and Merge/Consolidate is confirmed: they are not expressible.
Insert Pattern / New Variation / Duplicate Variation are Studio One concepts Live has no equivalent
of. Copy and Paste are *deferred, not impossible* — `ClipboardComponent` works by holding Copy and
tapping a **source** object then a **destination**, so it needs a clip grid to point at and arrives
with Session mode.

🔑 **The mechanism, and it is the framework's rather than ours.** `add_modified_control` accepts a
**matrix** (it detects `ButtonMatrixElement` and routes to `_add_modified_matrix`), publishing both
`pads_with_shift` and `pads_with_shift_raw[i]`. `ComboElement` then carries
`priority_increment = 0.5`, so a **bound** Shift-modified pad outranks the keyboard binding and takes
the press — the pad fires its command and plays no note. No mode set, no layer juggling.

⚠️ **An UNBOUND modified element claims nothing.** Priority is asserted by being in a live layer, so
leaving the top lane alone would have left the accidentals sounding under Shift — half a keybed of
notes and half of destructive edits. It is bound to a `BackgroundComponent` (a `NopControl` grab)
purely to be consumed. **On this surface "unbound" and "silent" are opposites**, which is the same
lesson the four dead keyboard pads taught: an identifier ≥ 128 *released* them and let their raw
notes loose.

⚠️ **`Clip_Actions` is deliberately NOT bound to the pads.** The framework component implements four
of these six properly, with availability LEDs, and on any other controller it would be the right
answer. Here it would take **LED ownership of four pad addresses** — a pad's LED address *is* its
note address — leaving twenty-eight pads with `PadLeds` and four with the framework. That split is
the two-writer bug that cost three attempts on the encoder halos. The actions are three LOM lines
each; the ownership is the part that matters.

**Shift-down is observed, not owned.** `MotionModifierComponent` subclasses
`ModifierBackgroundComponent` (not plain `BackgroundComponent` — the modifier subclass is the one
that builds the computed `ModifierBackground.Shift` keys) and hooks `_set_element_for_control` to
attach a *value listener* to the shift element. Binding a second `ButtonControl` would put two
layers on one element; observing the element does not.

**Unassigned slots are grey, not dark** — the factory's "present but unassigned" convention. With
ten of sixteen empty, darkening them would make the layer look broken. Pressing one still answers on
the notification bar, by the same rule that makes A–H announce a press that changes nothing.

### ✅ Built 2026-08-03 (Phase 10): Scale mode

A fourth mode on the Scale button (CC `0x21`), with the factory's own screen: header title
`Scales`, a single **`Guide`/`Locked`** toggle top-right, a 2×6 list scrolled by the wheel, and
`Main | Modes | ⬚ | Key` on the bottom row. The soft-button designation is the factory's, from
`Motion32_State_Trace_Table.md` §Scale (`[SRC]`): *"wheel selects scale/key; soft buttons pick
Main/Modes/Key + Guide/Lock"*.

**Three modules.** `scales.py` is the framework-free engine — the 15-scale table and both layouts,
executed rather than parsed by the suite. `menu.py` is the Template 1 list view. `scalemode.py` is
the state, the soft buttons and the wheel.

**`Guide` and `Locked` are one control, two states** (user decision — the factory names them and
defines them nowhere):

* **`Locked`, the default** — one row. Sixteen consecutive ascending scale degrees on the bottom
  lane, top lane entirely dead, which is what the factory does (§5.3c). Only scale notes reachable.
* **`Guide`** — both rows, the ordinary piano, with in-scale notes at full brightness and everything
  else dimmed. **A lighting change, not a layout change**: it returns the *unchanged*
  `pads.pad_pitches()`, so note translation, dead pads and held-pad feedback need no second path.

🔑 **The one-lane collapse is what makes duplicate pitches impossible.** Verified exhaustively:
15 scales × 12 roots × 7 octaves × 8 bank positions, **0 violations**, strictly ascending
throughout. The measured spans also match §5.3c's own figures exactly — Major 26 semitones,
pentatonics 36, triads 60 — which is independent confirmation that doc and generator agree.

**Two deliberate divergences from the factory, both the user's call:**

- **Chromatic is not a menu entry.** Leaving Scale mode *is* selecting chromatic, and the standard
  pad layout already is one.
- **The triads are not scales.** `Major Triad` is `(0, 4, 7)`; across sixteen pads that spans 60
  semitones — a chord voicing table. The firmware agrees about where they belong: `Triad`, `Sus2`,
  `Sus4` and `Add 7` sit in the *chord* string block. They stay in `SCALES` for Phase 11 to read.

⚠️ So the menu is **7 Main + 7 Modes = 14**, where the factory shows 16 (its 14 non-chromatic scales
plus the Ionian/Aeolian aliases, triads included). An earlier note in `scales.py` claimed 9 + 7 = 16
"matches the factory" — true only while the triads were listed as scales, and no longer the reason
to trust the split.

**The Control button returns, and is not a mode button.** Adding it to the `Main_Modes` radio would
make it a fourth *destination*; it has no screen of its own. The factory agrees — §Control describes
`kControl0` as *"the neutral 'return to underlying control-focus view' state that scale/chord/
launcher/velocity collapse to"*. It holds one value, not a stack.

**Writing back to Live.** `song.root_note` and `song.scale_name` are both R/W and observable, so the
Motion pushes its selection and Live's own scale awareness follows. ⚠️ `scale_name` takes **Live's**
vocabulary — our `Natural Minor` is Live's `Minor` — and an unrecognised name is *silently ignored*,
the same failure class as an unknown Layer control name. `scales.LIVE_SCALE_NAMES` is the explicit
map; a scale absent from it (the triads) is deliberately not pushed at all.

**Three hardware bugs, all fixed** — see §6b-35 and §6b-36 for the mechanisms:

1. `screen_component._keyboard` was declared and never assigned, so `_push_scale_layout` returned
   silently and the pads never re-laid. The LEDs still redrew, which is what made it look like it
   worked.
2. A **frozen** pitch list meant A–H banking moved the offsets and the pitches did not follow.
3. Returning from the notification bar left the menu's rows invisible — two views on one template.

### ✅ Built 2026-08-03 (Phase 7d): Mix mode's Sends page

The eight encoders as a **(track × send) grid** — columns are tracks, rows are sends, so encoder 1
and encoder 5 are send A and B of the same track and a column sits where its strip does on the
Volume page.

🔑 **The page count is derived from the set and no encoder is ever dead.** Sends are taken in pairs
(the two physical rows) with a leftover odd send given its own page of one row × eight tracks.
8 tracks with 2 returns is two pages; 3 returns is **three**, not four.

⚠️ The obvious arithmetic — `2 × ceil(S/2)` pages of four tracks — leaves the bottom row unmapped on
the last two pages of every *odd* send count: eight dead encoders in an ordinary three-return set.
Caught before hardware, and `page_table` / `page_slots` live at module level precisely so the suite
can **execute** the rule rather than restate it (§6b-37).

**Why not `MixerComponent.set_send_controls`.** It genuinely takes a 2D matrix indexed
`[strip, send]` — this exact shape — and drives `SendIndexControlComponent` to page send banks. What
it cannot do is page **tracks**: it maps `controls[x]` onto `_channel_strips[x]`, so a four-wide
matrix reaches strips 0-3 and leaves half the ring unreachable. The *mapping* is still the
framework's (`MappedControl.mapped_parameter`, engine-side, no Python in the value path); only the
choice of which parameter goes on which encoder is ours.

**One mode, several wheel steps.** A `ModesComponent`'s mode list is fixed at mapping time and the
page count is a fact about the user's set, so `mixpages.py` expands the single `sends` mode into as
many steps as the set needs. Declaring `sends_1..8` and hiding the empties would bake a guess about
set size into the mapping table and still be wrong for the ninth.

⚠️ **Three hardware bugs, all from one root** — this component maps parameters itself, and
inherited three duties the framework had been discharging silently for Volume and Pan. Written up
as **§6b-34**, which is the most transferable lesson of the session.

### ⚠️ Open (Medium, 2026-08-03): Song encoder 4 says `Loop End` and shows a length as a position

`mappings.SONG_ENCODERS` binds `loop_length_encoder` and labels it **`Loop End`**, and
`screen_component._song_encoder_readout` renders it as
`_format_beats(song, float(song.loop_length))` — i.e. it runs a *duration* through the bars.beats
formatter, which adds 1 to both the bar and the beat because it assumes an absolute position. A
2-bar loop starting at bar 3 therefore reads `3.1`, which is neither the loop end (bar 5) nor the
length (2 bars).

**Fix:** decide which the encoder should mean, then make label, control and formatter agree. Either
relabel to `Loop Len` and format the length as a duration, or keep the label and show
`loop_start + loop_length`. Not both halves independently — the failure here is exactly the §6b-16
shape of computing an agreement twice.

### ✅ Fixed 2026-08-03 (was Medium): `setup()` bound fourteen things inside one `try`

A failure in the first call silently skipped the other thirteen — the mixer, the ring, the page set,
all three LED groups, the keyboard's three listeners and the mode follow — behind one
`logger.exception` that named none of them. The presenting symptom would have been "the screen works
and nothing else does".

Now `Motion32._bind_screen_sources()`, a table of `(name, callable)` with a guard per entry: a
failure logs which binding was lost, the rest still run, and a summary line names them all. A table
rather than fourteen `try` blocks, because adding a binding should not be an opportunity to forget
the guard. Order is still load-bearing and the table preserves it — `bind_parameter_source` first,
`bind_modes` last (it triggers the first real render).

### ✅ Fixed 2026-08-03 (was Low): guards that swallowed the thing they were written to survive

Absorbing an exception so a Live callback cannot wedge the surface is right. Absorbing it *silently*
was not.

- **`parameters.ParameterSource.entries()`** now calls `_note_read_failure()` — a rate-limited log
  line (3 then quiet) naming the failure and saying that an `IndexError` here is the known Max for
  Live / `banking_util` bug rather than ours. Same for `bank_label()` and `device()`. Before this,
  that crash presented as all eight Plugin tiles going blank with **nothing** in `Log.txt`.
- **`transport._set_color()`** logs once per skin name. It was `except Exception: pass`, which is
  precisely what would have hidden the missing `Session.Navigation` keys above.
- **`transport.back_to_arrangement_button`** logs instead of passing.
- **`leds.LedGroup.set()`** now **raises** on an out-of-range index. That is a caller bug — a
  mismatch between the group's address list and whatever iterates it — and silently returning would
  turn "the 33rd pad never lights" into no symptom at all.

Still deliberately quiet: `_kill_task`, `_clear_mixer_listeners`, `_clear_track_listeners`,
`_stop_live_refresh`. These run during teardown against objects Live may already have destroyed, so
a failure there is expected rather than diagnostic.

### ✅ Fixed 2026-08-03 (was Low): teardown wrote every halo, the wheel and all 32 pads twice

`disconnect()` called `release()` on the three LED groups **and** `_clear_all_leds()`, whose address
list (`midi.LED_ADDRESSES_TO_CLEAR` + `PAD_NOTES`) already covers every one of them. Total overlap:
~196 redundant messages per unload, and it made `leds.py`'s "byte-identical to Studio Pro's" claim
false by a factor of two on those 41 addresses.

`release()` is now split into `release()` (transmit) and **`forget()`** (drop both maps, send
nothing), and `disconnect()` calls the latter. The guard is a *count*: a current teardown must emit
exactly `4×len(LED_ADDRESSES_TO_CLEAR) + 5×len(PAD_NOTES) + 1` messages. Nothing else catches this —
every individual message was correct.

### ✅ Fixed 2026-08-03 (was Low): `MixerView` was missing from `full_redraw()`'s forget list

There is now **one roster**, `runtime.views()`, and `full_redraw()` iterates it. The hand-written
tuple at the call site had never been updated when Mix mode landed, and got away with it only
because `invalidate()` clears `_sent` and leaves `_desired` intact. Same shape as the earlier LED
bug where a new group went into one named list and not the other and the keybed stayed dark after
connect — hence a roster rather than a fourth entry.

`test_every_view_is_on_the_roster_and_full_redraw_walks_it` checks both halves: every `_*_view`
global in `runtime.py` must appear in `views()`, **and** `full_redraw` must call `runtime.views()`
rather than growing a second list beside it.

### Dead code — mostly removed 2026-08-03, with one instructive exception

Removed: `screen_component._render_listener` · `formatting.MAXCHARS_PARAMS_VALUE` · unused imports
(`colors`: `dim`; `screen_component`: `EMPTY_TILE`) · `parameters.bank_index`.

⚠️ **`colors.color_from_live` / `color_from_rgb7` / `_dynamic_cache` were listed as dead and are
not.** Deleting them failed `test_framework_colours_are_built_from_the_shared_layer`, which requires
all three plus the `rgb7` import. That guard is deliberate: the pair is the *skin*-side equivalent of
`palette.live_rgb7`, for the first framework-owned control that has to wear a track or clip colour
(Session mode's clip pads), and the `rgb7` import **is** the assertion that this module takes its
conversion from `palette` rather than defining one. All restored, with the reasoning now in the
source so the next audit does not repeat the mistake. Recording this because "the suite caught the
audit" is the outcome the suite exists for.

Still open, low value: `screen_component._mixer_strip()` duplicates `_strip_track()` ·
`_song_encoder_readout` computes a `_fill` that Template 3 cannot display and throws it away ·
`screen_component.MAXCHARS_CENTRE` duplicates `display.MAXCHARS_CENTRE_TEXT`, both 24.

### ✅ Confirmed 2026-08-08: three captures, one correction, one new wire fact

Two experiments on hardware, neither of which changed the script.

**1. Live's factory Atom SQ script loaded against the Motion.** It emits PreSonus SysEx
(`F0 00 01 06 22 …`); the Motion speaks Fender (`F0 08 26 …`). Every message was discarded — no
screen response, no error. Two useful negatives: there is no latent Atom-SQ display compatibility,
and a foreign script cannot leave the device in a state we must defend against. The same run
re-captured the **stand-alone** strip behaviour (device-generated Mod/Expression/Breath, self-
centring pitch bend) from a different host, confirming §5.1b's three-state model from a second angle.

**2. Our script, strips touched with and without Shift.** Reproduces the 2026-07-30 capture exactly:
contact sensor down, **pitch bend only**, contact sensor up, no centre value, Shift changing nothing.
§5.1b needed no correction — see §6b-38 on how that re-derivation happened and how to avoid it.

**New, and the reason the run was worth it:** every strip value is a **multiple of 16**, so the
14-bit pitch-bend field carries **1024 steps, not 16384**. The firmware disassembly had independently
found a 10-bit ADC (§6b-33). Wire and bytecode agree; "14-bit", stated in five places, has been
corrected everywhere to distinguish the message width from the signal width.

**Incidental bonus:** the same capture contains the **Shift pad overlay working on hardware**, which
had been listed as an outstanding gate. Nobody was testing it, so nothing was staged for it.

### ⚠️ Open (Medium, 2026-07-31): strip 2 double-bends the armed instrument

The only known defect in shipped behaviour. The touch strips are undeclared — `elements.py` and
`mappings.py` contain no touch-strip element — so strip 2's **channel-1 pitch bend** passes straight
through to the armed track and fights strip 1's channel-0 bend. Two pitch benders on one instrument.

Not a regression; it has been true since native mode started working, and it was recorded as
"leaving strip 2 alone is worse than binding it" before the cause was understood.

**Fix — and it is now a fork, not a single answer** (decided 2026-08-08):

- **If strip 2 becomes a Live parameter:** declare it as a `MIDI_PB_TYPE` element on channel 1 with
  `ScriptForwarding.exclusive`. Consumption is decided purely by the forwarding type, so that alone
  stops the leak, independently of what it is later pointed at. Strip 1 must stay `non_consuming` or
  its working pitch bend breaks.
- **If strip 2 becomes a real mod wheel** — the user's stated preference — it must stay
  **un-consumed**, because the Max for Live converter can only convert what reaches it. The
  `[midiselect]` → `[ctlout]` device then swallows the channel-1 bend, emits CC 1, and passes
  channel 0 through, which fixes the double bend *at the instrument* rather than at the script. The
  defect then persists only on tracks without the device.

⚠️ **So this entry can be closed two ways, and one of them is not by writing script code.** Full
decision, candidate devices and the rejected conditional variant in
`Motion32_Pads_Banking_and_Strips.md` §5.1b; the wire model is §5.1b/§5.1c.

### ✅ Fixed 2026-07-29 (was High): a superseded instance sent the native-mode goodbye

**The bug.** `ControlSurface.disconnect()` calls `_send_specification_messages`, which reads
`specification.goodbye_messages` and calls **`self._send_midi` directly** — bypassing
`MotionProtocol`, `ScreenModel` and `LedGroup` entirely. `__init__.py` detected supersession
(`still_current = runtime.clear(self)`) and suspended our own writers, but suspending never touched
that path. So on a script reload the order was:

```
new instance sends 8F 00 7F  ->  old instance disconnects  ->  old instance sends 8F 00 00
```

…and **the device dropped out of native mode while the new instance believed it was in** — exactly
the pre-native half-state in §4 item 1: screen and LEDs still work, transport arrives on `0x66`-`0x69`
instead of `0x6F`. Intermittent, and only after a reload.

**The fix.** `Motion32` now overrides **`_send_midi`** itself and drops every outgoing message while
`self._midi_muted` is set; the superseded branch of `disconnect()` sets that flag before calling
`super().disconnect()`. Muting the transmitter rather than neutralising `goodbye_messages` is
deliberate — it is the only point that catches *every* path out of a superseded instance, including
element resets and any framework write not enumerated here. The flag is initialised at the very top
of `__init__` because the override is consulted during `super().__init__()`. The log line in that
branch no longer claims "no goodbye side effects"; it says the output is muted.

**The guard.** `test_a_superseded_teardown_emits_zero_bytes` lifts the three teardown methods out of
`__init__.py` by AST and re-compiles them as a class body (so the zero-argument `super()` gets its
`__class__` cell) against a base that reproduces the framework's goodbye path as it appears in
`control_surface.pyc`. It asserts the sent list is **empty** — not merely that the reset calls were
skipped, which is all the older `test_teardown_is_skipped_when_superseded` could see. It opens with a
positive control: a *current* instance must still emit `8F 00 00`, otherwise "zero bytes" would pass
vacuously. Verified by reintroducing both failure modes — removing the flag assignment (2 failures)
and neutering the override while leaving the flag (1 failure).

**Confirmed on hardware 2026-07-29**: after a reload, transport arrives on `0x6F`.

### ✅ Closed 2026-07-29: the A–H root shift does reach the notes

Confirmed on hardware. `PlayableComponent`'s plain `button.identifier = …` assignment *does* get
Live's MIDI map rebuilt, so no `request_rebuild_midi_map()` call is needed. Recorded because the
opposite was suspected for an afternoon, and because it also settles the same question for Octave ±,
which shares `_recompute`.

The layout log line in `_recompute` stays — it is what made this answerable, and it will answer the
same question again for the Scale layouts.

**Still worth doing:** vendor `ableton/v2/control_surface/` into `Resources/` alongside v3. It was
not needed in the end, but the only reason this took a hardware round-trip is that the relevant
setter could not be read. §6c's rule keeps earning its place.

### Lower-priority cleanups from the 2026-07-27 audit — **all four re-confirmed open 2026-08-03**

- `screen_component.py`: `_render_listener()` is unused; one duplicated colour-listener comment.
  *(The comment was fixed 2026-08-03; the unused helper remains.)*
- `colors.py`: imports `dim` and `rgb7` but uses only `live_rgb7`.
- `formatting.py`: `MAXCHARS_PARAMS_VALUE` is not on the active rendering path.
- `protocol.py`: `parse_identity_reply()` accepts any Universal Identity Reply without checking the
  Fender manufacturer/device IDs. Probably fine on a Motion-only port.

### Not blocking anything

The **pad musical-note capture** used to be the one blocker. It is **closed by source** — in native
mode the pads always send a fixed note per pad (lane 0 = 36–51, lane 1 = 52–67) and every musical
transform is host-side. Evidence in `Motion32_Scale_and_Chord_Engine.md` §2, and the piano layout has
since been confirmed working on hardware.

### Designed but not built, in rough order of readiness

- **Browser navigation on the wheel** — needs a Template 1 `MenuView` (2×6 list). ⚠️ It will share
  Template 1 with the notification bar; ownership has to be settled before both write it.
- **Top soft-button row labels** on Templates 0 and 3, and view-dependent nav LEDs.
- **Encoder acceleration** — still uncaptured, now curiosity rather than blocker (the "ten detents
  per step" complaint was the sensitivity default).

### Parked on purpose — Scale (Phase 10) and Chord (Phase 11)

Researched and designed; sequenced last by decision, not by blocker.

The factory pad layouts are **settled**: in both modes the **top lane is entirely dead**. Scale
collapses its pitches onto the bottom lane with tonics tinted — which makes duplicate pitches
impossible by construction, verified across all 15 scales × roots -3…+3 × octaves -2…+2. Chord splits
the bottom lane into **4 groups of 4** — four chords, four voicings each — which is exactly the shape
of `Famous.chords`.

`Motion32_Chord_Mode_Implementation_Guide.md` is the Phase 11 plan of record. Its most important
finding: **do not anchor chords on the lowest note.** 7 of 624 `Famous.chords` rows span more than 36
semitones, exceeding Live's Chord-device shift range, so the compiler must *choose* a carrier note.
Every row has at least one workable carrier. `Simple.chords` never triggers it (widest span 28), so
testing only against Simple would hide the bug entirely.

**The one thing to carry forward even if nothing else is read: no Python in the pad→note path.**

### A known crash that is not ours

`banking_util._get_parameters_for_bank_index` raises `IndexError` for Max for Live devices that
declare bank indices beyond their own parameter list. Entirely framework code; it surfaces more often
now that Left/Right appoints devices.

⚠️ **It reaches us through `ParameterSource.entries()`, which swallows it silently** — see §7. On
hardware the crash presents as all eight Plugin tiles going blank with nothing in `Log.txt`. The
framework bug is not ours to fix; the silence is.

---

## 8. First actions in a new session

1. Read this file, then `Motion32_Implementation_Notes.md` §4 (framework traps) and §6b (per-feature
   build notes). Skim `README.md` in the script folder for the behaviour contract.
2. `pip install xdis`, then run `python3 tests/test_screen.py`. Expect **169 test groups, 3999
   assertions, 0 failures** and a closing `PASSED` line. If it fails, fix that before anything else. A lower assertion count
   means guards did not run — see §5.
3. For any framework question, decompile the relevant `.pyc` from
   `Motion32/Resources/control_surface/` — before writing code, not after it fails.
   For any **Live object model** question (what a Track/Clip/DeviceParameter exposes, whether a
   property is observable), `Read` the matching file in `Resources/AbletonLOM/references/` — §6b.
   These are different sources answering different questions; do not substitute one for the other.
3b. ⚠️ **Before concluding anything is unknown, search for the evidence rather than the claim.**
   `grep` for `[CAP`, `[SRC`, `[MAN`, a date stamp or a hex address — not for the sentence you expect
   to find. This roadmap and this README *summarise*; the capture that settled a question lives in the
   topic doc, and a summary that leaves a question open does not mean the question is open. A whole
   session was spent re-deriving §5.1b this way — §6b-38.
4. Make the change, add an offline guard for anything the framework could silently disagree with, and
   **verify the guard by reintroducing the bug**.
5. Update the docs in the same pass. That's the standing instruction, and it is the only reason this
   handoff is usable at all.

### If you are picking up the 2026-08-03 audit findings — the suggested order

1. **The missing skin keys** (§7). Real dark buttons, a two-line fix, and it comes with the guard
   that stops a fourth instance of the same bug.
2. **`Loop End`** (§7). One decision, then make the three places agree.
3. **Split the `setup()` try** (§7). Cheap, and it is what makes the next silent failure visible.
4. **Log the swallowed `entries()` failure** and the other silent guards (§7).
5. **`MixerView.forget()`** in `full_redraw`, and the doubled teardown writes.
6. **Dead code and stale comments**, in one sweep, last — so the sweep catches whatever items 1-5
   leave behind.

Everything above is offline-testable. None of it needs hardware.

### If you are picking up Phase 9 (touch strips) — the next feature

Nothing is written yet. Read **`Motion32_Pads_Banking_and_Strips.md` §5.3b first** — it supersedes
the older §5 conclusion and the original Phase 9 bullets in the roadmap, both of which were partly
wrong. The single cheapest next action is the hardware test at the end of §5.3b, which decides the
whole design: declare strip 2 as `MIDI_PB_TYPE` / channel 1 / `exclusive` with a logging value
listener *and* a mapped parameter, then see whether both fire.

⚠️ **There is one real unfixed defect in the shipped behaviour**, and it is in this area: strip 2 is
undeclared, so its channel-1 pitch bend reaches the armed track and fights strip 1 — two pitch
benders on one instrument. Declaring it `exclusive` fixes that on its own, independently of whatever
we then point it at.

**Attach this folder to the new chat**, and grant access to the script folder at
`~/Music/Ableton/User Library/Remote Scripts/Motion32/`.
