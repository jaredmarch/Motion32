"""Scale mode — the state, the soft buttons and the wheel.

The musical engine is `scales.py` (framework-free, exhaustively tested); this is the part that
touches Live and the framework. It owns four facts and nothing else:

* which **category** the list is showing — `Main`, `Modes` or `Key`
* the current **scale** and **root**
* whether the pads are **Locked** or in **Guide**

Everything visible is derived from those. The menu content, the pad layout and the LED roles are
all computed on demand rather than stored, so there is no second copy to drift — the rule that has
now been re-learned three times in this project (`_pad_root_offset`, the Mix focus, the meter
labels).

**The screen, from the factory** (`Motion32_State_Trace_Table.md` §Scale, `[SRC]`: *"wheel selects
scale/key; soft buttons pick Main/Modes/Key + Guide/Lock"*), with the exact arrangement given by
the user 2026-08-03:

```
┌─ Scales ─────────────────────────┬────────┐
│                                  │ Locked │   top-right: ONE toggle, not two buttons
├──────────────────────────────────┴────────┤
│  the current category's list, wheel-scrolled │
├─────────┬─────────┬─────────┬─────────────┤
│  Main   │  Modes  │         │     Key     │
└─────────┴─────────┴─────────┴─────────────┘
```

⚠️ **`Guide` and `Locked` are one control, not two.** They are the two states of the pad layout,
so a single button that *reads out* the current state and toggles it is the honest shape — two
buttons would imply they could both be off. `Locked` is the default.

⚠️ **Writing to Live is guarded by a translation table.** `song.scale_name` takes Live's spelling,
not the Motion's, and an unrecognised name is **silently ignored**. `scales.LIVE_SCALE_NAMES` is
the map, and a scale absent from it (the two triads, which are pad layouts rather than scales) is
deliberately not pushed at all.
"""

from __future__ import annotations

import logging

from ableton.v3.control_surface import Component
from ableton.v3.control_surface.components import ScrollComponent
from ableton.v3.control_surface.controls import ButtonControl

from . import scales

logger = logging.getLogger(__name__)

#: What the header title says.
MENU_TITLE = "Scales"

#: The two faces of the single top-right button.
LABEL_LOCKED = "Locked"
LABEL_GUIDE = "Guide"

# ⚠️ **Scale mode raises no notifications, deliberately** (user, 2026-08-03).
#
# Two reasons, and the second is the stronger one:
#
# 1. **The screen already says it.** The list highlights the selection and the top-right button
#    reads `Locked` or `Guide`. A bar repeating that adds nothing — and scrolling a list is a
#    continuous gesture, so it would fire on every detent.
# 2. 🔑 **The bar and this menu share Template 1.** `notification.py` blanks the twelve rows and
#    writes its two header slots; the menu shows them again. So a notification raised *from* Scale
#    mode would wipe the very list you are scrolling, once per detent. The two views coexist
#    precisely because they are never both wanted at once, and this is the case that proves it.
#
# `keyboard.py` still notifies for Octave and A-H — those have no permanent home on screen, which
# is what the bar is for.


class MotionModeReturnComponent(Component):
    """The **Control** button: leave Scale (or Chord) for whatever mode was showing before.

    ⚠️ **Not a mode button.** Adding Control to the `Main_Modes` radio would make it a *fourth
    destination*, and it has no screen of its own — it is a way *back*. The factory agrees:
    `Motion32_State_Trace_Table.md` §Control describes `kControl0` as *"the neutral 'return to
    underlying control-focus view' state that scale/chord/launcher/velocity collapse to"*. It
    emits nothing itself.

    So this holds one fact — the last non-Scale mode — and restores it. A single value, not a
    stack: two presses of Control should not walk backwards through history, and Scale is the only
    thing it returns *from*, so there is nothing deeper to remember.
    """

    control_button = ButtonControl(color="Scale.Return")

    #: Modes that Control can return *to*. Anything else (Scale itself, and Chord when it lands)
    #: is a mode you leave rather than one you go back to.
    RETURNABLE = ("song", "plugin", "mix")

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self._modes = None
        self._previous = self.RETURNABLE[0]

    def bind_modes(self, modes_component) -> None:
        """Late-bound like everything else: modes exist only after `create_mappings` has run."""
        self._modes = modes_component
        if modes_component is None:
            logger.warning("Motion32: no Main_Modes; the Control button cannot return")

    def remember(self, mode: str) -> None:
        """Told by the screen component on every mode change.

        Only returnable modes are remembered, so pressing Control from Scale goes back to the
        mode you were actually in rather than to Scale itself.
        """
        if mode in self.RETURNABLE:
            self._previous = mode

    @control_button.pressed
    def control_button(self, _button):
        if self._modes is None:
            return
        try:
            if self._modes.selected_mode in self.RETURNABLE:
                # Already in a normal mode — Control has nothing to collapse, so it does nothing
                # rather than jumping somewhere arbitrary.
                return
            self._modes.selected_mode = self._previous
        except (AttributeError, RuntimeError):
            logger.exception("Motion32: could not return to the previous mode")


class MotionScaleComponent(ScrollComponent):
    """Scale mode's state and controls.

    Subclasses `ScrollComponent` for the same reason `mixpages.py` does: it is the framework's own
    decoder from a relative encoder to a direction, and it is what the wheel is already bound to
    in every other mode that uses it. All four `Scrollable` methods are overridden, so the
    injected scrollable is never consulted.

    ⚠️ **The list wraps.** With sixteen entries and a category button a keypress away, stopping at
    the ends would only ever be an obstacle; and wrapping is what the Mix pages already do, so the
    wheel behaves the same everywhere.
    """

    category_main_button = ButtonControl(color="Scale.CategoryOff", on_color="Scale.CategoryOn")
    category_modes_button = ButtonControl(color="Scale.CategoryOff", on_color="Scale.CategoryOn")
    category_key_button = ButtonControl(color="Scale.CategoryOff", on_color="Scale.CategoryOn")
    #: One button, two faces. `is_on` shows Guide; off shows Locked.
    guide_lock_button = ButtonControl(color="Scale.Locked", on_color="Scale.Guide")

    def __init__(self, *a, **k):
        k.setdefault("scrollable", None)
        super().__init__(*a, **k)
        self._category = scales.CATEGORY_MAIN
        self._scale_id = scales.DEFAULT_SCALE_ID
        self._root = 0
        self._locked = True
        self._on_changed = None

    # -- wiring ------------------------------------------------------------
    def set_changed_listener(self, listener) -> None:
        """Called with no arguments whenever anything visible changes."""
        self._on_changed = listener

    # -- state -------------------------------------------------------------
    @property
    def scale_id(self) -> int:
        return self._scale_id

    @property
    def root(self) -> int:
        return self._root

    @property
    def locked(self) -> bool:
        """True for the one-lane scale layout; False for the chromatic Guide layout."""
        return self._locked

    @property
    def category(self) -> str:
        return self._category

    @property
    def scale_label(self) -> str:
        return f"{scales.ROOT_NAMES[self._root % 12]} {scales.scale_name(self._scale_id)}"

    # -- the menu ----------------------------------------------------------
    def rows(self):
        return tuple(label for label, _value in scales.menu_entries(self._category))

    def selected_index(self):
        """Which row is current, derived from the state rather than stored alongside it.

        🔑 There is no `self._selected`. The selection *is* the scale (or the root) — storing an
        index as well would be a second copy of the same fact, and the failure mode is a list
        that highlights one thing while the pads play another.
        """
        entries = scales.menu_entries(self._category)
        wanted = self._root if self._category == scales.CATEGORY_KEY else self._scale_id
        for index, (_label, value) in enumerate(entries):
            if value == wanted:
                return index
        return None

    def soft_labels(self):
        """Eight labels: 0-3 top row, 4-7 bottom row.

        Only the top-**right** slot is used above the screen — the single Guide/Locked toggle —
        and the categories sit underneath, with slot 6 deliberately blank.
        """
        return (
            "", "", "", LABEL_LOCKED if self._locked else LABEL_GUIDE,
            scales.CATEGORY_MAIN, scales.CATEGORY_MODES, "", scales.CATEGORY_KEY,
        )

    # -- controls ----------------------------------------------------------
    @category_main_button.pressed
    def category_main_button(self, _button):
        self._select_category(scales.CATEGORY_MAIN)

    @category_modes_button.pressed
    def category_modes_button(self, _button):
        self._select_category(scales.CATEGORY_MODES)

    @category_key_button.pressed
    def category_key_button(self, _button):
        self._select_category(scales.CATEGORY_KEY)

    @guide_lock_button.pressed
    def guide_lock_button(self, _button):
        self._locked = not self._locked
        self._refresh_leds()
        # No notification: the button's own label already flipped, which is a better answer than
        # a bar that would blank the list underneath it. See the note at the top of this module.
        self._changed()

    def _select_category(self, category: str) -> None:
        """A radio: pressing a category selects it outright, never toggles it off.

        Same reasoning as the mode buttons and the A–H banks — "toggle off" has no well-defined
        destination for a set of three.
        """
        if category == self._category:
            return
        self._category = category
        self._refresh_leds()
        self._changed()

    # -- the wheel ---------------------------------------------------------
    def can_scroll_up(self) -> bool:
        return True

    def can_scroll_down(self) -> bool:
        return True

    def scroll_up(self) -> None:
        self._step(-1)

    def scroll_down(self) -> None:
        self._step(1)

    def _step(self, delta: int) -> None:
        """Move the selection, and apply it immediately.

        No confirm step: the State Trace says *"wheel selects scale/key"*, and on an instrument
        you want to hear the scale as you land on it, not after a second gesture.
        """
        entries = scales.menu_entries(self._category)
        if not entries:
            return
        current = self.selected_index() or 0
        _label, value = entries[(current + delta) % len(entries)]
        if self._category == scales.CATEGORY_KEY:
            self._root = value % 12
        else:
            self._scale_id = value
        self._push_to_live()
        self._changed()

    # -- Live --------------------------------------------------------------
    def _push_to_live(self) -> None:
        """Write the root and scale into the song, so Live's own key follows the Motion.

        The user's decision (2026-08-03) is that the Motion's documentation is the source of truth
        and Live is told about it — not the other way round. Both properties are R/W and
        observable, so Live's scale-aware clips and devices pick this up for free.

        ⚠️ **A name Live does not recognise is ignored in silence**, which is why the write goes
        through `scales.LIVE_SCALE_NAMES` and a scale missing from that map is not pushed at all.
        Pushing a guess would look like it worked.
        """
        song = self._live_song()
        if song is None:
            return
        try:
            song.root_note = self._root % 12
        except (AttributeError, RuntimeError):
            logger.exception("Motion32: could not set the song's root note")
        live_name = scales.LIVE_SCALE_NAMES.get(scales.scale_name(self._scale_id))
        if live_name is None:
            # A pad layout with no counterpart in Live's chooser — the two triads. Leaving the
            # song's scale alone is the honest outcome; the Motion still lays its pads out.
            return
        try:
            song.scale_name = live_name
        except (AttributeError, RuntimeError):
            logger.exception("Motion32: could not set the song's scale name")

    def _live_song(self):
        try:
            return self.song
        except AttributeError:
            return None

    # -- reporting ---------------------------------------------------------
    def _changed(self) -> None:
        if self._on_changed is None:
            return
        try:
            self._on_changed()
        except Exception:
            logger.exception("Motion32: scale-changed listener failed")

    def _refresh_leds(self) -> None:
        """Light the selected category and the Guide/Locked face.

        Every button is written on every change, because the one being turned *off* needs the
        message as much as the one being turned on — the same rule `keyboard._refresh_bank_leds`
        follows for the A–H radio.
        """
        self.category_main_button.is_on = self._category == scales.CATEGORY_MAIN
        self.category_modes_button.is_on = self._category == scales.CATEGORY_MODES
        self.category_key_button.is_on = self._category == scales.CATEGORY_KEY
        self.guide_lock_button.is_on = not self._locked

    def update(self):
        # Layer grabs reset the button elements, so the lit state has to be re-asserted after one
        # or the category silently stops showing — the lesson from `keyboard.update`.
        super().update()
        if self.is_enabled():
            self._refresh_leds()
