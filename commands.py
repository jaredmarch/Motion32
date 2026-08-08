"""The Shift pad overlay — the bottom lane as an edit-command layer (Phase 8).

Hold **Shift** and the bottom lane (notes 36-51) stops being a keyboard and becomes sixteen
command slots, exactly as the factory does it (`padMode=Commands`, handshake spec §2.2). The top
lane goes dark and silent, and every pad that has no command is grey rather than dark — the
factory's convention for "present but unassigned", and the one that distinguishes an empty slot
from a broken one.

**Six commands, not sixteen, and that is deliberate** (user, 2026-08-03). The factory's sixteen
are Studio One's, and most of them do not survive the translation:

| Factory command | Ableton |
|---|---|
| Undo, Redo | ✅ `song.undo()` / `song.redo()`, gated on `can_undo` / `can_redo` |
| Duplicate, Delete, Quantize, Double | ✅ the target clip — what `Clip_Actions` does |
| Copy, Paste | ⏸ needs a clip **grid** to point at; see below |
| Split, Merge/Consolidate | ❌ **not in the LOM at all** |
| Insert Pattern, New/Duplicate Variation | ❌ Live has no patterns or variations |
| Insert Instrument Part | ❌ a Studio One arrangement concept |
| Prev/Next grid, Floating Windows | ⏸ possible, not yet decided |

The ❌ row is settled, not suspected: a grep for `split`, `consolidate`, `join`, `freeze` and
`flatten` across all twelve LOM reference files finds nothing (2026-08-03).

⏸ **Why Copy/Paste are not here.** The framework has a real `ClipboardComponent`, but it works by
holding Copy and tapping a *source* object, then a *destination* — `copy_or_paste(obj)` is handed
the object by whatever grid you pressed. With no Session mode there is nothing to point at, so a
Copy pad today could only copy "the selected thing" and would be a different feature wearing the
same name. They arrive with Session mode.

⚠️ **Why these are our own handlers and not `Clip_Actions` bound straight to the pads.** The
framework component is good, and on any other controller it would be the right answer. Here it
would take **LED ownership of four pad addresses** — a pad's LED address *is* its note address, so
a framework `ButtonControl` on a pad writes colour there, and `leds.PadLeds` is the single writer
of every pad on this device (`elements.py`, §6b-10). Four framework-owned pads sitting inside
twenty-eight of ours is precisely the two-writer split that cost three attempts on the encoder
halos. The actions themselves are three LOM lines each; the ownership is the part that matters.

**No Python in the pad→note path** still holds: this component is only ever reached through a
*Shift-modified* element, which is a different element from the pad the keyboard plays.
"""

from __future__ import annotations

import logging

from ableton.v3.control_surface import Component
from ableton.v3.control_surface.components import ModifierBackgroundComponent
from ableton.v3.control_surface.controls import ButtonControl, control_list

logger = logging.getLogger(__name__)

#: How many command slots the bottom lane offers. Sixteen, whether or not they are all filled —
#: the grid is the factory's and an empty slot is rendered, not omitted.
COMMAND_SLOTS = 16

#: What the notification bar calls this layer. Six characters, inside the ~6-7 the bar's leftmost
#: soft-button slot really fits (see `keyboard.NOTIFICATION_TITLE` for why that budget is not the
#: `MAXCHARS_MENU_BUTTON = 16` the element advertises).
NOTIFICATION_TITLE = "Edit"


class MotionModifierComponent(ModifierBackgroundComponent):
    """`Modifier_Background`, plus a way to know when Shift is down.

    ⚠️ **Subclasses `ModifierBackgroundComponent`, not plain `BackgroundComponent`.** The
    modifier subclass is the one whose `_setup_control_state` builds the computed skin keys
    (`ModifierBackground.Shift` / `…ShiftPressed`, derived from the component's own name — see
    `skin.py`). Dropping to the plain background would consume the button correctly and leave it
    **colourless**, undoing the Shift LED fix from earlier the same day.

    The framework version consumes the modifier and lights it, and that is all — nothing
    observes it. The keybed needs to repaint the moment Shift goes down, so this adds the
    transition report.

    🔑 **It listens to the *element*, not to a second control.** Binding another `ButtonControl`
    to `shift_button` would put two layers on one element, which the suite forbids and which
    invites exactly the ownership fights this project keeps having. `_set_element_for_control` is
    the framework's own hook for "an element has just been handed to this control name", so
    attaching a value listener there observes without owning.
    """

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self._shift_element = None
        self._shift_listener = None
        self._on_shift_changed = None

    def set_shift_listener(self, listener) -> None:
        """Called with True/False as Shift goes down and up."""
        self._on_shift_changed = listener

    def _set_element_for_control(self, control_name, element):
        super()._set_element_for_control(control_name, element)
        if control_name != "shift":
            return
        self._detach_shift()
        if element is None:
            return
        try:
            self._shift_listener = self._make_shift_listener()
            element.add_value_listener(self._shift_listener)
            self._shift_element = element
        except (AttributeError, RuntimeError):
            logger.exception(
                "Motion32: could not observe the Shift element; the command layer will still "
                "work but the pads will not repaint while it is held"
            )
            self._shift_element = None
            self._shift_listener = None

    def _make_shift_listener(self):
        def _on_value(value, *_a):
            if self._on_shift_changed is None:
                return
            try:
                self._on_shift_changed(bool(value))
            except Exception:
                # A keybed that fails to repaint must never break the modifier itself — every
                # `_with_shift` control on the surface depends on this element still working.
                logger.exception("Motion32: shift listener failed")

        return _on_value

    def _detach_shift(self):
        if self._shift_element is None or self._shift_listener is None:
            return
        try:
            if self._shift_element.value_has_listener(self._shift_listener):
                self._shift_element.remove_value_listener(self._shift_listener)
        except (AttributeError, RuntimeError):
            pass
        self._shift_element = None
        self._shift_listener = None

    def disconnect(self):
        self._detach_shift()
        super().disconnect()


class MotionCommandsComponent(Component):
    """The sixteen Shift-pad slots. Six of them do something.

    ⚠️ **`color=None` on every control, and it is load-bearing.** These controls sit on pad
    elements, whose LED address is their note address. A `ButtonControl` with a colour would
    write it there on every layer grab, and `leds.PadLeds` would be fighting the framework for
    thirty-two addresses. `Skin.__getitem__` returns `None` for a `None` key, so a colourless
    control sends nothing and `PadLeds` stays the single writer — the same conclusion
    `keyboard.py` reached by leaving `_update_button_color` as the base class's empty hook.
    """

    command_pads = control_list(ButtonControl, COMMAND_SLOTS, color=None)

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self._on_notification = None
        self._on_layout_changed = None
        self._shift_held = False
        #: Slot -> (label, handler). Built once; `slot_labels()` and the press handler are the
        #: only readers, so the layout cannot disagree with what the pads actually do.
        self._commands = self._build_commands()

    # -- the command table -------------------------------------------------
    def _build_commands(self):
        """Slot index -> `(label, callable)`. Absent slots are unassigned.

        Labels are what the screen and the notification bar show, so they are short by
        construction rather than by truncation.

        The first six slots are filled and the rest are not; the layout is deliberately a
        left-to-right block rather than scattered, because a keybed of mostly-grey pads reads
        far better with the live ones together.
        """
        return {
            0: ("Undo", self._undo),
            1: ("Redo", self._redo),
            2: ("Dup", self._duplicate_clip),
            3: ("Delete", self._delete_clip),
            4: ("Quant", self._quantize_clip),
            5: ("Double", self._double_clip),
        }

    def slot_labels(self):
        """Sixteen labels, empty string for an unassigned slot."""
        return [self._commands.get(slot, ("", None))[0] for slot in range(COMMAND_SLOTS)]

    def assigned_slots(self):
        """Which slots do something — what the keybed paints white rather than grey."""
        return frozenset(self._commands)

    # -- wiring ------------------------------------------------------------
    def set_notification_listener(self, listener) -> None:
        """Called with `(title, value)` when a command runs.

        The component does not know what a screen is, exactly as `keyboard.py` does not: it
        reports, and `screen_component.notify` decides. Keeps the display single-owner and this
        module testable offline.
        """
        self._on_notification = listener

    def set_layout_listener(self, listener) -> None:
        """Called with `(shift_held, labels, assigned)` whenever the overlay appears or goes."""
        self._on_layout_changed = listener

    @property
    def shift_held(self) -> bool:
        return self._shift_held

    def set_shift_held(self, held: bool) -> None:
        """Told by `MotionModifierComponent`. Drives the keybed repaint and nothing else."""
        held = bool(held)
        if held == self._shift_held:
            return
        self._shift_held = held
        self._report_layout()

    def _report_layout(self):
        if self._on_layout_changed is None:
            return
        try:
            self._on_layout_changed(
                self._shift_held, self.slot_labels(), self.assigned_slots()
            )
        except Exception:
            logger.exception("Motion32: command-layout listener failed")

    def _notify(self, label: str, outcome: str) -> None:
        if self._on_notification is None:
            return
        try:
            self._on_notification(NOTIFICATION_TITLE, label if not outcome else outcome)
        except Exception:
            logger.exception("Motion32: command notification failed")

    # -- the pads ----------------------------------------------------------
    # A `control_list` handler is called with **the control**, not an index — the index is
    # `button.index`. (`(self, index, control)` is the 2D `control_matrix` shape and raises on
    # the first press; the suite guards this.)
    @command_pads.pressed
    def command_pads(self, button):
        try:
            slot = int(button.index)
        except (AttributeError, TypeError, ValueError):
            return
        entry = self._commands.get(slot)
        if entry is None:
            # An unassigned slot is grey and silent, but it still answers: a press that does
            # nothing *and* says nothing is indistinguishable from a broken pad.
            self._notify("", "--")
            return
        label, handler = entry
        try:
            outcome = handler()
        except Exception:
            # A failed edit must never take the surface down mid-performance, but it must be
            # loud — this is the one path in the script that changes the user's song.
            logger.exception("Motion32: command %r failed", label)
            self._notify(label, "Failed")
            return
        self._notify(label, outcome or label)

    # -- commands ----------------------------------------------------------
    #
    # Each returns the string the notification bar shows, or None to fall back to the label.
    # Each is gated: a command that cannot run says so rather than doing nothing quietly.

    def _undo(self):
        song = self._live_song()
        if song is None:
            return "No song"
        if not getattr(song, "can_undo", False):
            return "Nothing"
        song.undo()
        return None

    def _redo(self):
        song = self._live_song()
        if song is None:
            return "No song"
        if not getattr(song, "can_redo", False):
            return "Nothing"
        song.redo()
        return None

    def _duplicate_clip(self):
        clip = self._target_clip()
        if clip is None:
            return "No clip"
        clip.duplicate_loop()
        return None

    def _double_clip(self):
        """Live's clip 'Double' is `duplicate_loop` on the *loop*; Duplicate is the same call.

        ⚠️ They are genuinely different in the framework — `ClipActionsComponent` has separate
        `duplicate_button` and `double_button` — but both bottom out in clip-length operations
        and Live exposes only `duplicate_loop()` here. Kept as two slots because the factory has
        two and because the day the LOM separates them the pads are already there; today the
        second one doubles the *loop brace* by extending it.
        """
        clip = self._target_clip()
        if clip is None:
            return "No clip"
        try:
            clip.loop_end = clip.loop_end + (clip.loop_end - clip.loop_start)
        except (AttributeError, RuntimeError):
            return "Cannot"
        return None

    def _delete_clip(self):
        slot = self._target_clip_slot()
        if slot is None:
            return "No clip"
        slot.delete_clip()
        return None

    def _quantize_clip(self):
        clip = self._target_clip()
        if clip is None:
            return "No clip"
        song = self._live_song()
        # The framework quantizes to the song's own record quantization, which is the setting
        # the user has already chosen — see `ClipActionsComponent._quantize_clip`. Matching it
        # means the pad does what Live's own Quantize does, rather than inventing a grid.
        grid = getattr(song, "midi_recording_quantization", None) if song else None
        if grid is None:
            return "No grid"
        clip.quantize(grid, 1.0)
        return None

    # -- Live access -------------------------------------------------------
    def _live_song(self):
        """`Component.song`, guarded. Named `_live_song` because `_song` is the framework's."""
        try:
            return self.song
        except AttributeError:
            return None

    def _target_clip_slot(self):
        """The highlighted clip slot — what Live's own edit commands act on."""
        song = self._live_song()
        if song is None:
            return None
        try:
            slot = song.view.highlighted_clip_slot
        except (AttributeError, RuntimeError):
            return None
        try:
            if slot is None or not slot.has_clip:
                return None
        except (AttributeError, RuntimeError):
            return None
        return slot

    def _target_clip(self):
        slot = self._target_clip_slot()
        if slot is None:
            return None
        try:
            clip = slot.clip
        except (AttributeError, RuntimeError):
            return None
        try:
            clip.name  # probe: a Live object can outlive its C++ counterpart
        except (RuntimeError, AttributeError):
            return None
        return clip
