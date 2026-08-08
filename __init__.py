"""Ableton Live 12 MIDI Remote Script for Fender Motion 32."""

from __future__ import absolute_import, print_function, unicode_literals

import logging

from ableton.v3.control_surface import (
    ControlSurface,
    ControlSurfaceSpecification,
    create_skin,
)
from ableton.v3.control_surface.capabilities import (
    AUTO_LOAD_KEY,
    CONTROLLER_ID_KEY,
    NOTES_CC,
    PORTS_KEY,
    REMOTE,
    SCRIPT,
    SYNC,
    controller_id,
    inport,
    outport,
)

from ableton.v3.control_surface.components import BackgroundComponent

from . import midi, runtime
from .commands import MotionCommandsComponent, MotionModifierComponent
from .display import MainView, MixerView, ParamsView, ScreenModel
from .notification import NotificationView
from .elements import Elements
from .keyboard import MotionKeyboardComponent
from .leds import EncoderLeds, PadLeds
from .mappings import create_mappings
from .menu import MenuView
from .mixpages import MotionMixPagesComponent
from .parameters import ParameterSource
from .protocol import MotionProtocol, as_hex
from .scalemode import MotionModeReturnComponent, MotionScaleComponent
from .sends import MotionSendsComponent
from .screen_component import MotionScreenComponent
from .skin import Skin
from .transport import MotionTransportComponent
from .wheel import MotionWheelComponent

# v3 ControlSurface has no log_message(); Live routes the stdlib logger to Log.txt.
logger = logging.getLogger(__name__)

# USB identity captured from hardware via `ioreg -p IOUSB -l` (decimal): Fender vendor 7896
# (0x1ED8), Motion 32 product 513 (0x0201); corroborated by UsbDeviceSignature d81e/0201.
_USB_VENDOR_ID = 7896
_USB_PRODUCT_IDS = [513]


def get_capabilities():
    """Expose one deep-integration input/output pair on "Motion 32 Main".

    USB IDs enable auto-detection; the device's separate Control/MCU port is not used.
    """
    return {
        CONTROLLER_ID_KEY: controller_id(
            vendor_id=_USB_VENDOR_ID,
            product_ids=_USB_PRODUCT_IDS,
            model_name=["Motion 32", "Motion 32 Main"],
        ),
        PORTS_KEY: [
            inport(props=[NOTES_CC, SCRIPT, REMOTE]),
            outport(props=[NOTES_CC, SYNC, SCRIPT, REMOTE]),
        ],
        AUTO_LOAD_KEY: True,
    }


def create_instance(c_instance):
    return Motion32(c_instance=c_instance)


class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    control_surface_skin = create_skin(skin=Skin)
    create_mappings_function = create_mappings

    # **Why toggles and enum lists took a dozen clicks to step.** Not encoder acceleration —
    # a framework default. `DEFAULT_QUANTIZED_PARAMETER_SENSITIVITY` is **0.1**
    # (`parameter_mapping_sensitivities.pyc`), i.e. a quantized parameter needs roughly ten
    # detents per step. 1.0 gives one step per click, which is what a detented encoder should
    # do. Continuous parameters keep the framework default of 1.0.
    quantized_parameter_sensitivity = 1.0
    continuous_parameter_sensitivity = 1.0

    # The framework sends these in order when the output port connects. Putting the identity
    # request here (rather than using identity_response_id_bytes) matches Studio Pro's actual
    # startup and avoids the framework's contiguous-id match failing on the Motion's reply
    # (which arrives as 08 00 00 26 — non-contiguous). We parse the reply ourselves in receive_midi.
    hello_messages = (
        midi.NATIVE_MODE_ON_MESSAGE,
        midi.IDENTITY_REQUEST_MESSAGE,
    )

    # Always leave the Motion's native host mode when the script disconnects.
    goodbye_messages = (midi.NATIVE_MODE_OFF_MESSAGE,)

    # component_map both substitutes our implementations for framework component names
    # ("Transport") and registers entirely new ones ("Motion_Screen"):
    # ComponentMap._create_component_map ends with `self.update(specification.component_map)`,
    # so new keys sit alongside the built-ins and are instantiated lazily inside the
    # surface's dependency guard — which is what gives them `self.song` and `self._tasks`.
    component_map = {
        "Transport": MotionTransportComponent,
        "Motion_Screen": MotionScreenComponent,
        "Motion_Wheel": MotionWheelComponent,
        # Phase 8. `Modifier_Background` is **substituted**, not added: ours is the framework's
        # own `ModifierBackgroundComponent` plus a report of when Shift goes down, which is what
        # lets the keybed repaint into the command layer. Substituting keeps its skin keys and
        # its consumption of the button exactly as they were.
        "Modifier_Background": MotionModifierComponent,
        "Motion_Commands": MotionCommandsComponent,
        # Phase 10 — Scale mode's state/controls, and the Control button that leaves it.
        "Motion_Scale": MotionScaleComponent,
        "Motion_Mode_Return": MotionModeReturnComponent,
        # A plain background whose only job is to consume the top lane while Shift is held —
        # see the note in `mappings.py`. Registered rather than reusing `Translating_Background`
        # because that one translates MIDI channels, which is not what is wanted here.
        "Shift_Pad_Background": BackgroundComponent,
        # The big wheel paging Mix mode between Volume and Pan (Phase 7b). Nothing in the
        # framework switches modes from an encoder — see mixpages.py.
        "Motion_Mix_Pages": MotionMixPagesComponent,
        # Mix mode's Sends page — the (track x send) encoder grid (2026-08-03).
        "Motion_Sends": MotionSendsComponent,
        # The pads as a playable keyboard: note translation so they read as a piano AND
        # actually reach an armed track. See keyboard.py.
        "Motion_Keyboard": MotionKeyboardComponent,
    }


class Motion32(ControlSurface):
    def __init__(self, *a, **k):
        # Set before anything else: `_send_midi` is overridden below and consults this on
        # every call, including calls made from inside super().__init__().
        self._midi_muted = False
        self._motion_protocol = None
        self._screen_model = None
        self._main_view = None
        self._params_view = None
        self._mixer_view = None
        self._encoder_leds = None
        self._wheel_led = None
        self._pad_leds = None
        self._parameter_source = None
        self._screen = None
        self._dropped_messages = 0
        # Built before super().__init__() because the framework creates components
        # during construction and MotionScreenComponent reads these from `runtime`.
        # Nothing is transmitted yet — sending starts once setup() runs.
        self._build_screen()
        super().__init__(*a, specification=Specification, **k)

    # -- construction ------------------------------------------------------
    def _build_screen(self):
        self._motion_protocol = MotionProtocol(
            send_midi=self._deferred_send_midi,
            log_message=logger.info,
            on_feedback_resumed=self._on_feedback_resumed,
        )
        self._screen_model = ScreenModel(
            send=self._motion_protocol.send,
            log=logger.info,
        )
        self._main_view = MainView(self._screen_model)
        self._params_view = ParamsView(self._screen_model)
        # Template 2 — the eight channel strips used by Mix mode (Phase 7).
        self._mixer_view = MixerView(self._screen_model)
        # Template 1, borrowed for ~1s whenever something changes that has no permanent
        # home on screen — octave first (notification.py).
        self._notification_view = NotificationView(self._screen_model)
        # Template 1 again — the scrollable list Scale mode draws. ⚠️ It shares the template
        # with the bar above; they are never both active and each claims every element on the
        # way in, which is what makes that safe. See `menu.py`.
        self._menu_view = MenuView(self._screen_model)
        self._encoder_leds = EncoderLeds(send=self._motion_protocol.send)
        # The wheel halo is a single LED at the wheel's own CC — same wire shape as the
        # encoder halos, so the same cached writer drives it.
        self._wheel_led = EncoderLeds(
            send=self._motion_protocol.send, addresses=(midi.CC_WHEEL,)
        )
        # The 32 pads. Note-addressed (0x90 / 0x91-0x93), unlike every other LED group on
        # this device — see leds.py. Ours only while no component binds the pads.
        self._pad_leds = PadLeds(send=self._motion_protocol.send)
        self._wheel_led.set_suspended(True)
        self._encoder_leds.set_suspended(True)
        self._pad_leds.set_suspended(True)
        self._parameter_source = ParameterSource(log=logger.info)
        # Hold all output until setup() completes. Components are constructed during
        # super().__init__() and will paint immediately, but `_send_midi` is not usable
        # yet. Starting suspended means the model records nothing as sent, so the first
        # real redraw in setup() is complete rather than half-cached.
        self._screen_model.set_suspended(True)
        runtime.publish(
            self,
            self._screen_model,
            self._main_view,
            self._params_view,
            self._mixer_view,
            self._notification_view,
            self._menu_view,
            self._parameter_source,
        )

    def _deferred_send_midi(self, message):
        """Backstop for anything that tries to transmit before the surface is ready.

        Should not fire in normal operation — the screen model is held suspended until
        setup() — so log it once and keep going rather than raising through a listener.
        """
        try:
            self._send_midi(message)
        except Exception:
            # Was logged only once, which hid a screen that never drew. Log the first few
            # in full, then a single summary — enough to diagnose, not enough to flood.
            self._dropped_messages += 1
            if self._dropped_messages <= 3:
                logger.exception(
                    "Motion32: _send_midi FAILED for %s (drop #%d)",
                    as_hex(message),
                    self._dropped_messages,
                )
            elif self._dropped_messages == 4:
                logger.warning("Motion32: further dropped messages will not be logged")

    def setup(self):
        super().setup()

        # Output is safe from here on.
        self._screen_model.set_suspended(False)
        self._encoder_leds.set_suspended(False)
        self._wheel_led.set_suspended(False)
        self._pad_leds.set_suspended(False)

        # Hand the Device component to the parameter source so the screen reads the
        # same parameter list the encoders are wired to (see parameters.py).
        self._parameter_source.bind_device_component(self._component("Device"))

        # The screen component is created by the framework from component_map; fetch it and
        # give it the modes component so the Plugin button can switch the view. The modes
        # component only exists after create_mappings has run, which is why this is here
        # rather than in the screen component's constructor.
        self._screen = self._component("Motion_Screen")
        modes = self._component("Main_Modes")
        logger.info(
            f"Motion32: components — screen={type(self._screen).__name__ if self._screen else None}, "
            f"modes={type(modes).__name__ if modes else None}, "
            f"screen_enabled={self._screen.is_enabled() if self._screen else None}"
        )
        if self._screen is not None:
            self._bind_screen_sources(modes)
        if modes is None:
            logger.warning("Motion32: Main_Modes not found; the screen will stay on the device view")

        logger.info("Motion32: script setup complete")
        logger.info(
            "Motion32: native-mode entry and identity request are configured as hello messages"
        )
        self._redraw_everything("setup")

    def _bind_screen_sources(self, modes):
        """Hand the screen component everything it could not be given at construction time.

        ⚠️ **Each binding gets its own guard, and the log names the one that failed.** This was
        a single `try` around all fourteen calls until 2026-08-03, which meant a failure in the
        *first* one silently skipped the other thirteen — the mixer, the ring, the page set, all
        three LED groups, the keyboard's three listeners and the mode follow — behind one
        traceback that named none of them. The symptom would have been "the screen works and
        nothing else does", which is a long way from the log line you would have got.

        A table rather than fourteen `try` blocks: adding a binding should not be an
        opportunity to forget the guard.

        **Order is load-bearing** and the table preserves it:

        * `bind_parameter_source` must follow `ParameterSource.bind_device_component` above —
          the screen component was constructed inside `super().setup()`, before the Device
          component existed, so it has to be told to subscribe and re-read now. Without it the
          parameter list stays empty and bank changes never repaint.
        * `bind_modes` goes **last**, because it triggers the first real render and everything
          that render reads should already be attached.
        """
        screen_component = self._screen
        # The ring is **not** in `component_map`: `ControlSurface._create_session_ring` builds
        # it directly and stores it as `_session_ring`, so it is fetched by attribute.
        session_ring = getattr(self, "_session_ring", None)
        # Mix mode's page set. The wheel component pages it and the screen component reads it —
        # one source, both readers, so the encoders and the screen cannot disagree about which
        # page is up.
        pages = self._component("Mix_Pages")
        keyboard = self._component("Motion_Keyboard")
        wheel_pages = self._component("Motion_Mix_Pages")
        sends = self._component("Motion_Sends")
        commands = self._component("Motion_Commands")
        scale = self._component("Motion_Scale")
        mode_return = self._component("Motion_Mode_Return")
        modifier = self._component("Modifier_Background")

        bindings = [
            ("parameter source", lambda: screen_component.bind_parameter_source()),
            # Template 2 reads its eight strips off the Mixer component, so the view follows
            # the session ring rather than the first eight visible tracks.
            ("mixer", lambda: screen_component.bind_mixer(self._component("Mixer"))),
            # …and the ring itself, because it carries the `offset` event. Without this the Mix
            # screen does not repaint when Left/Right pages the ring: the tracks move out from
            # under the strips and nothing asks for a redraw.
            ("session ring", lambda: screen_component.bind_session_ring(session_ring)),
            ("mix pages (screen)", lambda: screen_component.bind_mix_pages(pages)),
            ("encoder halos", lambda: screen_component.bind_encoder_leds(self._encoder_leds)),
            ("wheel halo", lambda: screen_component.bind_wheel(self._wheel_led)),
            ("pad LEDs", lambda: screen_component.bind_pad_leds(self._pad_leds)),
        ]

        if wheel_pages is not None:
            bindings.append(("mix pages (wheel)", lambda: wheel_pages.bind_pages(pages)))
            if sends is not None:
                # The wheel needs the Sends page count, which depends on the set rather than on
                # the mapping table — see `mixpages.bind_sends`.
                bindings.append(("mix pages (sends)", lambda: wheel_pages.bind_sends(sends)))
        if sends is not None:
            bindings += [
                # The Sends grid follows the session ring, so it reads its tracks off the Mixer
                # exactly as the strips do — a column is the same track on both pages.
                ("sends mixer", lambda: sends.bind_mixer(self._component("Mixer"))),
                # …and the ring itself, or paging Left/Right leaves the encoders mapped to the
                # tracks that *used* to be under the strips — see `sends.bind_session_ring`.
                ("sends ring", lambda: sends.bind_session_ring(session_ring)),
                ("sends source", lambda: screen_component.bind_sends(sends)),
                ("sends state", lambda: sends.set_changed_listener(screen_component.on_sends_changed)),
            ]

        if keyboard is not None:
            bindings += [
                # The keyboard hears pad presses (its matrix is playable *and* listenable) but
                # does not paint them — `PadLeds` owns those addresses, so it reports the held
                # set and the screen component repaints. One writer.
                ("pads held", lambda: keyboard.set_held_listener(screen_component.set_pads_held)),
                # The pad *layout* comes from the keyboard too — A-H banking and Octave both
                # move it. The keyboard derives the roles from the same pitch list it translates
                # notes with, so the keybed cannot light a layout it does not play. Set here
                # rather than in the screen component, which has no way to reach the keyboard.
                ("pad roles", lambda: keyboard.set_roles_listener(screen_component.set_pad_roles)),
                # 🐛 Scale mode hands the keyboard a different pitch list, and without this
                # handle it silently could not — see `bind_keyboard`.
                ("keyboard handle", lambda: screen_component.bind_keyboard(keyboard)),
                # Octave and A-H changes have no permanent place on any mode's screen, so they
                # announce themselves on the transient bar. The keyboard does not know what a
                # screen is — it hands over a title and a value.
                ("notifications", lambda: keyboard.set_notification_listener(screen_component.notify)),
            ]
        else:
            logger.warning("Motion32: Motion_Keyboard not found; pads will not flash")

        if commands is not None:
            bindings += [
                # The command layer announces itself on the transient bar, the same route
                # Octave and A-H banking take. `Motion_Commands` does not know what a screen is.
                ("command notifications",
                 lambda: commands.set_notification_listener(screen_component.notify)),
                # …and reports its layout so `PadLeds` can paint the overlay. `PadLeds` stays
                # the single writer of every pad address; the component only says what to draw.
                ("command layout",
                 lambda: commands.set_layout_listener(screen_component.set_command_layout)),
            ]
            if modifier is not None:
                # Shift-down is what makes the keybed flip to the command layer. The modifier
                # component observes the element rather than owning a second control — see
                # `commands.MotionModifierComponent`.
                bindings.append(
                    ("shift observation",
                     lambda: modifier.set_shift_listener(commands.set_shift_held))
                )
            else:
                logger.warning(
                    "Motion32: Modifier_Background not found; the Shift commands will still "
                    "fire but the pads will not show the overlay"
                )
        else:
            logger.warning("Motion32: Motion_Commands not found; Shift+pad will do nothing")

        if scale is not None:
            bindings += [
                # Scale mode's list, pad layout and LEDs all derive from this component's state,
                # so one "something changed" report drives the whole redraw.
                ("scale state", lambda: scale.set_changed_listener(screen_component.on_scale_changed)),
                ("scale source", lambda: screen_component.bind_scale(scale)),
            ]
        else:
            logger.warning("Motion32: Motion_Scale not found; Scale mode will be empty")
        if mode_return is not None:
            # The Control button needs the modes component to return to the previous mode, and
            # the screen component tells it which mode that was.
            bindings.append(("mode return", lambda: mode_return.bind_modes(modes)))
            bindings.append(
                ("mode history", lambda: screen_component.bind_mode_return(mode_return))
            )

        # Last: this is what triggers the first real render.
        bindings.append(("modes", lambda: screen_component.bind_modes(modes)))

        failed = []
        for name, bind in bindings:
            try:
                bind()
            except Exception:
                failed.append(name)
                logger.exception(
                    "Motion32: binding %r failed; continuing with the rest", name
                )
        if failed:
            logger.warning(
                "Motion32: %d of %d screen bindings failed (%s) — the features they feed "
                "will be inert",
                len(failed),
                len(bindings),
                ", ".join(failed),
            )

    # -- screen lifecycle --------------------------------------------------
    def _component(self, name):
        """Fetch a framework-managed component, or None with a log line."""
        try:
            return self.component_map[name]
        except Exception:
            logger.exception(f"Motion32: could not reach the {name} component")
            return None

    def _screen_component(self):
        return self._screen

    def _redraw_everything(self, reason):
        """Invalidate the cache and re-send the whole screen.

        Needed whenever the device's display state becomes unknown to us: after the
        native-mode handshake (it comes up blank) and after the user closes the
        on-device Global Settings screen (which wipes whatever we drew).
        """
        component = self._screen_component()
        if component is None:
            return
        try:
            component.full_redraw()
            logger.info(f"Motion32: full screen redraw ({reason})")
        except Exception:
            logger.exception("Motion32: screen redraw failed")

    def _on_feedback_resumed(self):
        if self._screen_model is not None:
            self._screen_model.set_suspended(False)
        self._redraw_everything("Global Settings closed")

    def refresh_state(self):
        """Live calls this when it wants the surface fully re-lit."""
        super().refresh_state()
        self._redraw_everything("refresh_state")

    # -- MIDI --------------------------------------------------------------
    def _send_midi(self, *a, **k):
        """The single outgoing choke point, so a superseded instance can go silent.

        ⚠️ **Suspending our own writers is not enough.** `ControlSurface.disconnect()` sends
        `goodbye_messages` through `_send_specification_messages`, which calls
        `self._send_midi` **directly** — it never touches `MotionProtocol`, `ScreenModel` or
        `LedGroup`, so none of their suspend flags reach it (confirmed by disassembling
        `control_surface.pyc`: both branches of `disconnect` call
        `_send_specification_messages(messages_name="goodbye_messages")`, whose body is a
        `for msg in ...: self._send_midi(msg)` loop).

        On a script reload Live builds the replacement *before* disconnecting us, so the
        unguarded order was:

            new instance sends 8F 00 7F  ->  old instance disconnects  ->  old sends 8F 00 00

        …leaving the device out of native mode while the new instance believes it is in —
        which presents as the pre-native half-state: screen and LEDs still work, but
        transport arrives on 0x66-0x69 instead of 0x6F.

        Muting here rather than neutralising `goodbye_messages` is deliberate: it is the
        *only* place that catches every path out of a superseded instance, including
        element resets and any framework write we have not enumerated. Returning True keeps
        the framework's contract ("handled") so nothing retries or logs a failure.
        """
        if self._midi_muted:
            return True
        return super()._send_midi(*a, **k)

    def receive_midi(self, midi_bytes):
        """Handle the Motion's own SysEx; pass everything else to the framework.

        Messages we consume are NOT forwarded. The framework logs
        `Got unknown sysex message: …` for anything it cannot match, and since we
        deliberately avoid `identity_response_id_bytes` (see the Specification above) the
        identity reply is exactly such a message — ours to handle, and noise in the log if
        we pass it on.
        """
        packet = tuple(midi_bytes)
        if packet and packet[0] == midi.SYSEX_START:
            logger.info(f"Motion32 RX: {as_hex(packet)}")
            if self._motion_protocol is not None:
                handled = self._motion_protocol.handle_incoming(packet)
                if self._motion_protocol.feedback_suspended and self._screen_model is not None:
                    self._screen_model.set_suspended(True)
                if handled:
                    return None
        return super().receive_midi(midi_bytes)

    # -- teardown ----------------------------------------------------------
    def disconnect(self):
        """Leave the device clean.

        Studio Pro resets every LED and blanks the screen *before* it sends the
        native-mode goodbye. The framework sends our goodbye_messages during
        super().disconnect(), so the clearing has to happen first — otherwise the
        Motion sits there showing a stale device name and lit buttons after Live
        unloads the script.
        """
        # Are we still the live instance? On a script reload Live constructs the replacement
        # *before* disconnecting us, so a blind teardown here would reset a device the new
        # instance has already drawn on — leaving a blank screen and dark LEDs with nothing
        # in the log to explain it. `runtime.clear` returns False when we have been
        # superseded, which is our signal to leave the hardware alone.
        still_current = runtime.clear(self)

        if still_current:
            logger.info("Motion32: disconnecting; clearing LEDs and screen before native-mode exit")
            # ⚠️ **`_clear_all_leds()` already covers every address our groups own**, so the
            # groups only need to *forget* — not to transmit.
            #
            # `midi.LED_ADDRESSES_TO_CLEAR` contains `CC_ENCODERS` (the halos) and `CC_WHEEL`,
            # and `_clear_all_leds` walks `PAD_NOTES` itself, so calling `release()` on the
            # three groups first re-sent all 41 addresses a second time: ~196 redundant
            # messages on every unload, and it made the claim that our teardown is
            # byte-identical to Studio Pro's false. Fixed 2026-08-03.
            #
            # `forget()` still matters: a group that thinks it has sent something would
            # short-circuit the diff if this instance somehow drew again.
            try:
                for leds in (self._encoder_leds, self._wheel_led, self._pad_leds):
                    if leds is not None:
                        leds.set_suspended(False)
                        leds.forget()
                self._clear_all_leds()
            except Exception:
                logger.exception("Motion32: LED clear failed during teardown")
            try:
                if self._screen_model is not None:
                    self._screen_model.set_suspended(False)
                    self._screen_model.reset_to_defaults()
            except Exception:
                logger.exception("Motion32: screen reset failed during teardown")
        else:
            logger.info(
                "Motion32: disconnecting a superseded instance — leaving the device to the "
                "newer one (MIDI output muted: no LED/screen reset, and no native-mode goodbye)"
            )
            # Mute the transmitter itself, not just our writers. `super().disconnect()`
            # below sends `goodbye_messages` (8F 00 00) straight through `_send_midi`,
            # bypassing every suspend flag we own — see `_send_midi`. Without this, a
            # reload kicks the device out of native mode behind the new instance's back.
            self._midi_muted = True
            # Suspending the writers as well is redundant for the wire but keeps their
            # caches honest: a suspended model records nothing as sent.
            if self._screen_model is not None:
                self._screen_model.set_suspended(True)
            for leds in (self._encoder_leds, self._wheel_led, self._pad_leds):
                if leds is not None:
                    leds.set_suspended(True)

        self._screen = None
        super().disconnect()

    def _clear_all_leds(self):
        """Release every LED the way the factory host does: state off, colour **white**.

        Not black. The Studio Pro shutdown capture sends state 0 on channel 1 and 127 on
        channels 2/3/4 (R/G/B) for every address — so the LED goes dark but its colour is
        left at full white rather than zeroed. See midi.RESET_* and
        Motion32_Implementation_Notes.md §5.
        """
        if self._motion_protocol is None:
            return
        send = self._motion_protocol.send
        for address in midi.LED_ADDRESSES_TO_CLEAR:
            send((midi.STATUS_CC, address, midi.RESET_LED_STATE))
            send((midi.STATUS_CC_RED, address, midi.RESET_RGB))
            send((midi.STATUS_CC_GREEN, address, midi.RESET_RGB))
            send((midi.STATUS_CC_BLUE, address, midi.RESET_RGB))
        for note in midi.PAD_NOTES:
            # Two state writes per pad: the capture shows both the state and animation
            # handlers releasing the same note address.
            send((midi.STATUS_NOTE, note, midi.RESET_LED_STATE))
            send((midi.STATUS_NOTE, note, midi.RESET_LED_STATE))
            send((midi.STATUS_NOTE_RED, note, midi.RESET_RGB))
            send((midi.STATUS_NOTE_GREEN, note, midi.RESET_RGB))
            send((midi.STATUS_NOTE_BLUE, note, midi.RESET_RGB))
