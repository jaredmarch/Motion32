"""The transient notification bar — Template 1, borrowed for about a second.

**Reconstructed byte-for-byte from a Studio Pro octave capture (2026-07-26).** Pressing
Octave Up produced this, in order:

```
F0 08 26 21 01 01 01 03 01 F7                    <- (1,1) visible
F0 08 26 21 01 01 02 03 00 F7                    <- (1,2) hidden
F0 08 26 21 01 01 03 03 01 F7                    <- (1,3) visible
F0 08 26 21 01 01 04 03 00 F7                    <- (1,4) hidden
F0 08 26 21 01 01 05 03 00 F7                    <- (1,5) header title hidden
F0 08 26 21 01 01 01 04 01 F7                    <- (1,1) bold
F0 08 26 21 01 01 03 04 01 F7                    <- (1,3) bold
F0 08 26 21 01 01 01 00 4F 63 74 61 76 65 F7     <- (1,1) text "Octave"
F0 08 26 21 01 06 01 03 00 F7 ... 04 03 00 F7    <- all four footer labels hidden
F0 08 26 21 01 05 00 01 00 00 00 F7              <- footer divider blacked out
F0 08 26 21 01 01 03 00 2B 31 F7                 <- (1,3) text "+1"
F0 08 26 20 01 F7                                <- show Template 1
```

…then, ~1 s later, the same elements restored to their defaults and Template 3 repainted in
full before `F0 08 26 20 03`.

So the notification is **not a fifth template**: it is the Menu template with its title,
its footer labels and its footer divider taken away, leaving two bold texts on the header
bar. `screen.Menu` already named every address involved.

### What we do differently, and why

1. **We do not restore Template 1 on the way out, and we do not repaint the base template.**
   Studio Pro's renderer does not diff, so it rebuilds unconditionally. Ours does: the
   overlay's chrome is identical every time, so after the first showing a notification costs
   **two messages** (the value text, and the template select) and dismissing it costs **one**.
   Studio Pro spends about sixty-five.

   This is safe because the device keeps each template's element state independently while a
   different template is displayed — which the mode switch already proves on hardware, since
   Song ↔ Plugin relies on exactly that and never repaints.

2. **We paint the background and header bar explicitly.** The factory leaves both at whatever
   the firmware defaults to. Two extra messages once, and the screen no longer depends on an
   undocumented default.

⚠️ **Never write these addresses from anywhere else.** A future Menu view will own the same
template, and the moment two code paths write one element the cache in `display.ScreenModel`
starts describing a device state that does not exist.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from . import screen
from .display import ScreenModel
from .formatting import MAXCHARS_MENU_BUTTON
from .palette import text_on


@dataclass(frozen=True)
class NotificationContent:
    """One transient message: a label and the value it changed to.

    Deliberately just two fields. Every notification the device shows is of this shape —
    `Octave / +1`, and later `Bank / F`, `Scale / D Dorian`, `Tempo / 128.00` — so callers
    do not get to invent layouts, and the overlay stays one thing that always looks the same.
    """

    title: str = ""
    value: str = ""


class NotificationView:
    """Renders `NotificationContent` onto Template 1.

    Owns, exclusively: the Menu background, header background, all four header button
    labels, the header title, the footer divider and all four footer button labels.
    """

    #: Which header slots carry the two texts. The capture uses 0 and 2, leaving a gap —
    #: that spacing is what makes the bar read as "label … value" rather than as two words.
    TITLE_SLOT = 0
    VALUE_SLOT = 2

    HEADER_SLOTS = 4
    FOOTER_SLOTS = 4
    #: The Menu template's two columns of six rows. **They ship carrying placeholder text.**
    MENU_COLUMNS = 2
    MENU_ROWS = screen.Menu.ROWS_PER_COLUMN

    def __init__(self, model: ScreenModel) -> None:
        self._model = model
        self._writer = model.writer(screen.Menu)
        self._last: Optional[NotificationContent] = None

    def activate(self) -> None:
        self._model.select_template(screen.Menu.template)
        self.paint_chrome()

    def paint_chrome(self) -> None:
        """Strip the Menu template down to a two-field bar.

        Everything here is constant, so it is sent once and diffed away on every later
        showing. That is the whole reason a notification is cheap.
        """
        writer = self._writer
        palette = screen.Palette
        menu = screen.Menu

        writer.color(menu.BACKGROUND, palette.SCREEN_BACKGROUND)
        writer.color(menu.HEADER_BACKGROUND, palette.HEADER_BACKGROUND)

        # The header title element is a *third* text on the same bar. Left visible it would
        # sit alongside ours and make the bar look like a half-drawn menu.
        writer.visible(menu.HEADER_TITLE, False)

        for slot in range(self.HEADER_SLOTS):
            address = menu.header_button_label(slot)
            used = slot in (self.TITLE_SLOT, self.VALUE_SLOT)
            writer.visible(address, used)
            if used:
                writer.font(address, bold=True)
                writer.color(address, text_on(palette.HEADER_BACKGROUND))

        # The footer is chrome for a menu that is not being shown. Hiding the labels leaves
        # the divider hanging as a bright line across an empty screen, so it goes too — the
        # factory blacks it out rather than hiding it, and black on black is invisible either
        # way.
        # 🐛 The twelve menu rows were missed on the first hardware run and the device drew
        # its own placeholders — "MenuItem0" through "MenuItem5", twice — straight through the
        # bar. The firmware ships those strings in the elements, so an element we never write
        # is not blank, it is whatever the factory left there. Nothing about the octave code
        # was wrong; the screen simply had content we had not claimed.
        #
        # This is the general rule for this device, not a one-off: **an unwritten element is
        # not an empty one.** `test_the_bar_claims_every_element_on_its_template` now derives
        # the full element list from `Motion32_Screen_Template_Map.csv` and fails if any of
        # them goes unclaimed, so the next template gets this for free.
        for column in range(self.MENU_COLUMNS):
            writer.color(menu.menu_background(column), palette.SCREEN_BACKGROUND)
            for row in range(self.MENU_ROWS):
                writer.visible(menu.row(column, row), False)

        # The header divider stays as chrome, so the bar reads as a header with an empty body
        # rather than as a floating stripe.
        writer.color(menu.HEADER_DIVIDER, palette.DIVIDER)
        writer.visible(menu.HEADER_DIVIDER, True)

        writer.color(menu.FOOTER_DIVIDER, palette.SCREEN_BACKGROUND)
        writer.color(menu.FOOTER_BACKGROUND, palette.SCREEN_BACKGROUND)
        for slot in range(self.FOOTER_SLOTS):
            writer.visible(menu.footer_button_label(slot), False)

    def render(self, content: NotificationContent) -> bool:
        # Same guard as MainView/ParamsView: the three content types share field names, so a
        # view handed the wrong one draws a plausible-looking wrong screen instead of failing.
        if not isinstance(content, NotificationContent):
            raise TypeError(
                f"NotificationView renders NotificationContent, got {type(content).__name__}"
            )
        if content == self._last:
            return False

        menu = screen.Menu
        self._writer.text(
            menu.header_button_label(self.TITLE_SLOT), content.title, MAXCHARS_MENU_BUTTON
        )
        self._writer.text(
            menu.header_button_label(self.VALUE_SLOT), content.value, MAXCHARS_MENU_BUTTON
        )
        self._last = content
        return True

    def forget(self) -> None:
        self._last = None
