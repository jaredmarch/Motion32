"""Motion 32 screen engine — cached, diffed, one owner per element.

Deliberately free of framework imports so it can be exercised offline (see
`tests/test_screen.py`), which is the only way to check the byte stream without
hardware in front of you.

Design rules, straight out of Motion32_Build_Roadmap.md §0 and §2:

1. **Two maps, not one.** `_desired` is what we want on screen; `_sent` is what the
   device has. `flush()` transmits the difference. This is what makes a redundant
   re-render free, and it is why `invalidate()` works: clearing `_sent` makes the
   next flush re-send everything — exactly what the device needs after a reconnect,
   or after the Global Settings screen closes and wipes its display.
2. **One owner per element.** Writes go through named addresses in `screen.py`.
   Nothing else in the script may emit screen SysEx.
3. **Never write while suspended.** The device asks us to stop (`F0 08 26 22 01`)
   while the user is in Global Settings. `MotionProtocol.send` enforces that too;
   the model additionally records nothing as sent, so the later redraw is complete.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, Iterable, Optional, Sequence, Tuple

from . import midi, screen
from .palette import darken_under_fixed_light_text, text_on
from .formatting import (
    MAXCHARS_ENCODER_LABEL,
    MAXCHARS_HEADER_TITLE,
    MAXCHARS_HEADER_TITLE_WIDE,
    MAXCHARS_MIXER_CHANNEL,
    MAXCHARS_PARAMS_LABEL,
    MAXCHARS_PARAMS_TITLE,
    MAXCHARS_PARAMS_VALUE_LINE,
    MAXCHARS_SOFT_BUTTON,
    to_ascii_bytes,
)

Address = Tuple[int, int]
Key = Tuple[int, int, int, int]  # template, zone, element, attr

# The centre text area is wide; no factory MAXCHARS constant covers it.
MAXCHARS_CENTRE_TEXT = 24


def _clamp7(value: int) -> int:
    return 0 if value < 0 else (127 if value > 127 else int(value))


class ScreenModel:
    """Owns the device's screen state and emits only what changed."""

    #: Flushes of at least this many messages are logged; smaller ones are routine
    #: single-element updates and would drown the log during a live value refresh.
    LOG_FLUSH_THRESHOLD = 10

    def __init__(
        self,
        send: Callable[[Sequence[int]], None],
        log: Optional[Callable[[str], None]] = None,
    ) -> None:
        self._send = send
        self._log = log or (lambda _message: None)
        self._desired: Dict[Key, Tuple[int, ...]] = {}
        self._sent: Dict[Key, Tuple[int, ...]] = {}
        self._desired_template: Optional[int] = None
        self._sent_template: Optional[int] = None
        self._suspended = False

    # -- state -------------------------------------------------------------
    @property
    def suspended(self) -> bool:
        return self._suspended

    def set_suspended(self, suspended: bool) -> None:
        self._suspended = bool(suspended)

    def invalidate(self) -> None:
        """Forget what the device knows; the next flush re-sends everything."""
        self._sent.clear()
        self._sent_template = None

    # -- writes ------------------------------------------------------------
    def select_template(self, template: int) -> None:
        self._desired_template = template

    def _set(self, template: int, address: Address, attr: int, payload: Iterable[int]) -> None:
        zone, element = address
        self._desired[(template, zone, element, attr)] = tuple(payload)

    def text(self, template: int, address: Address, value: str, limit: int) -> None:
        self._set(template, address, midi.ATTR_TEXT, to_ascii_bytes(value, limit))

    def color(self, template: int, address: Address, rgb: Tuple[int, int, int]) -> None:
        self._set(
            template,
            address,
            midi.ATTR_COLOR,
            (_clamp7(rgb[0]), _clamp7(rgb[1]), _clamp7(rgb[2])),
        )

    def value(self, template: int, address: Address, amount: int) -> None:
        self._set(template, address, midi.ATTR_VALUE, (_clamp7(amount),))

    def visible(self, template: int, address: Address, shown: bool) -> None:
        self._set(template, address, midi.ATTR_VISIBLE, (1 if shown else 0,))

    def font(self, template: int, address: Address, bold: bool) -> None:
        self._set(
            template,
            address,
            midi.ATTR_FONT,
            (screen.FONT_BOLD if bold else screen.FONT_REGULAR,),
        )

    def writer(self, template_class) -> "TemplateWriter":
        return TemplateWriter(self, template_class.template)

    # -- transmit ----------------------------------------------------------
    def flush(self) -> int:
        """Send the difference between desired and sent. Returns messages sent."""
        if self._suspended:
            self._log(
                f"Motion32 screen: flush SUPPRESSED (suspended), "
                f"{self.pending_count()} message(s) pending"
            )
            return 0

        count = 0
        if self._desired_template is not None and self._desired_template != self._sent_template:
            self._send(
                midi.MOTION_SYSEX_HEADER
                + (midi.MSG_SCREEN_TEMPLATE, self._desired_template, midi.SYSEX_END)
            )
            self._sent_template = self._desired_template
            count += 1

        for key, payload in self._desired.items():
            if self._sent.get(key) == payload:
                continue
            template, zone, element, attr = key
            self._send(
                midi.MOTION_SYSEX_HEADER
                + (midi.MSG_SCREEN_UPDATE, template, zone, element, attr)
                + payload
                + (midi.SYSEX_END,)
            )
            self._sent[key] = payload
            count += 1
        # Only report substantial repaints. Logging every flush floods Log.txt once the
        # live value refresh is running (20 Hz while an encoder is being turned), and the
        # interesting events are the full redraws, not the single-element updates.
        if count >= self.LOG_FLUSH_THRESHOLD:
            self._log(f"Motion32 screen: flushed {count} message(s)")
        return count

    def reset_to_defaults(self) -> int:
        """Return every element we wrote to the factory's release state, then forget it.

        **Not** "blank it": a MIDI capture of a Studio Pro shutdown shows each element reset
        to *empty text, white, visible, regular font* — a neutral legible state — before the
        native-mode goodbye goes out. Sending black and `visible=0` instead (which is what
        this used to do) leaves the Motion dark after unload, because its own standalone UI
        draws into the same persistent screen elements and inherits hidden/black from us.
        """
        defaults: Dict[Key, Tuple[int, ...]] = {}
        for key in self._desired:
            attr = key[3]
            if attr == midi.ATTR_TEXT:
                defaults[key] = ()
            elif attr == midi.ATTR_VALUE:
                defaults[key] = (midi.RESET_VALUE,)
            elif attr == midi.ATTR_VISIBLE:
                defaults[key] = (midi.RESET_VISIBLE,)
            elif attr == midi.ATTR_COLOR:
                defaults[key] = midi.RESET_COLOR
            elif attr == midi.ATTR_FONT:
                defaults[key] = (midi.RESET_FONT,)
            else:
                defaults[key] = (0,)

        self._desired = defaults
        self._sent.clear()
        sent = self.flush()
        self._desired.clear()
        self._sent.clear()
        self._sent_template = None
        self._desired_template = None
        return sent

    # -- introspection (tests + logging) ----------------------------------
    def pending_count(self) -> int:
        return sum(1 for key, payload in self._desired.items() if self._sent.get(key) != payload)


@dataclass
class TemplateWriter:
    """A ScreenModel bound to one template, so callers never pass template ids."""

    model: ScreenModel
    template: int

    def text(self, address: Address, value: str, limit: int) -> None:
        self.model.text(self.template, address, value, limit)

    def color(self, address: Address, rgb: Tuple[int, int, int]) -> None:
        self.model.color(self.template, address, rgb)

    def value(self, address: Address, amount: int) -> None:
        self.model.value(self.template, address, amount)

    def visible(self, address: Address, shown: bool) -> None:
        self.model.visible(self.template, address, shown)

    def font(self, address: Address, bold: bool) -> None:
        self.model.font(self.template, address, bold)


# ---------------------------------------------------------------------------
# Content snapshots — immutable, so "did anything actually change?" is just ==
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class EncoderTile:
    label: str = ""
    value: int = 0  # 0-127, already scaled
    assigned: bool = False
    #: Transient value text, shown *instead of* the label while the encoder is touched
    #: or turning. Template 0's tile has only ONE text element (element 2), so name and
    #: value share it — which is exactly how the factory behaves: the label reads as the
    #: parameter name until you touch the encoder, then as the value, then reverts.
    value_text: str = ""
    show_value: bool = False

    @property
    def text(self) -> str:
        if self.show_value and self.value_text:
            return self.value_text
        return self.label


EMPTY_TILE = EncoderTile()


@dataclass(frozen=True)
class MainContent:
    title: str = ""
    centre: str = ""
    # The header carries the focused track's **real** colour when there is one. `None` means
    # "no track / no colour" and falls back to the factory blue. Part of the content snapshot
    # so the diff picks up a recolour like any other change.
    header_background: Optional[Tuple[int, int, int]] = None
    #: The centre strip's background. `None` keeps the factory grey, which is what Plugin mode
    #: wants for a bank name. Mix's Pan page passes the **selected track's** colour so the
    #: centre label marks the focus the same way the header does.
    centre_background: Optional[Tuple[int, int, int]] = None
    tiles: Tuple[EncoderTile, ...] = field(default_factory=lambda: (EMPTY_TILE,) * 8)
    soft_labels: Tuple[str, ...] = field(default_factory=lambda: ("",) * 8)


class MainView:
    """Renders `MainContent` onto Template 0.

    Owns, exclusively: the header background/title/divider, the 8 encoder tiles
    (background, halo, label), the centre text area, the footer, and the 8 soft
    button labels. Nothing else may write those addresses.
    """

    ENCODER_COUNT = 8
    SOFT_BUTTON_COUNT = 8

    def __init__(self, model: ScreenModel) -> None:
        self._model = model
        self._writer = model.writer(screen.Main)
        self._last: Optional[MainContent] = None

    def activate(self) -> None:
        """Select the template and paint the static chrome."""
        self._model.select_template(screen.Main.template)
        self.paint_chrome()

    def paint_chrome(self) -> None:
        writer = self._writer
        palette = screen.Palette
        main = screen.Main

        writer.color(main.BACKGROUND, palette.SCREEN_BACKGROUND)
        # HEADER_BACKGROUND is NOT painted here: it follows the focused track's colour, so
        # `render()` owns it. Two code paths to one element is what the one-owner rule forbids,
        # and they would fight on every mode switch.
        writer.color(main.HEADER_DIVIDER, palette.DIVIDER)
        writer.visible(main.HEADER_DIVIDER, True)
        # CENTRE_BACKGROUND is NOT painted here either: Mix's Pan page colours it from the
        # selected track, so `render()` owns it. Same one-owner reason as HEADER_BACKGROUND.
        writer.color(main.FOOTER_DIVIDER, palette.DIVIDER)
        writer.color(main.FOOTER_BACKGROUND, palette.FOOTER_BACKGROUND)

        for index in range(self.ENCODER_COUNT):
            writer.color(main.encoder_background(index), palette.SCREEN_BACKGROUND)

        # HEADER_TITLE's *colour* is owned by render() too — it has to contrast with whatever
        # the header background turns out to be. Font and visibility are genuinely static.
        writer.font(main.HEADER_TITLE, bold=True)
        writer.visible(main.HEADER_TITLE, True)

    def render(self, content: MainContent) -> bool:
        """Write `content` into the desired state. Returns True if it differed.

        Does not transmit — the caller flushes, so a burst of changes becomes one
        batch on the wire.
        """
        # See ParamsView.render — the two content types share field names and are NOT
        # interchangeable, so a mismatch must fail loudly rather than draw a wrong screen.
        if not isinstance(content, MainContent):
            raise TypeError(f"MainView renders MainContent, got {type(content).__name__}")
        if content == self._last:
            return False

        writer = self._writer
        palette = screen.Palette
        main = screen.Main

        # Header: the focused track's own colour, falling back to the factory blue when there
        # is no track or it has no colour. The title colour is derived from it so a pale track
        # stays readable — see palette.text_on().
        header_background = content.header_background or palette.HEADER_BACKGROUND
        writer.color(main.HEADER_BACKGROUND, header_background)
        writer.text(main.HEADER_TITLE, content.title, MAXCHARS_HEADER_TITLE_WIDE)
        writer.color(main.HEADER_TITLE, text_on(header_background))

        # Centre strip. Grey by default — the treatment Template 3 gives its title bar, and
        # what a bank name wants — but the Pan page passes the selected track's colour so the
        # centre label marks the focus like the header does. Text contrast is derived, because
        # Live's track colours include pale ones.
        centre_background = content.centre_background or palette.PLUGIN_TITLE_BACKGROUND
        writer.color(main.CENTRE_BACKGROUND, centre_background)
        writer.text(main.CENTRE_TEXT, content.centre, MAXCHARS_CENTRE_TEXT)
        writer.color(
            main.CENTRE_TEXT,
            text_on(centre_background)
            if content.centre_background
            else palette.HEADER_TEXT_DEFAULT,
        )
        writer.visible(main.CENTRE_TEXT, bool(content.centre))

        for index in range(self.ENCODER_COUNT):
            tile = content.tiles[index] if index < len(content.tiles) else EMPTY_TILE
            label_address = main.encoder_label(index)
            value_address = main.encoder_value(index)

            # One text element per tile, carrying the name or the transient value.
            writer.text(label_address, tile.text, MAXCHARS_ENCODER_LABEL)
            if not tile.assigned:
                # The factory greys an unassigned slot rather than hiding it.
                writer.color(label_address, palette.DISABLED)
            elif tile.show_value:
                # Blue while the value is live, matching PARAMS_VALUE_TRIGGERED.
                writer.color(label_address, palette.VALUE_TRIGGERED)
            else:
                writer.color(label_address, palette.VALUE)
            writer.visible(label_address, True)

            writer.value(value_address, tile.value)
            writer.color(
                value_address,
                palette.KNOB_DEFAULT if tile.assigned else palette.BUTTON_INACTIVE,
            )
            writer.visible(value_address, tile.assigned)

        for index in range(self.SOFT_BUTTON_COUNT):
            label = content.soft_labels[index] if index < len(content.soft_labels) else ""
            address = main.soft_button_label(index)
            writer.text(address, label, MAXCHARS_SOFT_BUTTON)
            writer.color(address, palette.FOOTER_TEXT_DEFAULT if label else palette.DISABLED)
            writer.visible(address, True)
            writer.font(address, bold=False)

        self._last = content
        return True

    def forget(self) -> None:
        """Drop the content memo so the next render rewrites everything.

        Call alongside `ScreenModel.invalidate()`. Without it, a render identical to
        the last one would short-circuit and leave the device's screen blank.
        """
        self._last = None


# ---------------------------------------------------------------------------
# Template 2 — Mixer (eight channel strips)
# ---------------------------------------------------------------------------
#: Where the meter changes colour, on Live's **normalised** 0.0-1.0 meter value.
#:
#: ⚠️ **These two numbers are inferred and have not been checked against hardware.** Live's
#: `output_meter_left` is its own normalised *display* value, not dB and not linear amplitude —
#: the scale is the one Live draws in its own mixer, which is expanded near the top. 0.76 and
#: 0.92 are where amber and red sit on that drawing, read off Live's meter rather than computed.
#: The check is in `README.md`: play a signal, compare the Motion's band changes with where
#: Live's own meter turns yellow and red, and move these if they disagree. They are two named
#: constants precisely so that is a one-line change.
METER_AMBER_AT = 0.76
METER_RED_AT = 0.92


def meter_colour(level: float) -> Tuple[int, int, int]:
    """Green / amber / red for a normalised meter level.

    🔑 **Three bands, not a gradient, and the quantisation is a traffic decision.** A screen
    element takes one colour and one value, so a continuously-varying colour would have to be
    re-sent every frame — **doubling** the meter traffic, from the factory's 160 messages a
    second to 320, on a wire this feature shares with every encoder and pad event.

    Quantising means the colour only reaches `ScreenModel._desired` as a *different* payload
    when a level crosses a threshold, so the existing desired/sent diff drops it on almost
    every frame. A signal sitting steady in the green costs **zero** colour messages; a
    transient crossing into red costs one, once, per meter.

    (A screen colour is a single SysEx carrying R G B as payload — not three messages, which is
    the LED model. Worth stating because the two are easy to conflate and the arithmetic above
    was wrong in the first draft by exactly that factor.)

    So: do not "improve" this into a smooth ramp. The bands are not a simplification of a
    gradient, they are what keeps the feature within the factory's own budget.
    """
    if level >= METER_RED_AT:
        return screen.Palette.METER_CLIP
    if level >= METER_AMBER_AT:
        return screen.Palette.METER_HIGH
    return screen.Palette.METER_LOW


@dataclass(frozen=True)
class MixerStrip:
    """One channel strip on Template 2.

    `volume`, `mute`, `solo` and the two meters are **`value`** attributes, not colours — the
    firmware draws the fader fill, the two indicators and the meter bars itself from a 0-127
    number. That is different from every other template we render, where state is carried by
    colour.
    """

    name: str = ""
    number: str = ""
    #: 0-127, the fader fill. Live's `mixer_device.volume.value` is 0.0-1.0.
    volume: int = 0
    muted: bool = False
    soloed: bool = False
    #: The track's own colour, behind the name. `None` falls back to the factory grey.
    colour: Optional[Tuple[int, int, int]] = None
    #: False for a strip with no track behind it — greyed, not hidden (the factory never hides).
    assigned: bool = False
    #: Live's normalised `output_meter_left` / `output_meter_right`, 0.0-1.0. **Already
    #: smoothed by Live**, so there is no ballistics code anywhere in this script: a Studio Pro
    #: capture shows the host doing the decay (six seconds of it after a note-off) and the
    #: device rendering whatever number it is handed.
    meter_left: float = 0.0
    meter_right: float = 0.0
    #: False for a track that **cannot** produce audio — a MIDI track with no instrument, which
    #: reads 0.0 forever. Its meters are hidden rather than drawn flat, because a dead meter is
    #: indistinguishable from a broken one. From `Track.has_audio_output`.
    metered: bool = False
    #: The volume reading, shown **in place of the name** while the encoder is touched. Same
    #: shape as `EncoderTile`, and for the same reason: one text element, two things to say.
    value_text: str = ""
    show_value: bool = False

    @property
    def text(self) -> str:
        """What `MIXER_CHANNEL_LABEL` actually carries — the value if revealed, else the name.

        ⚠️ **The reveal ends on release, not on a timeout** (user, 2026-08-03), which is the
        opposite of Plugin mode and of the Pan page. Both of those revert after the framework's
        `ACTIVE_PARAMETER_TIMEOUT`, because there the value is uncovered by a *touch* that may
        not be followed by a turn and the user wants a moment to read it. Here the fader is on
        screen permanently, so the number is a precision aid while your finger is on the
        control and nothing more — leaving it up after release would just hide the track name
        for no reason.

        That difference is why this is driven by `_touch_held` rather than by `_showing_value`:
        "is the finger down" is exactly the question, and a derived answer cannot get stuck.
        """
        if self.show_value and self.value_text:
            return self.value_text
        return self.name


EMPTY_STRIP = MixerStrip()


@dataclass(frozen=True)
class MixerContent:
    strips: Tuple[MixerStrip, ...] = field(default_factory=lambda: (EMPTY_STRIP,) * 8)
    #: Which strip has focus, or None. Cap-touch sets this (Phase 7's focus model); it is in
    #: the content snapshot so a focus change diffs like any other change.
    focused: Optional[int] = None


class MixerView:
    """Renders `MixerContent` onto Template 2.

    Template 2 is **pure strips** — zone 0 is the background and zones 1-8 are the eight
    channels, nine elements each. Notably it has **no header or title zone at all**, unlike
    Templates 0, 1 and 3, so there is nowhere to put a mode name or a global readout. Each
    strip carries its own label instead.

    ⚠️ **There is no pan element.** The strip is number / fader / mute / solo / label / two
    meters, and that is the whole vocabulary. Pan can be bound to an encoder, but it cannot be
    *shown* here — anything that needs a second per-strip readout has to share the fader or go
    on the notification bar.

    ⚠️ **`MIXER_CHANNEL_LABEL` has `text` but no `visible`.** It cannot be hidden, so it must
    always be given a string — an empty one for an unassigned strip. Every other text element
    on this device can be hidden; this one is the exception, and leaving it unwritten is the
    §6b-25 failure (the firmware's own placeholder shows through).
    """

    STRIP_COUNT = 8

    #: Value written to a `value` element to mean "off" / empty.
    VALUE_OFF = 0
    VALUE_ON = 127

    def __init__(self, model: ScreenModel) -> None:
        self._model = model
        self._writer = model.writer(screen.Mixer)
        self._last: Optional[MixerContent] = None

    def activate(self) -> None:
        self._model.select_template(screen.Mixer.template)
        self.paint_chrome()

    def paint_chrome(self) -> None:
        """Everything on this template that never changes — sent once, then diffed away.

        ⚠️ **The meters are NOT painted here.** They were, while they were deferred: claimed
        and hidden, because an element nobody writes shows whatever the firmware shipped in it
        (§6b-25). Now that `render()` drives them (Phase 7c, 2026-08-03) they belong to
        `render()` **alone** — two code paths writing one element is the one-owner rule, and
        here it would have been a real fight rather than a theoretical one: chrome runs on
        every `activate()` and would have re-hidden a live meter on every mode switch.
        """
        writer = self._writer
        palette = screen.Palette
        mixer = screen.Mixer

        writer.color(mixer.BACKGROUND, palette.SCREEN_BACKGROUND)

        for strip in range(self.STRIP_COUNT):
            writer.color(mixer.background_of(strip), palette.SCREEN_BACKGROUND)

    def render(self, content: MixerContent) -> bool:
        # Same guard as the other two views: several content classes share field names, so a
        # view handed the wrong one draws a plausible-but-wrong screen instead of failing.
        if not isinstance(content, MixerContent):
            raise TypeError(f"MixerView renders MixerContent, got {type(content).__name__}")
        if content == self._last:
            return False

        writer = self._writer
        palette = screen.Palette
        mixer = screen.Mixer

        for index in range(self.STRIP_COUNT):
            strip = content.strips[index] if index < len(content.strips) else EMPTY_STRIP
            focused = content.focused == index

            number_address = mixer.number(index)
            writer.text(number_address, strip.number, MAXCHARS_MIXER_CHANNEL)
            writer.visible(number_address, bool(strip.number))

            # The fader, mute and solo are `value` elements: the firmware draws them from a
            # number. An unassigned strip reads empty rather than being hidden.
            writer.value(mixer.fader(index), strip.volume if strip.assigned else self.VALUE_OFF)
            writer.visible(mixer.fader(index), True)

            writer.value(mixer.mute(index), self.VALUE_ON if strip.muted else self.VALUE_OFF)
            writer.visible(mixer.mute(index), strip.assigned)
            writer.value(mixer.solo(index), self.VALUE_ON if strip.soloed else self.VALUE_OFF)
            writer.visible(mixer.solo(index), strip.assigned)

            # The name sits on the track's own colour, with the text flipped for contrast —
            # Live's track colours include pale ones. The **focused** strip is marked by
            # brightening its swatch to the factory selection blue, which is the one thing on
            # this template that can carry focus: there is no ring and no header.
            if focused:
                background = palette.CHANNEL_LABEL_SELECTED
            elif strip.assigned:
                background = strip.colour or palette.PLUGIN_TITLE_BACKGROUND
            else:
                background = palette.SCREEN_BACKGROUND
            # ⚠️ **The label's text colour is not ours to set.** `MIXER_CHANNEL_LABEL` has
            # `text` and nothing else — no `color` — so the firmware draws it light and
            # `text_on()` has nowhere to write. A white or pale track rendered
            # white-on-white. Darkening the swatch is the only lever, and it keeps the hue.
            background = darken_under_fixed_light_text(background)
            writer.color(mixer.label_background(index), background)

            # ⚠️ No `visible` on this element — it does not have the attribute. An unassigned
            # strip gets an empty string, which is how it is blanked.
            #
            # `strip.text` is the name at rest and the volume reading while the encoder is
            # touched. Template 2 gives one text element per strip, so the two share it — the
            # same constraint that forces reveal-on-touch on Template 0, reached from the
            # opposite direction: there the value is the point and the name is the fallback.
            writer.text(mixer.label(index), strip.text, MAXCHARS_MIXER_CHANNEL)

            self._render_meters(index, strip)

        self._last = content
        return True

    def _render_meters(self, index: int, strip: MixerStrip) -> None:
        """The two meter bars — the one polled thing on this surface.

        Shown only for a strip whose track **can** produce audio. A MIDI track with no
        instrument reads 0.0 for ever, and eight strips where three sit permanently flat reads
        as a bug rather than as silence, so those two elements are hidden outright — the CSV
        carries `METER_LEFT_VISIBLE` / `METER_RIGHT_VISIBLE` precisely so a strip can render
        with no meter at all.

        The colour is written on **every** call and that is deliberate: `meter_colour()` returns
        one of three constants, so an unchanged band produces an identical payload and
        `ScreenModel.flush()` drops it. Writing it unconditionally and letting the diff decide
        is the same rule as the unconditional flush in `screen_component._render` — cheaper to
        reason about than a "has the band changed?" flag, and free because the diff already
        exists. See `meter_colour()` for the arithmetic that makes it matter.
        """
        writer = self._writer
        mixer = screen.Mixer
        shown = strip.assigned and strip.metered

        for address, level in (
            (mixer.meter_left(index), strip.meter_left),
            (mixer.meter_right(index), strip.meter_right),
        ):
            writer.visible(address, shown)
            if not shown:
                # Zeroed as well as hidden: an element we stop driving must not keep its last
                # value, or unhiding it later flashes a stale bar for one frame.
                writer.value(address, self.VALUE_OFF)
                continue
            writer.value(address, _clamp7(int(round(level * 127))))
            writer.color(address, meter_colour(level))

    def forget(self) -> None:
        self._last = None


# ---------------------------------------------------------------------------
# Template 3 — Params (label + value tiles), the Song mode screen
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class ParamsTile:
    """One tile on Template 3. Label and value are *separate* screen elements."""

    label: str = ""
    value: str = ""
    assigned: bool = True


EMPTY_PARAMS_TILE = ParamsTile(assigned=False)


@dataclass(frozen=True)
class ParamsContent:
    title: str = ""
    centre: str = ""
    # The centre bar carries the selected track's **real** colour when there is one. `None`
    # means "no track / no colour" and falls back to the factory grey. Part of the content
    # snapshot so the diff picks up a recolour like any other change.
    centre_background: Optional[Tuple[int, int, int]] = None
    tiles: Tuple[ParamsTile, ...] = field(default_factory=lambda: (EMPTY_PARAMS_TILE,) * 8)
    soft_labels: Tuple[str, ...] = field(default_factory=lambda: ("",) * 8)


class ParamsView:
    """Renders `ParamsContent` onto Template 3.

    Template 3 is the factory's **Song / Timeline** screen — identified from a photograph of
    Studio Pro: blue header title, grey centre bar, eight two-line tiles. Its advantage over
    Template 0 is that each tile has an independent **label** and **value** element, so a name
    and its reading are visible at once. Template 0 has a single text element per tile, which
    is what forced the reveal-on-touch behaviour there.

    Template 3 has no `value` (bar/arc) attribute anywhere — it is text only, which suits
    tempo/position/loop readouts where a numeric is more use than a fill.
    """

    TILE_COUNT = 8
    SOFT_BUTTON_COUNT = 8

    def __init__(self, model: ScreenModel) -> None:
        self._model = model
        self._writer = model.writer(screen.Params)
        self._last: Optional[ParamsContent] = None

    def activate(self) -> None:
        self._model.select_template(screen.Params.template)
        self.paint_chrome()

    def paint_chrome(self) -> None:
        writer = self._writer
        palette = screen.Palette
        params = screen.Params

        writer.color(params.BACKGROUND, palette.SCREEN_BACKGROUND)
        writer.color(params.HEADER_BACKGROUND, palette.HEADER_BACKGROUND)
        writer.color(params.HEADER_DIVIDER, palette.DIVIDER)
        writer.visible(params.HEADER_DIVIDER, True)
        writer.color(params.FOOTER_DIVIDER, palette.DIVIDER)
        writer.color(params.FOOTER_BACKGROUND, palette.FOOTER_BACKGROUND)

        # The centre bar's background is NOT painted here: it follows the selected track's
        # colour, so `render()` owns it. Writing it from both places would be two code paths
        # to one element — the exact thing the one-owner rule forbids.

        writer.color(params.HEADER_TITLE, palette.HEADER_TITLE)
        writer.font(params.HEADER_TITLE, bold=True)
        writer.visible(params.HEADER_TITLE, True)

        for index in range(self.TILE_COUNT):
            writer.color(params.tile_background(index), palette.SCREEN_BACKGROUND)
            writer.visible(params.tile_background(index), True)

    def render(self, content: ParamsContent) -> bool:
        # Reject the other template's content outright. `MainContent` and `ParamsContent`
        # share several field names, so a view handed the wrong one renders a plausible-looking
        # but wrong screen instead of failing — which is exactly what happened when the mode
        # predicate and the view predicate disagreed during setup.
        if not isinstance(content, ParamsContent):
            raise TypeError(
                f"ParamsView renders ParamsContent, got {type(content).__name__}"
            )
        if content == self._last:
            return False

        writer = self._writer
        palette = screen.Palette
        params = screen.Params

        writer.text(params.HEADER_TITLE, content.title, MAXCHARS_HEADER_TITLE)

        # Centre bar: the selected track's own colour, falling back to the factory grey when
        # there is no track or it has no colour. Text colour is derived from the background so
        # a pale track stays readable — see palette.text_on().
        centre_background = content.centre_background or palette.PLUGIN_TITLE_BACKGROUND
        writer.color(params.TITLE_BAR_BACKGROUND, centre_background)
        writer.text(params.TITLE_BAR_TEXT, content.centre, MAXCHARS_PARAMS_TITLE)
        writer.color(params.TITLE_BAR_TEXT, text_on(centre_background))
        writer.visible(params.TITLE_BAR_TEXT, bool(content.centre))

        for index in range(self.TILE_COUNT):
            tile = content.tiles[index] if index < len(content.tiles) else EMPTY_PARAMS_TILE
            label_address = params.tile_label(index)
            value_address = params.tile_value(index)

            writer.text(label_address, tile.label, MAXCHARS_PARAMS_LABEL)
            writer.color(label_address, palette.VALUE if tile.assigned else palette.DISABLED)
            writer.visible(label_address, True)

            # No `font` here: Template 3's label/value elements do not accept it.
            writer.text(value_address, tile.value, MAXCHARS_PARAMS_VALUE_LINE)
            writer.color(
                value_address, palette.VALUE_TRIGGERED if tile.value else palette.DISABLED
            )
            writer.visible(value_address, True)

        for index in range(self.SOFT_BUTTON_COUNT):
            label = content.soft_labels[index] if index < len(content.soft_labels) else ""
            address = params.soft_button_label(index)
            writer.text(address, label, MAXCHARS_SOFT_BUTTON)
            writer.color(address, palette.FOOTER_TEXT_DEFAULT if label else palette.DISABLED)
            writer.visible(address, True)

        self._last = content
        return True

    def forget(self) -> None:
        self._last = None
