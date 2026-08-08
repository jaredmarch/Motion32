"""Motion 32 native-protocol helpers and receive-side parsing."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Optional, Sequence, Tuple

from . import midi


MidiMessage = Tuple[int, ...]

# Absolute byte offsets of the firmware fields in the Identity Reply, counting from
# the leading 0xF0. Valid for a 1-byte manufacturer id (Fender = 0x08); a 3-byte
# manufacturer id would shift these by 2. See parse_identity_reply().
FIRMWARE_MAJOR_INDEX = 11
FIRMWARE_MINOR_INDEX = 12
FIRMWARE_PATCH_INDEX = 13


def as_hex(message: Sequence[int]) -> str:
    return " ".join(f"{byte:02X}" for byte in message)


def is_sysex(message: Sequence[int]) -> bool:
    return bool(message) and message[0] == midi.SYSEX_START and message[-1] == midi.SYSEX_END


def is_global_settings_state(message: Sequence[int]) -> bool:
    return (
        len(message) == 6
        and tuple(message[:4]) == midi.MOTION_SYSEX_HEADER + (midi.MSG_GLOBAL_SETTINGS_STATE,)
        and message[-1] == midi.SYSEX_END
    )


def parse_global_settings_state(message: Sequence[int]) -> Optional[bool]:
    """Return True while the device's Global Settings screen is open."""
    if not is_global_settings_state(message):
        return None
    return message[4] == midi.GLOBAL_SETTINGS_OPEN


@dataclass(frozen=True)
class IdentityInfo:
    manufacturer_id: Optional[int]
    raw_payload: Tuple[int, ...]
    firmware_major: Optional[int] = None
    firmware_minor: Optional[int] = None
    firmware_patch: Optional[int] = None

    @property
    def version(self) -> str:
        parts = (self.firmware_major, self.firmware_minor, self.firmware_patch)
        if any(p is None for p in parts):
            return "unknown"
        return ".".join(str(p) for p in parts)

    @property
    def version_code(self) -> Optional[int]:
        if self.firmware_major is None or self.firmware_minor is None or self.firmware_patch is None:
            return None
        # Mirrors the reference host's major*1000 + Number(f"{minor}{patch}") rule.
        return self.firmware_major * 1000 + int(f"{self.firmware_minor}{self.firmware_patch}")


def _decode_bcd(byte: int) -> Optional[int]:
    """Decode a firmware byte the way the reference host does.

    The JS is ``parseInt(byte.toString(16))`` — the byte is rendered as hex then
    read back as *decimal*, so 0x10 decodes to 10, not 16. Any byte containing a
    hex letter (0x0A-0x0F, 0x1A-…) has no decimal reading; JS yields NaN, we yield None.
    """
    try:
        return int(f"{byte:x}")
    except ValueError:
        return None


def parse_identity_reply(message: Sequence[int]) -> Optional[IdentityInfo]:
    """Parse a Universal MIDI Identity Reply.

    Firmware bytes live at **fixed offsets from the leading 0xF0**, per
    ``IdentityReplyMessage`` in the reference ``Motion32MidiDevice.js``:
    ``data[10 + mfrIdLen]`` … ``data[13 + mfrIdLen]``. Fender's manufacturer id is
    the single byte 0x08, so major/minor/patch are absolute indices 11/12/13.

        F0 7E 7F 06 02 08 00 00 26 00 00 01 00 06 F7
         0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
                                       ^maj ^min ^pat

    The build byte would be index 14, which in the Motion's 15-byte reply is the
    0xF7 terminator — it is not a real value and is not part of the version gate,
    so it is deliberately not parsed. Do NOT compute these offsets from the end of
    the message: that reads 00 01 00 06 and reports "0.1.0" (version code 10),
    which trips a bogus "firmware too old" warning.
    See Motion32_Implementation_Notes.md §1a.
    """
    if not is_sysex(message):
        return None
    # Need index 13 to exist, plus the terminator.
    if len(message) < FIRMWARE_PATCH_INDEX + 2:
        return None
    if tuple(message[:5]) != (0xF0, 0x7E, message[2], 0x06, 0x02):
        return None

    payload = tuple(message[5:-1])
    return IdentityInfo(
        manufacturer_id=payload[0] if payload else None,
        raw_payload=payload,
        firmware_major=_decode_bcd(message[FIRMWARE_MAJOR_INDEX]),
        firmware_minor=_decode_bcd(message[FIRMWARE_MINOR_INDEX]),
        firmware_patch=_decode_bcd(message[FIRMWARE_PATCH_INDEX]),
    )


def screen_template_message(template_id: int) -> MidiMessage:
    if not 0 <= template_id <= 3:
        raise ValueError(f"Invalid Motion screen template: {template_id}")
    return midi.MOTION_SYSEX_HEADER + (midi.MSG_SCREEN_TEMPLATE, template_id, midi.SYSEX_END)


def screen_update_message(
    template_id: int,
    zone_id: int,
    element_id: int,
    attribute: int,
    data: Iterable[int],
) -> MidiMessage:
    payload = tuple(int(value) for value in data)
    if any(value < 0 or value > 0x7F for value in payload):
        raise ValueError("Motion SysEx payload values must be 7-bit")
    return (
        midi.MOTION_SYSEX_HEADER
        + (midi.MSG_SCREEN_UPDATE, template_id, zone_id, element_id, attribute)
        + payload
        + (midi.SYSEX_END,)
    )


class MotionProtocol:
    """Small protocol facade owned by the control-surface instance."""

    def __init__(
        self,
        send_midi: Callable[[MidiMessage], None],
        log_message: Callable[[str], None],
        on_feedback_resumed: Optional[Callable[[], None]] = None,
    ) -> None:
        self._send_midi = send_midi
        self._log_message = log_message
        # Called when the device's Global Settings screen closes: everything the
        # device was showing is gone, so the owner must invalidate and redraw.
        self._on_feedback_resumed = on_feedback_resumed
        self.feedback_suspended = False
        self.identity: Optional[IdentityInfo] = None
        self.verbose = False  # per-message TX logging; noisy, off by default

    def send(self, message: Sequence[int]) -> None:
        packet = tuple(int(byte) for byte in message)
        if self.feedback_suspended and self._is_device_feedback(packet):
            return
        if self.verbose:
            self._log_message(f"Motion32 TX: {as_hex(packet)}")
        self._send_midi(packet)

    @staticmethod
    def _is_device_feedback(packet: MidiMessage) -> bool:
        """True for screen SysEx the device must not receive while suspended.

        Covers BOTH template select (0x20) and element update (0x21) — the previous
        version gated only 0x21, which let a template switch slip through while the
        user had Global Settings open.
        """
        return len(packet) >= 4 and packet[:3] == midi.MOTION_SYSEX_HEADER and packet[3] in (
            midi.MSG_SCREEN_TEMPLATE,
            midi.MSG_SCREEN_UPDATE,
        )

    def handle_incoming(self, message: Sequence[int]) -> bool:
        """Consume a device SysEx message. Returns True if we handled it.

        The caller uses that to decide whether to forward the message to the framework;
        forwarding one we own just produces a "Got unknown sysex message" warning.
        """
        packet = tuple(int(byte) for byte in message)

        settings_open = parse_global_settings_state(packet)
        if settings_open is not None:
            self.feedback_suspended = settings_open
            state = "opened" if settings_open else "closed"
            self._log_message(f"Motion32: Global Settings {state}")
            if not settings_open:
                self._log_message("Motion32: feedback resumed; invalidating and redrawing")
                if self._on_feedback_resumed is not None:
                    self._on_feedback_resumed()
            return True

        identity = parse_identity_reply(packet)
        if identity is not None:
            self.identity = identity
            version = identity.version_code
            if version is None:
                self._log_message(
                    f"Motion32: could not read firmware from identity reply {as_hex(packet)}"
                )
            else:
                self._log_message(f"Motion32 firmware: {identity.version} (code {version})")
                if version < midi.REQUIRED_FIRMWARE_VERSION:
                    self._log_message(
                        "Motion32 WARNING: firmware is older than the supported minimum "
                        f"{midi.REQUIRED_FIRMWARE_VERSION}"
                    )
            return True

        return False
