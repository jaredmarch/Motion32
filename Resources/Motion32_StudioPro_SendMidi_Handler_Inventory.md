# Motion 32 Studio Pro Send/Handler Inventory

Date: 2026-07-27

Scope:

- `Resources/From Studio Pro/Motion32MidiDevice.js`
- `Resources/From Studio Pro/Motion32Component.js`

Goal: inventory every direct `sendMidi` / `sendSysex` path and the handler writes
that feed them, then classify each as lifecycle command, screen command,
LED/color command, or host-only state change with no device-facing wire command.

## Executive Summary

`Motion32MidiDevice.js` owns the device-facing wire protocol. Every direct
`sendMidi()` / `sendSysex()` call found in the two requested files is in
`Motion32MidiDevice.js`; `Motion32Component.js` has no direct `sendMidi()` or
`sendSysex()` calls.

`Motion32Component.js` changes the control surface by writing host params and
requesting layered component states. Those writes become device commands only
when they are bound to handlers registered by `Motion32MidiDevice.js`:

- `screenTemplateSwitch` and screen element handlers -> screen SysEx.
- pad/button/strip LED handlers -> LED state/color MIDI messages.
- touch-strip LED invalidate options -> cached LED resend.
- most mode params (`knobMode`, `wheelMode`, `wheelPushMode`,
  `screenButtonsMode`, Scale/Chord states, etc.) -> host-only interpretation and
  redraw decisions, not separate firmware mode commands.

## Direct Wire Sends

| Source | Call | Command class | Wire effect |
|---|---:|---|---|
| `Motion32MidiDevice.js:252` | `sendMidi(NoteOff \| 15, 0x00, 0x00)` | lifecycle command | Exit native/integrated host mode: `8F 00 00`. |
| `Motion32MidiDevice.js:262` | `sendMidi(NoteOff \| 15, 0x00, 0x7F)` | lifecycle command | Enter native/integrated host mode: `8F 00 7F`. |
| `Motion32MidiDevice.js:984` | `sendSysex(IdentityRequestMessage.build(...))` | lifecycle / handshake command | Universal Identity Request after native-mode entry. |
| `Motion32MidiDevice.js:203` | `sendMidi(status, address, value)` | LED/color command | Pad state/animation LED write, usually NoteOn-class at pad address. |
| `Motion32MidiDevice.js:206` | `sendMidi(status, address, value)` | LED/color command | Button state LED write, Controller-class at button/LED address. |
| `Motion32MidiDevice.js:209-211` | `sendMidi(status \| 1/2/3, id, r/g/b)` | LED/color command | RGB write as three component messages. Pad color handlers use NoteOn base; button color handlers use Controller base. |
| `Motion32MidiDevice.js:390` | `sendMidi(Controller, state.address, state.value)` | LED/color command | Touch-strip LED write, one CC per strip LED address. |
| `Motion32MidiDevice.js:967` | `sendSysex(screen template buffer)` | screen command | Template select: `F0 08 26 20 <template> F7`, suppressed while Global Settings is active. |
| `Motion32MidiDevice.js:953` | `sendSysex(visibility buffer)` | screen command | Element visibility update: `F0 08 26 21 ... attr 0x03 ... F7`. |
| `Motion32MidiDevice.js:959` | `sendSysex(font-style buffer)` | screen command | Element font-style update: `F0 08 26 21 ... attr 0x04 ... F7`. |
| `Motion32MidiDevice.js:1058` | `sendSysex(text buffer)` | screen command | Element text update: `F0 08 26 21 ... attr 0x00 ... F7`. |
| `Motion32MidiDevice.js:1062` | `sendSysex(value buffer)` | screen command | Element value update: `F0 08 26 21 ... attr 0x02 ... F7`. |
| `Motion32MidiDevice.js:1066` | `sendSysex(color buffer)` | screen command | Element RGB/color update inside screen SysEx: attr `0x01`. Not the same address space as physical LED RGB. |
| `Motion32MidiDevice.js:1070` | `sendSysex(visibility buffer)` | screen command | Element visibility helper; same packet class as above. |
| `Motion32MidiDevice.js:1074` | `sendSysex(font-style buffer)` | screen command | Element font-style helper; same packet class as above. |

## Handler Write Inventory

### Lifecycle / handshake

- `PadControllerMidiDevice.onMidiOutConnected(true)` sends `8F 00 7F`, then
  invalidates cached LED/display handlers and host state
  (`Motion32MidiDevice.js:259-265`).
- `MotionSharedMidiDevice.onMidiOutConnected(true)` resets
  `globalSettingsActive`, calls the base method above, then sends the identity
  request (`Motion32MidiDevice.js:990-995`).
- `PadControllerMidiDevice.onExit()` sends `8F 00 00` before `super.onExit()`
  (`Motion32MidiDevice.js:251-253`).

Classification: lifecycle command.

### Pad and button LED handlers

- `ButtonStateLEDHandler.sendValue()` maps a normalized host value through
  `valueToButtonLEDState()` and sends a Controller LED state write
  (`Motion32MidiDevice.js:136-145`).
- `PadStateLEDHandler.sendValue()` updates cached pad state and emits the
  combined pad state/animation value (`Motion32MidiDevice.js:158-164`).
- `PadAnimationLEDHandler.sendValue()` updates cached animation and emits the
  combined pad state/animation value (`Motion32MidiDevice.js:166-172`).
- `PadControllerMidiDevice.combinePadStates()` maps off/on/blink/pulse to
  `0x00`, `0x7F`, `0x01`, `0x02` (`Motion32MidiDevice.js:213-225`).

Classification: LED/color command.

### RGB handlers

- `ColorLEDHandler.sendValue()` converts a host color code to RGB and calls
  `sendRgbColor()` (`Motion32MidiDevice.js:174-184`).
- `createHandlerInternal()` binds:
  - `PadColorLEDHandler` to NoteOn-base RGB messages.
  - `ButtonColorLEDHandler` to Controller-base RGB messages.
  - state LED handlers to their state-write classes
    (`Motion32MidiDevice.js:227-239`).
- `sendRgbColor()` sends three component messages using `status | 1`,
  `status | 2`, and `status | 3` (`Motion32MidiDevice.js:208-211`).

Classification: LED/color command.

### Touch-strip LED handlers

- `StripLEDHandler.sendState()` emits dirty strip LED states as Controller CCs
  (`Motion32MidiDevice.js:387-391`).
- `MultiLEDHandler` and `SingleLEDHandler` update cached on/off states based on
  normalized values and LED-index mapping (`Motion32MidiDevice.js:407-444`).
- Motion 32 registers two LED handler styles per strip:
  - `touchStripMultiLEDBipolar[n]`
  - `touchStripMultiLEDFill[n]`
  (`Motion32MidiDevice.js:1337-1340`).
- `MotionSharedComponentHelper.updateTouchStripMode()` does not send a mode
  command. It invalidates one of those LED handlers, which causes a cached LED
  resend later (`Motion32Component.js:3182-3196`).

Classification: LED/color command for the eventual strip LED CCs; host-only
state change for the mode choice itself.

### Screen SysEx handlers

- `ScreenTemplateChangeMessage.build()` creates `F0 08 <deviceId> 20
  <template> F7` (`Motion32MidiDevice.js:789-799`).
- `ScreenUpdateMessage` defines message `0x21` and attributes:
  - `0x00` text
  - `0x01` color
  - `0x02` value
  - `0x03` visibility
  - `0x04` font style
  (`Motion32MidiDevice.js:800-817`).
- `ScreenTextUpdateMessage`, `ScreenColorUpdateMessage`,
  `ScreenValueUpdateMessage`, `ScreenVisibilityUpdateMessage`, and
  `ScreenFontStyleUpdateMessage` build the concrete `0x21` packets
  (`Motion32MidiDevice.js:818-870`).
- `ElementControlHandler.sendValue()` is the common handler entry point for
  screen element writes (`Motion32MidiDevice.js:893-901`).
- `MotionSharedMidiDevice.createHandler()` maps XML handler classes to concrete
  screen senders (`Motion32MidiDevice.js:1032-1054`).
- `MotionSharedScreenWidget.flush()` / `LabelWidget.sendAttributes()` batch
  menu/list widget visibility, text, color, and font writes through the same
  screen senders (`Motion32MidiDevice.js:720-765`).
- `Motion32MenuList*Handler` updates the menu display buffer and flushes it
  through screen SysEx (`Motion32MidiDevice.js:1304-1334`).

Classification: screen command.

### Host-event generator handlers

- `HostEventHandler.sendValue()` calls a generator callback and does not send
  device-facing MIDI by itself (`Motion32MidiDevice.js:446-455`).
- Registered generator handlers:
  - `pitchBendEventGenerator` -> `sendPitchBendToHost`
  - `modulationEventGenerator` -> `sendModulationToHost`
  - `expressionEventGenerator` -> `sendExpressionToHost`
  - `breathControlEventGenerator` -> `sendBreathControlToHost`
  (`Motion32MidiDevice.js:969-970`, `Motion32MidiDevice.js:1359-1362`).

Classification: host-only state/event generation with no device-facing command.

### Receive-side / host-only handlers in the MIDI-device file

- `PitchBendHandler.receiveMidi()` consumes touch-strip pitch-bend input and
  updates host values; it sends nothing to the device
  (`Motion32MidiDevice.js:318-333`).
- `MotionSharedKnobTouchEnablerHandler.sendValue()` calls `updateValue(value)`
  only; it is a host/internal enable signal, not a wire write
  (`Motion32MidiDevice.js:921-927`).
- `GlobalSettingStateMessage` is device-to-host only. When open, outgoing
  screen template SysEx is suppressed; when closed, all controls are invalidated
  and redrawn (`Motion32MidiDevice.js:871-881`, `Motion32MidiDevice.js:997-1002`).
- Identity reply parsing is device-to-host only, then notifies the component of
  firmware version (`Motion32MidiDevice.js:1004-1010`).

Classification: host-only state change, except for the redraws triggered after
Global Settings closes, which re-enter the normal screen/LED command paths.

## Motion32Component.js Handler Writes

`Motion32Component.js` contains no direct device-facing `sendMidi()` or
`sendSysex()` calls. Its writes fall into these groups.

### Layered state queue

- `requestState()`, `requestGroup()`, and `requestNavigation()` enqueue host
  state changes (`Motion32Component.js:2701-2714`).
- `commitSnapshot()` activates changed layers, merges the state, applies payload
  corrections, and calls `component.onActivateState(mergedState, true)`
  (`Motion32Component.js:2759-2767`).
- `Motion32Component.applyComponentState()` writes merged state into params:
  common params plus `bankMode`, `padMode`, and `screenButtonsMode`
  (`Motion32Component.js:4416-4420`).

Classification: host-only state machine. Device-facing output happens only if a
written param is bound to a MIDI-device handler.

### Common component-state params

`applyComponentStateCommon()` writes these state attributes into host params
(`Motion32Component.js:3403-3414`):

- `controlFocusMode`
- `displayMode`
- `pageIndex`
- `knobMode`
- `screenTemplate`
- `wheelMode`
- `wheelPushMode`
- `octaveButtonsMode`
- `fixedButtonMode`
- `padsButtonMode`
- `soloMuteButtonsMode`

Classification:

- `screenTemplate` is screen command *when* it reaches the
  `screenTemplateSwitch` handler, producing message `0x20`.
- `pageIndex` and `displayMode` are host-side display routing inputs; their
  device-facing effect is redraw through the screen element handlers, not a
  standalone command.
- `knobMode`, `wheelMode`, `wheelPushMode`, `octaveButtonsMode`,
  `fixedButtonMode`, `padsButtonMode`, `soloMuteButtonsMode`, `bankMode`,
  `padMode`, and `screenButtonsMode` are host-only interpretation/routing state.

### Control-surface mode button handlers

These handlers request states; they do not directly send mode commands:

- Scale button toggles `ScreenMode` between `Scale0` and `Control0`
  (`Motion32Component.js:3505-3513`).
- Chord button toggles `ScreenMode` between `Chord0` and `Control0`
  (`Motion32Component.js:3515-3523`).
- Control/Add/Song/Edit/Mix buttons request screen or focus states
  (`Motion32Component.js:3459-3503`, `Motion32Component.js:3525-3528`).
- Shift press/release toggles `PadCommands` and touch-strip bypass
  (`Motion32Component.js:3530-3538`).
- Tap hold opens/closes the Tempo menu (`Motion32Component.js:3554-3560`).

Classification: host-only state change with no standalone wire command. The
visible device effect is subsequent screen/LED redraw.

### Touch-strip mode writes

- Constructor initializes `touchStrip0Mode` and `touchStrip1Mode`, then sets the
  receive handlers to default mode (`Motion32Component.js:4958-4963`).
- Shift + strip button toggles the mode params between pitch/expression and
  mod/breath (`Motion32Component.js:4736-4746`).
- `updateTouchStripMode()` invalidates the matching LED handler for bipolar vs
  fill visualization (`Motion32Component.js:3182-3196`).

Classification: host-only mode change plus LED/color command on redraw. No
separate device touch-strip-mode opcode found here.

### Scale and Chord writes

- `MotionSharedScaleMenuHelper` stores keyboard/layout state in host memory
  (`Motion32Component.js:2449-2463`).
- Keyboard/layout changes request or notify host state; they do not send a
  firmware scale/chord command (`Motion32Component.js:3347-3356`).
- Chord category changes notify the chord component state and update host menu
  state (`Motion32Component.js:2435-2447`, `Motion32Component.js:2995`).

Classification: host-only state change with subsequent screen redraw and
host-generated musical behavior. No direct device-facing Scale/Chord command in
these files.

### Pad section and performance-mode writes

- Pad section setup calls `addHandlerForRole`, `setActiveHandler`,
  `setPadColor`, `setMappingMode`, `setRowOffset`, and `setColumnOffset` on
  Studio Pro pad-section handlers (`Motion32Component.js:885-899`,
  `Motion32Component.js:1388-1423`, `Motion32Component.js:5095-5136`).
- Launcher, velocity trigger, note repeat, fixed velocity, octave, sampler mode,
  and pad command handlers all mutate host params/state/handlers. They may cause
  pad LEDs or screen content to redraw through registered handlers, but no
  discrete Motion firmware command is sent from this file.

Classification: host-only state change, with possible downstream LED/color or
screen commands through the MIDI-device handlers.

## Practical Classification for Reverse Engineering

### Real device-facing commands to capture

1. Lifecycle:
   - `8F 00 7F`
   - `8F 00 00`
   - Universal Identity Request
2. Screen:
   - `F0 08 26 20 <template> F7`
   - `F0 08 26 21 <template> <zone> <element> <attribute> <data...> F7`
3. LED/color:
   - Pad state/animation NoteOn-class writes.
   - Button state Controller writes.
   - Pad RGB component writes.
   - Button/encoder RGB component writes.
   - Touch-strip LED Controller writes.

### Host-only changes to avoid over-interpreting

- Scale mode and Chord mode activation.
- Knob/wheel/wheel-push mode changes.
- Screen button mode changes.
- Pad mode / launcher / command / velocity-trigger / note-repeat state.
- Touch-strip mode selection.
- Control focus and display mode changes, except for the redraw commands they
  cause.

These are still critical to the user experience, but the command on the wire is
usually "redraw the screen / LEDs" rather than "tell the firmware to enter that
feature mode."
