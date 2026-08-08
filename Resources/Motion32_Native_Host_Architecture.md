# Motion 32 — Native Host Architecture

The blueprint for a native client (Ableton or otherwise). This is **architecture, not protocol** —
it reconstructs the host-side state machine that makes the Motion feel native. Source: `Motion32Component.js`
(the Studio One control-surface *component*), corroborated by `Motion 32.surface.xml` and captures.

**Framing.** Motion firmware is the hardware *platform*. **Studio One is the known reference client of the
Fender native protocol on `Motion 32 Main`.** Logic, Cubase, and Ableton have *separate* clients — but of a
**different, simpler protocol (Mackie Control) on `Motion 32 Control`**, not the native protocol. Our goal is
to implement an **Ableton client of the Fender *native* protocol**, adapting the reference client's
architectural patterns to Live. The state machine below is Studio One's decomposition; it is a reference to
**adapt**, not a spec every native client is obligated to reproduce.

Confidence: everything in this document is **[SRC]** (read directly from the component source) unless
marked otherwise.

---

## 1. The core idea: a layered orthogonal state chart

The host does **not** track "one big mode." It maintains **14 independent layers**, each holding exactly
one active sub-state at a time. The active states across all layers are merged (higher layer wins on
conflicts) into a single **merged state** whose *attributes* configure every physical control. This is
the single most important architectural fact.

```
 Layer (0 = lowest priority … 13 = highest)         Active sub-state (examples)
 ──────────────────────────────────────────         ───────────────────────────
 0  kDefaultState          base defaults            (always kDefaultState)
 1  kPadMusicInput         pad layout               kPadPlayKeyboard | kPadPlayDrums
 2  kFocusInstrument       what instrument is up    kInstrumentNone|PolySynth|MonoSynth|DrumSampler
 3  kFixedVelocityModifier 16-fixed velocity        Off | On
 4  kControlFocusMode      MAIN MODE BUTTONS        kSong0 | kPlugin0 | kEditNone/Audio/Part/Pattern | kMix0
 5  kScreenMode            MENU/SCREEN BUTTONS      kAdd0 | kScale0 | kChord0 | kControl0 | kUser0 (+None variants)
 6  kVelocityTrigger       velocity-trigger pads    Off | On
 7  kNoteRepeatModifier    note-repeat hold         Off | On
 8  kMenu                  transient wheel menus    kMenuNone | FixedVelocity | Tempo | PluginDeviceRack
 9  kRateTrigger           note-repeat rate pads    Off | On
 10 kLauncher              clip launcher            Off | On
 11 kPadCommands           command pads             Off | On
 12 kNotification          transient overlays       None | OctaveChange | Plugin/Mixer/Edit/Song ParamChange | PresetChange
 13 kSplashScreen          connect / warnings       None | Default ("Studio Pro / Open a Session")
```

### Attributes the merged state produces
Each sub-state stamps zero or more of these attributes; the merge yields the live configuration:

| Attribute | Drives | Possible values (enums) |
|---|---|---|
| `screenTemplate` | which of the 4 screen templates is shown | Main(0) / Menu(1) / Mixer(2) / Params(3) |
| `pageIndex` | which **content page** the host renders into that template | `MotionSharedDisplayPage` (27 pages) |
| `knobMode` | what the **8 encoders** control | None/Song/Mixer/PluginGlobal/PluginFocus/PluginSampler/Edit… |
| `wheelMode` | what the **screen encoder (wheel)** does | ControlFocusModePaging/Mixer/ControlLinkPaging/ScreenModeFeedback/FixedVelocityMenu/TempoMenu/PluginDeviceRackMenu/UserCommandsPaging |
| `wheelPushMode` | what **pressing the wheel** does | None/AddMenuToggle/PluginDeviceRackMenuToggle/OpenExternalDeviceEditor |
| `padMode` | pad behavior | Keyboard/Sequencer/Launcher/VelocityTrigger/ChordTrigger/ScaleMusicInput/RateTrigger/Commands |
| `bankMode` | pad banking | None/KeyboardRange/KeyboardBanks16/KeyboardBanks32/ControlLinkPaging/Launcher/SimpleChordRange |
| `octaveButtonsMode` | Octave ± buttons | None/Keyboard/Launcher/SimpleChord |
| `fixedButtonMode` | the Fixed button | None/ToggleFixedVelocity/TogglePatternStepAccent |
| `padsButtonMode` | the Pads button | None/RestoreDefault/TogglePadSectionDrum/TogglePartDrum/TogglePatternDrum |
| `soloMuteButtonsMode` | Solo/Mute buttons | FocusChannel / Mixer |
| `screenButtonsMode` (Motion32) | the 8 LCD soft buttons | None/Default/ControlLink/MixerChannelSelect/MixerChannelSolo/MixerChannelMute/UserCommands |
| `displayMode` / `controlFocusMode` | high-level bookkeeping | — |

> **Design takeaway for Ableton (reference pattern, not a mandate):** this 14-layer chart is *Studio One's*
> decomposition. An Ableton client should adopt the **mechanism** — orthogonal layers that merge into a
> configuration, composed rather than hand-coded per combination — but need **not** reproduce all 14 layers
> exactly. Live has no step-sequencer/pattern or launcher-clip concepts identical to Studio One's, so some
> layers collapse or change meaning. Treat the layer list as the reference structure to adapt, not copy.

> **Critical caveat — a state attribute is NOT the same as a device command.** Of the 11 attributes the
> host applies on each commit (`applyComponentStateCommon`), only **`screenTemplate`** produces a direct
> device message (`F0 08 26 20`), and **`pageIndex`** selects *which* screen-content updates get sent. The
> other nine (`knobMode`, `wheelMode`, `wheelPushMode`, `controlFocusMode`, `displayMode`,
> `octaveButtonsMode`, `fixedButtonMode`, `padsButtonMode`, `soloMuteButtonsMode`) are **host-side
> interpretation** — they change how the host routes *incoming* controls and what LEDs it lights; they are
> not themselves commands the device receives. The full attribute→destination breakdown is in
> `Motion32_State_Trace_Table.md`.

---

## 2. Answers to the behavioral questions (the whole point)

- **When does Plugin become Mixer?** The **Plugin** and **Mix** buttons both write layer 4 (`kControlFocusMode`): `kPlugin0` sets template=Main, page=PluginGlobal, knobMode=PluginGlobal, wheel=ControlLinkPaging, soft-buttons=None. `kMix0` sets template=Mixer, page=Mix0, knobMode=Mixer, wheel=Mixer, soloMute=Mixer, soft-buttons=MixerChannelSelect. Switching the layer's active state swaps the whole configuration atomically.
- **Why do the soft keys change?** The `screenButtonsMode` attribute is stamped per state. In Mix it becomes `MixerChannelSelect`; holding Solo/Mute in Mix switches to `MixerChannelSolo/Mute`; in User mode it becomes `UserCommands`; in menus it becomes `None`.
- **How does the screen encoder (wheel) change function?** The `wheelMode`/`wheelPushMode` attributes. Song/Edit → `ControlFocusModePaging` (page through param banks). Plugin → `ControlLinkPaging`. Mix → `Mixer` (scroll channel bank). Add menu → `ScreenModeFeedback` + push = `AddMenuToggle`. Holding for Tempo/FixedVelocity/DeviceRack menus swaps wheelMode transiently (layer 8).
- **What governs Add / Scale / Chord?** Layer 5 (`kScreenMode`), gated by the **supervisor** (see §3). Scale requires a poly/mono synth focused **and** keyboard pads; Chord requires a poly synth. If those conditions fail, the mode is auto-suppressed to its `…None0` variant.
- **What triggers redraws?** Any committed layer change calls `component.onActivateState(mergedState)` → the host repaints the active template's page. Connection and the close of the on-device Global-Settings screen force a **full invalidate** (redraw everything from cache).
- **What invalidates pages?** Host notifications (`kPluginFocusChanged`, `kChordCategoryChanged`, `kSamplerControlModeChanged`, param/preset changes) re-run the affected state's `onNotifyInternal`, updating its `pageIndex`/`knobMode` and repainting. The notification layer (12) also temporarily overrides the screen (see §5).
- **What owns focus?** Layers 2 (`kFocusInstrument`) and 4 (`kControlFocusMode`), both driven by host events about what track/plugin/instrument is selected in the DAW.

---

## 3. The supervisor — transition guards & auto-corrections

State changes are not applied blindly. `MotionSharedComponentStateSupervisor` runs on every change:

**Side-effects (`applyStateChangeSideEffects`)** — when a state is requested, it may force other layers:
- Turning **Launcher On** → forces VelocityTrigger Off; if a Scale/Chord screen is up → screen→`Control0`.
- Turning **VelocityTrigger On** → forces Launcher Off; Scale/Chord screen → `Control0`.
- Entering **Scale/Chord** → cancels launcher & velocity-trigger; cancels step-sequencing if active.
- Entering **Edit Pattern** (step seq) → cancels launcher/velocity; Scale/Chord screen → `Control0`.
- Focus instrument becomes **PolySynth** → if a "ChordNone/ScaleNone" placeholder was showing, promote to real `Chord0`/`Scale0`. **MonoSynth** → promote `Scale0` only.
- Focus instrument becomes **None/DrumSampler** → suppress Chord and Scale to their None variants.

**Corrections (`applyStateCorrections`)** — applied after every change as a safety net:
- Chord active but not allowed (needs PolySynth) → suppress to `ChordNone0`.
- Scale active but not allowed (needs Poly/Mono synth **and** keyboard pads) → suppress to `ScaleNone0`.

**Rules (`MotionSharedComponentStateRules`)** — the predicates the above use:
- `isScaleModeAllowed` = (PolySynth OR MonoSynth) AND keyboard pads.
- `isChordModeAllowed` = PolySynth.

> For Ableton we must decide the analogues: e.g., "Scale allowed when the focused track hosts an instrument
> and pads are in keyboard mode." The *mechanism* (guarded layered transitions) transfers directly; only
> the DAW-specific predicates change.

---

## 4. Processing model — queued, batched, one redraw

`MotionSharedComponentStateHandler` is an async, coalescing engine:

1. Control handlers call `requestState(layer, stateId)` (or `requestGroup` / `requestNavigation`). Requests are pushed to a queue.
2. `beginStateUpdates()` / `commitStateUpdates()` wrap a batch so several requests coalesce.
3. Processing is **deferred** via `Host.Signals.postMessage(kProcessQueueSignal)` — it never runs inline.
4. `processQueue()` takes a **snapshot**, drains the queue applying each change through the supervisor (side-effects → set → corrections), then **commits once**: activates the changed layer states and calls `onActivateState(mergedState)`.

This is why the device never flickers through intermediate states: many layer changes collapse into one
coherent **commit**. Note the precise meaning:

> **One coherent state commit triggers one logical redraw batch — which may itself contain many
> individual screen, LED, and RGB packets** (a full template repaint can be dozens to hundreds of
> `F0 08 26 21 …` element updates plus button/pad LED and encoder-halo messages). "One redraw" is one
> *logical* repaint, not one device command.

**An Ableton script should replicate the commit model** (queue + single deferred commit), and — because
one commit can emit hundreds of packets — will also need **output throttling/scheduling** to avoid
flooding Live's MIDI thread. Cache the full device model and diff on commit so only changed elements are
re-sent.

---

## 5. Session lifecycle

**Verified source ordering** (from `Motion32MidiDevice.js` `onMidiOutConnected`): the redraw is
scheduled *before* the identity request is sent, and is **not** gated on the identity reply.

```
   MIDI out connects
          │  1. host → device: 8F 00 7F        (enter native mode)
          │  2. host: invalidate cached handlers + invalidateAll  → schedule FULL redraw
          │  3. host → device: identity request  F0 7E 7F 06 01 F7
          ▼
   Redraw runs (does NOT wait for the identity reply)
          │
          │  (async) device → host: identity reply → host parses firmware.
          │          firmware < 1003 → show a red warning splash. This gates the
          │          WARNING only, not the initial redraw.
          ▼
   Splash layer (13): "Studio Pro / Open a Session" until a session/host context exists
          │
          ▼
   Operational: layered state chart live; host pushes screen/LED per merged state
          │
   (device → host  F0 08 26 22 01  = user opened local Global Settings → SUSPEND feedback;
    …22 00 = closed → re-invalidate & redraw)
          │
          ▼
   MIDI out disconnects / unload
             host → device: 8F 00 00   (leave native mode)
```

> **Prototype implication:** a first Ableton client can enter native mode, send the identity request,
> and schedule a complete redraw immediately — then validate firmware asynchronously when the reply
> arrives. It should **not** withhold all feedback pending the identity reply; the reference host doesn't.

Layer 13 (Splash) and Layer 12 (Notification) sit **above** everything so they can transiently take over
the screen (warnings, "Open a Session," octave/param/preset pop-ups) without disturbing the underlying
mode — when they clear, the prior merged state repaints automatically.

---

## 6. Control ownership (who computes what)

⚠️ **Corrected 2026-07-25 — this section previously had the split badly wrong.** It claimed the firmware
owned the Scale engine, the Chord/progression engine and Keys/Blocks, and that "note generation happens
on-device." In **native host mode that is false**: the pads send a fixed note per pad (36–67) and every
musical transform runs in the host. The device's own engines are what it uses **stand-alone**. Full
evidence chain in `Motion32_Scale_and_Chord_Engine.md` §2.

**Motion firmware owns (genuinely local — do NOT reimplement):**
Pressure type/feel, Encoder Curve, DAW Mode, all Global Settings and the local Global-Settings menu
navigation, plus the entire stand-alone MIDI scene used when no native host is attached.

**Host (our Ableton client) owns — including everything musical:**
Pad → note mapping in all its forms: Keys/Blocks layout, Scale + root + octave, A–H range, and
chord voicing. Studio One does this through its own `PadSectionComponent`
(`setScale` / `setCurrentOctave` / `setRootOffset` / `setPadOffset` / `setKeyboardModeLayout`) and its
`chordTriggerModeSettings`, into which it imports `Famous.chords` / `Simple.chords` at init.
Fixed & 16-Velocity are likewise host params. Plus the layered state chart, all four screen templates'
content, every LED and RGB colour, encoder→parameter binding and paging, mixer values, track names and
colours, soft-key labels, transport reflection and notification overlays.

> The corollary for Live: because the transform is ours, it must not cost latency. A scale layout is a
> *static per-pad note remap* and is free; a chord is not, and needs a device in the signal path rather
> than Python in the note path. See `Motion32_Scale_and_Chord_Engine.md` §5.

**Host (our Ableton client) owns:**
The entire layered state chart above; all four screen templates' text/color/value content; every LED and
RGB color; encoder→parameter binding and paging per `knobMode`; mixer fader/mute/solo/meter values; track
names & colors; soft-key labels; transport reflection; and the notification overlays.

---

## 7. Event flow (encoder example)

```
 Encoder turn
   → relative CC 0x0E–0x15 (sign-bit; §Spec 2.1)
   → host decodes delta, routed by current knobMode:
        PluginGlobal/Focus → focused device parameter
        Mixer              → channel volume (bank of 8)
        Song/Edit          → song/edit parameter bank
   → apply to Live parameter
   → feedback back to device:
        screen value element (F0 08 26 21 … attr 02)   [encoder arc fill]
        encoder halo RGB (0xB1/B2/B3 <id> …)           [halo color = track/param color]
        optional transient Notification overlay (layer 12) showing the new value
```

Pads, buttons, and the wheel follow the same shape: physical event → interpret under the merged state's
mode attributes → act on Live → push screen/LED feedback → (optionally) raise a notification overlay.

---

## 8. What to build first for Ableton
1. **Session + layered engine skeleton:** handshake (§5), the 14-layer model (§1), the queued single-commit processor (§4). Prove one mode switch (Plugin↔Mix) reconfigures template + knobMode + soft-buttons in one redraw.
2. **Supervisor with Ableton predicates** (§3): port the guard structure; define Live-specific "scale/chord allowed" conditions.
3. **knobMode routing** (§7) to Live parameters/mixer with paging.
4. **Screen + LED feedback** per template using the screen map, driven off the cached merged state.
5. **Notifications & splash** (layers 12–13) last — they're overlays on a working base.

Still genuinely open (unchanged from the gap analysis): encoder acceleration under Encoder Curve, whether
feedback is gated on the handshake, aftertouch format, exact emitted pad-note ranges, and MCU-port
coexistence. None of these block starting the architecture above.
