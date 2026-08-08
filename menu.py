"""The Template 1 list view — a scrollable 2×6 menu with soft-button labels.

Built for Scale mode and deliberately generic, because three other things want it: Chord mode's
progression list, browser navigation, and any future picker. It renders a `MenuContent` and knows
nothing about scales.

**Layout** (user, 2026-08-03), matching the factory's own Scale screen:

```
┌─ Scales ──────────────────────────────┬────────┐
│                                       │ Locked │  ← header title, and ONE toggle top-right
├───────────────────────────────────────┴────────┤
│  Major            Dorian                       │
│  Melodic Minor    Phrygian                     │  ← 2 columns × 6 rows, wheel scrolls
│  Harmonic Minor   Lydian                       │
│  …                                             │
├──────────┬──────────┬──────────┬───────────────┤
│   Main   │  Modes   │          │      Key      │  ← footer: the category buttons
└──────────┴──────────┴──────────┴───────────────┘
```

⚠️ **Template 1 is shared with the notification bar, and that is now real rather than theoretical.**
`notification.py` has owned this template alone since 2026-07-26; the roadmap flagged the collision
in §5.6 — *"it will share Template 1 with the notification bar; ownership has to be settled before
both write it"* — and Scale mode is what settles it.

**How they coexist.** They are two *views*, never both active: `_screen_layer()` returns exactly one
key, and the notification bar outranks whatever mode is showing. Switching between them goes through
`_render`'s `view is not self._active_view` branch, which calls `activate()` — so each one repaints
its **whole** chrome on the way in, and `ScreenModel`'s diff sends only what actually differs. The
bar hides the twelve rows; the menu shows them again a second later.

That works only because of the §6b-25 rule, and this is the second feature to depend on it: **every
view must claim every element on its template.** A menu that left the bar's two header slots alone
would show `Octave` and `+1` sitting in its header after the bar cleared.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Tuple

from . import screen
from .display import ScreenModel
from .formatting import MAXCHARS_MENU_BUTTON
from .palette import text_on

#: Rows visible at once: two columns of six.
MENU_COLUMNS = screen.Menu.COLUMNS
MENU_ROWS = screen.Menu.ROWS_PER_COLUMN
VISIBLE_ROWS = MENU_COLUMNS * MENU_ROWS

#: A menu row is about a third of the screen wide. The element accepts far more, but the factory's
#: own rows ("Harmonic Minor", "I - V - vi - IV") sit around this and longer strings collide with
#: the second column.
MAXCHARS_MENU_ROW = 15


@dataclass(frozen=True)
class MenuContent:
    """One frame of the list. Immutable, so "did anything change?" is `==`, as everywhere else."""

    title: str = ""
    #: Every row in the list, not just the visible twelve — the view does the windowing so the
    #: caller can hold a plain list and an index without tracking a scroll offset as well.
    rows: Tuple[str, ...] = ()
    #: Index into `rows`, or None for a list with nothing chosen.
    selected: Optional[int] = None
    #: Eight labels: 0-3 are the top row (over the screen), 4-7 the bottom row (under it), the
    #: same split `screen.Main.soft_button_label` uses. An empty string leaves that button
    #: unlabelled and dark.
    soft_labels: Tuple[str, ...] = field(default_factory=lambda: ("",) * 8)

    @property
    def window_start(self) -> int:
        """First visible row, so the selection is always on screen.

        Pages rather than scrolls line-by-line: the list jumps a full twelve when the selection
        leaves the window. With sixteen scales that means at most two pages, and a page that
        holds still while you scroll within it is far easier to read than one that creeps.
        """
        if self.selected is None:
            return 0
        return (self.selected // VISIBLE_ROWS) * VISIBLE_ROWS


class MenuView:
    """Renders `MenuContent` onto Template 1.

    Owns, exclusively while it is the active view: the Menu background, header background,
    divider and title, all four header button labels, both column backgrounds, all twelve rows,
    the footer divider/background and all four footer button labels.

    That is **every** element on the template — see the module docstring for why nothing may be
    left out.
    """

    def __init__(self, model: ScreenModel) -> None:
        self._model = model
        self._writer = model.writer(screen.Menu)
        self._last: Optional[MenuContent] = None

    def activate(self) -> None:
        self._model.select_template(screen.Menu.template)
        self.paint_chrome()

    def paint_chrome(self) -> None:
        """The parts that never change. Sent once, then diffed away on every later showing."""
        writer = self._writer
        palette = screen.Palette
        menu = screen.Menu

        writer.color(menu.BACKGROUND, palette.SCREEN_BACKGROUND)
        writer.color(menu.HEADER_BACKGROUND, palette.HEADER_BACKGROUND)
        writer.color(menu.HEADER_DIVIDER, palette.DIVIDER)
        writer.visible(menu.HEADER_DIVIDER, True)

        # ⚠️ The title is *shown* here, where the notification bar explicitly hides it. Both must
        # write it, or whichever ran second would inherit the other's state.
        writer.visible(menu.HEADER_TITLE, True)
        writer.font(menu.HEADER_TITLE, bold=True)
        writer.color(menu.HEADER_TITLE, text_on(palette.HEADER_BACKGROUND))

        for column in range(MENU_COLUMNS):
            writer.color(menu.menu_background(column), palette.SCREEN_BACKGROUND)

        writer.color(menu.FOOTER_DIVIDER, palette.DIVIDER)
        writer.visible(menu.FOOTER_DIVIDER, True)
        writer.color(menu.FOOTER_BACKGROUND, palette.FOOTER_BACKGROUND)

    def render(self, content: MenuContent) -> bool:
        # Same guard as every other view: the content classes share field names, so a view handed
        # the wrong one draws a plausible-but-wrong screen instead of failing.
        if not isinstance(content, MenuContent):
            raise TypeError(f"MenuView renders MenuContent, got {type(content).__name__}")
        if content == self._last:
            return False

        writer = self._writer
        palette = screen.Palette
        menu = screen.Menu

        writer.text(menu.HEADER_TITLE, content.title, MAXCHARS_MENU_BUTTON)

        # Soft-button labels. Top row over the screen, bottom row under it — the labels are
        # anchored over their physical buttons, so an unused slot must be blanked rather than
        # left holding whatever the last view put there.
        for slot in range(4):
            self._write_soft_label(menu.header_button_label(slot), content, slot)
        for slot in range(4):
            self._write_soft_label(menu.footer_button_label(slot), content, slot + 4)

        # The rows, windowed so the selection is always visible.
        start = content.window_start
        for column in range(MENU_COLUMNS):
            for row in range(MENU_ROWS):
                index = start + column * MENU_ROWS + row
                address = menu.row(column, row)
                label = content.rows[index] if index < len(content.rows) else ""
                chosen = content.selected == index and bool(label)
                writer.text(address, label, MAXCHARS_MENU_ROW)
                writer.visible(address, bool(label))
                # The selected row is white and bold; the rest are the factory's menu grey. Both
                # cues together, because on a small screen either alone is easy to miss.
                writer.color(
                    address,
                    palette.MENU_TEXT_SELECTED if chosen else palette.MENU_TEXT_DEFAULT,
                )
                writer.font(address, bold=chosen)

        self._last = content
        return True

    def _write_soft_label(self, address, content: MenuContent, slot: int) -> None:
        label = content.soft_labels[slot] if slot < len(content.soft_labels) else ""
        writer = self._writer
        palette = screen.Palette
        writer.text(address, label, MAXCHARS_MENU_BUTTON)
        writer.visible(address, bool(label))
        writer.color(
            address,
            palette.FOOTER_TEXT_DEFAULT if label else palette.DISABLED,
        )
        writer.font(address, bold=False)

    def forget(self) -> None:
        self._last = None
