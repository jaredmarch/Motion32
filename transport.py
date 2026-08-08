"""Motion 32 transport component.

**Subclasses the framework's `TransportComponent`** rather than replacing it. That matters
for more than tidiness: the framework version already owns the controls Song mode needs —
`arrangement_position_encoder`, `loop_start_encoder`, `loop_length_encoder`,
`tempo_coarse_encoder`, `tempo_fine_encoder`, `cue_encoder` — plus `play_button`,
`stop_button`, `tap_tempo_button`, `loop_button`, `metronome_button` and
`capture_midi_button`. The earlier version of this file re-implemented four of those
buttons against the Live API and inherited none of the encoders, so Song mode had nothing
to map.

What is left here is the one thing the framework's transport genuinely lacks: a **record
button**. (Live's arrangement/session record lives in the `Recording` and
`View_Based_Recording` components, which are shaped around record *modes*; a plain "toggle
`song.record_mode`" is what the Motion's Record key should do.)

LED colours come from the skin, not from code — `skin.py` supplies the `Transport.*` keys
the framework asks for, and `create_skin` merges ours over the framework defaults. Undo is
the `Undo_Redo` component's job, mapped to Shift+Stop.
"""

import logging

from ableton.v3.base import listens
from ableton.v3.control_surface.components import TransportComponent
from ableton.v3.control_surface.controls import ButtonControl

logger = logging.getLogger(__name__)


class MotionTransportComponent(TransportComponent):

    # The framework has no record button; this one flashes white on press like the rest of
    # the Motion's momentary keys.
    record_button = ButtonControl(
        color="Transport.RecordOff",
        pressed_color="Transport.Flash",
    )

    # A *second* loop control. The framework's `loop_button` is already bound to Shift+Play
    # globally, and one control cannot be bound to two elements — so a soft button that also
    # toggles the loop needs its own control rather than a second binding.
    loop_toggle_button = ButtonControl(
        color="Transport.LoopOff",
        pressed_color="Transport.Flash",
    )

    # The framework has no Back-to-Arrangement control at all (nothing in the tree references
    # `back_to_arranger`), so this is ours. Live sets `song.back_to_arranger` True once
    # session playback has overridden the arrangement; clearing it returns to the arrangement.
    # The LED therefore means "there is something to go back to".
    back_to_arrangement_button = ButtonControl(
        color="Transport.BackToArrangementOff",
        pressed_color="Transport.Flash",
    )

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        #: Skin names `_set_color` has already failed on, so the log says it once rather than
        #: on every transport event. Assigned here rather than lazily on `self.__dict__`
        #: because `test_no_self_reference_is_undefined` resolves every `self.X` against the
        #: class and the framework, and a name that only ever appears inside a `setdefault`
        #: is invisible to it.
        self._colour_failures = set()
        self._on_record_mode_changed.subject = self.song
        self._on_loop_changed.subject = self.song
        self._on_back_to_arranger_changed.subject = self.song
        self._refresh_record_led()
        self._refresh_loop_led()
        self._refresh_back_to_arrangement_led()

    @record_button.pressed
    def record_button(self, _):
        self.song.record_mode = not self.song.record_mode

    # *a because a `listens` handler receives whatever the notifier passes, which varies by
    # property; accepting it keeps the handler correct instead of raising inside a callback.
    @listens("record_mode")
    def _on_record_mode_changed(self, *a):
        self._refresh_record_led()

    @loop_toggle_button.pressed
    def loop_toggle_button(self, _):
        self.song.loop = not self.song.loop

    @listens("loop")
    def _on_loop_changed(self, *a):
        self._refresh_loop_led()

    def _refresh_loop_led(self):
        self._set_color(
            self.loop_toggle_button,
            "Transport.LoopOn" if self._song_flag("loop") else "Transport.LoopOff",
        )

    @back_to_arrangement_button.pressed
    def back_to_arrangement_button(self, _):
        try:
            self.song.back_to_arranger = False
        except (RuntimeError, AttributeError):
            # A press that does nothing and says nothing is indistinguishable from a dead
            # button; a raise inside a Live callback can wedge the surface. So: log, continue.
            logger.exception("Motion32: could not clear back_to_arranger")

    @listens("back_to_arranger")
    def _on_back_to_arranger_changed(self, *a):
        self._refresh_back_to_arrangement_led()

    def _refresh_back_to_arrangement_led(self):
        self._set_color(
            self.back_to_arrangement_button,
            "Transport.BackToArrangementOn"
            if self._song_flag("back_to_arranger")
            else "Transport.BackToArrangementOff",
        )

    def _song_flag(self, name):
        try:
            return bool(getattr(self.song, name))
        except (RuntimeError, AttributeError):
            return False

    def _set_color(self, control, skin_name):
        """Setting `.color` at runtime is the v3 way to reflect state.

        Guarded so an API difference cannot take the surface down — the resting colour from the
        control declaration still shows. ⚠️ **But it must not be silent.** This was
        `except Exception: pass` until 2026-08-03, which meant a wrong skin name or a changed
        setter stopped that LED reflecting state *permanently* with nothing in `Log.txt` —
        exactly the failure that hid the missing `Session.Navigation` keys for a fortnight.

        Logged once per control, so a listener firing on every transport change cannot flood.
        """
        try:
            control.color = skin_name
        except Exception:
            if skin_name not in self._colour_failures:
                self._colour_failures.add(skin_name)
                logger.exception(
                    "Motion32: could not set %r on a transport LED; it will keep its "
                    "declared resting colour",
                    skin_name,
                )

    def _refresh_record_led(self):
        """Dim red at rest, full red when armed.

        Guarded because setting `.color` at runtime is the v3 way to reflect state, but an
        API difference here should not take the surface down — the resting colour from the
        control declaration still shows.
        """
        self._set_color(
            self.record_button,
            "Transport.RecordOn" if self._song_flag("record_mode") else "Transport.RecordOff",
        )
