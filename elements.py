"""Physical Motion 32 controls.

Element/kwarg patterns here follow the factory Atom SQ script (verified against its
bytecode and the readable Atom SQ Plus add-on), which targets the same framework
version Live 12 ships — so `add_encoder_matrix(..., map_mode=...,
sensitivity_modifier=...)` and `add_button(..., is_rgb=True)` are known-good
signatures rather than guesses.

Naming trap worth remembering: an element name that normalizes onto an `add_*`
method shadows it (`"Add_Button"` breaks `add_button()`), hence `Add_Mode_Button`
if/when the Add button gets wired.
"""

import logging

from ableton.v3.control_surface import (
    MIDI_CC_TYPE,
    MIDI_NOTE_TYPE,
    MIDI_PB_TYPE,
    ElementsBase,
    MapMode,
    ScriptForwarding,
)
from ableton.v3.control_surface.elements import ButtonElement, EncoderElement

from . import midi

logger = logging.getLogger(__name__)


class MotionEncoderElement(EncoderElement):
    """An encoder that never writes to its own CC, because that CC is its LED.

    On the Motion 32 an encoder halo has **no address of its own** — it is addressed by the
    encoder's CC (`Motion32_Control_Surface_Definition.md` §2.5). So the element and the halo
    are the same address, and every byte the element sends lands on the light.

    Two framework paths write there, and only one of them is a flag we can set:

    * **parameter feedback** — handled by `is_feedback_enabled=False`;
    * **element reset** — `install_connections()` calls `reset()`, and `reset_state()` sends the
      element's *off* value. This fires on every layer grab, i.e. every mode change, and no flag
      covers it.

    Racing it back (set the halo again, slightly later) is what we tried first, and it is a bad
    fix: the halo visibly flickers and any framework write we don't have an event for wins until
    the next re-assert. Turning and clicking the wheel kept knocking it out that way.

    So instead: **we own the address, exclusively.** The element keeps all of its input
    behaviour and internal bookkeeping — `reset()` and `reset_state()` still run, so sensitivity
    state stays correct — but its outgoing bytes are dropped. `leds.py` is the only writer.

    Both `send_value` and `send_midi` are overridden because the send path differs between the
    reset and feedback routes, and the base class is shipped as bytecode.
    """

    def send_value(self, *a, **k):
        self._note_suppressed_write("send_value")
        return None

    def send_midi(self, *a, **k):
        self._note_suppressed_write("send_midi")
        # True means "handled" to the framework, so it doesn't try another route.
        return True

    def _note_suppressed_write(self, route):
        # Once per element per route, at debug level: enough to confirm on hardware which path
        # the framework actually used, without flooding the log on every mode change.
        seen = self.__dict__.setdefault("_motion_suppressed", set())
        if route not in seen:
            seen.add(route)
            logger.debug(
                "Motion32: suppressing %s on %s — that CC is the LED, leds.py owns it",
                route,
                self.name,
            )


def create_motion_encoder(identifier, name=None, **k):
    """Factory in the shape `ElementsBase` expects: `factory(identifier, name=..., **k)`."""
    return MotionEncoderElement(identifier, name=name, **k)


class MotionInputOnlyButtonElement(ButtonElement):
    """A button that receives normally but never sends LED feedback.

    Used for shared input/output addresses where the outbound meaning is *not* this
    button. The wheel push is CC 0x78 on input, but host->device CC 0x78 is touch-strip
    2 LED 9, so any framework button feedback would light the strip instead of the wheel.
    """

    def send_value(self, *a, **k):
        self._note_suppressed_write("send_value")
        return None

    def send_midi(self, *a, **k):
        self._note_suppressed_write("send_midi")
        return True

    def _note_suppressed_write(self, route):
        seen = self.__dict__.setdefault("_motion_suppressed", set())
        if route not in seen:
            seen.add(route)
            logger.debug(
                "Motion32: suppressing %s on %s — input-only shared address",
                route,
                self.name,
            )


def create_motion_input_button(identifier, name=None, **k):
    """Factory for a receive-only button at a direction-overloaded address."""
    return MotionInputOnlyButtonElement(identifier, name=name, **k)


class Elements(ElementsBase):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)

        # Shift is momentary and creates framework-managed modified controls.
        self.add_modifier_button(midi.CC_SHIFT, "Shift_Button", channel=midi.MIDI_CHANNEL)

        # is_rgb=True so LED feedback sends the R/G/B messages (0xB1/0xB2/0xB3) plus the state
        # byte, giving bright, colored buttons instead of the dim state-only light.
        self.add_button(midi.CC_TAP, "Tap_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)
        self.add_button(midi.CC_RECORD, "Record_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)
        self.add_button(midi.CC_PLAY, "Play_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)
        self.add_button(midi.CC_STOP, "Stop_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)

        self.add_modified_control(self.tap_button, self.shift_button)
        self.add_modified_control(self.play_button, self.shift_button)
        self.add_modified_control(self.stop_button, self.shift_button)
        self.add_modified_control(self.record_button, self.shift_button)

        # -- Phase 2: encoders -------------------------------------------------
        # Relative, sign-magnitude with the sign bit at 0x40 -> LinearSignedBit.
        # Shift doubles as the fine/sensitivity modifier, which mirrors the device's
        # own "Fine" concept and the Atom SQ idiom.
        #
        # Do NOT pass `channel=` here. `add_matrix` supplies `channel` to
        # `create_encoder` itself, so an explicit one collides:
        #   TypeError: create_encoder() got multiple values for keyword argument 'channel'
        # ...which fails the whole script load. The singular `add_encoder` *does* accept
        # `channel` (see the wheel below) — the conflict is specific to the matrix
        # helpers. The device is on MIDI channel 1 (0-based 0), which is the default.
        # `is_feedback_enabled=False` is load-bearing on this device. An EncoderElement sends
        # parameter-value feedback **on its own CC**, and on the Motion that CC *is* the encoder
        # halo address (0x0E-0x15 — the halo has no address of its own). So Live was writing the
        # parameter value into the halo's state byte a moment after we set it: the halos lit in
        # the right colour and then went dim. Turning the element's feedback off leaves the halo
        # to us (leds.py).
        # ⚠️ Build this with the GENERIC `add_matrix`, not `add_encoder_matrix`.
        #
        # `add_encoder_matrix` hard-codes `element_factory=create_encoder` and forwards it to
        # `add_matrix` as a keyword, so passing our own is a *duplicate* and the whole script
        # fails to load:
        #   TypeError: ElementsBase.add_matrix() got multiple values for keyword argument
        #              'element_factory'
        # This is the same trap as `channel=` above, and it is not specific to encoders —
        # `add_button_matrix` hard-codes it too. Only `add_matrix` and `add_element` take a
        # factory. (Confirmed by decompiling `elements_base.pyc`: both wrappers carry the const
        # tuple `('channels', 'element_factory')`, which is the kwargs they pass on.)
        #
        # MotionEncoderElement is the stock element with its outgoing writes suppressed, so the
        # framework cannot darken the halo — see the class docstring.
        self.add_matrix(
            [list(midi.CC_ENCODERS)],
            "Encoders",
            element_factory=create_motion_encoder,
            map_mode=MapMode.LinearSignedBit,
            sensitivity_modifier=self.shift_button,
            is_feedback_enabled=False,
        )

        # Capacitive touch, one per encoder. A matrix so it can bind to a control_list
        # on the screen component, which uses touch to reveal the parameter value.
        # (No `channel=` on matrix helpers — see the note above.)
        self.add_button_matrix(
            [list(midi.CC_ENCODER_TOUCH)],
            "Encoder_Touch_Buttons",
        )

        # -- Pads: 32, in two lanes of 16 --------------------------------------
        # Notes, not CCs — `msg_type=MIDI_NOTE_TYPE`. Row 0 is lane 0 (notes 36-51, the
        # bottom lane / white keys in the device's Keys layout); row 1 is lane 1 (52-67).
        # Keeping that order means a pad's LED index in `leds.PadLeds` is simply
        # `note - 36`, so the element grid and the LED group cannot drift apart.
        #
        # In native mode a pad's note is FIXED — the device applies no Keys/Scale/Chord
        # transform (`Motion32_Scale_and_Chord_Engine.md` §2), so these addresses are the
        # whole story for both input and LED output.
        #
        # `is_rgb=True` is correct here even though nothing binds these yet: a NOTE-type
        # element derives its colour statuses from its own message type, so the skin's
        # `ColorPart(channel=1/2/3)` lands on `0x91`/`0x92`/`0x93` — the pad RGB addresses —
        # not on the `0xB1`-`0xB3` used by buttons.
        #
        # ⚠️ **Ownership.** A pad's LED address *is* its note address, the same shared-address
        # property that bit the encoder halos (§6b-10). The difference: for an encoder the
        # framework wrote *parameter values* to a light, which is meaningless; for a pad it
        # writes *colour*, which is exactly right. So these are deliberately **not** suppressed
        # the way `MotionEncoderElement` is — suppressing them would stop Session mode ever
        # lighting a clip. The rule is per-pad instead: while no component has bound them,
        # `leds.PadLeds` is the only writer; when Session binds them, the framework becomes the
        # writer for those pads and `PadLeds` must yield. One owner at a time, either way.
        self.add_button_matrix(
            [list(midi.PAD_NOTES[:16]), list(midi.PAD_NOTES[16:])],
            "Pads",
            msg_type=MIDI_NOTE_TYPE,
            is_rgb=True,
        )

        # -- Shift + pads: the command overlay (Phase 8) -----------------------
        # `add_modified_control` handles a **matrix** as well as a single control — it detects
        # `ButtonMatrixElement` and routes to `_add_modified_matrix`, which maps a modified
        # element over `matrix._orig_buttons` and then calls `_add_raw_elements`. So this one
        # line publishes both `pads_with_shift` (a 2x16 matrix) and `pads_with_shift_raw[i]`.
        #
        # 🔑 **A bound modified element OUTRANKS the plain binding.** `ComboElement` carries
        # `priority_increment = 0.5`, so while Shift is held a bound Shift-pad takes the press
        # and the keyboard underneath never sees it — the pad fires its command and plays no
        # note. That is the whole mechanism, and it is the framework's, not ours.
        #
        # ⚠️ **An UNBOUND modified element claims nothing.** Priority is asserted by being in a
        # live layer; a combo element nobody binds is not connected at all, so its pad would
        # still play its note while Shift is held. That is why the top lane is bound to a
        # Background below rather than simply left alone — "unbound" and "consumed" are
        # opposites here, the same lesson as the four dead keyboard pads (`keyboard.py`).
        self.add_modified_control(self.pads, self.shift_button, name="Pads_With_Shift")

        # The bottom lane (row 0 = notes 36-51) is the 16-slot command layer, matching the
        # factory: `padMode=Commands`, pads turn white, 16 edit commands on pad indices 0-15.
        #
        # A submatrix rather than sixteen `pads_with_shift_raw[i]` bindings, so the component
        # can take them as one `control_list` and read the slot off `button.index` — the same
        # idiom `encoder_touch_buttons` already uses. `add_submatrix` slices
        # `matrix.submatrix[columns, rows]`, so `rows=(0, 1)` is row 0 alone.
        self.add_submatrix(self.pads_with_shift, "Command_Pads", rows=(0, 1))

        # The top lane, while Shift is held. Bound to a Background purely to **consume** it:
        # `BackgroundComponent` grabs an element with a `NopControl`, which is exactly "claimed,
        # so nothing leaks, and nothing happens". Without this the accidentals would still sound
        # under Shift while the bottom lane ran commands — half a keybed of notes and half of
        # destructive edits, which is the worst of both.
        self.add_submatrix(self.pads_with_shift, "Muted_Pads_With_Shift", rows=(1, 2))

        # Octave +/- — transpose the whole keybed by 12 semitones. Singular add_button, so
        # channel= is fine here (only the *matrix* helpers supply it themselves).
        self.add_button(midi.CC_OCTAVE_UP, "Octave_Up_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)
        self.add_button(midi.CC_OCTAVE_DOWN, "Octave_Down_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)

        # -- A-H pad banks (CC 0x00-0x07) --------------------------------------
        # Declared individually rather than as a matrix, matching the factory Atom SQ (which
        # also names its bank buttons one by one) and matching `keyboard.py`, which declares
        # eight `ButtonControl`s because the `control_list` colour-forwarding path lives in
        # v2 and is not in the repo to read. Singular `add_button`, so `channel=` is fine.
        for index, cc in enumerate(midi.CC_BANK_BUTTONS):
            self.add_button(
                cc,
                f"Bank_{'ABCDEFGH'[index]}_Button",
                channel=midi.MIDI_CHANNEL,
                is_rgb=True,
            )

        # -- Control-focus buttons (Song / Plugin / Edit / Mix) ----------------
        # These select the main mode; Plugin is what reveals the device screen.
        self.add_button(midi.CC_SONG, "Song_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)
        self.add_button(midi.CC_PLUGIN, "Plugin_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)
        self.add_button(midi.CC_EDIT, "Edit_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)
        self.add_button(midi.CC_MIX, "Mix_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)

        # Shift+Song toggles Live's Session/Arrangement view.
        self.add_modified_control(self.song_button, self.shift_button)

        # -- Screen-mode buttons -----------------------------------------------
        # Scale enters Scale mode. Control is the way *out* of it — see `mappings.py`: it returns
        # to whichever main mode was showing before, which is why it is a plain button here and
        # not a mode button of its own.
        self.add_button(midi.CC_SCALE, "Scale_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)
        self.add_button(midi.CC_CONTROL, "Control_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)

        # -- LCD soft buttons, under/over the screen ---------------------------
        # Indices 0-3 are the top row (over the screen), 4-7 the bottom row — confirmed from
        # skin.xml's LcdButtonTopRow/BottomRow forms.
        #
        # ⚠️ **A matrix, not eight singles, even though Song mode binds them one at a time.**
        # Mix mode needs all eight as a *group* (`arm_buttons` on the Mixer, one per channel
        # strip), and a plural control needs something iterable. Declaring a matrix *and*
        # eight separate buttons would put two elements on each CC — one address, two
        # potential writers, which is the trap that cost three attempts on the encoder halos.
        #
        # `add_matrix` also publishes `<name>_raw[i]` for the individual elements (from
        # `_add_raw_elements` in `elements_base.pyc`), which is how Song mode still binds them
        # singly — the same idiom `SONG_ENCODERS` already uses for `encoders_raw[i]`.
        # No `channel=` on a matrix helper.
        self.add_button_matrix(
            [list(midi.CC_LCD_BUTTONS)],
            "Soft_Buttons",
            is_rgb=True,
        )

        # -- Solo / Mute -------------------------------------------------------
        # Act on the focused track via Target_Channel_Strip.
        self.add_button(midi.CC_SOLO, "Solo_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)
        self.add_button(midi.CC_MUTE, "Mute_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)

        # -- Preset Up / Down --------------------------------------------------
        # Used in Plugin mode to step the device selection along the track's chain.
        self.add_button(
            midi.CC_PRESET_UP, "Preset_Up_Button", channel=midi.MIDI_CHANNEL, is_rgb=True
        )
        self.add_button(
            midi.CC_PRESET_DOWN, "Preset_Down_Button", channel=midi.MIDI_CHANNEL, is_rgb=True
        )

        # -- Navigation --------------------------------------------------------
        # Non-contiguous on this device (0x57/0x59/0x5A/0x66); not a typo.
        self.add_button(midi.CC_NAV_UP, "Up_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)
        self.add_button(midi.CC_NAV_DOWN, "Down_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)
        self.add_button(midi.CC_NAV_LEFT, "Left_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)
        self.add_button(midi.CC_NAV_RIGHT, "Right_Button", channel=midi.MIDI_CHANNEL, is_rgb=True)

        # -- Screen wheel ------------------------------------------------------
        # Same collision as the encoder halos: the wheel LED lives at the wheel's own CC.
        # `add_encoder` hard-codes `create_encoder`, so the wheel goes through the generic
        # `add_element(name, factory, *a, **k)` to get the same write-suppressed element.
        # Without this the wheel halo drops out while turning or clicking, which is exactly
        # the reported behaviour.
        self.add_element(
            "Wheel_Encoder",
            create_motion_encoder,
            midi.CC_WHEEL,
            channel=midi.MIDI_CHANNEL,
            map_mode=MapMode.LinearSignedBit,
            is_feedback_enabled=False,
        )
        # Wheel push is **input only**. On the wire, input CC 0x78 is the wheel click, but
        # output CC 0x78 is touch-strip 2 LED 9. The click's result is shown by the screen
        # or menu it controls; there is no planned press LED. A normal `add_button` would
        # let ButtonControl/set_light write BasicColors to 0x78 and flicker the strip LED.
        self.add_element(
            "Wheel_Push_Button",
            create_motion_input_button,
            midi.CC_WHEEL_PUSH,
            channel=midi.MIDI_CHANNEL,
        )

        # -- Touch strip 2 -- EXPERIMENT, see the hardware test below ----------
        #
        # ⚠️ **This is a test, not the finished Phase 9 strip work.** It exists to answer one
        # question that cannot be answered by reading code: *does declaring the strip stop its
        # pitch bend reaching the armed track?*
        #
        # Why it cannot be answered statically. `_install_forwarding()` computes
        # `should_consume_event` and passes it to `Live.MidiMap.forward_midi_cc()` as a fifth
        # argument — but `forward_midi_pitchbend()` is called with **three** arguments and the
        # flag is not among them (verified in `control_surface.pyc` bytecode: `CALL 5` versus
        # `CALL 3`). So `exclusive` and `non_consuming` compile to an identical call for pitch
        # bend, and the script has no way to *request* consumption. Whether Live consumes a
        # forwarded pitch bend **inherently** is a property of its C++ side. Only hardware knows.
        #
        # Firmware context (`Resources/FirmwareAnalysis/strip_translation_chain.md`): in the
        # native host state the `8F 00 7F` handshake selects, strip position is hard-coded to
        # pitch bend — `FUN_10102e84` bypasses the strip assignment record entirely. There is no
        # table, command or setting that makes strip 2 send anything else. So the device *will*
        # send this; the only question is whether we can absorb it.
        #
        # ⚠️ **Strip 1 is deliberately NOT declared.** Its pitch bend already reaches the armed
        # instrument correctly and that is the behaviour we want to keep. Touching it risks the
        # one strip that works.
        #
        # `is_feedback_enabled=False` because the strip's LED bar lives at its own CC addresses
        # (`CC_TOUCHSTRIP_2_LEDS`), not at a pitch-bend address — any feedback write here would
        # be meaningless at best.
        # ⚠️ **`script_forwarding` is NOT a constructor kwarg** — this cost a failed script load.
        # `InputControlElement.__init__` takes exactly `msg_type, channel, identifier,
        # sysex_identifier, request_rebuild_midi_map, send_should_depend_on_forwarding,
        # is_feedback_enabled`; anything else falls through `**k` to `object.__init__` and raises
        # `TypeError: object.__init__() takes exactly one argument`. It is a **property with a
        # setter** that assigns `_script_forwarding` and calls `_request_rebuild` itself, so it is
        # assigned after construction — see `_install_strip2_probe` in `__init__.py`.
        self.add_encoder(
            0,  # pitch bend carries no CC number; the channel is the whole address
            "Touch_Strip_2",
            msg_type=MIDI_PB_TYPE,
            channel=midi.TOUCHSTRIP_2_CHANNEL,
            is_feedback_enabled=False,
        )
        # ⚠️ **Set forwarding here, not in `setup()`.** The property's setter calls
        # `_request_rebuild`, which is the `request_rebuild_midi_map` callable handed to the
        # element at construction — and if that was never wired, the setter silently does
        # nothing. `setup()` runs *after* the first `build_midi_map`, so a late assignment can
        # leave the element consuming (Live already claimed the address) while never registering
        # in `_forwarding_registry`, which is exactly "strip 2 goes dead and the script sees
        # nothing". Assigning during construction means the first map build already knows.
        self.touch_strip_2.script_forwarding = ScriptForwarding.exclusive

        # -- Touch-strip contact sensors --------------------------------------
        #
        # 🐛 **CC 0x7B is All Notes Off to Live.** Touching strip 2 silences held notes, because
        # CC 123 is the standard All-Notes-Off controller and Live obeys it. §5.2 records the
        # collision; this is it happening on hardware. Consuming the CC is the fix, and unlike
        # pitch bend it is *available*: `forward_midi_cc` takes `should_consume_event` as its
        # fifth argument, so `exclusive` genuinely stops Live seeing it.
        #
        # Input-only elements, for the same reason as the wheel push: these addresses carry the
        # strip **LED-bar mode** host->device, so any framework feedback write would drive the
        # LEDs instead of doing nothing. `leds.py` owns that direction.
        self.add_element(
            "Touch_Strip_1_Button",
            create_motion_input_button,
            midi.CC_TOUCHSTRIP_1_BUTTON,
            msg_type=MIDI_CC_TYPE,
            channel=midi.MIDI_CHANNEL,
        )
        self.add_element(
            "Touch_Strip_2_Button",
            create_motion_input_button,
            midi.CC_TOUCHSTRIP_2_BUTTON,
            msg_type=MIDI_CC_TYPE,
            channel=midi.MIDI_CHANNEL,
        )
        self.touch_strip_1_button.script_forwarding = ScriptForwarding.exclusive
        self.touch_strip_2_button.script_forwarding = ScriptForwarding.exclusive

        # HARDWARE TEST: if Live is not delivering CC 0x7B because our declaration is on the
        # wrong channel, these catchers should reveal it. MIDI Monitor reports the touch event
        # as channel 1, so the normal element above should be enough; channels 2-16 are only
        # here to close the loophole before we blame Live's All Notes Off handling.
        for channel in range(1, 16):
            self.add_element(
                f"Touch_Strip_2_Button_Channel_{channel + 1}",
                create_motion_input_button,
                midi.CC_TOUCHSTRIP_2_BUTTON,
                msg_type=MIDI_CC_TYPE,
                channel=channel,
            )
            getattr(
                self, f"touch_strip_2_button_channel_{channel + 1}"
            ).script_forwarding = ScriptForwarding.exclusive
