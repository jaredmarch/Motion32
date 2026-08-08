# Motion32 Python Code Audit - 2026-07-27

Scope: root-level Python Remote Script modules plus `tests/test_screen.py`, checked against the
current Markdown documentation in `README.md` and `Resources/*.md`.

This audit did not change runtime code.

## Verification Performed

- `python3 -m py_compile *.py tests/test_screen.py` passed: no Python syntax errors in the script files.
- `python3 tests/test_screen.py` ran 106 groups but failed because `xdis` is not installed:
  2660 assertions, 2 failures, both in `test_every_mapped_control_name_exists`.
- The failure is expected by the docs: without `xdis`, the suite refuses to pretend it validated
  framework bytecode control names.
- Standard-library bytecode inspection with Python 3.11 confirmed that
  `ControlSurface.disconnect()` always sends `goodbye_messages`.
- No Live or hardware run was performed in this audit.

## Findings

### High: superseded `disconnect()` can still send native-mode OFF — ✅ **RESOLVED 2026-07-29**

> **Resolution.** `Motion32` now overrides `_send_midi` and drops every outgoing message while
> `self._midi_muted` is set; the superseded branch of `disconnect()` sets that flag before
> `super().disconnect()`, so the framework's goodbye path is muted along with everything else. The
> flag is initialised at the top of `__init__` because the override runs during
> `super().__init__()`. Guarded by `test_a_superseded_teardown_emits_zero_bytes`, which asserts an
> empty sent list against a stand-in that reproduces the real goodbye path, and opens with a
> positive control so it cannot pass vacuously. The misleading "no goodbye side effects" log line is
> gone. **Confirmed on hardware 2026-07-29** — transport arrives on `0x6F` after a reload.
> Original finding below, for the record.


File: `__init__.py`

The code correctly gates LED and screen reset on `runtime.clear(self)`, but it always calls
`super().disconnect()` afterwards:

```python
still_current = runtime.clear(self)
...
self._screen = None
super().disconnect()
```

The file itself documents that the framework sends `goodbye_messages` during
`super().disconnect()`, and the framework bytecode confirms this. Since
`Specification.goodbye_messages = (midi.NATIVE_MODE_OFF_MESSAGE,)`, a superseded old instance can
still send `8F 00 00` after the new instance has entered native mode.

Impact: on script reload, the old instance may kick the device out of native mode even though it no
longer owns the hardware. This contradicts the log text saying "no goodbye side effects".

Recommendation: when `still_current` is false, prevent the framework goodbye from being sent by this
old instance before calling `super().disconnect()`, or otherwise bypass/neutralize the goodbye path.
Add a regression guard that checks not only `_clear_all_leds`, but also `goodbye_messages`.

### Resolved 2026-07-27: wheel push feedback was bound on an output-colliding address

Files: `elements.py`, `skin.py`, `wheel.py`

Earlier in this audit, `Wheel_Push_Button` was declared with normal `add_button(...)` feedback at
CC `0x78`. The docs say `0x78` is wheel push on input, but host-to-device `0x78` is touch-strip 2
LED 9. The wheel halo was already correctly owned separately at `0x1D`, but
`MotionWheelComponent.push_button` still had skin feedback keys `Wheel.Push` and
`Wheel.PushPressed`.

Hardware corroboration from MIDI Monitor, supplied 2026-07-27:

```text
Wheel right: Controller 29 value 1
Wheel left:  Controller 29 value 65
Wheel click: All Sound Off value 127, then 0
```

MIDI Monitor's "All Sound Off" label is the standard CC name for decimal 120, i.e. `0x78`.
In the Motion native protocol that CC is `wheelPush`, matching Fender's `wheelPush` definition.

Impact: today this may be harmless if non-RGB state feedback at `0x78` is ignored. It is still a
collision risk for the future touch-strip implementation, and the skin comment implies the push
button should behave like a normal lit button even though the address map says otherwise.

Resolution: wheel push is now a receive-only element. `elements.py` declares
`MotionInputOnlyButtonElement`, `Wheel_Push_Button` is built with `add_element(...,
create_motion_input_button, CC_WHEEL_PUSH, ...)`, `wheel.py` uses a feedbackless `ButtonControl()`,
and `skin.py` no longer defines wheel-push colours. `tests/test_screen.py` now has
`test_wheel_push_is_input_only` so `0x78` cannot accidentally become writable again.

### Medium: the test suite cannot currently perform its strongest mapping audit

File: `tests/test_screen.py`

The test failure is not a code failure, but it is a release blocker by the project's own rules.
Without `xdis`, mappings against framework components are not checked, including `Transport`,
`Device`, `Device_Navigation`, `View_Control`, `View_Toggle`, `Mixer`, `Undo_Redo`,
`Target_Channel_Strip`, and `Motion_Keyboard`.

Recommendation: install `xdis` in the test environment and rerun until the documented assertion count
is restored. Consider adding a one-line local test command wrapper that checks for `xdis` first.

### Low: `README.md` is stale relative to code and later docs

File: `README.md`

The README says the current milestone is Phase 2 and lists pads, encoder-halo LEDs, LCD soft buttons,
and notification overlays as not yet implemented. The actual code and later docs implement pads,
halos, per-mode soft labels/bindings, and notification overlays.

Impact: a new session reading README first gets an older project state.

Recommendation: update the README summary from the handoff/roadmap state, or point the top of README
at `Resources/Motion32_Ableton_Build_Handoff.md` as the authoritative state.

### Low: stale/inaccurate comments remain in code

Files: `keyboard.py`, `screen_component.py`, `colors.py`

- `keyboard.py` says dead pads are moved to identifiers "at or above 128", but the current strategy is
  own note on `DEAD_PAD_CHANNEL`.
- `screen_component.py` has an unused `_render_listener()` helper and a duplicated color-listener
  comment.
- `colors.py` imports `dim` and `rgb7` but only uses `live_rgb7`.

Impact: no runtime issue observed, but this project leans heavily on comments as executable memory.

Recommendation: clean these while touching nearby code.

## Per-File Audit

### `__init__.py`

Role: Live `ControlSurface`, capabilities, specification, native-mode lifecycle, runtime object
publication, setup binding, redraw, MIDI receive, and teardown.

Matches docs:

- Uses `Motion 32 Main` capability shape and avoids the Control/MCU port.
- Sends native mode ON plus identity request as `hello_messages`.
- Avoids `identity_response_id_bytes` and parses identity replies manually through `receive_midi`.
- Publishes screen/runtime objects before framework component construction.
- Suspends screen/LED output until `setup()` makes `_send_midi` usable.
- Binds `Motion_Screen`, `Motion_Wheel`, `Motion_Keyboard`, and custom transport through
  `component_map`.
- Clears LEDs and screen to the documented white/visible teardown state when still current.

Issues:

- ~~High: superseded instances still reach framework `goodbye_messages` through
  `super().disconnect()`.~~ **Resolved 2026-07-29** — `_send_midi` is overridden and muted for a
  superseded instance.
- Broad `except Exception` blocks are mostly defensive around Live callbacks and teardown. They log
  usefully in most places.

Efficiency:

- Good. Expensive redraws are delegated to diffed models. Startup suspension prevents half-cached
  sends.

### `midi.py`

Role: central wire constants for SysEx, CCs, pads, LEDs, reset values, and status bytes.

Matches docs:

- Constants match the control-surface definition: native messages, identity request, Fender/Motion
  SysEx header, screen message IDs, global-settings state, transport CCs, pad notes 36-67, and reset
  values.
- Explicitly documents address overlaps and pad state vocabulary.

Issues:

- No runtime issue found.
- Future-phase constants are present for unbound controls. That is intentional and useful for
  teardown.

Efficiency:

- Pure data. Good.

### `protocol.py`

Role: SysEx framing, identity parsing, global-settings feedback suspension, and protocol send gate.

Matches docs:

- Firmware offsets 11/12/13 are implemented directly.
- BCD-style firmware decode matches the docs.
- Screen template and screen update SysEx are gated during Global Settings.
- Consumed identity/global-settings SysEx messages are not forwarded to the framework.

Issues:

- Low: `parse_identity_reply()` accepts any Universal Identity Reply shape and does not verify Fender
  manufacturer/device IDs before logging firmware. On the Motion-only port this is probably fine, but
  stricter matching would better reflect the docs.

Efficiency:

- Good. Send gate is constant-time and avoids redundant logging unless verbose is enabled.

### `elements.py`

Role: physical control declarations and custom `MotionEncoderElement`.

Matches docs:

- Encoder matrix uses `add_matrix` with `create_motion_encoder`, not the helper wrappers that hard-code
  factories.
- Encoder and wheel elements suppress outgoing writes so LED/halo addresses are not stomped.
- Pads are NOTE elements in two rows of sixteen, lane order preserved.
- Shift-modified transport controls and Shift+Song are declared.
- Edit/Mix/Add/Scale/Chord/etc. constants exist in `midi.py` but unimplemented mode buttons are not
  mapped, matching the roadmap discipline.

Issues:

- Resolved: `Wheel_Push_Button` is now input-only at `0x78`, so the future touch-strip 2 LED 9 writer
  will not fight wheel-click feedback.

Efficiency:

- Good. Uses framework element declarations rather than runtime per-event routing.

### `mappings.py`

Role: declarative component/control assignments.

Matches docs:

- Global transport, Undo, target solo/mute, keyboard, and screen touch bindings are present.
- `Main_Modes` is a strict radio with Song and Plugin only.
- Song mode maps all eight encoders from one source table.
- Plugin mode maps encoders to `Device`, wheel to bank scroll, Up/Down to parameter banks, Left/Right
  to track navigation, Preset Up/Down to device navigation, wheel push to wraparound device selection.
- Edit and Mix remain deliberately unbound.

Issues:

- No code issue found, but full framework-name validation is blocked until `xdis` is installed.
- Device lock, device on/off, bank select, A-H, Mix, Shift pad overlay, touch strips, Scale, and Chord
  remain future work as documented in the roadmap.

Efficiency:

- Good. Static declarative mapping, no runtime churn.

### `transport.py`

Role: subclass of framework `TransportComponent`, adding record, loop soft toggle, and
back-to-arrangement.

Matches docs:

- Subclasses the framework component rather than replacing it.
- Adds only the controls the framework lacks or cannot bind twice.
- Uses listenable song properties to refresh LED color state.

Issues:

- Broad exception swallowing in `_set_color()` and back-to-arrangement press is defensive but quiet.
  Acceptable for Live API variance, but if a state LED does not work this can hide why.

Efficiency:

- Good. Event-driven listeners only.

### `wheel.py`

Role: wheel push behavior: select next device with wraparound.

Matches docs:

- Turning is left to framework mappings.
- Push selects next device and wraps at end.
- Does not report press state for wheel halo purposes.

Issues:

- The behavior is fine, and the `ButtonControl` is now feedbackless so it does not participate in the
  `0x78` output collision.

Efficiency:

- Good. Device list scan is tiny and occurs only on click.

### `display.py`

Role: framework-free screen model, diffing, Template 0 view, Template 3 view.

Matches docs:

- Desired/sent split is implemented.
- `invalidate()` forgets sent state.
- `flush()` always selects template before element updates.
- Reset-to-defaults uses empty/white/visible/regular values, not black/hidden.
- Template 0 uses one tile text element for label/value; Template 3 uses label and value lines.
- Type guards reject wrong content/view pairings.

Issues:

- No runtime issue found.

Efficiency:

- Good. Flush scans the desired dict, but only sends diffs. The unconditional flush strategy is a
  deliberate and documented correctness tradeoff.

### `screen.py`

Role: named screen address map and factory palette.

Matches docs:

- Templates 0, 1, 2, and 3 are represented.
- Main, Params, Menu, and Mixer address helpers line up with the documented screen map.
- Palette uses the shared `rgb7()` conversion layer.

Issues:

- No runtime issue found.
- Template 2 has address helpers but no renderer yet, matching Mix being future work.

Efficiency:

- Pure data. Good.

### `notification.py`

Role: transient two-field notification bar on Template 1.

Matches docs:

- Claims all Template 1 elements needed to avoid firmware placeholders.
- Uses two header slots for title/value.
- Hides menu body and footer labels.
- Diff-friendly, so repeat notifications are cheap.

Issues:

- No runtime issue found.
- Future Menu view must coordinate ownership carefully because it will share Template 1.

Efficiency:

- Good. Static chrome is diffed away after first use.

### `screen_component.py`

Role: content source for screen, encoder/wheel/pad LED orchestration, listeners, notifications.

Matches docs:

- Defers Device-component binding until after setup.
- Follows mode selection, mapped parameters, parameter values, selected track, track color/name,
  Live view, tempo/loop/signature, encoder touch, and notifications.
- Maintains one predicate ordering for notification vs Plugin vs Song views.
- Starts live refresh only while transient values are shown.
- Uses track color for Plugin header, Song centre bar, and root pads.
- Refreshes LEDs through shared group list.

Issues:

- Low: `_render_listener()` is unused.
- Low: duplicated color-listener comment in `_rebind_track()`.
- ~~Potential future issue: `_pad_root_offset` exists but no A-H binding updates it yet … a future
  A-H implementation must drive both keyboard root offset and screen/pad LED root offset from one
  source.~~ **Resolved 2026-07-29 by removal.** Phase 6 deleted `_pad_root_offset` rather than
  keeping it in step: the keyboard reports the pad roles it derives from its own pitch list, so the
  screen component has no layout state of its own. Guarded by
  `test_roles_come_from_the_pitch_list_not_a_second_offset`.

Efficiency:

- Mostly good. Rendering and LED refresh are intentionally frequent but diffed. The 20 Hz refresh is
  scoped to visible transient values.

### `leds.py`

Role: cached/diffed LED groups for CC-addressed halos/wheel and NOTE-addressed pads.

Matches docs:

- State and RGB are diffed separately.
- Pads use note statuses and release state twice.
- Normal dark state is off+black, while teardown release is off+white.

Issues:

- No runtime issue found.

Efficiency:

- Good. Minimal traffic on color-only changes and no redundant state bytes.

### `palette.py`

Role: single 8-bit to 7-bit color conversion layer plus Live object color helpers.

Matches docs:

- `rgb7()` implements `>> 1`.
- `live_rgb7()` treats black `0` as a real color, not missing.
- `text_on()` uses weighted luminance for readable text.
- `dim()` supports pad/halo brightness by color rather than invalid pad dim state.

Issues:

- No runtime issue found.

Efficiency:

- Pure and cheap. Good.

### `colors.py`

Role: framework `ComplexColor` creation and named skin colors.

Matches docs:

- ComplexColor carries RGB parts plus state byte.
- Dynamic Live-object color path uses `live_rgb7()`.
- Memoizes dynamic RGB colors.

Issues:

- Low: imports `dim` and `rgb7` but does not use them.

Efficiency:

- Good. Dynamic color memoization avoids object churn.

### `skin.py`

Role: skin key definitions for framework components and custom controls.

Matches docs:

- Supplies ComplexColor keys for framework defaults that would otherwise be BasicColors.
- Transport, ViewControl, Device, Mixer, Keyboard octave colors match documented behavior.

Issues:

- Resolved: wheel-push skin colours were removed because the click has no LED feedback by design.

Efficiency:

- Static data. Good.

### `formatting.py`

Role: screen text compaction, ASCII conversion, value truncation, parameter value formatting.

Matches docs:

- `compactify()` implements the documented factory algorithm shape.
- `to_ascii_bytes()` guarantees printable 7-bit bytes.
- `truncate_value()` deliberately avoids stripping minus signs from values.

Issues:

- Low: `MAXCHARS_PARAMS_VALUE` is currently not used by runtime code. This may be retained as a
  source constant, but it is not part of the active rendering path.

Efficiency:

- Good. Simple regex and string operations.

### `pads.py`

Role: framework-free pad layout model for Keys layout.

Matches docs:

- Bottom lane white keys, top lane black keys/gaps.
- Deadness derives from `pad_pitches()`.
- Negative root offsets are handled correctly through `divmod`.
- Root and dead indices follow the documented capture.

Issues:

- No runtime issue found.
- The module is intentionally diatonic; Scale/Chord will need the separate generator described in
  `Motion32_Scale_and_Chord_Engine.md`.

Efficiency:

- Good. Recomputed only on layout changes.

### `keyboard.py`

Role: playable pad keyboard, octave buttons, held-pad reporting, note translation.

Matches docs:

- Uses `PlayableComponent`, not Python note generation.
- Keeps pads playable and listenable.
- Dead pads are claimed on a separate channel and set to listenable mode.
- Recomputes both note translations and control modes on layout change.
- Octave notifications and LED color model match the docs.

Issues:

- Low: stale docstring in `_update_note_translations()` says dead pads move to identifiers at or
  above 128. The actual current strategy is own note plus `DEAD_PAD_CHANNEL`, and that is the right
  strategy according to the module header.

Efficiency:

- Good. No per-note Python generation; only press/release bookkeeping for LEDs.

### `parameters.py`

Role: normalize the framework Device component's current bank into eight display/control entries.

Matches docs:

- Handles `ParameterInfo(parameter, name)`.
- Pads to exactly 8 entries.
- Uses framework bank name and device reference when available.

Issues:

- No runtime issue found.
- Broad exceptions are intentional defensive handling around Live object invalidation.

Efficiency:

- Good. Reads only current bank on framework notifications or mode entry.

### `runtime.py`

Role: owner-scoped module state for screen/view/parameter objects.

Matches docs:

- `publish()` and `clear(owner)` implement ownership guard.
- Prevents old instances from clearing new runtime references.

Issues:

- No issue in this file. The remaining reload hazard is in `__init__.py`'s framework goodbye path,
  not in runtime ownership.

Efficiency:

- Pure module state. Good.

### `tests/test_screen.py`

Role: offline test and structural guard suite.

Matches docs:

- Guards many actual historical failure modes: screen addresses, teardown values, mapped control
  names, handler arity, pad layout, LED diffing, reload ownership, notification ownership, etc.
- Correctly fails when `xdis` is unavailable rather than silently skipping framework checks.

Issues:

- Current environment does not have `xdis`, so the suite cannot go green here.
- Existing superseded teardown test checks reset calls are guarded, but not that old instances avoid
  sending `goodbye_messages`.
- `test_wheel_push_is_input_only` now checks that wheel-push feedback cannot write to colliding output
  address `0x78`.

Efficiency:

- Large but appropriate for this project. Its AST checks are targeted at Live-only failure modes that
  cannot be imported offline.

## Documentation Alignment Summary

Most later docs align with the code, especially:

- `Motion32_Ableton_Build_Handoff.md`
- `Motion32_Build_Roadmap.md`
- `Motion32_Implementation_Notes.md`
- `Motion32_Control_Surface_Definition.md`
- `Motion32_Pads_Banking_and_Strips.md`

The main stale file is `README.md`. It should be refreshed after the teardown and wheel-push findings
are resolved, because it currently mixes modern implementation detail with an old milestone/footer.

## Suggested Next Fix Order

1. Fix superseded `disconnect()` so old instances cannot send native-mode OFF.
2. Add a regression test for that goodbye-message path.
3. Install `xdis` and rerun `python3 tests/test_screen.py`.
4. Clean stale comments/imports.
5. Update `README.md` to match the handoff/roadmap state.
