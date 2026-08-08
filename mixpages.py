"""The big wheel paging Mix mode between its Volume and Pan pages (Phase 7b).

**Why this is ours and not the framework's.** Nothing in `ableton.v3` switches *modes* from an
encoder. `ModesComponent` offers only `cycle_mode_button` — a button — and `PageComponent` has
`set_scroll_encoder` but pages a `Pageable` (the note-editor abstraction), not a mode set. So the
wheel-to-page link is a small component of ours, the same way `wheel.py` owns the wheel's *push*
because `Device_Navigation` stops at the ends and we wanted wraparound.

**It subclasses `ScrollComponent` rather than reading the encoder directly.** `ScrollComponent`
already decodes a relative encoder into a direction — `scroll_encoder(value, _)` tests `value < 0`
and calls `_do_scroll_up`/`_do_scroll_down` behind `can_scroll_up`/`can_scroll_down` — and it is the
same base `Device_Navigation` uses, so the wheel behaves consistently across modes. Overriding the
four `Scrollable` methods means the injected `scrollable` is never consulted.

⚠️ **The pages wrap** (user decision, 2026-07-30). `can_scroll_up`/`can_scroll_down` are therefore
always true once the pages are bound, and the step arithmetic is modulo the page count — so a third
page (sends) can be added later with no change here.
"""

from __future__ import annotations

import logging

from ableton.v3.control_surface.components import ScrollComponent

logger = logging.getLogger(__name__)


class MotionMixPagesComponent(ScrollComponent):
    """Turns wheel detents into page changes on the `Mix_Pages` modes component."""

    def __init__(self, *a, **k):
        # `ScrollComponent.__init__(self, scrollable, scroll_skin_name)` stores the scrollable
        # and consults it only through `can_scroll_*` / `scroll_*`, all four of which are
        # overridden below. Passing None keeps the required argument satisfied without
        # inventing a second object to hold the state.
        k.setdefault("scrollable", None)
        super().__init__(*a, **k)
        self._pages = None
        #: The Sends component, whose page count is a fact about the set — see `bind_sends`.
        self._sends = None

    #: The mode whose page count is not fixed. Everything else is one wheel step; this one
    #: expands into as many steps as the set has (track pages × send pages).
    EXPANDING_MODE = "sends"

    def bind_pages(self, modes_component) -> None:
        """Take the `Mix_Pages` modes component.

        Late-bound for the same reason as everything else on this surface: modes components are
        created during `ControlSurface.setup()`, after our constructor has run.
        """
        self._pages = modes_component
        if modes_component is None:
            logger.warning("Motion32: no Mix_Pages component; the wheel will not page Mix mode")

    def bind_sends(self, sends_component) -> None:
        """Take the Sends component, whose page count depends on the set.

        🔑 **This is why the wheel cannot simply cycle `modes`.** A `ModesComponent`'s mode list
        is declared in `create_mappings` and is therefore fixed, but the number of Sends pages is
        `ceil(tracks / per_page) × ceil(sends / per_page)` — a fact about the user's set, not
        about the script. So `sends` is **one mode that expands into several wheel steps**, and
        this component is what knows how many.

        The alternative — declaring, say, eight `sends_1..8` modes and hiding the empty ones —
        would put a guess about set size into the mapping table and still be wrong for the ninth.
        """
        self._sends = sends_component

    # -- Scrollable --------------------------------------------------------
    # Always scrollable in both directions: the pages wrap, so there is no end to stop at.
    def can_scroll_up(self) -> bool:
        return self._page_names() is not None

    def can_scroll_down(self) -> bool:
        return self._page_names() is not None

    def scroll_up(self) -> None:
        self._step(-1)

    def scroll_down(self) -> None:
        self._step(1)

    # -- paging ------------------------------------------------------------
    def _page_names(self):
        try:
            names = list(self._pages.modes)
        except (AttributeError, TypeError):
            return None
        return names or None

    def _sends_pages(self) -> int:
        """How many wheel steps the `sends` mode is worth. 0 if the set has no return tracks."""
        if self._sends is None:
            return 0
        try:
            return max(0, int(self._sends.page_count))
        except (AttributeError, TypeError, ValueError):
            return 0

    def _steps(self):
        """The flat sequence of wheel positions: `(mode, sub_page)` pairs.

        Volume and Pan are one step each; `sends` contributes one step per page. A set with no
        returns contributes none, so the wheel simply never lands on a Sends page that has
        nothing to show — which is better than an empty page you have to scroll past.
        """
        names = self._page_names()
        if names is None:
            return []
        steps = []
        for name in names:
            if name == self.EXPANDING_MODE:
                steps.extend((name, page) for page in range(self._sends_pages()))
            else:
                steps.append((name, 0))
        return steps

    def _current_step(self, steps) -> int:
        try:
            mode = self._pages.selected_mode
        except (AttributeError, RuntimeError):
            return 0
        sub_page = 0
        if mode == self.EXPANDING_MODE and self._sends is not None:
            try:
                sub_page = int(self._sends.page)
            except (AttributeError, TypeError, ValueError):
                sub_page = 0
        for index, step in enumerate(steps):
            if step == (mode, sub_page):
                return index
        # The current position is not in the sequence — the set changed under us (a return track
        # added or removed). Land on the first step of the current mode rather than jumping.
        for index, (name, _page) in enumerate(steps):
            if name == mode:
                return index
        return 0

    def _step(self, delta: int) -> None:
        steps = self._steps()
        if not steps:
            return
        index = (self._current_step(steps) + delta) % len(steps)
        mode, sub_page = steps[index]
        try:
            # ⚠️ Order matters. Set the sub-page **first**: selecting the mode grabs the layer,
            # which re-runs `update()` and re-maps the encoders, so the page must already be
            # right or the first frame maps the previous page's parameters.
            if mode == self.EXPANDING_MODE and self._sends is not None:
                self._sends.set_page(sub_page)
            if self._pages.selected_mode != mode:
                self._pages.selected_mode = mode
            elif mode == self.EXPANDING_MODE and self._sends is not None:
                # Same mode, different sub-page: no layer swap happens, so nothing else will
                # ask for a repaint. `set_page` already reported the change.
                pass
        except (AttributeError, ValueError, RuntimeError):
            logger.exception("Motion32: could not page Mix mode")
