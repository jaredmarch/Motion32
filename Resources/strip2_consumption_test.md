# Hardware test: does declaring strip 2 consume its pitch bend?

Date: 2026-08-10
Status: ✅ **RUN — answered YES.** Declaring the element consumes the pitch bend; strip 2 no longer
reaches the armed instrument. Position reaches the script once forwarding is set at construction
time. Full findings are in `Motion32_Pads_Banking_and_Strips.md` §5.3b under "RUN, 2026-08-10".

This file is kept as the method, not as an open question. Two things it did not anticipate:

- **`script_forwarding` is not a constructor kwarg** — it must be assigned after construction, and
  **during element construction rather than in `setup()`**, or the strip ends up consumed but
  silent. See Troubleshooting.
- **The contact sensor cannot be consumed at all.** CC `0x7B` is CC 123, All Notes Off, and Live
  acts on it before script forwarding. Touching strip 2 stops held notes and the script cannot
  prevent it.

## The one question

Strip 2 sends pitch bend on channel 1 (zero-based) in native host mode. This is not
configurable — `Resources/FirmwareAnalysis/strip_translation_chain.md` establishes that the
`8F 00 7F` state hard-codes it in `FUN_10102e84`, bypassing the strip assignment record.

So the device *will* send it. The question is whether the script can absorb it.

**Why reading the code cannot answer this.** `_install_forwarding()` computes
`should_consume_event` and passes it to `Live.MidiMap.forward_midi_cc()` as a fifth argument.
`forward_midi_pitchbend()` is called with **three** arguments and the flag is not among them —
verified in `control_surface.pyc` bytecode, `CALL 5` versus `CALL 3`. `ScriptForwarding.exclusive`
and `non_consuming` therefore compile to an identical call for pitch bend. The script cannot
*request* consumption. Whether Live consumes forwarded pitch bend **inherently** lives in its C++
side.

## What changed

| file | change |
|---|---|
| `midi.py` | `TOUCHSTRIP_1_CHANNEL = 0`, `TOUCHSTRIP_2_CHANNEL = 1` |
| `elements.py` | imports `MIDI_PB_TYPE` / `ScriptForwarding`; declares `Touch_Strip_2`, `MIDI_PB_TYPE`, channel 1, `ScriptForwarding.exclusive`, feedback off |
| `__init__.py` | `_install_strip2_probe()` — a value listener capped at 40 events |

**Strip 1 is deliberately untouched.** Its pitch bend already works and is what we want to keep.

## Procedure

1. Copy the folder to the User Library (or it is already there) and restart Live.
2. Create a MIDI track, load any instrument with audible pitch bend response — Wavetable or
   Operator is fine, a synth pad makes the bend obvious.
3. **Arm the track.** Confirm the pads play it.
4. Open `Log.txt` and check for:

   ```
   Motion32 strip2 probe: ARMED — element=..., channel=1, forwarding=...
   ```

   If instead you see `no 'touch_strip_2' element`, the declaration failed — see Troubleshooting.
5. Slide **strip 2** (the right-hand strip) up and down.
6. Note two things independently:
   - **Does the instrument's pitch bend?**
   - **Does `Log.txt` fill with `Motion32 strip2 rx:` lines?**
7. Slide **strip 1** and confirm it still bends the instrument — this must not have regressed.

## Reading the result

| instrument bends? | script receives? | meaning | what to do |
|---|---|---|---|
| **no** | **yes** | 🎉 Live consumes forwarded pitch bend inherently. The defect is fixable in the script. | Close the issue as fixable; build Phase 9 strip 2 on this, with the LED bar and a mapped parameter. |
| **no** | no | Consumed, but the script cannot see it either. Strip 2 becomes inert. | Still fixes the two-benders defect. Decide whether an inert strip 2 beats a duplicate bender. |
| **yes** | **yes** | Forwarded *and* still routed. The framework cannot consume pitch bend. | The defect is structural. Document it; M4L stays the only mod-wheel route. |
| **yes** | no | Declaration did not take effect at all. | Troubleshoot before drawing any conclusion. |

Row 3 is the outcome the bytecode predicts. Row 1 is the one worth hoping for.

## Troubleshooting

**`TypeError: object.__init__() takes exactly one argument` — already hit and fixed.**
`script_forwarding` is **not** a constructor kwarg. `InputControlElement.__init__` names exactly
`msg_type, channel, identifier, sysex_identifier, request_rebuild_midi_map,
send_should_depend_on_forwarding, is_feedback_enabled`; anything else falls through `**k` to
`object.__init__` and the script fails to load. It is a **property with a setter** that assigns
`_script_forwarding` and calls `_request_rebuild` itself, so it is assigned after construction —
which is what `_install_strip2_probe` now does. Recorded here because the same trap will catch the
Phase 9 strip work.

**`no 'touch_strip_2' element` in the log.** The element was not created. Check Log.txt above the
probe line for the real error, and consider the generic `add_element` route the wheel already uses.

**`could not set script_forwarding` in the log.** The test still runs — attaching the value
listener installs forwarding regardless (`script_wants_forwarding` is true when
`_input_signal_listener_count` is non-zero) — but as the default type rather than `exclusive`. For
pitch bend this may not matter at all, since the consumption flag is never passed to Live either
way, but note it when recording the result.

**Nothing in the log at all.** Confirm the script loaded (`Motion32: script setup complete`) and
that native mode was entered — the strips only send pitch bend in the native host state.

**Strip 1 stopped working.** Revert immediately; that is a regression and outranks this experiment.

## Afterwards

The probe is temporary. Once the answer is recorded, delete `_install_strip2_probe`,
`_on_strip2_value` and `MAX_LOGGED_STRIP_EVENTS` from `__init__.py`. Whether the element
declaration stays depends on which row above you landed on.
