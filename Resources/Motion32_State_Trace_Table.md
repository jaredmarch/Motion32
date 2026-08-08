# Motion 32 — State → Command Trace Table

Bridges the recovered Studio One state chart (`Motion32_Native_Host_Architecture.md`) to an implementable
Ableton client, by tracing each state through to actual device I/O. Source: `Motion32Component.js`
(`applyComponentStateCommon`, the Configurator) + `Motion 32.surface.xml` bindings + the screen map.

Confidence: **[SRC]** proven in source · **[DRV]** derived from the screen map / surface bindings (mechanism
proven, exact packet set is the logical consequence) · **[INF]** inferred, needs a capture to confirm.

---

## 1. The crucial distinction: attribute ≠ device command

On every state commit, `applyComponentStateCommon` writes 11 attributes to host params. **Only one becomes
a direct device message.** The rest change how the host *interprets the same, fixed incoming control
messages* and what LED/screen feedback it emits. Physical controls always send the same CC/note (see the
handshake spec §2) regardless of mode — the *meaning* is assigned host-side.

| Merged attribute | Host param | Destination | Produces outgoing device MIDI? |
|---|---|---|---|
| `screenTemplate` | screenTemplateParam | → `screenTemplateSwitch` control → **`F0 08 26 20 <t>`** | **YES — direct SysEx** [SRC] |
| `pageIndex` | displayPageIndexParam | selects which screen **content** the host renders | Indirect — drives a batch of `F0 08 26 21 …` element updates [DRV] |
| `knobMode` | knobModeParam | which parameter page the 8 encoders drive; encoder-halo colors | No command; routes incoming CC 0x0E–15 + emits halo RGB [SRC] |
| `wheelMode` | wheelModeParam | meaning of the wheel (CC 0x1D) | No command; host-side incoming [SRC] |
| `wheelPushMode` | wheelPushModeParam | action of wheel push (CC 0x78) | No command; host-side incoming [SRC] |
| `screenButtonsMode` | screenButtonsModeParam | meaning + labels of the 8 LCD buttons (CC 0x24–2B) | No command; routes incoming + drives label text [SRC] |
| `soloMuteButtonsMode` | soloMuteButtonsModeParam | meaning of Solo/Mute (CC 0x4A/4B) | No command; host-side incoming [SRC] |
| `octaveButtonsMode` | octaveButtonsModeParam | meaning of Octave ± (CC 0x40/41) | No command; host-side incoming [SRC] |
| `fixedButtonMode` | fixedButtonModeParam | action of Fixed (CC 0x43) | No command; host-side incoming [SRC] |
| `padsButtonMode` | padsButtonModeParam | action of Pads (CC 0x44) | No command; host-side incoming [SRC] |
| `controlFocusMode` / `displayMode` | params | host bookkeeping only | No [SRC] |
| `padMode` / `bankMode` | (pad section) | how incoming pad notes are routed/mapped | No discrete command; host-side pad-section config [SRC] |

**Takeaway for Ableton — scoped precisely:** *within the merged component-state application path*
(`applyComponentStateCommon`), only **`screenTemplate`** directly selects a device mode and **`pageIndex`**
drives screen content; the remaining merged attributes route host behavior and feedback. This is **not** the
whole device protocol — other host→device messages exist outside this path: native-mode entry/exit
(`8F 00 7F`/`8F 00 00`), button state + RGB, pad LED state, touch-strip LEDs, Global-Settings feedback
suspension, and possibly an as-yet-undiscovered pad-mode sync (see §5). The practical point stands:
"reproduce all 14 layers" is not required — you must reproduce the *interpretation*, however you structure it.

---

## 2. Per-state trace (control-focus layer, layer 4)

Columns: **Attributes** (key ones; all [SRC] from Configurator) · **Outgoing device effect** · **Incoming
controls interpreted** · **Screen/LED**.

### Song (`kSong0`)
- **Attributes:** template=Params(3), page=Song0, knobMode=Song, wheel=ControlFocusModePaging, focus=Song.
- **Outgoing:** `F0 08 26 20 03` then Params-template text/value/color updates for the 8 song params [DRV].
- **Incoming:** 8 encoders → song parameter bank; wheel → page through param banks; soft buttons=Default.
- **Screen/LED:** Params screen shows 8 label/value tiles; encoder halos colored per param.

### Plugin (`kPlugin0`)  — *the confirmed Control-Link screen*
- **Attributes:** template=**Main(0)**, page=PluginGlobal0, knobMode=PluginGlobal, wheel=ControlLinkPaging, wheelPush=None, screenButtons=None. On plugin focus → page/knobMode promote to PluginFocus0; if sampler → PluginSampler0.
- **Outgoing:** `F0 08 26 20 00` then Main-template encoder tiles (zones 3–6/8–11): value+color+CC label per encoder [DRV, capture-confirmed].
- **Incoming:** 8 encoders → Control-Link / focused-device params; wheel → page Control-Link banks; wheel push=none.
- **Screen/LED:** Main screen encoder tiles; halos yellow=focus-assigned / blue=global-assigned (`kControlLinkFocusAssigned`/`…GlobalAssigned`).

### Edit — None / Audio / Part / Pattern (`kEditNone0`/`kEditAudio0`/`kEditPart0`/`kEditPattern0`/`kEditPattern1Step`)
- **Attributes:** template=Params(3), page=EditX, knobMode=EditX, wheel=ControlFocusModePaging, focus=Edit. Pattern adds padMode=Sequencer, fixed=PatternStepAccent, pads=TogglePatternDrum, bank=KeyboardBanks16, octave=None. Part adds pads=TogglePartDrum.
- **Outgoing:** `F0 08 26 20 03` + Params content for the edit context [DRV].
- **Incoming:** encoders → edit params; **in Pattern**, pads become the step sequencer (notes reinterpreted as steps); Fixed button toggles step-accent modifier.
- **Screen/LED:** Params tiles; pattern pad LEDs reflect steps.
- **Note:** `kEditPattern0 ↔ kEditPattern1Step` are connected as prev/next (wheel/nav toggles the sub-page).

### Mix (`kMix0`)
- **Attributes:** template=**Mixer(2)**, page=Mix0, knobMode=Mixer, wheel=Mixer, soloMute=**Mixer**, screenButtons=**MixerChannelSelect**, focus=Mix.
- **Outgoing:** `F0 08 26 20 02` then Mixer-template per-channel updates: ch number, fader, mute, solo, label bg color (track color), label text, L/R meters (zones 1–8, elements 1–8) [DRV, capture-confirmed for element roles].
- **Incoming:** 8 encoders → channel volumes (bank of 8); wheel → scroll channel bank; **soft buttons select channels**; holding Solo/Mute + soft button → per-channel solo/mute (`screenButtonsMode` transiently → MixerChannelSolo/Mute).
- **Screen/LED:** Mixer screen with 8 strips; soft-button LEDs reflect channel selection.

---

## 3. Per-state trace (screen-mode layer, layer 5)

### Add (`kAdd0`)
- **Attributes:** template=Menu(1), page=Add0, displayMode=Add, wheel=ScreenModeFeedback, wheelPush=**AddMenuToggle**, screenButtons=None.
- **Outgoing:** `F0 08 26 20 01` + Menu-template two-column list text/color [DRV].
- **Incoming:** wheel scrolls the add menu; wheel push confirms/toggles; soft buttons navigate columns.
- **Screen/LED:** Menu screen; selected row bold + highlight color.

### Scale (`kScale0`)  — *host-side pad-section config, NOT a discrete command*
- **Attributes:** template=Menu(1), page=Scale0, displayMode=Scale, padMode=ScaleMusicInput, wheel=ScreenModeFeedback, pads=RestoreDefault.
- **Outgoing:** `F0 08 26 20 01` + Menu content [DRV]. **No discrete "scale on" command** — `onActivate` calls `enableScaleMode(true)` → `onPadSectionScaleChanged/…LayoutIndexChanged/…RootOffsetChanged` (host pad-section params). The on-wire consequence is the changed pad-note mapping + menu redraw, **not** a mode opcode. [SRC / on-wire effect INF — needs capture]
- **Incoming:** wheel selects scale/key; pads emit scale-mapped notes; soft buttons pick Main/Modes/Key + Guide/Lock.
- **Gate (supervisor):** only valid with a poly/mono synth focused **and** keyboard pads, else auto-suppressed to `kScaleNone0` (page=ScaleNoInstrument). [SRC]

### Chord (`kChord0`)
- **Attributes:** template=Menu(1), page=Chord0, displayMode=Chord, padMode=ChordTrigger, octave=None, bank=None, wheel=ControlFocusModePaging.
- **Outgoing:** `F0 08 26 20 01` + Menu content [DRV]. Enters via `MotionSharedChordComponentState`; category changes handled by `chordMenuHelper` (host-side). [SRC / on-wire INF]
- **Incoming:** single pad → chord; wheel pages; soft buttons choose category/progression.
- **Gate:** requires a poly synth, else suppressed to `kChordNone0`. [SRC]

### Control (`kControl0`)
- **Trigger:** **Control button** (CC `0x23`, unshifted). Shift+Control → `kUser0` instead (see User). [SRC]
- **Attributes:** displayMode=Control **only** (no template/page/knob overrides).
- **Outgoing:** none of its own — it is the neutral "return to underlying control-focus view" state that scale/chord/launcher/velocity collapse to. [SRC]
- **Incoming/Screen:** whatever the control-focus layer dictates.

### User (`kUser0`)
- **Trigger:** **Shift + Control button** (CC `0x23` while `shiftModifier` held) → requests `kUser0` on the screen-mode layer; Control **without** Shift → `kControl0`. There is no dedicated User button. [SRC — `onReceive_controlButton`]
- **Attributes:** template=Params(3), page=User0, displayMode=User(10), screenButtons=**UserCommands**, wheel=UserCommandsPaging, wheelPush=**OpenExternalDeviceEditor**, fixed=ToggleFixedVelocity.
- **Outgoing:** `F0 08 26 20 03` + Params content = user-command labels [DRV].
- **Incoming:** soft buttons trigger user commands; wheel pages command banks; wheel push opens external editor.

---

## 4. Modifier & overlay layers (brief)
- **VelocityTrigger On** (layer 6): padMode=VelocityTrigger, fixed=None, pads=RestoreDefault; forces Launcher off. Toggled by the **16-Velocity button (CC 0x42, `fineButton`)** via `onReceive_fineButton`. [SRC]
- **Launcher On** (layer 10): padMode=Launcher, octave=Launcher, bank=Launcher; forces VelocityTrigger off + opens launcher GUI (`showLauncher`). [SRC]
- **Menu** (layer 8, transient via wheel-hold): FixedVelocity / Tempo / PluginDeviceRack → template=Menu, its own wheelMode; overrides the wheel until dismissed. [SRC]
- **Notification** (layer 12, transient overlay): OctaveChange / Plugin·Mixer·Edit·Song ParamChange / PresetChange → temporarily swap template+page to show the change (per-knob for param changes), then revert to the underlying merged state. [SRC]
- **Splash** (layer 13, highest): Default → Params template, "Studio Pro / Open a Session"; red warning background if firmware < 1003. [SRC]

---

## 5. What this table proves vs. still needs a capture
- **Proven [SRC]:** the attribute set per state; that only `screenTemplate` is a direct device command; that `pageIndex` selects content; that all other attributes are host-side interpretation; the supervisor gates on Scale/Chord.
- **Derived [DRV]:** the exact element-update packet set per page (from the screen map) — mechanism certain, exact bytes are the logical consequence.
- ~~**Needs hardware capture [INF]:** the precise on-wire effect of entering Scale/Chord…~~
  **CLOSED (2026-07-25) — and the answer is "no on-wire effect at all."** Entering Scale or Chord
  produces **no pad-note remap on the wire and no mode opcode**, because the device never remaps pad
  notes in native mode: pads always send their fixed symbolic pitch (36–67) and Studio One applies the
  scale/chord itself via its own `PadSectionComponent`. The only outgoing traffic is the template
  switch plus content and LED updates, exactly as the `[DRV]` rows predicted. Evidence in
  `Motion32_Scale_and_Chord_Engine.md` §2.

  This also settles §2's `[SRC / on-wire effect INF]` caveats on `kScale0` and `kChord0`: the
  `enableScaleMode()` → `onPadSectionScaleChanged` chain terminates in a **host** call
  (`PadSectionComponent::setScale`), never in a device message.
