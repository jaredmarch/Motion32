# Motion32 — Ableton Live 12 Remote Script

> ⚠️ **Read this before installing.** This script was written largely by AI, working from a
> reverse-engineering of how PreSonus Studio Pro drives the Motion 32. It sends **undocumented
> SysEx to your hardware** and has [known open bugs](https://github.com/jaredmarch/Motion32/issues),
> including an active input defect on touch strip 2. It is not affiliated with, endorsed by or
> supported by Fender or PreSonus. Use at your own risk.

Native-mode integration for the Fender Motion 32 on the **`Motion 32 Main`** port.
DAW Mode must be **Off** — the device's separate Control/MCU port is intentionally unused.

**State:** four modes — **Song, Plugin, Mix and Scale** — plus the screen engine, the colour system,
the pads as a playable keyboard, Octave ±, A–H banking, the notification bar and the **Shift pad
overlay**. Mix mode is complete: strips, Pan, **Sends** and **meters**.

> The authoritative current state is `Resources/Motion32_Ableton_Build_Handoff.md`. This README is
> the *behaviour contract* — what the controller does and why — not a status page.

## What works

**Connection**
- Enters native host mode with `8F 00 7F`, leaves with `8F 00 00`
- Sends the Universal Identity Request as a hello message (matching Studio Pro's startup)
- Parses the identity reply manually — firmware from **fixed offsets 11/12/13**, BCD-style decode
- Watches `F0 08 26 22 <state>` and suspends *all* screen output while the device's
  Global Settings screen is open, then invalidates and fully redraws on close

**Transport** (global — works in every mode)
- Play / Stop / Record / Tap, with source-accurate LED colours and the dim(63)/full(127) model
- Shift+Play → Loop, Shift+Stop → Undo, Shift+Record → Capture MIDI, Shift+Tap → Metronome
- `transport.py` **subclasses** the framework `TransportComponent`, so Song mode inherits its
  position / loop / tempo / cue encoders. Only `record_button` is ours — the framework has none.
  Undo is the `Undo_Redo` component.

**Modes — the Plugin button reveals the device view**

| Button | Mode | Encoders | Left / Right | Up / Down |
|---|---|---|---|---|
| **Song** (default) | `song` — **Template 3** | tempo · position · loop start · loop length · H zoom · V zoom · cue · cue volume | prev / next track | prev / next scene |
| **Plugin** | `plugin` — **Template 0** | 8 device parameters | prev / next **track** | parameter **bank** |
| **Mix** | `mix` — **T2** / **T0** | 8 volumes · 8 pans · **8 sends** (a track × send grid) | page the session **ring** by 8 | — |
| **Scale** | `scale` — **Template 1** | — (the wheel scrolls the scale list) | — | — |

**Scale** is left by pressing any other mode button, or by **Control**, which returns to whichever
mode you came from. Control is not a fourth destination — it has no screen of its own.

> ⚠️ **Song encoder 4 is `loop_length_encoder`, and the screen labels it `Loop End`.** The label is
> wrong twice over: the control changes the loop's *length*, and the readout formats that length
> through `_format_beats()` as if it were an absolute position, so a 2-bar loop starting at bar 3
> reads `3.1` rather than either `2` bars or bar 5. Recorded as open — see
> `Motion32_Ableton_Build_Handoff.md` §7.

The **big wheel** scrolls parameter banks in Plugin mode (`bank_scroll_encoder`), and **clicking it**
selects the next device on the track, wrapping at the end (`wheel.py` — the framework's
`Device_Navigation` stops at the ends, so the wrap is ours). It is unused in Song mode.

Its halo is **lit for the whole of any mode that uses it** — Plugin and Mix — with no press
highlight and no reaction to scrolling. A light that changes while you're using the control gives every one of
those transitions a chance to leave it dark, which is what it did. The wheel is a mode-level
indicator, so mode is the only thing that moves it.

**Strict radio** — pressing a mode button goes straight to that mode, with no toggling. Plugin briefly
toggled back to Song on a second press, which reads fine with two modes but has no well-defined
destination once Edit and Mix exist, so it was removed. Exactly one mode button is lit at all times.

In Plugin mode, **Preset Up / Down** steps the device selection along the track's chain, and entering
the mode brings Live's device chain up in the Detail pane — otherwise you can be controlling a device
you can't see.

**Soft buttons are per-mode**, not global — so any mode that doesn't claim one leaves it dark and
unlabelled. Song mode uses: top row 3 = **Loop**, 4 = **Back to Arrangement**; bottom row =
**Sess/Arr · Browser · Cue Mrk · Clip/Dev**. Plugin mode claims none yet. Solo and Mute are global and
act on the focused track via `Target_Channel_Strip` (solo yellow, mute red).

Two of those needed controls the framework doesn't have: `loop_toggle_button` (the framework's
`loop_button` is already on Shift+Play, and one control can't bind two elements) and
`back_to_arrangement_button` (nothing in the framework references `back_to_arranger` at all). Both live
on our `TransportComponent` subclass, with LEDs reflecting real state.

**Why buttons weren't lighting.** A **missing** skin key does not raise and does not log — from
`Skin.__getitem__`, it becomes `BasicColors.ON` if the key ends in `on`/`pressed`/`enabled`/`selected`
and `BasicColors.OFF` otherwise. A `BasicColors` is a state byte with no RGB triple, so on the Motion
it renders colourless. Note the asymmetry, because it is what makes this hard to see: the `On`/`Pressed`
half still lights (in whatever colour the last mode left on that address) while its resting partner
writes state 0 and goes **dark**. The symptom reads as "this button only works while I hold it".

Four namespaces have no usable framework default and must be declared in `skin.py`: `ViewControl`,
`Device`/`Device.Bank`, `Session` and `UndoRedo` — plus `ModifierBackground`, whose keys are *computed*
from the component's own name (`Modifier_Background` → `ModifierBackground.Shift`) and so cannot be
found by grepping the framework for string literals. Two guards in the suite now check this: one
derives every namespace a bound component asks for, the other pins the exact keys per mapped control.

**Mix mode — Template 2**

Eight channel strips: number, name on the track's own colour, and a fader driven by the volume.
The strips come from the **Mixer component**, not from `song.visible_tracks`, so the view follows
the session ring rather than the first eight tracks. An absent track is greyed, not hidden.

> ⚠️ **Template 2 is pure strips — no header or title zone at all**, unlike Templates 0, 1 and 3.
> There is nowhere to put a mode name or a global readout, and **no pan element**: the strip
> vocabulary is number / fader / mute / solo / label / two meters. Pan can be bound to an encoder
> but cannot be shown here.
>
> ⚠️ **`MIXER_CHANNEL_LABEL` has `text` but no `visible`.** It is the one text element on this
> device that cannot be hidden, so it must always be given a string — an empty one blanks it.

**Meters (Phase 7c)** — the one polled thing in the whole script.

Everything else here is event-driven, on the rule that every fact on screen needs an event. Meters
are the documented exception, and for the opposite of the usual reason: `output_meter_left` *is*
observable, but it fires far faster than any rate the screen can use, so a listener would flood the
diff to produce a picture no better than 10 Hz gives.

**10 Hz, matching the factory.** A Studio Pro capture measured frame intervals of 96–117 ms, so the
rate is sufficient by demonstration rather than by guess. **Live does the ballistics** — the capture
shows its host still decaying a meter six seconds after a note-off while the device just renders the
numbers it is handed — so there is no smoothing code anywhere in this script. And the factory does
*not* diff (it repeats an unchanged `04` across five consecutive frames), so we send **fewer**
messages than Studio Pro for an identical picture.

- `output_meter_left` / `output_meter_right`, Live's smoothed momentary peak pair, scaled onto the
  element's 0–127. `output_meter_level` (the 1 s held peak) is unused: there are exactly two meter
  elements per strip and they are L and R, so a hold marker would cost a channel.
- **A track that cannot make audio gets no meter at all.** A MIDI track with no instrument has
  `has_audio_output == False` and reads 0.0 for ever; three permanently flat strips out of eight
  reads as a bug rather than as silence, so those elements are hidden outright.
- **The bar is green / amber / red**, and the banding is a traffic decision rather than a style one.
  A screen element takes one colour and one value, so a smooth gradient would mean re-sending the
  colour every frame and *doubling* the meter traffic. Quantised, the colour only becomes a
  different payload at a threshold crossing, so the diff drops it on almost every frame: a signal
  steady in the green costs zero colour messages.
- The loop is gated on **Mix mode and the Volume page** — the Pan page draws Template 0, which has
  no meter element — and it is killed on teardown.

> ✅ **Confirmed on hardware 2026-08-03**, which also settles a question the map could not.
> `METER_LEFT_BACKGROUND` is the only `_BACKGROUND` in the whole 181-element map that shares an
> element with a `value`, so it might have been the *trough* rather than the bar — in which case
> the banding would have coloured the empty space above the signal. It colours the **bar**. The
> thresholds `METER_AMBER_AT = 0.76` / `METER_RED_AT = 0.92` read correctly against Live's own
> meters and stay as they are.
>
> **A deliberate divergence from the factory:** Studio Pro colours each meter with its **track's
> fill colour**. We use signal level instead. The track is already identified three other ways on
> this screen — the name swatch, the encoder halo and, in Plugin mode, the header — so spending
> the meter's colour on identity too would say nothing new, whereas level is information the
> screen carries nowhere else. Switching back is a one-line change in `meter_colour()` if it ever
> reads better.

**The wheel halo is lit in Plugin *and* Mix** — every mode that gives the wheel a job. Still
strictly mode-level: a halo that changes while you're turning the control gives every transition a
chance to leave it dark, which is what it used to do.

**Two pages, and the big wheel moves between them** (Phase 7b). Page 1 is Volume on Template 2's
faders; page 2 is **Pan** on Template 0's eight arcs — Template 2 has no pan element at all, so the
page borrows the encoder-tile view, and an arc reads a pan better than a number anyway. The pages
**wrap**, so a third (sends) can be added with no change to the paging.

> ⚠️ **Nothing in `ableton.v3` switches modes from an encoder.** `ModesComponent` offers only
> `cycle_mode_button` (a button) and `PageComponent.set_scroll_encoder` pages a `Pageable`, not a
> mode set. So `mixpages.py` subclasses **`ScrollComponent`** — the same base `Device_Navigation`
> uses, and the thing that already decodes a relative encoder into a direction.
>
> ⚠️ **`Mix_Pages` is declared `"enable": False`.** A modes component is enabled by default
> (`_setup_modes_component` ends with `set_enabled(modes_config.pop("enable", True))`), and an
> always-on page layer would hold the eight encoders in Song and Plugin mode too. Mix mode enables
> it by naming it as a mode part — a component named with no mappings resolves to the component
> itself, which the mode system enables on enter and disables on leave. That is the general recipe
> for a **nested** mode set.
>
> The encoders are bound *in the pages*, never at Mix level — only a layer swap can rebind them.

**Touching an encoder reveals the value on both pages, but they end it differently.**

| Page | Where the value appears | How it ends |
|---|---|---|
| **Volume** (T2) | the strip's **track name**, replaced for the duration | **on release**, immediately |
| **Pan** (T0) | the tile's single text element | after the framework's **0.75 s** |
| *(Plugin, T0)* | *the tile's single text element* | *after 0.75 s* |

Both pages reveal because both templates give one text element per strip or tile, so a name and a
value must share it. The *ending* differs because the surrounding screen does. On Pan and in Plugin
mode the value may be uncovered by a touch that is never followed by a turn, so it needs a moment to
be read. On the Volume page the fader is on screen permanently — the number is a precision aid while
your finger is down, and holding it after release would hide the track name for nothing.

> That distinction is per **page**, not per mode; making it per mode is what made the Pan page
> silent on touch in the first place.
>
> ⚠️ **The Volume reveal is derived from the touch, not stored.** `MixerStrip.show_value` reads
> `_touch_held` directly, so there is no flag to clear and no timeout to miss — which is what makes
> "no timeout" safe rather than merely untested. It deliberately does **not** reuse
> `_showing_value`, which carries the 0.75 s revert; that is the roadmap's standing warning about
> one event source with two opposite meanings.
>
> The **focus** is untouched by any of this and still persists — focus is the track *selection*,
> which is exactly why the roadmap insisted the two not share a mechanism.

Live formats a pan as `50L` / `C` / `50R` through `str(parameter)`, so the bipolar reading comes
free, and a volume as `-12.345 dB`. Both go through `truncate_value()`, never `compactify()` — the
latter strips hyphens and would render every attenuation on the mixer as a boost. The Pan page's
centre label takes the selected track's colour, marking focus the way the header does.

> 🐛 **The unit is the last thing sacrificed, not the first.** `truncate_value` used to shorten by
> keeping only the leading token, so at the strip label's 8-character budget `-6.00 dB` kept its
> unit and `-12.00 dB` became `-12.00`. Every level below -10 dB lost its `dB`, which reads as a
> bug and leaves `-70.00` genuinely ambiguous. It now spends precision and whitespace first:
>
> | Input | 8 chars (strip) | 7 chars (tile) |
> |---|---|---|
> | `-6.00 dB` | `-6.00 dB` | `-6.00dB` |
> | `-12.00 dB` | `-12.00dB` | `-12.0dB` |
> | `-12.345 dB` | `-12.35dB` | `-12.3dB` |
> | `-100.00 dB` | `-100.0dB` | `-100 dB` |
>
> ⚠️ **Rounding alone would not have fixed this.** Live already sends two decimals, so
> `-12.00 dB` is over budget by exactly the space — closing that up is what saves it. Worth
> knowing because "cap the decimals" is the obvious fix and it ships the bug.

> ⚠️ **The arc itself cannot be bipolar.** `MAIN_ENCODER_ENCODER[n]` takes a single 0–127 `value`
> with no fill-mode attribute — the firmware draws one arc style, filling from one end. Centre pan
> therefore reads as a half-filled arc, and there is no host-side way to change that. (Contrast the
> *touch strips*, where the firmware does expose bipolar and fill modes — see
> `Motion32_Pads_Banking_and_Strips.md` §5.4.) The numeric `C` / `50L` / `50R` on touch is the
> honest readout.

**A light track colour darkens its swatch.** `MIXER_CHANNEL_LABEL` has a `text` attribute and
nothing else — **no `color`** — so the firmware picks the label's colour and it is light. `text_on()`,
which keeps the Plugin header and Song centre bar readable by flipping the *text*, has nowhere to
write. So `palette.darken_under_fixed_light_text()` pulls a light swatch below the readable
threshold, keeping the hue: white 127 → 47, pale yellow 118 → 47, while a deep blue at 26 passes
through untouched. Where the text colour *is* ours, keep using `text_on` — flipping the text
preserves the track's real colour, which is the point of showing it.

**Focus is the selection.** Touching an encoder in Mix mode **selects that strip's track**, so
Solo and Mute — which already follow the target track via `Target_Channel_Strip` — act on the strip
you last touched, and Live's own highlight agrees with the screen's. The focused strip is marked by
brightening its name swatch to the factory selection blue, because Template 2 has no ring and no
header to put focus anywhere else.

> The roadmap warned that this focus must **persist**, not time out, and specifically not reuse
> Plugin mode's `ACTIVE_PARAMETER_TIMEOUT` — "the same event source with opposite semantics, which
> is exactly the kind of reuse that produces a subtle bug". Selecting the track sidesteps it rather
> than managing around it: a selection persists by definition, and the on-screen mark is *derived*
> from it rather than stored, so there is no second copy to drift.

**Left / Right page the session ring by eight.** ⚠️ This first shipped on `View_Control`'s
`prev/next_track_button`, which moves Live's *selected track* one at a time and never touches the
ring — one wrong component, three symptoms: the strips stayed put, only one track looked
highlighted, and Solo/Mute crawled with the selection instead of following the touched strip. It is
`Session_Navigation`'s **page** buttons; its plain `left_button`/`right_button` scroll by one, which
is the behaviour that was wrong.

**The eight soft buttons arm the eight strips** in Mix mode — red when armed, dark when not.

> ⚠️ **If a track will not arm, check its input before suspecting the script.** Live silently
> refuses to arm an **audio track with no input selected** — and `track.can_be_armed` still reads
> `True`, because it reports track *type* (not a group, not a return), not whether Live has anywhere
> to record from. This cost a long debugging detour: MIDI tracks armed, audio tracks did not, and it
> looked like a control-binding fault. **Try the mouse first** — if Live won't arm it either, it
> isn't us.

The LED comes from Live: `MixerComponent._update_arm_button` listens to the track's own `arm`, so arming
with the mouse lights the button and there is no script-side toggle to fall out of step. The soft
buttons are declared as a **matrix** (`Soft_Buttons`) because a plural control needs something
iterable; Song mode still binds them singly through `soft_buttons_raw[i]`, the same idiom the
encoders use. Declaring a matrix *and* eight separate buttons would put two elements on each CC.

**Everything on the Mix screen has a listener.** Per strip: `mixer_device.volume` (the fader),
`mute`, `solo`, `name` and `color`; plus the session ring's own `offset` and `tracks`. The ring
listeners also *re-point* the per-track ones, because paging moves the tracks out from under the
strips.

> 🐛 **Without those, the screen was right but stale** — turning an encoder moved the volume in Live
> and the fader didn't follow; paging didn't repaint. Touching another encoder appeared to fix it,
> because a touch selects a track and *that* had a listener. Same shape as "the track name updates
> sometime later" and "bank changes never repainted": every fact on screen needs an event. The suite
> now checks it **field by field** off `MixerStrip`'s own dataclass fields, so adding a field without
> a listener fails rather than shipping.

**Encoder halos take the track colours in Mix mode** — eight strips, eight colours, so the ring of
lights says which tracks you are holding without looking at the screen. An empty strip is dark; a
track with no colour falls back to the row colour rather than vanishing.

`volume_controls` in `mappings.py` is plural and it is not a typo: `MixerComponent.__getattr__`
catches any `set*` name and returns `partial(self._set_strip_controls, name[4:-1])`, dropping
`set_` and the trailing `s`, then looks the singular up on **each channel strip**. Unusually for a
Layer name, a typo here fails loudly — `getattr(strip, "volumes_control")` raises at bind time.

**Encoder halos** are ours to drive — no framework component binds them. Three colour models, one per
mode, each saying what the eight encoders *are*:

- **Song** — the fixed Song purple. There is nothing track-shaped to follow.
- **Plugin** — eight facets of one device, so one colour for the row: **the owning track's colour**,
  the same colour the header bar wears. Falls back to the factory blue for an uncoloured track.
- **Mix** — eight strips, so eight colours: each halo takes its own strip's track colour.

Plus **white while an encoder is touched**, and dark for an unassigned slot. Cached and diffed like
the screen (`leds.py`).

> The Plugin colour comes from the same `_plugin_device()` / `_plugin_header_track()` pair the header
> uses, deliberately: derive it twice and a halo eventually wears one track's colour while the bar
> above it names another.

> ⚠️ **A halo has no address of its own — it lives at the encoder's own CC**, so every byte the
> framework's element sends lands on the light. Two paths write there, and only one is a flag:
> parameter feedback (`is_feedback_enabled=False`) and **element reset** (`install_connections()`
> calls `reset()`; `reset_state()` sends the off value) — which fires on every layer grab, i.e.
> every mode change.
>
> The fix is **exclusive ownership, not racing**: `MotionEncoderElement` in `elements.py` subclasses
> `EncoderElement` and drops its outgoing writes (`send_value` / `send_midi`), keeping all of its
> input behaviour and internal bookkeeping. `leds.py` is then the only writer of those addresses.
> Both go through a **generic** helper: the encoders via `add_matrix(..., element_factory=...)` and
> the wheel via `add_element`. ⚠️ `add_encoder_matrix` / `add_button_matrix` / `add_encoder` all
> **hard-code the factory** and forward it, so passing your own is a duplicate keyword and the whole
> script fails to load — the same trap as `channel=`. Only `add_matrix` and `add_element` accept one.
>
> An earlier attempt re-asserted the LEDs on a timer instead. Don't go back to that — it flickers,
> and anything without an event to hook wins until the next beat, which is why turning and clicking
> the wheel kept knocking its light out.
>
> The diagnostic that identified the reset path: **encoder 8 kept its colour while 1-7 went dark.**
> Encoder 8 is a `MappedControl` (cue volume), whose reset re-sends the parameter value; 1-7 are
> `StepEncoderControl`s, whose reset sends zero.
>
> A Studio Pro capture confirms the model exactly — halos `0x0E`-`0x15` and wheel `0x1D` set to
> state 127 with RGB `(0, 52, 102)` = `#0069CC` — and shows Studio Pro **never** writing state 0 to
> a halo.

**Notification bar** — a generic transient overlay on **Template 1**, up for 1 s, outranking
whichever mode is showing. Two fields: a label and the value it changed to. Octave was the first
caller (`Octave` / `+1`, and `0` at rest — the factory sends a bare `0x30`, not `+0`) and A–H
banking is the second (`Root` / `-2`); scale/root and tempo want the same shape. Both
offsets render through one `signed_label()` — naming it for one of two callers is how a second copy
gets written, and two copies of that rule would eventually disagree about rest.

> ⚠️ **An element you never write is not blank — it shows whatever the firmware shipped in it.**
> The first hardware run drew the device's own `MenuItem0`…`MenuItem5` placeholders straight
> through the bar, from twelve Template 1 elements the renderer had not claimed. Every view must
> claim *every* element on its template; the suite now derives that list from the template map.

Reconstructed byte-for-byte from a Studio Pro capture, with one deliberate difference: Studio
Pro restores Template 1 and repaints the whole base template on the way out, about 65 messages
per press. Its renderer does not diff; ours does, so after the first showing a notification
costs **two** messages and dismissing it costs **one**. That relies on the device keeping each
template's element state while another is displayed — which the Song ↔ Plugin switch already
proves on hardware.

**A–H pad banks** move where the root sits. A strict radio of eight resting on **E**, which leaves
four steps down (D C B A) and three up (F G H) — a bank resting at one end would leave half the
buttons dead until you moved. One step is **one scale degree** — one pad along the bottom row, so
pad 1 takes over what pad 2 was playing. Pressing a bank pops
`Root` / the signed offset on the notification bar, on every press — including a press that changes
nothing, because a button that answers only sometimes reads as broken.

> ⚠️ **The bar's four fields are soft-button labels, not free text.** Each is
> `MENU_HEADER_BUT_TEXT[n]`, anchored over its physical button across the screen width, and the
> title sits in slot 0 — the leftmost. The practical budget is about one button wide, **6–7
> characters**, not the `MAXCHARS_MENU_BUTTON = 16` the element accepts. This first shipped as
> `Root Shifted` and ran off the left edge of the screen. `Octave` is 6 and has always fitted.

`pads.bank_step()` is deliberately **unitless** — it returns −4…+3 and says nothing about what a step
is worth. `keyboard.DEGREES_PER_BANK_STEP` is the conversion. Scale mode (Phase 10) keeps the same
meaning — `scales.locked_pitches` takes the same `degree_offset` — so one row of eight buttons
serves the piano and every scale without a mode-dependent handler.

> ⚠️ This used to add "even though both rows are lit in Scale mode". **That was wrong.** The
> factory's Scale layout puts the pitches on the **bottom row only** and leaves the top row
> entirely off (`Motion32_Scale_and_Chord_Engine.md` §5.3c, marked resolved). The collapse is not
> cosmetic: one lane of consecutive degrees is what makes duplicate pitches impossible.

> ⚠️ **Octave and A–H are different transforms and must not be summed.** Octave is a rigid semitone
> transposition — the whole shape moves and the gaps stay put. A–H is a *degree* shift: it slides the
> window along the piano, so which positions have a black key above them changes and **the gaps move
> with it**. They are the two arguments to `pad_pitches`, not one term.
>
> This shipped as a semitone shift first, from the manual's chromatic-sounding "moves the musical
> root note left/right along the piano". Factory behaviour settles it: **A–H only ever shifts the
> bottom row**, so one press is one bottom-row pad. The visible symptom of the wrong unit was a
> keybed that never redrew when you banked — and it wasn't an LED bug: a rigid transposition changes
> no pad's *role*, so `pad_roles` returned an identical list and there was genuinely nothing to
> repaint. Getting the unit right fixed the lights as a side effect.
>
> **Both rows move, and for the same reason: the pattern belongs to the pitches, not the pads.** The
> root tint marks the pads playing the root pitch class — the C's, the landmark you orient by on a
> piano — so it slides across the keybed as the window moves. It was pinned to `index % 7 == 0`
> ("pad 1 is always the root") on a reading of the manual's *"Bank E will be selected and Pad 1 will
> be assigned to the root note"*. That sentence describes the **default**: at bank E the window
> starts on C, so the two rules give the same pads. They agree nowhere else, and the capture that
> verified this layout was taken at rest — so the top lane's gaps moved while the bottom lane's tint
> stood still, and half the keybed redrew.
>
> Eight banks over a seven-degree cycle give exactly seven distinct patterns — A and H are an octave
> apart and share one — and that holds for the gaps and the tint alike.
>
> **The octave limit is derived, not fixed.** `OCTAVE_LIMIT = 3` used to guarantee on its own that
> every pad stayed inside MIDI 0–127 — the layout spans ~2½ octaves, so ±3 could not reach the edge.
> A–H adds four more semitones downward and broke that: bank A at octave −3 is −40 semitones and puts
> pad 1 on note **−4**. The limit now comes from `pads.safe_semitone_range()` combined with the
> current bank, so at bank A the octave floor is −2. Selecting a low bank while the octave is already
> floored pulls the octave up: **the bank wins and the octave yields**, because A–H is an explicit
> selection and the octave is a range control.
>
> This matters because **a bottom-lane pad is never legitimately dead.** The gaps are missing *black*
> keys and black keys only exist on the top lane; the bottom lane is sixteen white keys, all real
> notes, and the root lives there.
>
> **The lights and the notes come from one list, not two offsets.** The screen component used to keep
> its own `_pad_root_offset` and call `pad_roles()` with it. Nothing kept that in step with the
> keyboard's copy, and the symptom would have been a keybed lit for a layout it does not play. The
> keyboard now reports the roles derived from `self._pitches` — the very list the note translation is
> built from — so there is no second copy to drift.

**The Shift pad overlay** (Phase 8) — hold **Shift** and the bottom lane stops being a keyboard and
becomes a 16-slot edit layer, as the factory does it. The top lane goes dark and silent.

| 1 | 2 | 3 | 4 | 5 | 6 | 7–16 |
|---|---|---|---|---|---|---|
| Undo | Redo | Dup | Delete | Quant | Double | *(grey)* |

**Six commands, not sixteen, and the shortfall is the interesting part.** The factory's sixteen are
Studio One's, and most don't survive translation: **Split** and **Merge/Consolidate** are *not in the
LOM at all* (a grep for `split`, `consolidate`, `join`, `freeze`, `flatten` across all twelve LOM
reference files finds nothing), and **Insert Pattern / New Variation / Duplicate Variation** are
Studio One concepts Live has no equivalent of. Copy and Paste are deferred rather than impossible:
the framework's `ClipboardComponent` works by holding Copy and tapping a *source* then a
*destination*, so it needs a clip grid to point at and arrives with Session mode.

Unassigned slots are **grey, not dark** — the factory's "present but unassigned" convention, and
with ten of sixteen empty it is what stops the layer looking broken. Pressing one still answers on
the notification bar, because a pad that responds only sometimes reads as a dead pad.

> 🔑 **How a pad can be a command without also being a note.** `ComboElement` carries
> `priority_increment = 0.5`, so a *bound* Shift-modified pad outranks the keyboard binding and takes
> the press. No mode switching, no layer juggling — the framework's own mechanism.
>
> ⚠️ **But an *unbound* modified element claims nothing.** Priority is asserted by being in a live
> layer, so leaving the top lane alone would have left the accidentals sounding under Shift. It is
> bound to a `BackgroundComponent` purely to be consumed — on this surface "unbound" and "silent"
> are opposites, exactly as the four dead keyboard pads taught.
>
> ⚠️ **`Clip_Actions` is deliberately not bound to the pads**, despite implementing four of these
> commands properly with availability LEDs. It would take LED ownership of four pad addresses — a
> pad's LED address *is* its note address — leaving twenty-eight with `PadLeds` and four with the
> framework. That split is the two-writer bug that cost three attempts on the encoder halos. The
> actions are three LOM lines each; the ownership is the part that matters.

**Scale mode — Template 1**

Press **Scale** and the pads re-lay to a scale. The screen is the factory's own layout: header title
`Scales`, a single **`Guide`/`Locked`** toggle top-right, the scale list, and `Main | Modes | ⬚ | Key`
underneath. The **wheel scrolls the list** and the scale changes as you land on it — no confirm step,
because on an instrument you want to hear it.

| | Pads | Lighting |
|---|---|---|
| **`Locked`** *(default)* | bottom lane only — 16 consecutive scale degrees, top lane dead | tonics in the track colour, other degrees white |
| **`Guide`** | the ordinary piano, both lanes, everything playable | in-scale full brightness, out-of-scale **dimmed, not dark** |

> 🔑 **The one-lane collapse is what makes duplicate pitches impossible.** Sixteen consecutive
> degrees ascend strictly, so no two pads can sound the same note — verified across 15 scales × 12
> roots × 7 octaves × 8 bank positions with zero violations. `Guide` cannot collide either, because
> it *is* the piano layout.
>
> ⚠️ **`Guide` is a lighting change, not a layout change.** It returns the *unchanged*
> `pads.pad_pitches()`, so note translation, dead pads and held-pad feedback need no second path.
>
> A–H banking works in both, in the same unit — one scale degree — so one radio serves the piano and
> every scale.

**Two deliberate divergences from the factory.** **Chromatic is not offered**: leaving Scale mode
*is* selecting chromatic. **The triads are not offered either** — `Major Triad` is `(0, 4, 7)`, which
across sixteen pads spans 60 semitones; that is a chord voicing table, and the firmware keeps
`Triad`/`Sus2`/`Sus4`/`Add 7` in its *chord* strings. So the menu is 7 + 7 = 14 where the factory
shows 16.

**The Motion writes its key to Live.** `song.root_note` and `song.scale_name` are both writable, so
Live's own scale awareness follows the controller. ⚠️ `scale_name` takes Live's spelling — our
`Natural Minor` is Live's `Minor` — and an unrecognised name is silently ignored, so the translation
is an explicit table and a scale with no Live counterpart is simply not pushed.

**Sends — the third Mix page**

The eight encoders become a **(track × send) grid**: columns are tracks, rows are sends, so
**encoder 1 and encoder 5 are send A and B of the same track**, and a column sits where its strip
does on the Volume page. Halos wear the slot's track colour, so both encoders in a column match.

🔑 **The page count comes from your set, and no encoder is ever dead.** Sends are taken in pairs —
the two physical rows — with a leftover odd send given its own page of one row × eight tracks:

| Returns | Pages | |
|---|---|---|
| 1 | 1 | one row of 8 tracks |
| 2 | 2 | 4 tracks × 2 sends, twice |
| 3 | **3** | two as above, then one row of 8 on send C |
| 4 | 4 | 4 tracks × 2 sends, four times |

> ⚠️ **`Clip_Actions`-style framework help stops just short here.** `MixerComponent.set_send_controls`
> genuinely takes a 2D matrix indexed `[strip, send]` — this exact shape — but it maps `controls[x]`
> onto `_channel_strips[x]`, so a four-wide matrix reaches strips 0-3 and leaves half the ring
> unreachable. The *mapping* is still the framework's (`MappedControl`, engine-side, no Python in the
> value path); only the choice of which parameter goes where is ours.
>
> ⚠️ **And that choice brings duties with it.** A component that maps parameters must follow the
> session ring, resolve which track each encoder means, **and release its parameters when the page
> is not showing** — the last one, omitted, stopped Plugin mode binding its device at all. See
> `Motion32_Implementation_Notes.md` §6b-34.

**Octave buttons** carry two meanings on one LED, matching the factory: the **state byte** is
press feedback (dim 63 at rest, full 127 while held) and the **RGB** shows whether that
direction is engaged (blue at rest, white when transposed). Pressing Down when the offset
returns to zero repaints *Up* blue — both buttons read one shared value, each showing its own
direction.

**Encoder feel** — `quantized_parameter_sensitivity = 1.0` on the Specification. The framework default
is **0.1**, which is why a toggle or enum list took roughly ten detents to advance one step. This was
never an encoder-acceleration problem.

**Edit** is deliberately unmapped until that view is designed — its element exists, but a mode button
without a matching mode binds a control the framework never created. Mix was in that state until
2026-07-29 and is now a full mode.

## The LED colour contract

| Control | Rest | Active | Pressed |
|---|---|---|---|
| **Shift** | purple `#8A2BE2` | — | white |
| Play | dim green | green | — |
| Stop | orange | orange (always available) | white |
| Record | dim red | red | white |
| Tap | blue | — | white |
| **Loop** (Shift+Play, and soft button 3) | blue | **yellow** — Live's loop brace | white |
| **Metronome** (Shift+Tap) | **dark** | **yellow** | — |
| **Undo** (Shift+Stop) | blue | — | white |
| Solo | blue | yellow | — |
| **Mute** | **yellow** — the track is playing | **red** — muted | — |
| Arm (Mix mode, 8 soft buttons) | dark | red | — |
| Nav ← → ↑ ↓ (all modes) | blue | — | white |
| Octave ± | dim blue | dim white (that direction engaged) | full white |
| A–H banks | dim blue | dim white (selected) | full white |

Yellow means "Live is doing something to your timing or your signal path" — loop, metronome, an
audible track. Blue means "this control is live". White means "you are touching it".

> ⚠️ **`Mixer.MuteOn` means *muted*, not *active*.** From `channel_strip.pyc`:
> `self.mute_button.is_on = self._track.mute or self._track.muted_via_solo`. So `MuteOn` is red and
> `MuteOff` is yellow, which reads backwards until you know that.
>
> ⚠️ Mute-audible and Solo-engaged are now the same yellow on adjacent keys. If that reads badly on
> the hardware, move **Solo** to Live's solo blue — Mute is the one matching Live's own scheme.

**Song mode uses Template 3**, the factory's Song/Timeline screen (identified from a photo of Studio
Pro). Each tile there has a separate label *and* value element, so the full encoder name and its live
reading are both on screen — no reveal-on-touch needed. Layout follows the factory: blue header shows
which Live view is up (**Session** / **Arrangement**), the grey centre bar shows the selected track,
and the eight tiles show name + value.

Plugin mode stays on **Template 0** for its encoder arcs — a device parameter reads better as a fill
than a number, with the value revealed on touch.

**Plugin view — Template 0**
- Cached, diffed renderer: only changed elements go on the wire; a redundant re-render costs nothing
- Header bar carries the **focused track's own colour** (falling back to the factory `#0069CC`), with
  the title text flipped to black or white for contrast — Live's track colours include pale ones
- Header title = **`Track | Device`**, using the header's full width (26 chars). Fender's 13-char
  budget keeps the title in the left half, which is only necessary when the top soft-button labels
  are in use — Plugin mode leaves them blank
- The bank name sits on a **grey strip** (`#303336`), the same treatment Template 3 gives its title bar
- 8 encoder tiles: parameter name (7 chars), halo fill from the live value, greyed when unassigned
- Centre area = Live's own bank name ("Filter", "Envelope"), else the owning track
- Factory colour palette (`#0069CC` header, white active, `#BBBFC3` unassigned, `#303336` dividers)
- Full redraw on connect, on `refresh_state`, and after Global Settings closes
- Labels cannot desync from the knobs: the screen listens to `DeviceComponent.parameters`, a
  listenable property that fires on device change *and* bank change, and it reads the same
  `ParameterInfo` list the encoders are mapped from (so it also picks up Live's bank-specific
  parameter names)

**Live values**

Song-mode readouts come from song properties, so the screen listens to `tempo`, `loop_start`,
`loop_length` and `signature_numerator`, plus the selected track and its name. Arrangement position,
zoom and cue have no property to subscribe to (they're driven by the Transport/Zoom components, and
`current_song_time` is far too chatty), so while a value is actually on screen the component re-reads at
20 Hz and stops when the last value times out. The diff makes idle refreshes free — nothing goes on the
wire unless a number really changed.

With no device in focus, Plugin mode shows the focused track and "No device selected" with every tile
labelled `-`: an empty screen is indistinguishable from a broken one.

**Parameter values on touch and turn (Plugin mode only)**

A Template 0 tile has only one text element, so the name and the value share it — the same reason the
factory shows the name at rest. Song mode doesn't need this; Template 3 shows both at once.

Touching an encoder reveals its value; releasing starts a **0.75 s** timeout (the framework's own
`ACTIVE_PARAMETER_TIMEOUT`) after which it reverts to the name. A value change
from anywhere — encoder, mouse, automation — reveals it too. The value is drawn in blue to distinguish
it from the name.

Values use `truncate_value()`, not `compactify()`: compactify strips hyphens, which would turn
`-12.5 dB` into `12.5 dB` and silently flip the sign. A deliberate divergence from the factory.

**Teardown**
- Releases every LED and screen element *before* the native-mode goodbye, using the exact values from a
  Studio Pro shutdown capture: LED state off with colour **white**, and screen elements left **empty,
  white, visible**. Not black-and-hidden — that leaves the Motion's own UI dark after unload, because it
  draws into the same persistent screen elements.

## Layout

| File | Role |
|---|---|
| `__init__.py` | `ControlSurface`, specification, handshake, redraw lifecycle, teardown |
| `midi.py` | Wire constants — CCs, SysEx ids, attributes, LED addresses |
| `protocol.py` | SysEx framing, identity parsing, the feedback-suspend gate |
| `palette.py` | **The one colour conversion layer** — `rgb7` (8-bit -> 7-bit), `live_rgb7` (a Live object's real colour), `dim`. Screen *and* LEDs go through it |
| `screen.py` | Screen address map (named, never raw zone/element) + factory chrome palette |
| `formatting.py` | `compactify` label abbreviation + character budgets |
| `display.py` | `ScreenModel` (cache/diff/flush/invalidate) + `MainView` (T0) + `MixerView` (T2) + `ParamsView` (T3) |
| `notification.py` | `NotificationView` (T1) — the transient title/value bar that outranks every mode |
| `screen_component.py` | Where screen content comes from in Live, and when it changes |
| `parameters.py` | Resolves which 8 parameters the encoders are wired to |
| `runtime.py` | Hand-off point between the control surface and components |
| `elements.py` | Physical control declarations, incl. `MotionEncoderElement` (why the halos work) |
| `mappings.py` | Component ↔ element assignments |
| `transport.py` | Subclasses the framework `TransportComponent`; adds record, loop-toggle, back-to-arrangement |
| `pads.py` | The Keys layout — which pad is which key, and the four that are not keys at all |
| `keyboard.py` | The pads as a playable keyboard: note translation, Octave ±, the A–H bank radio. **Single source of the layout** |
| `wheel.py` | The big wheel's **push**: next device, with wraparound |
| `commands.py` | The **Shift pad overlay** — the six edit commands, and the modifier subclass that reports Shift-down |
| `mixpages.py` | The big wheel **turning**: pages Mix mode, expanding Sends into as many steps as the set needs |
| `sends.py` | Mix mode's **Sends** page — the (track × send) grid and its derived page count |
| `scales.py` | The **15-scale table** and both Scale layouts. Framework-free, so the suite executes it |
| `scalemode.py` | Scale mode's state, soft buttons and wheel; plus the **Control** button that returns |
| `menu.py` | The Template 1 **list view**, shared with the notification bar |
| `commands.py` | The **Shift pad overlay**, and the modifier subclass that reports Shift-down |
| `leds.py` | Encoder halo, wheel and pad LEDs — cached/diffed, no framework component owns these |
| `skin.py`, `colors.py` | LED colours (keys must match what the framework asks for) |

All 26 modules are listed. `Motion32_Ableton_Build_Handoff.md` §2 carries the same table with more
detail on each module's reason for existing.

Two architectural rules hold the screen together, both from the roadmap:

1. **One owner per element.** `MainView` alone writes Template 0 and `ParamsView` alone writes
   Template 3. Addresses are named in `screen.py` so a second writer shows up in review rather than on
   hardware as a flickering label.
2. **Desired vs sent.** `ScreenModel` keeps both. `flush()` sends the difference;
   `invalidate()` clears "sent" so the next flush repaints everything. That is what makes
   reconnect and post-Global-Settings recovery correct.

## Tests

```
pip install xdis          # a prerequisite, not an optional extra — see below
python3 tests/test_screen.py
```

Runs without Live or hardware — the modules it covers import nothing from the framework.
**169 test groups, 3999 assertions**, ending in a `PASSED` or `FAILED` line. The checks that earn
their keep:

- **skin coverage, both halves** — every skin *namespace* a bound component asks for must exist
  (derived from the framework `.pyc`, so it needs no maintenance), and every LED-bearing control we
  map must have its exact keys declared (an explicit table, because nothing in the bytecode links a
  control name to its skin keys). Verified by deleting `class Session`, and again by renaming
  `ModifierBackground` back to `Modifier`;

- every `(template, zone, element, attr)` the renderer emits is validated against
  `Motion32_Screen_Template_Map.csv`, the machine-extracted list of the device's 433 real attribute
  handlers, so an address typo or unsupported attribute fails here instead of silently doing nothing
  on the device;
- AST guards for mistakes that have actually failed a script load or a render, each verified by
  reintroducing the bug and confirming the test fails:
  - **every `self.X` in a Component subclass resolves** — against the class *and* the real framework
    members, read from `Resources/control_surface/*.pyc`. `screen_component.py` and `transport.py`
    import the framework so the suite can't execute them; this is what stands in for that;
  - **no framework *property* is called** — `application`, `song`, `parent`, `layer`, `_tasks` are
    properties (`self.application()` raises), while `is_enabled()` is a method; the list is derived
    from the class-body bytecode;
  - **every `@listens` handler accepts `*a`** — notifiers differ in whether they pass a value;
  - **control event handlers match the framework's arity** — a `control_list` handler is
    `(self, control)` with the index on `control.index`; `(self, index, control)` is the 2D
    `control_matrix` shape and raises on the first press;
  - no matrix element helper is passed `channel=` (the framework supplies it);
  - no `Component` subclass shadows a framework attribute (`_song`, `_parent`, `song`, `name`, …);
  - the screen component is registered in `component_map` and never hand-constructed (registration is
    what gets it dependency injection, and therefore `self._tasks` for the value timeout);
  - **every mapped control name exists on its target component**, resolved from the framework
    `.pyc` — a `Layer` binds an unknown name *silently*, which hid a broken `Device_Navigation`
    mapping for several rounds;
  - **the teardown values match the capture** (white + visible, not black + hidden);
  - **a superseded instance cannot wipe the live one, and emits zero bytes** — Live builds the new
    surface before disconnecting the old, so shared module state is owner-scoped and the hardware
    reset in `disconnect()` is gated on still owning the device. The stronger of the two guards runs
    the real teardown methods against a stand-in for the framework's own goodbye path and asserts
    **nothing** goes on the wire — suspending our writers never reached `goodbye_messages`, which
    `ControlSurface.disconnect()` sends through `_send_midi` directly;
  - no *element* is bound twice in layers that are live at once (global + any one mode), every
    declared mode button has a matching mode, Song mode claims each of the 8 encoders exactly once,
    and `transport.py` subclasses the framework component rather than replacing it.

  The mapping tests evaluate the real `create_mappings()` with the framework's mode module stubbed,
  rather than picking the dict apart with AST — the specs are built from helpers, and a walker that
  has to understand those is likelier to be wrong than the thing it checks.

  See `Motion32_Implementation_Notes.md` §4 for the reserved-name list and the reasoning.

**Why `xdis` is a prerequisite.** Every guard that resolves a name against the *real* framework reads
Live's `.pyc` through it. Without it the suite silently dropped all 36 assertions of
`test_every_mapped_control_name_exists` and still reported "0 failures" — the historical
`prev_button`/`next_button` bug passed clean in that state. An unrunnable guard is now a **failure**
that names each mapping it could not check, so a green run always means the guards actually ran.
See `Motion32_Implementation_Notes.md` §6b-13.

## Install

**Requirements:** Ableton Live 12 (the script targets the `ableton.v3` control-surface framework, so
Live 11 and earlier will not load it), a Fender Motion 32 on firmware **1.0.6** or later, and no
other software holding the `Motion 32 Main` port.

Clone or copy this repository into Live 12's User Library so that the folder is named `Motion32`:

| OS | Path |
|---|---|
| macOS | `~/Music/Ableton/User Library/Remote Scripts/Motion32` |
| Windows | `%USERPROFILE%\Documents\Ableton\User Library\Remote Scripts\Motion32` |

```
cd "<User Library>/Remote Scripts"
git clone https://github.com/<you>/Motion32.git Motion32
```

The folder name matters — Live derives the Control Surface name from it, so a clone that lands in
`Motion32-main` will show up under that name or not at all.

Then, in Live: **Preferences → Link/Tempo/MIDI → Control Surface**, select **Motion32**, and set both
Input and Output to **Motion 32 Main**. On the device itself, set **DAW Mode to Off** — the script
drives the native host protocol on the Main port and deliberately leaves the separate Control/MCU
port unused. Restart Live if the surface does not appear in the dropdown.

If nothing lights up, check `Log.txt` against the list in the next section before anything else.

## What to check in Log.txt on the next hardware run

- `Motion32: script setup complete`
- `Motion32 firmware: 1.0.6 (code 1006)` — and **no** "older than the supported minimum" warning.
  If it reports `0.1.0`, the identity-offset fix did not take effect.
- `Motion32: reading encoder parameters from DeviceComponent.parameters`
- `Motion32: full screen redraw (setup)`
- **no** `Got unknown sysex message` warnings — we now consume the messages we parse

What to try:

1. Press **Plugin** — the device view appears; press **Song** — back to the song view. The mode
   buttons are a **strict radio**, so a second press of Plugin does *nothing*: exactly one of
   Song/Plugin/Mix is lit at all times, and there is no toggle-back.
2. **Shift+Song** should flip Live between Session and Arrangement.
3. In Plugin mode, turn an encoder: the tile shows the value in blue, then reverts to the name
   after ~0.75 s. Touching without turning should reveal it too.
4. Step banks with Left/Right and devices with Up/Down: labels, halo fills and the centre bank
   name should all follow with no stale text.
5. **Mix mode (2026-07-29).** Press **Mix**: eight strips with number, track name on the track's
   colour, and a fader at the right level. Then:
   - Turning an encoder moves that strip's volume; the **eight halos wear the eight track colours**.
   - **Left/Right pages the ring by eight**, not one, and the strips follow.
   - **Touching an encoder selects that track** — Live's highlight moves, the strip's name swatch
     goes selection-blue, and **Solo/Mute now act on that strip**. Let go and wait: the focus must
     *stay* put.
   - The **eight soft buttons arm** the eight strips: red when armed, dark when not. Arm one with
     the mouse and its button should light without you touching the Motion. ⚠️ Use a **MIDI** track
     or an audio track with a real input selected — Live won't arm an inputless audio track, from
     the Motion or the mouse.
   - The **meters** ✅ (Phase 7c, confirmed 2026-08-03 — levels, decay and the green/amber/red
     banding all read correctly against Live's own meters). Still worth a glance on any new run:
     a MIDI track with no instrument must show **no meter at all** rather than a flat one, the
     loop must stop on the Pan page so nothing is left frozen mid-decay, and there should be no
     lag in the pads or encoders while it runs.
     - ⚠️ **One question the first run did not answer:** do meters keep updating with Live in the
       background? If they freeze mid-decay on app switch they need a zeroing path — §7c.
   - **Touch an encoder and hold it**: that strip's **track name is replaced by the volume**
     (`-6.0 dB`). **Let go and the name comes back at once** — no pause. The other seven strips
     must not change, and a negative value must keep its minus sign.
   - A **white or pale-coloured track** must still show its name — the swatch behind it darkens.
   - **Turn the big wheel**: the screen should flip to eight **pan** arcs with the track names, and
     the encoders should move pan. Keep turning — the pages **wrap**. Turn back for Volume.
   - The **wheel halo should be lit** throughout Mix mode, as it is in Plugin.
   - On the Pan page, **touch an encoder**: the tile should show `C` / `50L` / `50R` and revert
     after ~0.75 s, and the centre label should wear the selected track's colour. Move a pan with
     the mouse — the arc should follow live.
6. In Song mode: encoders 1-4 = tempo / position / loop start / loop length, 5-6 = zoom, 7-8 = cue /
   **cue volume** (not a second tempo). Transport buttons should still work in every mode
   (Play/Stop/Rec/Tap, and the four Shift combos).
7. **The Shift pad overlay (2026-08-03) — ✅ *painting* confirmed 2026-08-08, ⚠️ *silence* not.**
   A capture shows the overlay drawing correctly on `CC 31`. It shows only **outbound** writes, so it
   proves nothing about whether the pads stay quiet — that still needs a listen. Hold **Shift**:
   - The bottom lane should show **six white pads** (Undo, Redo, Dup, Delete, Quant, Double) and
     **ten grey** ones. Grey, not dark — a dark slot would look broken rather than empty.
   - The **top lane must go dark**, and — the load-bearing check — **no pad should play a note**
     while Shift is held. If the accidentals still sound, the top lane is not being consumed.
   - Each command should announce itself on the bar: `Edit` / `Undo`. Press a **grey** pad — it
     must answer `Edit` / `--` rather than doing nothing silently.
   - Press **Undo** with nothing to undo: `Edit` / `Nothing`. Press **Quant** with no clip
     selected: `Edit` / `No clip`. A command that cannot act has to say so.
   - Let Shift go: the keybed must return to the piano layout, in the track's colour.

8. **Scale mode (2026-08-03).** Press **Scale**:
   - The pads collapse to **one lane** of the scale with tonics in the track colour; the **top lane
     goes dark**. The wheel scrolls the list and the scale changes as you land on it.
   - `Main` / `Modes` / `Key` switch what the list shows; the **top-right** button flips between
     `Locked` and `Guide`. In `Guide` the keybed returns to the piano with out-of-scale notes
     **dimmed, not dark** — they still play.
   - **A–H banking must move the pitches**, not just the lights. That was the bug: a frozen layout
     re-lit the keybed while the notes stayed put.
   - **No notification bar** should appear in Scale mode — it shares Template 1 with the list.
   - **Control** returns to whichever mode you came from; Song/Plugin/Mix leave directly.

9. **The Sends page (2026-08-03) — the axis that found three bugs.** Cross modes deliberately:
   - Mix → wheel to **Sends**: encoder 1 and encoder 5 must be **send A and B of the same track**,
     and both halos wear that track's colour.
   - **Left/Right, then turn an encoder.** It must move the *new* track's send — this is the ring
     the grid has to follow.
   - **Touch an encoder**: the track it focuses must be the one the knob turns, not the strip at the
     encoder's index.
   - **Sends → Plugin.** The device must bind and its encoders must work. If they are dead, the
     Sends page has not released its parameters (§6b-34).
   - With **three** return tracks there should be **three** pages, the last one a single row of
     eight — no dead encoders anywhere.

10. **The colour pass (2026-08-03) — none of this has been on hardware yet.**
   - **Shift** should sit **purple** at rest and flash **white** while held. It was dark before this
     change, so "it lights at all" is the first thing to confirm.
   - **Mix mode Left/Right** should be **blue**, white on press. They were dark for the whole of
     Phase 7 — this is the fix with the most visible before/after.
   - Hold **Shift**: Stop should turn **blue** (Undo). It was dark under Shift before.
   - Toggle the **loop** (Shift+Play, or soft button 3): the LED should go **yellow**, not green.
   - Toggle the **metronome** (Shift+Tap): **yellow** when on, **dark** when off.
   - **Mute**: **yellow** while the track is audible, **red** when muted. Mute one with the mouse and
     watch it change without touching the Motion.
   - **Plugin mode halos** should now wear the **owning track's colour**, matching the header bar
     above them. Switch tracks and check the two move together — if the halos and the header ever
     disagree, that is the bug the shared resolver exists to prevent.
   - Also worth a glance: teardown now writes each LED address **once** rather than twice, so unload
     should be visibly quicker on the MIDI monitor. Nothing should look different on the device.

11. **The reload test (2026-07-29).** Reload the script — re-select Motion32 as the Control
   Surface, or just save an edit to any module — then press **Play** and watch the incoming CC. It
   must be `0x6F`. If it is `0x66`-`0x69` the device fell out of native mode, which is the superseded
   instance sending `8F 00 00` behind the new one's back. The log should carry
   `Motion32: disconnecting a superseded instance — … (MIDI output muted: …)` and **no** further
   output from that instance.

## Framework source

**Check the framework source before assuming any framework API.** It is the authority on call
signatures, component control names, listenable properties and skin keys. Two bugs in this script
came from reasoning about the framework without it; see `Motion32_Implementation_Notes.md` §6b–6c.

That source is Ableton's own `.pyc`, so it is **not distributed here**. Copy it out of your own Live
installation into `Resources/control_surface/` (git ignores that path), then read it with `xdis`
(`pip install xdis`):

| OS | Location inside the Live application |
|---|---|
| macOS | `/Applications/Ableton Live 12 Suite.app/Contents/App-Resources/MIDI Remote Scripts/../../Frameworks/.../ableton/v3/control_surface/` |
| Windows | `C:\ProgramData\Ableton\Live 12 Suite\Resources\MIDI Remote Scripts\` and the bundled Python lib |

The exact path moves between Live builds; searching the install directory for `control_surface` finds
it faster than following a path from memory.

## Live Object Model reference

`Resources/AbletonLOM/references/` holds a 12-file Live 12.3 LOM reference (from
[mikecfisher/ableton-lom-skill](https://github.com/mikecfisher/ableton-lom-skill), MIT), paired with
an installed `ableton-lom` skill. Read the matching file for questions about **Live's objects** —
what a Track, Clip or DeviceParameter exposes, and crucially whether a property is *observable*,
since guessing that produces listeners that silently never fire.

This is a different source from the one above and answers a different question: LOM = Live's object
model; `Resources/control_surface/` = the control-surface framework. Neither substitutes for the
other. If the directory is absent:

```
git clone https://github.com/mikecfisher/ableton-lom-skill.git Resources/AbletonLOM
```

## Firmware analysis

`Resources/FirmwareAnalysis/` holds the written analysis and the Ghidra probe scripts. The settled
conclusions are in `Motion32_Implementation_Notes.md` §6b-33 — in short, **the device's control
mapping cannot be changed by a host**: CC numbers are immediate operands in the instruction stream,
and the only variability is a boot-time Motion 32 / Motion 16 selection.

The **firmware image and the Ghidra databases are not in this repository** — they are Fender's
copyright and are not ours to redistribute. The `.md` findings, the address tables and the `.java`
probe scripts are, and they are written to stand on their own. To reproduce the analysis, extract the
firmware from your own PreSonus Universal Control installation and re-run the probes in
`run_*_probe.sh`.

⚠️ Two Ghidra imports were used and are not interchangeable; `motion32_fw_payload_0x1000.bin` is the
one every documented address belongs to. Its image base is 0, so many questions can be answered by
reading the `.bin` directly in Python rather than opening Ghidra at all.

## Not yet implemented

**Edit** mode, the **touch strips** (Phase 9), **Chord** mode (Phase 11) and Session mode.

The **Shift pad overlay** has six of sixteen slots filled; the rest wait on Session mode (Copy and
Paste need a clip grid to point at) or on decisions still to take. **Scale mode** is built; its
Template 1 list view is now general enough for Chord's progressions and for browser navigation.

**Mix mode is complete and on hardware** — strips, volume, the Pan page, cap-touch focus and its
value reveal, per-strip arm, the track-coloured halos, and the **meters** as of 2026-08-03. See
`Motion32_Build_Roadmap.md` for the sequence and `Resources/Motion32_Ableton_Build_Handoff.md` §7 for
what is open.

> Pads, the playable keyboard, Octave ±, A–H banking, LCD soft buttons, encoder halos and the
> notification bar **are** implemented — this list said otherwise until 2026-07-29.

⚠️ **The touch strips are not merely absent — strip 2 is actively wrong.** Undeclared, its channel-1
pitch bend reaches the armed track and fights strip 1, so an instrument gets two pitch benders.
Declaring strip 2 with `ScriptForwarding.exclusive` fixes it on its own. See
`Motion32_Pads_Banking_and_Strips.md` §5.3b.

## Licence

The **Python source** in this repository is licensed under the
[GNU General Public License v3.0](LICENSE).

The **documentation** — this README, and all Markdown and CSV under `Resources/` — is licensed under
[CC BY-SA 4.0](LICENSE-DOCS.md). GPL is written for software and reads poorly applied to a SysEx
table; CC BY-SA gives the prose the same share-alike protection in a licence built for written work.

A note on the GPL and Live: a Remote Script is loaded by, and imports from, Ableton Live, which is
proprietary. Whether that constitutes linking in the GPL's sense is a question nobody has ever tested
in court, and Remote Scripts have shipped under the GPL for years without incident. If that
uncertainty matters to your use, open an issue — relicensing the code under LGPL is not off the table.

## What this repository does not contain

This project documents the Motion 32's MIDI and SysEx protocol so that the device can be driven from
Ableton Live. The protocol documentation is original work, produced for interoperability.

Deliberately **excluded** from this repository, and listed in [`.gitignore`](.gitignore):

- Fender Motion 32 firmware images, and the Ghidra databases that embed them
- PreSonus Universal Control and Studio Pro binaries, integration scripts, artwork and skins
- Ableton Live's `ableton.v3.control_surface` framework `.pyc`
- The Motion 32 owner's and integration manuals

All of the above remain the property of their respective owners. Several of them are needed to work
on this script or to reproduce the firmware analysis, and the README says where to get each from your
own licensed installation. None of them are redistributed here.

## Disclaimer

This is an **unofficial, community-built** project. It is not affiliated with, authorised by,
endorsed by or supported by Fender Musical Instruments Corporation, PreSonus Audio Electronics, or
Ableton AG.

*Fender* and *Motion 32* are trademarks of Fender Musical Instruments Corporation. *PreSonus*,
*Studio One* and *Universal Control* are trademarks of PreSonus Audio Electronics, Inc. *Ableton* and
*Live* are trademarks of Ableton AG. These names are used here only to identify the hardware and
software this script interoperates with, as permitted by nominative fair use.

The script sends undocumented SysEx to your hardware. It is provided **without warranty of any kind**
— see sections 15 and 16 of the [GPL](LICENSE). Use at your own risk.
