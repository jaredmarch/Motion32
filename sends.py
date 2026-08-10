"""Mix mode's **Sends** page — the eight encoders as a (track × send) grid.

**The layout** (user, 2026-08-03): *"encoder 1 and encoder 5 are assigned to send A and B for
track 1"*. The encoders are physically two rows of four, so:

```
        track 1   track 2   track 3   track 4
send A    enc 1     enc 2     enc 3     enc 4     ← top row
send B    enc 5     enc 6     enc 7     enc 8     ← bottom row
```

**Columns are tracks, rows are sends**, and that meaning never changes — which is what makes the
page learnable. Track order is preserved left to right exactly as the strips show it on the Volume
page, so a column is in the same place on both.

🔑 **The page count is derived from the set, not declared**, and **no encoder is ever dead.**
Sends are taken in pairs — two rows of encoders — with a leftover odd send getting a page of its
own at one row of eight tracks. `_page_table()` is the whole rule.

| Returns | Pages | Shape |
|---|---|---|
| 1 | 1 | one row of 8 tracks |
| 2 | 2 | 4 tracks × 2 sends, twice |
| 3 | 3 | two as above, then one row of 8 on send C |
| 4 | 4 | 4 tracks × 2 sends, four times |

⚠️ The obvious arithmetic — `2 × ceil(S / 2)` pages of four tracks — is what this replaces. It
left the bottom row unmapped on the last two pages of every **odd** send count: eight dead
encoders in an ordinary three-return set, and a page that reads as broken rather than as
half-empty. Corrected 2026-08-03 before it ever reached hardware.

⚠️ **This is not `MixerComponent.set_send_controls`, and the reason is the layout.** The framework
does support a 2D send matrix — `controls[strip, send]`, columns strips and rows sends, exactly
this shape — and it drives `SendIndexControlComponent` to page through send *banks*. What it
cannot do is page through **tracks**: `set_send_controls` maps `controls[x]` onto
`_channel_strips[x]`, so a four-wide matrix reaches strips 0-3 and nothing else. Half the ring
would be unreachable without also moving the session ring, which Left/Right already owns for a
different purpose.

So the *mapping* is still the framework's — `MappedControl.mapped_parameter` is what
`channel_strip._connect_send_parameters` uses, and it maps engine-side with no Python in the value
path. Only the **choice of which parameter goes on which encoder** is ours.
"""

from __future__ import annotations

import logging

from ableton.v3.base import listens
from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import MappedControl, control_list

logger = logging.getLogger(__name__)

#: The eight encoders.
ENCODER_COUNT = 8

#: How many sends can be shown at once — the two physical rows of encoders.
MAX_SENDS_PER_PAGE = 2

#: How many strips the session ring holds, and therefore how many tracks a Sends page walks.
RING_TRACKS = 8

#: Send letters, matching Live's own naming of the return tracks.
#:
#: **Twelve, not eight.** The shipped v3 `ChannelStripComponent` allocates twelve send controls,
#: so a set with nine returns is an ordinary configuration rather than an edge case.
SEND_LETTERS = "ABCDEFGHIJKL"


def send_label(index: int) -> str:
    """The name of send `index` — `"A"`…`"L"`, then a plain number.

    🔑 **One helper, because the two callers disagreed.** `slot_label` guarded the lookup and fell
    back to a number; `page_label` indexed `SEND_LETTERS` raw. A set with nine returns therefore
    labelled its tiles correctly and raised `IndexError` building the page title — and because the
    screen layer catches that further up, the symptom was not an error but a page that quietly
    stopped updating and left stale text on the device. Two copies of one rule will eventually
    disagree; this is that same lesson as `page_table`.

    **No index can raise.** Beyond L the label is the 1-based number, which is unambiguous and
    keeps the failure mode "unfamiliar label" rather than "dead page".

    ⚠️ **Module level and self-contained on purpose**, exactly like `page_table` and `page_slots`:
    `sends.py` imports the framework, so the offline suite cannot import it, but it *can* lift a
    top-level function out of the AST and execute it. A guard that re-implemented this rule would
    test its own arithmetic and nothing else.
    """
    if 0 <= index < len(SEND_LETTERS):
        return SEND_LETTERS[index]
    return str(index + 1)


def page_table(send_count: int):
    """Every page as `(first_track, first_send, rows)`. **The one source of the geometry.**

    Sends are taken in **pairs**, because there are two rows of encoders — and a leftover odd
    send gets a page of its **own** with a single row of eight tracks.

    🔑 **That last rule is why no encoder is ever dead** (user, 2026-08-03). The obvious
    arithmetic — `2 × ceil(sends / 2)` pages of four tracks — leaves the bottom row unmapped on
    the last two pages of every *odd* send count, which is eight dead encoders in a perfectly
    ordinary three-return set:

        3 sends, before:  1C 2C 3C 4C | -- -- -- --      (and again for tracks 5-8)
        3 sends, after:   1C 2C 3C 4C | 5C 6C 7C 8C

    The invariant survives intact: a column is still a track and a row is still a send. That page
    simply has one row — exactly what a set with a single return already looked like.

    Track groups advance **within** a send group, so the wheel walks the whole mix on sends A/B
    before moving to C/D. That keeps one pass over the mix together rather than interleaving it
    with a change of send.

    ⚠️ **Module level and self-contained on purpose.** `sends.py` imports the framework, so the
    offline suite cannot import it — but it *can* lift a top-level function out of the AST and
    run it (`_exec_module_function`, the same trick `keyboard.signed_label` exists for). A guard
    that re-implements this rule instead of executing it tests its own arithmetic and nothing
    else; that version was written first and did **not** fail when the bug was put back.
    """
    if send_count <= 0:
        return ()
    table = []
    first_send = 0
    while first_send < send_count:
        rows = MAX_SENDS_PER_PAGE if send_count - first_send >= MAX_SENDS_PER_PAGE else 1
        per_page = ENCODER_COUNT // rows
        for first_track in range(0, RING_TRACKS, per_page):
            table.append((first_track, first_send, rows))
        first_send += rows
    return tuple(table)


def page_slots(page, send_count: int):
    """`(track_index, send_index)` per encoder for one page, or `None` for an empty slot.

    The inverse of the layout table at the top of this module, and — like `page_table` — kept at
    module level and free of `self` so the suite can execute it rather than re-derive it.
    """
    first_track, first_send, rows = page
    per_page = ENCODER_COUNT // rows
    slots = []
    for index in range(ENCODER_COUNT):
        column, row = index % per_page, index // per_page
        track, send = first_track + column, first_send + row
        slots.append(
            None
            if (row >= rows or track >= RING_TRACKS or send >= send_count)
            else (track, send)
        )
    return slots


class MotionSendsComponent(Component):
    """Maps the eight encoders onto (track, send) pairs, a page at a time.

    Holds one number — the page — and derives everything else. The grid shape, the page count,
    the parameter on each encoder, the colour of each halo and the label on each tile all come
    from the current page plus what Live currently has, so there is no second copy to drift.
    """

    send_controls = control_list(MappedControl, ENCODER_COUNT)

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self._mixer = None
        self._page = 0
        self._on_changed = None

    # -- wiring ------------------------------------------------------------
    def bind_mixer(self, mixer_component) -> None:
        """Take the Mixer, which is how the tracks are reached.

        Reading the tracks off the component rather than off `song.visible_tracks` is what makes
        the Sends page follow the **session ring**, exactly as the strips do — so a column is the
        same track on both pages. Taking the first eight visible tracks would look right until
        Left/Right moved the ring.
        """
        self._mixer = mixer_component
        self._remap()

    def bind_session_ring(self, session_ring) -> None:
        """Follow the ring, so paging Left/Right re-maps the encoders.

        🐛 **Without this, turning an encoder did nothing after paging.** `_remap()` ran once at
        setup, on layer grab and on a page change — but *not* when Left/Right moved the ring, so
        the encoders stayed mapped to whichever tracks had been under the strips before. Slots
        that had no track then were left with `mapped_parameter = None` and simply refused to
        turn, while the touch highlight still worked because that is keyed on the encoder index
        rather than on the mapping. Found on hardware 2026-08-03.

        ⚠️ **The obligation came with the mapping.** Volume and Pan never had this problem
        because `MixerComponent.__init__` subscribes to `__on_offset_changed` on its provider and
        re-connects its own parameters. Taking the mapping into our own hands — which the
        (track × send) layout required — meant inheriting the duty the framework had been
        discharging quietly. Any component that maps ring-derived parameters has to follow the
        ring; there is a guard for it now.

        `tracks` as well as `offset`: adding or deleting a track moves what is under a strip just
        as surely as paging does.
        """
        if session_ring is None:
            logger.warning(
                "Motion32: no session ring; the Sends page will not follow Left/Right paging"
            )
            return
        try:
            self._on_ring_offset_changed.subject = session_ring
            self._on_ring_tracks_changed.subject = session_ring
        except (AttributeError, RuntimeError):
            logger.exception("Motion32: could not follow the session ring from the Sends page")
        self._remap()

    @listens("offset")
    def _on_ring_offset_changed(self, *a):
        self._remap()

    @listens("tracks")
    def _on_ring_tracks_changed(self, *a):
        self._remap()

    def set_changed_listener(self, listener) -> None:
        self._on_changed = listener

    # -- geometry ----------------------------------------------------------
    @property
    def send_count(self) -> int:
        """How many sends every track has — i.e. how many return tracks the set holds."""
        try:
            return len(self.song.return_tracks)
        except (AttributeError, RuntimeError):
            return 0

    def _page_table(self):
        """This set's pages. The rule itself is `page_table` — see there for why it is module
        level and why that matters to the guard."""
        return page_table(self.send_count)

    def _current_page(self):
        table = self._page_table()
        if not table:
            return None
        return table[min(self._page, len(table) - 1)]

    @property
    def sends_per_page(self) -> int:
        """Rows on the **current** page — two normally, one on a leftover-send page."""
        page = self._current_page()
        return page[2] if page else 1

    @property
    def tracks_per_page(self) -> int:
        """Columns on the current page: eight when there is one row, four when there are two."""
        return ENCODER_COUNT // self.sends_per_page

    @property
    def page_count(self) -> int:
        """How many pages the set is worth. Zero sends means the page does not exist at all."""
        return len(self._page_table())

    @property
    def page(self) -> int:
        return self._page

    def set_page(self, page: int) -> None:
        """Show page `page`, clamped. Re-maps the encoders and reports the change."""
        count = self.page_count
        if count <= 0:
            self._page = 0
        else:
            self._page = max(0, min(count - 1, int(page)))
        self._remap()

    def slot(self, index: int):
        """`(track, send_index)` for encoder `index`, or `(None, None)` if the slot is empty.

        With the packing rule in `page_table`, an empty slot is now only reachable when the ring
        itself is short of tracks — never because of the send arithmetic.
        """
        page = self._current_page()
        if page is None or not 0 <= index < ENCODER_COUNT:
            return None, None
        entry = page_slots(page, self.send_count)[index]
        if entry is None:
            return None, None
        track_index, send_index = entry
        return self._ring_track(track_index), send_index

    def _ring_track(self, index: int):
        if self._mixer is None:
            return None
        try:
            return self._mixer.channel_strip(index).track
        except (AttributeError, IndexError, RuntimeError):
            return None

    # -- mapping -----------------------------------------------------------
    def _remap(self) -> None:
        """Point each encoder at its send parameter — or at nothing.

        ⚠️ **`mapped_parameter` is the framework's own mapping**, the same one
        `channel_strip._connect_send_parameters` uses. It hands the parameter to Live's engine, so
        turning an encoder costs no Python at all. Setting it to `None` releases the encoder,
        which is what an empty slot must do — an encoder still mapped to the previous page's
        parameter would quietly move the wrong send.
        """
        for index in range(ENCODER_COUNT):
            track, send_index = self.slot(index)
            parameter = None
            if track is not None and send_index is not None:
                try:
                    parameter = track.mixer_device.sends[send_index]
                except (AttributeError, IndexError, RuntimeError):
                    parameter = None
            try:
                self.send_controls[index].mapped_parameter = parameter
            except (AttributeError, IndexError, RuntimeError):
                logger.exception("Motion32: could not map send encoder %d", index)
        self._changed()

    def _changed(self) -> None:
        if self._on_changed is None:
            return
        try:
            self._on_changed()
        except Exception:
            logger.exception("Motion32: sends-changed listener failed")

    # -- what the screen and the halos need --------------------------------
    def slot_track(self, index: int):
        """The track encoder `index` is sending from, for the halo colour."""
        return self.slot(index)[0]

    def slot_label(self, index: int) -> str:
        """`"Drums A"` — the track and which send it is.

        The track name is what makes a column readable at a glance and the letter is what
        distinguishes the two rows, so both have to be there. Truncation happens on the way to
        the wire, where the element's real budget is known.
        """
        track, send_index = self.slot(index)
        if track is None or send_index is None:
            return ""
        try:
            name = str(track.name or "")
        except (AttributeError, RuntimeError):
            name = ""
        return f"{name} {send_label(send_index)}".strip()

    def slot_parameter(self, index: int):
        """The Live parameter on encoder `index`, for the arc and the value readout."""
        track, send_index = self.slot(index)
        if track is None or send_index is None:
            return None
        try:
            return track.mixer_device.sends[send_index]
        except (AttributeError, IndexError, RuntimeError):
            return None

    def page_label(self) -> str:
        """`"Sends A-B · 1-4"` — which sends and which tracks this page is showing."""
        page = self._current_page()
        if page is None:
            return "No sends"
        first_track, first_send, rows = page
        last_send = min(first_send + rows, self.send_count) - 1
        letters = (
            send_label(first_send)
            if last_send == first_send
            else f"{send_label(first_send)}-{send_label(last_send)}"
        )
        last_track = min(first_track + ENCODER_COUNT // rows, RING_TRACKS)
        return f"Send {letters} · {first_track + 1}-{last_track}"

    def _release(self) -> None:
        """Drop every mapping. **Leaving this page must free the encoders for the next mode.**

        🐛 **Plugin mode stopped binding its device.** This component set `mapped_parameter` on
        the eight encoders and never cleared it, so after a visit to the Sends page they were
        still holding send parameters — and the Device component's own mapping did not take the
        elements when Plugin was entered. Found on hardware 2026-08-03.

        ⚠️ **The framework does exactly this and it is not optional.**
        `ChannelStripComponent.update()` is
        `_connect_parameters()` when enabled and `_disconnect_parameters()` when not, and the
        latter is nothing more than `mapped_parameter = None` over its controls. Ours had only
        the first half.

        That is the **third** duty inherited unnoticed from taking the mapping into our own
        hands, after following the session ring and resolving the touched track. The rule they
        share: a component that maps parameters owns the whole lifecycle — point them, follow
        what moves under them, and let go.
        """
        for index in range(ENCODER_COUNT):
            try:
                self.send_controls[index].mapped_parameter = None
            except (AttributeError, IndexError, RuntimeError):
                pass

    def update(self):
        super().update()
        if self.is_enabled():
            # A layer grab re-creates the control connections, so the parameters have to be
            # re-pointed or the encoders come back mapped to nothing.
            self._remap()
        else:
            self._release()
