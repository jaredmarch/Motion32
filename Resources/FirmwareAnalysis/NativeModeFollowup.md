# Motion 32 Native Mode Follow-Up

Date: 2026-07-26

Scope: follow-up on "native mode" / integrated host mode entry and exit, with
special attention to what Studio Pro sends and what the firmware appears to do.
The firmware may not name this state "native mode"; this note tracks behavior
instead of relying on string names.

## Summary

- Studio Pro's exposed JavaScript does send the lifecycle bytes:
  - Enter integrated/host mode: `8F 00 7F`
  - Leave integrated/host mode: `8F 00 00`
- The Studio Pro MIDI-device subclass then sends the Universal Identity Request
  after the base/shared MIDI device has handled connect and host-mode entry.
- The firmware image does not contain a useful plain-text name for this state.
  The useful firmware-facing terms are instead local/global UI terms such as
  `DAW mode`, `Global Settings`, `MIDI OK`, `Motion 32 Main`, and
  `Motion 32 Control`.
- The firmware-side native-mode receiver has not been identified yet. A raw
  binary search for `8F 00 7F` finds no exact byte sequence, and the exact
  `8F 00 00` byte triples found in the image are not inside Ghidra-recovered
  functions.
- Ghidra's best `0x8f` candidate, `FUN_0002164c`, is not the lifecycle
  receiver. It appears to build an outgoing Fender SysEx packet: the decompiler
  shows `0x8f0`, which is little-endian bytes `F0 08`, not MIDI status `8F`.

## Studio Pro Source Evidence

From `Resources/From Studio Pro/Motion32MidiDevice.js`:

- `SharedMidiDevice.onMidiOutConnected(state)`:
  - calls `super.onMidiOutConnected(state)`
  - when `state` is true, sends `PreSonus.Midi.kNoteOff | 15, 0x00, 0x7F`
  - invalidates cached handlers and calls `hostDevice.invalidateAll()`
- `SharedMidiDevice.onExit()`:
  - sends `PreSonus.Midi.kNoteOff | 15, 0x00, 0x00`
  - then calls `super.onExit()`
- `Motion32MidiDevice.onMidiOutConnected(state)`:
  - resets `globalSettingsActive` when connected
  - calls `super.onMidiOutConnected(state)`
  - when `state` is true, sends the identity request

So the source-level order is:

1. MIDI out connects.
2. Base/shared device sends `8F 00 7F`.
3. Cached output handlers are invalidated and full feedback is scheduled.
4. Motion32 subclass sends Universal Identity Request
   `F0 7E 7F 06 01 F7`.
5. Device replies with Universal Identity Reply.

On exit, the visible JS sends `8F 00 00`. Hardware capture says the full
effective teardown first releases LEDs/screen through handler teardown, then the
native-mode goodbye is last. Treat the capture as the higher-level behavioral
truth, because the reset writes come from base teardown code outside the small
`onExit()` override.

## Device Behavior We Can Infer

Native/integrated mode changes the identity of the main port from a standalone
MIDI scene into a host-driven control surface:

- Pads emit fixed symbolic notes `36-67`; Scale/Chord/Octave/range decisions
  are host-side in Studio Pro native integration.
- Transport uses the integrated-mode CC map on `Motion 32 Main`; a known
  hardware symptom of not fully entering native mode is seeing the pre-native
  transport CCs instead.
- Screen and LED SysEx are accepted even in the pre-native half-state, so
  visible screen output is not proof that native mode is entered.
- When the user opens on-device Global Settings, the device sends
  `F0 08 26 22 01 F7`; when closed, it sends `F0 08 26 22 00 F7`.
  The host must pause screen/template feedback while open and redraw after
  close.

## Firmware Notes

Payload-aligned Ghidra import is the cleaner model for low firmware addresses:

- File: `Resources/From Universal Control/motionupgrade.bin`
- Container header: `0x1000` bytes
- Payload file: `Resources/FirmwareAnalysis/motion32_fw_payload_0x1000.bin`
- Payload vector table: `0x0000`
- Ghidra project: `Resources/FirmwareAnalysis/ghidra_project/Motion32Firmware.gpr`
- The full-container project is still useful for wrapper/header metadata, but
  low code/data addresses in decompiled firmware should be checked against the
  payload file. For example, runtime address `0x95f4` maps to container offset
  `0xA5F4`, not container offset `0x95F4`.

Firmware strings confirm the local/device side:

- `DAW mode`
- `Global Settings`
- `Motion 32 Main`
- `Motion 32 Control`
- `MIDI OK` / `MIDI NG`
- scale/chord UI vocabulary such as `Scale`, `Chord`, `Scales`,
  `Chords/Intervals`, `Ionian`, `Dorian`, `Major Pent`, etc.

Search/probe results:

- Exact raw bytes `8F 00 7F`: no hits in `motionupgrade.bin`.
- Exact raw bytes `8F 00 00`: three hits, none in Ghidra-recovered functions.
- USB-MIDI packet forms `08 8F 00 7F` and `08 8F 00 00`: no hits. So the
  receive path is not carrying a literal packet template in flash.
- `0x8f` constants in recovered code:
  - `FUN_0002164c`
  - `FUN_0003bb58`
  - `FUN_0003e600`
- `FUN_0002164c` builds `F0 08 ... F7` outgoing SysEx-like packets. The
  decompiler renders the leading `F0 08` as halfword `0x8f0`, which is not the
  native-mode input status byte `0x8f`.
- `FUN_0003bb58` / `FUN_0003e600` look like UI/graphics assertion or draw-path
  code, not MIDI lifecycle handlers.
- `Motion32MidiReceiveProbe.java` and `Motion32AddressProbe.java` were added to
  rank/decompile functions with MIDI-like constants. The strongest-ranked
  functions are mostly allocators, UTF-8/text decoding, graphics/LVGL drawing,
  flash/PIO helpers, or outgoing SysEx construction rather than a three-byte
  MIDI receiver.
- `FUN_00022b70` is worth keeping as a firmware foothold, but it is not the
  host-mode receiver. It builds or refreshes a MIDI/control mapping table:
  it writes channel/control-shaped values including `0x0f`, `0x7f`, and a run of
  offsets, and reads internal keys `0x2c`/`0x30` through `FUN_0002ec30`.
- `FUN_00021f24` appears to redraw/update UI objects based on internal keys
  `0x2d`/`0x3b` and related value/color helpers. It is not evidence of the
  `8F 00 7F` receive branch.
- `Motion32FunctionTraceProbe.java` found no direct code references to
  `FUN_0002164c`, `FUN_00021f24`, or `FUN_00022b70`; they are likely callback
  entries reached through tables/schedulers that Ghidra has not recovered as
  ordinary call references.
- `Motion32TableProbe.java` searched for raw Thumb/ARM callback pointers to
  the candidate functions and exact native/pre-native map byte sequences. It
  found no raw function-pointer table entries for the candidates and no compact
  native transport, nav, or pad-note tables; the few byte-sequence hits were
  incidental ASCII/lookup data.
- `Motion32ConstantSetProbe.java` searched for sparse function/data matches
  containing the native/pre-native map values. It found no function containing
  the full native transport set `0x69/0x6B/0x6D/0x6F`, no function containing
  the full pre-native set `0x66/0x67/0x68/0x69`, and no non-executable data
  windows containing those sets. This argues against a simple switch/table that
  stores the map bytes together.
- The config/control-record subsystem around
  `0x2ee68-0x2fb60`:
  - `FUN_0002ec30(key)` reads a 16-bit value from RAM at
    `0x2000b5d4 + (key + 0x10) * 2 + 2`.
  - `FUN_0002edc4(group, index, offset)` reads bytes from `0x1A`-byte records
    whose active base pointer is stored at RAM `0x2000aa90`.
  - Several temporary Ghidra functions in this address range looked promising
    at first, but they should be treated as suspect until the RP2040 memory map
    is corrected. One apparent jump-table pointer decoded to LVGL/string data
    rather than a real branch target, so the provisional `PROBE_0002f304`
    dispatcher lead is not reliable.
  - `FUN_00022b70` reads keys `0x2c` and `0x30` from this subsystem to build or
    refresh a MIDI/control mapping table, but the writer that changes those
    keys in response to `8F 00 7F` has not been isolated.

## Concrete Event-Path Findings

The most useful firmware data from the follow-up probes is the local
control-event path, not the raw `8F` receiver.

Important correction: the byte at `0x20004291` is now best understood as a
device/protocol variant selector, not the live native-mode latch. The reason is
that its mode `0` branch uses the `F0 08 26 ...` prefix observed from the actual
Motion 32 hardware, while the nonzero branch uses `F0 08 24 ...`. Keep using
this byte to understand Motion-family protocol/scan differences, but do not
claim that `8F 00 7F` directly changes it unless a separate writer is found.

- `FUN_00001e50()` is a one-byte mode getter. It returns `DAT_20004291`.
- `DAT_20004291` is initialized by `FUN_00001e5c()` from persistent/config
  key `0x204` via `FUN_00005df4(0x20005cbc, 0x204, &local_9)`.
- `FUN_000020a4()` is an input parser for a framed SysEx-like byte stream:
  it waits for `0xF0`, matches four bytes from a mode-selected prefix pointer,
  stores payload bytes in `0x200042a0`, and completes on `0xF7`.
- The prefix pointer is selected from the mode byte:
  - mode `0`: `_DAT_20004294 = 0x95f4`
  - mode nonzero: `_DAT_20004294 = 0x95f8`
  - expected prefix length: `DAT_20004292 = 4`
- With the payload-aligned file, those prefixes decode cleanly:
  - mode `0` / Motion 32 branch: `F0 08 26 05`
  - mode nonzero / sibling-device branch: `F0 08 24 05`
- `FUN_000026f4()` uses the same mode byte to set how many relative controls
  are active:
  - mode `0`: `DAT_200045cc = 8`, `DAT_200045ca = 2`
  - mode nonzero: `DAT_200045cc = 9`, `DAT_200045ca = 1`
- `FUN_0000240c()` polls those relative-control state slots at
  `0x20004538`, `0x20004548`, ... and emits deltas through `FUN_00001fb0()`.
  This is the concrete firmware-side explanation for a ninth relative source
  appearing in the host/integrated mode path.
- `FUN_00001fb0(control_id, delta)` writes the internal event stream at
  `0x20004084`:
  - if the current control changes, it writes `control_id - 0x50`
  - then writes opcode `0x15`
  - then writes the relative delta as `delta + 0x40`
- `FUN_00001f6c(control_id, value)` writes opcode `0x14` plus an absolute
  value, and `FUN_00001eec(control_id, value14)` writes opcodes `0x16` and
  `0x36` with the high/low 7-bit halves of a 14-bit value.
- `FUN_00003a14(mode)` initializes the inbound byte queue by calling
  `FUN_00001d28(0x200040a0)`, sets `DAT_20005b60 = 1`, and initializes one of
  two USB/TinyUSB endpoint contexts through `FUN_00005854(...)`.
- A small forced-boundary function at `0x00003ac4` is the concrete inbound
  byte feeder for that queue:
  - if `event[4] == 0x02`, it sets `DAT_20005b60 = 1`
  - if `event[4] == 0x04`, it enqueues `event[8]` into `0x200040a0` with
    `FUN_00001d6c(0x200040a0, event[8])`
- `FUN_00003ab8()` returns `0x200040a0`, and the only recovered consumer of
  that ring is `FUN_000020a4()`. This strongly suggests `0x200040a0` is a
  SysEx/framed-byte queue, not the full channel-voice MIDI receiver.

Additional mode-dependent tables recovered from the payload:

- Button/touch gate table at `0x9620`, 11 slots per mode:
  - mode `0`: `01 01 01 01 01 01 01 01 00 01 01`
  - mode nonzero: `01 01 01 01 01 01 01 01 01 01 00`
- Button/touch bit-mask table at `0x9638`, 11 halfwords per mode:
  - mode `0`: `0004 0008 0010 0020 0001 0002 0080 0100 0040 0200 0400`
  - mode nonzero: `0001 0002 0080 0004 0008 0010 0020 0040 0100 0200 0400`
- Relative selector table at `0x9664`, 9 bytes per mode:
  - mode `0`: `00 03 05 07 01 02 04 06 08`
  - mode nonzero: `02 08 06 05 01 00 07 04 03`

Other mode-byte callers show the same split:

- `FUN_0000234c()` uses the mode-specific gate and bit-mask tables to emit
  absolute on/off events through `FUN_00001f6c()`.
- `FUN_0000240c()` uses the mode-specific relative selector table to emit
  deltas through `FUN_00001fb0()`.
- `FUN_000028d0()` and `FUN_00002b08()` initialize scan/filter state with
  10 channels in mode `0` and 5 channels in nonzero mode.
- `FUN_000030cc()` changes scan geometry/constants:
  - mode `0`: `_DAT_20005a5e = 0x10`, `DAT_20005a60 = 4`,
    `DAT_20005a61 = 2`
  - mode nonzero: `_DAT_20005a5e = 0x20`, `DAT_20005a60 = 5`,
    `DAT_20005a61 = 1`
- `FUN_00003370()` installs different descriptor/config blocks in mode `0` vs
  nonzero mode.
- Small descriptor helpers return mode-specific table addresses:
  - `FUN_000098c4()`: mode `0` -> `0x9dfc`, mode `1` -> `0x9e38`
  - `FUN_000098e4()`: mode `0` -> `0x9d40`, mode `1` -> `0x9d80`
  - `FUN_00009904()`: mode `0` -> `0x9cc4`, mode `1` -> `0x9cd4`
  - `FUN_00009924()`: mode `0` -> `0x9cbc`, mode `1` -> `0x9cc0`
- The main scan loop (`FUN_00009944()` / `FUN_00009e1c()`) handles the two
  analog/touch inputs differently:
  - mode `0`: both `_DAT_200064d4` and `_DAT_200064d6` can become active
    output values (`DAT_200064bd` and `DAT_200064bc`)
  - nonzero mode: `_DAT_200064d4` is routed into the primary active value
    (`DAT_200064bc`) and the second active flag is not driven by that branch

Current status: firmware disassembly still has not named or isolated the exact
internal branch that receives host bytes `8F 00 7F` and `8F 00 00`. What is now
concrete is adjacent but different: a persistent/config byte at `0x20004291`
changes the Motion-family protocol prefix, descriptor/config blocks,
button/touch bit masks, scan geometry, active analog channel count, and
relative-control count/selectors. Because the Motion 32 branch is mode `0`, this
is not the native-command latch. The recovered inbound byte queue explains where
SysEx-like bytes go, but it appears to discard non-`0xF0` bytes while idle;
therefore the `8F` lifecycle message is probably handled earlier at the
USB-MIDI packet/event layer, or in a separate channel-voice path that Ghidra has
not recovered through ordinary call references.

### 2026-07-27 lifecycle receive pass

`Motion32NativeLifecycleProbe.java` added a stricter search for the actual
`8F 00 7F` / `8F 00 00` receive branch. It scored functions for channel-voice
MIDI parsing shape, USB-MIDI note-off CIN (`0x08`), byte-packet indexing, value
`0x7f`, and writes near known control/report RAM.

The exact `0x8f` scalar sites in the payload are now exhausted:

- `FUN_0002064c()` writes halfword `0x08f0`, which is the outgoing Fender SysEx
  prefix bytes `F0 08`, not input status byte `8F`.
- `FUN_0003ab58()` uses `0x8f` only as an error/assertion line or code when a
  UI/callback parameter is null.
- `FUN_0003d600()` is UI/image/layout work; its nearby constants include
  dimensions and flags, not MIDI lifecycle parsing.

The strongest non-exact hits were also not lifecycle handlers:

- `FUN_00003ce8()` / `FUN_00003d5c()` / `FUN_00003dde()` are capacitive or
  analog scan/filter routines feeding `0x200064xx` state.
- `FUN_00004854()` is TinyUSB/endpoint configuration, not inbound MIDI byte
  dispatch.
- `FUN_00002544()` and adjacent `0x20005aXX` callers are analog calibration /
  sensor-state processing.

So the current best firmware model is:

1. USB-MIDI receives a host packet containing `8F 00 7F` or `8F 00 00`.
2. TinyUSB or a compact callback layer decodes it without leaving a literal
   `0x8f` compare/template in application code.
3. The command sets an internal "host attached / integrated surface" state.
4. That state changes which report/control model the device exposes to the host:
   fixed native pad notes, native transport/control identities, host-owned
   screen/LED feedback, and host-owned Scale/Chord behavior.

What this pass did *not* find: a direct firmware write such as
`native_mode = (data2 == 0x7f)`. The practical script implication is unchanged:
send the lifecycle bytes exactly as Studio Pro does, then verify true entry by
observing native transport/control output rather than by expecting any visible
local-device acknowledgement.

## Documentation Drift Found

`Resources/Motion32_Gap_Analysis.md` contained superseded Scale/Chord wording
in the same section as the corrected conclusion. The stale "note generation
remains local" sentence has now been replaced with the current conclusion:
native-mode Scale/Chord menu and note behavior are host-owned.

## Follow-Up Tests

Best hardware capture to close the remaining firmware-behavior question:

1. Capture `Motion 32 Main`.
2. Start from standalone/pre-native state.
3. Send only `8F 00 7F`.
4. Press/turn a few controls:
   - transport buttons
   - pads
   - main wheel
   - Scale/Chord buttons
5. Send only `8F 00 00`.
6. Repeat the same controls.

Expected useful distinction:

- If `8F 00 7F` alone changes transport to the integrated CC map, it is the
  true mode switch.
- If full behavior only appears after the identity request/reply, then the
  firmware has a two-stage host state: mode latch plus identified/armed host.

## Script Implication

The Live script's current handshake shape is still right:

- hello: `8F 00 7F`, then `F0 7E 7F 06 01 F7`
- parse identity manually
- handle `F0 08 26 22 <state> F7` as the Global Settings feedback gate
- release LEDs/screen before `8F 00 00`

One separate code risk remains from the audit: a superseded script instance can
still reach framework `goodbye_messages` through `super().disconnect()`, which
may send `8F 00 00` after a replacement instance has entered native mode. That
is a reload robustness bug in our script, not a firmware uncertainty.
