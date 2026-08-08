"""The pads as a playable piano keyboard — transposition, press feedback, and the dead keys.

**What works:** the pads play a piano layout (bottom lane the white keys, top lane the
accidentals), notes reach an armed track, a press lights the pad green and a release reverts it.

Both halves come from `PlayableComponent` (`components/playable.pyc`):

* `_note_translation_for_button(button)` returns `(identifier, channel)` and
  `_set_button_control_properties` writes them onto the element. **This is the transposition** —
  pad X plays its layout pitch rather than its own note.
* `_button_should_be_enabled(button)` is, from the bytecode:

  ```python
  identifier, _ = self._note_translation_for_button(button)
  return identifier is None or (isinstance(identifier, int) and identifier < 128)
  ```

  ⚠️ **`None` means ENABLED, not disabled** — "no translation needed, leave this button alone".

**The dead keys took four attempts, and the reason is worth stating once.** A control is keyed by
`(identifier, channel)`, and the framework matches an incoming note against that key. So:

| Attempt | Why it failed |
|---|---|
| identifier `None` | enabled *and* untranslated — the raw note passed straight through |
| identifier ≥ 128 | disables the pad, and a disabled element is **released**, so its raw note floats loose |
| identifier = its own note, keyboard channel | **collides** with whichever real pad is transposed to that number — 54/58/61/65 are all live targets, so pressing a gap fired controls 26/28/30 and lit *their* pads |
| identifier = its own note, **own channel** | claimed, unique, and silenced by mode ✅ |

**The lever that silences is `mode`, per button.** `playable_and_listenable` passes the note to
the track and reports press/release to us; `listenable` consumes it and passes nothing. Dead pads
get `listenable`; everything else gets the playable mode. See `_update_control_from_script`,
which also has to defeat the base class's drum-rack "take the pads over while one is held"
behaviour — that was what swallowed notes.

**No latency.** Address and mode are set only when the layout changes, never per note.

⚠️ **LED ownership stays with `leds.PadLeds`.** `PlayableComponent._update_button_color` is an
empty hook and we deliberately leave it that way: a pad's LED address is its note address, and
two writers on one address is the problem that cost three attempts on the encoder halos
(§6b-10). One owner.
"""

from __future__ import annotations

import logging

from ableton.v3.control_surface.components import PlayableComponent
from ableton.v3.control_surface.controls import ButtonControl, PlayableControl

from . import pads

logger = logging.getLogger(__name__)

#: MIDI channel the translated notes are emitted on (0-based). Channel 1.
KEYBOARD_CHANNEL = 0

#: How far the Octave buttons may travel, in octaves either side of rest. This is the **musical**
#: limit only — ±3 is as far as anyone wants a keybed to jump.
#:
#: ⚠️ **It no longer guarantees the pads stay inside MIDI 0-127, and must not be relied on for
#: that.** It used to, because the layout spans ~2½ octaves so ±3 could not reach the edge. A-H
#: banking adds up to four more semitones downward and broke it — bank `A` at octave -3 is -40
#: semitones and puts pad 1 on note **-4**. The range limit is now *derived*, by
#: `pads.safe_semitone_range()` combined with the current bank; `_octave_limits()` takes whichever
#: of the two is tighter.
OCTAVE_LIMIT = 3

#: Channel the **dead** pads are claimed on. A control is keyed by `(identifier, channel)`, so
#: parking the gaps on their own channel makes them unique — they cannot collide with a real
#: pad's transposed pitch, which is what made pressing a gap fire someone else's pad.
#:
#: ⚠️ **Do not disable a dead pad instead.** `enabled = False` *releases* the element rather than
#: consuming it, letting its raw note loose. Dead pads stay claimed and are silenced by mode.
DEAD_PAD_CHANNEL = 15

#: What one A-H step is worth: **one scale degree — one pad along the bottom row.**
#:
#: ⚠️ **Corrected 2026-07-29 against factory behaviour, having first shipped as one semitone.**
#: The manual's "moves the musical root note left/right along the piano" reads chromatic, and the
#: firmware's `KeyboardRange` bank mode says "range, not whole banks" — but neither says what the
#: step *is*. Watching the factory settles it: **A-H only ever shifts the bottom row**, i.e. one
#: press slides the keybed by exactly one bottom-row pad. That is a degree, not a semitone. Pad 1
#: takes over what pad 2 was playing.
#:
#: This is why the unit matters rather than being a detail of feel: a degree shift **moves the
#: dead pads**, because whether a black key exists depends on which white key a position now
#: represents. A semitone shift transposes the whole shape rigidly and moves nothing. The visible
#: symptom of getting it wrong was a keybed that never redrew when you banked.
#:
#: `pads.bank_step()` stays deliberately unitless; this is the conversion. Scale mode keeps the
#: same meaning — `scales.locked_pitches` takes the same `degree_offset` — so one radio serves the
#: piano and every scale without a mode-dependent handler.
#:
#: ⚠️ This note used to add "even though both rows are lit in Scale mode". **That was wrong**, and
#: it contradicted `Motion32_Scale_and_Chord_Engine.md` §5.3c, which is marked resolved and is the
#: authority: in the factory's Scale layout the **top row is entirely off** and the pitches
#: collapse onto the bottom row. That collapse is not cosmetic — it is what makes duplicate
#: pitches impossible by construction. Corrected 2026-08-03.
DEGREES_PER_BANK_STEP = 1

#: What the notification bar calls the A-H root shift.
#:
#: ⚠️ **The bar's four fields are the soft-button labels, not free text on a wide bar.** Each is
#: `MENU_HEADER_BUT_TEXT[n]`, anchored over its physical button across the screen width, and the
#: title sits in slot 0 — the leftmost. So the practical budget is roughly the width of one
#: button, about 6-7 characters, *not* the `MAXCHARS_MENU_BUTTON = 16` the element will accept.
#: This read "Root Shifted" (12 characters) on the first hardware run and ran off the left edge;
#: "Octave" is 6 and has always fitted. Anything longer needs a different slot pair, which would
#: diverge from the captured factory layout and move the Octave bar with it.
NOTIFICATION_TITLE = "Root"

#: Shared by all eight A-H buttons. Same two-channel model as Octave: the **state byte** is press
#: feedback (dim at rest, full while held) and the **RGB** says whether this is the selected bank.
_BANK_COLOURS = {
    "color": "Keyboard.Bank",
    "on_color": "Keyboard.BankSelected",
    "pressed_color": "Keyboard.BankPressed",
}


def signed_label(value: int) -> str:
    """What the notification bar shows for an offset. `"0"` at rest, else signed.

    Not `f"{value:+d}"`: that renders rest as `"+0"`, and the capture shows the factory
    sending the single byte `0x30` — plain `"0"` — when the offset returns to zero, against
    `2B 31` (`"+1"`) when it does not.

    One function for both offsets. Octave was the first caller and A-H root shift is the
    second; they are the same rule, and two copies of it would eventually disagree about rest.

    Module level and self-contained so the offline suite can lift it out of the AST and
    execute it — `keyboard.py` imports the framework, so the suite cannot import the module
    (see `_exec_module_function` in the test suite). That is also why this calls no helper.
    """
    return "0" if value == 0 else f"{value:+d}"


class MotionKeyboardComponent(PlayableComponent):
    """Maps the 32 pads onto a piano layout and lets them play the armed track."""

    #: How many pad press/release events to log before going quiet. Enough to diagnose a
    #: stuck light on the next hardware run, few enough that playing does not flood Log.txt.
    MAX_LOGGED_PAD_EVENTS = 12

    #: How many layout changes to log. A bank or octave press is a deliberate action, so a
    #: handful is enough to answer "did the transposition reach the element?" on one run.
    MAX_LOGGED_LAYOUTS = 16

    #: Octave +/- (CC 0x40 / 0x41). They belong here rather than on the screen component
    #: because transposition is a property of the keyboard, and the keyboard owns the
    #: translation the transposition changes.
    #
    # `on_color` + the `is_on` setter are the factory's two-state colour model, and both are
    # real framework API — `ButtonControl.State.__init__(self, color, on_color, *a)` stores
    # both, `_send_button_color` picks `on_color if is_on else color`, and the `is_on` setter
    # calls `_send_current_color()` so assigning it repaints immediately. Verified by
    # disassembling `control_surface/controls/button.pyc`; see skin.py for the colour model.
    octave_up_button = ButtonControl(
        color="Keyboard.Octave",
        on_color="Keyboard.OctaveShifted",
        pressed_color="Keyboard.OctavePressed",
    )
    octave_down_button = ButtonControl(
        color="Keyboard.Octave",
        on_color="Keyboard.OctaveShifted",
        pressed_color="Keyboard.OctavePressed",
    )

    #: A-H (CC 0x00-0x07) — the pad bank, i.e. where the root sits. A **radio**: exactly one is
    #: lit, and pressing one selects it outright rather than toggling.
    #
    # ⚠️ **Eight declarations rather than `control_list(ButtonControl, 8)`, on purpose.**
    # `control_list(control_type, *a, **k)` forwards its kwargs to a `ControlList` that lives in
    # `ableton.v2.control_surface.control` — which is **not** in `Resources/control_surface/`, so
    # whether it passes `color`/`on_color` down to each element cannot be read. If it silently
    # dropped them, every bank button would light with the framework default and `is_on` would do
    # nothing (`_send_button_color` falls through to `color` whenever `on_color` is None), which
    # is a wrong-colour bug with no error attached. The two-argument `ButtonControl` form below is
    # verified from `controls/button.pyc` and already running on hardware for Octave, and it is
    # also the factory Atom SQ's own idiom — its bank buttons are individually named too.
    # If v2's source ever lands in the repo, a `control_list` is the obvious simplification.
    bank_a_button = ButtonControl(**_BANK_COLOURS)
    bank_b_button = ButtonControl(**_BANK_COLOURS)
    bank_c_button = ButtonControl(**_BANK_COLOURS)
    bank_d_button = ButtonControl(**_BANK_COLOURS)
    bank_e_button = ButtonControl(**_BANK_COLOURS)
    bank_f_button = ButtonControl(**_BANK_COLOURS)
    bank_g_button = ButtonControl(**_BANK_COLOURS)
    bank_h_button = ButtonControl(**_BANK_COLOURS)

    def __init__(self, *a, **k):
        # `matrix_always_listenable=True` keeps the pads **playable AND listenable**: the notes
        # still pass through to the track, and we additionally hear press/release so the pad
        # can flash while it is held. Without it the matrix is playable-only and we never see
        # a press.
        k.setdefault("matrix_always_listenable", True)
        super().__init__(*a, **k)
        self._root_offset = 0
        self._octave_semitones = 0
        #: Which A-H button is selected. Rests on **E**, so the root can move either way.
        self._bank_index = pads.BANK_REST_INDEX
        self._pitches = pads.pad_pitches()
        self._held = set()
        self._events_logged = 0
        self._layouts_logged = 0
        self._on_held_changed = None
        self._on_notification = None
        self._on_roles_changed = None
        #: A layout **provider**, not a layout. Called on every `_recompute()` with the current
        #: offsets; returns `(pitches, roles)` or `None` to mean "use the piano".
        #:
        #: 🐛 This was a frozen *list* and that was the bug behind A-H doing nothing in Scale
        #: mode: `_recompute()` re-used the stale list, so banking changed `root_offset` and the
        #: pitches never moved. A layout that depends on the offsets cannot be handed over once.
        self._layout_provider = None
        self._provided_roles = None

    # -- press feedback ----------------------------------------------------
    def set_held_listener(self, listener) -> None:
        """Called with the set of held pad indices whenever it changes.

        The keyboard does **not** paint the pads itself — `leds.PadLeds` owns those addresses
        (see the module docstring), so it reports the held set and the screen component
        repaints. Keeping the writer single is the whole point.
        """
        self._on_held_changed = listener

    @property
    def held_pads(self):
        return frozenset(self._held)

    # -- layout reporting --------------------------------------------------
    def set_roles_listener(self, listener) -> None:
        """Called with the pad roles whenever the layout changes.

        🔑 **This is what keeps the lights and the notes from disagreeing.** The screen
        component used to keep its *own* `_pad_root_offset` and call `pad_roles()` with it — two
        copies of the offset, and the handoff flagged the obvious failure: move one and not the
        other and the keybed lights a layout it does not play. Reporting the roles derived from
        `self._pitches` — the very list the note translation is built from — removes the second
        copy entirely rather than trying to keep it in step.

        Same shape as `set_held_listener`: the keyboard reports, `leds.PadLeds` stays the single
        writer of the pad addresses.
        """
        self._on_roles_changed = listener
        self._report_roles()

    @property
    def pad_pitches(self):
        """The pitch list this keyboard is currently playing. Read by the LED painter."""
        return list(self._pitches)

    def set_layout_provider(self, provider) -> None:
        """Install a layout **generator**, or `None` to go back to the piano.

        `provider(root_degrees, octave_semitones)` returns `(pitches, roles)`, or `None` to mean
        "the piano is right here". It is called on **every** `_recompute()` — which is what makes
        A-H and Octave work in Scale mode, because both change the arguments.

        🔑 **The keyboard remains the single authority on the layout.** The provider answers
        "what should these offsets produce"; the keyboard still owns `self._pitches`, still
        derives deadness and translation from it, and still reports the roles that the LEDs are
        painted from. Nothing downstream gains a second opinion.

        🐛 The first version took a finished *list*. A-H then moved `root_offset`, `_recompute()`
        re-used the same frozen list, and the keybed re-lit (the painter recomputed separately)
        while the notes did not move. Two symptoms, one cause: a layout that depends on state
        must be regenerated from that state, not captured once.
        """
        self._layout_provider = provider
        self._recompute()

    @property
    def pad_roles(self):
        """Role per pad — the provider's if there is one, else derived from the pitches.

        Either way it is **one** answer, computed alongside the very pitch list the notes come
        from. The LED painter reads this and never recomputes a layout of its own; doing so is
        what let the keybed light for a layout it was not playing.
        """
        if self._provided_roles is not None:
            return list(self._provided_roles)
        return pads.roles_for_pitches(self._pitches)

    def _report_roles(self) -> None:
        if self._on_roles_changed is None:
            return
        try:
            self._on_roles_changed(self.pad_roles)
        except Exception:
            # A screen that fails to repaint must never stop the keyboard transposing.
            logger.exception("Motion32: pad-roles listener failed")

    # -- notifications -----------------------------------------------------
    def set_notification_listener(self, listener) -> None:
        """Called with `(title, value)` when something worth announcing changes.

        The keyboard does not know what a screen is, in the same way it does not paint its own
        pads: it reports, and `screen_component.notify` decides. That keeps the transposition
        logic testable offline and leaves one owner for the display.
        """
        self._on_notification = listener

    def _notify(self, title: str, value: str) -> None:
        if self._on_notification is None:
            return
        try:
            self._on_notification(title, value)
        except Exception:
            # A screen that fails to draw must never stop the keyboard transposing.
            logger.exception("Motion32: notification listener failed")

    def _note_held(self, button, pressed: bool) -> None:
        """Record a pad as held or released and report the change immediately.

        Strictly note-on -> held, note-off -> not held. No timers, no timeouts: the light is a
        direct function of whether the pad is down.
        """
        index = self._index_for(button)
        if self._is_dead(index):
            # A dead pad is consumed, not played — it must never light either.
            return
        before = self._held.copy()
        if pressed:
            self._held.add(index)
        else:
            self._held.discard(index)

        # Bounded diagnostic. If a pad ever stays lit again, the question is simply "did the
        # release event arrive?" — and this answers it from Log.txt without a MIDI monitor.
        # Capped so it cannot flood during playing: instrumentation has to survive the traffic
        # it is meant to observe (§6b-6).
        if self._events_logged < self.MAX_LOGGED_PAD_EVENTS:
            self._events_logged += 1
            logger.info(
                "Motion32 pad %s: index=%s note=%s held=%s",
                "DOWN" if pressed else "UP  ",
                index,
                pads.note_for_index(index) if 0 <= index < 32 else "?",
                sorted(self._held),
            )

        if self._held == before:
            return
        if self._on_held_changed is not None:
            try:
                self._on_held_changed(self.held_pads)
            except Exception:
                logger.exception("Motion32: pad-held listener failed")

    def _update_control_from_script(self):
        """🔑 Keep every pad playable at all times. **This is the fix for swallowed notes.**

        The base class does:

        ```python
        takeover_pads = self._takeover_pads or len(self.pressed_pads) > 0
        mode = PlayableControl.Mode.listenable if takeover_pads else self._default_playable_mode
        for button in self.matrix:
            button.set_mode(mode)
        ```

        So **the moment any pad goes down, the whole matrix flips to `listenable`** — which
        consumes notes instead of passing them. That is deliberate for a drum rack, where
        holding a pad is meant to take the grid over for selection. It is exactly wrong for a
        keyboard: it swallowed the note that lit the pad, and made a second press behave
        differently from the first.

        `matrix_always_listenable=True` does **not** prevent this — it only sets the *default*
        mode, and the takeover overrides the default.

        We never take the pads over, so the mode is constant: `playable_and_listenable`. Notes
        always reach the track, and we always hear press/release for the LED.
        """
        for button in self.matrix:
            if self._is_dead(self._index_for(button)):
                # Claimed, so its note cannot leak; `listenable` means the script consumes it
                # and nothing is passed to the track. A dead key does nothing at all.
                button.set_mode(PlayableControl.Mode.listenable)
            else:
                button.set_mode(self._default_playable_mode)

    def _on_matrix_pressed(self, button):
        # Our bookkeeping first, so the light is correct even if the base class's
        # `pressed_pads` handling raises.
        self._note_held(button, True)
        super()._on_matrix_pressed(button)

    def _on_matrix_released(self, button):
        self._note_held(button, False)
        super()._on_matrix_released(button)

    # -- octave ------------------------------------------------------------
    @octave_up_button.pressed
    def octave_up_button(self, _button):
        self._nudge_octave(+1)

    @octave_down_button.pressed
    def octave_down_button(self, _button):
        self._nudge_octave(-1)

    def _octave_limits(self):
        """How far the octave may travel **given where A-H has put the root**.

        Two clamps, and the tighter wins: `OCTAVE_LIMIT` is the musical one (±3 is as far as
        anyone wants a keybed to jump), and `pads.safe_semitone_range` is the physical one
        (every pad must stay inside MIDI 0-127).

        The second used to be implicit in the first — the layout spans ~2½ octaves, so ±3 could
        not reach the edge. A-H moves the root by up to four more semitones downward, so at bank
        `A` the octave floor is **-2**, not -3. Deriving it means the invariant holds rather
        than being remembered. Do not re-collapse this back into the constant: see the note on
        `OCTAVE_LIMIT`.
        """
        # The window A-H has moved the layout to is what decides how much headroom is left, so
        # the range is asked for at the *current* root offset rather than at rest.
        lowest, highest = pads.safe_semitone_range(self.root_offset)
        # Octaves are whole, so round *inward* at each end: ceil on the floor, floor on the
        # ceiling. `-((-a) // b)` is integer ceil.
        low = max(-OCTAVE_LIMIT, -((-lowest) // 12))
        high = min(OCTAVE_LIMIT, highest // 12)
        return low, high

    def _nudge_octave(self, direction: int) -> None:
        low, high = self._octave_limits()
        octaves = self._octave_semitones // 12 + direction
        octaves = max(low, min(high, octaves))
        self.set_octave(octaves * 12)
        # **After** set_octave, and unconditionally. The bar answers a press, not a change:
        # at the clamp limit the offset does not move and `set_octave` returns early, but a
        # press that produced no feedback at all reads as a dead button rather than a limit.
        self._notify("Octave", self.octave_text)

    @property
    def octave(self) -> int:
        """Current transposition in octaves — 0 at rest. Drives the buttons' colour."""
        return self._octave_semitones // 12

    @property
    def octave_text(self) -> str:
        """What the notification bar shows for the current transposition."""
        return signed_label(self.octave)

    # -- A-H banking -------------------------------------------------------
    #
    # Eight one-line handlers rather than a loop, for the same reason the controls are declared
    # individually: `@bank_x_button.pressed` is a descriptor on the class, and the framework
    # resolves the handler by name. All eight funnel into `_select_bank`, which is the only
    # place the bank moves.
    @bank_a_button.pressed
    def bank_a_button(self, _button):
        self._select_bank(0)

    @bank_b_button.pressed
    def bank_b_button(self, _button):
        self._select_bank(1)

    @bank_c_button.pressed
    def bank_c_button(self, _button):
        self._select_bank(2)

    @bank_d_button.pressed
    def bank_d_button(self, _button):
        self._select_bank(3)

    @bank_e_button.pressed
    def bank_e_button(self, _button):
        self._select_bank(4)

    @bank_f_button.pressed
    def bank_f_button(self, _button):
        self._select_bank(5)

    @bank_g_button.pressed
    def bank_g_button(self, _button):
        self._select_bank(6)

    @bank_h_button.pressed
    def bank_h_button(self, _button):
        self._select_bank(7)

    def _select_bank(self, index: int) -> None:
        """Move the root to bank `index`. **Strict radio — a press selects, never toggles.**

        The same call the mode buttons make (`mappings.py`): re-pressing the selected bank is a
        no-op on the layout, not a fallback to E. "Toggle off" has no well-defined destination
        for a radio of eight.
        """
        self.set_bank(index)
        # **After** set_bank, and unconditionally — the same rule as `_nudge_octave`. The bar
        # answers a *press*, not a change: re-pressing the current bank moves nothing and
        # `set_bank` returns early, but a press with no feedback at all reads as a dead button.
        self._notify(NOTIFICATION_TITLE, self.root_shift_text)

    @property
    def bank_index(self) -> int:
        """Which A-H button is selected. 4 (`E`) at rest."""
        return self._bank_index

    @property
    def bank_letter(self) -> str:
        return pads.BANK_LETTERS[self._bank_index]

    @property
    def root_degrees(self) -> int:
        """How far A-H has moved the root, in **scale degrees** (bottom-row pads). 0 at `E`."""
        return pads.bank_step(self._bank_index) * DEGREES_PER_BANK_STEP

    @property
    def root_offset(self) -> int:
        """The layout's total degree offset: the programmatic base plus wherever A-H sits.

        One number, so `pad_pitches` and `pad_roles` cannot be handed different windows.
        """
        return self._root_offset + self.root_degrees

    @property
    def root_shift_text(self) -> str:
        """What the notification bar shows for the root shift — `"0"` at rest, else signed."""
        return signed_label(self.root_degrees)

    def _refresh_bank_leds(self) -> None:
        """Light the selected bank and only the selected bank.

        Unlike Octave — where two buttons read one shared value and each shows *its own*
        direction — this is a plain radio, so `is_on` is an equality test. Every button is
        written on every change, because the one being turned *off* needs the message just as
        much as the one being turned on.
        """
        for index, control in enumerate(self._bank_controls()):
            control.is_on = index == self._bank_index

    def _bank_controls(self):
        """The eight A-H controls in bank order. **One list — index here and nowhere else.**"""
        return (
            self.bank_a_button,
            self.bank_b_button,
            self.bank_c_button,
            self.bank_d_button,
            self.bank_e_button,
            self.bank_f_button,
            self.bank_g_button,
            self.bank_h_button,
        )

    def _refresh_octave_leds(self) -> None:
        """Each button is white when the offset is engaged **in its own direction**.

        `[INF]` from the capture: at +1 the host wrote *Up* white and never touched Down. Had
        the rule been "either button lights whenever the offset is non-zero", Down would have
        been written too. We have not seen a negative offset on the wire to confirm the mirror
        image, so this is inference from an absence — a capture of Octave Down from rest would
        settle it.
        """
        octaves = self.octave
        self.octave_up_button.is_on = octaves > 0
        self.octave_down_button.is_on = octaves < 0

    def update(self):
        # Layer grabs reset the button elements, so the engaged colour has to be re-asserted
        # afterwards or the offset silently stops showing after a mode change.
        super().update()
        if self.is_enabled():
            self._refresh_octave_leds()
            self._refresh_bank_leds()

    # -- layout ------------------------------------------------------------
    def set_root_offset(self, offset: int) -> None:
        """Move the root, in **white-key degrees**.

        This is the **programmatic base**; A-H adds to it (`root_offset` is the sum). Nothing
        moves it today — it exists so a future caller can reposition the window without
        disturbing which bank button is lit.
        """
        offset = int(offset)
        if offset == self._root_offset:
            return
        self._root_offset = offset
        self._recompute()

    def set_bank(self, index: int) -> None:
        """Select an A-H bank, sliding the keybed by whole bottom-row pads. `E` (4) is rest.

        Clamped rather than wrapped: the buttons are a fixed row of eight, so an out-of-range
        index has no button to light and wrapping would make `A` and `H` neighbours on a
        control whose whole point is left-to-right travel.
        """
        index = max(0, min(pads.BANK_COUNT - 1, int(index)))
        if index == self._bank_index:
            return
        self._bank_index = index
        # ⚠️ **The bank wins; the octave yields.** A-H is an explicit selection — pressing `A`
        # must give you `A` — while the octave is a range control, so it is the one that gives
        # way when the two together would push a pad off the end of MIDI. A bottom-lane pad is
        # never legitimately dead: the gaps are missing *black* keys and the bottom row is
        # sixteen white keys, so a dark one there means the layout left MIDI's range.
        low, high = self._octave_limits()
        octaves = max(low, min(high, self._octave_semitones // 12))
        self._octave_semitones = octaves * 12
        self._recompute()
        self._refresh_bank_leds()
        self._refresh_octave_leds()

    def set_octave(self, semitones: int) -> None:
        """Transpose every pad. Octave +/- moves this by 12 (`Motion32_Pads_...` §4)."""
        semitones = int(semitones)
        if semitones == self._octave_semitones:
            return
        self._octave_semitones = semitones
        self._recompute()
        self._refresh_octave_leds()

    def _recompute(self) -> None:
        """Re-derive the layout and push **both** halves of it into the elements.

        ⚠️ Two passes, and a layout change needs both:

        * `_update_note_translations()` sets each pad's **identifier** (which note it is) and
          `enabled`;
        * `_update_control_from_script()` sets each pad's **mode**, and mode is the only thing
          that makes a dead pad silent.

        Calling only the first leaves the mode stale, so a pad that has just *become* dead keeps
        `playable_and_listenable` and still sounds, while one that has just become alive keeps
        `listenable` and stays mute. That is invisible while the gaps never move — an octave
        shift does not move them — and appears the moment A-H banking or a non-diatonic scale
        does. Both are called here, always, on every layout change.

        **Octave and A-H are different transforms and must not be summed.** Octave is a rigid
        semitone transposition — the whole shape moves and the gaps stay put. A-H is a *degree*
        shift: it slides the window along the piano, so which positions have a black key above
        them changes and **the gaps move with it**. They are the two arguments to `pad_pitches`,
        not one term.

        That distinction is exactly what the first hardware run exposed. Built as a semitone
        shift, banking left `pad_roles` identical, `set_pad_roles` correctly saw no change, and
        the keybed never redrew — a rigid transposition genuinely has nothing to repaint.
        """
        before = self._pitches
        # Ask the provider *now*, with the current offsets. A-H and Octave both land here, so
        # regenerating is what makes them work in every layout rather than only in the piano.
        provided = None
        if self._layout_provider is not None:
            try:
                provided = self._layout_provider(self.root_offset, self._octave_semitones)
            except Exception:
                logger.exception("Motion32: the layout provider failed; falling back to the piano")
                provided = None
        if provided is None:
            self._pitches = pads.pad_pitches(self.root_offset, self._octave_semitones)
            self._provided_roles = None
        else:
            pitches, roles = provided
            self._pitches = list(pitches)
            self._provided_roles = list(roles)
        # Only on change — never per note.
        self._update_note_translations()
        self._update_control_from_script()
        # The lights come from the list we just built, not from a second copy of the offsets.
        self._report_roles()

        # 🔍 **Diagnostic, and it earns its place.** "The pads did not transpose" has two very
        # different causes and no way to tell them apart from the hardware: either this method
        # never computed a new layout, or it did and the framework did not carry the new
        # identifier into Live's MIDI map. Logging what we computed *and* what actually landed
        # on the element separates them in one line of Log.txt.
        #
        # Bounded like the pad-press log (§6b-6): a layout change is a deliberate user action,
        # not a stream, but a stuck listener could still make it one.
        if self._layouts_logged < self.MAX_LOGGED_LAYOUTS:
            self._layouts_logged += 1
            landed = None
            for button in self.matrix:
                if self._index_for(button) == 0:
                    landed = getattr(button, "identifier", None)
                    break
            logger.info(
                "Motion32 layout: bank=%s octave=%+d root=%+d degrees -> pad1 was %s, "
                "now %s, element identifier now %s",
                self.bank_letter,
                self.octave,
                self.root_degrees,
                before[0] if before else None,
                self._pitches[0],
                landed,
            )

    def _index_for(self, button) -> int:
        """Matrix coordinate -> flat pad index, matching `leds.PadLeds` and `pads.py`.

        `elements.py` declares the matrix as two rows of 16 in lane order, so row 0 is lane 0
        (notes 36-51) and row 1 is lane 1 (52-67). Keeping the same flattening everywhere is
        what lets a pad's LED index be simply `note - 36`.

        ⚠️ `button.coordinate` is **`(y, x)` — row first**. Verified from the bytecode of
        `DrumGroupComponent._button_coordinates_to_pad_index`, which opens with
        `y, x = coordinates`. Unpacking it the other way silently transposes the keyboard,
        which would look like a plausible-but-wrong layout rather than an error.

        (The drum group additionally *inverts* y, because drum racks number bottom-up. That is
        drum-specific: our two lanes are already in declaration order, so no inversion.)
        """
        try:
            row, column = button.coordinate
        except (AttributeError, TypeError, ValueError):
            return getattr(button, "index", 0)
        return row * pads.PADS_PER_LANE + column

    # -- PlayableComponent hooks -------------------------------------------
    def _note_translation_for_button(self, button):
        """`(identifier, channel)` for one pad, or a dead identifier to disable it.

A real pad gets its **layout pitch** — that is the transposition, and it works: the
        keyboard plays a piano.

        🔑 **A dead pad gets its own note on a SEPARATE CHANNEL.** The framework keys a control
        by `(identifier, channel)`, so this makes it unique, and uniqueness is the whole problem:

        * an identifier **≥ 128** disables the pad, and a disabled element is *released*, so its
          raw note floats loose;
        * its own note on the **keyboard** channel collides with whichever real pad is currently
          transposed to that number — 54, 58, 61 and 65 are all live translation targets, which
          is why pressing a dead pad fired controls 26 / 28 / 30 and lit their pads instead.

        On its own channel it is **claimed** (so nothing leaks), **unique** (so it cannot be
        confused with a real pad), and silenced by its `listenable` mode.
        """
        index = self._index_for(button)
        pitch = self._pitches[index] if 0 <= index < len(self._pitches) else None
        if pitch is None or not 0 <= pitch < 128:
            return (pads.note_for_index(max(0, min(31, index))), DEAD_PAD_CHANNEL)
        return (pitch, KEYBOARD_CHANNEL)

    def _is_dead(self, index: int) -> bool:
        return not (0 <= index < len(self._pitches)) or self._pitches[index] is None

    def _update_note_translations(self):
        """🔑 Set the identifier on **every** pad, including the disabled ones.

        The base class only calls `_set_button_control_properties` for buttons it is enabling:

        ```python
        for button in self.matrix:
            if self._button_should_be_enabled(button):
                self._set_button_control_properties(button)
                button.enabled = True
            else:
                button.enabled = False
        ```

        So a disabled pad is never given an identifier and **keeps its declared raw note** —
        54, 58, 61, 65 for our four gaps. Those are real notes, and they are also translation
        *targets* for other pads: at the default octave three of the four collide, at +12 all
        four do, at -12 none. Two controls on one identifier means a press can be delivered to
        the wrong control — which is precisely the reported symptom set: dead pads playing
        notes, dead pads lighting *a different* pad, and some lit pads not turning green
        because their event went elsewhere. It was octave-dependent because the overlap is.

        Assigning the properties unconditionally is what gives every dead pad the identifier
        `_note_translation_for_button` chose for it: **its own note on `DEAD_PAD_CHANNEL`**. A
        control is keyed by `(identifier, channel)`, so that is unique, claimed, and silenced by
        its `listenable` mode.

        ⚠️ This docstring used to say dead pads move to an identifier "at or above 128". That
        was attempt 2 in the table at the top of this module, and it **failed** — an identifier
        ≥ 128 disables the pad, and a disabled element is released, so its raw note floats
        loose. Corrected 2026-08-03; the code has been on the channel strategy since it shipped.
        """
        for button in self.matrix:
            enabled = self._button_should_be_enabled(button)
            self._set_button_control_properties(button)
            button.enabled = enabled

    # `_update_button_color` is deliberately NOT overridden — see the module docstring.
    # Leaving the base class's empty hook keeps `leds.PadLeds` the sole writer of the pad
    # addresses. If this component ever needs to own the colour too, `PadLeds` must stop
    # painting them in the same change, not alongside it.
