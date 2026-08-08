"""The component that decides *what* goes on the Motion 32 screen.

Split of responsibility:

* `display.ScreenModel` — how bytes reach the device (cache, diff, suspend).
* `display.MainView`    — Template 0 (encoder tiles + arcs), used by Plugin mode.
* `display.ParamsView`  — Template 3 (label + value tiles), used by Song mode.
* `parameters.ParameterSource` — which 8 parameters the encoders are mapped to.
* this module           — where the content comes from and when it changes.

Re-renders on real state change only: the Device component's `parameters` listenable
property (fires on device *and* bank change), a value listener per mapped parameter, the
selected main mode, and encoder touch. No polling.

**Two templates, two value strategies.** Template 0 (Plugin mode) has one text element per
tile, so the name and value share it: the factory shows the name at rest and the value while
you touch or turn, then reverts — reproduced with the framework's own timeout
(`ACTIVE_PARAMETER_TIMEOUT` = 0.75 s in `control_surface/consts.pyc`). Template 3 (Song mode)
has a separate label *and* value element per tile, so both stay on screen and no timeout is
needed. Template 3 carries no bar/arc attribute at all — it is text only.
"""

from __future__ import annotations

import logging
from functools import partial

from ableton.v3.base import listens, task
from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl, control_list

from . import midi, pads, runtime, scales, screen
from .display import (
    EncoderTile,
    MainContent,
    MixerContent,
    MixerStrip,
    ParamsContent,
    ParamsTile,
)
from .menu import MenuContent
from .notification import NotificationContent
from .pads import pad_roles
from .palette import dim, live_rgb7
from .formatting import (
    MAXCHARS_ENCODER_LABEL,
    MAXCHARS_HEADER_TITLE,
    MAXCHARS_MIXER_CHANNEL,
    compactify,
    format_parameter_value,
    truncate_value,
)
from .mappings import SONG_ENCODERS
from .parameters import PARAMETERS_PER_BANK
from . import scalemode

logger = logging.getLogger(__name__)

NO_DEVICE_TEXT = "No device selected"
MAXCHARS_CENTRE = 24

#: Matches the framework's own ACTIVE_PARAMETER_TIMEOUT (control_surface/consts.pyc).
VALUE_TIMEOUT = 0.75

#: How long the transient notification bar stays up. Studio Pro's own dwell measured 995 ms
#: and then 848 ms across two consecutive octave presses, so its timer is coarse rather than
#: exact; 1 s sits inside that and is the round number.
NOTIFICATION_TIMEOUT = 1.0

#: Mix-mode meter refresh, in seconds. **10 Hz, matching the factory** — a Studio Pro capture
#: measured frame intervals of 96-117 ms, so this rate is sufficient by demonstration rather
#: than by guess. Eight strips x two meters = 16 values per frame, 160 messages/s at the
#: factory's own cadence, and our diff sends fewer: the capture shows Studio Pro repeating an
#: unchanged `04` across five consecutive frames, which `ScreenModel` suppresses.
#:
#: One named constant so a hardware run can raise it without touching the component.
METER_INTERVAL = 0.1

#: **The halos are ours because nothing else may write to their address.**
#: A halo has no address of its own — it lives at the encoder's own CC — so the framework's
#: element writes land on the light. That is fixed at the source, in `elements.py`:
#: `MotionEncoderElement` drops the element's outgoing bytes entirely. See its docstring.
#:
#: Racing the framework (set the halo again, a moment later) was the earlier attempt and it is
#: not good enough — it flickers, and anything we have no event for wins until the next
#: re-assert. Turning and clicking the wheel kept knocking it out.
#:
#: What remains here is one short deferred re-assert after a mode change. Not a race any more:
#: mode changes re-grab layers and rebuild the entries list, so this is simply the point at
#: which the halos' *intended* colours have settled.
LED_REASSERT_DELAY = 0.15

#: The mode in which the screen shows the device/plugin detail view.
PLUGIN_MODE = "plugin"
MIX_MODE = "mix"
SONG_MODE = "song"
#: Scale mode (Phase 10) — Template 1's list, and the pads re-laid to the scale.
SCALE_MODE = "scale"

#: Mix mode's two pages, from the `Mix_Pages` modes component. The **layer** key for the pan
#: page is its own, because the page decides which template is up — Volume draws Template 2's
#: strips and Pan draws Template 0's arcs.
MIX_PAGE_VOLUME = "volume"
MIX_PAGE_PAN = "pan"
MIX_PAGE_SENDS = "sends"
MIX_PAN_LAYER = "mix_pan"
#: The Sends page borrows Template 0 too — eight arcs, one per (track, send) slot.
MIX_SENDS_LAYER = "mix_sends"

#: The layer keys `_screen_layer()` returns. The notification bar is not a mode — it outranks
#: whichever mode is showing — so it gets a key of its own alongside them.
NOTIFICATION_LAYER = "notification"

#: Soft-button labels per mode — the buttons are bound per mode, so the labels follow.
#: Top row is 0-3 (over the screen), bottom row 4-7 (under it).
SONG_SOFT_LABELS = ("", "", "Loop", "Bck2Arr", "Sess/Arr", "Browser", "Cue Mrk", "Clip/Dev")
#: Plugin mode claims none of them yet, so they are dark and unlabelled.
PLUGIN_SOFT_LABELS = ("",) * 8

#: How many channel strips Template 2 shows.
MIXER_STRIP_COUNT = 8

#: An empty pan tile: greyed, centred arc. The factory greys rather than hiding.
EMPTY_TILE_FOR_PAN = EncoderTile(value=64, assigned=False)

#: Second line for encoders whose "value" is really a hint about what turning does, rather
#: than a readable number. Keyed by the framework control name.
SONG_ENCODER_HINTS = {
    "cue_encoder": "Prev/Next",
    "horizontal_zoom_encoder": "In/Out",
    "vertical_zoom_encoder": "In/Out",
}


def _liveobj_valid(obj) -> bool:
    if obj is None:
        return False
    try:
        obj.name
        return True
    except (RuntimeError, AttributeError):
        return False


def _normalized_value(parameter) -> int:
    """Parameter value scaled to the 0-127 the screen's fill/halo element takes."""
    try:
        minimum = parameter.min
        maximum = parameter.max
        current = parameter.value
    except (RuntimeError, AttributeError):
        return 0
    span = maximum - minimum
    if span <= 0:
        return 0
    fraction = (current - minimum) / span
    fraction = 0.0 if fraction < 0.0 else (1.0 if fraction > 1.0 else fraction)
    return int(round(fraction * 127))


class MotionScreenComponent(Component):
    """Owns the screen's content. The only writer of either view.

    Registered the normal way: `Specification.component_map["Motion_Screen"]`. The
    framework's `ComponentMap._create_component_map` ends with
    `self.update(specification.component_map)`, so a brand-new name is registered
    alongside the built-ins, and `__getitem__` instantiates it lazily *inside* the
    surface's dependency guard. That injection is what makes `self.song` and
    `self._tasks` work — a hand-built component gets neither.

    Reserved-name warning: `Component.__init__` assigns `self._song`, `self._parent`,
    `self.name`, `self._layer` and more. Never define attributes with those names on a
    subclass (a read-only `_song` property fails the build outright).
    """

    #: Capacitive touch, one per encoder. Bound via create_mappings.
    encoder_touch_buttons = control_list(ButtonControl, PARAMETERS_PER_BANK)

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self._entries = []
        self._value_slots = []
        self._track_slots = []
        self._modes = None
        self._touch_held = [False] * PARAMETERS_PER_BANK
        self._showing_value = [False] * PARAMETERS_PER_BANK
        self._hide_tasks = [None] * PARAMETERS_PER_BANK
        self._live_refresh_task = None
        self._active_view = None
        #: The transient title/value bar, or None when a mode's own screen is up.
        self._notification = None
        self._notification_task = None
        self._encoder_leds = None
        self._pad_leds = None
        #: The keyboard, bound after setup — Scale mode hands it a different pitch list.
        self._keyboard = None
        #: The framework Mixer component, bound after setup — see `bind_mixer`.
        self._mixer = None
        #: The session ring, bound after setup — it owns the `offset` event.
        self._session_ring = None
        #: Mix mode's page set, bound after setup — see `bind_mix_pages`.
        self._mix_pages = None
        #: Listener slots for the eight strips' tracks. Rebound whenever the ring moves.
        self._mixer_slots = []
        #: Role per pad — which are roots, which are ordinary keys, which are gaps.
        #:
        #: 🔑 **Received from the keyboard, never recomputed here.** This used to be a
        #: `_pad_root_offset` int that `_refresh_pad_leds` fed to `pad_roles()`, i.e. a second
        #: copy of an offset the keyboard also holds — and the handoff flagged the failure
        #: mode before A-H existed: move one copy and not the other and the keybed lights a
        #: layout it does not play. The keyboard now derives these from the *same pitch list*
        #: it builds the note translation from, so there is nothing left to keep in step.
        #:
        #: Seeded with the resting layout so the pads are correct on the very first paint,
        #: which happens during `bind_pad_leds` — before the keyboard has reported anything.
        self._pad_roles = pad_roles()
        #: Pad indices currently held. The keyboard component reports these; we paint them,
        #: because `leds.PadLeds` is the single writer of the pad addresses.
        self._pads_held = frozenset()
        #: The Shift command overlay (Phase 8): whether it is up, its 16 labels, and which
        #: slots do something. Reported by `commands.MotionCommandsComponent`; painted here,
        #: because `leds.PadLeds` is the single writer of every pad address.
        #: Scale mode's component, bound after setup — see `bind_scale`.
        #: Mix mode's Sends grid, bound after setup.
        self._sends = None
        self._scale = None
        #: The Control button's memory of the last returnable mode.
        self._mode_return = None
        self._commands_shown = False
        self._command_labels = [""] * pads.PADS_PER_LANE
        self._command_slots = frozenset()
        self._wheel_led = None
        self._led_reassert_task = None
        #: The Mix-mode meter poll (Phase 7c). The one polled source on this surface.
        self._meter_task = None

        # NOTE: the Device component is NOT available yet. The framework builds this
        # component during ControlSurface.setup(), and the surface binds the Device component
        # to the ParameterSource *after* that returns. Subscribing here silently did nothing,
        # which left `_entries` frozen at eight empty slots and meant bank changes never
        # repainted. The surface calls `bind_parameter_source()` once binding is done — see
        # Motion32_Implementation_Notes.md §6b-7.

        # Song mode reads song properties directly, so it needs its own listeners —
        # without them the screen only refreshed when something *else* caused a render,
        # which read as laggy, batched updates.
        song = self._live_song
        if song is not None:
            self._on_tempo_changed.subject = song
            self._on_loop_start_changed.subject = song
            self._on_loop_length_changed.subject = song
            self._on_signature_changed.subject = song
            self._on_selected_track_changed.subject = song.view

        # Session <-> Arrangement. Without this the header only caught up when some *other*
        # event happened to force a render.
        try:
            self._on_focused_document_view_changed.subject = self.application.view
        except (AttributeError, RuntimeError, TypeError):
            logger.warning(
                "Motion32: could not follow the focused document view; the Song header may lag"
            )

        # No modes component yet, so this is Song mode (Template 3) until told otherwise.
        view = self._view_for_mode()
        if view is not None:
            self._active_view = view
            view.activate()
        self._rebind_track()
        self._rebind_parameters()

    @property
    def _live_song(self):
        """`Component.song` (the injected `_song`), guarded.

        Named `_live_song` because `_song` itself is assigned by `Component.__init__` and
        must never be shadowed — see Motion32_Implementation_Notes.md §4.
        """
        try:
            return self.song
        except AttributeError:
            return None

    def bind_pad_leds(self, pad_leds):
        """Take ownership of the 32 pad LEDs, for as long as nothing else binds them.

        The pads rest in the **focused track's own colour** at dim brightness — the factory's
        "present but inactive" model, where the state byte carries brightness (0 / 63 / 127) and
        the RGB triple carries hue. That means the whole keybed tells you which track you are
        playing into, without a mode having to claim the pads.

        ⚠️ This holds only while no component owns the pads. When Session mode binds them to
        `SessionComponent`, the framework becomes the writer for those addresses and this must
        yield — a pad's LED address is its note address, so two writers would fight exactly the
        way the encoder halos did (§6b-10).
        """
        self._pad_leds = pad_leds
        self._refresh_pad_leds()

    def set_pads_held(self, held) -> None:
        """Called by the keyboard component when the held-pad set changes."""
        held = frozenset(held)
        if held == self._pads_held:
            return
        self._pads_held = held
        self._refresh_pad_leds()

    def set_pad_roles(self, roles) -> None:
        """Called by the keyboard component when the pad layout changes.

        A-H banking and Octave both land here. The roles arrive already derived from the
        keyboard's own pitch list — see `keyboard.set_roles_listener` — so this component's
        job is only to paint them.
        """
        roles = list(roles)
        if roles == self._pad_roles:
            return
        self._pad_roles = roles
        self._refresh_pad_leds()

    def set_command_layout(self, shown, labels, assigned) -> None:
        """Called by `Motion_Commands` when the Shift overlay appears or goes.

        Only the paint job lives here — the component owns *what* the commands are, this owns
        *the pad addresses*, and `leds.PadLeds` is still the one writer. Same split as the
        keyboard's `set_pad_roles`.
        """
        shown = bool(shown)
        labels = list(labels)
        assigned = frozenset(assigned)
        if (shown, labels, assigned) == (
            self._commands_shown, self._command_labels, self._command_slots
        ):
            return
        self._commands_shown = shown
        self._command_labels = labels
        self._command_slots = assigned
        self._refresh_pad_leds()

    def bind_keyboard(self, keyboard) -> None:
        """Take the keyboard, so Scale mode can hand it a different pitch list.

        🐛 **Without this, Scale mode changed nothing at all.** `_push_scale_layout` opened with
        `if keyboard is None: return`, and `_keyboard` was initialised to `None` and never
        assigned — so every scale change returned immediately and the pads went on playing the
        piano. The LEDs still redrew, because they fall back to `pads.pad_pitches()`, which is
        what made it look like the feature was working. Found on hardware 2026-08-03.

        The lesson is the one this project keeps re-learning: a guard that returns silently turns
        a missing wire into no symptom. `_push_scale_layout` now says so in the log.
        """
        self._keyboard = keyboard
        try:
            keyboard.set_layout_provider(self._layout_for)
        except (AttributeError, RuntimeError):
            logger.exception("Motion32: could not install the layout provider")

    def bind_sends(self, sends_component) -> None:
        """Take Mix mode's Sends grid — the source of its labels, arcs and halo colours."""
        self._sends = sends_component
        if sends_component is None:
            logger.warning("Motion32: no Motion_Sends component; the Sends page will be empty")

    def on_sends_changed(self) -> None:
        """The Sends page moved, or its parameters were re-pointed. Repaint everything."""
        self._refresh_encoder_leds()
        self._render()

    def _sends_content(self) -> MainContent:
        """Mix mode's **Sends** page — Template 0's arcs, one per (track, send) slot.

        Borrows the encoder-tile view for the same reason the Pan page does: Template 2 has no
        send element, and an arc reads a level better than a number. The tile's single text
        element carries `"Drums A"` at rest and the value while the encoder is touched — the
        same reveal, for the same reason.
        """
        sends = self._sends
        if sends is None:
            return MainContent(title="Mix | Sends", centre="No sends")
        tiles = []
        for index in range(PARAMETERS_PER_BANK):
            parameter = sends.slot_parameter(index)
            if parameter is None:
                tiles.append(EMPTY_TILE_FOR_PAN)
                continue
            tiles.append(
                EncoderTile(
                    label=compactify(sends.slot_label(index), MAXCHARS_ENCODER_LABEL),
                    value=_normalized_value(parameter),
                    assigned=True,
                    value_text=truncate_value(
                        format_parameter_value(parameter), MAXCHARS_ENCODER_LABEL
                    ),
                    show_value=self._showing_value[index],
                )
            )
        # The header wears the **selected** track's colour, exactly as the Pan page's does, so
        # the track the last touch focused is visible rather than merely implied. Without it,
        # "which track am I focused on" had no answer anywhere on this page — which is what made
        # the touch/turn mismatch hard to see.
        selected = self._selected_track_colour()
        return MainContent(
            title="Mix | Sends",
            centre=sends.page_label(),
            header_background=selected,
            tiles=tuple(tiles),
            soft_labels=PLUGIN_SOFT_LABELS,
        )

    def bind_scale(self, scale_component) -> None:
        """Take Scale mode's state. The pads and the list both derive from it."""
        self._scale = scale_component
        if scale_component is None:
            logger.warning("Motion32: no Motion_Scale component; Scale mode will be empty")
            return
        self.on_scale_changed()

    def bind_mode_return(self, mode_return) -> None:
        """Take the Control button's component, so it can be told the last returnable mode."""
        self._mode_return = mode_return
        self._remember_mode()

    def _remember_mode(self) -> None:
        if self._mode_return is None:
            return
        try:
            self._mode_return.remember(self._mode)
        except (AttributeError, RuntimeError):
            pass

    def on_scale_changed(self) -> None:
        """Scale, root, category or Guide/Locked moved — repaint the list and the keybed.

        One entry point for all four, because every visible thing in Scale mode is *derived*
        from that state rather than stored beside it. There is nothing to keep in step.
        """
        self._refresh_layout()
        self._refresh_pad_leds()
        self._render()

    def _layout_for(self, root_degrees, octave_semitones):
        """The keyboard's layout provider. `(pitches, roles)`, or `None` for the piano.

        🔑 **Called by the keyboard on every `_recompute()`**, with the offsets as they are at
        that moment — which is what makes A-H and Octave work in Scale mode. It used to be a
        list handed over once, and banking then moved the offsets while the pitches sat still.

        This is also the *only* place a scale layout is generated. The LED painter reads the
        roles the keyboard reports rather than recomputing — the §5.3b rule, and the thing that
        let the keybed light for a layout it was not playing.
        """
        scale = self._scale
        if self._mode != SCALE_MODE or scale is None:
            return None
        if scale.locked:
            pitches = scales.locked_pitches(
                scale.scale_id, scale.root, octave_semitones, root_degrees
            )
            return pitches, scales.locked_roles(pitches, scale.root)
        # Guide: the ordinary piano, with the scale marked. Same pitches the keyboard would
        # have produced on its own — only the roles differ.
        pitches = pads.pad_pitches(root_degrees, octave_semitones)
        return pitches, scales.guide_roles(pitches, scale.scale_id, scale.root)

    def _refresh_layout(self) -> None:
        """Ask the keyboard to re-derive its layout, because something it depends on moved."""
        keyboard = self._keyboard
        if keyboard is None:
            if self._mode == SCALE_MODE:
                logger.warning(
                    "Motion32: no keyboard bound, so Scale mode cannot re-lay the pads — "
                    "they are still playing the chromatic layout"
                )
            return
        try:
            keyboard.set_layout_provider(self._layout_for)
        except (AttributeError, RuntimeError):
            logger.exception("Motion32: could not refresh the pad layout")

    def _scale_content(self) -> MenuContent:
        """The scale list — title, rows, selection and the eight soft labels."""
        scale = self._scale
        if scale is None:
            return MenuContent(title=scalemode.MENU_TITLE)
        return MenuContent(
            title=scalemode.MENU_TITLE,
            rows=scale.rows(),
            selected=scale.selected_index(),
            soft_labels=scale.soft_labels(),
        )

    def _refresh_command_leds(self, leds):
        """The Shift overlay: bottom lane is the command layer, top lane is dark.

        Three states, and the middle one is the point: **an unassigned slot is grey, not dark.**
        That is the factory's convention for "present but unassigned" — the same one the Plugin
        tiles use — and it is what distinguishes an empty slot from a broken pad. Ten of the
        sixteen are grey today (see `commands.py` for why), so getting this wrong would make
        most of the layer look broken.
        """
        for index in range(leds.count):
            if index >= pads.PADS_PER_LANE:
                # Top lane: dark, and consumed by the background so it is silent too.
                leds.set(index, None)
            elif index in self._pads_held:
                leds.set(index, screen.Palette.PAD_PLAYED, state=midi.LED_ON)
            elif index in self._command_slots:
                # A live command. White, as the factory does it.
                leds.set(index, screen.Palette.WHITE, state=midi.LED_ON)
            else:
                leds.set(index, screen.Palette.DISABLED, state=midi.LED_ON)

    def _refresh_pad_leds(self):
        """Paint the keybed the way the factory does.

        From a Studio Pro track-change capture: **root pads take the track's colour, every
        other key is white, and the four pads with no black key above them are dark.** The
        layout itself lives in `pads.py`.

        🐛 **Pads do not have a dim state.** This first shipped with `state=midi.LED_DIM` (63)
        and *nothing lit at all*. A pad's state byte accepts only Off `0x00`, On `0x7F`,
        Blink `0x01` and Pulse `0x02` — 63 is not in that vocabulary. The dim/full brightness
        model belongs to **button** LEDs, which are a different address space entirely. Pad
        brightness has to come from the colour, which is exactly why the factory sends
        colour-only updates and why `palette.dim()` exists.
        """
        leds = self._pad_leds
        if leds is None:
            return
        # ⚠️ **One writer, two layouts — chosen here, before any `set()` call.** While Shift is
        # held the keybed is not a keyboard at all, so painting roles over it would be a second
        # opinion about what the pads currently mean. Branching once at the top keeps `PadLeds`
        # written by exactly one loop per repaint.
        if self._commands_shown:
            self._refresh_command_leds(leds)
        else:
            self._refresh_keyboard_leds(leds)
        try:
            leds.flush()
        except Exception:
            logger.exception("Motion32: pad LED flush failed")

    def _refresh_keyboard_leds(self, leds):
        """The keybed — piano or scale, from **the roles the keyboard reported**.

        🔑 One painter, one role vocabulary. The roles arrive from `keyboard.pad_roles`, which the
        keyboard derives alongside the very pitch list it plays, so the lights cannot describe a
        layout the notes do not.

        🐛 There used to be a second painter for Scale mode that regenerated
        `scales.locked_pitches` itself. That is exactly the second opinion §5.3b forbids, and it
        actively hid the A-H bug: banking left the pitches frozen but the painter recomputed, so
        the LEDs moved and the notes did not.
        """
        track_colour = self._selected_track_colour() or screen.Palette.BUTTON_DEFAULT
        roles = self._pad_roles
        for index in range(leds.count):
            role = roles[index] if index < len(roles) else pads.ABSENT
            if role == pads.ABSENT:
                # No black key here — dark, and the keyboard component disables it so it
                # makes no sound either.
                leds.set(index, None)
            elif index in self._pads_held:
                # Held pads flash green, the factory's played-note colour.
                leds.set(index, screen.Palette.PAD_PLAYED, state=midi.LED_ON)
            elif role == pads.ROOT:
                leds.set(index, track_colour, state=midi.LED_ON)
            elif role == scales.OUT_OF_SCALE:
                # Guide: this pad plays, it is simply not in the scale. **Dimmed, never dark** —
                # a dark pad on this keybed means "no note here".
                leds.set(index, dim(screen.Palette.WHITE, 0.18, floor=4), state=midi.LED_ON)
            else:
                leds.set(index, screen.Palette.WHITE, state=midi.LED_ON)

    def bind_encoder_leds(self, encoder_leds):
        """Take ownership of the encoder halos.

        No framework component binds them, so they are ours: colour by mode (purple in Song,
        blue in Plugin) with a white highlight while an encoder is touched.
        """
        self._encoder_leds = encoder_leds
        self._refresh_encoder_leds()

    # -- LED re-assertion --------------------------------------------------
    def _schedule_led_reassert(self):
        """Re-assert the LEDs once the framework has finished shuffling layers."""
        self._kill_task("_led_reassert_task")
        try:
            self._led_reassert_task = self._tasks.add(
                task.sequence(
                    task.wait(LED_REASSERT_DELAY), task.run(self._reassert_leds)
                )
            )
        except Exception:
            # No task group: fall back to an immediate refresh, which may lose the race.
            logger.exception("Motion32: could not schedule the LED re-assert")
            self._reassert_leds()

    def _led_groups(self):
        """Every LED group we own. **The single list — add a new group here and nowhere else.**

        Both the full redraw and the post-mode-change re-assert walk this. They used to name
        their groups separately, and the pads were added to one but not the other, which left
        the keybed dark until a mode switch.
        """
        return (self._encoder_leds, self._wheel_led, self._pad_leds)

    def _invalidate_led_groups(self):
        for leds in self._led_groups():
            if leds is not None:
                leds.invalidate()

    def _refresh_all_leds(self):
        self._refresh_encoder_leds()
        self._refresh_wheel_led()
        self._refresh_pad_leds()

    def _reassert_leds(self):
        """Forget what the device has, then set every LED again."""
        self._led_reassert_task = None
        self._invalidate_led_groups()
        self._refresh_all_leds()

    def _kill_task(self, attribute):
        pending = getattr(self, attribute, None)
        if pending is not None:
            try:
                pending.kill()
            except Exception:
                pass
            setattr(self, attribute, None)

    def _refresh_encoder_leds(self):
        leds = self._encoder_leds
        if leds is None:
            return
        # Three colour models, one per mode, and each says something different about what the
        # eight encoders *are*:
        #
        # * **Mix** — eight strips, so eight colours: each halo takes its own channel strip's
        #   track colour. The ring of lights tells you which tracks you are holding without
        #   looking at the screen (roadmap §4.3).
        # * **Plugin** — eight facets of one device, so one colour for the row: **the owning
        #   track's colour** (user, 2026-08-03), which is the same colour the header bar
        #   wears. Falls back to the factory blue for a track with no colour.
        # * **Song** — nothing track-shaped to follow, so the fixed Song purple.
        #
        # ⚠️ The Plugin colour comes from `_plugin_track_colour()`, which resolves the device
        # through the *same* `_plugin_device()` / `_plugin_header_track()` pair the header uses.
        # Deriving it separately is how a halo ends up wearing one track's colour while the
        # header names another — the §6b-16 rule: when two things must agree, do not compute
        # the agreement twice.
        mix = self._mode == MIX_MODE
        if mix:
            base = screen.Palette.KNOB_PLUGIN
        elif self._mode == PLUGIN_MODE:
            base = self._plugin_track_colour() or screen.Palette.KNOB_PLUGIN
        else:
            base = screen.Palette.KNOB_SONG
        for index in range(leds.count):
            if self._touch_held[index]:
                leds.set(index, screen.Palette.KNOB_TOUCHED)
            elif mix and self._mix_page == MIX_PAGE_SENDS and self._sends is not None:
                # Sends: the halo wears the colour of the track that **slot** belongs to, so the
                # two encoders in a column match and the grid reads as columns of tracks.
                track = self._sends.slot_track(index)
                leds.set(
                    index,
                    (live_rgb7(track) or base) if _liveobj_valid(track) else None,
                )
            elif mix:
                track = self._strip_track(index)
                # An empty strip is dark, the same as an unassigned parameter slot. A track
                # with no colour falls back to the row colour rather than going dark, so a
                # real strip is never invisible.
                leds.set(
                    index,
                    (live_rgb7(track) or base) if _liveobj_valid(track) else None,
                )
            elif self._is_encoder_assigned(index):
                leds.set(index, base)
            else:
                leds.set(index, None)
        try:
            leds.flush()
        except Exception:
            logger.exception("Motion32: encoder LED flush failed")

    def _is_encoder_assigned(self, index):
        """Song mode maps all eight; Plugin mode only as many as the bank provides."""
        if self._mode != PLUGIN_MODE:
            return True
        if index >= len(self._entries):
            return False
        return self._entries[index].assigned

    def bind_wheel(self, wheel_led):
        """Own the wheel halo. Lit for the whole of any mode that gives the wheel a job.

        That is **Plugin** (bank scroll, and click to step devices) and **Mix** (turning pages
        Volume/Pan) — see `_refresh_wheel_led`. Dark in Song, where the wheel does nothing.

        It deliberately does **not** react to press or to turning. A press highlight means the
        light changes while you are using the control, and every one of those transitions is a
        chance to end up dark; that is what "goes out depending on what it's interacting with"
        was. The wheel is a **mode-level** indicator, so mode is the only thing that moves it.
        """
        self._wheel_led = wheel_led
        self._refresh_wheel_led()
        self._schedule_led_reassert()

    def _refresh_wheel_led(self):
        leds = self._wheel_led
        if leds is None:
            return
        # Lit in every mode that gives the wheel a job, dark otherwise — Plugin (bank scroll
        # + click to step devices) and Mix (paging Volume/Pan). Still mode-level and nothing
        # else: a halo that changes while you are turning the control gives every transition a
        # chance to leave it dark, which is exactly what it used to do.
        colour = (
            screen.Palette.KNOB_PLUGIN
            if self._mode in (PLUGIN_MODE, MIX_MODE)
            else None
        )
        leds.set(0, colour)
        try:
            leds.flush()
        except Exception:
            logger.exception("Motion32: wheel LED flush failed")

    def bind_parameter_source(self):
        """Subscribe to the Device component and re-read the mapped parameters.

        Must be called by the surface *after* `ParameterSource.bind_device_component()`.
        `DeviceComponent.parameters` is a `listenable_property` notified from
        `_update_parameters()`, so this one subscription covers device changes *and* bank
        changes — which is what keeps the labels honest.
        """
        source = runtime.parameter_source()
        component = source.component if source is not None else None
        if component is None:
            logger.warning(
                "Motion32: no Device component to follow; encoder labels will stay empty"
            )
        else:
            self._on_mapped_parameters_changed.subject = component
        self._rebind_parameters()

    def bind_mixer(self, mixer_component):
        """Take the Mixer component as the source of Template 2's eight strips.

        Same late-binding reason as `bind_parameter_source`: this component is constructed
        inside `ControlSurface.setup()`, before the surface can hand it anything, so the
        surface calls this afterwards.

        Reading the strips off the component rather than off `song.visible_tracks` is what
        makes the view follow the **session ring**: `MixerComponent.channel_strip(i).track` is
        the track that strip is actually driving, offset included. Taking the first eight
        visible tracks instead would look right until the ring moved.
        """
        self._mixer = mixer_component
        self._rebind_mixer_strips()
        self._render()

    def bind_session_ring(self, session_ring):
        """Follow the session ring, so paging repaints the strips.

        🐛 **Without this the Mix screen only updated when something else happened to fire.**
        Paging the ring moved the eight tracks under the strips and nothing repainted; touching
        an encoder appeared to fix it, because a touch selects a track and *that* has a
        listener. Classic stale-screen: the content was right and nobody asked for it.

        The ring is the object carrying the `offset` event — `MixerComponent` itself listens to
        `offset` on its **provider**, which is the ring (`mixer.pyc.__init__` sets
        `self._provider.subject`). `SessionRingComponent` declares `offset` and `tracks` as
        `listenable_property`. The surface holds it as `_session_ring`
        (`ControlSurface._create_session_ring`).
        """
        self._session_ring = session_ring
        if session_ring is None:
            logger.warning(
                "Motion32: no session ring; the Mix screen will not follow ring paging"
            )
            return
        try:
            self._on_ring_offset_changed.subject = session_ring
            self._on_ring_tracks_changed.subject = session_ring
        except (AttributeError, RuntimeError):
            logger.exception("Motion32: could not follow the session ring")
        self._rebind_mixer_strips()

    @listens("offset")
    def _on_ring_offset_changed(self, *a):
        # New tracks under the strips: re-point the per-track listeners, then repaint.
        self._rebind_mixer_strips()
        self._refresh_encoder_leds()
        self._render()

    @listens("tracks")
    def _on_ring_tracks_changed(self, *a):
        self._rebind_mixer_strips()
        self._refresh_encoder_leds()
        self._render()

    def _rebind_mixer_strips(self):
        """Listen to the eight tracks the strips are showing.

        🐛 **This is the other half of the stale screen.** Turning an encoder moved the volume
        in Live and the fader on screen did not follow, because nothing was listening to it —
        the only value listeners in this component are for *device parameters* (Plugin mode).
        The value jumped into place on the next unrelated render, which is why touching another
        encoder appeared to "fix" it.

        Five things per strip, because all five are on screen: volume (the fader), mute and
        solo (the two indicators), and name and colour (the label and its swatch). Colour also
        drives the halo, so the handler refreshes both.

        Rebound rather than permanent: the ring moves the tracks, so these listeners have to
        move with it.
        """
        self._clear_mixer_listeners()
        for index in range(MIXER_STRIP_COUNT):
            track = self._strip_track(index)
            if not _liveobj_valid(track):
                continue
            try:
                volume = track.mixer_device.volume
            except (AttributeError, RuntimeError):
                volume = None
            if volume is not None:
                self._add_mixer_listener(
                    volume,
                    "add_value_listener",
                    "value_has_listener",
                    "remove_value_listener",
                )
            try:
                panning = track.mixer_device.panning
            except (AttributeError, RuntimeError):
                panning = None
            if panning is not None:
                # 🐛 **The Pan page had no listener.** The same omission as the volume fader,
                # one page along: `_mixer_pan_content` reads `mixer_device.panning` and nothing
                # was watching it, so the arcs only moved when an unrelated event forced a
                # render. Every Live value the Mix screen reads needs an entry here.
                self._add_mixer_listener(
                    panning,
                    "add_value_listener",
                    "value_has_listener",
                    "remove_value_listener",
                )
            for verb in ("mute", "solo", "name", "color"):
                self._add_mixer_listener(
                    track,
                    f"add_{verb}_listener",
                    f"{verb}_has_listener",
                    f"remove_{verb}_listener",
                )

    def _add_mixer_listener(self, subject, add, has, remove):
        try:
            listener = self._mixer_strip_listener()
            getattr(subject, add)(listener)
            self._mixer_slots.append((subject, has, remove, listener))
        except (AttributeError, RuntimeError):
            pass

    def _mixer_strip_listener(self):
        """One handler for everything a strip shows.

        The halos are refreshed too because a track's colour drives them in Mix mode, and the
        LED diff makes the redundant case free — a volume change queues eight identical
        colours and sends nothing.
        """

        def _on_changed(*a):
            self._refresh_encoder_leds()
            self._render()

        return _on_changed

    def _clear_mixer_listeners(self):
        for subject, has, remove, listener in self._mixer_slots:
            try:
                if getattr(subject, has)(listener):
                    getattr(subject, remove)(listener)
            except (AttributeError, RuntimeError):
                pass
        self._mixer_slots = []

    def bind_mix_pages(self, modes_component) -> None:
        """Follow Mix mode's page selection.

        The page decides the **template**, so the screen has to know it: Volume is Template 2's
        strips, Pan is Template 0's arcs. Bound rather than inferred, and read through
        `_screen_layer()` like everything else so the view and the content stay in step.
        """
        self._mix_pages = modes_component
        if modes_component is None:
            logger.warning("Motion32: no Mix_Pages component; Mix will not page to Pan")
            return
        try:
            self._on_mix_page_changed.subject = modes_component
        except (AttributeError, RuntimeError):
            logger.exception("Motion32: could not follow the Mix page")
        self._render()

    @listens("selected_mode")
    def _on_mix_page_changed(self, *a):
        # A page change swaps the template *and* what the encoders are mapped to, so the
        # halos want re-asserting alongside the repaint.
        self._refresh_encoder_leds()
        # Volume shows meters, Pan draws Template 0 and has none — so the poll follows the page.
        self._update_meter_task()
        self._render()

    @property
    def _mix_page(self) -> str:
        try:
            return self._mix_pages.selected_mode or MIX_PAGE_VOLUME
        except AttributeError:
            return MIX_PAGE_VOLUME

    def bind_modes(self, modes_component):
        """Follow the main mode, so the Plugin button reveals the device view.

        Called by the surface after setup, because the modes component is created from
        `create_mappings` and does not exist while this component is being built.
        """
        self._modes = modes_component
        if modes_component is not None:
            self._on_selected_mode_changed.subject = modes_component
        self._render()

    # -- lifecycle ---------------------------------------------------------
    def disconnect(self):
        self._clear_mixer_listeners()
        for index in range(PARAMETERS_PER_BANK):
            self._cancel_hide(index)
        self._stop_live_refresh()
        # ⚠️ `_kill_task`, not `_stop_meters` — the latter renders, and rendering into a
        # surface that is being torn down is how a superseded instance writes to a device it no
        # longer owns (§7). Teardown blanks the screen wholesale anyway.
        self._kill_task("_meter_task")
        self._kill_task("_led_reassert_task")
        self._kill_task("_notification_task")
        self._clear_value_listeners()
        self._clear_track_listeners()
        super().disconnect()

    def full_redraw(self):
        """Re-send everything. Used after connect and after the device's Global Settings
        screen closes (both leave the display in an unknown state)."""
        model = runtime.screen_model()
        view = self._view_for_mode()
        if model is None or view is None:
            # Silence here was hiding a blank screen; say so.
            logger.warning(
                "Motion32: full_redraw with no screen model/view "
                f"(model={model is not None}, view={view is not None})"
            )
            return
        model.invalidate()
        # **Every** view must forget: the cache was just cleared for every template, so a later
        # mode switch would otherwise short-circuit on an unchanged snapshot and draw nothing.
        #
        # ⚠️ **The list is derived, not typed out.** `runtime.views()` is the single roster;
        # `MixerView` was missing from a hand-written list here for the whole of Phase 7 (found
        # 2026-08-03) and got away with it only because `invalidate()` clears `_sent` and leaves
        # `_desired` intact. That is the same shape as the LED-group bug two lines below, where
        # the pads were added to one named list and not the other — hence one roster, two
        # readers, and a guard that fails if a view exists outside it.
        for each in runtime.views():
            each.forget()
        self._active_view = view
        view.activate()
        # The device forgot its LED state too, not just the screen — so **every** group has to
        # be invalidated and repainted, not just the halos.
        #
        # 🐛 This listed `_encoder_leds` by name and refreshed only that. When the pads were
        # added they were silently left out, so after connect the keybed stayed dark until a
        # mode change happened to run `_schedule_led_reassert` (which did include them). A
        # named list is exactly the thing that goes stale when a group is added, so both paths
        # now iterate `_led_groups()`.
        self._invalidate_led_groups()
        self._refresh_all_leds()
        logger.info(
            f"Motion32: redraw — mode={self._mode!r} suspended={model.suspended} "
            f"pending={model.pending_count()}"
        )
        self._render()

    # -- change detection --------------------------------------------------
    # Both take *a: a `listens` handler is called with whatever the notifier passes, and
    # that differs per property — `notify_parameters()` passes nothing while
    # `selected_mode` passes the new mode. Accepting *a makes the handler correct either
    # way instead of raising TypeError inside a Live callback.
    @listens("parameters")
    def _on_mapped_parameters_changed(self, *a):
        self._rebind_parameters()

    @listens("selected_mode")
    def _on_selected_mode_changed(self, *a):
        # You asked for a different screen; you get it now, not in a second's time.
        self._kill_task("_notification_task")
        self._notification = None
        # Mix mode is the only one with meters, so the poll starts and stops here. Before the
        # render below, so entering Mix draws its first frame with real levels rather than
        # zeros that get corrected 100 ms later.
        self._update_meter_task()
        # Scale mode swaps the pad layout on the way in and hands it back on the way out.
        self._refresh_layout()
        self._refresh_pad_leds()
        # …and the Control button needs to know where to return to.
        self._remember_mode()
        if self._mode == PLUGIN_MODE:
            # Bring Live's device chain up: without this the Motion shows a device you cannot
            # see on the laptop, which makes the parameter names hard to place.
            self._show_device_chain()
            # Re-read on the way in: the Device component only reports its mapped parameters
            # once its layer has been granted, which happens as this mode is entered.
            self._rebind_parameters()
        else:
            self._render()
        # The framework re-grabs layers as part of this change and resets the encoder
        # elements, which writes to the halo addresses. Assert them again once it settles.
        self._schedule_led_reassert()

    def _show_device_chain(self):
        """Show the Detail pane with the device chain in it.

        `show_view("Detail/DeviceChain")` is the counterpart of the framework's
        `clip_view_toggle_button`, which shows/hides `"Detail/Clip"` — the two are the two
        halves of Live's detail pane.
        """
        try:
            view = self.application.view
        except (AttributeError, RuntimeError, TypeError):
            return
        for name in ("Detail", "Detail/DeviceChain"):
            try:
                if not view.is_view_visible(name):
                    view.show_view(name)
            except (AttributeError, RuntimeError):
                continue

    # Song-mode sources. Each just re-renders; the diff in ScreenModel means an unchanged
    # value costs nothing on the wire.
    @listens("tempo")
    def _on_tempo_changed(self, *a):
        self._render()

    @listens("loop_start")
    def _on_loop_start_changed(self, *a):
        self._render()

    @listens("loop_length")
    def _on_loop_length_changed(self, *a):
        self._render()

    @listens("signature_numerator")
    def _on_signature_changed(self, *a):
        self._render()

    @listens("focused_document_view")
    def _on_focused_document_view_changed(self, *a):
        self._render()

    @listens("selected_track")
    def _on_selected_track_changed(self, *a):
        # Pads rest in the focused track's colour, so a selection change repaints them.
        self._refresh_pad_leds()
        # Re-point the name listener as well as redrawing: the *selection* changing and the
        # selected track being *renamed* are different events, and Song mode shows the name.
        self._rebind_track()
        self._render()

    def _rebind_track(self):
        """Follow the selected track's name.

        Without this the title only refreshed when some other event happened to trigger a
        render — the "track name updates sometime later" symptom.
        """
        self._clear_track_listeners()
        song = self._live_song
        if song is None:
            return
        try:
            track = song.view.selected_track
        except (RuntimeError, AttributeError):
            return
        for add, has, remove in (
            ("add_name_listener", "name_has_listener", "remove_name_listener"),
            # `color` is an observable LOM property, so recolouring a track in Live repaints
            # the centre bar — and the keybed — immediately instead of waiting for some
            # unrelated event.
            ("add_color_listener", "color_has_listener", "remove_color_listener"),
        ):
            try:
                listener = self._track_appearance_listener()
                getattr(track, add)(listener)
                self._track_slots.append((track, has, remove, listener))
            except (RuntimeError, AttributeError):
                continue

    def _track_appearance_listener(self):
        """For the selected track's *name* and *colour*.

        Both feed the screen, and the colour also feeds the pads — so recolouring the current
        track in Live has to repaint the keybed, not just the centre bar. Routing name and
        colour through one handler keeps that from depending on which listener fired; the LED
        diff makes the redundant half free (a rename queues 32 identical colours and sends
        nothing).
        """

        def _on_changed(*a):
            self._refresh_pad_leds()
            self._render()

        return _on_changed

    def _clear_track_listeners(self):
        for subject, has, remove, listener in self._track_slots:
            try:
                if getattr(subject, has)(listener):
                    getattr(subject, remove)(listener)
            except (RuntimeError, AttributeError):
                pass
        self._track_slots = []

    @property
    def _mode(self) -> str:
        try:
            return self._modes.selected_mode or ""
        except AttributeError:
            return ""

    def _rebind_parameters(self):
        self._clear_value_listeners()
        source = runtime.parameter_source()
        self._entries = source.entries() if source is not None else []

        for index, entry in enumerate(self._entries):
            if not entry.assigned:
                continue
            try:
                listener = partial(self._on_parameter_value_changed, index)
                entry.parameter.add_value_listener(listener)
                self._value_slots.append((entry.parameter, listener))
            except (RuntimeError, AttributeError):
                continue
        self._refresh_encoder_leds()
        self._render()

    def _clear_value_listeners(self):
        for parameter, listener in self._value_slots:
            try:
                if parameter.value_has_listener(listener):
                    parameter.remove_value_listener(listener)
            except (RuntimeError, AttributeError):
                pass
        self._value_slots = []

    # -- transient value display -------------------------------------------
    # A `control_list` handler is called with **the control**, not an index — the index is
    # `button.index`. (Verified against the framework's own `ActiveParameterComponent`,
    # which implements this very feature the same way, and `SessionComponent`. Note the
    # 2D `control_matrix` handlers do take a separate leading argument, which is what makes
    # this easy to get wrong.)
    @encoder_touch_buttons.pressed
    def encoder_touch_buttons(self, button):
        index = self._touch_index(button)
        if index is None:
            return
        self._touch_held[index] = True
        self._refresh_encoder_leds()
        if self._mode == MIX_MODE:
            # 🔑 **Focus, by selecting the track.** The roadmap's Phase 7 design is that
            # cap-touch focuses a channel strip so Solo/Mute act on it, and it warns that the
            # focus must *persist* rather than time out like Plugin mode's value readout —
            # "the same event source with opposite semantics, which is exactly the kind of
            # reuse that produces a subtle bug".
            #
            # Selecting the track sidesteps that trap entirely instead of managing a second
            # timeout. `Target_Channel_Strip` already follows the target track, which is the
            # selected one, so Solo and Mute follow for free; a selection persists by
            # definition; and Live's own highlight agrees with the screen's. There is no
            # separate focus state to keep in step — the on-screen mark is *derived* from the
            # selection in `_mixer_content`.
            self._select_strip_track(index)
            # 🐛 **The Pan page showed no value on touch.** Focusing used to `return` here for
            # the whole of Mix mode, which was wrong for Pan: Template 0 gives one text element
            # per tile and the value has to share it with the name, exactly as in Plugin mode.
            if self._mix_page not in (MIX_PAGE_PAN, MIX_PAGE_SENDS):
                # **Volume page: the strip's label shows the volume while you hold the
                # encoder** (user, 2026-08-03). Template 2 has one text element per strip, so
                # the reading replaces the track name for as long as the touch lasts.
                #
                # No `_show_value` and no timeout — `_mixer_strip` reads `_touch_held`
                # directly, so the render below is all that is needed and the release handler
                # undoes it by the same route. An explicit render is required because
                # `_select_strip_track` only fires a listener when the selection actually
                # *changes*; touching the already-selected strip would otherwise show nothing.
                self._render()
                return
        self._show_value(index)

    @encoder_touch_buttons.released
    def encoder_touch_buttons(self, button):
        index = self._touch_index(button)
        if index is None:
            return
        self._touch_held[index] = False
        self._refresh_encoder_leds()
        if self._mode == MIX_MODE and self._mix_page not in (MIX_PAGE_PAN, MIX_PAGE_SENDS):
            # **Volume page: the name comes back the instant you let go** (user, 2026-08-03) —
            # no `_schedule_hide`, no 0.75 s wait. `_touch_held[index]` is already False by the
            # line above, so this render restores the track name by itself.
            #
            # Deliberately different from Plugin mode and from the Pan page, which *do* time
            # out: there the value is uncovered by a touch that may not be followed by a turn,
            # so it needs a moment to be read. Here the fader is on screen permanently and the
            # number is a precision aid while your finger is down — holding it after release
            # would hide the track name for nothing.
            #
            # The *focus* is unaffected and still persists: it is the track selection, not this
            # reveal, which is exactly why the roadmap insisted the two not share a mechanism.
            self._render()
            return
        # Reveal-on-touch alone is useful even without a turn, so start the timeout on
        # release rather than clearing immediately.
        self._schedule_hide(index)

    def _touch_index(self, button):
        try:
            index = int(button.index)
        except (AttributeError, TypeError, ValueError):
            return None
        return index if 0 <= index < PARAMETERS_PER_BANK else None

    def _on_parameter_value_changed(self, index):
        """A mapped parameter moved — from the encoder, the mouse, or automation."""
        self._show_value(index)
        if not self._touch_held[index]:
            # Turning without touch (or a change from elsewhere in Live) still reveals
            # the value; it just starts timing out immediately.
            self._schedule_hide(index)
        self._render()

    def _show_value(self, index):
        self._cancel_hide(index)
        if not self._showing_value[index]:
            self._showing_value[index] = True
            self._render()
        self._start_live_refresh()

    # -- Mix-mode meters (Phase 7c) ----------------------------------------
    #
    # ⚠️ **The only polled thing in this script, and it is polled on purpose.** Everything else
    # here is event-driven: the roadmap's rule is that every fact on screen needs an event, and
    # the bugs that rule exists to prevent were all stale-screen bugs. Meters are the documented
    # exception, for a reason that is the opposite of the usual one — `output_meter_left` *is*
    # observable, but it fires far faster than any rate the screen can use, so a listener would
    # flood the diff to produce a picture no better than 10 Hz gives.
    #
    # `task.loop` is the framework's own repeating idiom (`ScrollComponent._make_scroll_task`),
    # deliberately used instead of the self-rescheduling chain `_schedule_live_refresh` uses:
    # a chain that misses one reschedule stops for good and looks like "the meters froze", and
    # this loop runs for as long as Mix mode is up rather than for a 0.75 s timeout.

    def _meters_wanted(self) -> bool:
        """True while the meters are actually on screen.

        Gated on **mode and page**, not on `_screen_layer()`. The two differ while a
        notification is up: the bar borrows Template 1 for a second, but Template 2 keeps its
        own element state underneath (the same property the notification bar's cheapness
        depends on), so stopping the loop for that second would only make the meters jump when
        the bar cleared. The Pan page is a real stop — it draws Template 0, which has no meter
        element at all.
        """
        return self._mode == MIX_MODE and self._mix_page == MIX_PAGE_VOLUME

    def _update_meter_task(self):
        """Start or stop the poll to match `_meters_wanted()`. Idempotent."""
        if self._meters_wanted():
            self._start_meters()
        else:
            self._stop_meters()

    def _start_meters(self):
        if self._meter_task is not None:
            return
        try:
            self._meter_task = self._tasks.add(
                task.loop(task.wait(METER_INTERVAL), task.run(self._poll_meters))
            )
        except Exception:
            # No task group: the strips still work, they just have no meters. Loud, because
            # "the meters never came on" has no other explanation available from the device.
            logger.exception("Motion32: could not start the meter loop; meters will be dark")
            self._meter_task = None

    def _stop_meters(self):
        if self._meter_task is None:
            return
        try:
            self._meter_task.kill()
        except Exception:
            pass
        self._meter_task = None
        # Leaving Mix mode mid-decay would freeze a bar at whatever it last showed, and the
        # device holds each template's element state — so it would still be sitting there on
        # the next visit. One render with the loop stopped zeroes them.
        self._render()

    def _poll_meters(self):
        """One frame. Deliberately just a render.

        The meter values live in `MixerStrip`, so a render is what puts them on the wire, and
        routing them through the ordinary path means they are diffed, suspended during Global
        Settings, and validated against the template map like every other element. A private
        write path for meters would have to reimplement all four.
        """
        if not self._meters_wanted():
            # The gate can close between frames — a mode change kills the task, but a page
            # change that races it would otherwise get one stray frame on the wrong template.
            self._stop_meters()
            return
        self._render()

    # -- live refresh while a value is on screen ---------------------------
    #
    # Song-mode encoders have no single property to listen to: arrangement position, zoom
    # and cue are driven by the framework's Transport/Zoom components mutating Live, and
    # `current_song_time` is far too chatty to subscribe to. So while a value is actually
    # being displayed, re-read at a modest rate. The ScreenModel diff means an unchanged
    # value sends nothing, so an idle refresh is free — this costs wire traffic only while a
    # number is genuinely moving.
    LIVE_REFRESH_INTERVAL = 0.05  # 20 Hz, smooth enough to read while turning

    def _start_live_refresh(self):
        if self._live_refresh_task is not None:
            return
        self._schedule_live_refresh()

    def _schedule_live_refresh(self):
        try:
            self._live_refresh_task = self._tasks.add(
                task.sequence(
                    task.wait(self.LIVE_REFRESH_INTERVAL),
                    task.run(self._live_refresh),
                )
            )
        except Exception:
            # No task group: values still update on their listeners, just less smoothly.
            logger.exception("Motion32: could not schedule the live value refresh")
            self._live_refresh_task = None

    def _live_refresh(self):
        self._live_refresh_task = None
        if not any(self._showing_value):
            return
        self._render()
        self._schedule_live_refresh()

    def _stop_live_refresh(self):
        if self._live_refresh_task is not None:
            try:
                self._live_refresh_task.kill()
            except Exception:
                pass
            self._live_refresh_task = None

    def _schedule_hide(self, index):
        self._cancel_hide(index)
        try:
            self._hide_tasks[index] = self._tasks.add(
                task.sequence(task.wait(VALUE_TIMEOUT), task.run(partial(self._hide_value, index)))
            )
        except Exception:
            # Without a task group the value would stick; drop straight back to the name
            # rather than leaving the screen wrong.
            logger.exception("Motion32: could not schedule the value timeout")
            self._hide_value(index)

    def _cancel_hide(self, index):
        pending = self._hide_tasks[index]
        if pending is not None:
            try:
                pending.kill()
            except Exception:
                pass
            self._hide_tasks[index] = None

    def _hide_value(self, index):
        self._hide_tasks[index] = None
        if self._showing_value[index]:
            self._showing_value[index] = False
            self._render()
        if not any(self._showing_value):
            self._stop_live_refresh()

    # -- content -----------------------------------------------------------
    def _screen_layer(self) -> str:
        """**The one place that decides what is on screen.** Everything else looks it up.

        🐛 View and content MUST come from the same decision. They were once made separately —
        `_view_for_mode()` from `self._mode`, `_content()` from `self._mode` *and*
        `self._modes is not None` — so before the modes component binds (`_mode` is `""`) the
        **Params view was handed Main content**. It only appeared to work because the content
        classes happen to share field names.

        The first fix gave both functions the same two predicates and required them to be
        called in the same order. That works for three layers and stops working at four: an
        ordered chain of `if`s is a rule a reader has to maintain, not one the structure
        enforces. Returning a **key** that both functions index by makes disagreement
        impossible rather than merely tested for — see `_VIEWS` and `_CONTENT`.

        The suspend gate in `ScreenModel.flush` still outranks this: a notification raised
        while the device is in Global Settings queues silently, and the redraw on close sorts
        it out.
        """
        if self._notification is not None:
            return NOTIFICATION_LAYER
        mode = self._mode
        if mode == MIX_MODE:
            # Mix has two pages and they use different templates, so the page is part of the
            # layer key rather than a separate flag — same reason the notification bar is a
            # key and not a boolean.
            page = self._mix_page
            if page == MIX_PAGE_PAN:
                return MIX_PAN_LAYER
            if page == MIX_PAGE_SENDS:
                return MIX_SENDS_LAYER
            return MIX_MODE
        if mode == SCALE_MODE:
            return SCALE_MODE
        # An unknown or not-yet-bound mode falls back to Song, which is also the startup mode.
        return mode if mode == PLUGIN_MODE else SONG_MODE

    def _content(self):
        if self._screen_layer() == NOTIFICATION_LAYER:
            return self._notification
        return self._CONTENT[self._screen_layer()](self)

    # -- notifications -----------------------------------------------------
    def notify(self, title, value=""):
        """Raise the transient bar for `NOTIFICATION_TIMEOUT`, then fall back to the mode.

        ⚠️ **Suppressed while the scale menu is up** (user, 2026-08-03). The bar and the menu are
        both Template 1: the bar blanks the twelve rows to draw itself, so an Octave or A-H
        announcement in Scale mode wipes the list you are reading and then has to rebuild it.
        Scale mode shows its state permanently — the highlighted row, the `Locked`/`Guide` label
        — so there is nothing the bar could add that is worth that.

        Generic on purpose: it takes a label and a value and knows nothing about octaves.
        Octave is simply the first caller; A-H banking, scale/root and tempo want the same
        two fields (`notification.py`).

        ⚠️ **Never call this from the pad path.** A pad press must reach the note translation
        and nothing else — no Python between press and note. This runs on button handlers,
        which are not on that path.
        """
        if self._screen_layer() == SCALE_MODE:
            return
        content = NotificationContent(title=str(title), value=str(value))
        # Re-notifying restarts the clock rather than queueing, so holding Octave Up keeps
        # one bar alive showing the running value instead of stacking four of them.
        self._kill_task("_notification_task")
        self._notification = content
        try:
            self._notification_task = self._tasks.add(
                task.sequence(
                    task.wait(NOTIFICATION_TIMEOUT), task.run(self._dismiss_notification)
                )
            )
        except Exception:
            # Without a task group the bar would never come down and the mode's screen would
            # be lost for good. Show nothing rather than strand the display.
            logger.exception("Motion32: could not schedule the notification timeout")
            self._notification = None
        self._render()

    def _dismiss_notification(self):
        self._notification_task = None
        if self._notification is None:
            return
        self._notification = None
        # One message on the wire: the base template's elements were never disturbed, so the
        # diff has nothing to say and only the template select goes out.
        self._render()

    def _plugin_device(self):
        """The device Plugin mode is showing, or None.

        **One resolver, two readers** — `_device_content` draws it and `_plugin_track_colour`
        colours the halos from it. Both used to be a possibility rather than a fact: if the
        halos resolved the device independently they could light for one track while the
        header named another, which is the §6b-16 failure shape.
        """
        source = runtime.parameter_source()
        device = source.device() if source is not None else None
        if _liveobj_valid(device):
            return device
        # Fall back to the appointed device: the framework's Device component reports none
        # until its layer is granted, so relying on it alone leaves the first render after a
        # mode change with nothing to show.
        device = self._appointed_device()
        return device if _liveobj_valid(device) else None

    def _plugin_track_colour(self):
        """The colour Plugin mode's header wears — and now its encoder halos too.

        With a device in focus that is the device's **owning** track; with none it is the
        selected track, which is exactly what `_device_content`'s no-device branch shows. Both
        branches go through the same two helpers as the header, so the halo cannot disagree
        with the bar above it.
        """
        device = self._plugin_device()
        if device is None:
            return self._selected_track_colour()
        return live_rgb7(self._plugin_header_track(device))

    def _device_content(self) -> MainContent:
        source = runtime.parameter_source()
        device = self._plugin_device()

        if device is None:
            # Never draw an empty screen — an empty screen is indistinguishable from a
            # broken one. Say which track is in focus and that it has no device, and label
            # the tiles so the layout still reads as a device view.
            return MainContent(
                title=compactify(self._selected_track_name(), MAXCHARS_HEADER_TITLE),
                header_background=self._selected_track_colour(),
                centre=NO_DEVICE_TEXT,
                tiles=tuple(
                    EncoderTile(label="-", assigned=False) for _ in range(PARAMETERS_PER_BANK)
                ),
                soft_labels=PLUGIN_SOFT_LABELS,
            )

        try:
            device_name = str(device.name or "")
        except (RuntimeError, AttributeError):
            device_name = ""

        tiles = []
        for index, entry in enumerate(self._entries):
            if not entry.assigned:
                tiles.append(EncoderTile())
                continue
            tiles.append(
                EncoderTile(
                    label=entry.name,
                    value=_normalized_value(entry.parameter),
                    assigned=True,
                    value_text=truncate_value(
                        format_parameter_value(entry.parameter), MAXCHARS_ENCODER_LABEL
                    ),
                    show_value=self._showing_value[index],
                )
            )
        while len(tiles) < PARAMETERS_PER_BANK:
            tiles.append(EncoderTile())

        header_track = self._plugin_header_track(device)
        return MainContent(
            # "Track | Device" — the header's full width is free because Plugin mode leaves the
            # top soft-button labels blank. Title and colour both come from `header_track`.
            title=self._plugin_title(header_track, device_name),
            header_background=live_rgb7(header_track),
            centre=self._centre_text(source, device),
            tiles=tuple(tiles),
            soft_labels=PLUGIN_SOFT_LABELS,
        )

    # -- Song mode (Template 3) --------------------------------------------
    def _song_content(self) -> ParamsContent:
        """High-level song info on Template 3 — the factory's Song/Timeline screen.

        Template 3 gives each tile a separate **label** and **value** element, so the full
        parameter name and its live reading are both on screen at once. No reveal-on-touch
        needed here; that exists only because Template 0 has one text element per tile.

        Layout follows the factory Song screen:
          * header  — which Live view is up ("Session" / "Arrangement")
          * grey bar — the selected track
          * 8 tiles  — encoder name + current value

        Labels come from `mappings.SONG_ENCODERS`, the same table that assigns the encoders,
        so a label cannot drift from what the knob under it does.

        Position is read at render time rather than listened to: `current_song_time` fires
        continuously during playback and would flood the wire. The 20 Hz live refresh covers
        it while a value is actually moving.
        """
        song = self._live_song

        tiles = []
        for control, label, _owner in SONG_ENCODERS:
            value_text, _fill = self._song_encoder_readout(song, control)
            if not value_text:
                # Nothing readable to show (zoom, cue): use the second line for what turning
                # the encoder does, rather than leaving half the tile empty.
                value_text = SONG_ENCODER_HINTS.get(control, "")
            tiles.append(ParamsTile(label=label, value=value_text, assigned=True))

        return ParamsContent(
            title=self._view_mode_name(),
            centre=self._selected_track_name(),
            centre_background=self._selected_track_colour(),
            tiles=tuple(tiles),
            soft_labels=SONG_SOFT_LABELS,
        )

    def _selected_track_colour(self):
        """The selected track's real colour, or None to fall back to the factory grey.

        `track.color` is `0x00rrggbb` and user-chosen, so this is deliberately a conversion
        and not a lookup — any colour the user picks renders correctly.
        """
        song = self._live_song
        if song is None:
            return None
        try:
            return live_rgb7(song.view.selected_track)
        except (RuntimeError, AttributeError):
            return None

    def _view_mode_name(self) -> str:
        """"Session" or "Arrangement", from whichever Live view is showing.

        Kept to one word: the header title budget is 13 characters, so "Arrangement Mode"
        (16) would be mangled by the abbreviator. "Session" / "Arrangement" reads cleanly and
        matches the factory's single-word header ("Timeline").
        """
        # `Component.application` is a **property**, not a method — calling it raises
        # `TypeError: 'Application' object is not callable`. Same for `song`, `parent`,
        # `layer`, `is_root`. (`is_enabled()` *is* a method. See §4 of the notes.)
        try:
            view = self.application.view
        except (AttributeError, RuntimeError, TypeError):
            return ""
        try:
            if view.is_view_visible("Session"):
                return "Session"
            if view.is_view_visible("Arranger"):
                return "Arrangement"
        except (AttributeError, RuntimeError):
            return ""
        return ""

    @staticmethod
    def _song_time(song):
        try:
            return float(song.current_song_time)
        except (RuntimeError, AttributeError, TypeError):
            return None

    @staticmethod
    def _format_beats(song, beats) -> str:
        """Beats -> bars.beats, using the song's time signature."""
        if beats is None:
            return ""
        try:
            per_bar = int(song.signature_numerator) or 4
        except (RuntimeError, AttributeError, TypeError):
            per_bar = 4
        bar = int(beats // per_bar) + 1
        beat = int(beats % per_bar) + 1
        return f"{bar}.{beat}"

    def _song_encoder_readout(self, song, control_name):
        """(value text, 0-127 fill) for one Song-mode encoder."""
        if song is None:
            return "", 0
        try:
            if control_name in ("tempo_coarse_encoder", "tempo_fine_encoder"):
                tempo = float(song.tempo)
                # Live's tempo range is 20-999 BPM.
                return f"{tempo:.1f}", int(round((tempo - 20.0) / 979.0 * 127))
            if control_name == "arrangement_position_encoder":
                return self._format_beats(song, self._song_time(song)), 0
            if control_name == "loop_start_encoder":
                return self._format_beats(song, float(song.loop_start)), 0
            if control_name == "loop_length_encoder":
                return self._format_beats(song, float(song.loop_length)), 0
            if control_name == "prehear_volume_control":
                # Live's preview/cue level lives on the master track's mixer device.
                parameter = song.master_track.mixer_device.cue_volume
                return truncate_value(format_parameter_value(parameter), 9), _normalized_value(
                    parameter
                )
        except (RuntimeError, AttributeError, TypeError, ValueError):
            return "", 0
        # Zoom and cue have no readable value — label only.
        return "", 0

    def _plugin_header_track(self, device):
        """The track the Plugin header names — the device's owner, else the selected track.

        The header's **colour and its text must come from this one object**. Deriving them
        separately is how a bar ends up naming one track while wearing another's colour, which
        is the same failure as §6b-16 in the implementation notes: when two things must agree,
        do not compute the agreement twice.
        """
        try:
            track = device.canonical_parent
            if _liveobj_valid(track):
                return track
        except (RuntimeError, AttributeError):
            pass
        song = self._live_song
        if song is None:
            return None
        try:
            return song.view.selected_track
        except (RuntimeError, AttributeError):
            return None

    def _plugin_title(self, track, device_name) -> str:
        """`Track | Device`, falling back to whichever half we can read."""
        try:
            track_name = str(track.name or "") if track is not None else ""
        except (RuntimeError, AttributeError):
            track_name = ""
        if track_name and device_name:
            return f"{track_name} | {device_name}"
        return device_name or track_name

    def _appointed_device(self):
        """Live's own "blue hand" device — what the Device component follows."""
        song = self._live_song
        if song is None:
            return None
        device = getattr(song, "appointed_device", None)
        if _liveobj_valid(device):
            return device
        try:
            device = song.view.selected_track.view.selected_device
        except (RuntimeError, AttributeError):
            return None
        return device if _liveobj_valid(device) else None

    def _selected_track_name(self) -> str:
        song = self._live_song
        try:
            return str(song.view.selected_track.name or "")
        except (RuntimeError, AttributeError):
            return ""

    # -- which view is on screen -------------------------------------------
    def _view_for_mode(self):
        """Template 3 for Song, Template 0 for Plugin, Template 2 for Mix.

        Song mode wants numbers (tempo, bars.beats), which Template 3 shows permanently
        alongside the name. Plugin mode keeps Template 0 for its encoder arcs — a device
        parameter reads better as a fill than as a number, with the value revealed on touch.
        Mix mode gets Template 2, which is eight channel strips and nothing else: it has no
        header or title zone at all.

        Indexed by `_screen_layer()`, the same key `_content()` uses, so the two cannot disagree.
        """
        return self._VIEWS[self._screen_layer()]()

    def _centre_text(self, source, device) -> str:
        """Live's own bank name if there is one, else the owning track.

        The bank name is the honest thing to show now that the bank buttons are mapped —
        it is what Live calls the current page ("Filter", "Envelope", ...), not a
        synthetic counter.
        """
        bank = source.bank_label() if source is not None else ""
        if bank:
            return compactify(bank, MAXCHARS_CENTRE)
        try:
            return compactify(str(device.canonical_parent.name or ""), MAXCHARS_CENTRE)
        except (RuntimeError, AttributeError):
            return ""

    def _strip_track(self, index: int):
        """The Live track strip `index` is driving, or None."""
        if self._mixer is None:
            return None
        try:
            return self._mixer.channel_strip(index).track
        except (AttributeError, IndexError, RuntimeError):
            return None

    def _touched_track(self, index: int):
        """The track encoder `index` belongs to **on the current page**.

        🐛 **Not `_strip_track(index)`, and that was the bug.** On Volume and Pan, encoder N is
        strip N, so the two are the same. On the **Sends** page encoder N is a (track, send)
        slot — encoder 5 is track 1's send *B* — so selecting the strip at the encoder's index
        focused a different track from the one the encoder turns. Touch highlighted one track
        while the knob moved another's send. Found on hardware 2026-08-03.

        The page owns the mapping, so the page has to answer this question too.
        """
        if (
            self._mode == MIX_MODE
            and self._mix_page == MIX_PAGE_SENDS
            and self._sends is not None
        ):
            return self._sends.slot_track(index)
        return self._strip_track(index)

    def _select_strip_track(self, index: int) -> None:
        track = self._touched_track(index)
        if not _liveobj_valid(track):
            return
        song = self._live_song
        if song is None:
            return
        try:
            if song.view.selected_track != track:
                song.view.selected_track = track
        except (AttributeError, RuntimeError):
            logger.exception("Motion32: could not focus the touched channel strip")

    def _focused_strip(self):
        """Which strip holds the selected track, or None.

        **Derived, never stored.** The alternative — a `_focused` int set on touch — is a
        second copy of a fact Live already owns, and the pad-roles bug earlier in this project
        is what two copies of a layout fact look like. Here the selection *is* the focus.
        """
        song = self._live_song
        if song is None:
            return None
        try:
            selected = song.view.selected_track
        except (AttributeError, RuntimeError):
            return None
        for index in range(MIXER_STRIP_COUNT):
            if self._strip_track(index) == selected:
                return index
        return None

    def _mixer_content(self) -> MixerContent:
        """Eight channel strips off the Mixer component.

        An absent track gives an **unassigned** strip rather than a hidden one — the factory
        greys, it never hides, and Template 2's label element cannot be hidden anyway (it has
        `text` but no `visible`).
        """
        strips = []
        for index in range(MIXER_STRIP_COUNT):
            strips.append(self._mixer_strip(index))
        return MixerContent(strips=tuple(strips), focused=self._focused_strip())

    def _mixer_pan_content(self) -> MainContent:
        """Mix mode's **Pan** page — Template 0's eight arcs, one per channel strip.

        Template 2 has no pan element at all, so the page borrows the encoder-tile view. An
        arc suits a pan better than a number anyway: centre reads at a glance.

        The tile's single text element carries the **track name** at rest and the pan value
        while the encoder is touched, which is the same reveal-on-touch Plugin mode uses and
        for the same reason — Template 0 gives one text element per tile, not two.
        """
        tiles = []
        for index in range(MIXER_STRIP_COUNT):
            track = self._strip_track(index)
            if not _liveobj_valid(track):
                tiles.append(EMPTY_TILE_FOR_PAN)
                continue
            try:
                pan = track.mixer_device.panning
            except (AttributeError, RuntimeError):
                pan = None
            tiles.append(
                EncoderTile(
                    label=compactify(str(track.name or ""), MAXCHARS_ENCODER_LABEL),
                    value=_normalized_value(pan) if pan is not None else 64,
                    assigned=True,
                    value_text=format_parameter_value(pan) if pan is not None else "",
                    show_value=self._showing_value[index],
                )
            )
        focused = self._focused_strip()
        selected = self._strip_track(focused) if focused is not None else None
        return MainContent(
            title="Mix | Pan",
            centre=(
                compactify(str(selected.name or ""), MAXCHARS_CENTRE)
                if _liveobj_valid(selected)
                else "Pan"
            ),
            header_background=live_rgb7(selected) if _liveobj_valid(selected) else None,
            # The centre label marks the focused strip, the same way the header does.
            centre_background=live_rgb7(selected) if _liveobj_valid(selected) else None,
            tiles=tuple(tiles),
            soft_labels=PLUGIN_SOFT_LABELS,
        )

    def _mixer_strip(self, index: int) -> MixerStrip:
        track = self._strip_track(index)
        if not _liveobj_valid(track):
            return MixerStrip(number=str(index + 1))
        try:
            volume_parameter = track.mixer_device.volume
        except (AttributeError, RuntimeError):
            volume_parameter = None
        volume = _normalized_value(volume_parameter) if volume_parameter is not None else 0
        try:
            muted, soloed = bool(track.mute), bool(track.solo)
        except (AttributeError, RuntimeError):
            muted = soloed = False
        left, right, metered = self._track_meters(track)
        return MixerStrip(
            name=compactify(str(track.name or ""), MAXCHARS_MIXER_CHANNEL),
            number=str(index + 1),
            volume=volume,
            muted=muted,
            soloed=soloed,
            colour=live_rgb7(track),
            assigned=True,
            meter_left=left,
            meter_right=right,
            metered=metered,
            # ⚠️ `truncate_value`, never `compactify`. Compactify's first move is to strip
            # hyphens, which turns "-6.0 dB" into "6.0 dB" and silently flips the sign of every
            # attenuation on the mixer. Same rule as the Plugin tiles.
            value_text=(
                truncate_value(
                    format_parameter_value(volume_parameter), MAXCHARS_MIXER_CHANNEL
                )
                if volume_parameter is not None
                else ""
            ),
            # 🔑 **Derived from the touch, not stored.** "Is the finger on the encoder" is
            # exactly the question the reveal asks, so reading `_touch_held` directly means the
            # value cannot get stuck on: there is no flag to clear and no timeout to miss.
            # Deliberately *not* `_showing_value`, which carries Plugin mode's 0.75 s revert —
            # the roadmap's warning about reusing one event source with opposite semantics.
            show_value=self._touch_held[index] if index < len(self._touch_held) else False,
        )

    @staticmethod
    def _track_meters(track):
        """`(left, right, metered)` for one track — Live's own normalised meter values.

        ⚠️ **Meters live on `Track` and nowhere else** — not on `MixerDevice`, not on `Chain`,
        and the framework has no meter support at all to build on. (A grep that appears to find
        `meter_provider` or `meterBank` in the framework is matching inside *para·meter*.)

        `output_meter_left` / `output_meter_right` are the **smoothed momentary peak** pair, and
        the smoothing is Live's — which is why this script contains no ballistics code. A Studio
        Pro capture shows its host decaying a meter for six seconds after a note-off while the
        device just renders the numbers it is handed; we get that decay for free.

        `output_meter_level` (1 s held peak) is deliberately unused: Template 2 has exactly two
        meter elements per strip and they are L and R, so there is nowhere to put a hold marker
        without giving up one channel.

        `has_audio_output` is False for a MIDI track with no instrument — the case that would
        otherwise sit flat at zero for ever and read as broken.
        """
        try:
            metered = bool(track.has_audio_output)
        except (AttributeError, RuntimeError):
            # Older Live, or an object that does not answer: meter it rather than hide it. A
            # meter that should not be there is a smaller wrong than a missing one.
            metered = True
        if not metered:
            return 0.0, 0.0, False
        try:
            return float(track.output_meter_left), float(track.output_meter_right), True
        except (AttributeError, RuntimeError, TypeError, ValueError):
            return 0.0, 0.0, False

    #: Layer key -> the view that draws it. Indexed by `_screen_layer()`, never by a separate
    #: test. Plain functions, not `staticmethod` — a dict value is not a descriptor, so
    #: `self._VIEWS[key]` hands back the function itself and `()` calls it.
    #:
    #: ⚠️ The method is `_screen_layer`, not `_layer`: `Component.__init__` assigns
    #: `self._layer`, and shadowing it fails the build outright (§4, and
    #: `COMPONENT_RESERVED_NAMES` in the suite).
    #: `_CONTENT` below is keyed identically and that is the whole point: two dicts with the
    #: same keys cannot fall out of step the way two ordered `if` chains can.
    _VIEWS = {
        NOTIFICATION_LAYER: runtime.notification_view,
        PLUGIN_MODE: runtime.main_view,
        MIX_MODE: runtime.mixer_view,
        # The pan page borrows Template 0. Two content sources for one view is fine — the
        # view's own `_last` memo diffs against whatever it drew last, and `activate()` is
        # re-run whenever the active view changes, so the chrome is always right.
        MIX_PAN_LAYER: runtime.main_view,
        MIX_SENDS_LAYER: runtime.main_view,
        SONG_MODE: runtime.params_view,
        # ⚠️ Template 1 again — the same template the notification bar uses. They are never both
        # active, and each claims every element on `activate()`, which is what makes the sharing
        # safe. See `menu.py`.
        SCALE_MODE: runtime.menu_view,
    }

    #: Layer key -> the content builder. The notification layer is handled in `_content()`
    #: because its content is a stored object rather than something we build.
    _CONTENT = {
        PLUGIN_MODE: lambda self: self._device_content(),
        MIX_MODE: lambda self: self._mixer_content(),
        MIX_PAN_LAYER: lambda self: self._mixer_pan_content(),
        MIX_SENDS_LAYER: lambda self: self._sends_content(),
        SONG_MODE: lambda self: self._song_content(),
        SCALE_MODE: lambda self: self._scale_content(),
    }

    # -- rendering ---------------------------------------------------------
    def _render(self):
        model = runtime.screen_model()
        view = self._view_for_mode()
        if model is None or view is None:
            return
        # Switching mode switches template. `select_template` is diffed, and each template's
        # elements live in their own cache keys, so flipping back and forth is cheap and does
        # not need a full repaint.
        if view is not self._active_view:
            self._active_view = view
            # 🐛 **Forget, or a shared template strands the incoming view.** `activate()` paints
            # chrome, but row *visibility* is set in `render()` — and `render()` short-circuits
            # when the content is unchanged. So after the notification bar borrowed Template 1
            # and hid the twelve menu rows, returning to the scale menu found identical content,
            # skipped the render, and left the list invisible. Found on hardware 2026-08-03.
            #
            # This is the trap the roadmap already names for `MainView`: *"reset forget() at the
            # same time or the view short-circuits on an unchanged snapshot and nothing is
            # redrawn."* It only became reachable once two views shared a template.
            #
            # Free in practice: the model's diff still sends only what actually differs.
            view.forget()
            view.activate()
        try:
            content = self._content()
        except Exception:
            # A raised exception inside a Live listener can wedge the script; a missed
            # frame is recoverable, a wedged surface is not. But it must be loud.
            logger.exception("Motion32: building screen content failed")
            return
        try:
            changed = view.render(content)
        except Exception:
            logger.exception("Motion32: screen render failed")
            return
        # ALWAYS flush, even when the content snapshot is unchanged.
        #
        # This used to be `if changed:`, which broke returning to a mode: switching away and
        # back leaves the content identical, so `render()` short-circuits — but `activate()`
        # has just queued a *template select* that then never went out, and the device stayed
        # on the other template. Flushing unconditionally also removes a whole class of
        # "forgot to flush" bug; the diff makes it free when there is genuinely nothing to
        # send (a dict scan of ~200 entries, even at the 20 Hz refresh rate).
        del changed
        try:
            model.flush()
        except Exception:
            logger.exception("Motion32: flushing the screen failed")

        # Same reasoning as the unconditional flush: refresh the LEDs on every render rather
        # than only when the view changes. The halos were going dark on a mode switch because
        # the refresh depended on the exact code path taken, and the LED cache makes this free.
        self._refresh_encoder_leds()
        self._refresh_wheel_led()

    def update(self):
        super().update()
        if self.is_enabled():
            self._render()
