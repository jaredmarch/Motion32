"""Shared runtime objects for the Motion 32 script.

The framework instantiates components from `Specification.component_map` and does not pass
our own constructor arguments, so components cannot be handed the screen model directly.
This module is the agreed hand-off point: the `ControlSurface` publishes the screen here
before the components are built, and components read it lazily.

**Ownership matters, because this is module state that outlives a script instance.** Live
constructs a new `ControlSurface` *before* disconnecting the old one when the script is
reloaded (re-selecting the control surface, or editing a file). With an unscoped
`clear()`, the outgoing instance's `disconnect()` wipes the *incoming* instance's
references, and every later redraw finds nothing to draw on — a silently blank screen.
So publish/clear are keyed by owner, and a stale owner clearing is a no-op.
"""

from __future__ import annotations

_owner = None
_screen_model = None
_main_view = None
_params_view = None
_mixer_view = None
_notification_view = None
_menu_view = None
_parameter_source = None


def publish(
    owner,
    screen_model,
    main_view,
    params_view,
    mixer_view,
    notification_view,
    menu_view,
    parameter_source,
) -> None:
    """Install this instance's objects, taking ownership."""
    global _owner, _screen_model, _main_view, _params_view, _mixer_view
    global _notification_view, _menu_view, _parameter_source
    _owner = owner
    _screen_model = screen_model
    _main_view = main_view
    _params_view = params_view
    _mixer_view = mixer_view
    _notification_view = notification_view
    _menu_view = menu_view
    _parameter_source = parameter_source


def clear(owner) -> bool:
    """Release, but only if `owner` is the current owner.

    Returns True if it actually cleared. A False return means a previous instance tried to
    tear down state that now belongs to a newer one — the case that blanked the screen on
    every script reload.
    """
    global _owner, _screen_model, _main_view, _params_view, _mixer_view
    global _notification_view, _menu_view, _parameter_source
    if owner is not _owner:
        return False
    _owner = None
    _screen_model = None
    _main_view = None
    _params_view = None
    _mixer_view = None
    _notification_view = None
    _menu_view = None
    _parameter_source = None
    return True


def screen_model():
    return _screen_model


def main_view():
    """Template 0 — the encoder-tile view used by Plugin mode."""
    return _main_view


def params_view():
    """Template 3 — the label+value view used by Song mode."""
    return _params_view


def mixer_view():
    """Template 2 — the eight channel strips used by Mix mode."""
    return _mixer_view


def notification_view():
    """Template 1 — the transient title/value bar. Outranks the mode's view while shown."""
    return _notification_view


def menu_view():
    """Template 1 — the scrollable list, shared with the notification bar (see `menu.py`)."""
    return _menu_view


def parameter_source():
    return _parameter_source


def views():
    """Every view, in one place — **the single roster.**

    `full_redraw()` has to call `forget()` on all of them: it clears the screen model's "sent"
    map for *every* template, so any view still holding a content memo would short-circuit on
    an unchanged snapshot and draw nothing.

    🐛 That list used to be typed out at the call site and `MixerView` was never added to it
    (found 2026-08-03, harmless only by luck — `invalidate()` leaves `_desired` intact, so the
    last strip content still went back out). It is the same failure as the LED groups, where a
    newly added group was put in one named list and not the other and the keybed stayed dark
    after connect. A roster is the fix for both: add a view here and every walker gets it.

    Nones are filtered, so a caller during construction or after `clear()` gets an empty
    sequence rather than having to guard each entry.
    """
    return tuple(
        view
        for view in (_main_view, _params_view, _mixer_view, _notification_view, _menu_view)
        if view is not None
    )


def is_ready() -> bool:
    """True when a live instance owns a complete set of objects here.

    The reload guard in the suite reads this: after a superseded instance's `clear()` it must
    still be True, because the *newer* instance's publish is what is installed. Derived from
    `views()` so a view added to the roster is covered by both.
    """
    return _screen_model is not None and len(views()) == 5
