"""The big screen wheel.

Only the **push** lives here. Turning is handled by whichever framework component the wheel is
bound to in the current mode — in Plugin mode that is the Device component's
`bank_scroll_encoder`, which already scrolls parameter banks properly.

The push needs its own component because the behaviour Live's framework offers is not quite
it: `Device_Navigation` (a `ScrollComponent`) **stops** at the ends of the device chain, and we
want the next device with **wraparound** so repeated clicks cycle a track's devices.

Note the wheel is a *clickable* encoder, not a capacitive one — only encoders 1-8 have touch
(`knobTouch`, CC 0x70-0x77).

The push deliberately does **not** touch the wheel's LED. The halo is a mode-level indicator
owned by `screen_component.py`: lit for the whole of **every mode that gives the wheel a job** —
Plugin (bank scroll + click) and Mix (paging Volume/Pan) — and dark otherwise. A press
highlight meant the light changed while the control was in use, and each of those transitions
was a chance to be left dark.
"""

from __future__ import annotations

import logging

from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl

logger = logging.getLogger(__name__)


class MotionWheelComponent(Component):
    """Wheel push: select the next device on the current track, wrapping at the end."""

    # No feedback: input CC 0x78 is wheel push, but output CC 0x78 is touch-strip 2 LED 9.
    # The screen/menu shows the result of the click; the wheel halo is handled separately.
    push_button = ButtonControl()

    @push_button.pressed
    def push_button(self, _):
        self._select_next_device()

    def _select_next_device(self):
        try:
            song = self.song
            track = song.view.selected_track
            devices = list(track.devices)
        except (RuntimeError, AttributeError):
            return
        if not devices:
            return

        try:
            current = track.view.selected_device
        except (RuntimeError, AttributeError):
            current = None

        index = -1
        for position, device in enumerate(devices):
            if device == current:
                index = position
                break
        target = devices[(index + 1) % len(devices)]

        # `select_device` is the documented way; `appointed_device` is the fallback, and is
        # also what the framework's Device component follows.
        try:
            song.view.select_device(target)
            return
        except (RuntimeError, AttributeError, TypeError):
            pass
        try:
            song.appointed_device = target
        except (RuntimeError, AttributeError):
            logger.warning("Motion32: could not select the next device")
