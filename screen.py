"""Motion 32 screen address map and factory colour palette.

Pure data — no framework imports, no I/O. Everything here is machine-checkable
against `Motion32_Screen_Template_Map.csv` (433 attribute handlers over 181 unique
`(template, zone, element)` addresses).

**Why addresses are named, not numeric at the call site:** the build rule is *one
owner per screen element*. Callers ask for `main.encoder_label(3)`, never
`(0, 6, 2)`. That makes double-ownership visible in review instead of showing up as
a flickering label on hardware.

Colours are the factory values from `$MOTION32_COLORS_*` / `$MOTIONSHARED_COLORS_*`,
converted to the 7-bit form the wire takes (`v7 = v8 >> 1`).
See Motion32_Screen_Style_Spec.md §3.
"""

from __future__ import annotations

from typing import Tuple

from .palette import rgb7

Address = Tuple[int, int]  # (zone, element) within a template

# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------
TEMPLATE_MAIN = 0
TEMPLATE_MENU = 1
TEMPLATE_MIXER = 2
TEMPLATE_PARAMS = 3

TEMPLATE_NAMES = {
    TEMPLATE_MAIN: "Main",
    TEMPLATE_MENU: "Menu",
    TEMPLATE_MIXER: "Mixer",
    TEMPLATE_PARAMS: "Params",
}


# ---------------------------------------------------------------------------
# Template 0 — Main / Control-Link / plugin view
# ---------------------------------------------------------------------------
class Main:
    """Encoder-tile layout: header (title + 4 labels), 8 tiles, centre text, footer."""

    template = TEMPLATE_MAIN

    BACKGROUND: Address = (0, 0)
    HEADER_BACKGROUND: Address = (1, 0)
    HEADER_TITLE: Address = (1, 5)
    HEADER_DIVIDER: Address = (2, 0)
    CENTRE_BACKGROUND: Address = (7, 0)
    CENTRE_TEXT: Address = (7, 1)
    FOOTER_DIVIDER: Address = (12, 0)
    FOOTER_BACKGROUND: Address = (13, 0)

    # Encoder tiles: top row is zones 3-6, bottom row zones 8-11.
    ENCODER_ZONES = (3, 4, 5, 6, 8, 9, 10, 11)

    # Element indices within an encoder tile.
    _TILE_BACKGROUND = 0
    _TILE_VALUE = 1
    _TILE_LABEL = 2

    @classmethod
    def encoder_background(cls, index: int) -> Address:
        return (cls.ENCODER_ZONES[index], cls._TILE_BACKGROUND)

    @classmethod
    def encoder_value(cls, index: int) -> Address:
        """The halo / fill arc — takes both a value (0-127) and a colour."""
        return (cls.ENCODER_ZONES[index], cls._TILE_VALUE)

    @classmethod
    def encoder_label(cls, index: int) -> Address:
        return (cls.ENCODER_ZONES[index], cls._TILE_LABEL)

    @staticmethod
    def soft_button_label(index: int) -> Address:
        """LCD soft-button labels 0-7.

        The factory splits them **top row 0-3 -> header zone 1, bottom row 4-7 ->
        footer zone 13** (confirmed by skin.xml's LcdButtonTopRow/BottomRow forms).
        Getting this backwards puts the labels on the wrong side of the screen.
        """
        if index < 4:
            return (1, 1 + index)
        return (13, 1 + (index - 4))


# ---------------------------------------------------------------------------
# Template 2 — Mixer (8 channel strips)
# ---------------------------------------------------------------------------
class Mixer:
    template = TEMPLATE_MIXER

    BACKGROUND: Address = (0, 0)

    _STRIP_BACKGROUND = 0
    _STRIP_NUMBER = 1
    _STRIP_FADER = 2
    _STRIP_MUTE = 3
    _STRIP_SOLO = 4
    _STRIP_LABEL_BACKGROUND = 5
    _STRIP_LABEL = 6
    _STRIP_METER_LEFT = 7
    _STRIP_METER_RIGHT = 8

    @staticmethod
    def _zone(strip: int) -> int:
        return 1 + strip  # strips 0-7 -> zones 1-8

    @classmethod
    def background_of(cls, strip: int) -> Address:
        return (cls._zone(strip), cls._STRIP_BACKGROUND)

    @classmethod
    def number(cls, strip: int) -> Address:
        return (cls._zone(strip), cls._STRIP_NUMBER)

    @classmethod
    def fader(cls, strip: int) -> Address:
        return (cls._zone(strip), cls._STRIP_FADER)

    @classmethod
    def mute(cls, strip: int) -> Address:
        return (cls._zone(strip), cls._STRIP_MUTE)

    @classmethod
    def solo(cls, strip: int) -> Address:
        return (cls._zone(strip), cls._STRIP_SOLO)

    @classmethod
    def label_background(cls, strip: int) -> Address:
        """Track-colour swatch behind the channel name."""
        return (cls._zone(strip), cls._STRIP_LABEL_BACKGROUND)

    @classmethod
    def label(cls, strip: int) -> Address:
        return (cls._zone(strip), cls._STRIP_LABEL)

    @classmethod
    def meter_left(cls, strip: int) -> Address:
        return (cls._zone(strip), cls._STRIP_METER_LEFT)

    @classmethod
    def meter_right(cls, strip: int) -> Address:
        return (cls._zone(strip), cls._STRIP_METER_RIGHT)


# ---------------------------------------------------------------------------
# Template 3 — Params (text label + text value tiles)
# ---------------------------------------------------------------------------
class Params:
    """The factory's **Song / Timeline** screen — and ours: this is what Song mode draws.

    Identified from a photograph of Studio Pro and **confirmed on hardware**. Each tile has a
    separate label *and* value element, so a name and its reading are on screen at once — which
    is why Song mode needs no reveal-on-touch, unlike Template 0. The template carries no
    bar/arc `value` attribute anywhere; it is text only.

    (This docstring read "runtime role unconfirmed [INF]" until 2026-08-03. It predates Song
    mode being built on it.)"""

    template = TEMPLATE_PARAMS

    BACKGROUND: Address = (0, 0)
    HEADER_BACKGROUND: Address = (1, 0)
    HEADER_TITLE: Address = (1, 5)
    HEADER_DIVIDER: Address = (2, 0)
    TITLE_BAR_BACKGROUND: Address = (7, 0)
    TITLE_BAR_TEXT: Address = (7, 1)
    FOOTER_DIVIDER: Address = (12, 0)
    FOOTER_BACKGROUND: Address = (13, 0)

    TILE_ZONES = (3, 4, 5, 6, 8, 9, 10, 11)

    @classmethod
    def tile_background(cls, index: int) -> Address:
        return (cls.TILE_ZONES[index], 0)

    @classmethod
    def tile_label(cls, index: int) -> Address:
        return (cls.TILE_ZONES[index], 1)

    @classmethod
    def tile_value(cls, index: int) -> Address:
        return (cls.TILE_ZONES[index], 2)

    @staticmethod
    def soft_button_label(index: int) -> Address:
        if index < 4:
            return (1, 1 + index)
        return (13, 1 + (index - 4))


# ---------------------------------------------------------------------------
# Template 1 — Menu (two columns of six rows)
# ---------------------------------------------------------------------------
class Menu:
    template = TEMPLATE_MENU

    BACKGROUND: Address = (0, 0)
    HEADER_BACKGROUND: Address = (1, 0)
    HEADER_TITLE: Address = (1, 5)
    HEADER_DIVIDER: Address = (2, 0)
    COLUMN_1_BACKGROUND: Address = (3, 0)
    COLUMN_2_BACKGROUND: Address = (4, 0)
    FOOTER_DIVIDER: Address = (5, 0)
    FOOTER_BACKGROUND: Address = (6, 0)

    ROWS_PER_COLUMN = 6

    COLUMNS = 2

    @classmethod
    def row(cls, column: int, row: int) -> Address:
        """column 0 or 1, row 0-5."""
        return (3 + column, 1 + row)

    @classmethod
    def menu_background(cls, column: int) -> Address:
        """The panel behind one column of rows — `MENU_MENU_BACKGROUND[column]`."""
        return (3 + column, 0)

    @staticmethod
    def header_button_label(index: int) -> Address:
        return (1, 1 + index)

    @staticmethod
    def footer_button_label(index: int) -> Address:
        return (6, 1 + index)


# ---------------------------------------------------------------------------
# Palette — factory colours as 7-bit RGB triples
# ---------------------------------------------------------------------------
"""`rgb7` lives in `palette.py`, which is the single conversion layer for screen *and* LEDs
(roadmap Phase 4). It is imported at the top of this module; this note is here because the
function used to be defined at this spot and a future reader may come looking for it."""


class Palette:
    """Factory values. Use these for device chrome; use `rgb7(obj.color)` for
    anything that mirrors a Live object (track/clip/scene colour)."""

    BLACK = rgb7(0x000000)
    WHITE = rgb7(0xFFFFFF)

    # Screen chrome
    SCREEN_BACKGROUND = rgb7(0x000000)
    HEADER_BACKGROUND = rgb7(0x0069CC)
    HEADER_TITLE = rgb7(0xFFFFFF)
    HEADER_TEXT_DEFAULT = rgb7(0xCCCCCC)
    HEADER_TEXT_SELECTED = rgb7(0xFFFFFF)
    FOOTER_BACKGROUND = rgb7(0x000000)
    FOOTER_DIVIDER = rgb7(0x303336)
    FOOTER_TEXT_DEFAULT = rgb7(0xFFFFFF)
    DIVIDER = rgb7(0x303336)

    # Content
    VALUE = rgb7(0xFFFFFF)
    VALUE_TRIGGERED = rgb7(0x0069CC)
    PLUGIN_TITLE = rgb7(0xFFFFFF)
    PLUGIN_TITLE_BACKGROUND = rgb7(0x303336)
    # "Present but unassigned" — the factory greys, it never hides.
    DISABLED = rgb7(0xBBBFC3)
    MENU_TEXT_DEFAULT = rgb7(0xBBBFC3)
    MENU_TEXT_SELECTED = rgb7(0xFFFFFF)

    # Buttons / halos / pads
    BUTTON_DEFAULT = rgb7(0x0069CC)
    BUTTON_SELECTED = rgb7(0xFFFFFF)
    BUTTON_INACTIVE = rgb7(0x1C1C1C)
    KNOB_DEFAULT = rgb7(0x0069CC)
    KNOB_TOUCHED = rgb7(0xFFFFFF)
    # Encoder halo colour per mode. Purple for transport/song is the convention across
    # Ableton controllers; blue matches the factory's own knob colour for plugin parameters.
    # **Mix mode uses no constant from here** — each halo takes its own channel strip's track
    # colour, straight from `live_rgb7`, and falls back to KNOB_PLUGIN only for a track that
    # has no colour of its own. See `screen_component._refresh_encoder_leds`.
    #: A pad while it is held. Green is the factory's played-note colour on this keybed.
    PAD_PLAYED = rgb7(0x00FF00)
    KNOB_SONG = rgb7(0x8A2BE2)
    KNOB_PLUGIN = rgb7(0x0069CC)
    MODIFIER_KEY = rgb7(0xFF00FF)
    RECORD_ACTIVE = rgb7(0xFF0000)
    STOP_ACTIVE = rgb7(0xFFA500)
    CHANNEL_SOLO = rgb7(0xFFFF00)
    CHANNEL_MUTE = rgb7(0xFF0000)
    CHANNEL_LABEL_SELECTED = rgb7(0x0069CC)

    # Mix-mode meters (Phase 7c). Three bands, not a gradient — see `meter_colour()` in
    # display.py for why the quantisation is load-bearing rather than cosmetic.
    METER_LOW = rgb7(0x00CC44)      # green: normal signal
    METER_HIGH = rgb7(0xFFA500)     # amber: approaching the top of Live's scale
    METER_CLIP = rgb7(0xFF0000)     # red: at or over
    # Control-Link scope language: cyan = global assignment, amber = focus assignment.
    CONTROL_LINK_GLOBAL = rgb7(0x4FD3FF)
    CONTROL_LINK_FOCUS = rgb7(0xFCCA03)
    TOUCH_STRIP_PRIMARY = rgb7(0x0069CC)
    TOUCH_STRIP_SECONDARY = rgb7(0xFFA500)


# Font styles ($MOTIONSHARED_FONTSTYLE_*)
FONT_REGULAR = 0
FONT_BOLD = 1
