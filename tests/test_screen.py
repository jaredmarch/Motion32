"""Offline tests for the Motion 32 screen engine and identity parsing.

Run from anywhere:

    python3 tests/test_screen.py

No Ableton, no hardware. The modules under test (`midi`, `screen`, `formatting`,
`display`, `protocol`) deliberately import nothing from the framework, so they can be
loaded directly — the package `__init__` is bypassed because *that* does import
`ableton.*`.

The most valuable check here is `test_every_address_is_real`: every
`(template, zone, element, attr)` the renderer emits is verified against
`Motion32_Screen_Template_Map.csv` — the machine-extracted list of the device's 433
real attribute handlers. That catches an address typo or an attribute the element
doesn't actually accept, which on hardware would just look like "nothing happened".
"""

from __future__ import annotations

import csv
import dataclasses
import importlib.machinery
import importlib.util
import os
import sys
import textwrap
import types

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT_DIR = os.path.dirname(HERE)

# Candidate locations for the extracted screen map (script-local, then the project
# resources folder next to it).
CSV_CANDIDATES = [
    os.path.join(SCRIPT_DIR, "Resources", "Motion32_Screen_Template_Map.csv"),
    os.path.join(SCRIPT_DIR, "Motion32_Screen_Template_Map.csv"),
]


# ---------------------------------------------------------------------------
# Load the framework-free modules under a synthetic package
# ---------------------------------------------------------------------------
PACKAGE = "motion32_under_test"

# Never let a cached .pyc stand in for the source.
#
# CPython validates cached bytecode on the source's **(mtime, size)** pair, and mtime has
# one-second granularity. A same-second edit that happens to leave the file the same size is
# therefore invisible: the stale .pyc is reused and the suite tests code that is no longer on
# disk, reporting a confident pass. That is not hypothetical — it bit this suite while
# verifying the contrast guard, because `(299, 587, 114)` and `(333, 333, 333)` are both
# exactly 15 characters. A fast edit/test loop is precisely the situation that triggers it.
sys.dont_write_bytecode = True


class _AlwaysCompile(importlib.machinery.SourceFileLoader):
    """A loader that compiles from source every time, ignoring any cached bytecode."""

    def get_code(self, fullname):
        return compile(self.get_source(fullname), self.get_filename(fullname), "exec")


def _spec(name, path):
    return importlib.util.spec_from_file_location(name, path, loader=_AlwaysCompile(name, path))


def _load_package():
    package = types.ModuleType(PACKAGE)
    package.__path__ = [SCRIPT_DIR]
    sys.modules[PACKAGE] = package
    modules = {}
    for name in (
        "midi", "palette", "pads", "screen", "formatting", "display", "protocol",
        "parameters", "runtime", "leds", "notification", "scales", "menu",
    ):
        path = os.path.join(SCRIPT_DIR, f"{name}.py")
        spec = _spec(f"{PACKAGE}.{name}", path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[f"{PACKAGE}.{name}"] = module
        spec.loader.exec_module(module)
        modules[name] = module
    return modules


def _load_mappings():
    """Import mappings.py for real, with the framework's mode module stubbed.

    Evaluating the actual `create_mappings()` beats picking the dict apart with AST: the
    mode specs are built with helpers and `dict(...)` calls, and an AST walker that has to
    understand those is more likely to be wrong than the thing it is checking.
    """

    class _Behaviour:
        def __init__(self, *a, **k):
            self.args, self.kwargs = a, k

        def __repr__(self):
            return f"<{type(self).__name__}>"

    ableton = types.ModuleType("ableton")
    v3 = types.ModuleType("ableton.v3")
    cs = types.ModuleType("ableton.v3.control_surface")
    mode = types.ModuleType("ableton.v3.control_surface.mode")
    for name in (
        "ImmediateBehaviour",
        "LatchingBehaviour",
        "ToggleBehaviour",
        "MomentaryBehaviour",
    ):
        setattr(mode, name, type(name, (_Behaviour,), {}))
    ableton.v3 = v3
    v3.control_surface = cs
    cs.mode = mode
    for name, module in (
        ("ableton", ableton),
        ("ableton.v3", v3),
        ("ableton.v3.control_surface", cs),
        ("ableton.v3.control_surface.mode", mode),
    ):
        sys.modules.setdefault(name, module)

    path = os.path.join(SCRIPT_DIR, "mappings.py")
    spec = _spec(f"{PACKAGE}.mappings", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[f"{PACKAGE}.mappings"] = module
    spec.loader.exec_module(module)
    return module


M = _load_package()
mappings_module = _load_mappings()
MAPPINGS = mappings_module.create_mappings(None)
midi = M["midi"]
palette = M["palette"]
pads = M["pads"]
scales = M["scales"]
menu = M["menu"]
screen = M["screen"]
formatting = M["formatting"]
display = M["display"]
protocol = M["protocol"]
parameters = M["parameters"]
runtime = M["runtime"]
leds = M["leds"]
notification = M["notification"]


# ---------------------------------------------------------------------------
# Tiny assertion helpers (no pytest dependency inside Live's environment)
# ---------------------------------------------------------------------------
_failures = []
_checks = [0]


def check(condition, message):
    _checks[0] += 1
    if not condition:
        _failures.append(message)


def check_equal(actual, expected, message):
    _checks[0] += 1
    if actual != expected:
        _failures.append(f"{message}\n     expected: {expected!r}\n     actual:   {actual!r}")


class Recorder:
    """Stands in for MotionProtocol.send and keeps every frame."""

    def __init__(self):
        self.messages = []

    def __call__(self, message):
        self.messages.append(tuple(message))

    def clear(self):
        self.messages = []

    def hex(self):
        return [" ".join(f"{b:02X}" for b in m) for m in self.messages]


def make_model():
    recorder = Recorder()
    return recorder, display.ScreenModel(send=recorder)


def sample_params_content():
    tiles = tuple(
        display.ParamsTile(label=label, value=value)
        for label, value in (
            ("Tempo", "124.0"),
            ("Position", "17.2.1"),
            ("Loop Start", "9.1.1"),
            ("Loop End", "17.1.1"),
            ("H Zoom", ""),
            ("V Zoom", ""),
            ("Cue", ""),
            ("Fine Tempo", "124.0"),
        )
    )
    return display.ParamsContent(title="Session", centre="Lead Synth 2", tiles=tiles)


def sample_mixer_content(focused=None, meters=None):
    """Eight strips: 0-5 assigned, 6-7 empty. Strip 4 is a MIDI track with no instrument.

    `meters` overrides the per-strip `(left, right)` levels, so a test can place a signal in a
    particular colour band without rebuilding the whole content.
    """
    default_meters = (
        (0.30, 0.28),   # 0 Drums  — green
        (0.80, 0.78),   # 1 Bass   — amber
        (0.95, 0.99),   # 2 Keys   — red
        (0.00, 0.00),   # 3 Lead   — silent but capable
        (0.00, 0.00),   # 4 Pad    — not metered at all (see below)
        (0.10, 0.10),   # 5 FX     — green
        (0.00, 0.00),
        (0.00, 0.00),
    )
    levels = meters or default_meters
    strips = tuple(
        display.MixerStrip(
            name=name,
            number=str(index + 1),
            volume=volume,
            muted=index == 2,
            soloed=index == 5,
            colour=(index * 9, 40, 80),
            assigned=index < 6,
            meter_left=levels[index][0],
            meter_right=levels[index][1],
            # Strip 4 stands in for a MIDI track with no instrument: assigned, but
            # `has_audio_output` is False, so its meters must be hidden rather than flat.
            metered=index < 6 and index != 4,
        )
        for index, (name, volume) in enumerate(
            (
                ("Drums", 100),
                ("Bass", 92),
                ("Keys", 80),
                ("Lead", 64),
                ("Pad", 48),
                ("FX", 20),
                ("", 0),
                ("", 0),
            )
        )
    )
    return display.MixerContent(strips=strips, focused=focused)


def sample_content():
    tiles = tuple(
        display.EncoderTile(label=name, value=value, assigned=True)
        for name, value in (
            ("Filter Freq", 64),
            ("Resonance", 0),
            ("Attack", 127),
            ("Decay", 32),
            ("Sustain", 96),
            ("Release", 12),
            ("Dry/Wet", 127),
            ("Volume", 100),
        )
    )
    return display.MainContent(title="Operator", centre="Bank 1/3", tiles=tiles)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
def test_compactify_matches_factory():
    """Locked against values differentially tested vs Fender's own JavaScript."""
    expected = {
        ("Filter Freq", 7): "FiltFre",
        ("Auto Filter", 7): "AutoFil",
        ("Delay Feedback Amount", 7): "DelFeAm",
        ("Hi-Pass Frequency Cutoff", 7): "HiPFrCu",
        ("Frequency", 7): "Frqncy",
        ("Resonance", 7): "Rsnnce",
        ("Envelope", 7): "Envlpe",
        ("Operator", 7): "Oprtr",
        ("Attack", 7): "Attack",
        ("Dry/Wet", 7): "Dry/Wet",
        ("Reverb Send A", 8): "ReveSenA",
        ("Lead Synth 2", 8): "LeadSyn2",
        ("Drum Rack", 8): "DrumRack",
        ("Spectral Resonator", 8): "SpecReso",
        ("Glue Compressor", 13): "GlueCompresso",
        ("Oscillator Pitch Coarse", 13): "OscilPitcCoar",
        ("", 7): "",
        ("A", 7): "A",
        ("x y z w v u t s", 7): "xyzwvut",
    }
    for (text, limit), want in expected.items():
        check_equal(formatting.compactify(text, limit), want, f"compactify({text!r}, {limit})")

    # Nothing may ever exceed its budget — that is the whole point of the function.
    for limit in (7, 8, 13, 16):
        for text in expected:
            got = formatting.compactify(text[0], limit)
            check(len(got) <= limit, f"compactify({text[0]!r}, {limit}) overflowed: {got!r}")


def test_ascii_encoding_is_seven_bit():
    payload = formatting.to_ascii_bytes("Café—Über", 13)
    check(all(0x20 <= b <= 0x7E for b in payload), f"non-7-bit ASCII byte in {payload}")
    check("?" in "".join(chr(b) for b in payload), "non-ASCII should degrade to '?', not vanish")


def test_frames_are_well_formed():
    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()
    view.render(sample_content())
    model.flush()

    check(len(recorder.messages) > 0, "nothing was sent")
    for message in recorder.messages:
        check_equal(message[0], midi.SYSEX_START, f"frame does not start with F0: {message}")
        check_equal(message[-1], midi.SYSEX_END, f"frame does not end with F7: {message}")
        check_equal(
            message[1:3],
            (midi.FENDER_MANUFACTURER_ID, midi.MOTION_32_DEVICE_ID),
            f"wrong manufacturer/device header: {message}",
        )
        for byte in message[1:-1]:
            check(0 <= byte <= 0x7F, f"non-7-bit data byte {byte:#02x} in {message}")


def test_template_select_comes_first():
    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()
    view.render(sample_content())
    model.flush()
    first = recorder.messages[0]
    check_equal(
        first,
        (0xF0, 0x08, 0x26, 0x20, 0x00, 0xF7),
        "first message should select template 0",
    )


def test_diff_suppresses_redundant_writes():
    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()
    content = sample_content()

    view.render(content)
    initial = model.flush()
    check(initial > 20, f"first paint should be substantial, got {initial} messages")

    # Same content again: the view short-circuits and the model has nothing to send.
    recorder.clear()
    view.render(content)
    check_equal(model.flush(), 0, "re-rendering identical content must send nothing")

    # One parameter value moves -> exactly one element changed.
    tiles = list(content.tiles)
    tiles[2] = display.EncoderTile(label="Attack", value=90, assigned=True)
    moved = display.MainContent(
        title=content.title, centre=content.centre, tiles=tuple(tiles)
    )
    recorder.clear()
    view.render(moved)
    check_equal(model.flush(), 1, "a single value change must be a single message")
    sent = recorder.messages[0]
    zone = screen.Main.encoder_value(2)[0]
    check_equal(
        sent,
        (0xF0, 0x08, 0x26, 0x21, 0x00, zone, 1, midi.ATTR_VALUE, 90, 0xF7),
        "value message payload",
    )


def test_invalidate_resends_everything():
    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()
    content = sample_content()
    view.render(content)
    total = model.flush()

    model.invalidate()
    view.forget()
    view.activate()
    recorder.clear()
    view.render(content)
    resent = model.flush()
    check_equal(resent, total, "invalidate + redraw must re-send exactly the full screen")


def test_forget_is_required_after_invalidate():
    """Guards the trap the docstring warns about: invalidating the model without
    clearing the view memo leaves the device blank."""
    _recorder, model = make_model()
    view = display.MainView(model)
    view.activate()
    content = sample_content()
    view.render(content)
    model.flush()

    model.invalidate()
    # Deliberately NOT calling view.forget()
    view.render(content)
    check(
        model.pending_count() > 0,
        "model should still know a resend is pending even if the view short-circuits",
    )


def test_suspend_blocks_output_and_redraw_recovers():
    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()
    content = sample_content()

    model.set_suspended(True)
    view.render(content)
    check_equal(model.flush(), 0, "nothing may be sent while feedback is suspended")
    check_equal(len(recorder.messages), 0, "recorder must be empty while suspended")

    # Resume the way the control surface does: unsuspend, invalidate, forget, redraw.
    model.set_suspended(False)
    model.invalidate()
    view.forget()
    view.activate()
    view.render(content)
    check(model.flush() > 20, "the post-suspend redraw must repaint the whole screen")


def test_unassigned_tiles_are_greyed_not_hidden():
    """The factory greys an unassigned slot; it never hides it. If we hide the label
    instead, a shorter bank leaves ghost text from the previous device."""
    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()
    tiles = [display.EncoderTile(label="Freq", value=10, assigned=True)] + [
        display.EncoderTile() for _ in range(7)
    ]
    view.render(display.MainContent(title="Test", tiles=tuple(tiles)))
    model.flush()

    label_zone = screen.Main.encoder_label(5)[0]
    label_visible = [
        m
        for m in recorder.messages
        if len(m) > 7 and m[5] == label_zone and m[6] == 2 and m[7] == midi.ATTR_VISIBLE
    ]
    check_equal(label_visible[0][8], 1, "an unassigned encoder label must stay visible")

    label_colour = [
        m
        for m in recorder.messages
        if len(m) > 7 and m[5] == label_zone and m[6] == 2 and m[7] == midi.ATTR_COLOR
    ]
    check_equal(
        tuple(label_colour[0][8:11]),
        screen.Palette.DISABLED,
        "an unassigned encoder label must use the DISABLED grey",
    )

    halo_visible = [
        m
        for m in recorder.messages
        if len(m) > 7 and m[5] == label_zone and m[6] == 1 and m[7] == midi.ATTR_VISIBLE
    ]
    check_equal(halo_visible[0][8], 0, "an unassigned encoder halo must be hidden")


def test_soft_button_rows_and_encoder_zones():
    """Row order and tile zones, per skin.xml and the screen map. Getting these
    backwards puts content on the wrong half of the screen."""
    check_equal(screen.Main.soft_button_label(0), (1, 1), "soft button 0 -> header zone 1")
    check_equal(screen.Main.soft_button_label(3), (1, 4), "soft button 3 -> header zone 1")
    check_equal(screen.Main.soft_button_label(4), (13, 1), "soft button 4 -> footer zone 13")
    check_equal(screen.Main.soft_button_label(7), (13, 4), "soft button 7 -> footer zone 13")

    check_equal(screen.Main.encoder_label(0), (3, 2), "encoder 0 label")
    check_equal(screen.Main.encoder_label(3), (6, 2), "encoder 3 label")
    check_equal(screen.Main.encoder_label(4), (8, 2), "encoder 4 label (bottom row starts at zone 8)")
    check_equal(screen.Main.encoder_label(7), (11, 2), "encoder 7 label")


def test_text_is_compactified_on_the_wire():
    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()
    view.render(
        display.MainContent(
            title="Glue Compressor",
            tiles=tuple(
                [display.EncoderTile(label="Filter Freq", value=0, assigned=True)]
                + [display.EncoderTile() for _ in range(7)]
            ),
        )
    )
    model.flush()

    def text_at(zone, element):
        for message in recorder.messages:
            if len(message) > 7 and message[5] == zone and message[6] == element and message[7] == midi.ATTR_TEXT:
                return "".join(chr(b) for b in message[8:-1])
        return None

    # Template 0's title uses the *wide* budget: the header's right half belongs to the top
    # soft-button labels, which Plugin mode leaves blank, so "Track | Device" fits.
    check_equal(text_at(1, 5), "Glue Compressor", "title uses the full header width")
    check_equal(
        formatting.compactify("Glue Compressor", formatting.MAXCHARS_HEADER_TITLE),
        "GlueCompresso",
        "for contrast: the factory's 13-char budget would have squeezed it",
    )
    check_equal(text_at(3, 2), "FiltFre", "encoder label must be compactified to 7 chars")


def test_teardown_matches_the_factory_release_state():
    """Values taken from a MIDI capture of a Studio Pro shutdown.

    The device is released to *empty text, white, visible, regular font* — NOT blanked to
    black and hidden. Blanking left the Motion dark after unload, because its standalone UI
    draws into the same persistent screen elements.
    """
    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()
    view.render(sample_content())
    model.flush()

    recorder.clear()
    sent = model.reset_to_defaults()
    check(sent > 20, f"the release should touch everything it drew, sent {sent}")

    seen = set()
    for message in recorder.messages:
        if message[3] != midi.MSG_SCREEN_UPDATE:
            continue
        attr = message[7]
        payload = tuple(message[8:-1])
        seen.add(attr)
        if attr == midi.ATTR_TEXT:
            check_equal(payload, (), f"released text must be empty: {message}")
        elif attr == midi.ATTR_COLOR:
            check_equal(payload, midi.RESET_COLOR, "released colour must be white (7F 7F 7F)")
        elif attr == midi.ATTR_VISIBLE:
            check_equal(payload, (1,), "released elements must stay VISIBLE, not hidden")
        elif attr == midi.ATTR_FONT:
            check_equal(payload, (0,), "released font must be regular")
        elif attr == midi.ATTR_VALUE:
            check_equal(payload, (0,), "released value must be 0")

    check(midi.ATTR_TEXT in seen and midi.ATTR_COLOR in seen and midi.ATTR_VISIBLE in seen,
          "the release should cover text, colour and visibility")
    check_equal(model.flush(), 0, "nothing should remain pending after the release")


def test_led_release_values_are_white_not_black():
    """Same capture: state 0 on channel 1, 127 on channels 2/3/4."""
    check_equal(midi.RESET_LED_STATE, 0, "LED state goes off")
    check_equal(midi.RESET_RGB, 0x7F, "LED colour goes to full white, not black")
    check_equal(midi.RESET_COLOR, (0x7F, 0x7F, 0x7F), "screen colour release is white")
    check_equal(midi.RESET_VISIBLE, 1, "screen elements are left visible")

    # The address list must cover what the capture showed, including the strip LED ranges.
    for address in (0x37, 0x3F, 0x70, 0x78, 0x1D, 0x00, 0x07, 0x6F):
        check(
            address in midi.LED_ADDRESSES_TO_CLEAR,
            f"LED release should cover {address:#02x}",
        )


def test_every_address_is_real():
    """Cross-check the renderer against the extracted device address map."""
    path = next((p for p in CSV_CANDIDATES if os.path.exists(p)), None)
    if path is None:
        print("    ! skipped: Motion32_Screen_Template_Map.csv not found")
        return

    attr_names = {
        midi.ATTR_TEXT: "text",
        midi.ATTR_COLOR: "color",
        midi.ATTR_VALUE: "value",
        midi.ATTR_VISIBLE: "visible",
        midi.ATTR_FONT: "font",
    }

    known = set()
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            known.add(
                (int(row["template"]), int(row["zone"]), int(row["element"]), row["attr"].strip())
            )

    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()
    view.render(sample_content())
    model.flush()

    # Template 3 as well — a whole second set of addresses.
    params = display.ParamsView(model)
    params.activate()
    params.render(sample_params_content())
    model.flush()

    # Template 2 — the mixer strips. A third set, and the newest, so the most likely to
    # contain a typo that would simply do nothing on the device.
    mixer = display.MixerView(model)
    mixer.activate()
    mixer.render(sample_mixer_content())
    model.flush()

    unknown = []
    for message in recorder.messages:
        if message[3] != midi.MSG_SCREEN_UPDATE:
            continue
        template, zone, element, attr = message[4], message[5], message[6], message[7]
        key = (template, zone, element, attr_names.get(attr, str(attr)))
        if key not in known:
            unknown.append(key)

    check_equal(
        unknown,
        [],
        "renderer wrote addresses/attributes the device does not document",
    )
    print(f"    (validated against {len(known)} documented attribute handlers)")


def test_identity_reply_parsing():
    """The exact bug this pass fixes: firmware read from fixed offsets, not the tail."""
    reply = (0xF0, 0x7E, 0x7F, 0x06, 0x02, 0x08, 0x00, 0x00, 0x26, 0x00, 0x00, 0x01, 0x00, 0x06, 0xF7)
    info = protocol.parse_identity_reply(reply)
    check(info is not None, "the real Motion identity reply must parse")
    check_equal(info.firmware_major, 1, "major")
    check_equal(info.firmware_minor, 0, "minor")
    check_equal(info.firmware_patch, 6, "patch")
    check_equal(info.version, "1.0.6", "version string")
    check_equal(info.version_code, 1006, "version code (major*1000 + concat(minor,patch))")
    check(
        info.version_code >= midi.REQUIRED_FIRMWARE_VERSION,
        "1.0.6 must satisfy the 1003 minimum — the old code reported 10 and warned",
    )
    check_equal(info.manufacturer_id, 0x08, "Fender manufacturer id")

    # BCD-style decode: 0x10 reads as ten, not sixteen.
    bcd = (0xF0, 0x7E, 0x7F, 0x06, 0x02, 0x08, 0, 0, 0x26, 0, 0, 0x01, 0x10, 0x02, 0xF7)
    info = protocol.parse_identity_reply(bcd)
    check_equal(info.firmware_minor, 10, "0x10 must decode to 10 (BCD-style), not 16")
    check_equal(info.version_code, 1102, "1.10.2 -> 1000 + int('102')")

    check_equal(protocol.parse_identity_reply((0xF0, 0x7E, 0x7F, 0x06, 0x02, 0xF7)), None,
                "a truncated reply must be rejected, not misread")
    check_equal(protocol.parse_identity_reply((0xB0, 0x6D, 0x7F)), None, "a CC is not a reply")


def test_suspend_gate_covers_template_select():
    """The old gate only filtered 0x21, letting a template switch through while the
    user had Global Settings open."""
    check(
        protocol.MotionProtocol._is_device_feedback(
            (0xF0, 0x08, 0x26, midi.MSG_SCREEN_TEMPLATE, 0x00, 0xF7)
        ),
        "template select must be gated while suspended",
    )
    check(
        protocol.MotionProtocol._is_device_feedback(
            (0xF0, 0x08, 0x26, midi.MSG_SCREEN_UPDATE, 0, 1, 5, 0, 0xF7)
        ),
        "element update must be gated while suspended",
    )
    check(
        not protocol.MotionProtocol._is_device_feedback(midi.NATIVE_MODE_OFF_MESSAGE),
        "the native-mode goodbye must never be gated",
    )
    check(
        not protocol.MotionProtocol._is_device_feedback((0xB0, midi.CC_PLAY, 127)),
        "LED writes are not screen feedback",
    )


def test_midi_constants_match_the_definition_doc():
    check_equal(midi.CC_ENCODERS, tuple(range(0x0E, 0x16)), "encoders 0x0E-0x15")
    check_equal(midi.CC_ENCODER_TOUCH, tuple(range(0x70, 0x78)), "encoder touch 0x70-0x77")
    check_equal(midi.CC_LCD_BUTTONS, tuple(range(0x24, 0x2C)), "LCD soft buttons 0x24-0x2B")
    check_equal(
        (midi.CC_NAV_UP, midi.CC_NAV_DOWN, midi.CC_NAV_LEFT, midi.CC_NAV_RIGHT),
        (0x57, 0x59, 0x5A, 0x66),
        "navigation is deliberately non-contiguous",
    )
    check_equal(
        (midi.CC_TAP, midi.CC_RECORD, midi.CC_PLAY, midi.CC_STOP),
        (0x69, 0x6B, 0x6D, 0x6F),
        "native-mode transport",
    )
    check_equal(
        (midi.CC_TOUCHSTRIP_1_BUTTON, midi.CC_TOUCHSTRIP_2_BUTTON),
        (0x7A, 0x7B),
        "touch-strip buttons (found in the surface XML)",
    )
    check_equal((midi.LED_OFF, midi.LED_DIM, midi.LED_ON), (0, 63, 127), "LED brightness model")
    check_equal(screen.Palette.HEADER_BACKGROUND, (0, 52, 102), "#0069CC -> 7-bit")
    check_equal(screen.Palette.STOP_ACTIVE, (127, 82, 0), "orange -> 7-bit")


# ---------------------------------------------------------------------------
# Colour translation (roadmap Phase 4)
# ---------------------------------------------------------------------------


class FakeColoured:
    """Stand-in for a Live track / clip / scene.

    The LOM gives `color` as `0x00rrggbb` = (2**16 * red) + (2**8 * green) + blue, each
    component 0-255. Access is get/set/**observe**, so a colour change is subscribable.
    """

    def __init__(self, color=0x0069CC):
        self.color = color


def test_rgb7_matches_the_lom_colour_format():
    """`0x00rrggbb`, 8-bit per channel, to the device's 7 bits."""
    check_equal(palette.rgb7(0x000000), (0, 0, 0), "black")
    check_equal(palette.rgb7(0xFFFFFF), (127, 127, 127), "white is the 7-bit maximum")
    check_equal(palette.rgb7(0xFF0000), (127, 0, 0), "pure red stays in the red channel")
    check_equal(palette.rgb7(0x00FF00), (0, 127, 0), "pure green")
    check_equal(palette.rgb7(0x0000FF), (0, 0, 127), "pure blue")
    check_equal(palette.rgb7(0x0069CC), (0, 52, 102), "the factory blue #0069CC")
    # Channel independence: a value in one channel must not leak into another.
    check_equal(palette.rgb7(0x123456), (0x12 >> 1, 0x34 >> 1, 0x56 >> 1), "channels are independent")
    # The LOM's documented arithmetic form, not just the hex form.
    packed = (2 ** 16) * 200 + (2 ** 8) * 100 + 50
    check_equal(palette.rgb7(packed), (100, 50, 25), "(2**16 * r) + (2**8 * g) + b")


def test_live_colours_need_no_lookup_table():
    """The Phase 4 requirement: an arbitrary user-chosen colour must work.

    Nothing may depend on the colour appearing in a palette or a nearest-match table — the
    named `screen.Palette` entries are device chrome only.
    """
    for value in (0x000000, 0x010203, 0x7F7F7F, 0xABCDEF, 0xFFFFFF, 0xFF00AA, 0x00FF7B):
        expected = ((value >> 16 & 0xFF) >> 1, (value >> 8 & 0xFF) >> 1, (value & 0xFF) >> 1)
        check_equal(
            palette.live_rgb7(FakeColoured(value)),
            expected,
            f"arbitrary Live colour {value:#08x} converts without a lookup table",
        )


def test_a_black_live_object_is_black_not_missing():
    """`0` is a real colour. The obvious truthiness test would silently default it.

    This is the bug this assertion exists to prevent: `if not colour:` treats black exactly
    like an absent colour, so every black-coloured track would quietly render as the fallback.
    """
    check_equal(palette.live_rgb7(FakeColoured(0x000000)), (0, 0, 0), "black converts to black")
    check_equal(
        palette.live_rgb7(FakeColoured(0x000000), default=(9, 9, 9)),
        (0, 0, 0),
        "a black object must not fall back to the default",
    )


def test_live_rgb7_handles_objects_with_no_colour():
    sentinel = (1, 2, 3)
    check_equal(palette.live_rgb7(None, default=sentinel), sentinel, "no object")
    check_equal(palette.live_rgb7(object(), default=sentinel), sentinel, "no .color attribute")
    check_equal(
        palette.live_rgb7(FakeColoured(None), default=sentinel),
        sentinel,
        "an uncoloured scene / empty clip slot",
    )
    check_equal(
        palette.live_rgb7(FakeColoured("not a colour"), default=sentinel),
        sentinel,
        "a non-numeric colour does not raise",
    )
    check_equal(palette.live_rgb7(None), None, "the default default is None")


def test_live_rgb7_survives_a_deleted_live_object():
    """A deleted Live object raises RuntimeError on *attribute access*, not just on use.

    So guarding only the int() conversion is not enough — the getattr itself throws, and an
    exception here would propagate into a Live listener and wedge the render.
    """

    class Dead:
        @property
        def color(self):
            raise RuntimeError("this object is dead")

    check_equal(
        palette.live_rgb7(Dead(), default=(7, 7, 7)),
        (7, 7, 7),
        "a deleted Live object falls back instead of raising",
    )


def test_plugin_header_colour_and_text_share_one_source():
    """The Plugin header's colour and its text must come from the same track object.

    Deriving them separately lets the bar name one track while wearing another's colour —
    the same class of bug as the view/content mismatch (§6b-16).
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read())
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    check("_plugin_header_track" in functions, "there must be one source for the header track")

    device_content = functions.get("_device_content")
    check(device_content is not None, "screen_component must define _device_content")
    if device_content is None:
        return

    # Find the MainContent(...) call that carries the device title, and confirm its title and
    # header_background are both derived from the same name.
    for node in ast.walk(device_content):
        if not (isinstance(node, ast.Call) and getattr(node.func, "id", "") == "MainContent"):
            continue
        kwargs = {kw.arg: kw.value for kw in node.keywords}
        if "header_background" not in kwargs:
            continue
        title, background = ast.dump(kwargs.get("title")), ast.dump(kwargs["header_background"])
        # Either both mention the shared track variable, or both use the selected-track pair.
        shared = ("header_track" in title and "header_track" in background) or (
            "_selected_track_name" in title and "_selected_track_colour" in background
        )
        check(
            shared,
            "the header's title and header_background must derive from the same track — "
            f"got title={title[:60]}, background={background[:60]}",
        )


def test_dim_keeps_hue_and_can_floor():
    check_equal(palette.dim((100, 50, 0), 0.5), (50, 25, 0), "scales each channel")
    check_equal(palette.dim((127, 127, 127), 0.0), (0, 0, 0), "a zero factor is black")
    check_equal(palette.dim((0, 0, 0), 0.5), (0, 0, 0), "black stays black")
    check_equal(
        palette.dim((0, 52, 102), 0.05, floor=4),
        (0, 4, 5),
        "floor keeps a scaled colour visible, but does not light a dark channel",
    )
    check_equal(palette.dim((127, 127, 127), 2.0), (127, 127, 127), "clamped to 7 bits")


def _colour_at(recorder, address):
    """The last colour written to a (zone, element) address, decoded from the frames."""
    zone, element = address
    found = None
    for message in recorder.messages:
        if (
            # F0 08 26 21 <template> <zone> <element> <attr> <r> <g> <b> F7 — 12 bytes.
            len(message) == 12
            and message[3] == midi.MSG_SCREEN_UPDATE
            and message[5] == zone
            and message[6] == element
            and message[7] == midi.ATTR_COLOR
        ):
            found = (message[8], message[9], message[10])
    return found


def test_song_centre_bar_takes_the_tracks_real_colour():
    """The first consumer of the colour layer: the Song-mode centre bar.

    Selecting a differently-coloured track must repaint the bar, using the track's own
    `0x00rrggbb` rather than any table.
    """
    recorder, model = make_model()
    view = display.ParamsView(model)
    view.activate()
    view.render(display.ParamsContent(
        title="Session", centre="Lead Synth", centre_background=palette.rgb7(0xFF6600),
    ))
    model.flush()
    check_equal(
        _colour_at(recorder, screen.Params.TITLE_BAR_BACKGROUND),
        palette.rgb7(0xFF6600),
        "the centre bar carries the selected track's colour",
    )


def test_plugin_header_takes_the_tracks_real_colour():
    """Template 0's header bar carries the focused track's colour, with readable title text."""
    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()
    view.render(display.MainContent(
        title="Bass | Operator", header_background=palette.rgb7(0xFF6600),
    ))
    model.flush()
    check_equal(
        _colour_at(recorder, screen.Main.HEADER_BACKGROUND),
        palette.rgb7(0xFF6600),
        "the Plugin header carries the focused track's colour",
    )
    check_equal(
        _colour_at(recorder, screen.Main.HEADER_TITLE),
        (0, 0, 0),
        "orange is bright (luma 67 of 127), so the title flips to dark text",
    )


def test_plugin_header_falls_back_to_factory_blue():
    """No track colour keeps the factory #0069CC identity rather than going black."""
    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()
    view.render(display.MainContent(title="No device", header_background=None))
    model.flush()
    check_equal(
        _colour_at(recorder, screen.Main.HEADER_BACKGROUND),
        screen.Palette.HEADER_BACKGROUND,
        "an uncoloured track leaves the factory blue header",
    )


def test_plugin_header_title_stays_readable():
    for colour, expected, why in (
        (0xFFFF99, (0, 0, 0), "pale yellow header needs dark title text"),
        (0x0069CC, (127, 127, 127), "the factory blue keeps light title text"),
    ):
        recorder, model = make_model()
        view = display.MainView(model)
        view.activate()
        view.render(display.MainContent(title="T | D", header_background=palette.rgb7(colour)))
        model.flush()
        check_equal(_colour_at(recorder, screen.Main.HEADER_TITLE), expected, why)


def test_plugin_header_has_one_owner():
    """`paint_chrome` must not also write the header background or title colour."""
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "display.py"), encoding="utf-8").read())
    classes = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)}

    # Only MainView's header is dynamic. ParamsView (Song mode) keeps the factory blue, because
    # its header names the Live *view* ("Session" / "Arrangement"), not a track — so its
    # paint_chrome legitimately still owns HEADER_BACKGROUND.
    main_view = classes.get("MainView")
    check(main_view is not None, "display.py must define MainView")
    if main_view is None:
        return
    chrome = next(
        (n for n in ast.walk(main_view) if isinstance(n, ast.FunctionDef) and n.name == "paint_chrome"),
        None,
    )
    check(chrome is not None, "MainView must define paint_chrome")
    if chrome is None:
        return

    written = {
        node.args[0].attr
        for node in ast.walk(chrome)
        if isinstance(node, ast.Call)
        and getattr(node.func, "attr", "") == "color"
        and node.args
        and isinstance(node.args[0], ast.Attribute)
    }
    for owned in ("HEADER_BACKGROUND", "HEADER_TITLE"):
        check(
            owned not in written,
            f"MainView.paint_chrome must not set the colour of {owned} — it is dynamic now "
            f"(the header follows the track, the title must contrast with it), so render() owns it",
        )


def test_song_centre_bar_falls_back_to_factory_grey():
    """No track, or a track with no colour, keeps the factory look rather than going black."""
    recorder, model = make_model()
    view = display.ParamsView(model)
    view.activate()
    view.render(display.ParamsContent(title="Session", centre="", centre_background=None))
    model.flush()
    check_equal(
        _colour_at(recorder, screen.Params.TITLE_BAR_BACKGROUND),
        screen.Palette.PLUGIN_TITLE_BACKGROUND,
        "an uncoloured track leaves the factory grey bar",
    )


def test_centre_bar_text_stays_readable_on_a_pale_track():
    """Live's track colours are user-chosen and include very light ones.

    Fixed white text on pale yellow is unreadable *and fails silently* — the element is drawn,
    it just can't be seen. The text colour is therefore derived from the background.
    """
    for colour, expected, why in (
        (0xFFFF99, (0, 0, 0), "pale yellow needs dark text"),
        (0xFFFFFF, (0, 0, 0), "white needs dark text"),
        (0x101010, (127, 127, 127), "near-black needs light text"),
        (0x0069CC, (127, 127, 127), "a saturated blue is dark, despite a high blue channel"),
    ):
        recorder, model = make_model()
        view = display.ParamsView(model)
        view.activate()
        view.render(display.ParamsContent(
            title="Session", centre="Track", centre_background=palette.rgb7(colour),
        ))
        model.flush()
        check_equal(_colour_at(recorder, screen.Params.TITLE_BAR_TEXT), expected, why)


def test_text_on_weights_by_perceived_brightness():
    """A raw channel sum would call pure blue 'light'. Luma weights are why it doesn't."""
    check_equal(palette.text_on((0, 0, 127)), (127, 127, 127), "pure blue is dark")
    check_equal(palette.text_on((0, 127, 0)), (0, 0, 0), "pure green is light")
    check(
        palette.luminance((0, 127, 0)) > palette.luminance((0, 0, 127)),
        "green must read brighter than blue, or the threshold means nothing",
    )


def test_centre_bar_has_one_owner():
    """`paint_chrome` must not also write the centre-bar background.

    It is dynamic now, so chrome writing it too would be two code paths to one element — the
    thing the one-owner rule exists to prevent, and it would fight the track colour on every
    mode switch.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "display.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    chrome = next(
        (n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "paint_chrome"
         and any("TITLE_BAR" in ast.dump(c) for c in ast.walk(n))),
        None,
    )
    check(
        chrome is None,
        "paint_chrome must not write TITLE_BAR_BACKGROUND — render() owns it now",
    )


def test_track_colour_is_followed_live():
    """`color` is an observable LOM property, so a recolour should repaint immediately.

    Without the listener the bar would only catch up when some unrelated event happened to
    trigger a render — the same "updates sometime later" symptom the name listener fixed.
    """
    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    for needed in ("add_color_listener", "color_has_listener", "remove_color_listener"):
        check(needed in source, f"the selected track's colour needs {needed} to update live")
    check(
        "live_rgb7" in source,
        "the content source must read the track's real colour through the shared layer",
    )


def test_views_reject_the_other_templates_content():
    """A view handed the wrong content must fail, not draw a plausible-looking wrong screen.

    `MainContent` and `ParamsContent` share field names (`title`, `centre`, `tiles`,
    `soft_labels`), so duck typing let a mismatch render *almost* correctly and go unnoticed —
    until a field was added to one of them and every render raised `AttributeError` instead.
    The underlying cause was two predicates disagreeing (see
    `test_view_and_content_use_one_predicate`); this is the backstop.
    """
    _, model = make_model()
    main, params = display.MainView(model), display.ParamsView(model)

    for view, wrong, name in (
        (params, display.MainContent(title="x"), "ParamsView"),
        (main, display.ParamsContent(title="x"), "MainView"),
    ):
        try:
            view.render(wrong)
        except TypeError:
            check(True, f"{name} rejects the other template's content")
        else:
            check(False, f"{name} silently accepted the wrong content type")

    # ...and still accepts its own.
    check(main.render(display.MainContent(title="ok")) is True, "MainView renders MainContent")
    check(
        params.render(display.ParamsContent(title="ok")) is True,
        "ParamsView renders ParamsContent",
    )


def test_view_and_content_use_one_predicate():
    """Which layer is on screen must be decided in exactly one place.

    🐛 The view was chosen from `self._mode`, while the content was chosen from `self._mode`
    **and** `self._modes is not None`. Before the modes component binds, `_mode` is `""` — so
    the Params view was handed Main content on every render during setup.

    The first fix gave both functions the same two predicates and asserted they were called
    in the same *order*. That held for three layers and stopped scaling at four: an ordered
    chain of `if`s is a rule a reader maintains, not one the structure enforces. Both now
    index dicts by a single key from `_screen_layer()`, so disagreement is impossible rather
    than merely tested for — and this guard checks that shape instead of the old one.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read())
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    check(
        "_screen_layer" in functions,
        "screen_component must define _screen_layer() — the one place the layer is decided",
    )
    # ⚠️ `_layer` is assigned by `Component.__init__`. Naming this method `_layer` would
    # shadow a framework attribute and fail the build outright (see COMPONENT_RESERVED_NAMES).
    check(
        "_layer" not in functions,
        "the layer method must not be called _layer — Component.__init__ owns that name",
    )

    for name in ("_content", "_view_for_mode"):
        node = functions.get(name)
        check(node is not None, f"screen_component must define {name}")
        if node is None:
            continue
        calls = [
            n.func.attr
            for n in ast.walk(node)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
        ]
        check(
            "_screen_layer" in calls,
            f"{name}() must dispatch on _screen_layer(), not on its own test — two "
            f"decisions is how the view and the content came to disagree",
        )
        # No mode comparison of its own: the layer key is the only input.
        compares_mode = any(
            isinstance(n, ast.Compare)
            and any(
                "_modes" in ast.dump(c) or "_mode" == getattr(c, "attr", "")
                for c in [n.left] + list(n.comparators)
            )
            for n in ast.walk(node)
        )
        check(
            not compares_mode,
            f"{name}() must not re-test the mode; that extra condition is the original bug",
        )

    # The two lookup tables must be keyed identically apart from the notification layer,
    # which `_content()` handles directly because its content is stored rather than built.
    class_body = next(
        n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)
        and n.name == "MotionScreenComponent"
    )
    tables = {}
    for node in class_body.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in ("_VIEWS", "_CONTENT"):
                    tables[target.id] = {
                        k.id for k in node.value.keys if isinstance(k, ast.Name)
                    }
    for table in ("_VIEWS", "_CONTENT"):
        check(table in tables, f"MotionScreenComponent must define {table}")
    if len(tables) == 2:
        check_equal(
            tables["_VIEWS"] - tables["_CONTENT"],
            {"NOTIFICATION_LAYER"},
            "_VIEWS and _CONTENT must agree on every mode key — a key in one and not the "
            "other is the disagreement this whole guard exists to prevent",
        )
        check_equal(
            tables["_CONTENT"] - tables["_VIEWS"],
            set(),
            "_CONTENT must not carry a layer _VIEWS cannot draw",
        )

    # And every mode the modes component can select must have a layer.
    modes = {
        key
        for key, value in MAPPINGS["Main_Modes"].items()
        if isinstance(value, dict) and key not in MAPPING_META_KEYS
    }
    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    for mode in sorted(modes):
        check(
            f'"{mode}"' in source,
            f"mode {mode!r} is selectable but screen_component never names it — it would "
            f"fall through to the Song view",
        )


def test_the_mixer_claims_every_element_on_template_2():
    """🐛 **An element nobody writes is not blank — it shows what the firmware shipped in it.**

    This is §6b-25, the bug that drew the device's own `MenuItem0`…`MenuItem5` straight through
    the notification bar. Template 2 has 137 attribute handlers across 73 elements, and the
    meters are the trap: we deliberately do **not** drive them (Studio Pro does not either),
    which is exactly the condition under which they would show whatever the firmware left
    there. They must be claimed and hidden, not skipped.
    """
    path = next((p for p in CSV_CANDIDATES if os.path.exists(p)), None)
    if path is None:
        check(False, "the template map is required to derive what must be claimed")
        return

    expected = {}
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if int(row["template"]) != screen.Mixer.template:
                continue
            expected.setdefault(
                (int(row["zone"]), int(row["element"])), set()
            ).add(row["attr"].strip())

    _, model = make_model()
    view = display.MixerView(model)
    view.activate()
    view.render(sample_mixer_content())

    written = {}
    for template, zone, element, attr in model._desired:
        if template == screen.Mixer.template:
            written.setdefault((zone, element), set()).add(attr)

    for address in sorted(expected):
        attrs = expected[address]
        got = written.get(address)
        check(
            got is not None,
            f"Template 2 element {address} is never written by the mixer view — the "
            f"firmware's own content shows through",
        )
        if got is None:
            continue
        if "text" not in attrs:
            continue
        # A text-capable element must be deliberately hidden or deliberately filled.
        hidden = model._desired.get(
            (screen.Mixer.template,) + address + (midi.ATTR_VISIBLE,)
        ) == (0,)
        filled = (screen.Mixer.template,) + address + (midi.ATTR_TEXT,) in model._desired
        check(
            hidden or filled,
            f"Template 2 element {address} can carry text, so the view must either hide it "
            f"or give it text",
        )


def _meter_key(strip, right=False, attr=midi.ATTR_VALUE):
    address = screen.Mixer.meter_right(strip) if right else screen.Mixer.meter_left(strip)
    return (screen.Mixer.template,) + address + (attr,)


def test_the_meters_render_only_where_there_is_audio():
    """Phase 7c. A meter is shown for a track that can produce audio and hidden otherwise.

    A MIDI track with no instrument has `has_audio_output == False` and reads 0.0 for ever.
    Eight strips where three sit permanently flat reads as a bug rather than as silence, and
    the CSV carries `METER_LEFT_VISIBLE` / `METER_RIGHT_VISIBLE` precisely so a strip can
    render with no meter at all. Strip 4 of the sample content is that case; strips 6-7 are
    the empty-slot case.
    """
    _, model = make_model()
    view = display.MixerView(model)
    view.activate()
    view.render(sample_mixer_content())

    for strip in range(display.MixerView.STRIP_COUNT):
        shown = strip < 6 and strip != 4
        for right in (False, True):
            check_equal(
                model._desired.get(_meter_key(strip, right, midi.ATTR_VISIBLE)),
                (1 if shown else 0,),
                f"strip {strip} meter visibility must follow whether the track makes audio",
            )
            if not shown:
                check_equal(
                    model._desired.get(_meter_key(strip, right)),
                    (0,),
                    f"strip {strip}'s hidden meter must also be zeroed — unhiding it later "
                    f"would otherwise flash a stale bar for one frame",
                )

    # Levels are Live's normalised 0.0-1.0 scaled onto the element's 0-127.
    check_equal(model._desired.get(_meter_key(0)), (round(0.30 * 127),), "strip 1 left level")
    check_equal(model._desired.get(_meter_key(2, right=True)), (round(0.99 * 127),), "strip 3 right")


def test_the_meters_are_banded_green_amber_red():
    """The colour is quantised to three bands, and that is a performance decision.

    A screen element takes one colour and one value, so a smooth gradient would mean re-sending
    the colour every frame — 16 extra messages per frame, doubling the meter traffic from the
    factory's 160/s to 320/s. Banding means the colour only becomes a *different* payload when
    a level crosses a threshold, so the desired/sent diff suppresses almost all of it.
    `test_a_steady_meter_costs_nothing_between_band_crossings` proves the consequence; this
    pins the bands themselves.
    """
    palette = screen.Palette
    check_equal(display.meter_colour(0.0), palette.METER_LOW, "silence is green")
    check_equal(
        display.meter_colour(display.METER_AMBER_AT - 0.01), palette.METER_LOW,
        "just below the amber threshold is still green",
    )
    check_equal(
        display.meter_colour(display.METER_AMBER_AT), palette.METER_HIGH,
        "the threshold itself is amber — inclusive, so a level sitting exactly on it does not "
        "flicker between bands",
    )
    check_equal(display.meter_colour(display.METER_RED_AT), palette.METER_CLIP, "the top is red")
    check_equal(display.meter_colour(1.0), palette.METER_CLIP, "full scale is red")
    check(
        display.METER_AMBER_AT < display.METER_RED_AT,
        "amber must come before red or the bands are unreachable",
    )

    _, model = make_model()
    view = display.MixerView(model)
    view.activate()
    view.render(sample_mixer_content())
    for strip, expected in ((0, palette.METER_LOW), (1, palette.METER_HIGH), (2, palette.METER_CLIP)):
        check_equal(
            model._desired.get(_meter_key(strip, attr=midi.ATTR_COLOR)),
            expected,
            f"strip {strip}'s meter must wear its band's colour",
        )


def test_a_steady_meter_costs_nothing_between_band_crossings():
    """The whole reason the colour is banded rather than continuous.

    A level that moves *within* a band must put only its two value messages on the wire, not
    six. Reintroducing a gradient — returning a colour derived from the level — makes this fail
    with three extra messages per meter per frame.
    """
    recorder, model = make_model()
    view = display.MixerView(model)
    view.activate()
    view.render(sample_mixer_content(meters=((0.20, 0.20),) + ((0.0, 0.0),) * 7))
    model.flush()

    before = len(recorder.messages)
    # Same band (green), different level: two value writes and nothing else.
    view.render(sample_mixer_content(meters=((0.25, 0.25),) + ((0.0, 0.0),) * 7))
    model.flush()
    check_equal(
        len(recorder.messages) - before,
        2,
        "a level moving within one band must cost exactly its two value messages — anything "
        "more means the colour is being re-sent every frame",
    )

    before = len(recorder.messages)
    # Cross into red: the two values, plus one colour message per meter. A screen colour is a
    # single SysEx carrying R G B as payload — unlike an LED colour, which is three separate
    # CC messages. So a crossing costs 4, not 8.
    view.render(sample_mixer_content(meters=((0.99, 0.99),) + ((0.0, 0.0),) * 7))
    model.flush()
    check_equal(
        len(recorder.messages) - before,
        4,
        "crossing a band must cost the two values plus one colour message per meter, once",
    )


def test_the_meters_have_exactly_one_owner():
    """`render()` drives the meters; `paint_chrome()` must not touch them.

    They *were* painted in chrome, hidden, while the feature was deferred. Leaving that in
    would have been a genuine two-writer fight rather than a theoretical one: chrome runs on
    every `activate()`, so every mode switch would have re-hidden a live meter.
    """
    _, model = make_model()
    view = display.MixerView(model)
    view.activate()  # chrome only, no render
    for strip in range(display.MixerView.STRIP_COUNT):
        for right in (False, True):
            for attr in (midi.ATTR_VALUE, midi.ATTR_VISIBLE, midi.ATTR_COLOR):
                check(
                    _meter_key(strip, right, attr) not in model._desired,
                    f"paint_chrome wrote meter {strip} {attr} — render() is the sole owner of "
                    f"these addresses now that they are driven",
                )


def test_a_touched_strip_shows_its_volume_instead_of_the_track_name():
    """Mix Volume page: the label carries the reading while the encoder is held.

    Template 2 gives one text element per strip and it has neither `visible` nor `color`, so
    the name and the value must share it — the same constraint that forces reveal-on-touch on
    Template 0, arrived at from the other direction. Here the name is the resting state and the
    number is the interruption.
    """
    label = lambda strip: (screen.Mixer.template,) + screen.Mixer.label(strip) + (midi.ATTR_TEXT,)

    _, model = make_model()
    view = display.MixerView(model)
    view.activate()

    view.render(sample_mixer_content())
    check_equal(
        bytes(model._desired[label(1)]).decode(), "Bass", "at rest the label is the track name"
    )

    touched = sample_mixer_content()
    strips = list(touched.strips)
    strips[1] = dataclasses.replace(strips[1], value_text="-6.0 dB", show_value=True)
    view.render(dataclasses.replace(touched, strips=tuple(strips)))
    check_equal(
        bytes(model._desired[label(1)]).decode(),
        "-6.0 dB",
        "while the encoder is touched the label shows the volume",
    )
    check_equal(
        bytes(model._desired[label(0)]).decode(),
        "Drums",
        "only the touched strip changes — the other seven keep their names",
    )

    # ⚠️ The sign must survive. `compactify` strips hyphens, which would render every
    # attenuation on the mixer as a boost; `truncate_value` exists precisely to avoid that, and
    # `ScreenModel.text` runs compactify on whatever it is handed, so the value has to arrive
    # already short enough to pass through untouched.
    check(
        "-" in bytes(model._desired[label(1)]).decode(),
        "a negative dB value must keep its minus sign on the way to the wire",
    )


def test_the_mix_reveal_ends_on_release_with_no_timeout():
    """The deliberate divergence from Plugin mode and from the Pan page.

    Both of those revert after `ACTIVE_PARAMETER_TIMEOUT` (0.75 s), because there a touch may
    not be followed by a turn and the value needs a moment to be read. On the Volume page the
    fader is on screen permanently, so the number is a precision aid while your finger is down
    — user decision, 2026-08-03.

    Structurally: the released handler must **not** schedule a hide for the Volume page, and
    `show_value` must be derived from `_touch_held` rather than from `_showing_value`. Deriving
    it is what makes "no timeout" safe — there is no flag left set and nothing to miss.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    tree = ast.parse(source)

    strip_builder = next(
        (n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "_mixer_strip"),
        None,
    )
    check(strip_builder is not None, "screen_component must define _mixer_strip")
    if strip_builder is None:
        return
    dumped = ast.dump(strip_builder)
    check(
        "_touch_held" in dumped,
        "MixerStrip.show_value must come from _touch_held — 'is the finger down' is exactly "
        "the question, and a derived answer cannot get stuck on",
    )
    check(
        "_showing_value" not in dumped,
        "the Mix reveal must NOT reuse _showing_value: that carries Plugin mode's 0.75 s "
        "revert, and the roadmap's standing warning is against reusing one event source with "
        "opposite semantics",
    )
    check(
        "truncate_value" in dumped,
        "the volume reading must go through truncate_value, not compactify — compactify "
        "strips hyphens and would flip the sign of every attenuation",
    )

    handlers = [
        n for n in ast.walk(tree)
        if isinstance(n, ast.FunctionDef) and n.name == "encoder_touch_buttons"
    ]
    released = [h for h in handlers if any(
        isinstance(d, ast.Attribute) and d.attr == "released" for d in h.decorator_list
    )]
    check(len(released) == 1, "expected exactly one released handler")
    if not released:
        return
    body = ast.dump(released[0])
    check("_render" in body, "the released handler must repaint so the name comes back")
    # It may still call `_schedule_hide` — the Pan page needs it — but the Volume branch must
    # return before reaching it.
    volume_branch_returns = "MIX_PAGE_PAN" in body and "Return" in body
    check(
        volume_branch_returns,
        "the released handler must return early on the Volume page, before the timeout that "
        "the Pan page uses",
    )


def test_every_late_bound_handle_is_actually_bound():
    """🐛 **Scale mode changed the screen and not a single note.**

    `screen_component` held `self._keyboard = None` and nothing ever assigned it, so
    `_push_scale_layout` hit `if keyboard is None: return` on every scale change and the pads went
    on playing the piano. The LEDs still redrew — they fall back to `pads.pad_pitches()` — which is
    exactly what made it look like the feature worked. Found on hardware 2026-08-03.

    Two failures in one: a handle declared but never wired, and a guard that turned that into
    *no symptom at all*. This checks the first; the second is now a `logger.warning`.

    The rule: every `self._x = None` in the screen component that a `bind_*` method is supposed to
    fill must actually be filled by `_bind_screen_sources`.
    """
    import ast

    screen_src = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    surface_src = open(os.path.join(SCRIPT_DIR, "__init__.py"), encoding="utf-8").read()
    screen_tree = ast.parse(screen_src)

    binders = {
        n.name
        for n in ast.walk(screen_tree)
        if isinstance(n, ast.FunctionDef) and n.name.startswith("bind_")
    }
    check(len(binders) >= 6, f"expected several bind_* methods, found {sorted(binders)}")

    surface_tree = ast.parse(surface_src)
    setup = next(
        (
            n
            for n in ast.walk(surface_tree)
            if isinstance(n, ast.FunctionDef) and n.name == "_bind_screen_sources"
        ),
        None,
    )
    check(setup is not None, "__init__.py must define _bind_screen_sources")
    if setup is None:
        return
    called = {
        n.func.attr
        for n in ast.walk(setup)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
    }
    missing = sorted(binders - called)
    check_equal(
        missing, [],
        "these bind_* methods exist on the screen component but nothing in "
        "_bind_screen_sources calls them — the feature they feed will be silently inert",
    )


def test_the_pad_layout_is_regenerated_not_captured():
    """🐛 **A-H did nothing in Scale mode: the layout was handed over as a finished list.**

    `_recompute()` re-used that list, so banking moved `root_offset` and the pitches sat still.
    Three symptoms from one cause, and the middle one is the tell: the pitch did not shift, the
    LEDs did not shift *on the bank press*, and then they did shift after a pad press — because a
    second painter was recomputing the layout independently.

    A layout that depends on state must be **regenerated from that state**, not captured once.
    So the keyboard takes a provider it calls on every recompute, and the LED painter reads the
    roles the keyboard reports rather than deriving its own.
    """
    import ast

    keyboard_src = open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read()
    tree = ast.parse(keyboard_src)
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    check(
        "set_layout_provider" in functions,
        "the keyboard must accept a layout *provider*; a finished list cannot follow A-H",
    )
    check(
        "set_scale_pitches" not in functions,
        "set_scale_pitches took a frozen list and is the bug — it must not come back",
    )

    recompute = functions.get("_recompute")
    check(recompute is not None, "keyboard must define _recompute")
    if recompute is not None:
        dumped = ast.dump(recompute)
        check(
            "_layout_provider" in dumped,
            "_recompute must consult the layout provider, or a new layout is never generated",
        )
        # And it must pass the *current* offsets, not stored ones.
        check(
            "root_offset" in dumped and "_octave_semitones" in dumped,
            "_recompute must hand the provider the current A-H and Octave offsets — those are "
            "exactly what changed",
        )

    # The screen component supplies it, and does so from one place.
    screen_src = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    screen_functions = {
        n.name for n in ast.parse(screen_src).body[0].body
        if isinstance(n, ast.FunctionDef)
    } if False else {
        n.name for n in ast.walk(ast.parse(screen_src)) if isinstance(n, ast.FunctionDef)
    }
    check("_layout_for" in screen_functions, "the screen component must provide the layout")
    check(
        "_push_scale_layout" not in screen_functions,
        "_push_scale_layout pushed a captured list — replaced by the provider",
    )


def test_switching_view_forgets_so_a_shared_template_repaints():
    """🐛 **The scale menu stayed invisible after a notification.**

    Both live on Template 1. The bar hides the twelve rows to draw itself; returning to the menu
    found *identical* content, so `render()` short-circuited and the rows were never re-shown —
    `activate()` paints chrome, but row visibility is set in `render()`.

    This is the trap the roadmap already names for `MainView` (*"reset forget() at the same time
    or the view short-circuits on an unchanged snapshot"*); sharing a template is what made it
    reachable. Forgetting on every view change is free, because the model's diff still sends only
    the difference.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    render = next(
        (
            n
            for n in ast.walk(ast.parse(source))
            if isinstance(n, ast.FunctionDef) and n.name == "_render"
        ),
        None,
    )
    check(render is not None, "screen_component must define _render")
    if render is None:
        return
    dumped = ast.dump(render)
    check(
        "forget" in dumped,
        "_render must forget() a view as it becomes active, or a shared template can strand it",
    )
    check(
        "activate" in dumped,
        "_render must still activate the incoming view",
    )

    # Behavioural: the bar hides the rows, the menu shows them again.
    _, model = make_model()
    bar = notification.NotificationView(model)
    menu_view = menu.MenuView(model)
    content = menu.MenuContent(
        title="Scales", rows=("Major", "Dorian"), selected=0,
        soft_labels=("", "", "", "Locked", "Main", "Modes", "", "Key"),
    )
    menu_view.activate()
    menu_view.render(content)
    row0 = (screen.Menu.template,) + screen.Menu.row(0, 0) + (midi.ATTR_VISIBLE,)
    check_equal(model._desired.get(row0), (1,), "the menu shows its rows")

    bar.activate()
    bar.render(notification.NotificationContent(title="Root", value="+1"))
    check_equal(model._desired.get(row0), (0,), "the bar hides them")

    # Coming back with *identical* content must still restore them — which is what forget() buys.
    menu_view.forget()
    menu_view.activate()
    menu_view.render(content)
    check_equal(
        model._desired.get(row0), (1,),
        "after forget(), returning to the menu re-shows the rows even though nothing changed",
    )


def test_scale_mode_raises_no_notifications():
    """Scale mode must not use the transient bar — **it shares Template 1 with the menu.**

    The bar blanks the twelve menu rows and writes its own header slots. A notification raised
    from Scale mode would therefore wipe the very list being scrolled, once per detent. The two
    views coexist only because they are never wanted at the same time.

    (Octave and A–H still notify. Those have no permanent home on screen, which is what the bar
    is for.)
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "scalemode.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    names = {
        n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)
    } | {
        n.id for n in ast.walk(tree) if isinstance(n, ast.Name)
    }
    for forbidden in ("notify", "_notify", "set_notification_listener", "_on_notification"):
        check(
            forbidden not in names,
            f"scalemode.py references {forbidden!r} — Scale mode must not raise notifications, "
            f"because the bar and the scale menu are on the same template",
        )

    surface = open(os.path.join(SCRIPT_DIR, "__init__.py"), encoding="utf-8").read()
    check(
        "scale.set_notification_listener" not in surface,
        "the surface must not wire a notification listener to the scale component",
    )


def test_the_scale_table_matches_the_factory():
    """15 scales, decoded from the factory's own `.musicalscale` files.

    Indices are `PreSonus.MusicalScaleID` and must not be renumbered — they are how the Motion's
    own menu, the firmware strings and our table refer to the same thing.
    """
    check_equal(len(scales.SCALES), 15, "the factory ships exactly 15 scales")
    for scale_id, (name, degrees) in scales.SCALES.items():
        check(0 <= scale_id <= 14, f"scale id {scale_id} is outside the SDK enum")
        check(bool(name), f"scale {scale_id} has no name")
        check_equal(degrees[0], 0, f"{name} must start on its root")
        check_equal(
            list(degrees), sorted(set(degrees)),
            f"{name}'s degrees must be strictly ascending and unique",
        )
        check(
            all(0 <= d < 12 for d in degrees),
            f"{name} has a degree outside one octave — the period is the scale, not the span",
        )
    # Spot-check the three that carry the most weight elsewhere.
    check_equal(scales.SCALES[1][1], (0, 2, 4, 5, 7, 9, 11), "Major")
    check_equal(scales.SCALES[6][1], (0, 3, 5, 7, 10), "Minor Pentatonic")
    check_equal(scales.SCALES[0][1], tuple(range(12)), "Chromatic is all twelve")

    # An unknown id degrades to Chromatic, which is the factory's own fallback for an
    # unrecognised title — every note is in a chromatic scale, so a bad id means "no filtering"
    # rather than an empty keybed.
    check_equal(scales.scale_degrees(99), tuple(range(12)), "unknown id falls back to Chromatic")


def test_a_locked_scale_layout_can_never_repeat_a_pitch():
    """🔑 **The invariant the factory's one-lane collapse exists to buy.**

    16 consecutive ascending degrees on one lane cannot duplicate a pitch, for any scale length
    — 3 for the triads, 12 for chromatic. This is what dissolved the duplicate-pitch problem: the
    naive two-lane pentatonic that produced fifteen collisions was solving a problem the factory
    does not have.

    Exhaustive rather than sampled, because "impossible by construction" is the claim.
    """
    violations = []
    for scale_id, (name, _degrees) in scales.SCALES.items():
        for root in range(12):
            for octaves in range(-3, 4):
                for degree_offset in range(-4, 4):
                    lane = [
                        p for p in
                        scales.locked_pitches(scale_id, root, octaves * 12, degree_offset)[:16]
                        if p is not None
                    ]
                    if len(set(lane)) != len(lane):
                        violations.append(f"{name} root={root} oct={octaves}: duplicate pitch")
                    if any(b <= a for a, b in zip(lane, lane[1:])):
                        violations.append(f"{name} root={root} oct={octaves}: not ascending")
    check_equal(
        violations[:5], [],
        f"a locked scale layout must be strictly ascending and duplicate-free "
        f"({len(violations)} violations)",
    )

    # The top lane is dead, and dead by being None — which is what gives it every dead-pad
    # behaviour for free (`keyboard._is_dead` is `pitches[i] is None`).
    for scale_id in scales.SCALES:
        top = scales.locked_pitches(scale_id, 0)[16:]
        check_equal(
            list(top), [None] * 16,
            f"scale {scale_id}: the top lane must be entirely dead, as the factory does it",
        )


def test_the_scale_spans_match_the_documented_figures():
    """§5.3c measured the span a scale layout buys. Checking the code agrees with the doc.

    "Major covers 26 semitones across the 16 pads, the pentatonics 36, and the triad 'scales' 60."
    If these drift, either the generator or the doc is wrong and the mismatch should be loud.
    """
    def span(scale_id):
        lane = [p for p in scales.locked_pitches(scale_id, 0)[:16] if p is not None]
        return lane[-1] - lane[0]

    check_equal(span(1), 26, "Major spans 26 semitones across the 16 pads (§5.3c)")
    check_equal(span(5), 36, "Major Pentatonic spans 36 (§5.3c)")
    check_equal(span(6), 36, "Minor Pentatonic spans 36 (§5.3c)")
    check_equal(span(13), 60, "Major Triad spans 60 (§5.3c)")
    check(
        span(0) < span(1),
        "Chromatic must be the narrowest — 16 consecutive semitones",
    )


def test_guide_keeps_the_piano_and_only_changes_the_lighting():
    """⚠️ **`Guide` is a lighting change, not a layout change.**

    It returns the *unchanged* `pads.pad_pitches()` list, so note translation, dead pads and
    held-pad feedback all keep working with no second code path. Only the roles differ: in-scale
    notes at full brightness, out-of-scale dimmed but still playable.

    A generator that produced its own pitches here would be a second opinion about what the
    keybed plays — the failure this project has now guarded against three times.
    """
    piano = pads.pad_pitches()
    roles = scales.guide_roles(piano, scale_id=1, root=0)   # C Major

    check_equal(len(roles), len(piano), "one role per pad")
    for index, (pitch, role) in enumerate(zip(piano, roles)):
        if pitch is None:
            check_equal(role, pads.ABSENT, f"pad {index} has no note, so it is absent")
        elif pitch % 12 == 0:
            check_equal(role, pads.ROOT, f"pad {index} plays C, so it is a root")

    # C Major on a piano: every white key is in the scale, every black key is out.
    for index, (pitch, role) in enumerate(zip(piano, roles)):
        if pitch is None:
            continue
        in_scale = pitch % 12 in (0, 2, 4, 5, 7, 9, 11)
        if in_scale:
            check(
                role in (pads.ROOT, pads.KEY),
                f"pad {index} ({pitch}) is in C Major and must be lit, got {role!r}",
            )
        else:
            check_equal(
                role, scales.OUT_OF_SCALE,
                f"pad {index} ({pitch}) is outside C Major and must be dimmed, not dark — "
                f"it still plays",
            )

    # ⚠️ An out-of-scale pad is NOT absent. It plays; it is only dimmer. Confusing the two would
    # silence half the keybed.
    check(
        scales.OUT_OF_SCALE != pads.ABSENT,
        "out-of-scale and absent must be different roles — one plays and one does not",
    )

    # A pentatonic leaves more out than a 7-note scale, and chromatic leaves nothing out.
    pent = scales.guide_roles(piano, scale_id=5, root=0)
    chrom = scales.guide_roles(piano, scale_id=0, root=0)
    check(
        pent.count(scales.OUT_OF_SCALE) > roles.count(scales.OUT_OF_SCALE),
        "a pentatonic must dim more pads than a major scale",
    )
    check_equal(
        chrom.count(scales.OUT_OF_SCALE), 0,
        "nothing is outside a chromatic scale",
    )


def test_every_scale_name_we_push_to_live_is_translated():
    """`song.scale_name` is writable but takes **Live's** vocabulary, not the Motion's.

    ⚠️ Writing a name Live does not recognise is silently ignored — no raise, no log — which is
    the same class of failure as an unknown `Layer` control name. So the translation is explicit,
    and a scale with no Live counterpart is **absent from the map** rather than mapped to a guess:
    absent means "do not write", which is honest, where a guess would push a name that does
    nothing and look like it worked.
    """
    for scale_id, (name, _degrees) in scales.SCALES.items():
        if name in scales.LIVE_SCALE_NAMES:
            check(
                bool(scales.LIVE_SCALE_NAMES[name]),
                f"{name} maps to an empty Live name",
            )
    # The two triads are pad layouts rather than scales and have no Live counterpart.
    for name in ("Major Triad", "Minor Triad"):
        check(
            name not in scales.LIVE_SCALE_NAMES,
            f"{name} has no scale in Live's chooser — it must not be pushed to the song",
        )
    # Everything else must be translatable, or Scale mode would silently fail to set the key.
    for scale_id, (name, _degrees) in scales.SCALES.items():
        if name in ("Major Triad", "Minor Triad"):
            continue
        check(
            name in scales.LIVE_SCALE_NAMES,
            f"{name} has no entry in LIVE_SCALE_NAMES, so selecting it would leave Live's key "
            f"untouched with nothing in the log to say why",
        )
    # The one that is genuinely renamed, and the reason this map exists at all.
    check_equal(
        scales.LIVE_SCALE_NAMES["Natural Minor"], "Minor",
        "Live calls our 'Natural Minor' simply 'Minor'",
    )


def test_the_menu_categories_cover_the_table():
    """`Main` / `Modes` / `Key` — the factory's soft-button categories (State Trace §Scale).

    `Modes` is the church-mode block the firmware carries as its own contiguous string run, with
    Ionian and Aeolian as **aliases** of Major and Natural Minor rather than extra scales.
    """
    main = scales.menu_entries(scales.CATEGORY_MAIN)
    modes = scales.menu_entries(scales.CATEGORY_MODES)
    keys = scales.menu_entries(scales.CATEGORY_KEY)

    check_equal(len(keys), 12, "Key lists the twelve roots")
    check_equal(keys[0], ("C", 0), "roots start at C = 0, matching song.root_note")

    check_equal(len(main), 7, "Main lists the seven real scales — no Chromatic, no triads")
    check_equal(len(modes), 7, "seven church modes")
    mode_names = [label for label, _ in modes]
    check_equal(
        mode_names,
        ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"],
        "the modes must be in the firmware's own order",
    )
    aliases = dict(modes)
    check_equal(aliases["Ionian"], 1, "Ionian is an alias of Major")
    check_equal(aliases["Aeolian"], 4, "Aeolian is an alias of Natural Minor")

    # Every id a menu offers must be a real scale.
    for category in (scales.CATEGORY_MAIN, scales.CATEGORY_MODES):
        for label, scale_id in scales.menu_entries(category):
            check(scale_id in scales.SCALES, f"{label} points at unknown scale {scale_id}")

    # Between them the two scale categories reach every scale **except Chromatic**, which is
    # deliberately not offered: leaving Scale mode is what selects chromatic, and the standard
    # pad layout already is one. Offering it would be a second, worse way to say the same thing.
    reachable = {i for _, i in main} | {i for _, i in modes}
    check_equal(
        sorted(set(scales.SCALES) - reachable), [scales.CHROMATIC_ID, 13, 14],
        "the menu must omit exactly Chromatic and the two triads, and offer everything else",
    )
    check(
        scales.CHROMATIC_ID not in reachable,
        "Chromatic must not be a menu entry — the standard pad layout is already chromatic",
    )
    # ⚠️ The triads are chord voicings, not scales: `(0, 4, 7)` across sixteen pads spans 60
    # semitones. They stay in `SCALES` because Phase 11's Chord engine reads its interval sets
    # from there, but offering them as scales was wrong.
    for triad in (13, 14):
        check(
            triad not in reachable,
            f"{scales.scale_name(triad)} is a chord voicing and must not be offered as a scale",
        )
    # …but it must still exist as a fallback, which is the factory's behaviour for an
    # unrecognised scale title.
    check_equal(
        scales.scale_degrees(scales.CHROMATIC_ID), tuple(range(12)),
        "Chromatic stays in the table as the fallback even though the menu omits it",
    )

    # ⚠️ **14, not the factory's 16 — a deliberate divergence.** Studio Pro's 16 are the 14
    # non-chromatic scales plus the Ionian/Aeolian aliases, triads included. Dropping the triads
    # to Chord mode costs two entries, and that is the intended trade.
    check_equal(
        len(main) + len(modes), 14,
        "7 Main + 7 Modes. The factory shows 16 because it lists the two triads as scales; we "
        "do not, so the counts differ on purpose",
    )


def test_the_octave_range_is_derived_per_scale():
    """A fixed ±3 octaves is meaningless for scales — the spans differ by a factor of four.

    A triad layout already covers 60 semitones of the 128 available before Octave touches it, so
    the limit has to come from the layout, exactly as `pads.safe_semitone_range` does for the
    piano. This is the same lesson A–H taught: `OCTAVE_LIMIT = 3` stopped being a guarantee the
    moment something else could move the window.
    """
    for scale_id, (name, _d) in scales.SCALES.items():
        low, high = scales.safe_octave_range(scale_id, root=0)
        check(low <= 0 <= high, f"{name}: the untransposed layout must itself be in range")
        # Applying the limits must keep every playable pad inside MIDI.
        for semitones in (low, high):
            lane = scales.locked_pitches(scale_id, 0, semitones)[:16]
            check(
                all(p is None or 0 <= p < 128 for p in lane),
                f"{name}: transposing by {semitones} left a pad outside MIDI",
            )
        # And going one semitone further must actually break it, or the range is too tight.
        lane = scales.locked_pitches(scale_id, 0, low - 1)[:16]
        check(
            any(p is None for p in lane),
            f"{name}: the low limit {low} is looser than it needs to be",
        )

    # The triads are the case that proves the point.
    triad = scales.safe_octave_range(13, root=0)
    major = scales.safe_octave_range(1, root=0)
    check(
        triad[1] < major[1],
        "a triad layout spans 60 semitones and must have less headroom than a major scale",
    )


def test_the_shift_overlay_consumes_every_pad_it_covers():
    """🔑 **The invariant that makes Shift+pad safe: no pad both commands and plays.**

    `ComboElement` carries `priority_increment = 0.5`, so a *bound* Shift-modified pad outranks
    the keyboard binding and takes the press. But priority is asserted by being in a live layer
    — an **unbound** modified element is not connected at all and claims nothing, so its pad
    would still sound its note while Shift was held.

    That is why the top lane goes to a Background rather than being left alone: on this surface
    "unbound" and "silent" are opposites, the same lesson the four dead keyboard pads taught
    (identifier ≥ 128 *released* them and let their raw notes loose).

    So: every one of the 32 modified pads must be claimed by exactly one binding.
    """
    import ast

    elements_source = open(os.path.join(SCRIPT_DIR, "elements.py"), encoding="utf-8").read()
    check(
        "add_modified_control(self.pads" in elements_source,
        "the pads must have a Shift-modified twin, or there is no command layer at all",
    )
    for name in ("Command_Pads", "Muted_Pads_With_Shift"):
        check(
            f'"{name}"' in elements_source,
            f"elements.py must declare the {name} submatrix",
        )

    # Both halves of the modified matrix are bound, and to different components.
    bound = {}
    for component, section in MAPPINGS.items():
        if not isinstance(section, dict):
            continue
        for key, value in section.items():
            if isinstance(value, str) and "with_shift" in value or value == "command_pads":
                bound[value] = component
    check(
        "command_pads" in bound,
        "the bottom lane of Shift pads must be bound, or Shift+pad does nothing",
    )
    check(
        "muted_pads_with_shift" in bound,
        "the TOP lane of Shift pads must be bound to something that consumes it — unbound "
        "means the accidentals keep playing while the command layer is up",
    )
    check(
        bound.get("muted_pads_with_shift") in WILDCARD_COMPONENTS,
        "the top lane must go to a Background (a NopControl grab), not to a component that "
        "would give those pads a meaning",
    )
    check_equal(
        bound.get("command_pads"),
        "Motion_Commands",
        "the command lane belongs to the commands component",
    )


def test_the_command_pads_never_write_their_own_colour():
    """`leds.PadLeds` is the single writer of all 32 pad addresses, Shift layer included.

    ⚠️ A pad's LED address **is** its note address. A `ButtonControl` with a colour on a pad
    element would write there on every layer grab, and the framework would be fighting `PadLeds`
    for sixteen addresses — the two-writer split that cost three attempts on the encoder halos
    and that `keyboard.py` avoids by leaving `_update_button_color` as the base class's empty
    hook.

    This is also the reason the framework's own `Clip_Actions` is *not* bound straight to the
    pads, despite implementing four of these commands properly: it would take ownership of four
    pad addresses and leave twenty-eight with us.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "commands.py"), encoding="utf-8").read()
    tree = ast.parse(source)

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        name = getattr(func, "id", None) or getattr(func, "attr", None)
        if name != "control_list":
            continue
        colours = [k for k in node.keywords if k.arg in ("color", "on_color", "pressed_color")]
        check(
            bool(colours),
            "the command pads must pass an explicit colour argument — the ButtonControl "
            "default is 'DefaultButton.On', which would write to the pad's note address",
        )
        for keyword in colours:
            check(
                isinstance(keyword.value, ast.Constant) and keyword.value.value is None,
                f"command pad {keyword.arg} must be None so nothing is sent — PadLeds owns "
                f"every pad address",
            )

    check(
        "Clip_Actions" not in str(MAPPINGS),
        "Clip_Actions must not be bound to the pads — it would take LED ownership of four pad "
        "addresses; see commands.py for the reasoning",
    )


def test_every_command_slot_is_labelled_and_gated():
    """Sixteen slots, six filled, and the empty ones are rendered rather than omitted.

    The roadmap's convention for an unassigned slot is **grey, not dark** — the same treatment
    the Plugin tiles give an unmapped encoder. Ten of the sixteen are empty today, so a layer
    that hid them would look like a four-pad feature and one that darkened them would look
    broken.

    Each command must also be *gated*: `Undo` with nothing to undo, or `Quantize` with no clip,
    has to say so. A pad that answers only sometimes reads as a dead pad — the same rule that
    makes A-H announce a press that changes nothing.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "commands.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    builder = functions.get("_build_commands")
    check(builder is not None, "commands.py must define _build_commands")
    if builder is None:
        return

    # Every entry is (label, handler) and every handler exists.
    entries = [n for n in ast.walk(builder) if isinstance(n, ast.Dict)]
    check(bool(entries), "_build_commands must return a slot -> (label, handler) dict")
    labels = []
    for table in entries:
        for key, value in zip(table.keys, table.values):
            check(
                isinstance(key, ast.Constant) and isinstance(key.value, int),
                "command slots must be integer indices",
            )
            check(
                0 <= key.value < 16,
                f"command slot {getattr(key, 'value', '?')} is outside the 16-pad bottom lane",
            )
            check(
                isinstance(value, ast.Tuple) and len(value.elts) == 2,
                "each command must be a (label, handler) pair",
            )
            if isinstance(value, ast.Tuple) and len(value.elts) == 2:
                label, handler = value.elts
                check(
                    isinstance(label, ast.Constant) and isinstance(label.value, str),
                    "a command label must be a literal string",
                )
                if isinstance(label, ast.Constant):
                    labels.append(label.value)
                    check(
                        0 < len(label.value) <= formatting.MAXCHARS_SOFT_BUTTON,
                        f"command label {label.value!r} must fit a soft-button slot",
                    )
                attr = getattr(handler, "attr", None)
                check(
                    attr in functions,
                    f"command handler {attr!r} is named but not defined",
                )

    check_equal(len(labels), len(set(labels)), "two command slots share a label")
    check(
        len(labels) >= 6,
        f"expected at least the six framework-backed commands, found {len(labels)}",
    )

    # Every handler returns a string on the paths where it cannot act — that is the gate.
    for name in ("_undo", "_redo", "_duplicate_clip", "_delete_clip", "_quantize_clip"):
        handler = functions.get(name)
        check(handler is not None, f"commands.py must define {name}")
        if handler is None:
            continue
        returns_a_reason = any(
            isinstance(n, ast.Return)
            and isinstance(n.value, ast.Constant)
            and isinstance(n.value.value, str)
            for n in ast.walk(handler)
        )
        check(
            returns_a_reason,
            f"{name} must return a reason string when it cannot act — a command that does "
            f"nothing and says nothing is indistinguishable from a dead pad",
        )


def test_the_meter_loop_is_gated_and_uses_the_framework_idiom():
    """The one polled source on this surface, checked structurally.

    `screen_component.py` imports the framework so the suite cannot execute it; this is the AST
    stand-in. Four properties, each of which is a bug if absent:

    1. **`task.loop`, not a self-rescheduling chain.** `_schedule_live_refresh` re-adds itself
       after each run, which is right for a 0.75 s timeout — miss a reschedule and it simply
       ends. A meter loop that misses one runs for the rest of the session showing a frozen
       bar. `task.loop` is the framework's own repeating idiom
       (`ScrollComponent._make_scroll_task`) and cannot stop by omission.
    2. **Gated on mode *and* page.** The Pan page draws Template 0, which has no meter element,
       so polling there writes to a template nobody is looking at.
    3. **Both mode and page changes drive the gate**, or entering Mix from a page change leaves
       the loop off.
    4. **`disconnect()` kills it.** A live task holding `self` through teardown is how a
       superseded instance writes to a device it no longer owns (§7).
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    for name in ("_meters_wanted", "_update_meter_task", "_start_meters", "_stop_meters", "_poll_meters"):
        check(name in functions, f"screen_component must define {name}")
    if "_start_meters" not in functions:
        return

    start = ast.dump(functions["_start_meters"])
    check(
        "'loop'" in start or '"loop"' in start,
        "the meter poll must use task.loop — a self-rescheduling chain that misses one hop "
        "leaves a frozen bar on screen for the rest of the session",
    )
    check(
        "METER_INTERVAL" in start,
        "the poll interval must come from the named constant, so a hardware run can change "
        "the rate in one place",
    )

    wanted = ast.dump(functions["_meters_wanted"])
    check("MIX_MODE" in wanted, "the meter loop must be gated on Mix mode")
    check(
        "MIX_PAGE_VOLUME" in wanted or "MIX_PAGE_PAN" in wanted,
        "the meter loop must be gated on the page too — the Pan page draws Template 0, which "
        "has no meter element at all",
    )

    for driver in ("_on_selected_mode_changed", "_on_mix_page_changed"):
        check(
            driver in functions and "_update_meter_task" in ast.dump(functions[driver]),
            f"{driver} must call _update_meter_task, or the loop's state drifts from the "
            f"screen's",
        )

    disconnect = functions.get("disconnect")
    check(
        disconnect is not None and "_meter_task" in ast.dump(disconnect),
        "disconnect() must kill the meter task — a live task holds a reference to this "
        "component through teardown",
    )

    # The poll re-checks the gate, because a page change can race the frame.
    poll = ast.dump(functions["_poll_meters"])
    check(
        "_meters_wanted" in poll,
        "_poll_meters must re-check the gate: killing the task and the next frame firing can "
        "race, and a stray frame writes meters onto whichever template is now up",
    )


def test_the_mixer_renders_strips_and_diffs():
    """Behaviour: the strips reach the wire, and a redundant render costs nothing."""
    recorder, model = make_model()
    view = display.MixerView(model)
    view.activate()
    check(view.render(sample_mixer_content()), "the first render must change something")
    model.flush()
    first = len(recorder.messages)
    check(first > 0, "the first paint must go on the wire")

    check(
        not view.render(sample_mixer_content()),
        "an identical re-render must report no change",
    )
    model.flush()
    check_equal(len(recorder.messages), first, "a redundant render must cost zero messages")

    # An unassigned strip is greyed, not hidden — and its label is *blanked*, because
    # MIXER_CHANNEL_LABEL has `text` but no `visible` and so cannot be hidden at all.
    label = (screen.Mixer.template,) + screen.Mixer.label(7) + (midi.ATTR_TEXT,)
    check_equal(model._desired.get(label), (), "an unassigned strip's label must be empty")
    check(
        (screen.Mixer.template,) + screen.Mixer.label(7) + (midi.ATTR_VISIBLE,)
        not in model._desired,
        "MIXER_CHANNEL_LABEL has no visible attribute — writing one would be an address that "
        "does nothing on the device",
    )

    # Mute and solo are `value` elements on this template, not colours.
    muted = (screen.Mixer.template,) + screen.Mixer.mute(2) + (midi.ATTR_VALUE,)
    check_equal(model._desired.get(muted), (127,), "strip 3 is muted in the sample content")
    soloed = (screen.Mixer.template,) + screen.Mixer.solo(5) + (midi.ATTR_VALUE,)
    check_equal(model._desired.get(soloed), (127,), "strip 6 is soloed in the sample content")


def test_the_mixer_marks_the_focused_strip():
    """Template 2 has no ring and no header, so focus has to live on the label swatch."""
    _, model = make_model()
    view = display.MixerView(model)
    view.activate()
    view.render(sample_mixer_content(focused=3))
    swatch = (screen.Mixer.template,) + screen.Mixer.label_background(3) + (midi.ATTR_COLOR,)
    check_equal(
        model._desired.get(swatch),
        tuple(screen.Palette.CHANNEL_LABEL_SELECTED),
        "the focused strip's swatch must be the selection blue",
    )
    other = (screen.Mixer.template,) + screen.Mixer.label_background(1) + (midi.ATTR_COLOR,)
    check(
        model._desired.get(other) != tuple(screen.Palette.CHANNEL_LABEL_SELECTED),
        "only the focused strip may wear the selection colour",
    )


def test_the_mixer_rejects_the_other_templates_content():
    """Same guard the other two views carry: content classes share field names."""
    _, model = make_model()
    view = display.MixerView(model)
    view.activate()
    for wrong in (sample_content(), sample_params_content()):
        raised = False
        try:
            view.render(wrong)
        except TypeError:
            raised = True
        check(raised, f"MixerView must refuse {type(wrong).__name__}")


def test_mix_pages_the_ring_rather_than_moving_the_selection():
    """🐛 **Left/Right in Mix mode must move the session ring, not Live's selection.**

    This shipped bound to `View_Control.prev_track_button`/`next_track_button`, which moves
    the *selected track* one at a time and never touches the ring. Three symptoms, one cause:
    the eight strips stayed put, only one track looked highlighted, and Solo/Mute — which
    follow the target (selected) track — crawled along with the selection instead of following
    the strip you touched.

    `Session_Navigation`'s **page** buttons move a whole bank of eight. Its plain
    `left_button`/`right_button` scroll by one, which is the behaviour that was wrong.
    """
    mix = MAPPINGS["Main_Modes"]["mix"]["modes"]
    nav = next((m for m in mix if m.get("component") == "Session_Navigation"), None)
    check(nav is not None, "Mix mode must bind Session_Navigation for Left/Right")
    if nav is not None:
        check_equal(
            nav.get("page_left_button"),
            "left_button",
            "Left must page the ring a whole bank",
        )
        check_equal(
            nav.get("page_right_button"),
            "right_button",
            "Right must page the ring a whole bank",
        )
        for single in ("left_button", "right_button"):
            check(
                single not in nav,
                f"Session_Navigation.{single} scrolls by one track — that is the bug this "
                f"replaced, not the fix",
            )
    check(
        not any(m.get("component") == "View_Control" for m in mix),
        "Mix mode must not move Live's selection with Left/Right — the ring is what moves",
    )

    # The ring is eight wide because the Specification says so; if that ever changed, the
    # strips and the pages would disagree.
    import ast

    display_count = display.MixerView.STRIP_COUNT
    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    strips = next(
        (
            n.value.value
            for n in ast.walk(tree)
            if isinstance(n, ast.Assign)
            and any(
                isinstance(t, ast.Name) and t.id == "MIXER_STRIP_COUNT" for t in n.targets
            )
            and isinstance(n.value, ast.Constant)
        ),
        None,
    )
    check_equal(
        strips,
        display_count,
        "the content builder and the view must agree on how many strips there are",
    )


def test_mix_focus_is_the_selection_and_never_times_out():
    """Cap-touch focuses a strip by **selecting its track**.

    The roadmap's warning for this phase: the focus must *persist*, and it must not reuse
    Plugin mode's value timeout — "the same event source with opposite semantics, which is
    exactly the kind of reuse that produces a subtle bug".

    Selecting the track avoids the trap rather than managing around it. `Target_Channel_Strip`
    already follows the target (selected) track, so Solo and Mute follow for free; a selection
    persists by definition; and the on-screen mark is *derived* from the selection rather than
    stored, so there is no second copy to drift.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    for name in ("_select_strip_track", "_focused_strip"):
        check(name in functions, f"screen_component must define {name}")

    # No stored focus: the strip mark must come from the selection.
    stored = [
        n
        for n in ast.walk(tree)
        if isinstance(n, ast.Assign)
        for t in n.targets
        if isinstance(t, ast.Attribute) and t.attr in ("_focused", "_focused_strip_index")
    ]
    check(
        not stored,
        "focus must be derived from the selected track, not stored — a second copy of a fact "
        "Live already owns is what the pad-roles bug was",
    )
    focused = functions.get("_focused_strip")
    if focused is not None:
        check(
            "selected_track" in ast.dump(focused),
            "_focused_strip must read Live's selected track",
        )

    # The touch handlers must branch on Mix and must NOT schedule the value timeout there.
    handlers = [
        n
        for n in ast.walk(tree)
        if isinstance(n, ast.FunctionDef) and n.name == "encoder_touch_buttons"
    ]
    check_equal(len(handlers), 2, "there must be a pressed and a released touch handler")
    pressed, released = handlers
    check(
        "MIX_MODE" in ast.dump(pressed),
        "the touch handler must treat Mix mode differently — it focuses, it does not reveal",
    )
    calls_hide = [
        n
        for n in ast.walk(released)
        if isinstance(n, ast.Call)
        and isinstance(n.func, ast.Attribute)
        and n.func.attr == "_schedule_hide"
    ]
    check(
        calls_hide,
        "the release handler must still start Plugin mode's value timeout",
    )
    check(
        "MIX_MODE" in ast.dump(released),
        "…but it must return early in Mix mode: a selection does not expire, and reusing the "
        "value timeout for focus is the reuse the roadmap warned about",
    )


def test_mix_halos_take_the_track_colours():
    """Eight strips, eight colours — the ring of halos says which tracks you are holding."""
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read())
    refresh = next(
        (
            n
            for n in ast.walk(tree)
            if isinstance(n, ast.FunctionDef) and n.name == "_refresh_encoder_leds"
        ),
        None,
    )
    check(refresh is not None, "screen_component must define _refresh_encoder_leds")
    if refresh is None:
        return
    dumped = ast.dump(refresh)
    check(
        "MIX_MODE" in dumped,
        "the halos must know about Mix mode, or all eight stay one colour",
    )
    check(
        "live_rgb7" in dumped,
        "Mix halos must come from the track's own colour via the shared conversion layer",
    )
    check(
        "_strip_track" in dumped,
        "each halo must read *its own* strip's track, not the focused one",
    )

    # ⚠️ The three checks above are substring checks over the function's AST dump, and a
    # disabled branch (`elif False:`) leaves every one of those names in place. Verified by
    # reintroducing exactly that and watching them all pass. So: the Mix branch's condition
    # must be a real test, not a constant.
    branch_tests = [n.test for n in ast.walk(refresh) if isinstance(n, ast.If)]
    check(
        branch_tests,
        "_refresh_encoder_leds must branch at all",
    )
    check(
        not [t for t in branch_tests if isinstance(t, ast.Constant)],
        "a branch in _refresh_encoder_leds is switched off by a constant — the Mix colours "
        "would never run and every substring guard above would still pass",
    )


def test_no_branch_in_the_script_is_disabled_by_a_constant():
    """`if False:` / `elif True:` anywhere in the script is dead or unconditional code.

    This exists because it is how bugs get *simulated* while verifying guards, and one such
    edit slipped past a whole set of substring-based assertions during Phase 7 — every name
    they searched for was still present, just unreachable. A guard that cannot see a disabled
    branch is not guarding the branch.

    `while True:` is a legitimate loop and is not an `ast.If`, so it is unaffected.
    """
    import ast
    import glob

    offenders = []
    for path in sorted(glob.glob(os.path.join(SCRIPT_DIR, "*.py"))):
        tree = ast.parse(open(path, encoding="utf-8").read())
        for node in ast.walk(tree):
            if isinstance(node, ast.If) and isinstance(node.test, ast.Constant):
                offenders.append(
                    f"{os.path.basename(path)}:{node.lineno} if {node.test.value!r}"
                )
    check_equal(
        offenders,
        [],
        "these branches are switched off by a literal, so the code under them never runs",
    )


def test_arm_sits_on_the_soft_buttons_and_reads_live():
    """The eight LCD buttons arm the eight strips; red when armed, dark when not."""
    mix = MAPPINGS["Main_Modes"]["mix"]["modes"]
    mixer = next((m for m in mix if m.get("component") == "Mixer"), None)
    check(mixer is not None, "Mix mode must bind the Mixer component")
    if mixer is not None:
        check_equal(
            mixer.get("arm_buttons"),
            "soft_buttons",
            "arm_buttons is the plural spelling and needs the *matrix*, not a raw element",
        )

    # The matrix must exist, and the singles must come off it rather than being declared
    # separately — two elements on one CC is two potential writers.
    elements_source = open(os.path.join(SCRIPT_DIR, "elements.py"), encoding="utf-8").read()
    check(
        '"Soft_Buttons"' in elements_source,
        "elements.py must declare the soft buttons as a matrix so Mix can bind them as a group",
    )
    check(
        "Soft_{index + 1}_Button" not in elements_source,
        "the individual soft buttons must not also be declared — that puts two elements on "
        "each CC, which is the shared-address trap that cost three attempts on the halos",
    )
    song_binds = [
        value
        for section in MAPPINGS["Main_Modes"]["song"]["modes"]
        for key, value in section.items()
        if isinstance(value, str) and "soft" in value
    ]
    check(song_binds, "Song mode must still bind soft buttons")
    for value in song_binds:
        check(
            value.startswith("soft_buttons_raw["),
            f"Song mode must take its soft buttons off the matrix, got {value!r}",
        )

    skin_source = open(os.path.join(SCRIPT_DIR, "skin.py"), encoding="utf-8").read()
    check("ArmOn = Rgb.RED" in skin_source, "an armed track's button must be red")
    check("ArmOff = Rgb.OFF" in skin_source, "an unarmed track's button must be dark, not blue")


#: Every field of `MixerStrip`, and what has to be listening for it to update live.
#: `None` means the field cannot go stale on its own — it is derived from the strip index or
#: from the ring, and the ring has its own listeners.
#:
#: ⚠️ **Add a field to `MixerStrip` and this table must grow with it.** That is the point: the
#: guard below fails on an unclassified field, so "I put it on screen and forgot to listen for
#: it" cannot pass review.
#: Live properties Mix mode's **Pan page** reads, and the listener each needs. The Volume page's
#: table below is keyed off `MixerStrip`'s fields; the Pan page builds `MainContent` instead, so it
#: needs its own entry — and that gap is exactly how the pan arcs shipped with no listener.
MIX_PAN_LISTENERS = {
    "panning": "add_value_listener",
    "name": "add_name_listener",
}

#: A field that is kept fresh by the **meter poll loop** rather than by an event.
#:
#: ⚠️ Distinct from `None`, and the distinction is the point. `None` means "this cannot go
#: stale" (a strip number never changes). `POLLED` means "this changes constantly and is
#: refreshed on a timer" — a completely different promise, and one that carries its own
#: obligation: the loop must exist, must be gated so it is not running when its template is not
#: on screen, and must stop on teardown. Collapsing the two would let someone add a
#: genuinely event-driven field, mark it `None`, and reintroduce the stale-screen bug this
#: whole guard exists for.
POLLED = "<polled>"

#: A field driven by a **control event of ours** — an encoder touch — rather than by anything
#: in Live.
#:
#: The third freshness contract on this dataclass, and the three are not interchangeable:
#: a listener name means "Live tells us", `None` means "this cannot change", `POLLED` means
#: "a timer re-reads it", and `CONTROL_DRIVEN` means "our own handler changes it and must
#: repaint in the same breath". That last obligation is the whole risk: a handler that mutates
#: the state and forgets to render leaves the screen a frame behind the hardware for ever,
#: which is the stale-screen bug wearing a different hat.
CONTROL_DRIVEN = "<control>"

MIXER_STRIP_LISTENERS = {
    "name": "add_name_listener",
    "number": None,
    "volume": "add_value_listener",
    "muted": "add_mute_listener",
    "soloed": "add_solo_listener",
    "colour": "add_color_listener",
    "assigned": None,
    # Phase 7c. `output_meter_left`/`_right` ARE observable, but they fire far faster than any
    # rate the screen can use, so a listener would flood the diff to produce a picture no
    # better than 10 Hz gives. The documented exception to "every fact on screen needs an
    # event" — see `test_the_meter_loop_is_gated_and_uses_the_framework_idiom`.
    "meter_left": POLLED,
    "meter_right": POLLED,
    "metered": POLLED,
    # The volume reading shown while an encoder is touched. The *text* moves with the volume,
    # so it rides the same listener as the fader; whether it is *shown* is our own touch state.
    "value_text": "add_value_listener",
    "show_value": CONTROL_DRIVEN,
}


def test_mix_mode_listens_to_everything_it_draws():
    """🐛 **The stale-screen bug, which this project has now hit three times.**

    Symptom on hardware: the Mix screen showed the right thing but only *after* something
    unrelated happened. Turning an encoder moved the volume in Live and the fader did not
    follow; paging the ring moved the tracks and the strips did not follow. Touching another
    encoder appeared to fix it — because a touch selects a track, and the selection *does* have
    a listener. The content was correct throughout; nobody was asking for a redraw.

    The same shape as "the track name updates sometime later" (fixed by `_rebind_track`) and
    "bank changes never repainted" (fixed by listening to `DeviceComponent.parameters`). Every
    fact on screen needs an event, and this asserts it field by field rather than by memory.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    rebind = functions.get("_rebind_mixer_strips")
    check(rebind is not None, "screen_component must define _rebind_mixer_strips")
    if rebind is None:
        return
    rebind_dump = ast.dump(rebind)

    # Every field of the strip must be accounted for, and its listener must be subscribed.
    fields = [f.name for f in dataclasses.fields(display.MixerStrip)]
    for field in fields:
        check(
            field in MIXER_STRIP_LISTENERS,
            f"MixerStrip.{field} is drawn but not classified in MIXER_STRIP_LISTENERS — "
            f"either name the listener that keeps it fresh, or record that it cannot go stale",
        )
        required = MIXER_STRIP_LISTENERS.get(field)
        if required is None:
            continue
        if required is CONTROL_DRIVEN:
            # Our own handler owns it, so the obligation is that the handler repaints. Both
            # touch handlers are named `encoder_touch_buttons` (pressed and released share the
            # name, as the framework's decorator idiom requires), so this checks every
            # definition of it.
            handlers = [
                n
                for n in ast.walk(tree)
                if isinstance(n, ast.FunctionDef) and n.name == "encoder_touch_buttons"
            ]
            check(
                len(handlers) == 2,
                f"expected a pressed and a released handler for the encoder touch, found "
                f"{len(handlers)}",
            )
            for handler in handlers:
                check(
                    "_render" in ast.dump(handler),
                    f"MixerStrip.{field} is CONTROL_DRIVEN, so every encoder-touch handler "
                    f"must repaint — one that mutates the state without rendering leaves the "
                    f"screen a frame behind the hardware permanently",
                )
            continue
        if required is POLLED:
            # A polled field's freshness is the loop's job, and the loop has its own guard.
            # What must be true *here* is that the loop is actually what reads it: a field
            # marked POLLED whose value never enters `_poll_meters`'s render path would go
            # stale exactly like an unlistened one.
            check(
                "_poll_meters" in functions and "_update_meter_task" in functions,
                f"MixerStrip.{field} is marked POLLED but there is no meter loop to poll it",
            )
            continue
        # The verbs are built with f-strings for mute/solo/name/color, so check the stem.
        stem = required.replace("add_", "").replace("_listener", "")
        check(
            required in rebind_dump or f'"{stem}"' in rebind_dump or f"'{stem}'" in rebind_dump,
            f"nothing listens for MixerStrip.{field} — it will update only when some "
            f"unrelated event forces a render, which is the stale-screen bug",
        )
    for field in MIXER_STRIP_LISTENERS:
        check(
            field in fields,
            f"MIXER_STRIP_LISTENERS names {field!r}, which is no longer a MixerStrip field",
        )

    # Volume lives on the mixer device, not the track.
    check(
        "mixer_device" in rebind_dump,
        "the fader follows `track.mixer_device.volume`, so that is what must be listened to",
    )

    # 🐛 **And the Pan page, which shipped without one.** The table above is keyed off
    # `MixerStrip`, so it could not see the Pan page at all — that page builds `MainContent`.
    # Any Live property the pan content reads must also be listened to.
    pan_content = functions.get("_mixer_pan_content")
    check(pan_content is not None, "screen_component must define _mixer_pan_content")
    if pan_content is not None:
        pan_dump = ast.dump(pan_content)
        for prop, listener in MIX_PAN_LISTENERS.items():
            if prop not in pan_dump:
                continue
            stem = listener.replace("add_", "").replace("_listener", "")
            check(
                listener in rebind_dump
                or f'"{stem}"' in rebind_dump
                or f"'{stem}'" in rebind_dump,
                f"the Pan page reads {prop!r} but nothing listens for it — the arcs would "
                f"only move when an unrelated event forced a render",
            )
        check(
            "panning" in pan_dump,
            "the Pan page must read mixer_device.panning",
        )
        # ⚠️ **Not a substring check.** Verified by deleting the listener call and watching a
        # `"panning" in rebind_dump` test still pass — the *variable* survives even when the
        # subscription does not. Assert the subscription itself: `_add_mixer_listener` must be
        # called with `panning` as its subject.
        subjects = {
            n.args[0].id
            for n in ast.walk(rebind)
            if isinstance(n, ast.Call)
            and isinstance(n.func, ast.Attribute)
            and n.func.attr == "_add_mixer_listener"
            and n.args
            and isinstance(n.args[0], ast.Name)
        }
        check(
            "panning" in subjects,
            "nothing *subscribes* to panning — this is the stale-screen bug, one page along. "
            f"Subjects actually subscribed: {sorted(subjects)}",
        )
        check(
            "volume" in subjects,
            f"nothing subscribes to volume either. Subjects: {sorted(subjects)}",
        )

    # The ring: paging must repaint, and it must re-point the per-track listeners because the
    # tracks under the strips have changed.
    check("bind_session_ring" in functions, "screen_component must bind the session ring")
    for handler, event in (
        ("_on_ring_offset_changed", "offset"),
        ("_on_ring_tracks_changed", "tracks"),
    ):
        node = functions.get(handler)
        check(node is not None, f"screen_component must define {handler}")
        if node is None:
            continue
        check(
            any(
                isinstance(d, ast.Call)
                and getattr(d.func, "id", "") == "listens"
                and d.args
                and isinstance(d.args[0], ast.Constant)
                and d.args[0].value == event
                for d in node.decorator_list
            ),
            f"{handler} must be @listens({event!r})",
        )
        called = {
            n.func.attr
            for n in ast.walk(node)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
        }
        check("_render" in called, f"{handler} must repaint")
        check(
            "_rebind_mixer_strips" in called,
            f"{handler} must re-point the per-track listeners — the ring moved the tracks out "
            f"from under them",
        )

    # And the listeners must be released, or a reload leaks them onto dead tracks.
    disconnect = functions.get("disconnect")
    if disconnect is not None:
        check(
            "_clear_mixer_listeners" in ast.dump(disconnect),
            "disconnect must release the strip listeners",
        )


def test_a_light_track_colour_does_not_hide_the_strip_name():
    """🐛 **White track, white text, invisible label.**

    `MIXER_CHANNEL_LABEL` has a `text` attribute and **nothing else** — no `color` — so the
    firmware picks the text colour and it is light. `text_on()`, which keeps the Plugin header
    and Song centre bar readable by flipping the *text*, has nowhere to write. The only lever is
    the swatch behind it, so a light track colour is darkened until white text reads, keeping
    the hue so the track stays identifiable.
    """
    # The premise: the label really has no colour attribute, so this cannot be fixed the
    # normal way. Derived from the template map so it fails if the device map is ever revised.
    path = next((p for p in CSV_CANDIDATES if os.path.exists(p)), None)
    check(path is not None, "the template map is required")
    if path is None:
        return
    label_attrs = set()
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if (
                int(row["template"]) == screen.Mixer.template
                and (int(row["zone"]), int(row["element"])) == screen.Mixer.label(0)
            ):
                label_attrs.add(row["attr"].strip())
    check_equal(
        sorted(label_attrs),
        ["text"],
        "MIXER_CHANNEL_LABEL is text-only; if it gained a `color` attribute, use text_on() "
        "instead of darkening the swatch and keep the track's real colour",
    )

    # Behaviour: a white track must not produce a light swatch.
    white = (127, 127, 127)
    strips = (
        display.MixerStrip(name="Vox", number="1", volume=100, colour=white, assigned=True),
    ) + (display.EMPTY_STRIP,) * 7
    _, model = make_model()
    view = display.MixerView(model)
    view.activate()
    view.render(display.MixerContent(strips=strips))

    swatch = model._desired.get(
        (screen.Mixer.template,) + screen.Mixer.label_background(0) + (midi.ATTR_COLOR,)
    )
    check(swatch is not None, "the swatch must be painted")
    if swatch is None:
        return
    check(
        palette.luminance(swatch) < palette.luminance(white),
        f"a white track produced a swatch of luminance {palette.luminance(swatch)} — the "
        f"firmware draws the name in light text on top of it, so it would be invisible",
    )
    check(
        palette.luminance(swatch) <= 63,
        "the swatch must be below the light/dark threshold for light text to read on it",
    )
    # …and a colour that is already dark must be left alone, or every track looks the same.
    dark = palette.rgb7(0x1A2FA0)
    check_equal(
        palette.darken_under_fixed_light_text(dark),
        dark,
        "an already-dark track colour must pass through untouched",
    )
    # Hue is preserved, not flattened to grey — the swatch is what identifies the track.
    warm = palette.rgb7(0xFF9C40)
    out = palette.darken_under_fixed_light_text(warm)
    check(
        out[0] > out[2],
        f"darkening must keep the hue: {warm} -> {out} lost its warm bias",
    )


def test_the_wheel_halo_is_lit_in_every_mode_that_uses_it():
    """The wheel now has a job in Mix mode too, so its halo has to say so.

    Still strictly mode-level: a halo that changes while you are turning the control gives
    every transition a chance to leave it dark, which is what it used to do (§6b-10).
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read())
    refresh = next(
        (n for n in ast.walk(tree)
         if isinstance(n, ast.FunctionDef) and n.name == "_refresh_wheel_led"),
        None,
    )
    check(refresh is not None, "screen_component must define _refresh_wheel_led")
    if refresh is None:
        return
    dumped = ast.dump(refresh)
    for mode in ("PLUGIN_MODE", "MIX_MODE"):
        check(
            mode in dumped,
            f"the wheel halo must be lit in {mode} — the wheel does something there",
        )
    # Mode only: nothing about touch, press or scrolling may reach the halo.
    for forbidden in ("_touch_held", "pressed", "is_pressed"):
        check(
            forbidden not in dumped,
            f"the wheel halo must not react to {forbidden} — it is a mode indicator",
        )


def test_the_pan_page_marks_focus_on_the_centre_label():
    """Template 0's centre strip has a `color`, so the Pan page can mark focus there too."""
    _, model = make_model()
    view = display.MainView(model)
    view.activate()
    track_colour = (90, 30, 20)
    view.render(
        display.MainContent(
            title="Mix | Pan",
            centre="Lead",
            header_background=track_colour,
            centre_background=track_colour,
            tiles=(display.EncoderTile(label="Lead", value=64, assigned=True),) * 8,
        )
    )
    background = model._desired.get(
        (screen.Main.template,) + screen.Main.CENTRE_BACKGROUND + (midi.ATTR_COLOR,)
    )
    check_equal(
        background, track_colour, "the centre strip must take the selected track's colour"
    )
    text = model._desired.get(
        (screen.Main.template,) + screen.Main.CENTRE_TEXT + (midi.ATTR_COLOR,)
    )
    check_equal(
        text,
        tuple(palette.text_on(track_colour)),
        "the centre text must contrast with it — Live's track colours include pale ones",
    )

    # Plugin mode passes no centre colour and must still get the factory grey.
    _, model2 = make_model()
    view2 = display.MainView(model2)
    view2.activate()
    view2.render(sample_content())
    check_equal(
        model2._desired.get(
            (screen.Main.template,) + screen.Main.CENTRE_BACKGROUND + (midi.ATTR_COLOR,)
        ),
        tuple(screen.Palette.PLUGIN_TITLE_BACKGROUND),
        "with no centre colour the strip stays the factory grey, as Plugin mode wants",
    )

    # ⚠️ One owner: the centre background moved out of paint_chrome into render, so it must
    # not be painted in both places.
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "display.py"), encoding="utf-8").read())
    main_view = next(
        n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "MainView"
    )
    chrome = next(
        n for n in main_view.body
        if isinstance(n, ast.FunctionDef) and n.name == "paint_chrome"
    )
    check(
        "CENTRE_BACKGROUND" not in ast.dump(chrome),
        "CENTRE_BACKGROUND must be painted by render() alone — two writers on one element is "
        "what the one-owner rule forbids",
    )


def test_the_pan_page_reveals_its_value_on_touch():
    """🐛 **Focus used to swallow the reveal for all of Mix mode.**

    Right for the Volume page — Template 2 shows the fader permanently, so there is nothing to
    reveal — and wrong for Pan, where Template 0 gives one text element per tile and the value
    has to share it with the name, exactly as in Plugin mode.

    Live formats a pan as `50L` / `C` / `50R` through `str(parameter)`, so the bipolar reading
    comes free once the value is actually shown. ⚠️ The **arc** cannot be bipolar:
    `MAIN_ENCODER_ENCODER[n]` takes a single 0-127 `value` with no fill-mode attribute, so
    centre reads as a half-filled arc and that is a firmware limit, not a choice.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read())
    handlers = [
        n for n in ast.walk(tree)
        if isinstance(n, ast.FunctionDef) and n.name == "encoder_touch_buttons"
    ]
    check_equal(len(handlers), 2, "there must be a pressed and a released touch handler")
    pressed, released = handlers

    # The early return that implements "focus only" must be page-aware, not mode-aware.
    for node, what in ((pressed, "press"), (released, "release")):
        dumped = ast.dump(node)
        check(
            "MIX_PAGE_PAN" in dumped,
            f"the touch {what} handler must distinguish the Pan page — otherwise focusing "
            f"swallows the value reveal on both pages",
        )

    # The pan content has to pass the reveal flag through, or the tile never shows a value.
    pan = next(
        n for n in ast.walk(tree)
        if isinstance(n, ast.FunctionDef) and n.name == "_mixer_pan_content"
    )
    dumped = ast.dump(pan)
    check("_showing_value" in dumped, "the pan tile must carry the reveal flag")
    # The centre strip's colour has to be *passed*, not just supported by the view.
    keywords = {
        kw.arg
        for n in ast.walk(pan)
        if isinstance(n, ast.Call)
        and isinstance(n.func, ast.Name)
        and n.func.id == "MainContent"
        for kw in n.keywords
    }
    check(
        "centre_background" in keywords,
        "the pan page must pass centre_background, or the centre label never marks the focus "
        f"however well MainView supports it. Passed: {sorted(k for k in keywords if k)}",
    )
    check("header_background" in keywords, "the header must still take the track colour")
    check(
        "format_parameter_value" in dumped,
        "the pan value text must come from Live's own formatting — that is what gives L/C/R",
    )


def test_mix_pages_are_scoped_to_mix_mode():
    """🔑 **`Mix_Pages` must be dormant outside Mix mode.**

    A modes component is **enabled by default** — `_setup_modes_component` ends with
    `set_enabled(modes_config.pop("enable", True))`. Left on, its page layer would hold the
    eight encoders in Song and Plugin mode too, silently outranking the bindings those modes
    make. `"enable": False` plus naming it as a mode part is what scopes it.
    """
    pages = MAPPINGS.get("Mix_Pages")
    check(pages is not None, "Mix_Pages must be declared")
    if pages is None:
        return
    check_equal(
        pages.get("enable"),
        False,
        'Mix_Pages must declare "enable": False, or its page layer is live in every mode',
    )

    mix = MAPPINGS["Main_Modes"]["mix"]["modes"]
    check(
        any(part.get("component") == "Mix_Pages" and len(part) == 1 for part in mix),
        "Mix mode must enable Mix_Pages by naming it as a mode part — a component named with "
        "no mappings resolves to the component itself, which the mode enables on enter",
    )

    # The first mode listed is the default: `_setup_modes_component` assigns
    # `selected_mode = modes[0]` when none is set.
    page_names = [k for k, v in pages.items() if isinstance(v, dict)]
    check_equal(
        page_names[:1], ["volume"], "Mix mode must open on the Volume page, not on Pan"
    )
    check_equal(
        sorted(page_names), ["pan", "sends", "volume"],
        "three Mix pages: Volume, Pan and Sends",
    )


def test_mix_encoders_belong_to_the_page_not_the_mode():
    """The eight encoders rebind between pages, so only a page layer may claim them.

    Binding `volume_controls` at Mix level *and* `pan_controls` at page level would put two
    claims on one control from two layers that are live together — the ownership stack would
    resolve it by priority rather than by intent, which is not something to leave to chance.
    """
    mix_parts = MAPPINGS["Main_Modes"]["mix"]["modes"]
    for part in mix_parts:
        for key, value in part.items():
            check(
                value != "encoders" or key == "scroll_encoder",
                f"Mix mode binds {key!r} to the encoders at mode level — that belongs to a "
                f"page, or the two pages cannot rebind them",
            )

    pages = MAPPINGS["Mix_Pages"]
    bound = {}
    for page, spec in pages.items():
        if not isinstance(spec, dict):
            continue
        for part in spec.get("modes", []):
            for key, value in part.items():
                if value == "encoders":
                    bound[page] = key
    check_equal(
        bound,
        {"volume": "volume_controls", "pan": "pan_controls", "sends": "send_controls"},
        "each Mix page must claim the encoders for exactly its own parameter",
    )


def test_the_wheel_pages_mix_and_wraps():
    """The wheel is the pager, it wraps, and the paging is ours because the framework has no
    encoder-driven mode switch.

    `ModesComponent` exposes only `cycle_mode_button` (a button) and `PageComponent.
    set_scroll_encoder` pages a `Pageable`, not a mode set — so `MotionMixPagesComponent`
    subclasses `ScrollComponent`, whose `scroll_encoder(value, _)` already decodes a relative
    encoder into a direction.
    """
    import ast

    mix_parts = MAPPINGS["Main_Modes"]["mix"]["modes"]
    pager = next(
        (p for p in mix_parts if p.get("component") == "Motion_Mix_Pages"), None
    )
    check(pager is not None, "Mix mode must bind the page scroller")
    if pager is not None:
        check_equal(
            pager.get("scroll_encoder"),
            "wheel_encoder",
            "the big wheel is the pager",
        )

    source = open(os.path.join(SCRIPT_DIR, "mixpages.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    classes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    check(classes, "mixpages.py must define a component")
    bases = {b.id for c in classes for b in c.bases if isinstance(b, ast.Name)}
    check(
        "ScrollComponent" in bases,
        "the pager must subclass ScrollComponent — that is what decodes the relative encoder",
    )

    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    for required in ("can_scroll_up", "can_scroll_down", "scroll_up", "scroll_down"):
        check(
            required in functions,
            f"the pager must override {required} — otherwise ScrollComponent consults the "
            f"injected scrollable, which is None",
        )
    step = functions.get("_step")
    check(step is not None, "mixpages.py must define _step")
    if step is not None:
        check(
            any(isinstance(n, ast.Mod) for n in ast.walk(step)),
            "the pages must wrap (user decision, 2026-07-30), so the step is modulo the page "
            "count — that also means a third page needs no change here",
        )
    # Wrapping means there is no end to stop at, so both directions are always available.
    for direction in ("can_scroll_up", "can_scroll_down"):
        node = functions[direction]
        check(
            not [n for n in ast.walk(node) if isinstance(n, ast.Compare)
                 and any(isinstance(o, (ast.Lt, ast.Gt)) for o in n.ops)],
            f"{direction} must not test a boundary — the pages wrap",
        )


def test_the_pan_page_draws_template_0():
    """Mix's Pan page borrows the encoder-tile view, and shares its key with the content."""
    import ast

    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    tree = ast.parse(source)

    class_body = next(
        n for n in ast.walk(tree)
        if isinstance(n, ast.ClassDef) and n.name == "MotionScreenComponent"
    )
    tables = {}
    for node in class_body.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in ("_VIEWS", "_CONTENT"):
                    tables[target.id] = {
                        (k.id if isinstance(k, ast.Name) else None): ast.dump(v)
                        for k, v in zip(node.value.keys, node.value.values)
                    }
    for table in ("_VIEWS", "_CONTENT"):
        check(
            "MIX_PAN_LAYER" in tables.get(table, {}),
            f"{table} must carry the Mix pan layer, or the page cannot draw",
        )
    if "MIX_PAN_LAYER" in tables.get("_VIEWS", {}):
        check(
            "main_view" in tables["_VIEWS"]["MIX_PAN_LAYER"],
            "the pan page must use MainView — Template 2 has no pan element at all",
        )

    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    check("_mixer_pan_content" in functions, "there must be a pan content builder")
    if "_mixer_pan_content" in functions:
        dumped = ast.dump(functions["_mixer_pan_content"])
        check("panning" in dumped, "the pan page must read mixer_device.panning")
        check(
            "MainContent" in dumped,
            "the pan page must build MainContent, the content class MainView accepts",
        )

    # The page must reach the layer key, and via the bound modes component.
    check("bind_mix_pages" in functions, "the screen must follow the Mix page selection")
    layer = functions.get("_screen_layer")
    if layer is not None:
        check(
            "MIX_PAN_LAYER" in ast.dump(layer),
            "_screen_layer must return the pan layer, or the page never draws",
        )


def test_pad_leds_are_note_addressed():
    """Pads are the only LED group on this device that is NOT CC-addressed.

    State goes out on `0x90` and colour on `0x91`/`0x92`/`0x93`, against notes 36-67. Sending
    the button statuses (`0xB0`-`0xB3`) instead would address encoder halos and bank buttons —
    lighting the wrong hardware entirely, with nothing to indicate it.
    """
    sent = []
    pads = leds.PadLeds(send=sent.append)
    check_equal(pads.count, 32, "32 pads, two lanes of 16")
    check_equal(
        (midi.PAD_NOTES[0], midi.PAD_NOTES[15], midi.PAD_NOTES[16], midi.PAD_NOTES[-1]),
        (36, 51, 52, 67),
        "lane 0 = notes 36-51, lane 1 = 52-67",
    )

    pads.set(0, (127, 51, 0))
    pads.flush()
    check_equal(
        [tuple(m) for m in sent],
        [(0x90, 36, 127), (0x91, 36, 127), (0x92, 36, 51), (0x93, 36, 0)],
        "a pad writes state on 0x90 and RGB on 0x91/0x92/0x93 at its own note",
    )

    # ...and the halos must still be CC-addressed, or the parameterisation broke them.
    sent.clear()
    halos = leds.EncoderLeds(send=sent.append)
    halos.set(0, (0, 52, 102))
    halos.flush()
    check_equal(
        [m[0] for m in sent],
        [0xB0, 0xB1, 0xB2, 0xB3],
        "encoder halos stay on the CC statuses",
    )


def test_pad_layout_matches_the_studio_pro_capture():
    """Every claim here is checked against a real Studio Pro track-change burst.

    The pads are a **piano**, not a chromatic grid: bottom lane = 16 white keys, top lane =
    the black key above each, dark where none exists. The capture tinted exactly C1/G1/D2
    (36/43/50) with the track colour and zeroed exactly F#2/A#2/C#3/F3 (54/58/61/65).
    """
    roles = pads.pad_roles(0)
    check_equal(len(roles), 32, "32 pads")

    tinted = [pads.note_for_index(i) for i, r in enumerate(roles) if r == pads.ROOT]
    dark = [pads.note_for_index(i) for i, r in enumerate(roles) if r == pads.ABSENT]
    check_equal(tinted, [36, 43, 50], "roots are the pads the capture tinted (C1, G1, D2)")
    check_equal(dark, [54, 58, 61, 65], "dark pads are the ones the capture zeroed")
    check_equal(
        sum(1 for r in roles if r != pads.ABSENT), 28, "28 of 32 pads are lit, as captured"
    )

    check_equal(pads.note_for_index(0), 36, "pad 0 is note 36")
    check_equal(pads.note_for_index(15), 51, "lane 0 ends at 51")
    check_equal(pads.note_for_index(16), 52, "lane 1 starts at 52")
    check_equal(pads.note_for_index(31), 67, "lane 1 ends at 67")

    # The white keys really are a piano row, not every semitone.
    check_equal(
        pads.pad_pitches()[:8],
        [36, 38, 40, 41, 43, 45, 47, 48],
        "lane 0 walks C D E F G A B C — whole tones except E-F and B-C",
    )


def test_pad_root_offset_moves_the_tinted_pads():
    """A-H banking slides the window; the tint travels with the pitches.

    🐛 **This test asserted the exact opposite until 2026-07-29**, and said so confidently:
    *"the tint does not move with the offset"*, on the strength of the manual's "Bank E will be
    selected and Pad 1 will be assigned to the root note". That sentence describes the
    **default** — at bank E the window starts on C, so "pad 1" and "the C's" are the same pads —
    not a rule that pad 1 is permanently the root.

    The two readings agree at bank E and nowhere else, and the capture that verified this layout
    was taken at rest, so nothing could tell them apart until banking ran on hardware. What gave
    it away: the top lane's gaps moved while the bottom lane's tint stood still. **One frame for
    both rows.**
    """
    # At rest, unchanged and still matching the capture.
    check_equal(pads.root_indices(0), (0, 7, 14), "at bank E the C's are pads 1, 8 and 15")
    check_equal(
        [pads.pad_pitches(0, 0)[i] for i in pads.root_indices(0)],
        [36, 48, 60],
        "…and those are the three C's",
    )

    # Sliding the window moves them.
    check(
        pads.root_indices(1) != pads.root_indices(0),
        "the tint must move with the window — it marks pitches, not pad positions",
    )
    check_equal(
        pads.root_indices(1), (6, 13), "at +1 degree the C's have slid one pad to the left"
    )
    check_equal(
        pads.root_indices(-1), (1, 8, 15), "at -1 degree they slide one pad to the right"
    )

    # Whatever the offset: every tinted pad plays the root pitch class and lives on the bottom
    # lane, and *every* such pad is tinted. That is the property both rows now share.
    for offset in range(-4, 4):
        pitches = pads.pad_pitches(offset, 0)
        roots = pads.root_indices(offset)
        check(
            all(index < pads.PADS_PER_LANE for index in roots),
            f"offset {offset}: the tint belongs on the bottom lane — black keys are never C",
        )
        # ⚠️ **That assertion cannot currently fail, and this is why.** In the Keys layout a
        # top-lane pad is always a white key plus one semitone, so it can never carry the root
        # pitch class — the lane test in `roles_for_pitches` is dormant belt-and-braces. Rather
        # than leave a guard that has never been shown to test anything, assert the *reason*,
        # which is falsifiable. It also fails loudly if Phase 10 changes the premise: in Scale
        # mode **both rows are lit** and the top lane carries scale pitches, so a tonic can land
        # there — at which point the lane restriction becomes a real decision, not a no-op.
        check(
            not [
                i
                for i, pitch in enumerate(pitches)
                if i >= pads.PADS_PER_LANE
                and pitch is not None
                and pitch % 12 == pads.ROOT_PITCH_CLASS
            ],
            f"offset {offset}: a top-lane pad plays the root pitch class, so the lane test in "
            f"roles_for_pitches is now load-bearing and needs deciding, not assuming",
        )
        check_equal(
            sorted(roots),
            sorted(
                i
                for i, pitch in enumerate(pitches)
                if i < pads.PADS_PER_LANE
                and pitch is not None
                and pitch % 12 == pads.ROOT_PITCH_CLASS
            ),
            f"offset {offset}: the tint must mark every C on the bottom lane and no other pad",
        )

    # Octave transposes by whole octaves, so it moves no pad's role at all.
    for octaves in (-2, -1, 0, 1, 2):
        check_equal(
            pads.root_indices(0, octaves * 12),
            (0, 7, 14),
            f"octave {octaves:+d} is a whole-octave shift, so the C's stay on the same pads",
        )

    # ⚠️ Corrected 2026-07-25: the dark pads DO move, because sliding the window changes which
    # positions have a black key above them.
    check_equal(
        list(pads.dead_indices(0)), [18, 22, 25, 29], "at rest the gaps match the capture"
    )
    check(
        pads.dead_indices(1) != pads.dead_indices(0),
        "the gaps must move with the window — they are a property of the pitches, not the pads",
    )


def test_ah_banks_rest_on_e_and_step_one_degree():
    """A-H is a radio of eight resting on **E**, and one step is one **scale degree**.

    Two separate decisions live here:

    * **Rest on E** (`[MAN]`: "Bank E will be selected and Pad 1 will be assigned to the root
      note"). Resting at either end would leave half the buttons dead until you moved.
    * **One step = one scale degree**, i.e. one pad along the bottom row. ⚠️ This shipped as
      one *semitone* first, from the manual's chromatic-sounding "moves the musical root note
      left/right along the piano". Factory behaviour (user, 2026-07-29) settles it: A-H only ever
      shifts the **bottom row**, so a press slides the keybed by exactly one bottom-row pad.
    """
    check_equal(pads.BANK_COUNT, 8, "there are eight A-H buttons")
    check_equal(pads.BANK_LETTERS[pads.BANK_REST_INDEX], "E", "the bank rests on E")
    check_equal(pads.bank_step(pads.BANK_REST_INDEX), 0, "E is the zero point")
    check_equal(
        [pads.bank_step(i) for i in range(pads.BANK_COUNT)],
        [-4, -3, -2, -1, 0, 1, 2, 3],
        "A-H spans -4..+3 around E — four steps down, three up",
    )
    # Round-trips, and clamps rather than wrapping: A and H must not be neighbours on a
    # control whose whole point is left-to-right travel.
    for index in range(pads.BANK_COUNT):
        check_equal(
            pads.bank_index_for_step(pads.bank_step(index)),
            index,
            f"bank {pads.BANK_LETTERS[index]} round-trips through its step",
        )
    check_equal(pads.bank_index_for_step(-99), 0, "below A clamps to A, it does not wrap to H")
    check_equal(pads.bank_index_for_step(99), 7, "above H clamps to H, it does not wrap to A")

    # The conversion, read from keyboard.py so the two cannot drift.
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read())
    per_step = next(
        (
            n.value.value
            for n in ast.walk(tree)
            if isinstance(n, ast.Assign)
            and any(
                isinstance(t, ast.Name) and t.id == "DEGREES_PER_BANK_STEP"
                for t in n.targets
            )
            and isinstance(n.value, ast.Constant)
        ),
        None,
    )
    check_equal(per_step, 1, "one A-H step is one scale degree")
    check(
        "SEMITONES_PER_BANK_STEP" not in open(
            os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8"
        ).read(),
        "the semitone conversion must be gone, not left alongside the degree one",
    )


def test_ah_slides_the_window_and_moves_the_gaps():
    """🐛 **The bug the first hardware run found: banking never redrew the keybed.**

    Built as a semitone shift, A-H transposed the whole shape rigidly — every pad moved by the
    same amount and *no pad changed role*, so `pad_roles` returned an identical list,
    `set_pad_roles` correctly saw no change, and the 32 pad LEDs never repainted. There was
    genuinely nothing to repaint.

    A **degree** shift slides the window along the piano, so which positions have a black key
    above them changes and the gaps move with it. That is what makes the keybed redraw, and it
    is the observable difference between the two units.
    """
    rest_gaps = pads.dead_indices(0, 0)
    check_equal(list(rest_gaps), [18, 22, 25, 29], "at rest the gaps match the capture")

    patterns = {}
    for index, letter in enumerate(pads.BANK_LETTERS):
        offset = pads.bank_step(index)
        roles = pads.pad_roles(offset, 0)
        gaps = tuple(i for i, role in enumerate(roles) if role == pads.ABSENT)
        patterns[letter] = gaps

        # The tint marks the C's, so it slides with the window rather than sitting on fixed
        # pads — the bottom row has to redraw too, which is the second half of the same bug.
        tinted = [i for i, role in enumerate(roles) if role == pads.ROOT]
        check(tinted, f"bank {letter}: the keybed must still show where the root is")
        check(
            all(pads.pad_pitches(offset, 0)[i] % 12 == 0 for i in tinted),
            f"bank {letter}: every tinted pad must actually play a C",
        )
        # …and every gap must be on the top lane. The bottom row is sixteen white keys.
        check(
            all(i >= pads.PADS_PER_LANE for i in gaps),
            f"bank {letter}: a gap appeared on the bottom row, which is all white keys",
        )

    # Adjacent banks must differ, or nothing on screen changes when you press one.
    for left, right in zip(pads.BANK_LETTERS, pads.BANK_LETTERS[1:]):
        check(
            patterns[left] != patterns[right],
            f"banks {left} and {right} produce the same gap pattern — the keybed would not "
            f"redraw between them, which is exactly the reported symptom",
        )
    # 🐛 **And the same must hold for the bottom row.** The first fix moved the top lane's gaps
    # and left the tint pinned to pad indices, so half the keybed redrew and half did not.
    tints = {
        letter: pads.root_indices(pads.bank_step(i))
        for i, letter in enumerate(pads.BANK_LETTERS)
    }
    for left, right in zip(pads.BANK_LETTERS, pads.BANK_LETTERS[1:]):
        check(
            tints[left] != tints[right],
            f"banks {left} and {right} tint the same pads — the bottom row would stay fixed "
            f"while the top row moves, which is the reported symptom",
        )
    check_equal(
        tints["A"], tints["H"], "A and H are an octave apart and must tint the same pads"
    )

    # A and H are seven degrees apart, i.e. one octave, so they *should* match. Anything else
    # matching would mean the window is not really sliding.
    check_equal(
        patterns["A"],
        patterns["H"],
        "A and H are an octave apart and must share a gap pattern",
    )
    check_equal(
        len(set(patterns.values())),
        7,
        "eight banks over a seven-degree cycle give exactly seven distinct patterns",
    )


def test_pad_roles_sees_the_transposition():
    """🐛 The regression this exists to prevent, reachable only once A-H lands.

    `pad_roles` used to hard-code `0` for the transposition, reasoning that a rigid shift
    cannot change which positions have a black key above them. True — but it *can* push a pad
    off the bottom of MIDI, and `pad_pitches` calls such a pad dead. Octave alone could not
    reach the edge; bank **A** at octave **-3** is -16 semitones and puts pad 1 on note **-4**.
    A `pad_roles` that ignores the offset calls that pad a ROOT and lights it, while the
    keyboard silences it: a lit pad that plays nothing.
    """
    import inspect

    signature = inspect.signature(pads.pad_roles)
    check(
        "semitone_offset" in signature.parameters,
        "pad_roles must accept the transposition, or it cannot see a pad pushed off the end "
        "of MIDI",
    )

    edge = pads.bank_step(0) + (-3 * 12)  # bank A, octave -3
    check_equal(pads.pad_pitches(0, edge)[0], None, "the test premise: pad 1 is off the end")
    check_equal(
        pads.pad_roles(0, edge)[0],
        pads.ABSENT,
        "a pad pushed below note 0 must be dark — pad_roles is ignoring the transposition",
    )


def test_roles_come_from_the_pitch_list_not_a_second_offset():
    """The screen component must not keep its own copy of the layout offsets.

    `_refresh_pad_leds` used to call `pad_roles(self._pad_root_offset)` from an int the screen
    component maintained itself — a second copy of state the keyboard also holds. Nothing kept
    them in step, and the symptom would have been the keybed lighting a layout it does not
    play. The keyboard now reports roles derived from `self._pitches`, the very list the note
    translation is built from.
    """
    import ast

    screen_source = open(
        os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8"
    ).read()
    tree = ast.parse(screen_source)
    # AST, not a substring search: the comment explaining *why* this attribute is gone names
    # it, and a guard that a docstring can fail teaches people to delete the docstring.
    check(
        not [
            n
            for n in ast.walk(tree)
            if isinstance(n, ast.Attribute) and n.attr == "_pad_root_offset"
        ],
        "screen_component.py must not keep its own root offset — that is the second copy",
    )
    refresh = next(
        (
            n
            for n in ast.walk(tree)
            if isinstance(n, ast.FunctionDef) and n.name == "_refresh_pad_leds"
        ),
        None,
    )
    check(refresh is not None, "screen_component.py must define _refresh_pad_leds")
    if refresh is not None:
        called = {
            n.func.id
            for n in ast.walk(refresh)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
        }
        check(
            "pad_roles" not in called,
            "_refresh_pad_leds must paint the roles it was given, not compute a second opinion",
        )
    check(
        "set_pad_roles" in screen_source,
        "the screen component must accept roles from the keyboard",
    )

    # And the keyboard must actually derive them from the pitch list, and report on every
    # layout change — a listener that is only fired from `set_bank` would miss Octave.
    keyboard_source = open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read()
    ktree = ast.parse(keyboard_source)
    kfunctions = {n.name: n for n in ast.walk(ktree) if isinstance(n, ast.FunctionDef)}
    recompute = kfunctions.get("_recompute")
    check(recompute is not None, "keyboard.py must define _recompute")
    if recompute is not None:
        called = {
            n.func.attr
            for n in ast.walk(recompute)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
        }
        check(
            "_report_roles" in called,
            "_recompute must report the roles — otherwise the lights follow only whichever "
            "setter remembered to push them",
        )
    roles_property = kfunctions.get("pad_roles")
    check(roles_property is not None, "keyboard.py must expose pad_roles")
    if roles_property is not None:
        check(
            "_pitches" in ast.dump(roles_property),
            "the keyboard's roles must come from its own pitch list, not be recomputed from "
            "the offsets that produced it",
        )

    # The surface has to wire the two together, or the roles never arrive.
    init_source = open(os.path.join(SCRIPT_DIR, "__init__.py"), encoding="utf-8").read()
    check(
        "set_roles_listener" in init_source,
        "__init__.py must connect the keyboard's roles to the screen component",
    )


def test_ah_is_a_radio_with_one_bank_lit():
    """Exactly one A-H button is lit, and a press selects rather than toggles.

    Same reasoning as the mode buttons in `mappings.py`: "toggle off" has no well-defined
    destination for a radio, and a bank that could be deselected would leave the pads with no
    root at all.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read())
    assigned = {
        t.id
        for n in ast.walk(tree)
        if isinstance(n, ast.Assign)
        for t in n.targets
        if isinstance(t, ast.Name)
    }
    for letter in pads.BANK_LETTERS:
        name = f"bank_{letter.lower()}_button"
        check(name in assigned, f"keyboard.py must declare {name}")

    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    # Every handler funnels into the one mutator, and each claims its own index.
    claimed = []
    for index, letter in enumerate(pads.BANK_LETTERS):
        handler = functions.get(f"bank_{letter.lower()}_button")
        check(handler is not None, f"keyboard.py must handle bank_{letter.lower()}_button")
        if handler is None:
            continue
        selects = [
            n
            for n in ast.walk(handler)
            if isinstance(n, ast.Call)
            and isinstance(n.func, ast.Attribute)
            and n.func.attr == "_select_bank"
        ]
        check(
            len(selects) == 1,
            f"bank {letter} must go through _select_bank — one place moves the bank",
        )
        if selects and selects[0].args and isinstance(selects[0].args[0], ast.Constant):
            claimed.append(selects[0].args[0].value)
    check_equal(
        claimed,
        list(range(pads.BANK_COUNT)),
        "each A-H button must claim its own index, in order — a duplicated or skipped index "
        "is a button that selects the wrong bank, silently",
    )

    # The LED refresh must be an equality test against the selected bank, not a comparison
    # that could light more than one.
    refresh = functions.get("_refresh_bank_leds")
    check(refresh is not None, "keyboard.py must define _refresh_bank_leds")
    if refresh is not None:
        dumped = ast.dump(refresh)
        check("Eq" in dumped, "_refresh_bank_leds must test equality — a radio lights one")
        check(
            "is_on" in dumped,
            "_refresh_bank_leds must drive is_on, the verified two-colour mechanism",
        )

    # set_bank must clamp and early-return, like every other layout setter.
    set_bank = functions.get("set_bank")
    check(set_bank is not None, "keyboard.py must define set_bank")
    if set_bank is not None:
        dumped = ast.dump(set_bank)
        check("max" in dumped and "min" in dumped, "set_bank must clamp, not wrap or run free")
        check(
            any(isinstance(n, ast.Return) for n in ast.walk(set_bank)),
            "set_bank must early-return when nothing changed — the latency rule",
        )
        called = {
            n.func.attr
            for n in ast.walk(set_bank)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
        }
        check(
            "_recompute" in called,
            "set_bank must go through _recompute, so both layout passes refresh",
        )

    # A press always answers, even at the ends — the dead-button rule from _nudge_octave.
    select = functions.get("_select_bank")
    check(select is not None, "keyboard.py must define _select_bank")
    if select is not None:
        notifies = [
            n
            for n in ast.walk(select)
            if isinstance(n, ast.Call)
            and isinstance(n.func, ast.Attribute)
            and n.func.attr == "_notify"
        ]
        check(
            len(notifies) == 1,
            "_select_bank must notify on every press, not only when the bank moved — a press "
            "with no feedback reads as a dead button",
        )
        check(
            not any(isinstance(n, ast.If) for n in select.body),
            "the notification must not be conditional",
        )


def test_ah_elements_and_mappings_line_up():
    """Eight buttons at CC 0x00-0x07, bound to the eight control names, one each."""
    check_equal(
        list(midi.CC_BANK_BUTTONS),
        list(range(0x00, 0x08)),
        "A-H is CC 0x00-0x07 (Motion32_Control_Surface_Definition.md §2)",
    )
    keyboard_map = MAPPINGS["Motion_Keyboard"]
    for letter in pads.BANK_LETTERS:
        name = f"bank_{letter.lower()}_button"
        check_equal(
            keyboard_map.get(name),
            name,
            f"{name} must be bound to its element — an unknown Layer name binds silently",
        )
    bound = [v for k, v in keyboard_map.items() if k.startswith("bank_")]
    check_equal(
        len(set(bound)), pads.BANK_COUNT, "no element may be bound to two bank buttons"
    )

    source = open(os.path.join(SCRIPT_DIR, "elements.py"), encoding="utf-8").read()
    check(
        "CC_BANK_BUTTONS" in source,
        "elements.py must declare the A-H buttons from the midi.py constant",
    )
    for key in ("Bank", "BankSelected", "BankPressed"):
        check(
            f"{key} = " in open(os.path.join(SCRIPT_DIR, "skin.py"), encoding="utf-8").read(),
            f"skin.py must define Keyboard.{key} — a missing skin key falls back to the "
            f"framework default and the button lights the wrong colour",
        )


_KEYBOARD_MODULE = [None]


def _load_keyboard():
    """Import `keyboard.py` for real, against a stand-in for `PlayableComponent`.

    ⚠️ **Why this exists, written down because it cost a hardware round-trip.** A–H shipped with
    AST guards only — "the handler calls `_select_bank`", "`set_bank` clamps", "`_recompute` is
    called". Every one passed, and the feature still did not do what it should on hardware,
    because *structure is not behaviour*. An AST guard can prove a call exists; it cannot prove
    the number that comes out the other end is right.

    The stand-in reproduces the parts of `PlayableComponent` the layout actually touches — the
    matrix, `_set_button_control_properties` writing `identifier`/`channel` onto the element,
    and `_button_should_be_enabled`'s `identifier is None or identifier < 128` rule — all read
    from `components/playable.pyc`. It deliberately does **not** model Live's MIDI map: what it
    proves is that the component computes and applies the right identifiers. Whether the
    framework then carries them into Live is a hardware question, and the layout log line in
    `_recompute` is what answers that one.
    """
    if _KEYBOARD_MODULE[0] is not None:
        return _KEYBOARD_MODULE[0]

    class _Mode:
        listenable = "listenable"
        playable = "playable"
        playable_and_listenable = "playable_and_listenable"

    class PlayableControl:
        Mode = _Mode

        def __init__(self, *a, **k):
            pass

    class _ButtonState:
        """`ButtonControl.State`, reduced to the colour model verified in `button.pyc`."""

        def __init__(self, color=None, on_color=None, pressed_color=None):
            self.color, self.on_color, self.pressed_color = color, on_color, pressed_color
            self._is_on = False

        @property
        def is_on(self):
            return self._is_on

        @is_on.setter
        def is_on(self, value):
            self._is_on = bool(value)

        @property
        def rendered_color(self):
            """What `_send_button_color` would pick: `on_color if is_on else color`."""
            if self.on_color is not None and self._is_on:
                return self.on_color
            return self.color

    class ButtonControl:
        def __init__(self, color=None, on_color=None, pressed_color=None, **k):
            self._kw = dict(color=color, on_color=on_color, pressed_color=pressed_color)
            self._name = None

        def __set_name__(self, owner, name):
            self._name = name

        def pressed(self, function):
            self._handler = function
            return self

        def __get__(self, obj, owner=None):
            if obj is None:
                return self
            states = obj.__dict__.setdefault("_states", {})
            return states.setdefault(self._name, _ButtonState(**self._kw))

    class _Button:
        def __init__(self, row, column):
            self.coordinate = (row, column)
            self.identifier = None
            self.channel = None
            self.enabled = None
            self.mode = None

        def set_mode(self, mode):
            self.mode = mode

    class PlayableComponent:
        def __init__(self, *a, **k):
            self._takeover_pads = False
            self._default_playable_mode = _Mode.playable_and_listenable
            self.matrix = [_Button(r, c) for r in range(2) for c in range(16)]
            self.pressed_pads = []

        def is_enabled(self):
            return True

        def update(self):
            pass

        def _note_translation_for_button(self, button):
            return (None, None)

        def _button_should_be_enabled(self, button):
            identifier, _ = self._note_translation_for_button(button)
            return identifier is None or (isinstance(identifier, int) and identifier < 128)

        def _set_button_control_properties(self, button):
            identifier, channel = self._note_translation_for_button(button)
            button.identifier = identifier
            button.channel = channel

        def _on_matrix_pressed(self, button):
            pass

        def _on_matrix_released(self, button):
            pass

    cs = sys.modules["ableton.v3.control_surface"]
    components = types.ModuleType("ableton.v3.control_surface.components")
    controls = types.ModuleType("ableton.v3.control_surface.controls")
    components.PlayableComponent = PlayableComponent
    controls.ButtonControl = ButtonControl
    controls.PlayableControl = PlayableControl
    cs.components, cs.controls = components, controls
    sys.modules.setdefault("ableton.v3.control_surface.components", components)
    sys.modules.setdefault("ableton.v3.control_surface.controls", controls)

    path = os.path.join(SCRIPT_DIR, "keyboard.py")
    spec = _spec(f"{PACKAGE}.keyboard", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[f"{PACKAGE}.keyboard"] = module
    spec.loader.exec_module(module)
    _KEYBOARD_MODULE[0] = module
    return module


def _keyboard():
    """A fresh keyboard component with its listeners captured."""
    module = _load_keyboard()
    component = module.MotionKeyboardComponent()
    component.notifications = []
    component.roles_pushed = []
    component.set_notification_listener(
        lambda title, value: component.notifications.append((title, value))
    )
    component.set_roles_listener(lambda roles: component.roles_pushed.append(list(roles)))
    return component


def test_pressing_a_bank_actually_moves_the_notes():
    """**Behaviour, not structure.** Press each A–H button and check the pitches moved.

    The AST guards said the handlers call `_select_bank` and `set_bank` calls `_recompute`.
    All true, and none of it proves pad 1 plays a different note afterwards. This does.
    """
    keyboard = _keyboard()
    check_equal(keyboard.bank_index, pads.BANK_REST_INDEX, "the keyboard starts on E")
    check_equal(keyboard._pitches[0], 36, "pad 1 is C1 at rest")

    for index, letter in enumerate(pads.BANK_LETTERS):
        keyboard._select_bank(index)
        degrees = pads.bank_step(index)
        # One degree is one bottom-row pad, so pad 1 takes over what pad `degrees` played.
        expected = 36 + pads.white_key_semitone(degrees)
        check_equal(
            keyboard.bank_index, index, f"pressing {letter} must select bank {letter}"
        )
        check_equal(
            keyboard.root_degrees,
            degrees,
            f"bank {letter} is {degrees:+d} degrees from rest",
        )
        check_equal(
            keyboard._pitches[0],
            expected,
            f"bank {letter} must move pad 1 to {expected}",
        )
        # …and the identifier must actually land on the element, which is the thing the
        # framework carries into Live's MIDI map.
        check_equal(
            keyboard.matrix[0].identifier,
            expected,
            f"bank {letter} computed the pitch but never wrote it to the element",
        )
        # The keybed must slide by whole pads: pad 1 now plays what pad 2 played one bank back.
        if index > 0:
            check_equal(
                expected,
                36 + pads.white_key_semitone(degrees),
                "each bank is one bottom-row pad along",
            )
        check_equal(
            keyboard.matrix[0].channel,
            keyboard.__class__.__module__ and _load_keyboard().KEYBOARD_CHANNEL,
            "a live pad stays on the keyboard channel",
        )

    # Re-pressing the selected bank changes nothing but still answers.
    before = list(keyboard._pitches)
    count = len(keyboard.notifications)
    keyboard._select_bank(keyboard.bank_index)
    check_equal(list(keyboard._pitches), before, "re-pressing a bank is a no-op on the layout")
    check_equal(
        len(keyboard.notifications), count + 1, "…but it still puts something on the bar"
    )


def test_exactly_one_bank_button_renders_lit():
    """The radio, checked through the colour `_send_button_color` would actually pick."""
    keyboard = _keyboard()
    module = _load_keyboard()
    for index, letter in enumerate(pads.BANK_LETTERS):
        keyboard._select_bank(index)
        lit = [
            i
            for i, control in enumerate(keyboard._bank_controls())
            if control.rendered_color == module._BANK_COLOURS["on_color"]
        ]
        check_equal(
            lit, [index], f"bank {letter} selected: exactly {letter} may render as selected"
        )
        others = {
            control.rendered_color
            for i, control in enumerate(keyboard._bank_controls())
            if i != index
        }
        check_equal(
            others,
            {module._BANK_COLOURS["color"]},
            "every unselected bank renders in the resting colour",
        )


def test_the_bar_says_root_and_fits_its_slot():
    """The title lives in header slot 0 — one soft-button width, not the whole bar.

    🐛 First hardware run read `Root Shifted`, twelve characters centred over the leftmost
    button, and ran off the edge of the screen. `MAXCHARS_MENU_BUTTON = 16` is what the
    *element* accepts, not what the slot shows.
    """
    module = _load_keyboard()
    title = module.NOTIFICATION_TITLE
    check_equal(title, "Root", "the root-shift bar is titled Root")
    check(
        len(title) <= len("Octave"),
        f"{title!r} is wider than 'Octave', which is the widest title known to fit slot 0",
    )

    keyboard = _keyboard()
    keyboard._select_bank(6)
    check_equal(
        keyboard.notifications[-1], ("Root", "+2"), "bank G reads +2 on the bar"
    )
    keyboard._select_bank(pads.BANK_REST_INDEX)
    check_equal(
        keyboard.notifications[-1], ("Root", "0"), "back at E the bar reads a bare 0"
    )
    keyboard._select_bank(0)
    check_equal(keyboard.notifications[-1], ("Root", "-4"), "bank A reads -4")


def test_a_bottom_lane_pad_is_never_dead():
    """🔑 **The invariant, at every bank × every octave.**

    The gaps in this layout are *missing black keys*, and black keys only exist on the top lane
    — the bottom lane is sixteen white keys and every one is a real note. So a dark pad on the
    bottom row means the layout has been pushed off the end of MIDI. The root lives there, and a
    dead root is nonsense.

    `OCTAVE_LIMIT = 3` used to guarantee this by itself. A–H added four more semitones downward
    and broke it: bank A at octave −3 is −40 semitones and puts pad 1 on note −4. The octave
    limit is now derived from the layout and the bank, so the invariant holds by construction.
    """
    keyboard = _keyboard()
    for index, letter in enumerate(pads.BANK_LETTERS):
        keyboard.set_bank(index)
        for direction, name in ((-1, "down"), (1, "up")):
            # Drive well past the limit in both directions; the clamp must absorb it.
            for _ in range(8):
                keyboard._nudge_octave(direction)
            bottom = keyboard._pitches[: pads.PADS_PER_LANE]
            check(
                all(pitch is not None for pitch in bottom),
                f"bank {letter}, octave driven {name} to the limit ({keyboard.octave:+d}): "
                f"a bottom-lane pad went dead, so a white key fell off the end of MIDI",
            )
            check(
                all(0 <= pitch < 128 for pitch in keyboard._pitches if pitch is not None),
                f"bank {letter}, octave {keyboard.octave:+d}: a pitch left MIDI's range",
            )
            check(
                keyboard.pad_roles[0] != pads.ABSENT,
                f"bank {letter}, octave {keyboard.octave:+d}: pad 1 must be a playable key",
            )
            check(
                any(role == pads.ROOT for role in keyboard.pad_roles),
                f"bank {letter}, octave {keyboard.octave:+d}: the keybed must show a root "
                f"somewhere, or there is no landmark to orient by",
            )
        keyboard.set_octave(0)

    # And selecting a low bank while the octave is already floored must pull the octave up
    # rather than strand the layout: the bank is an explicit choice, the octave is a range.
    keyboard = _keyboard()
    for _ in range(8):
        keyboard._nudge_octave(-1)
    check_equal(keyboard.octave, -3, "at bank E the floor is the musical limit, -3")
    keyboard.set_bank(0)
    check_equal(keyboard.octave, -2, "bank A pulls the octave up to keep pad 1 in range")
    check_equal(
        keyboard._pitches[0],
        36 + pads.white_key_semitone(-4) - 24,
        "pad 1 lands on a real note rather than off the bottom of MIDI",
    )
    check(
        keyboard._pitches[0] >= 0,
        "the whole point: pad 1 must be a playable note, not a negative one",
    )


def test_octave_and_bank_are_different_transforms():
    """Octave transposes rigidly; A-H slides the window. They compose, but they do not add.

    Conflating them is what shipped first: A-H was folded into the semitone term alongside
    Octave, which made it a rigid shift and left the keybed static when you banked.
    """
    keyboard = _keyboard()
    rest_gaps = [i for i, role in enumerate(keyboard.pad_roles) if role == pads.ABSENT]

    # Octave alone: every pad moves by the same amount, the gaps stay put.
    for octaves in (-2, -1, 0, 1, 2):
        keyboard.set_bank(pads.BANK_REST_INDEX)
        keyboard.set_octave(octaves * 12)
        check_equal(
            keyboard._pitches[0],
            36 + octaves * 12,
            f"octave {octaves:+d} moves pad 1 by {octaves * 12} semitones",
        )
        check_equal(
            [i for i, role in enumerate(keyboard.pad_roles) if role == pads.ABSENT],
            rest_gaps,
            f"octave {octaves:+d} must not move the gaps — it is a rigid transposition",
        )

    # Bank alone: the window slides, so the gaps move.
    moved = 0
    for bank in range(pads.BANK_COUNT):
        keyboard.set_octave(0)
        keyboard.set_bank(bank)
        gaps = [i for i, role in enumerate(keyboard.pad_roles) if role == pads.ABSENT]
        if gaps != rest_gaps:
            moved += 1
    check(moved >= 5, "banking must move the gaps for most banks, or the keybed never redraws")

    # Together: the degree shift picks the window, the octave then transposes it.
    for bank in range(pads.BANK_COUNT):
        for octaves in (-2, 0, 2):
            keyboard.set_bank(bank)
            keyboard.set_octave(octaves * 12)
            expected = 36 + pads.white_key_semitone(pads.bank_step(bank)) + octaves * 12
            check_equal(
                keyboard._pitches[0],
                expected,
                f"bank {pads.BANK_LETTERS[bank]} at octave {octaves:+d}: pad 1 must be "
                f"{expected}",
            )


def test_banking_pushes_a_changed_layout_to_the_pad_leds():
    """🐛 **The reported symptom: the 32 pad LEDs did not redraw when banking.**

    Two things have to hold, and only the pair of them makes the keybed follow: the roles must
    actually differ between banks (they could not, while the shift was rigid), and the keyboard
    must push them. This asserts the screen component would receive a *different* list, which is
    what makes `set_pad_roles` repaint rather than early-return.
    """
    keyboard = _keyboard()
    keyboard.roles_pushed.clear()

    seen = []
    for index, letter in enumerate(pads.BANK_LETTERS):
        keyboard._select_bank(index)
        check(
            keyboard.roles_pushed,
            f"bank {letter} produced no roles push at all — the screen is never told",
        )
        seen.append(tuple(keyboard.roles_pushed[-1]))

    changes = sum(1 for a, b in zip(seen, seen[1:]) if a != b)
    check_equal(
        changes,
        len(seen) - 1,
        "every step between adjacent banks must push a different layout, or the pads sit "
        "still while the notes move",
    )


def test_root_offset_maths_survives_negative_values():
    """🐛 `root_offset` was computed with `% 7` and `// 7` applied to *different* terms.

    Python floors toward negative infinity, so `-1 % 7 == 6` and `-1 // 7 == -1`: the old
    expression subtracted B's offset *and* an octave, sending pad 1 to note 13 instead of 35.
    Positive offsets were wrong too — +1 gave 34 where it should give 38, moving the root the
    wrong way entirely. One `divmod`-based helper now covers every case.
    """
    # One white key per step, in the right direction, in both directions.
    expected = {-3: 31, -2: 33, -1: 35, 0: 36, 1: 38, 2: 40, 3: 41}
    for offset, pitch in expected.items():
        check_equal(
            pads.pad_pitches(offset, 0)[0],
            pitch,
            f"root offset {offset:+d} puts pad 1 on note {pitch}",
        )

    # White-key positions must be monotonic and never collide, at any offset or octave.
    for offset in range(-3, 4):
        for octaves in (-2, -1, 0, 1, 2):
            pitches = pads.pad_pitches(offset, octaves * 12)
            real = [p for p in pitches if p is not None]
            check_equal(
                len(set(real)),
                len(real),
                f"no two pads share a pitch at root {offset:+d}, octave {octaves:+d}",
            )
            lane0 = pitches[: pads.PADS_PER_LANE]
            check(
                all(b > a for a, b in zip(lane0, lane0[1:])),
                f"the white-key lane ascends at root {offset:+d}, octave {octaves:+d}",
            )
            # Roles and pitches must agree about which pads are dead.
            check_equal(
                sorted(pads.dead_indices(offset)),
                sorted(i for i, p in enumerate(pitches) if p is None),
                f"roles and pitches agree at root {offset:+d}, octave {octaves:+d}",
            )


def test_pads_never_get_the_dim_state_byte():
    """🐛 The bug that left the whole keybed dark on the first hardware run.

    A pad's state byte accepts Off `0x00`, On `0x7F`, Blink `0x01`, Pulse `0x02` — and nothing
    else. `midi.LED_DIM` (63) is the **button** brightness model; sending it to a pad lights
    nothing at all. Pad brightness comes from the colour instead.
    """
    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    import ast

    tree = ast.parse(source)
    refresh = next(
        (n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "_refresh_pad_leds"),
        None,
    )
    check(refresh is not None, "screen_component must define _refresh_pad_leds")
    if refresh is None:
        return
    for node in ast.walk(refresh):
        if isinstance(node, ast.Attribute) and node.attr == "LED_DIM":
            check(False, "pads have no dim state — 63 is not a valid pad state byte")
    check(True, "no LED_DIM reaches the pads")

    # And the valid values must be exactly the documented set.
    check_equal(
        (midi.LED_OFF, midi.LED_ON, midi.LED_BLINK, midi.LED_PULSE),
        (0x00, 0x7F, 0x01, 0x02),
        "the pad state vocabulary, from the surface XML",
    )


def test_pad_colour_and_state_are_diffed_separately():
    """Studio Pro updates a lit pad with colour-only writes; it does not re-send the state.

    Verified in the track-change capture — channels 2/3/4 carry the new colour and channel 1
    is absent. Re-sending "on" with every colour change is extra traffic and risks retriggering
    the device's own state handling.
    """
    sent = []
    group = leds.PadLeds(send=sent.append)
    group.set(0, (127, 21, 21))
    group.flush()
    check_equal(len(sent), 4, "the first write sends state and colour")

    sent.clear()
    group.set(0, (127, 127, 127))  # colour changes, state does not
    group.flush()
    check_equal(
        [m[0] for m in sent],
        [0x91, 0x92, 0x93],
        "a colour-only change sends colour only — no 0x90 state byte",
    )

    sent.clear()
    group.set(0, (127, 127, 127), state=midi.LED_BLINK)  # state changes, colour does not
    group.flush()
    check_equal([m[0] for m in sent], [0x90], "a state-only change sends the state byte only")


def test_pad_state_passes_blink_and_pulse_through():
    """Pad state accepts Off/On plus Blink (0x01) and Pulse (0x02) — Session mode needs them."""
    sent = []
    pads = leds.PadLeds(send=sent.append)
    for state in (0x00, 0x7F, 0x01, 0x02):
        sent.clear()
        pads.invalidate()
        pads.set(3, (10, 20, 30), state=state)
        pads.flush()
        check_equal(sent[0][2], state, f"pad state {state:#04x} reaches the wire unmodified")


def test_pad_release_writes_the_state_byte_twice():
    """The factory's state *and* animation handlers both release a pad's address.

    The shutdown capture shows two state writes per note, then white RGB. Matching it keeps our
    teardown byte-identical to Studio Pro's — see Motion32_Implementation_Notes.md §5.1.
    """
    sent = []
    pads = leds.PadLeds(send=sent.append)
    count = pads.release()
    check_equal(count, 32 * 5, "32 pads x (2 state + 3 colour)")
    check_equal(
        [tuple(m) for m in sent[:5]],
        [
            (0x90, 36, midi.RESET_LED_STATE),
            (0x90, 36, midi.RESET_LED_STATE),
            (0x91, 36, midi.RESET_RGB),
            (0x92, 36, midi.RESET_RGB),
            (0x93, 36, midi.RESET_RGB),
        ],
        "state off twice, then colour WHITE (not black) — the factory release state",
    )

    # The halos are released once, not twice.
    sent.clear()
    leds.EncoderLeds(send=sent.append, addresses=(0x0E,)).release()
    check_equal(len(sent), 4, "a halo releases with one state write plus three colour writes")


def test_pads_are_declared_as_note_elements():
    """The pad matrix must use MIDI_NOTE_TYPE and must not be passed the forbidden kwargs."""
    import ast

    source = open(os.path.join(SCRIPT_DIR, "elements.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    pad_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in ("add_button_matrix", "add_matrix")
        and any(isinstance(a, ast.Constant) and a.value == "Pads" for a in node.args)
    ]
    check_equal(len(pad_calls), 1, "exactly one pad matrix")
    for call in pad_calls:
        kwargs = {kw.arg: kw.value for kw in call.keywords}
        check(
            "msg_type" in kwargs and "MIDI_NOTE_TYPE" in ast.dump(kwargs["msg_type"]),
            "pads are notes, not CCs — without msg_type=MIDI_NOTE_TYPE they would bind to "
            "CCs 36-67, which are real controls on this device",
        )
        check("channel" not in kwargs, "no channel= on a matrix wrapper (it supplies it)")
        check(
            "element_factory" not in kwargs,
            "no element_factory= on a matrix wrapper (it hard-codes it; the script would "
            "fail to load)",
        )


def test_pad_leds_follow_the_focused_track():
    """Resting colour comes from the track, and both track listeners must repaint the pads.

    Selecting another track and *recolouring the current one* are different events; the
    colour listener only called `_render()`, which does not touch LEDs, so a recolour would
    have left the keybed on the old colour.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read())
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    def calls(function_name, callee):
        node = functions.get(function_name)
        if node is None:
            return False
        return any(
            isinstance(n, ast.Call)
            and isinstance(n.func, ast.Attribute)
            and n.func.attr == callee
            for n in ast.walk(node)
        )

    def any_painter_calls(callee):
        """`_refresh_pad_leds` dispatches to one painter per layout (keyboard / Shift commands /
        Scale), so the assertion is about the family rather than the entry point."""
        return any(
            calls(name, callee)
            for name in functions
            if name.startswith("_refresh_") and "led" in name
        )

    check("bind_pad_leds" in functions, "the surface must be able to hand over the pad LEDs")
    check(
        any_painter_calls("_selected_track_colour"),
        "the pads' resting colour must come from the focused track, not a constant",
    )
    check(
        calls("_track_appearance_listener", "_refresh_pad_leds")
        or any(
            calls(inner, "_refresh_pad_leds")
            for inner in functions
            if inner.startswith("_on_changed")
        ),
        "the track name/colour listener must repaint the pads, not just the screen",
    )
    check(
        calls("_on_selected_track_changed", "_refresh_pad_leds"),
        "changing the selected track must repaint the pads",
    )


def test_keyboard_translates_pads_to_a_piano():
    """The pads must be translated, not just declared.

    Two symptoms, one cause: an element the script declares but does not translate is consumed
    by the control surface, so the pads played chromatically *and* never reached an armed track
    (the press showed in Live's Key/MIDI indicator and made no sound).
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read()
    tree = ast.parse(source)

    classes = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)}
    check("MotionKeyboardComponent" in classes, "keyboard.py must define the component")
    keyboard = classes.get("MotionKeyboardComponent")
    if keyboard is None:
        return
    check(
        any(getattr(b, "id", "") == "PlayableComponent" for b in keyboard.bases),
        "it must extend PlayableComponent — that is what performs the translation",
    )
    methods = {n.name for n in ast.walk(keyboard) if isinstance(n, ast.FunctionDef)}
    check(
        "_note_translation_for_button" in methods,
        "the translation hook is the whole mechanism",
    )
    check(
        "_update_button_color" not in methods,
        "do NOT override _update_button_color — the base hook is empty, which is what keeps "
        "leds.PadLeds the sole writer of the pad addresses. Overriding it creates two writers "
        "on one address, the encoder-halo problem all over again",
    )


def test_dead_pads_are_unique_by_channel():
    """🔑 A control is keyed by `(identifier, channel)`. The gaps must not share a key.

    Four attempts, and only the last is correct:

    | identifier | outcome |
    |---|---|
    | `None` | enabled *and* untranslated — the raw note passes through |
    | `>= 128` | disables the pad, and a disabled element is **released**, so the note floats loose |
    | own note, keyboard channel | collides with whichever real pad is transposed to that number |
    | own note, **own channel** | claimed, unique, silenced by mode ✅ |

    The collision was measured: 54, 58, 61 and 65 are all live translation targets at some
    reachable octave, so pressing a gap fired controls 26 / 28 / 30 and lit *their* pads.

    Real pads keep their layout pitch on the keyboard channel — that is the transposition, and it
    must not be touched.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read())
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    source = open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read()

    constants = {
        t_.id: n.value.value
        for n in ast.walk(tree)
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Constant)
        for t_ in n.targets
        if isinstance(t_, ast.Name)
    }
    keyboard_channel = constants.get("KEYBOARD_CHANNEL")
    dead_channel = constants.get("DEAD_PAD_CHANNEL")
    check(
        isinstance(dead_channel, int) and dead_channel != keyboard_channel,
        f"dead pads need their own channel, distinct from the keyboard's "
        f"(got {dead_channel!r} vs {keyboard_channel!r})",
    )

    translation = functions.get("_note_translation_for_button")
    check(translation is not None, "keyboard.py must define _note_translation_for_button")
    if translation is not None:
        body = "".join(
            ast.dump(n)
            for n in translation.body
            if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant))
        )
        check(
            "_pitches" in body,
            "a real pad must translate to its LAYOUT pitch — that is the transposition, and the "
            "keyboard genuinely plays a piano because of it",
        )
        check("DEAD_PAD_CHANNEL" in body, "a dead pad must be parked on the dead channel")
        check(
            "note_for_index" in body,
            "a dead pad keeps its own note (on its own channel), so it stays claimed",
        )
    check(
        "DEAD_PAD_IDENTIFIER" not in source,
        "out-of-range identifiers are superseded — they disable the pad, and a disabled element "
        "is released rather than consumed",
    )

    # The collision this design removes, demonstrated.
    dead_raw = [pads.note_for_index(i) for i in pads.dead_indices(0)]
    collisions = set()
    for octaves in range(-3, 4):
        played = {p for p in pads.pad_pitches(0, octaves * 12) if p is not None}
        collisions |= {n for n in dead_raw if n in played}
    check_equal(
        sorted(collisions),
        sorted(dead_raw),
        "every gap's own note is a live translation target somewhere in range — which is why "
        "sharing the keyboard channel could never work",
    )


def test_dead_pads_are_silenced_by_mode_not_by_disabling():
    """`enabled = False` releases the element; the note then floats loose and hits another control.

    Silence comes from the per-button **mode** instead: `listenable` consumes the note and passes
    nothing to the track, while every other pad gets `playable_and_listenable`.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read())
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    mode = functions.get("_update_control_from_script")
    check(mode is not None, "keyboard.py must override _update_control_from_script")
    if mode is not None:
        dumped = ast.dump(mode)
        check("listenable" in dumped, "dead pads must be set to the listenable mode")
        check("_is_dead" in dumped, "the mode must be chosen per pad, not matrix-wide")

    held = functions.get("_note_held")
    if held is not None:
        check(
            "_is_dead" in ast.dump(held),
            "a dead pad must never enter the held set, or it would light green",
        )

    check(
        "DEAD_PAD_IDENTIFIER" not in open(
            os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8"
        ).read(),
        "the out-of-range-identifier approach is superseded — it disables the pad, and a "
        "disabled element is released, not consumed",
    )


def test_no_two_live_pads_ever_share_a_pitch():
    """🔑 The invariant the whole pad scheme rests on — and the one scales will break.

    A control is keyed by `(identifier, channel)`. Two *live* pads carrying the same pitch is one
    key with two controls, which is precisely the collision that made pressing a gap fire someone
    else's pad. The diatonic layout satisfies this by construction; **a scale layout will not,
    unless its generator is written to.**

    Checked across the full space A-H and Octave can reach, plus margin.
    """
    for offset in range(-6, 7):
        for octaves in range(-4, 5):
            pitches = pads.pad_pitches(offset, octaves * 12)
            live = [p for p in pitches if p is not None]
            check_equal(
                len(set(live)),
                len(live),
                f"no duplicate pitches at root {offset:+d}, octave {octaves:+d}",
            )
            check(
                all(0 <= p < 128 for p in live),
                f"every live pitch is a real MIDI note at root {offset:+d}, "
                f"octave {octaves:+d}",
            )
            # And roles must agree — an out-of-range pitch has to read as ABSENT, or the pad
            # would be lit white by the renderer and silenced by the keyboard.
            check_equal(
                sorted(pads.dead_indices(offset)),
                sorted(i for i, p in enumerate(pads.pad_pitches(offset, 0)) if p is None),
                f"roles and pitches agree at root {offset:+d}",
            )


def test_a_naive_scale_layout_would_break_the_invariant():
    """Documents *why* Phase 10 needs a purpose-built generator, with the failure demonstrated.

    The obvious pentatonic layout — bottom lane = scale degrees, top lane = "the note between" —
    produces **fifteen** duplicate pitches, because in a 5-note scale the note between two
    degrees is usually just the next degree, which is already on the bottom lane.

    That is not a hypothetical: it is the same one-key-two-controls collision, and it would
    reproduce the dead-pad symptoms exactly. A scale generator must therefore either leave the
    top lane dead, or map it to something that cannot already appear below.
    """
    pentatonic = (0, 2, 4, 7, 9)

    def naive(mask):
        out = [None] * 32
        for i in range(16):
            octave, degree = divmod(i, len(mask))
            out[i] = 36 + 12 * octave + mask[degree]
            next_octave, next_degree = divmod(i + 1, len(mask))
            following = 36 + 12 * next_octave + mask[next_degree]
            out[16 + i] = following if following - out[i] > 1 else None
        return out

    live = [p for p in naive(pentatonic) if p is not None]
    duplicates = sorted({p for p in live if live.count(p) > 1})
    check(
        len(duplicates) > 0,
        "this test exists to record the failure — if the naive layout stopped colliding, the "
        "constraint it documents would need re-deriving",
    )
    check_equal(
        len(duplicates),
        15,
        "the naive pentatonic layout collides on 15 pitches; a real generator must not",
    )


def test_layout_change_refreshes_both_translation_and_mode():
    """🐛 A layout change must push **both** halves, or a pad's mode goes stale.

    Two passes set two different things:

    * `_update_note_translations()` — the pad's **identifier** and `enabled`;
    * `_update_control_from_script()` — the pad's **mode**, and mode is the only thing that
      makes a dead pad silent.

    Refreshing only the first means a pad that has just *become* dead keeps
    `playable_and_listenable` and still sounds, while one that has just become alive keeps
    `listenable` and stays mute. Invisible today, because an octave shift does not move the
    gaps — and guaranteed to appear the moment A-H banking or a non-diatonic scale does.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read())
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    recompute = functions.get("_recompute")
    check(recompute is not None, "keyboard.py must define _recompute")
    if recompute is None:
        return
    called = {
        n.func.attr
        for n in ast.walk(recompute)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
    }
    for required in ("_update_note_translations", "_update_control_from_script"):
        check(
            required in called,
            f"_recompute must call {required}() — a layout change that refreshes only one of "
            f"the two passes leaves the other stale",
        )

    # Every public entry point that changes the layout must go through _recompute.
    for setter in ("set_root_offset", "set_octave"):
        node = functions.get(setter)
        if node is None:
            continue
        setter_calls = {
            n.func.attr
            for n in ast.walk(node)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
        }
        check(
            "_recompute" in setter_calls,
            f"{setter}() must go through _recompute, not update one pass itself",
        )


def test_deadness_has_a_single_source():
    """Roles must be *derived* from pitches, never computed a second time.

    Two independent opinions about which pads are dead is the §6b-16 failure, and it gets worse
    with scales: a pentatonic or blues layout has a different number of gaps in different
    places, so any second computation will disagree with the pitches — silently, because a
    disagreement shows up as a pad that looks dead but plays, or plays but looks dead.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "pads.py"), encoding="utf-8").read())
    roles = next(
        (n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "pad_roles"),
        None,
    )
    check(roles is not None, "pads.py must define pad_roles")
    if roles is not None:
        body = "".join(
            ast.dump(n)
            for n in roles.body
            if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant))
        )
        check(
            "pad_pitches" in body,
            "pad_roles must derive deadness from pad_pitches, not recompute it",
        )
        check(
            "NO_BLACK_KEY_ABOVE" not in body,
            "pad_roles must not re-test the black-key pattern — that is the second opinion",
        )

    # And they must agree, for every root offset and octave, by construction.
    for offset in range(-3, 4):
        expected = sorted(
            i for i, p in enumerate(pads.pad_pitches(offset, 0)) if p is None
        )
        check_equal(
            sorted(pads.dead_indices(offset)),
            expected,
            f"roles and pitches agree about dead pads at root {offset:+d}",
        )


def test_pads_flash_while_held():
    """Held pads flash green, and the keyboard reports them rather than painting them.

    `leds.PadLeds` is the single writer of the pad addresses, so the keyboard component hears
    the press (its matrix is playable *and* listenable) and hands the held set to the screen
    component, which repaints. Two writers on one address is the encoder-halo problem.
    """
    import ast

    keyboard_src = open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read()
    tree = ast.parse(keyboard_src)
    # Structural, not a substring search: the phrase also appears in the docstring, so
    # `"matrix_always_listenable" in source` stayed true when the call was deleted. Check that
    # __init__ actually sets it.
    init = next(
        (n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "__init__"),
        None,
    )
    check(init is not None, "keyboard.py must define __init__")
    if init is not None:
        sets_listenable = any(
            isinstance(n, ast.Constant) and n.value == "matrix_always_listenable"
            for n in ast.walk(init)
        )
        check(
            sets_listenable,
            "__init__ must set matrix_always_listenable — without it the matrix is "
            "playable-only and the component never sees a press, so pads cannot flash",
        )
    methods = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    for hook in ("_on_matrix_pressed", "_on_matrix_released", "set_held_listener"):
        check(hook in methods, f"keyboard.py must define {hook}")

    screen_tree = ast.parse(
        open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    )
    screen_methods = {
        n.name for n in ast.walk(screen_tree) if isinstance(n, ast.FunctionDef)
    }
    functions = screen_methods
    check("set_pads_held" in screen_methods, "the screen component must accept the held set")

    # `_refresh_pad_leds` dispatches to one painter per layout — the piano, the Shift command
    # overlay, and Scale's Locked/Guide. **Every** painter must honour the held set, or a pad
    # would stop flashing green in one layout and nowhere else, which is the hardest kind of
    # inconsistency to notice.
    painters = [
        n
        for n in ast.walk(screen_tree)
        if isinstance(n, ast.FunctionDef)
        and n.name.startswith("_refresh_")
        and n.name.endswith("_leds")
        and "pad" in n.name or (isinstance(n, ast.FunctionDef) and n.name in (
            "_refresh_keyboard_leds", "_refresh_command_leds", "_refresh_scale_leds"
        ))
    ]
    painters = [n for n in painters if n.name != "_refresh_pad_leds"]
    check(
        len(painters) >= 2,
        f"expected at least the keyboard and Shift-command pad painters, found "
        f"{[n.name for n in painters]}",
    )
    # ⚠️ Scale mode deliberately has **no painter of its own**. It reports roles through
    # `keyboard.pad_roles` and the keyboard painter draws them, so the lights and the notes come
    # from one list. A separate scale painter regenerated the layout independently, which is the
    # §5.3b second-opinion failure and is what hid the A-H banking bug: the LEDs moved and the
    # pitches did not.
    check(
        "_refresh_scale_leds" not in functions,
        "Scale mode must not have its own pad painter — it reports roles and the keyboard "
        "painter draws them, so the lights cannot describe a layout the notes do not play",
    )
    for painter in painters:
        dumped = ast.dump(painter)
        check(
            "PAD_PLAYED" in dumped,
            f"{painter.name}: a held pad must use the played colour, not its resting colour",
        )
        check(
            "_pads_held" in dumped,
            f"{painter.name}: every pad layout must consult the held set",
        )
    check_equal(
        screen.Palette.PAD_PLAYED, palette.rgb7(0x00FF00), "the played colour is green"
    )


def test_pads_are_never_taken_over_from_the_player():
    """🔑 The fix for swallowed notes, and the most important guard in this file.

    `PlayableComponent._update_control_from_script` is, from the bytecode:

        takeover_pads = self._takeover_pads or len(self.pressed_pads) > 0
        mode = PlayableControl.Mode.listenable if takeover_pads else self._default_playable_mode
        for button in self.matrix:
            button.set_mode(mode)

    So **the moment any pad goes down the whole matrix flips to `listenable`**, which consumes
    notes rather than passing them on. That is right for a drum rack (hold a pad to take the
    grid over for selection) and completely wrong for a keyboard: it swallowed the very note
    that lit the pad, and made a second press behave differently from the first.

    `matrix_always_listenable=True` does not prevent it — that only sets the *default* mode,
    and the takeover overrides the default. The override must therefore keep the mode constant.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read())
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    override = functions.get("_update_control_from_script")
    check(
        override is not None,
        "keyboard.py MUST override _update_control_from_script — without it, holding a pad "
        "makes the matrix consume notes instead of playing them",
    )
    if override is None:
        return

    # Dump the executable body only. The docstring quotes the base class's buggy logic
    # verbatim, so including it would match every term we are trying to forbid.
    body = [
        n
        for n in override.body
        if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant))
    ]
    dumped = "".join(ast.dump(n) for n in body)
    check(
        "listenable" not in dumped or "_default_playable_mode" in dumped,
        "the override must not select the listenable mode",
    )
    check(
        "pressed_pads" not in dumped and "_takeover_pads" not in dumped,
        "the mode must not depend on whether a pad is held — that dependency IS the bug",
    )
    check(
        "_default_playable_mode" in dumped,
        "every pad stays on the default playable mode, always",
    )
    check(
        any(
            isinstance(n, ast.Call)
            and isinstance(n.func, ast.Attribute)
            and n.func.attr == "set_mode"
            for n in ast.walk(override)
        ),
        "the override must still set the mode on each button",
    )

    # Our own bookkeeping must precede the base class's, so a failure in `pressed_pads`
    # handling cannot leave a pad lit.
    for handler in ("_on_matrix_pressed", "_on_matrix_released"):
        node = functions.get(handler)
        check(node is not None, f"keyboard.py must define {handler}")
        if node is None:
            continue
        calls = [
            n.func.attr
            for n in ast.walk(node)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
        ]
        check(
            calls and calls[0] == "_note_held",
            f"{handler} must record the held state before delegating (got {calls[:1]})",
        )


def test_dead_pads_get_unique_out_of_range_identifiers():
    """🐛 Disabled pads kept their declared raw note, and collided with real translations.

    The base `_update_note_translations` only assigns properties to buttons it *enables*:

        for button in self.matrix:
            if self._button_should_be_enabled(button):
                self._set_button_control_properties(button)
                button.enabled = True
            else:
                button.enabled = False

    So a dead pad never got an identifier and kept its **declared** note — 54, 58, 61, 65. Those
    are real notes and also translation targets for other pads: three of the four collide at the
    default octave and all four at +12. Two controls on one identifier means a press can be
    delivered to the wrong control, which produced every reported symptom at once — dead pads
    sounding, dead pads lighting a *different* pad, and lit pads not turning green.

    So: assign properties to **every** button, and give dead pads unique identifiers >= 128
    where no incoming 7-bit note can reach them.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read())
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    override = functions.get("_update_note_translations")
    check(
        override is not None,
        "keyboard.py MUST override _update_note_translations — the base skips disabled pads, "
        "leaving them on their raw note where they collide with real translations",
    )
    if override is not None:
        body = [
            n
            for n in override.body
            if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant))
        ]
        dumped = "".join(ast.dump(n) for n in body)
        check(
            "_set_button_control_properties" in dumped,
            "every button must get its properties assigned",
        )
        # The assignment must not be inside a conditional on enabled-ness.
        conditional_assign = any(
            isinstance(n, ast.If)
            and "_set_button_control_properties" in ast.dump(n)
            for n in ast.walk(override)
        )
        check(
            not conditional_assign,
            "properties must be assigned unconditionally — skipping disabled pads is the bug",
        )

    # And the identifiers themselves must be unique and out of range.
    # ⚠️ Superseded approach, kept as a negative check. Out-of-range identifiers *disabled* the
    # dead pads, and a disabled element is released rather than consumed — which is what let the
    # raw note escape and hit another control. Identity translation keeps them claimed instead.
    check(
        "DEAD_PAD_IDENTIFIER" not in open(
            os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8"
        ).read(),
        "the out-of-range-identifier approach is superseded — it disables the pad, and a "
        "disabled element is released, not consumed",
    )

    # Prove the collision the fix removes: every dead pad's *declared* note is a real
    # translation target at some reachable octave.
    dead_raw = [pads.note_for_index(i) for i, r in enumerate(pads.pad_roles(0)) if r == pads.ABSENT]
    collisions = set()
    for octaves in range(-3, 4):
        played = {p for p in pads.pad_pitches(0, octaves * 12) if p is not None}
        collisions |= {n for n in dead_raw if n in played}
    check_equal(
        sorted(collisions),
        sorted(dead_raw),
        "every dead pad's raw note collides with a real translation somewhere in range — "
        "which is why leaving them untranslated broke the keyboard",
    )


def test_pad_event_logging_is_bounded():
    """Diagnostics must survive the traffic they observe — playing must not flood Log.txt."""
    import ast

    source = open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    limits = {
        t.id: n.value.value
        for n in ast.walk(tree)
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Constant)
        for t in n.targets
        if isinstance(t, ast.Name)
    }
    cap = limits.get("MAX_LOGGED_PAD_EVENTS")
    check(
        isinstance(cap, int) and 0 < cap <= 100,
        f"pad event logging must be capped at a small number (got {cap!r})",
    )
    held = next(
        (n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "_note_held"),
        None,
    )
    if held is not None:
        check(
            "_events_logged" in ast.dump(held),
            "_note_held must consult the counter before logging",
        )


def test_octave_buttons_are_wired_and_clamped():
    """Octave +/- transposes the whole keybed by 12 semitones, within a safe range."""
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read())
    assigned = {
        t.id
        for n in ast.walk(tree)
        if isinstance(n, ast.Assign)
        for t in n.targets
        if isinstance(t, ast.Name)
    }
    for control in ("octave_up_button", "octave_down_button"):
        check(control in assigned, f"keyboard.py must declare {control}")

    nudge = next(
        (n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "_nudge_octave"),
        None,
    )
    check(nudge is not None, "there must be one place that moves the octave")
    if nudge is not None:
        dumped = ast.dump(nudge)
        check("max" in dumped and "min" in dumped, "the octave must be clamped, not unbounded")

    # And the transposition must actually reach the pitches.
    for octaves in (-1, 0, 1, 2):
        shifted = pads.pad_pitches(0, octaves * 12)
        base = pads.pad_pitches(0, 0)
        check_equal(
            [p for p in shifted if p is not None],
            [p + octaves * 12 for p in base if p is not None],
            f"{octaves:+d} octave shifts every real pad by {octaves * 12} semitones",
        )
        check_equal(
            [i for i, p in enumerate(shifted) if p is None],
            [i for i, p in enumerate(base) if p is None],
            "transposing must not change which pads are dead",
        )


def test_keyboard_coordinate_order_is_row_first():
    """`button.coordinate` is `(y, x)`, verified from the framework's own bytecode.

    `DrumGroupComponent._button_coordinates_to_pad_index` opens with `y, x = coordinates`.
    Unpacking it the other way transposes the keyboard — a plausible-looking wrong layout
    rather than a crash, which is the hardest kind of bug to notice.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read())
    index_for = next(
        (n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "_index_for"),
        None,
    )
    check(index_for is not None, "keyboard.py must define _index_for")
    if index_for is None:
        return
    unpacked = [
        [e.id for e in n.targets[0].elts]
        for n in ast.walk(index_for)
        if isinstance(n, ast.Assign)
        and isinstance(n.targets[0], ast.Tuple)
        and all(isinstance(e, ast.Name) for e in n.targets[0].elts)
    ]
    check_equal(
        unpacked,
        [["row", "column"]],
        "button.coordinate unpacks as (row, column) — the framework's own (y, x)",
    )


def test_dead_pads_are_disabled_not_silently_wrong():
    """The four gap pads must produce a NON-int identifier, which is how the base disables them.

    `PlayableComponent._button_should_be_enabled` is
    `isinstance(identifier, int) and identifier < 128`. Returning a real pitch for a gap pad
    would make it play a note the keyboard does not have; returning None makes it dead.
    """
    roles = pads.pad_roles(0)
    pitches = pads.pad_pitches(0)
    for index, role in enumerate(roles):
        if role == pads.ABSENT:
            check_equal(
                pitches[index],
                None,
                f"pad {index} (note {pads.note_for_index(index)}) has no black key, so it "
                f"must have no pitch and be disabled",
            )
        else:
            check(
                isinstance(pitches[index], int) and 0 <= pitches[index] < 128,
                f"pad {index} must carry a real, in-range pitch",
            )


def test_keyboard_translation_is_recomputed_only_on_change():
    """Latency rule: the translation is static, recomputed on root/octave change only.

    `Motion32_Scale_and_Chord_Engine.md` §5.0 — no Python in the pad->note path. If the
    setters ever recomputed unconditionally, or the translation moved into a per-note handler,
    playing would inherit our thread's scheduling jitter.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read())
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    for setter in ("set_root_offset", "set_octave"):
        node = functions.get(setter)
        check(node is not None, f"keyboard.py must define {setter}")
        if node is None:
            continue
        check(
            any(isinstance(n, ast.Return) for n in ast.walk(node)),
            f"{setter}() must early-return when nothing changed, not recompute every call",
        )
    recompute = functions.get("_recompute")
    check(recompute is not None, "there must be a single _recompute")
    if recompute is not None:
        called = {
            n.func.attr
            for n in ast.walk(recompute)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
        }
        check(
            "_update_note_translations" in called,
            "_recompute must push the new mapping into the elements",
        )


def test_one_colour_conversion_layer():
    """Phase 4's architectural requirement, enforced.

    Screen colour and LED colour must come from the *same* function or they drift — a track
    could read one hue on the display and another on its pad, and nothing would fail. So the
    `>> 1` conversion may be written exactly once in the package, in `palette.py`, and every
    other module must import it.
    """
    import ast

    definitions = []
    rederivers = []
    for filename in sorted(os.listdir(SCRIPT_DIR)):
        if not filename.endswith(".py"):
            continue
        source = open(os.path.join(SCRIPT_DIR, filename), encoding="utf-8").read()
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "rgb7":
                definitions.append(filename)
            # A right-shift by 1 applied to a masked byte is the conversion, open-coded.
            if (
                isinstance(node, ast.BinOp)
                and isinstance(node.op, ast.RShift)
                and isinstance(node.right, ast.Constant)
                and node.right.value == 1
                and filename != "palette.py"
            ):
                rederivers.append(filename)

    check_equal(
        definitions,
        ["palette.py"],
        "rgb7 must be defined exactly once, in palette.py — a second definition is how the "
        "screen and the LEDs start disagreeing about a colour",
    )
    check_equal(
        sorted(set(rederivers)),
        [],
        "no module may open-code the 8->7 bit conversion; import rgb7 from palette instead",
    )


def test_screen_and_leds_share_the_conversion():
    """`screen.Palette` must be built from the shared function, not from literals."""
    check_equal(
        screen.rgb7,
        palette.rgb7,
        "screen.rgb7 is palette.rgb7, not a copy",
    )
    # A Live colour fed through the shared layer produces the identical triple the screen
    # palette would produce for the same hex — that is what "one conversion layer" buys.
    check_equal(
        palette.live_rgb7(FakeColoured(0x0069CC)),
        screen.Palette.HEADER_BACKGROUND,
        "a Live object coloured #0069CC matches the chrome value for #0069CC",
    )


def test_framework_colours_are_built_from_the_shared_layer():
    """`colors.py` imports the framework so the suite cannot execute it — check structurally.

    It must import the conversion rather than re-deriving it, and its dynamic Live-colour
    helpers must go through `live_rgb7`.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "colors.py"), encoding="utf-8").read()
    tree = ast.parse(source)

    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "palette":
            imported |= {alias.name for alias in node.names}
    check(
        "rgb7" in imported,
        "colors.py must import rgb7 from palette rather than defining its own conversion",
    )
    check(
        "live_rgb7" in imported,
        "colors.py must import live_rgb7 so Live objects use their real colour",
    )

    functions = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    for required in ("color_from_live", "color_from_rgb7"):
        check(
            required in functions,
            f"colors.py must expose {required}() so components can colour from a Live object",
        )

    # The cache is what keeps this off the allocation path during repaints. Check it
    # structurally: a module-level dict that `color_from_rgb7` both reads and writes. An
    # earlier version of this assertion just looked for the name anywhere in the file, which
    # still passed when the module-level dict was deleted — the name survived inside the
    # function body. A substring check is not a structural check.
    module_level_dicts = {
        target.id
        for node in tree.body
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict)
        for target in node.targets
        if isinstance(target, ast.Name)
    }
    builder = next(
        (n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "color_from_rgb7"),
        None,
    )
    read, written = set(), set()
    if builder is not None:
        for node in ast.walk(builder):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                read.add(node.id)
            if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name):
                if isinstance(node.ctx, ast.Store):
                    written.add(node.value.id)
    cached = module_level_dicts & read & written
    check(
        bool(cached),
        "dynamic colours must be memoised in a module-level dict that color_from_rgb7 both "
        "reads and writes — framework colours are re-read on every layer grab, so building a "
        "fresh ComplexColor per repaint would churn allocations on a hot path",
    )


class FakeLiveParameter:
    """Minimal stand-in for a Live device parameter."""

    def __init__(self, name="Freq", value=0.5, minimum=0.0, maximum=1.0):
        self.name = name
        self.value = value
        self.min = minimum
        self.max = maximum


class FakeParameterInfo:
    """The framework's `ParameterInfo(parameter=..., name=...)` shape.

    Reproduced from the decompiled `parameter_info.pyc`: the *label* lives on the info
    object (Live's curated bank definitions rename parameters per bank), while min/max/
    value live on the wrapped parameter.
    """

    def __init__(self, parameter, name):
        self.parameter = parameter
        self.name = name


class FakeDeviceComponent:
    def __init__(self, entries, bank_name="Filter", device=None):
        self.parameters = entries
        self.bank_name = bank_name
        self.bank_index = 0
        self.device = device


def test_parameter_info_is_unwrapped():
    """Regression for a bug the framework source exposed: `DeviceComponent.parameters`
    yields `ParameterInfo` wrappers, so reading `.min`/`.value` off them directly gives
    nothing and every halo renders as zero."""
    raw = FakeLiveParameter(name="Frequency", value=0.75)
    info = FakeParameterInfo(raw, name="Freq")  # bank-specific label differs

    entry = parameters._as_entry(info)
    check_equal(entry.name, "Freq", "label must come from ParameterInfo.name, not the parameter")
    check(entry.parameter is raw, "entry must expose the underlying Live parameter")
    check(entry.assigned, "a wrapped valid parameter is assigned")

    # A bare Live parameter is still accepted.
    entry = parameters._as_entry(raw)
    check(entry.parameter is raw, "a bare Live parameter should be accepted directly")
    check_equal(entry.name, "Frequency", "bare parameter falls back to parameter.name")

    # Junk and None degrade to an unassigned slot rather than raising in a listener.
    check_equal(parameters._as_entry(None), parameters.EMPTY_ENTRY, "None -> empty slot")
    check(not parameters._as_entry(object()).assigned, "unknown object -> unassigned slot")


def test_parameter_source_pads_and_truncates():
    infos = [FakeParameterInfo(FakeLiveParameter(name=f"P{i}"), f"P{i}") for i in range(3)]
    source = parameters.ParameterSource()
    source.bind_device_component(FakeDeviceComponent(infos))

    entries = source.entries()
    check_equal(len(entries), 8, "always exactly 8 slots, one per encoder")
    check(all(e.assigned for e in entries[:3]), "the first three are assigned")
    check(not any(e.assigned for e in entries[3:]), "the rest are unassigned, not missing")
    check_equal(source.bank_label(), "Filter", "bank label comes from DeviceComponent.bank_name")

    # More than 8 must be truncated, never overflow the tiles.
    many = [FakeParameterInfo(FakeLiveParameter(), f"P{i}") for i in range(20)]
    source.bind_device_component(FakeDeviceComponent(many))
    check_equal(len(source.entries()), 8, "a long bank is truncated to 8")

    # No component at all is a legal state (script loaded before Device exists).
    source.bind_device_component(None)
    check_equal(len(source.entries()), 8, "8 empty slots when there is no component")
    check(not any(e.assigned for e in source.entries()), "all unassigned with no component")
    check_equal(source.bank_label(), "", "no bank label without a component")


def test_parameter_source_survives_a_hostile_component():
    """Every accessor is inside a listener path; a raising property must not propagate."""

    class Exploding:
        @property
        def parameters(self):
            raise RuntimeError("device went away")

        @property
        def bank_name(self):
            raise RuntimeError("device went away")

        @property
        def device(self):
            raise RuntimeError("device went away")

    source = parameters.ParameterSource()
    source.bind_device_component(Exploding())
    check_equal(len(source.entries()), 8, "a raising component yields 8 empty slots")
    check_equal(source.bank_label(), "", "a raising bank_name yields empty")
    check_equal(source.device(), None, "a raising device yields None")


# Names the framework's `Component` owns, read from the decompiled
# `Resources/control_surface/component.pyc`. Defining any of these on a subclass shadows
# the base class: a read-only `_song` property made `Component.__init__` raise
# "property '_song' of '...' object has no setter" and the component failed to build.
COMPONENT_RESERVED_NAMES = {
    # assigned by Component.__init__
    "name",
    "is_private",
    "_parent",
    "_explicit_is_enabled",
    "_recursive_is_enabled",
    "_is_enabled",
    "_song",
    "_layer",
    "_child_components",
    "_has_task_group",
    "_initializing_children",
    # properties on Component
    "application",
    "song",
    "parent",
    "is_root",
    "layer",
    "canonical_parent",
    "num_layers",
    "any_clipboard_has_content",
    "_tasks",
}

# Methods we legitimately override by calling super().
COMPONENT_OVERRIDABLE = {"disconnect", "update", "set_enabled", "is_enabled", "on_enabled_changed"}


def test_components_do_not_shadow_framework_attributes():
    """Regression for a real failed build of the screen component."""
    import ast

    for filename in ("screen_component.py", "transport.py"):
        path = os.path.join(SCRIPT_DIR, filename)
        if not os.path.exists(path):
            continue
        tree = ast.parse(open(path, encoding="utf-8").read())
        for node in ast.walk(tree):
            if not isinstance(node, ast.ClassDef):
                continue
            defined = set()
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    defined.add(item.name)
                elif isinstance(item, ast.Assign):
                    for target in item.targets:
                        if isinstance(target, ast.Name):
                            defined.add(target.id)
            # Attributes assigned on self inside methods count too.
            for sub in ast.walk(node):
                if isinstance(sub, ast.Assign):
                    for target in sub.targets:
                        if (
                            isinstance(target, ast.Attribute)
                            and isinstance(target.value, ast.Name)
                            and target.value.id == "self"
                        ):
                            defined.add(target.attr)
            clashes = (defined & COMPONENT_RESERVED_NAMES) - COMPONENT_OVERRIDABLE
            check_equal(
                sorted(clashes),
                [],
                f"{filename}:{node.name} shadows framework Component attribute(s)",
            )


def test_screen_component_is_framework_registered():
    """The screen component must be built by the framework, not by hand.

    `ComponentMap._create_component_map` ends with
    `self.update(specification.component_map)`, so a new key is registered alongside the
    built-ins and instantiated lazily *inside* the surface's dependency guard. That
    injection is what supplies `self.song` and `self._tasks` (the value-timeout timer needs
    the latter). Hand-constructing it gets neither, and passing `parent=<surface>` makes
    `Component.__init__` call `add_children` on a non-Component.
    """
    import ast

    surface_src = open(os.path.join(SCRIPT_DIR, "__init__.py"), encoding="utf-8").read()
    tree = ast.parse(surface_src)

    # Must never be instantiated directly.
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "MotionScreenComponent"
        ):
            check(False, "MotionScreenComponent must not be constructed by hand")

    # Must be registered in Specification.component_map.
    registered = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "component_map":
                    for key in getattr(node.value, "keys", []):
                        if isinstance(key, ast.Constant):
                            registered.add(key.value)
    check("Motion_Screen" in registered, "Motion_Screen must be in Specification.component_map")
    check("Transport" in registered, "Transport override must remain in component_map")

    # And it needs a create_mappings entry so the framework builds its Layer (which is what
    # binds encoder_touch_buttons).
    check("Motion_Screen" in MAPPINGS, "Motion_Screen needs a create_mappings entry")
    check(
        "Main_Modes" in MAPPINGS,
        "Main_Modes must exist so the Plugin button can switch the view",
    )
    check_equal(
        MAPPINGS["Motion_Screen"].get("encoder_touch_buttons"),
        "encoder_touch_buttons",
        "the screen needs encoder touch bound to reveal values",
    )


def test_plugin_mode_owns_the_encoders():
    """The device view is reached with the Plugin button, and the encoders are mapped only
    there — otherwise they would move parameters while another view is on screen."""
    mapping = MAPPINGS
    modes = mapping.get("Main_Modes")
    check(isinstance(modes, dict), "Main_Modes should be a dict of modes and mode buttons")
    if not isinstance(modes, dict):
        return

    for button in ("song_button", "plugin_button"):
        check(button in modes, f"Main_Modes needs {button}")

    plugin = modes.get("plugin")
    check(isinstance(plugin, dict), "there must be a 'plugin' mode")
    parts = plugin.get("modes", [plugin]) if isinstance(plugin, dict) else []
    components = {part.get("component") for part in parts if isinstance(part, dict)}
    check("Device" in components, "plugin mode drives the Device component")
    encoder_part = next(
        (part for part in parts if isinstance(part, dict) and part.get("component") == "Device"),
        {},
    )
    check_equal(
        encoder_part.get("parameter_controls"),
        "encoders",
        "the encoders belong to plugin mode, not the global layer",
    )

    mode_names = [
        name
        for name, value in modes.items()
        if isinstance(value, dict) and not name.endswith("_button")
    ]

    # The real invariant is about *elements*, not components: the same component may appear
    # globally and inside a mode (the factory scripts do exactly that — global Transport
    # buttons plus per-mode Transport encoders). What must not happen is one element being
    # bound twice in layers that are active at the same time, i.e. global + any one mode.
    # Reuse across two different modes is fine — they are mutually exclusive.
    def elements_of(section):
        found = set()
        if not isinstance(section, dict):
            return found
        for key, value in section.items():
            if key in ("component", "behaviour", "selector", "index", "modes", "enable"):
                continue
            if isinstance(value, str):
                found.add(value)
        for part in section.get("modes", []) if isinstance(section.get("modes"), list) else []:
            found |= elements_of(part)
        return found

    global_elements = set()
    for name, section in mapping.items():
        if name == "Main_Modes":
            continue
        global_elements |= elements_of(section)

    for name in mode_names:
        overlap = global_elements & elements_of(modes[name])
        check_equal(
            sorted(overlap),
            [],
            f"element(s) bound both globally and in mode '{name}' — two owners, one control",
        )

    # Within a single mode, no element may be claimed by two of its parts either.
    for name in mode_names:
        spec = modes[name]
        parts = spec.get("modes", [spec]) if isinstance(spec, dict) else []
        seen = {}
        for part in parts:
            for element in elements_of(part):
                owner = part.get("component") if isinstance(part, dict) else "?"
                check(
                    element not in seen,
                    f"mode '{name}': {element} claimed by both {seen.get(element)} and {owner}",
                )
                seen[element] = owner

    # Every declared mode button must correspond to a real mode, or the framework binds a
    # control for a mode that was never added.
    for key in modes:
        if key.endswith("_button") and key != "cycle_mode_button":
            check(
                key[: -len("_button")] in mode_names,
                f"{key} has no matching mode",
            )

    # Every mode must have content; an empty mode spec is a needless risk.
    for name in mode_names:
        spec = modes[name]
        check(bool(spec), f"mode '{name}' is empty")

    check(len(mode_names) >= 2, "expected several modes")
    check_equal(mode_names[0], "song", "the first mode listed is the startup default")


def test_params_view_shows_label_and_value_together():
    """Template 3's whole advantage: two independent text elements per tile.

    Identified as the factory's Song/Timeline screen from a photo of Studio Pro — blue header
    title, grey centre bar, eight two-line tiles. Because label and value are separate
    elements, Song mode needs no reveal-on-touch (that exists only because Template 0 has one
    text element per tile).
    """
    recorder, model = make_model()
    view = display.ParamsView(model)
    view.activate()
    view.render(sample_params_content())
    model.flush()

    # Template select must be Params (3), not Main (0).
    check_equal(
        recorder.messages[0],
        (0xF0, 0x08, 0x26, 0x20, screen.TEMPLATE_PARAMS, 0xF7),
        "the first message should select template 3",
    )

    def text_at(zone, element):
        for message in recorder.messages:
            if (
                len(message) > 7
                and message[4] == screen.TEMPLATE_PARAMS
                and message[5] == zone
                and message[6] == element
                and message[7] == midi.ATTR_TEXT
            ):
                return "".join(chr(b) for b in message[8:-1])
        return None

    # Header title and the grey centre bar.
    check_equal(text_at(1, 5), "Session", "header shows which Live view is up")
    check_equal(text_at(7, 1), "Lead Synth 2", "the grey centre bar shows the selected track")

    # Tile 0: label and value are DIFFERENT elements, both populated.
    label_zone, label_element = screen.Params.tile_label(0)
    value_zone, value_element = screen.Params.tile_value(0)
    check(
        (label_zone, label_element) != (value_zone, value_element),
        "label and value must be separate elements",
    )
    check_equal(text_at(label_zone, label_element), "Tempo", "tile 0 label")
    check_equal(text_at(value_zone, value_element), "124.0", "tile 0 value")

    # A full word survives here where Template 0 would have abbreviated it to 7 chars.
    check_equal(text_at(*screen.Params.tile_label(2)), "Loop Start", "full label, not 'LoopSt'")
    check_equal(
        formatting.compactify("Loop Start", formatting.MAXCHARS_ENCODER_LABEL),
        "LoopSta",
        "for contrast: Template 0's 7-char budget would have mangled it",
    )
    check_equal(
        formatting.compactify("Position", formatting.MAXCHARS_ENCODER_LABEL),
        "Pstn",
        "and 'Position' would have lost its vowels entirely on Template 0",
    )

    # No bar/arc attribute may ever be sent to Template 3 — it has none.
    for message in recorder.messages:
        if len(message) > 7 and message[4] == screen.TEMPLATE_PARAMS:
            check(
                message[7] != midi.ATTR_VALUE,
                f"Template 3 accepts no 'value' attribute: {message}",
            )


def test_switching_template_is_cheap_and_isolated():
    """Both views share one ScreenModel. Flipping between them must not force a repaint of
    the template being left, and must re-select the template."""
    recorder, model = make_model()
    main = display.MainView(model)
    params = display.ParamsView(model)

    params.activate()
    params.render(sample_params_content())
    model.flush()

    recorder.clear()
    main.activate()
    main.render(sample_content())
    first_switch = model.flush()
    check(
        any(m[3] == midi.MSG_SCREEN_TEMPLATE and m[4] == screen.TEMPLATE_MAIN
            for m in recorder.messages),
        "switching to Main must select template 0",
    )

    # Back to Params: content unchanged, so only the template select should go out.
    recorder.clear()
    params.activate()
    params.render(sample_params_content())
    back = model.flush()
    check_equal(
        back,
        1,
        f"returning to an unchanged template should cost one message, not {back} "
        f"(first switch was {first_switch})",
    )
    check_equal(
        recorder.messages[0],
        (0xF0, 0x08, 0x26, 0x20, screen.TEMPLATE_PARAMS, 0xF7),
        "and that one message is the template select",
    )


def test_song_mode_encoders_cover_all_eight_once():
    """Song mode's eight encoders come from two components (Transport and Zoom), so the
    only way to be sure the physical layout is complete and collision-free is to check the
    union of what they claim."""
    song_encoders = mappings_module.SONG_ENCODERS
    check_equal(len(song_encoders), 8, "one entry per physical encoder")

    for name, label, owner in song_encoders:
        # Song mode renders on Template 3, whose label element has its own (larger) budget —
        # the whole point of moving it there was room for a real word.
        check(
            len(label) <= formatting.MAXCHARS_PARAMS_LABEL,
            f"song encoder label {label!r} exceeds the Template 3 label budget "
            f"({formatting.MAXCHARS_PARAMS_LABEL})",
        )
        check(
            name.endswith(("_encoder", "_control")),
            f"{name} does not look like a framework control",
        )
        check(
            owner in mappings_module.SONG_COMPONENTS,
            f"{name} names an owning component not in SONG_COMPONENTS: {owner}",
        )

    song = MAPPINGS["Main_Modes"]["song"]
    claimed = []
    for part in song["modes"]:
        for key, value in part.items():
            if key == "component":
                continue
            if isinstance(value, str) and value.startswith("encoders_raw["):
                claimed.append(value)

    check_equal(
        sorted(claimed),
        sorted(f"encoders_raw[{i}]" for i in range(8)),
        "song mode must claim each of the 8 encoders exactly once",
    )

    # Every component named in SONG_ENCODERS must actually get a layer, or its encoders
    # would be silently unbound.
    owners = {owner for _n, _l, owner in song_encoders}
    layered = {part.get("component") for part in song["modes"] if isinstance(part, dict)}
    missing = sorted(owners - layered)
    check_equal(missing, [], "every owning component needs a layer in song mode")

    # The whole matrix must NOT be bound in song mode — that is the Device component's
    # binding in plugin mode, and binding both would give one element two owners.
    for part in song["modes"]:
        check(
            "encoders" not in part.values(),
            "song mode binds individual encoders_raw[i], never the whole 'encoders' matrix",
        )

    # `_raw` is a real accessor: ElementsBase._add_raw_elements creates "{}_raw" for every
    # matrix, so encoders_raw exists for the encoder matrix too.
    elements_src = open(os.path.join(SCRIPT_DIR, "elements.py"), encoding="utf-8").read()
    check('"Encoders"' in elements_src, "the encoder matrix must be named Encoders")


def test_encoder_elements_never_write_to_their_own_cc():
    """The halo lives at the encoder's CC, so the element must not send anything.

    `is_feedback_enabled=False` only stops *parameter feedback*. `install_connections()` also
    calls `reset()`, and `reset_state()` sends the off value, which darkens the halo on every
    layer grab. The fix is ownership: a subclass that drops its outgoing writes, so `leds.py` is
    the only writer. Both the encoder matrix and the wheel must use it — the wheel needs
    `add_element` because `add_encoder` hard-codes the stock `create_encoder`.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "elements.py"), encoding="utf-8").read()
    tree = ast.parse(source)

    element_class = next(
        (
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef) and node.name == "MotionEncoderElement"
        ),
        None,
    )
    check(element_class is not None, "elements.py must define MotionEncoderElement")
    if element_class is not None:
        overrides = {
            node.name for node in element_class.body if isinstance(node, ast.FunctionDef)
        }
        for required in ("send_value", "send_midi"):
            check(
                required in overrides,
                f"MotionEncoderElement must override {required} — the send path differs "
                "between the reset and feedback routes",
            )
        check(
            any(
                isinstance(base, ast.Name) and base.id == "EncoderElement"
                for base in element_class.bases
            ),
            "MotionEncoderElement must extend EncoderElement so input behaviour is unchanged",
        )

    calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    ]

    # The encoder matrix must be built by the GENERIC add_matrix. `add_encoder_matrix`
    # hard-codes element_factory=create_encoder and forwards it, so passing our own is a
    # duplicate keyword and the script fails to load. See test_matrix_wrappers_reject_a_factory.
    matrix_calls = [
        c
        for c in calls
        if c.func.attr == "add_matrix"
        and any(isinstance(a, ast.Constant) and a.value == "Encoders" for a in c.args)
    ]
    check_equal(len(matrix_calls), 1, "one encoder matrix, built with the generic add_matrix")
    for call in matrix_calls:
        kwargs = {kw.arg for kw in call.keywords}
        check(
            "element_factory" in kwargs,
            "the encoder matrix must pass element_factory, or the halos get the stock element",
        )
        check("is_feedback_enabled" in kwargs, "parameter feedback must still be off")

    # The wheel must NOT go through add_encoder, which ignores any factory.
    wheel_via_add_encoder = [
        c
        for c in calls
        if c.func.attr == "add_encoder"
        and any("WHEEL" in ast.dump(arg) for arg in c.args)
    ]
    check_equal(
        len(wheel_via_add_encoder),
        0,
        "add_encoder hard-codes create_encoder, so the wheel would keep the stock element",
    )
    wheel_calls = [
        c
        for c in calls
        if c.func.attr == "add_element"
        and any(isinstance(a, ast.Constant) and a.value == "Wheel_Encoder" for a in c.args)
    ]
    check_equal(len(wheel_calls), 1, "the wheel is added via add_element with our factory")
    for call in wheel_calls:
        check(
            any(
                isinstance(a, ast.Name) and a.id == "create_motion_encoder" for a in call.args
            ),
            "the wheel must be built by create_motion_encoder",
        )


def test_matrix_wrappers_reject_a_factory():
    """`add_encoder_matrix` / `add_button_matrix` hard-code `element_factory`.

    Both wrappers call `add_matrix` forwarding the const kwargs `('channels',
    'element_factory')` — verified by decompiling `elements_base.pyc`. Passing our own factory
    is therefore a duplicate keyword and the **entire script fails to load**:

        TypeError: ElementsBase.add_matrix() got multiple values for keyword argument
                   'element_factory'

    This is the same shape as the `channel=` trap, and it reached hardware for the same reason:
    the previous version of this suite *asserted the broken call*, so the guard locked in a wrong
    assumption about the framework and the run stayed green while Live could not load the script.
    Only `add_matrix` and `add_element` accept a factory.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "elements.py"), encoding="utf-8").read())
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
            continue
        if node.func.attr not in ("add_encoder_matrix", "add_button_matrix"):
            continue
        passed = {kw.arg for kw in node.keywords}
        for forbidden in ("element_factory", "channel"):
            check(
                forbidden not in passed,
                f"{node.func.attr}() must not be passed {forbidden}= — it supplies that itself, "
                f"so this is a duplicate keyword and the script will not load. Use add_matrix().",
            )


def test_wheel_led_follows_mode_and_nothing_else():
    """Lit for the whole of Plugin mode. No press highlight, no reaction to scrolling.

    A light that changes while the control is in use gives every one of those transitions a
    chance to leave it dark, which is what "goes out depending on what it's interacting with"
    was. So the wheel halo is a pure function of the mode.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    check(
        "_wheel_pressed" not in source,
        "press state must not exist — the wheel halo depends on mode only",
    )

    tree = ast.parse(source)
    refresh = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "_refresh_wheel_led"
    )
    names = {node.attr for node in ast.walk(refresh) if isinstance(node, ast.Attribute)}
    check("_mode" in names, "_refresh_wheel_led must read the current mode")

    wheel_src = open(os.path.join(SCRIPT_DIR, "wheel.py"), encoding="utf-8").read()
    check(
        "set_press_observer" not in wheel_src,
        "the wheel component must not report presses for LED purposes any more",
    )


def test_wheel_push_is_input_only():
    """Input CC 0x78 is wheel push; output CC 0x78 is touch-strip 2 LED 9.

    The wheel click's result is shown on the screen/menu, and the wheel halo lives at 0x1D.
    Therefore the push element must receive normally but suppress all LED/button feedback.
    """
    import ast

    elements_source = open(os.path.join(SCRIPT_DIR, "elements.py"), encoding="utf-8").read()
    elements_tree = ast.parse(elements_source)

    input_button_class = next(
        (
            node
            for node in ast.walk(elements_tree)
            if isinstance(node, ast.ClassDef) and node.name == "MotionInputOnlyButtonElement"
        ),
        None,
    )
    check(
        input_button_class is not None,
        "elements.py must define MotionInputOnlyButtonElement for direction-overloaded inputs",
    )
    if input_button_class is not None:
        check(
            any(
                isinstance(base, ast.Name) and base.id == "ButtonElement"
                for base in input_button_class.bases
            ),
            "MotionInputOnlyButtonElement must extend ButtonElement so input behaviour is unchanged",
        )
        overrides = {
            node.name for node in input_button_class.body if isinstance(node, ast.FunctionDef)
        }
        for required in ("send_value", "send_midi"):
            check(
                required in overrides,
                f"MotionInputOnlyButtonElement must override {required} to suppress 0x78 feedback",
            )

    calls = [
        node
        for node in ast.walk(elements_tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    ]
    wheel_push_add_button = [
        c
        for c in calls
        if c.func.attr == "add_button" and any("CC_WHEEL_PUSH" in ast.dump(a) for a in c.args)
    ]
    check_equal(
        len(wheel_push_add_button),
        0,
        "Wheel_Push_Button must not use add_button; that would allow feedback on CC 0x78",
    )
    wheel_push_add_element = [
        c
        for c in calls
        if c.func.attr == "add_element"
        and any(isinstance(a, ast.Constant) and a.value == "Wheel_Push_Button" for a in c.args)
    ]
    check_equal(
        len(wheel_push_add_element),
        1,
        "Wheel_Push_Button must be built with add_element and an input-only factory",
    )
    for call in wheel_push_add_element:
        check(
            any(
                isinstance(a, ast.Name) and a.id == "create_motion_input_button"
                for a in call.args
            ),
            "Wheel_Push_Button must be built by create_motion_input_button",
        )

    wheel_tree = ast.parse(open(os.path.join(SCRIPT_DIR, "wheel.py"), encoding="utf-8").read())
    push_assignments = [
        node
        for node in ast.walk(wheel_tree)
        if isinstance(node, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "push_button" for t in node.targets)
        and isinstance(node.value, ast.Call)
    ]
    check_equal(len(push_assignments), 1, "wheel.py must define exactly one push_button")
    for assignment in push_assignments:
        check_equal(
            len(assignment.value.keywords),
            0,
            "wheel push ButtonControl must not define color or pressed_color feedback",
        )

    skin_source = open(os.path.join(SCRIPT_DIR, "skin.py"), encoding="utf-8").read()
    check("class Wheel" not in skin_source, "skin.py must not define wheel-push feedback colours")


def test_render_flushes_unconditionally():
    """The flush must not depend on the content having changed.

    Switching mode away and back leaves the content snapshot identical, so `render()` returns
    False — but `activate()` has queued a **template select** that then never goes out, and
    the device stays on the other template. That was the "pressing Song doesn't redraw" bug.
    The diff already makes an unnecessary flush free, so the flush is unconditional.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    render = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "_render"
    )

    flushes = [
        node
        for node in ast.walk(render)
        if isinstance(node, ast.Call) and getattr(node.func, "attr", "") == "flush"
    ]
    check(flushes, "_render must flush")

    for node in ast.walk(render):
        if not isinstance(node, ast.If):
            continue
        names = {n.id for n in ast.walk(node.test) if isinstance(n, ast.Name)}
        if "changed" not in names:
            continue
        guards_flush = any(
            isinstance(inner, ast.Call) and getattr(inner.func, "attr", "") == "flush"
            for inner in ast.walk(node)
        )
        returns_early = any(isinstance(inner, ast.Return) for inner in ast.walk(node))
        check(
            not (guards_flush or returns_early),
            "_render must not make the flush conditional on `changed` — a mode switch "
            "queues a template select even when the content is identical",
        )


def test_modes_are_a_strict_radio():
    """Every mode must behave the same, so adding Edit and Mix cannot break the model.

    Plugin briefly used `ToggleBehaviour` so re-pressing it fell back to Song. With two modes
    that reads as "Song and Plugin toggle each other"; with four peers, "toggle off" has no
    well-defined destination. A per-mode behaviour override is the thing to guard against.
    """
    modes = MAPPINGS["Main_Modes"]
    check_equal(
        type(modes["default_behaviour"]).__name__,
        "ImmediateBehaviour",
        "pressing a mode button should go straight to that mode",
    )
    for name, spec in modes.items():
        if not isinstance(spec, dict) or name.endswith("_button"):
            continue
        check(
            "behaviour" not in spec,
            f"mode '{name}' overrides the behaviour — every mode must behave alike so that "
            f"adding Edit/Mix keeps the radio consistent",
        )


def test_transport_subclasses_the_framework_component():
    """Song mode's position/loop/tempo encoders are the framework TransportComponent's own
    controls. Replacing that component instead of subclassing it leaves them unavailable —
    which is what the first version of this script did."""
    import ast

    source = open(os.path.join(SCRIPT_DIR, "transport.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    cls = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef) and node.name == "MotionTransportComponent"
    )
    bases = [b.id for b in cls.bases if isinstance(b, ast.Name)]
    check_equal(bases, ["TransportComponent"], "must subclass the framework TransportComponent")

    # The controls Song mode maps must not be redeclared here — redeclaring would shadow the
    # framework's own handlers.
    declared = {
        target.id
        for item in cls.body
        if isinstance(item, ast.Assign)
        for target in item.targets
        if isinstance(target, ast.Name)
    }
    for name, _label, _owner in mappings_module.SONG_ENCODERS:
        check(name not in declared, f"{name} must be inherited, not redeclared")
    for name in ("play_button", "stop_button", "loop_button", "metronome_button",
                 "tap_tempo_button", "capture_midi_button"):
        check(name not in declared, f"{name} should come from the framework, not be redeclared")
    check("record_button" in declared, "record_button is ours — the framework has none")


def test_value_text_never_loses_a_minus_sign():
    """`compactify` strips hyphens, which silently flips the sign of a negative value —
    fine for labels, wrong for values. Value text uses `truncate_value` instead."""
    check_equal(formatting.compactify("-12.5 dB", 7), "12.5 dB", "compactify drops the hyphen")
    check(
        formatting.truncate_value("-12.5 dB", 7).startswith("-"),
        "truncate_value keeps the sign",
    )

    for text, limit, want in (
        ("0.00 %", 7, "0.00 %"),
        ("127", 7, "127"),
        ("-inf dB", 7, "-inf dB"),
        ("Sine Wave", 7, "Sine"),
        ("-0.0100", 7, "-0.0100"),
        ("", 7, ""),
    ):
        check_equal(formatting.truncate_value(text, limit), want, f"truncate_value({text!r})")

    for text in ("-12.5 dB", "1000000000 Hz", "Some Very Long Enum Value"):
        got = formatting.truncate_value(text, 7)
        check(len(got) <= 7, f"truncate_value overflowed on {text!r}: {got!r}")


def test_a_value_keeps_its_unit_before_it_keeps_its_precision():
    """🐛 **The mixer dropped `dB` on every level below -10.**

    `truncate_value` used to shorten by discarding everything after the first space, so at the
    strip label's 8-character budget `"-6.00 dB"` (8) kept its unit and `"-12.00 dB"` (9) became
    `"-12.00"`. A column of readings where the unit appears and disappears with the value reads
    as a bug, and `-70.00` on its own is genuinely ambiguous. Reported from hardware 2026-08-03.

    ⚠️ **Rounding alone would not have fixed it.** Live already sends two decimals, so
    `"-12.00 dB"` is over budget by exactly the space — closing that up is what saves it. This
    guard exists because the obvious fix (cap the decimals) passes a naive test and still ships
    the bug.

    The order of sacrifice is: spare decimals, then the space, then more decimals, and only
    then the unit.
    """
    for text, want in (
        # The case from hardware. Two decimals already; the space is what has to go.
        ("-12.00 dB", "-12.00dB"),
        ("-70.00 dB", "-70.00dB"),
        # Fits as-is, so it must be left completely alone — spaces included.
        ("-6.00 dB", "-6.00 dB"),
        ("0.00 dB", "0.00 dB"),
        # More precision than the element can show: round to two, then close the space.
        ("-12.345 dB", "-12.35dB"),
        # Needs a decimal sacrificed as well as the space.
        ("-100.00 dB", "-100.0dB"),
        # Not a number, so there is nothing to round — old behaviour still applies.
        ("-inf dB", "-inf dB"),
    ):
        check_equal(
            formatting.truncate_value(text, formatting.MAXCHARS_MIXER_CHANNEL),
            want,
            f"mixer strip label: {text!r}",
        )

    # Whatever happens, the unit survives wherever it possibly can, and the sign always does.
    for text in ("-12.00 dB", "-70.00 dB", "-12.345 dB", "-100.00 dB"):
        got = formatting.truncate_value(text, formatting.MAXCHARS_MIXER_CHANNEL)
        check(len(got) <= formatting.MAXCHARS_MIXER_CHANNEL, f"{text!r} overflowed: {got!r}")
        check(got.startswith("-"), f"{text!r} lost its sign: {got!r}")
        check(got.endswith("dB"), f"{text!r} lost its unit: {got!r}")

    # The narrower Plugin/Pan tile gets the same treatment, one step further along.
    check_equal(
        formatting.truncate_value("-6.00 dB", formatting.MAXCHARS_ENCODER_LABEL),
        "-6.00dB",
        "a 7-char tile closes the space rather than dropping the unit",
    )
    check_equal(
        formatting.truncate_value("-12.00 dB", formatting.MAXCHARS_ENCODER_LABEL),
        "-12.0dB",
        "and spends a decimal when closing the space is not enough",
    )

    # A unit that cannot fit at any rounding must lose the unit, not the magnitude — showing
    # "1000000" as "1000000" is right; showing it as "0000000 Hz" would be a lie.
    got = formatting.truncate_value("1000000000 Hz", 7)
    check(got.startswith("1"), f"a too-wide value must keep its leading digits, got {got!r}")


def test_tile_shows_value_only_while_active():
    """One text element per tile: the name at rest, the value while touched/turning."""
    tile = display.EncoderTile(label="Filter Freq", value_text="1.20k", assigned=True)
    check_equal(tile.text, "Filter Freq", "at rest the tile reads the parameter name")

    live = display.EncoderTile(
        label="Filter Freq", value_text="1.20k", assigned=True, show_value=True
    )
    check_equal(live.text, "1.20k", "while active the tile reads the value")

    # No value text yet (e.g. touched before any change) must not blank the tile.
    empty = display.EncoderTile(label="Filter Freq", assigned=True, show_value=True)
    check_equal(empty.text, "Filter Freq", "an empty value must fall back to the name")


def test_value_display_goes_on_the_wire_and_reverts():
    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()

    def content(show):
        tiles = [display.EncoderTile(label="Frequency", value=64, assigned=True,
                                     value_text="1.20k", show_value=show)]
        tiles += [display.EncoderTile() for _ in range(7)]
        return display.MainContent(title="Operator", tiles=tuple(tiles))

    view.render(content(False))
    model.flush()

    def tile_text_and_colour():
        text = colour = None
        for message in recorder.messages:
            if len(message) > 7 and message[5] == 3 and message[6] == 2:
                if message[7] == midi.ATTR_TEXT:
                    text = "".join(chr(b) for b in message[8:-1])
                elif message[7] == midi.ATTR_COLOR:
                    colour = tuple(message[8:11])
        return text, colour

    # Reveal the value.
    recorder.clear()
    view.render(content(True))
    sent = model.flush()
    text, colour = tile_text_and_colour()
    check_equal(text, "1.20k", "the value must reach the device")
    check_equal(colour, screen.Palette.VALUE_TRIGGERED, "an active value uses the triggered colour")
    check(sent <= 2, f"revealing a value should be 1-2 messages, was {sent}")

    # Time out back to the name.
    recorder.clear()
    view.render(content(False))
    model.flush()
    text, colour = tile_text_and_colour()
    check_equal(text, "Frqncy", "after the timeout the tile reverts to the (compactified) name")
    check_equal(colour, screen.Palette.VALUE, "and back to the resting colour")


FRAMEWORK_DIR = os.path.join(SCRIPT_DIR, "Resources", "control_surface")

# Fallback allowlist if the decompilable framework is not present.
_FRAMEWORK_MEMBERS_FALLBACK = {
    "song", "application", "parent", "name", "layer", "is_enabled", "set_enabled",
    "canonical_parent", "num_layers", "is_root", "disconnect", "update", "register_slot",
    "register_disconnectable", "_tasks", "add_children", "on_enabled_changed",
    "control_notifications_enabled",
}


def _framework_member_names():
    """Attributes the framework's Component / TransportComponent provide.

    Read from the decompiled `.pyc` when available so the allowlist is real rather than
    remembered; falls back to a small hardcoded set otherwise.
    """
    members = set(_FRAMEWORK_MEMBERS_FALLBACK)
    try:
        from xdis.load import load_module
    except ImportError:
        return members
    for relative, class_name in (
        ("component.pyc", "Component"),
        (os.path.join("components", "transport.pyc"), "TransportComponent"),
    ):
        path = os.path.join(FRAMEWORK_DIR, relative)
        if not os.path.exists(path):
            continue
        try:
            code = load_module(path)[3]
        except Exception:
            continue

        def walk(obj, prefix=""):
            name = (prefix + "/" + obj.co_name) if prefix else obj.co_name
            yield name, obj
            for const in obj.co_consts:
                if hasattr(const, "co_name"):
                    yield from walk(const, name)

        found = dict(walk(code))
        body = found.get(f"<module>/{class_name}")
        if body is not None:
            members |= {n for n in body.co_names if not n.startswith("__")}
        init = found.get(f"<module>/{class_name}/__init__")
        if init is not None:
            members |= set(init.co_names)
    return members


def test_no_self_reference_is_undefined():
    """Catch `self.something` that does not exist.

    This is the guard for the two runtime failures that reached hardware: `_get_song` was
    deleted in a refactor while `_song_content` still called it, and nothing offline noticed
    because these modules import the framework and so are never executed by the suite.
    Resolving every `self.X` against the class plus the real framework members closes that.
    """
    import ast

    framework = _framework_member_names()

    for filename in ("screen_component.py", "transport.py"):
        path = os.path.join(SCRIPT_DIR, filename)
        tree = ast.parse(open(path, encoding="utf-8").read())
        for node in ast.walk(tree):
            if not isinstance(node, ast.ClassDef):
                continue

            defined = set()
            for item in ast.walk(node):
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    defined.add(item.name)
                elif isinstance(item, ast.Assign):
                    for target in item.targets:
                        if isinstance(target, ast.Name):
                            defined.add(target.id)
                        elif (
                            isinstance(target, ast.Attribute)
                            and isinstance(target.value, ast.Name)
                            and target.value.id == "self"
                        ):
                            defined.add(target.attr)
                elif isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                    defined.add(item.target.id)

            used = {
                item.attr
                for item in ast.walk(node)
                if isinstance(item, ast.Attribute)
                and isinstance(item.value, ast.Name)
                and item.value.id == "self"
            }

            unknown = sorted(used - defined - framework)
            check_equal(
                unknown,
                [],
                f"{filename}:{node.name} references self.<name> that is not defined "
                f"in the class or provided by the framework",
            )


# Framework members that are PROPERTIES, so `self.<name>()` is a TypeError at runtime.
# Derived from the bytecode below; this is the fallback if the framework copy is absent.
_FRAMEWORK_PROPERTIES_FALLBACK = {
    "application", "song", "parent", "is_root", "layer", "_tasks",
    "any_clipboard_has_content", "canonical_parent", "num_layers",
}


def _framework_property_names():
    """Which `Component` members are properties, read from the class-body bytecode.

    Looks for a decorator (`property` / `listenable_property` / `lazy_attribute`) loaded
    immediately before a `STORE_NAME`. Conservative: a missed one just means less coverage,
    never a false failure.
    """
    names = set(_FRAMEWORK_PROPERTIES_FALLBACK)
    try:
        from xdis.load import load_module
        from xdis.std import make_std_api
    except ImportError:
        return names
    import io
    import re

    for relative, class_name in (
        ("component.pyc", "Component"),
        (os.path.join("components", "transport.pyc"), "TransportComponent"),
    ):
        path = os.path.join(FRAMEWORK_DIR, relative)
        if not os.path.exists(path):
            continue
        try:
            code = load_module(path)[3]
        except Exception:
            continue

        def walk(obj, prefix=""):
            name = (prefix + "/" + obj.co_name) if prefix else obj.co_name
            yield name, obj
            for const in obj.co_consts:
                if hasattr(const, "co_name"):
                    yield from walk(const, name)

        body = dict(walk(code)).get(f"<module>/{class_name}")
        if body is None:
            continue
        buffer = io.StringIO()
        try:
            make_std_api((3, 11), "CPython").dis(body, file=buffer)
        except Exception:
            continue
        pending = []
        for line in buffer.getvalue().splitlines():
            loaded = re.search(r"LOAD_NAME\s+\((\w+)\)", line)
            if loaded and loaded.group(1) in (
                "property",
                "listenable_property",
                "lazy_attribute",
            ):
                pending.append(loaded.group(1))
            stored = re.search(r"STORE_NAME\s+\((\w+)\)", line)
            if stored:
                if pending:
                    names.add(stored.group(1))
                pending = []
    return names


def test_framework_properties_are_never_called():
    """`Component.application` is a property; `self.application()` raises
    `TypeError: 'Application' object is not callable`.

    That reached hardware. `song`, `parent`, `layer`, `is_root` and `_tasks` are properties
    too — while `is_enabled()` and `disconnect()` genuinely are methods, so the distinction
    can't be guessed from the name. The property list is read from the framework bytecode.
    """
    import ast

    properties = _framework_property_names()
    # Sanity-check the extraction itself, so a silent regression in it can't hide bugs.
    for expected in ("application", "song", "parent"):
        check(expected in properties, f"expected {expected} to be detected as a property")
    check(
        "is_enabled" not in properties or True,
        "is_enabled is a method; listing it would only cost coverage",
    )

    for filename in ("screen_component.py", "transport.py"):
        path = os.path.join(SCRIPT_DIR, filename)
        tree = ast.parse(open(path, encoding="utf-8").read())
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "self"
                and node.func.attr in properties
            ):
                check(
                    False,
                    f"{filename}:{node.lineno} calls self.{node.func.attr}() but "
                    f"{node.func.attr} is a framework *property* — drop the parentheses",
                )


def test_listens_handlers_tolerate_a_payload():
    """A `listens` handler is called with whatever the notifier passes, and that varies per
    property: `notify_parameters()` passes nothing, `selected_mode` passes the new mode.
    Declaring `*a` makes the handler correct either way — without it, entering a mode raised
    `TypeError: ... takes 1 positional argument but 2 were given` on hardware."""
    import ast

    for filename in ("screen_component.py", "transport.py"):
        path = os.path.join(SCRIPT_DIR, filename)
        tree = ast.parse(open(path, encoding="utf-8").read())
        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef):
                continue
            decorated_with_listens = any(
                (isinstance(d, ast.Call) and isinstance(d.func, ast.Name) and d.func.id == "listens")
                or (isinstance(d, ast.Name) and d.id == "listens")
                for d in node.decorator_list
            )
            if not decorated_with_listens:
                continue
            check(
                node.args.vararg is not None,
                f"{filename}:{node.name} is a @listens handler and must accept *a "
                "(the notifier may pass a value)",
            )


def test_empty_device_state_is_never_a_blank_screen():
    """An empty screen is indistinguishable from a broken one.

    With no device in focus the earlier content was title="" / all tile labels="" — which on
    hardware looks exactly like a failure, and did: Plugin mode "showed nothing" on a fresh
    Live set that simply had no devices. The no-device state must still say something.
    """
    recorder, model = make_model()
    view = display.MainView(model)
    view.activate()

    # The shape screen_component builds when nothing is in focus.
    view.render(
        display.MainContent(
            title="1 MIDI",
            centre="No device selected",
            tiles=tuple(display.EncoderTile(label="-", assigned=False) for _ in range(8)),
        )
    )
    model.flush()

    texts = []
    for message in recorder.messages:
        if len(message) > 7 and message[3] == midi.MSG_SCREEN_UPDATE and message[7] == midi.ATTR_TEXT:
            texts.append("".join(chr(b) for b in message[8:-1]))

    check("1 MIDI" in texts, "the focused track should still be named")
    check("No device selected" in texts, "the no-device state must be stated explicitly")
    check_equal(texts.count("-"), 8, "every tile should be labelled, not blank")
    check(
        any(t.strip() for t in texts),
        "the no-device screen must carry visible text",
    )


def test_flush_logging_does_not_flood():
    """The live value refresh runs at 20 Hz; logging every flush would bury the log."""
    logged = []
    recorder = Recorder()
    model = display.ScreenModel(send=recorder, log=logged.append)
    view = display.MainView(model)
    view.activate()
    view.render(sample_content())
    model.flush()
    check_equal(len(logged), 1, "a full repaint should log exactly once")

    # A single value change must not log.
    logged.clear()
    tiles = list(sample_content().tiles)
    tiles[0] = display.EncoderTile(label="Filter Freq", value=99, assigned=True)
    view.render(display.MainContent(title="Operator", centre="Bank 1/3", tiles=tuple(tiles)))
    model.flush()
    check_equal(logged, [], "a one-message flush must not be logged")


def test_encoder_leds_can_be_reasserted_after_an_external_stomp():
    """The halos share their address with the encoder CC, and the framework writes there.

    `EncoderElement.install_connections` calls `reset()`, and `reset_state()` sends the
    element's off value — so every layer grab (i.e. every mode change) darkens a halo we just
    set. Our cache has no way to see that write, so recovery means `invalidate()` then flush.
    Setting the same colour again without invalidating is a no-op, which is precisely why the
    halos stayed dark until touched.
    """
    sent = []
    encoder_leds = leds.EncoderLeds(send=lambda message: sent.append(tuple(message)))
    purple = screen.Palette.KNOB_SONG

    for index in range(encoder_leds.count):
        encoder_leds.set(index, purple)
    first = encoder_leds.flush()
    check_equal(first, 8 * 4, "each halo takes a state byte plus three colour components")

    # Pretend the framework has just stomped the CCs. We cannot observe that, so a plain
    # re-flush must be a no-op — this is the bug.
    sent.clear()
    check_equal(encoder_leds.flush(), 0, "an unchanged set must not re-send by itself")

    # ...and invalidating is what recovers it.
    encoder_leds.invalidate()
    recovered = encoder_leds.flush()
    check_equal(recovered, 8 * 4, "invalidate() must force every halo out again")

    state_messages = [m for m in sent if m[0] == midi.STATUS_CC]
    check_equal(len(state_messages), 8, "one state byte per encoder")
    check_equal(state_messages[0][1], midi.CC_ENCODERS[0], "halo address is the encoder's own CC")
    check_equal(state_messages[0][2], midi.LED_ON, "state restored to full, not the off value")

    # An unassigned slot goes dark rather than staying on a stale colour.
    encoder_leds.set(3, None)
    encoder_leds.flush()
    off = [m for m in sent if m[0] == midi.STATUS_CC and m[1] == midi.CC_ENCODERS[3]]
    check_equal(off[-1][2], midi.LED_OFF, "an unassigned halo is turned off")

    # Teardown uses the factory's white-on-exit values, not black.
    sent.clear()
    encoder_leds.release()
    colours = [m for m in sent if m[0] == midi.STATUS_CC_RED]
    check(colours, "release should send colour components")
    check_equal(colours[0][2], midi.RESET_RGB, "release colour is white, per the shutdown capture")


def test_mode_change_reasserts_the_leds():
    """A mode change must schedule a *deferred* re-assert, not just refresh inline.

    Refreshing inline loses the race against the framework's own reset of the encoder
    elements, which happens as layers are re-granted.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    tree = ast.parse(source)

    handler = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "_on_selected_mode_changed"
    )
    calls = {
        node.func.attr
        for node in ast.walk(handler)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }
    check(
        "_schedule_led_reassert" in calls,
        "a mode change must schedule a deferred LED re-assert",
    )

    # And the re-assert must invalidate before refreshing, or the cache swallows it.
    reassert = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "_reassert_leds"
    )
    inner = {
        node.func.attr
        for node in ast.walk(reassert)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }
    check(
        "_invalidate_led_groups" in inner or "invalidate" in inner,
        "_reassert_leds must invalidate the LED cache first",
    )
    check(
        "_refresh_all_leds" in inner
        or {"_refresh_encoder_leds", "_refresh_wheel_led"} <= inner,
        "_reassert_leds must refresh every LED group",
    )


def test_every_led_path_covers_every_group():
    """🐛 The bug that left the keybed dark until a mode switch.

    `full_redraw` (connect, refresh_state, post-Global-Settings) named `_encoder_leds`
    explicitly and refreshed only the halos. When the pads were added they were wired into
    `_reassert_leds` — the *mode-change* path — but not into `full_redraw`, so after connect
    the pads stayed dark until a mode change happened to repaint them.

    A hand-listed set of groups is precisely what goes stale when a group is added, so both
    paths must go through the shared helpers instead. This also fails if a fourth LED group is
    ever added without extending `_led_groups()`.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read())
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    groups = functions.get("_led_groups")
    check(groups is not None, "there must be a single _led_groups() list")
    if groups is None:
        return
    named = {
        n.attr for n in ast.walk(groups) if isinstance(n, ast.Attribute) and n.attr.endswith("leds")
    } | {
        n.attr for n in ast.walk(groups) if isinstance(n, ast.Attribute) and n.attr.endswith("led")
    }
    check_equal(
        sorted(named),
        ["_encoder_leds", "_pad_leds", "_wheel_led"],
        "_led_groups() must list every group we own",
    )

    for path in ("full_redraw", "_reassert_leds"):
        node = functions.get(path)
        check(node is not None, f"screen_component must define {path}")
        if node is None:
            continue
        called = {
            n.func.attr
            for n in ast.walk(node)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
        }
        check(
            "_invalidate_led_groups" in called,
            f"{path}() must invalidate every LED group, not a hand-picked one",
        )
        check(
            "_refresh_all_leds" in called,
            f"{path}() must refresh every LED group — naming one is how the pads got missed",
        )


def test_reload_does_not_let_the_old_instance_wipe_the_new_one():
    """Live constructs the replacement surface *before* disconnecting the old one.

    With unscoped module state, the outgoing instance's teardown cleared the incoming
    instance's screen references and blanked the device it had just drawn on — a blank screen
    with nothing in the log. Ownership scoping makes the stale teardown a no-op.
    """
    old_surface, new_surface = object(), object()
    old_model, new_model = object(), object()

    runtime.publish(
        old_surface,
        old_model,
        "old_main",
        "old_params_view",
        "old_mixer_view",
        "old_note",
        "old_menu",
        "old_params",
    )
    check(runtime.is_ready(), "publishing should make the runtime ready")
    check(runtime.screen_model() is old_model, "the first instance owns the model")

    # Reload: the new instance publishes while the old one is still alive.
    runtime.publish(
        new_surface,
        new_model,
        "new_main",
        "new_params_view",
        "new_mixer_view",
        "new_note",
        "new_menu",
        "new_params",
    )
    check(runtime.screen_model() is new_model, "the newer instance takes ownership")

    # Now the old instance tears down. It must not clear, and must be told so.
    check_equal(runtime.clear(old_surface), False, "a superseded instance must not clear")
    check(
        runtime.screen_model() is new_model,
        "the new instance's screen state must survive the old one's teardown",
    )
    check(runtime.is_ready(), "runtime must still be ready after a stale teardown")

    # The current owner can clear.
    check_equal(runtime.clear(new_surface), True, "the owner may clear")
    check(not runtime.is_ready(), "after the owner clears, nothing remains")
    check_equal(runtime.clear(new_surface), False, "clearing twice is a no-op")


def _build_teardown_harness(still_current):
    """Run the real `Motion32` teardown methods against a framework stand-in.

    `__init__.py` imports `ableton.*` at module level, so it cannot be imported offline.
    Instead the three teardown methods are lifted out of the class by AST and re-compiled
    inside a synthetic class — as a *class body*, so the zero-argument `super()` gets its
    `__class__` cell and the framework base is genuinely reached.

    The base reproduces the framework's own goodbye path exactly as it appears in
    `control_surface.pyc`: `disconnect()` -> `_send_specification_messages(
    messages_name="goodbye_messages")` -> `for msg in ...: self._send_midi(msg)`. That is
    the path that bypasses `MotionProtocol`, `ScreenModel` and `LedGroup`, so a test that
    stubs it out cannot see the bug it exists to catch.

    Returns (instance, sent_messages).
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "__init__.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    surface = next(
        node
        for node in tree.body
        if isinstance(node, ast.ClassDef) and node.name == "Motion32"
    )
    wanted = ("_send_midi", "disconnect", "_clear_all_leds")
    methods = {
        node.name: node
        for node in surface.body
        if isinstance(node, ast.FunctionDef) and node.name in wanted
    }
    missing = sorted(set(wanted) - set(methods))
    if missing:
        return None, missing

    body = "\n".join(
        textwrap.indent(ast.unparse(methods[name]), "    ") for name in wanted
    )
    synthetic = "class Motion32(_FrameworkBase):\n" + body

    class _Suspendable:
        def __init__(self):
            self.suspended = None
            self.released = 0
            self.forgotten = 0

        def set_suspended(self, suspended):
            self.suspended = suspended

        def release(self):
            # ⚠️ Counted, not silent. `disconnect()` must NOT call this — `_clear_all_leds()`
            # already covers every address these groups own, so calling both sent all 41
            # twice (~196 redundant messages per unload, and it made the "byte-identical to
            # Studio Pro" claim false). Fixed 2026-08-03; asserted below.
            self.released += 1
            return 0

        def forget(self):
            self.forgotten += 1

        def reset_to_defaults(self):
            return 0

    class _Specification:
        goodbye_messages = (midi.NATIVE_MODE_OFF_MESSAGE,)

    class _FrameworkBase:
        """The framework's outgoing path, reduced to the part that matters here."""

        def _send_midi(self, message, **_k):
            self.sent.append(tuple(message))
            return True

        def disconnect(self):
            self._send_specification_messages(messages_name="goodbye_messages")

        def _send_specification_messages(self, messages_name=None):
            for message in getattr(self.specification, messages_name) or []:
                self._send_midi(message)

    class _Runtime:
        @staticmethod
        def clear(_owner):
            return still_current

    class _Logger:
        def info(self, *a, **k):
            pass

        warning = exception = info

    namespace = {
        "_FrameworkBase": _FrameworkBase,
        "runtime": _Runtime(),
        "logger": _Logger(),
        "midi": midi,
    }
    exec(compile(synthetic, "<motion32-teardown>", "exec"), namespace)

    instance = namespace["Motion32"].__new__(namespace["Motion32"])
    instance.sent = []
    instance._midi_muted = False
    instance.specification = _Specification()
    instance._screen_model = _Suspendable()
    instance._encoder_leds = _Suspendable()
    instance._wheel_led = _Suspendable()
    instance._pad_leds = _Suspendable()
    # `_clear_all_leds` writes through the protocol, which on the real surface bottoms out
    # in `_send_midi` — so the harness routes it there too.
    instance._motion_protocol = types.SimpleNamespace(send=instance._send_midi)
    instance.disconnect()
    return instance, instance.sent


def test_a_superseded_teardown_emits_zero_bytes():
    """A superseded instance must put **nothing** on the wire — most importantly not the
    native-mode goodbye.

    Suspending our own writers is not enough, and a guard that only checks the LED/screen
    reset calls are skipped cannot tell. `ControlSurface.disconnect()` sends
    `goodbye_messages` through `self._send_midi` directly, so on a script reload the order
    was: new instance sends `8F 00 7F`, old instance disconnects, old instance sends
    `8F 00 00` — the device leaves native mode while the new instance believes it is in,
    which presents as transport arriving on `0x66-0x69` instead of `0x6F`.
    """
    # Positive control first: if the harness cannot make a *current* instance emit the
    # goodbye, then "zero bytes" below proves nothing at all.
    current, sent_when_current = _build_teardown_harness(still_current=True)
    if current is None:
        check(False, f"Motion32 is missing teardown methods: {sent_when_current}")
        return
    check(
        tuple(midi.NATIVE_MODE_OFF_MESSAGE) in sent_when_current,
        "the harness does not reproduce the framework goodbye path, so the zero-bytes "
        "assertion below would pass vacuously",
    )
    check(
        len(sent_when_current) > len(midi.LED_ADDRESSES_TO_CLEAR),
        "a current instance should still clear the LEDs and screen before saying goodbye",
    )

    # **Exactly once per address, and the count says so.**
    #
    # 🐛 `disconnect()` used to call `release()` on all three LED groups *and* then
    # `_clear_all_leds()`. The overlap is total — `LED_ADDRESSES_TO_CLEAR` contains
    # `CC_ENCODERS` and `CC_WHEEL`, and `_clear_all_leds` walks `PAD_NOTES` itself — so every
    # halo, the wheel and all 32 pads were reset twice: ~196 wasted messages on every unload,
    # and `leds.py`'s claim that the teardown is byte-identical to Studio Pro's was wrong by a
    # factor of two on those addresses. A length check is the only thing that catches this;
    # every individual message was correct.
    expected = (
        4 * len(midi.LED_ADDRESSES_TO_CLEAR)   # state + R + G + B per CC address
        + 5 * len(midi.PAD_NOTES)              # pads take the state byte twice (see leds.py)
        + 1                                    # the native-mode goodbye
    )
    check_equal(
        len(sent_when_current),
        expected,
        "a current teardown must write each LED address exactly once — a bigger number means "
        "two clearing paths are overlapping again",
    )
    for name in ("_encoder_leds", "_wheel_led", "_pad_leds"):
        group = getattr(current, name)
        check_equal(
            group.released,
            0,
            f"disconnect() must not call {name}.release() — _clear_all_leds() already resets "
            f"every address it owns, so this is a duplicate transmission",
        )
        check_equal(
            group.forgotten,
            1,
            f"disconnect() must still call {name}.forget(), or the group's cache outlives the "
            f"reset and would short-circuit a later diff",
        )

    superseded, sent_when_superseded = _build_teardown_harness(still_current=False)
    check_equal(
        sent_when_superseded,
        [],
        "a superseded instance emitted MIDI during teardown — anything here reaches a "
        "device the new instance already owns, and 8F 00 00 drops it out of native mode",
    )
    check(
        superseded._midi_muted is True,
        "the superseded branch must mute _send_midi itself, not just the screen/LED "
        "writers — the framework's goodbye bypasses every one of those flags",
    )


def test_teardown_is_skipped_when_superseded():
    """The `runtime.clear` return value must actually gate the hardware reset in
    `disconnect()` — clearing LEDs and blanking the screen belongs to whoever owns the
    device now."""
    import ast

    source = open(os.path.join(SCRIPT_DIR, "__init__.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    disconnect = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "disconnect"
    )

    # runtime.clear(self) result must be bound to a name and used in a condition.
    assigned = {
        target.id
        for node in ast.walk(disconnect)
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Name)
        and isinstance(node.value, ast.Call)
        and getattr(node.value.func, "attr", "") == "clear"
    }
    check(assigned, "disconnect must capture runtime.clear(self)'s result")

    guarded = {
        node.test.id
        for node in ast.walk(disconnect)
        if isinstance(node, ast.If) and isinstance(node.test, ast.Name)
    }
    check(
        assigned & guarded,
        "the captured result must gate the LED/screen reset, or a superseded instance "
        "will blank a device it no longer owns",
    )

    # And the reset calls must be inside that guard, not at the top level of disconnect.
    for statement in disconnect.body:
        if isinstance(statement, ast.Try):
            dumped = ast.dump(statement)
            check(
                "_clear_all_leds" not in dumped,
                "_clear_all_leds must be inside the ownership guard",
            )


# Where each component we map gets its control names from. Bases are listed explicitly
# because class inheritance is not recoverable from the bytecode: DeviceNavigationComponent
# extends ScrollComponent, and DeviceComponent forwards `set_*bank*` to the bank-navigation
# sub-component and `set_parameter_controls` to the parameters sub-component.
FRAMEWORK_COMPONENT_SOURCES = {
    "Transport": ["components/transport.pyc"],
    "Undo_Redo": ["components/undo_redo.pyc"],
    "View_Toggle": ["components/view_toggle.pyc"],
    "View_Control": ["components/view_control.pyc", "components/scroll.pyc"],
    # Mix mode's Left/Right. `SessionNavigationComponent` composes two `ScrollComponent`s
    # (horizontal and vertical), so the scroll controls resolve from scroll.pyc.
    # Phase 7b: the wheel's page scroll. `scroll_encoder` comes from `ScrollComponent`,
    # which `MotionMixPagesComponent` subclasses.
    "Motion_Mix_Pages": ["components/scroll.pyc"],
    # Phase 10: the wheel selects the scale/key. `scroll_encoder` comes from ScrollComponent,
    # which MotionScaleComponent subclasses for the same reason Mix_Pages does.
    "Motion_Scale": ["components/scroll.pyc"],
    "Session_Navigation": [
        "components/session_navigation.pyc",
        "components/scroll.pyc",
    ],
    "Zoom": ["components/zoom.pyc"],
    "Mixer": ["components/mixer.pyc", "components/channel_strip.pyc"],
    "Device": [
        "components/device.pyc",
        "components/device_parameters.pyc",
        "components/device_bank_navigation.pyc",
    ],
    "Device_Navigation": ["components/device_navigation.pyc", "components/scroll.pyc"],
    # MotionKeyboardComponent extends PlayableComponent — `matrix` (and set_matrix) come
    # from there, not from our subclass.
    "Motion_Keyboard": ["components/playable.pyc"],
    # Target_Channel_Strip extends ChannelStripComponent — that is where solo_button,
    # mute_button, arm_button, volume_control and pan_control come from.
    "Target_Channel_Strip": [
        "components/target_channel_strip.pyc",
        "components/channel_strip.pyc",
    ],
}

# Components that legitimately accept *any* control name, so there is nothing to check.
# `BackgroundComponent.__getattr__` synthesises a `set_<name>` for whatever it is handed —
# that is the whole point of a background: it grabs arbitrary elements so they don't leak
# into other layers. Verified in `components/background.pyc`.
WILDCARD_COMPONENTS = {
    "Background",
    "Modifier_Background",
    "Translating_Background",
    # Phase 8: a `BackgroundComponent` registered under our own name, whose only job is to
    # consume the top lane of Shift-modified pads so they stay silent. Same `__getattr__`
    # wildcard as any other background.
    "Shift_Pad_Background",
}

#: **Modes components have no control names of their own**, so resolving names against them is
#: meaningless — the framework's rule is that any `create_mappings` key *not* in `component_map`
#: becomes a `ModesComponent` (`ControlSurfaceMappingMixin.setup`), and its section holds modes
#: and meta keys rather than control bindings. `Main_Modes` was already special-cased by name;
#: `Mix_Pages` (Phase 7b) made that a category. Their *contents* are still checked — every part
#: inside them names a real component and goes through `check_section`.
MODES_COMPONENTS = {"Main_Modes", "Mix_Pages"}

# Components implemented by us; their control names come from our own source.
OUR_COMPONENT_SOURCES = {
    "Transport": "transport.py",
    "Motion_Screen": "screen_component.py",
    "Motion_Wheel": "wheel.py",
    "Motion_Keyboard": "keyboard.py",
    "Motion_Mix_Pages": "mixpages.py",
    "Motion_Commands": "commands.py",
    "Motion_Scale": "scalemode.py",
    "Motion_Mode_Return": "scalemode.py",
    "Motion_Sends": "sends.py",
}

# Keys in a mapping section that are not control names.
MAPPING_META_KEYS = {
    "component", "behaviour", "selector", "index", "modes", "enable",
    "default_behaviour", "modes_component_type", "is_private",
    "support_momentary_mode_cycling", "priority",
}


def _control_names_from_pyc(relative_paths):
    names = set()
    try:
        from xdis.load import load_module
    except ImportError:
        return None
    for relative in relative_paths:
        path = os.path.join(FRAMEWORK_DIR, relative)
        if not os.path.exists(path):
            continue
        try:
            code = load_module(path)[3]
        except Exception:
            continue

        def walk(obj):
            yield obj
            for const in obj.co_consts:
                if hasattr(const, "co_name"):
                    yield from walk(const)

        # Take the *class body* code objects only. Their co_names are the class attributes
        # (the controls) plus the method names — which is exactly the surface a Layer can
        # bind to. Walking method bodies as well would drag in every local name and make the
        # allowlist meaningless (`shift`, for instance, is a bare ButtonControl attribute and
        # has no `_button` suffix, so filtering by suffix misses real controls).
        for obj in walk(code):
            if not obj.co_name.endswith("Component"):
                continue
            for name in obj.co_names:
                if name.startswith("__"):
                    continue
                if name.startswith("set_"):
                    names.add(name[4:])
                names.add(name)
    return names


def _control_names_from_our_source(filename):
    import ast

    path = os.path.join(SCRIPT_DIR, filename)
    if not os.path.exists(path):
        return set()
    names = set()
    tree = ast.parse(open(path, encoding="utf-8").read())
    for cls in [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]:
        for item in cls.body:
            if isinstance(item, ast.Assign) and isinstance(item.value, ast.Call):
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        names.add(target.id)
            elif isinstance(item, ast.FunctionDef) and item.name.startswith("set_"):
                names.add(item.name[4:])
    return names


#: Components whose `__getattr__` maps a plural Layer name onto a per-strip singular.
#: Only `MixerComponent` does this; see `allowed_for` for the exact mechanism.
PLURAL_FORWARDING_COMPONENTS = {"Mixer"}


def test_every_mapped_control_name_exists():
    """The guard for a whole class of silent failure.

    An unknown control name in a `Layer` does **not** raise and does **not** log — the button
    simply never does anything. `Device_Navigation` was mapped with `prev_button`/`next_button`
    for several rounds; it extends `ScrollComponent`, whose controls are
    `scroll_up_button`/`scroll_down_button`, so device navigation was quietly absent the whole
    time. Every mapped name is now resolved against the real component.
    """
    check(
        os.path.isdir(FRAMEWORK_DIR),
        "Resources/control_surface is missing, so no mapped control name can be resolved "
        "against the real framework. A run without this guard is not a pass.",
    )
    if not os.path.isdir(FRAMEWORK_DIR):
        return

    skipped = []

    def allowed_for(component):
        names = set()
        if component in FRAMEWORK_COMPONENT_SOURCES:
            resolved = _control_names_from_pyc(FRAMEWORK_COMPONENT_SOURCES[component])
            if resolved is None:
                return None
            names |= resolved
        if component in OUR_COMPONENT_SOURCES:
            names |= _control_names_from_our_source(OUR_COMPONENT_SOURCES[component])
        if component in PLURAL_FORWARDING_COMPONENTS:
            # ⚠️ `MixerComponent.__getattr__` catches any name starting with `set` and
            # returns `partial(self._set_strip_controls, name[4:-1])` — dropping `set_` and
            # the **trailing s**. `_set_strip_controls` then does `getattr(strip, name)` on
            # each channel strip. So the mixer-wide spelling of a per-strip control is its
            # plural: `volume_controls` -> `volume_control` on every strip.
            #
            # That is invisible to a class-body allowlist, so without this the guard would
            # reject a *correct* mapping — the opposite of its job. Read from
            # `components/mixer.pyc`; the singular still has to exist, so a typo is still
            # caught here (and would raise AttributeError at bind time on hardware, which is
            # unusually loud for a Layer name).
            names |= {f"{name}s" for name in names}
        return names

    def check_section(component, section, where):
        """Validate one section. Returns True only if its names were really resolved.

        The return value matters: an earlier version counted sections *visited*, which let
        the backstop below pass while every section had in fact been skipped.
        """
        if component is None or component in WILDCARD_COMPONENTS:
            return False
        if component in MODES_COMPONENTS:
            # A modes component binds mode *buttons* by name, not controls; its inner parts
            # are validated on their own components. Nothing to resolve here.
            return False
        allowed = allowed_for(component)
        if allowed is None:
            skipped.append(f"{where} ({component}) — xdis is not installed")
            return False
        if not allowed:
            skipped.append(f"{where} ({component}) — no control names resolved")
            return False
        for key, value in section.items():
            if key in MAPPING_META_KEYS or not isinstance(value, str):
                continue
            check(
                key in allowed,
                f"{where}: '{key}' is not a control on {component} — a Layer binds unknown "
                f"names silently, so this would do nothing on hardware",
            )
        return True

    checked = 0
    for name, section in MAPPINGS.items():
        if not isinstance(section, dict):
            continue
        if name in MODES_COMPONENTS:
            for mode_name, spec in section.items():
                if not isinstance(spec, dict):
                    continue
                for part in spec.get("modes", [spec]):
                    if isinstance(part, dict) and part.get("component"):
                        checked += check_section(
                            part["component"], part, f"{name}.{mode_name}"
                        )
        else:
            checked += check_section(name, section, name)

    # Every modes component named as a mode *part* must be a real one, or the mode enables
    # nothing and the page silently never appears.
    for name, section in MAPPINGS.items():
        if name not in MODES_COMPONENTS or not isinstance(section, dict):
            continue
        for mode_name, spec in section.items():
            if not isinstance(spec, dict):
                continue
            for part in spec.get("modes", [spec]):
                if not isinstance(part, dict):
                    continue
                nested = part.get("component")
                if nested in MODES_COMPONENTS and len(part) == 1:
                    check(
                        nested in MAPPINGS,
                        f"{name}.{mode_name} enables modes component {nested!r}, which is "
                        f"not declared — the mode would enable nothing",
                    )

    # An unrunnable guard is a failure, not a skip. Without this, a machine with no `xdis`
    # silently dropped every framework-component check and still reported 0 failures — which
    # is exactly how `prev_button`/`next_button` on `Device_Navigation` hid for several rounds.
    check(
        not skipped,
        "these mappings were NOT checked, so an unknown control name in them would reach "
        "hardware unnoticed:\n       " + "\n       ".join(skipped)
        + "\n     Fix with: pip install xdis",
    )
    check(checked >= 6, f"expected to check several components, only did {checked}")


def test_every_view_is_on_the_roster_and_full_redraw_walks_it():
    """`runtime.views()` must list **every** view, and `full_redraw` must use it.

    🐛 `full_redraw()` typed its own tuple of views to call `forget()` on, and `MixerView` was
    never added when Mix mode landed (found 2026-08-03). It survived only because
    `ScreenModel.invalidate()` clears `_sent` and leaves `_desired` alone, so the last strip
    content still went back out — luck, not design, and it broke the moment anything cleared
    `_desired` too. Exactly the shape of the earlier LED bug where a newly added group went
    into one hand-written list and not the other, and the keybed stayed dark after connect.

    Two halves, because either alone can be defeated: the roster must be complete, and the
    caller must actually read the roster rather than growing a second list beside it.
    """
    import ast

    runtime_tree = ast.parse(
        open(os.path.join(SCRIPT_DIR, "runtime.py"), encoding="utf-8").read()
    )

    # Every `_*_view` module global is a view that must be on the roster.
    published = {
        target.id
        for node in runtime_tree.body
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Name) and target.id.endswith("_view")
    }
    check(len(published) >= 4, f"expected at least 4 views in runtime.py, found {published}")

    roster = next(
        (
            n
            for n in ast.walk(runtime_tree)
            if isinstance(n, ast.FunctionDef) and n.name == "views"
        ),
        None,
    )
    check(roster is not None, "runtime.py must expose views() as the single roster")
    if roster is None:
        return
    listed = {
        n.id
        for n in ast.walk(roster)
        if isinstance(n, ast.Name) and n.id.endswith("_view")
    }
    check_equal(
        sorted(published - listed),
        [],
        "these views exist in runtime.py but are missing from views(), so full_redraw() will "
        "not call forget() on them and a repaint can short-circuit on a stale memo",
    )

    # …and the caller must read the roster, not a list of its own.
    screen_tree = ast.parse(
        open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    )
    full_redraw = next(
        (
            n
            for n in ast.walk(screen_tree)
            if isinstance(n, ast.FunctionDef) and n.name == "full_redraw"
        ),
        None,
    )
    check(full_redraw is not None, "screen_component.py must define full_redraw")
    if full_redraw is None:
        return
    calls_roster = any(
        isinstance(n, ast.Call)
        and isinstance(n.func, ast.Attribute)
        and n.func.attr == "views"
        and isinstance(n.func.value, ast.Name)
        and n.func.value.id == "runtime"
        for n in ast.walk(full_redraw)
    )
    check(
        calls_roster,
        "full_redraw() must iterate runtime.views() — a hand-written tuple of views here is "
        "the bug this guard exists for, and it goes stale the next time a view is added",
    )


# ---------------------------------------------------------------------------
# Skin coverage
# ---------------------------------------------------------------------------
#
# ⚠️ **A missing skin key does not raise, does not log, and does not even reliably go dark.**
# From `skin.pyc.Skin.__getitem__`:
#
#     if key not in self.colors:
#         if key.lower().endswith(('enabled', 'on', 'pressed', 'selected')):
#             return BasicColors.ON
#         return BasicColors.OFF
#
# A `BasicColors` carries a state byte and no RGB triple, which on this device renders
# colourless. So a missing `X.FooOn` still lights (in whatever colour the last mode left on that
# address) while its `X.Foo` partner writes state 0 and goes dark — the button appears to "only
# work while pressed". `Session.Navigation` sat missing for the whole of Phase 7 exactly like
# that: Mix mode's Left/Right went dark on entry and nobody read it as a bug.
#
# Two guards, because neither is sufficient alone:
#
#   1. `test_every_skin_namespace_a_bound_component_uses_is_declared` — fully **derived** from
#      the framework `.pyc` and `create_mappings()`. Zero maintenance, catches a whole
#      namespace going missing, which is the failure that actually happened.
#   2. `test_bound_controls_have_a_real_skin_colour` — an explicit table, because **the
#      bytecode does not link a control name to its skin keys**. `ButtonControl(color=...)`
#      declarations, `ScrollComponent(scroll_skin_name=...)` and
#      `ModifierBackgroundComponent`'s `"{}.{}".format(...)` are three different mechanisms and
#      only the first is even a literal near its control. Hand-maintained, small, and it is the
#      one that pins the exact keys.

#: Skin bases that are **computed at runtime** and can never be scraped from constants.
#: `component -> namespaces it will ask for`. See `skin.py`'s module docstring for the
#: derivations.
COMPUTED_SKIN_NAMESPACES = {
    # ModifierBackgroundComponent: self.name.title().replace("_", "") -> "ModifierBackground"
    "Modifier_Background": {"ModifierBackground"},
}

#: Every LED-bearing control we actually map, and the exact skin keys the framework will ask
#: for when it lights it. Hand-maintained on purpose — see the note above.
#:
#: Controls with no LED (encoders, the write-suppressed wheel elements) are absent by design.
#: `Motion_Keyboard`'s Octave and A-H keys have their own dedicated guard already.
REQUIRED_SKIN_KEYS = {
    ("Modifier_Background", "shift"): ("ModifierBackground.Shift", "ModifierBackground.ShiftPressed"),

    ("Transport", "play_button"): ("Transport.PlayOn", "Transport.PlayOff"),
    ("Transport", "stop_button"): ("Transport.StopOn", "Transport.StopOff", "Transport.StopPressed"),
    ("Transport", "tap_tempo_button"): ("Transport.TapTempo", "Transport.TapTempoPressed"),
    ("Transport", "loop_button"): ("Transport.LoopOn", "Transport.LoopOff"),
    ("Transport", "metronome_button"): ("Transport.MetronomeOn", "Transport.MetronomeOff"),
    ("Transport", "capture_midi_button"): ("Transport.CanCaptureMidi",),
    # Ours (transport.py) — the framework has no equivalent control.
    ("Transport", "record_button"): ("Transport.RecordOn", "Transport.RecordOff", "Transport.Flash"),
    ("Transport", "loop_toggle_button"): ("Transport.LoopOn", "Transport.LoopOff", "Transport.Flash"),
    ("Transport", "back_to_arrangement_button"): (
        "Transport.BackToArrangementOn", "Transport.BackToArrangementOff", "Transport.Flash",
    ),
    ("Transport", "set_cue_button"): ("Transport.SetCue", "Transport.SetCuePressed"),

    ("Undo_Redo", "undo_button"): ("UndoRedo.Undo", "UndoRedo.UndoPressed"),

    ("Target_Channel_Strip", "solo_button"): ("Mixer.SoloOn", "Mixer.SoloOff"),
    ("Target_Channel_Strip", "mute_button"): ("Mixer.MuteOn", "Mixer.MuteOff"),
    ("Mixer", "arm_buttons"): ("Mixer.ArmOn", "Mixer.ArmOff"),

    ("View_Toggle", "main_view_toggle_button"): ("ViewToggle.SessionOn", "ViewToggle.SessionOff"),
    ("View_Toggle", "browser_view_toggle_button"): ("ViewToggle.BrowserOn", "ViewToggle.BrowserOff"),
    ("View_Toggle", "clip_view_toggle_button"): ("ViewToggle.ClipOn", "ViewToggle.ClipOff"),

    ("View_Control", "prev_track_button"): ("ViewControl.Track", "ViewControl.TrackPressed"),
    ("View_Control", "next_track_button"): ("ViewControl.Track", "ViewControl.TrackPressed"),
    ("View_Control", "prev_scene_button"): ("ViewControl.Scene", "ViewControl.ScenePressed"),
    ("View_Control", "next_scene_button"): ("ViewControl.Scene", "ViewControl.ScenePressed"),

    # 🐛 The pair this whole section exists for. Undeclared until 2026-08-03.
    ("Session_Navigation", "page_left_button"): ("Session.Navigation", "Session.NavigationPressed"),
    ("Session_Navigation", "page_right_button"): ("Session.Navigation", "Session.NavigationPressed"),

    ("Device", "prev_bank_button"): ("Device.Bank.Navigation", "Device.Bank.NavigationPressed"),
    ("Device", "next_bank_button"): ("Device.Bank.Navigation", "Device.Bank.NavigationPressed"),
    ("Device_Navigation", "scroll_up_button"): ("Device.Navigation", "Device.NavigationPressed"),
    ("Device_Navigation", "scroll_down_button"): ("Device.Navigation", "Device.NavigationPressed"),
}

#: Skin keys a bound component references that we deliberately do **not** declare, with the
#: reason. Anything not on this list and not declared is a failure.
SKIN_KEYS_DELIBERATELY_ABSENT = {
    # Wrapped in `OptionalSkinEntry(name=..., fallback_name='Mixer.ArmOn')`, and
    # `Skin._from_wrapper` follows the fallback when the preferred name is undeclared — so an
    # implicitly-armed track already gets our red. Declaring it would only be to give implicit
    # arm a *different* colour from explicit arm, which we do not want.
    "Mixer.ImplicitArmOn",
}


def _declared_skin_keys():
    """Every dotted key `skin.py` declares, e.g. `Transport.PlayOn`, `Device.Bank.Selected`.

    Read from the AST rather than by importing: `skin.py` pulls in `colors.py`, which imports
    the framework, so the suite cannot execute it.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "skin.py"), encoding="utf-8").read())
    keys = set()
    namespaces = set()

    def walk(node, prefix):
        for item in node.body:
            if isinstance(item, ast.ClassDef):
                name = f"{prefix}.{item.name}" if prefix else item.name
                namespaces.add(name)
                walk(item, name)
            elif isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name) and prefix:
                        keys.add(f"{prefix}.{target.id}")

    for item in tree.body:
        # The outer `class Skin:` is the container, not a namespace.
        if isinstance(item, ast.ClassDef) and item.name == "Skin":
            walk(item, "")
    return keys, namespaces


def _skin_key_literals(relative_paths):
    """Skin-key string constants in a component's `.pyc`, e.g. `'Session.Navigation'`."""
    import re

    try:
        from xdis.load import load_module
    except ImportError:
        return None
    pattern = re.compile(r"^[A-Z][A-Za-z0-9]*(\.[A-Z][A-Za-z0-9]*)+$")
    found = set()
    for relative in relative_paths:
        path = os.path.join(FRAMEWORK_DIR, relative)
        if not os.path.exists(path):
            continue
        try:
            code = load_module(path)[3]
        except Exception:
            continue

        def walk(obj):
            yield obj
            for const in obj.co_consts:
                if hasattr(const, "co_consts"):
                    yield from walk(const)

        for obj in walk(code):
            for const in obj.co_consts:
                if isinstance(const, str) and pattern.match(const):
                    found.add(const)
    return found


def _bound_components():
    """Every component named in `create_mappings()`, at any nesting depth."""
    names = set()
    for name, section in MAPPINGS.items():
        if not isinstance(section, dict):
            continue
        if name in MODES_COMPONENTS:
            for spec in section.values():
                if not isinstance(spec, dict):
                    continue
                for part in spec.get("modes", [spec]):
                    if isinstance(part, dict) and part.get("component"):
                        names.add(part["component"])
        else:
            names.add(name)
    return names


def test_every_skin_namespace_a_bound_component_uses_is_declared():
    """Derived guard: if we bind a component, its skin namespace must exist in `skin.py`.

    This is the cheap, maintenance-free half. It would have failed the moment
    `Session_Navigation` was mapped, because `skin.py` had no `Session` class at all — and it
    keeps failing for the next component whose namespace we forget, without anyone having to
    remember to extend a list.

    It checks *namespaces*, not individual keys, on purpose: a component references keys for
    controls we never map (`Transport.PunchOn`, `Session.ClipPlaying`), and demanding all of
    them would be noise. The exact keys for the controls we **do** map are pinned by
    `test_bound_controls_have_a_real_skin_colour` below.
    """
    check(
        os.path.isdir(FRAMEWORK_DIR),
        "Resources/control_surface is missing, so no skin namespace can be resolved against "
        "the real framework. A run without this guard is not a pass.",
    )
    if not os.path.isdir(FRAMEWORK_DIR):
        return

    _keys, namespaces = _declared_skin_keys()
    skipped, checked = [], 0

    for component in sorted(_bound_components()):
        wanted = set(COMPUTED_SKIN_NAMESPACES.get(component, ()))
        sources = FRAMEWORK_COMPONENT_SOURCES.get(component)
        if sources:
            literals = _skin_key_literals(sources)
            if literals is None:
                skipped.append(f"{component} — xdis is not installed")
                continue
            wanted |= {literal.split(".")[0] for literal in literals}
        if not wanted:
            continue
        checked += 1
        for namespace in sorted(wanted):
            check(
                namespace in namespaces,
                f"{component} asks the skin for {namespace}.* but skin.py declares no "
                f"{namespace} class — every one of those keys silently becomes a BasicColors, "
                f"which renders colourless on this device",
            )

    check(
        not skipped,
        "these components' skin namespaces were NOT checked:\n       "
        + "\n       ".join(skipped)
        + "\n     Fix with: pip install xdis",
    )
    check(checked >= 5, f"expected to check several components, only did {checked}")


def test_bound_controls_have_a_real_skin_colour():
    """Explicit guard: every LED-bearing control we map has its exact keys declared.

    Hand-maintained (`REQUIRED_SKIN_KEYS`), because the framework does not link a control name
    to its skin keys anywhere a walker could read. Kept honest from both ends: the table must
    only name controls that are really mapped, so a stale entry fails just as loudly as a
    missing skin key.
    """
    declared, _namespaces = _declared_skin_keys()

    # Which (component, control) pairs does create_mappings actually bind?
    bound = set()

    def collect(component, section):
        for key, value in section.items():
            if key not in MAPPING_META_KEYS and isinstance(value, str):
                bound.add((component, key))

    for name, section in MAPPINGS.items():
        if not isinstance(section, dict):
            continue
        if name in MODES_COMPONENTS:
            for spec in section.values():
                if not isinstance(spec, dict):
                    continue
                for part in spec.get("modes", [spec]):
                    if isinstance(part, dict) and part.get("component"):
                        collect(part["component"], part)
        else:
            collect(name, section)

    for (component, control), keys in sorted(REQUIRED_SKIN_KEYS.items()):
        check(
            (component, control) in bound,
            f"REQUIRED_SKIN_KEYS names {component}.{control}, which create_mappings no longer "
            f"binds — a stale row here weakens the guard silently",
        )
        for key in keys:
            if key in SKIN_KEYS_DELIBERATELY_ABSENT:
                continue
            check(
                key in declared,
                f"{component}.{control} needs skin key {key!r} and skin.py does not declare "
                f"it — the framework will fall back to BasicColors, which has no RGB triple "
                f"and renders colourless on the Motion",
            )

    # The absent-by-design list must stay honest too: an entry that IS declared is a
    # contradiction, and one nothing asks for is dead weight.
    for key in sorted(SKIN_KEYS_DELIBERATELY_ABSENT):
        check(
            key not in declared,
            f"{key} is on SKIN_KEYS_DELIBERATELY_ABSENT but skin.py declares it — remove one",
        )


def test_the_shift_skin_key_is_the_computed_one():
    """`ModifierBackground.Shift`, not `Modifier.On`. The keys are built from names at runtime.

    🐛 `skin.py` carried `class Modifier: On/Off` for months — a namespace nothing in the
    framework ever asks for. `ModifierBackgroundComponent._setup_control_state` builds
    `"{}.{}".format(self.name.title().replace("_", ""), name.title().replace("_", ""))`, so
    binding `shift` on `Modifier_Background` asks for `ModifierBackground.Shift` and
    `ModifierBackground.ShiftPressed`. Both were undeclared, so Shift resolved to
    `BasicColors.OFF` at rest (dark) and `BasicColors.ON` while held — a state-only write that
    wears whatever RGB the address happened to hold. It looked like a working momentary light.

    Recomputed here rather than hardcoded, so the derivation is checked and not just the
    answer.
    """
    declared, namespaces = _declared_skin_keys()

    section = MAPPINGS.get("Modifier_Background", {})
    check(bool(section), "Modifier_Background must still be mapped")
    for control in section:
        if control in MAPPING_META_KEYS:
            continue
        base = "Modifier_Background".title().replace("_", "")
        name = control.title().replace("_", "")
        for key in (f"{base}.{name}", f"{base}.{name}Pressed"):
            check(
                key in declared,
                f"binding {control!r} on Modifier_Background makes the framework ask for "
                f"{key!r}; skin.py must declare it",
            )

    check(
        "Modifier" not in namespaces,
        "skin.py declares a `Modifier` skin class — nothing asks for that namespace; the "
        "component's own name makes it `ModifierBackground`",
    )


def test_control_handlers_have_the_framework_arity():
    """A `control_list` event handler takes `(self, control)` — the index is `control.index`.

    Verified against the framework's own `ActiveParameterComponent.touch_controls` and
    `SessionComponent.stop_track_clip_buttons`, both of which read `button.index`. Declaring
    `(self, index, control)` instead — the shape 2D `control_matrix` handlers use — raised
    `TypeError: ... missing 1 required positional argument` on the first touch.

    A plain (non-list) `ButtonControl` handler takes `(self, value)`.
    """
    import ast

    for filename in ("screen_component.py", "transport.py"):
        path = os.path.join(SCRIPT_DIR, filename)
        tree = ast.parse(open(path, encoding="utf-8").read())
        for cls in [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]:
            # Which class attributes are control lists, and which are plain controls?
            list_controls, plain_controls = set(), set()
            for item in cls.body:
                if not isinstance(item, ast.Assign) or not isinstance(item.value, ast.Call):
                    continue
                func = item.value.func
                factory = func.id if isinstance(func, ast.Name) else getattr(func, "attr", "")
                for target in item.targets:
                    if not isinstance(target, ast.Name):
                        continue
                    if factory in ("control_list", "control_matrix"):
                        list_controls.add(target.id)
                    elif factory.endswith("Control"):
                        plain_controls.add(target.id)

            for item in cls.body:
                if not isinstance(item, ast.FunctionDef):
                    continue
                for decorator in item.decorator_list:
                    if not (
                        isinstance(decorator, ast.Attribute)
                        and isinstance(decorator.value, ast.Name)
                        and decorator.attr in ("pressed", "released", "value", "double_clicked")
                    ):
                        continue
                    owner = decorator.value.id
                    args = [a.arg for a in item.args.args]
                    if owner in list_controls:
                        check_equal(
                            args,
                            ["self", args[1] if len(args) > 1 else "?"],
                            f"{filename}:{item.name} handles a control_list event and must take "
                            f"exactly (self, control) — got {args}",
                        )
                        # And it must derive the index from the control, not assume one.
                        body_src = ast.dump(item)
                        check(
                            "index" in body_src,
                            f"{filename}:{item.name} should use control.index",
                        )
                    elif owner in plain_controls:
                        check_equal(
                            len(args),
                            2,
                            f"{filename}:{item.name} handles a plain control event and must take "
                            f"(self, value) — got {args}",
                        )


def test_matrix_helpers_are_not_passed_channel():
    """Regression guard for a real failed load.

    `add_matrix` supplies `channel` to `create_encoder`/`create_button` itself, so
    passing an explicit `channel=` to `add_encoder_matrix` / `add_button_matrix` raises
    `TypeError: got multiple values for keyword argument 'channel'` and the whole
    script fails to load. The singular `add_encoder` / `add_button` DO accept `channel`.
    Source-level check because the framework can't be imported offline.
    """
    import ast

    matrix_helpers = {"add_encoder_matrix", "add_button_matrix", "add_matrix", "add_submatrix"}
    singular_helpers = {"add_encoder", "add_button", "add_modifier_button"}

    source = open(os.path.join(SCRIPT_DIR, "elements.py"), encoding="utf-8").read()
    tree = ast.parse(source)

    seen_matrix = 0
    seen_singular_with_channel = 0
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        name = node.func.attr
        kwargs = {keyword.arg for keyword in node.keywords}
        if name in matrix_helpers:
            seen_matrix += 1
            check(
                "channel" not in kwargs,
                f"{name}() must not be passed channel= — the framework supplies it, and "
                "the duplicate raises TypeError and fails the whole script load",
            )
        elif name in singular_helpers and "channel" in kwargs:
            seen_singular_with_channel += 1

    check(seen_matrix > 0, "expected at least one matrix helper call to inspect")
    check(
        seen_singular_with_channel > 0,
        "singular add_encoder/add_button DO take channel=; expected some to use it",
    )


# ---------------------------------------------------------------------------
# The transient notification bar (Template 1)
# ---------------------------------------------------------------------------
def _show_notification(model, view, title, value):
    view.activate()
    view.render(notification.NotificationContent(title=title, value=value))
    return model.flush()


def test_notification_bar_matches_the_studio_pro_capture():
    """Byte-for-byte against the octave capture of 2026-07-26.

    Studio Pro strips the Menu template down to two bold texts on the header bar: header
    labels 0 and 2 carry them, labels 1 and 3 and the header *title* are hidden, all four
    footer labels are hidden, and the footer divider is blacked out. Those are the addresses
    the capture writes, and getting any of them wrong draws a half-built menu.
    """
    recorder, model = make_model()
    view = notification.NotificationView(model)
    _show_notification(model, view, "Octave", "+1")
    frames = set(recorder.messages)

    def sysex(zone, element, attr, *payload):
        return (
            midi.MOTION_SYSEX_HEADER
            + (midi.MSG_SCREEN_UPDATE, screen.Menu.template, zone, element, attr)
            + tuple(payload)
            + (midi.SYSEX_END,)
        )

    # The two texts, at the slots the capture used, spelled out in ASCII.
    check(
        sysex(1, 1, midi.ATTR_TEXT, *b"Octave") in frames,
        "the title must go to header label 0 as ASCII, as `01 01 01 00 4F 63 74 61 76 65`",
    )
    check(
        sysex(1, 3, midi.ATTR_TEXT, *b"+1") in frames,
        "the value must go to header label 2, as `01 01 03 00 2B 31`",
    )
    # Visibility, exactly as captured: 1/3 shown, 2/4 and the title hidden.
    for element, shown in ((1, 1), (2, 0), (3, 1), (4, 0), (5, 0)):
        check(
            sysex(1, element, midi.ATTR_VISIBLE, shown) in frames,
            f"header element {element} must be {'shown' if shown else 'hidden'} — "
            f"the capture sends `01 01 {element:02X} 03 {shown:02X}`",
        )
    # Bold on both texts, and only those.
    for element in (1, 3):
        check(
            sysex(1, element, midi.ATTR_FONT, screen.FONT_BOLD) in frames,
            f"header element {element} must be bold, as `01 01 {element:02X} 04 01`",
        )
    # The whole footer goes away.
    for element in (1, 2, 3, 4):
        check(
            sysex(6, element, midi.ATTR_VISIBLE, 0) in frames,
            f"footer label {element} must be hidden, as `01 06 {element:02X} 03 00`",
        )
    check(
        sysex(5, 0, midi.ATTR_COLOR, 0, 0, 0) in frames,
        "the footer divider must be blacked out, as `01 05 00 01 00 00 00` — left lit it "
        "hangs as a bright line across an otherwise empty screen",
    )
    # And the template actually gets shown.
    check(
        midi.MOTION_SYSEX_HEADER
        + (midi.MSG_SCREEN_TEMPLATE, screen.Menu.template, midi.SYSEX_END)
        in frames,
        "the bar is only visible once Template 1 is selected (`F0 08 26 20 01 F7`)",
    )


def test_a_repeat_notification_costs_two_messages():
    """The chrome is identical every time, so only the value and the template select move.

    This is the whole reason we do not copy Studio Pro's restore-and-repaint: its renderer
    does not diff, so it spends ~65 messages per octave press. If this number ever grows,
    something has started rewriting constant chrome on every showing.
    """
    recorder, model = make_model()
    view = notification.NotificationView(model)
    first = _show_notification(model, view, "Octave", "+1")
    check(first > 10, f"the first showing paints the chrome (got {first} messages)")

    # Come back to the base template, as the timeout does.
    model.select_template(screen.Params.template)
    model.flush()
    recorder.clear()

    second = _show_notification(model, view, "Octave", "+2")
    check_equal(
        second,
        2,
        "a repeat notification must cost exactly the value text plus the template select",
    )


def test_dismissing_the_bar_leaves_the_base_template_untouched():
    """Going back to a mode's screen is one message, and it is only the template select.

    The device keeps each template's element state while another template is displayed —
    which the Song <-> Plugin mode switch already relies on — so nothing needs repainting.
    Studio Pro repaints all of Template 3 on the way back; we must not, or every octave press
    would cost sixty-odd messages for no change.
    """
    recorder, model = make_model()
    params = display.ParamsView(model)
    params.activate()
    params.render(sample_params_content())
    model.flush()

    bar = notification.NotificationView(model)
    _show_notification(model, bar, "Octave", "+1")
    recorder.clear()

    # Dismiss: reselect the base template and re-render the unchanged content.
    params.activate()
    params.render(sample_params_content())
    sent = model.flush()
    check_equal(
        sent, 1, "dismissing must send only the template select, not a repaint"
    )
    check_equal(
        recorder.messages[0],
        midi.MOTION_SYSEX_HEADER
        + (midi.MSG_SCREEN_TEMPLATE, screen.Params.template, midi.SYSEX_END),
        "and that one message must be the base template select",
    )


def test_notification_view_rejects_the_other_templates_content():
    """Three content types now share field names; a mismatch must fail loudly."""
    _, model = make_model()
    view = notification.NotificationView(model)
    for wrong in (sample_params_content(), display.MainContent(title="x")):
        try:
            view.render(wrong)
        except TypeError:
            check(True, "wrong content type raised")
        else:
            check(
                False,
                f"NotificationView accepted {type(wrong).__name__} instead of raising — "
                f"that is how a view draws a plausible-looking wrong screen",
            )


def test_the_bar_never_shares_an_element_with_a_mode_view():
    """One owner per element, across templates.

    The overlay lives on Template 1 and both mode views live on 0 and 3, so they cannot
    collide today — but this asserts it rather than assuming it, because the moment a real
    Menu view arrives it will want these same addresses.
    """
    _, model = make_model()
    bar = notification.NotificationView(model)
    bar.activate()
    bar.render(notification.NotificationContent(title="Octave", value="+1"))
    bar_templates = {key[0] for key in model._desired}
    check_equal(
        bar_templates,
        {screen.Menu.template},
        "the notification view must write to Template 1 and nothing else",
    )

    _, other = make_model()
    main = display.MainView(other)
    main.activate()
    main.render(display.MainContent(title="x"))
    params = display.ParamsView(other)
    params.activate()
    params.render(sample_params_content())
    check(
        screen.Menu.template not in {key[0] for key in other._desired},
        "no mode view may write to Template 1 — it belongs to the notification bar",
    )


def _exec_module_function(filename, name):
    """Execute one module-level function from a framework-importing module.

    `keyboard.py` imports `PlayableComponent`, so the suite cannot import it — but a
    self-contained function can be lifted out of the AST and run for real. That beats
    asserting on its source text, which is how several guards here used to pass while the
    code was broken (a docstring matched the substring they searched for).
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, filename), encoding="utf-8").read())
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            namespace = {}
            exec(compile(ast.Module(body=[node], type_ignores=[]), filename, "exec"), namespace)
            return namespace[name]
    return None


def test_signed_label_matches_the_factory_bytes():
    """Rest reads `0`, not `+0`.

    The capture is unambiguous: returning to zero sent the single byte `0x30`, while +1 sent
    `2B 31`. `f"{n:+d}"` alone would have put a `+` in front of the resting state.

    One function serves both the Octave bar and the A-H "Root Shifted" bar. It was
    `octave_label` while octave was the only caller; naming it for one of two callers is how a
    second copy gets written, and two copies of this rule would eventually disagree about rest.
    """
    label = _exec_module_function("keyboard.py", "signed_label")
    check(label is not None, "keyboard.py must define a module-level signed_label()")
    if label is None:
        return
    check_equal(label(0), "0", "rest is a bare 0 — the factory sends 0x30, not 0x2B 0x30")
    check_equal(label(1), "+1", "up one octave is +1 — the factory sends 2B 31")
    check_equal(label(-2), "-2", "down two octaves keeps its minus sign")
    check_equal(label(3), "+3", "the limit still reads signed")
    # The root shift reuses it, and its range is -4..+3 rather than -3..+3.
    check_equal(label(-4), "-4", "bank A is four semitones down and keeps its sign")

    # And it must be self-contained: `_exec_module_function` compiles the single function node
    # into an empty namespace, so a call out to a shared helper would raise NameError here
    # rather than at import. That is exactly why this rule is written inline.
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read())
    node = next(
        (n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "signed_label"),
        None,
    )
    if node is not None:
        called = {
            n.func.id
            for n in ast.walk(node)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
        }
        check(
            not called,
            "signed_label must call nothing — the offline harness runs it in an empty "
            f"namespace, so {sorted(called)} would raise NameError",
        )


def test_octave_buttons_show_the_direction_that_is_engaged():
    """Up lights when the offset is positive, Down when it is negative — not either/or.

    `[INF]` from the capture: at +1 the host wrote *Up* white and never touched Down. Had the
    rule been "both light whenever the offset is non-zero", Down would have been written too.
    Coding it as `!= 0` would light both buttons and lose the direction.
    """
    import ast

    tree = ast.parse(open(os.path.join(SCRIPT_DIR, "keyboard.py"), encoding="utf-8").read())
    refresh = next(
        (
            n
            for n in ast.walk(tree)
            if isinstance(n, ast.FunctionDef) and n.name == "_refresh_octave_leds"
        ),
        None,
    )
    check(refresh is not None, "keyboard.py must define _refresh_octave_leds")
    if refresh is None:
        return

    directions = {}
    for node in ast.walk(refresh):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Attribute) and target.attr == "is_on":
                owner = target.value
                if isinstance(owner, ast.Attribute):
                    directions[owner.attr] = node.value

    for button, operator in (
        ("octave_up_button", ast.Gt),
        ("octave_down_button", ast.Lt),
    ):
        test_node = directions.get(button)
        check(test_node is not None, f"{button}.is_on must be assigned")
        if test_node is None:
            continue
        check(
            isinstance(test_node, ast.Compare)
            and isinstance(test_node.ops[0], operator),
            f"{button}.is_on must test the offset with {operator.__name__} — "
            f"'!= 0' would light both buttons and lose which way you moved",
        )


def test_octave_buttons_rest_dim_and_brighten_only_on_press():
    """State byte and RGB carry different meanings and must not be conflated.

    From the capture: the button sits at state **63** and goes to **127** only while
    physically held, while its *colour* tracks the offset. Giving the resting entry a full
    127 would make an untouched keyboard look like a held one.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "colors.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    assignments = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value

    for name, expected_rgb in (("BLUE_DIM", (0, 52, 102)), ("WHITE_DIM", (127, 127, 127))):
        call = assignments.get(name)
        check(call is not None, f"colors.py must define Rgb.{name}")
        if call is None:
            continue
        rgb = tuple(a.value for a in call.args if isinstance(a, ast.Constant))
        check_equal(rgb, expected_rgb, f"Rgb.{name} must carry the factory triple")
        state = next(
            (k.value for k in call.keywords if k.arg == "on_value"), None
        )
        check(
            isinstance(state, ast.Name) and state.id == "STATE_DIM",
            f"Rgb.{name} must rest at STATE_DIM (63) — a full 127 reads as 'held'",
        )

    skin_tree = ast.parse(open(os.path.join(SCRIPT_DIR, "skin.py"), encoding="utf-8").read())
    keyboard_class = next(
        (
            n
            for n in ast.walk(skin_tree)
            if isinstance(n, ast.ClassDef) and n.name == "Keyboard"
        ),
        None,
    )
    check(keyboard_class is not None, "skin.py must define a Keyboard skin class")
    if keyboard_class is None:
        return
    entries = {
        t.id: n.value.attr
        for n in keyboard_class.body
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Attribute)
        for t in n.targets
        if isinstance(t, ast.Name)
    }
    check_equal(entries.get("Octave"), "BLUE_DIM", "the resting octave colour is dim blue")
    check_equal(
        entries.get("OctaveShifted"),
        "WHITE_DIM",
        "the engaged octave colour is dim white — it is on_color, not pressed_color",
    )


def test_notification_restarts_its_clock_rather_than_queueing():
    """Holding Octave Up must keep one bar alive, not stack four of them."""
    import ast

    tree = ast.parse(
        open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    )
    notify = next(
        (n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "notify"),
        None,
    )
    check(notify is not None, "screen_component must define notify()")
    if notify is None:
        return

    order = []
    for node in ast.walk(notify):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "_kill_task":
                order.append(("kill", node.lineno))
            elif node.func.attr == "add":
                order.append(("add", node.lineno))
    order.sort(key=lambda pair: pair[1])
    check(
        [step for step, _ in order][:2] == ["kill", "add"],
        "notify() must kill any pending dismissal *before* scheduling the next one, or a "
        "held button queues one timeout per press and the bar outstays every one of them",
    )


def test_the_notification_never_outlives_what_replaced_it():
    """A mode change, and teardown, must both take the bar down immediately."""
    import ast

    tree = ast.parse(
        open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    )
    functions = {
        n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)
    }

    mode_change = functions.get("_on_selected_mode_changed")
    check(mode_change is not None, "screen_component must handle selected_mode")
    if mode_change is not None:
        clears = any(
            isinstance(n, ast.Assign)
            and any(
                isinstance(t, ast.Attribute) and t.attr == "_notification"
                for t in n.targets
            )
            for n in ast.walk(mode_change)
        )
        check(
            clears,
            "a mode change must clear the bar — you asked for a different screen, you should "
            "not have to wait a second for it",
        )

    disconnect = functions.get("disconnect")
    check(disconnect is not None, "screen_component must define disconnect()")
    if disconnect is not None:
        killed = {
            n.args[0].value
            for n in ast.walk(disconnect)
            if isinstance(n, ast.Call)
            and isinstance(n.func, ast.Attribute)
            and n.func.attr == "_kill_task"
            and n.args
            and isinstance(n.args[0], ast.Constant)
        }
        check(
            "_notification_task" in killed,
            "disconnect() must kill the dismissal task — a timer that fires into a torn-down "
            "component is the same class of bug as the reload that blanked the screen",
        )


def _template_elements(template):
    """Every (zone, element) on a template, and which attributes it accepts.

    Read from `Motion32_Screen_Template_Map.csv` — the extracted list of all 433 attribute
    handlers — so this cannot go stale against a remembered list.
    """
    import csv

    path = os.path.join(SCRIPT_DIR, "Resources", "Motion32_Screen_Template_Map.csv")
    if not os.path.exists(path):
        return None
    elements = {}
    with open(path, encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["template"] == "template" or int(row["template"]) != template:
                continue
            key = (int(row["zone"]), int(row["element"]))
            elements.setdefault(key, set()).add(row["attr"])
    return elements


def test_the_bar_claims_every_element_on_its_template():
    """🐛 An element we never write is **not blank** — it is whatever the firmware left there.

    The first hardware run of the notification bar drew the device's own placeholders straight
    through it: `MenuItem0`..`MenuItem5`, twice, from the twelve TEXT_ROW elements in zones 3
    and 4 that `paint_chrome` had not touched. Nothing about the octave logic was wrong; the
    screen simply had content we had not claimed.

    The earlier tests all passed, because every one of them asserted that the elements we
    *thought about* were correct. This one asks the opposite question — is there anything on
    this template we did not think about? — and derives the list from the template map rather
    than from memory, so a future view on any template gets the same guard for free.
    """
    expected = _template_elements(screen.Menu.template)
    check(expected is not None, "the screen template map must be present to check this")
    if not expected:
        return

    _, model = make_model()
    view = notification.NotificationView(model)
    view.activate()
    view.render(notification.NotificationContent(title="Octave", value="+1"))

    written = {}
    for template, zone, element, attr in model._desired:
        if template == screen.Menu.template:
            written.setdefault((zone, element), set()).add(attr)

    for address in sorted(expected):
        attrs = expected[address]
        got = written.get(address)
        check(
            got is not None,
            f"Template 1 element {address} is never written by the notification bar — "
            f"the firmware's own content shows through (this is how MenuItem0..5 appeared)",
        )
        if got is None:
            continue
        if "text" not in attrs:
            continue
        # A text-capable element must be deliberately hidden or deliberately filled. Left
        # alone it displays the factory placeholder.
        hidden = model._desired.get(
            (screen.Menu.template,) + address + (midi.ATTR_VISIBLE,)
        ) == (0,)
        filled = (screen.Menu.template,) + address + (midi.ATTR_TEXT,) in model._desired
        check(
            hidden or filled,
            f"Template 1 element {address} can carry text, so the bar must either hide it "
            f"or give it text — leaving it shows whatever the firmware put there",
        )


def test_the_sends_grid_is_tracks_by_sends():
    """🔑 **Columns are tracks, rows are sends — encoder 1 and 5 are send A and B of track 1.**

    The user's spec (2026-08-03), and the point of the page: a column sits in the same place as
    its strip on the Volume page, so the mix reads the same across pages.

    🔑 **And no encoder is ever dead.** Sends are taken in pairs, with a leftover odd send given
    its own page of one row x eight tracks. The obvious arithmetic (`2 x ceil(S/2)` pages of four
    tracks) left the bottom row unmapped on the last two pages of every odd count — eight dead
    encoders in an ordinary three-return set.

    ⚠️ **This executes `sends.page_table` and `sends.page_slots` for real.** The first version of
    this guard re-implemented the rule and therefore tested its own arithmetic: putting the bug
    back did **not** fail it. That is precisely the failure mode §5 of the handoff warns about —
    an assertion that has never failed has not been shown to test anything — so the rule was
    moved to module level for `_exec_module_function` to lift out and run.
    """
    build = _exec_module_function("sends.py", "page_table")
    slots_for = _exec_module_function("sends.py", "page_slots")
    check(build is not None, "sends.py must expose page_table at module level")
    check(slots_for is not None, "sends.py must expose page_slots at module level")
    if build is None or slots_for is None:
        return

    # `_exec_module_function` compiles the single function node, so the module constants it
    # closes over have to be supplied — which also pins them.
    import ast

    constants = {
        t.id: n.value.value
        for n in ast.parse(open(os.path.join(SCRIPT_DIR, "sends.py"), encoding="utf-8").read()).body
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Constant)
        for t in n.targets
        if isinstance(t, ast.Name)
    }
    check_equal(constants.get("ENCODER_COUNT"), 8, "eight encoders")
    check_equal(constants.get("MAX_SENDS_PER_PAGE"), 2, "two physical rows of encoders")
    check_equal(constants.get("RING_TRACKS"), 8, "the session ring holds eight strips")
    for function in (build, slots_for):
        function.__globals__.update(constants)

    ring = constants["RING_TRACKS"]

    # The case the user named, and the arrangement it must produce.
    table = build(2)
    check_equal(len(table), 2, "8 tracks x 2 sends is two pages of four")
    first = slots_for(table[0], 2)
    check_equal(
        list(first),
        [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1)],
        "encoders 1-4 are send A of tracks 1-4; encoders 5-8 are send B of the same four",
    )
    for column in range(4):
        top, bottom = first[column], first[column + 4]
        check_equal(
            (top[0], bottom[0]), (column, column),
            f"encoder {column + 1} and encoder {column + 5} must be the same track",
        )
        check(top[1] != bottom[1], "…and they must be different sends")

    # **The invariant the packing rule buys**: every page fully mapped, every pair reachable once.
    #
    # ⚠️ **Through twelve, not eight.** The shipped v3 `ChannelStripComponent` allocates twelve
    # send controls, so nine returns is an ordinary set. Stopping at eight is what let the
    # `page_label` IndexError survive — the geometry was never exercised past H.
    for send_count in range(1, 13):
        table = build(send_count)
        every = [slot for page in table for slot in slots_for(page, send_count)]
        check_equal(
            sum(1 for slot in every if slot is None), 0,
            f"{send_count} send(s): dead encoder slots — a leftover send must take a page of "
            f"one row x eight tracks, not half a page of four",
        )
        check_equal(
            len(every), len(set(every)),
            f"{send_count} send(s): a (track, send) pair appears on more than one page",
        )
        check_equal(
            len(set(every)), ring * send_count,
            f"{send_count} send(s): not every track/send pair is reachable",
        )

    check_equal(len(build(1)), 1, "a single send fills one row of eight tracks")
    check_equal(len(build(3)), 3, "three sends pack into three pages, not four")
    check_equal(len(build(4)), 4, "four sends are four full pages")
    check_equal(build(0), (), "a set with no return tracks has no Sends page")


def test_every_send_has_a_label_and_none_of_them_raise():
    """🐛 **Nine return tracks raised `IndexError` and froze the Sends page.**

    `SEND_LETTERS` was eight characters. `slot_label` guarded the lookup and fell back to a
    number, but `page_label` indexed the string raw — so a set with nine returns labelled its
    *tiles* correctly and then blew up building the page *title*. The screen layer catches that
    higher up, so it never surfaced as an error: the page simply stopped updating and left stale
    text on the device, which is the failure mode this suite exists to catch.

    🔑 **Two callers, one rule.** The fix is a single `send_label()` both of them use. This guard
    executes it for real rather than asserting on its source, so putting the bug back fails here.

    **Twelve is not arbitrary** — the shipped v3 `ChannelStripComponent` allocates twelve send
    controls, so A-L is the range Live itself works in. Past L the label is the 1-based number:
    unfamiliar, but never an exception.
    """
    label = _exec_module_function("sends.py", "send_label")
    check(label is not None, "sends.py must expose send_label at module level")
    if label is None:
        return

    import ast

    constants = {
        t.id: n.value.value
        for n in ast.parse(open(os.path.join(SCRIPT_DIR, "sends.py"), encoding="utf-8").read()).body
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Constant)
        for t in n.targets
        if isinstance(t, ast.Name)
    }
    label.__globals__.update(constants)

    check_equal(
        constants.get("SEND_LETTERS"), "ABCDEFGHIJKL",
        "the framework allocates twelve send controls, so the letters must reach L",
    )

    check_equal(label(0), "A", "send 0 is A")
    check_equal(label(7), "H", "send 7 is H — the old end of the string")
    check_equal(label(8), "I", "send 8 is I — this is the index that used to raise")
    check_equal(label(11), "L", "send 11 is L, the twelfth and last letter")

    # Past the letters, a number rather than an exception.
    check_equal(label(12), "13", "beyond L the label is the 1-based number")
    check_equal(label(99), "100", "an absurd return count still labels rather than raises")

    # **The point of the guard**: no index reachable from any set can raise.
    for index in range(0, 128):
        try:
            text = label(index)
        except Exception as error:
            check(False, f"send_label({index}) raised {type(error).__name__} — it must never raise")
            break
        check(bool(text), f"send_label({index}) returned an empty label")


def test_the_strip_led_index_is_the_factory_mapping():
    """🔑 **`round((count - 1) * normalized)`, not truncation** — `Pads_Banking_and_Strips` §5.4.

    The difference only shows at the ends and at the halfway points, which is exactly where a
    misplaced LED is visible: truncating puts the lit LED a step below the finger for most of the
    strip and never lights the top one at all. So the guard pins a value where `round` and `int`
    disagree rather than only checking the endpoints.

    ⚠️ **This executes `strips.led_index` for real.** `strips.py` is importable offline, but the
    rule is kept module level and self-contained — like `sends.page_table` — so the suite runs the
    shipped arithmetic instead of a copy of it. A guard that re-derives the formula tests its own
    formula, which is the §5 failure this suite exists to avoid.

    Hardware, 2026-08-10: position arrives as a 14-bit pitch bend whose low four bits are always
    zero, so the real input is ~10-bit in a 14-bit field. The mapping still has to cover the full
    `0…16383` range, because nothing guarantees that stays true across firmware versions.
    """
    index_for = _exec_module_function("strips.py", "led_index")
    check(index_for is not None, "strips.py must expose led_index at module level")
    if index_for is None:
        return

    import ast

    constants = {
        t.id: n.value.value
        for n in ast.parse(open(os.path.join(SCRIPT_DIR, "strips.py"), encoding="utf-8").read()).body
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Constant)
        for t in n.targets
        if isinstance(t, ast.Name)
    }
    index_for.__globals__.update(constants)

    count = constants.get("LED_COUNT")
    top = constants.get("POSITION_MAX")
    check_equal(count, 9, "nine LEDs per strip — CC 0x37-0x3F and 0x70-0x78")
    check_equal(top, 16383, "pitch bend is 14-bit, so the position field tops out at 16383")
    if count is None or top is None:
        return

    check_equal(index_for(0), 0, "rest at the bottom lights LED 0")
    check_equal(index_for(top), count - 1, "full travel must reach the LAST LED, not one short")
    check_equal(index_for(top // 2), (count - 1) // 2, "centre position lights the centre LED")

    # **The discriminator.** 8 * 1024 / 16383 = 0.50003 — `round` gives 1, truncation gives 0.
    # Putting the bug back (int() instead of round()) fails here and nowhere else.
    check_equal(
        index_for(1024), 1,
        "just past the half-step must round UP — truncating here is the classic off-by-one that "
        "leaves the lit LED trailing the finger",
    )

    # Out-of-range input is clamped, never raised: the strip is a real-time control and an
    # exception in the position path would take the whole render down mid-slide.
    check_equal(index_for(-1), 0, "a negative position clamps to the bottom")
    check_equal(index_for(top * 2), count - 1, "an over-range position clamps to the top")

    previous = -1
    for value in range(0, top + 1, 7):
        try:
            got = index_for(value)
        except Exception as error:
            check(False, f"led_index({value}) raised {type(error).__name__} — it must never raise")
            break
        if not 0 <= got <= count - 1:
            check(False, f"led_index({value}) = {got}, outside 0..{count - 1}")
            break
        if got < previous:
            check(False, f"led_index went backwards at {value}: {previous} -> {got}")
            break
        previous = got
    check_equal(previous, count - 1, "sweeping the whole range must finish on the top LED")


def test_a_parameter_mapper_releases_when_disabled():
    """🐛 **Plugin mode stopped binding its device after a visit to the Sends page.**

    `MotionSendsComponent` set `mapped_parameter` on the eight encoders and never cleared it, so
    leaving the page left them holding send parameters and the Device component's own mapping did
    not take the elements. Found on hardware 2026-08-03.

    ⚠️ **The framework does this and it is not optional.** `ChannelStripComponent.update()` is
    `_connect_parameters()` when enabled and `_disconnect_parameters()` when not — and the latter
    is just `mapped_parameter = None` across its controls. Ours had only the first half.

    The rule, now that three separate duties have arrived the same way: **a component that maps
    parameters owns the whole lifecycle** — point them, follow whatever moves under them, and let
    go when it is not showing. This checks the third.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "sends.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    update = functions.get("update")
    check(update is not None, "sends.py must define update()")
    if update is None:
        return

    # An `else` (or equivalent) branch must exist — enabling alone is half the contract.
    has_else = any(
        isinstance(node, ast.If) and node.orelse for node in ast.walk(update)
    )
    check(
        has_else,
        "update() must handle the *disabled* case as well — the framework's own channel strip "
        "disconnects its parameters there, and skipping it strands the encoders",
    )

    called = {
        node.func.attr
        for node in ast.walk(update)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }
    check(
        "_release" in called,
        "update() must call _release() when disabled, or the encoders keep the send parameters "
        "and the next mode cannot map them",
    )

    release = functions.get("_release")
    check(release is not None, "sends.py must define _release()")
    if release is not None:
        clears_to_none = any(
            isinstance(node, ast.Assign)
            and any(
                isinstance(t, ast.Attribute) and t.attr == "mapped_parameter"
                for t in node.targets
            )
            and isinstance(node.value, ast.Constant)
            and node.value.value is None
            for node in ast.walk(release)
        )
        check(
            clears_to_none,
            "_release() must set mapped_parameter = None — that is what actually frees the "
            "element for the next component to map",
        )


def test_touch_focuses_the_track_the_encoder_actually_turns():
    """🐛 **Touch selected one track while the encoder turned another's send.**

    On Volume and Pan, encoder N is strip N, so `_strip_track(index)` is the right answer. On the
    **Sends** page encoder N is a (track, send) slot — encoder 5 is track 1's send *B* — so
    selecting the strip at the encoder's index focused a different track from the one the knob
    moved. Found on hardware 2026-08-03, straight after the ring-listener fix made the encoders
    live enough for the mismatch to be visible.

    🔑 **The page owns the mapping, so the page must answer "which track is this".** Anything
    that turns an encoder index into a track has to go through the same resolver the mapping
    does, or the two drift the moment a page lays the encoders out differently.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "screen_component.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    resolver = functions.get("_touched_track")
    check(resolver is not None, "screen_component must define _touched_track")
    if resolver is None:
        return
    dumped = ast.dump(resolver)
    check(
        "MIX_PAGE_SENDS" in dumped,
        "_touched_track must know about the Sends page — that is the one where the encoder "
        "index is not the strip index",
    )
    check(
        "slot_track" in dumped,
        "on the Sends page the touched track must come from the slot, not from the strip at "
        "the encoder's index",
    )

    # And the selection must go through it rather than reaching for the strip directly.
    selector = functions.get("_select_strip_track")
    check(selector is not None, "screen_component must define _select_strip_track")
    if selector is not None:
        # ⚠️ Match **calls**, not substrings. `"_strip_track" not in ast.dump(selector)` is the
        # obvious spelling and it can never pass: the function's own name,
        # `_select_strip_track`, contains that substring. Third time today a substring guard has
        # been wrong — twice too weak, once too strong.
        called = {
            node.func.attr
            for node in ast.walk(selector)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
        }
        check(
            "_touched_track" in called,
            "_select_strip_track must resolve the track through _touched_track",
        )
        check(
            "_strip_track" not in called,
            "_select_strip_track must NOT call _strip_track directly — that assumes encoder "
            "index == strip index, which the Sends page breaks",
        )


def test_anything_mapping_ring_tracks_follows_the_ring():
    """🐛 **Turning a Sends encoder did nothing after paging Left/Right.**

    `MotionSendsComponent` re-mapped on setup, on layer grab and on a page change — but not when
    the ring moved. So the encoders stayed pointed at whichever tracks had been under the strips
    before, and any slot that had been empty kept `mapped_parameter = None` and refused to turn.
    The touch highlight still worked, because that is keyed on the encoder index rather than on
    the mapping — which is exactly what made it look like a hardware fault. Found 2026-08-03.

    ⚠️ **The obligation arrives with the mapping.** Volume and Pan never had this problem:
    `MixerComponent.__init__` subscribes to `__on_offset_changed` on its provider and re-connects
    its own parameters. Taking the mapping into our own hands — which the (track × send) layout
    required — meant inheriting a duty the framework had been discharging silently.

    So the rule, now that two components have needed it: **anything that derives parameters or
    content from the session ring must subscribe to `offset` and `tracks`.** `tracks` matters as
    much as `offset` — adding or deleting a track moves what sits under a strip just as paging
    does.
    """
    import ast

    for filename, why in (
        ("sends.py", "the Sends grid maps a parameter per ring track"),
        ("screen_component.py", "the Mix strips draw a ring track each"),
    ):
        tree = ast.parse(open(os.path.join(SCRIPT_DIR, filename), encoding="utf-8").read())
        listened = set()
        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef):
                continue
            for decorator in node.decorator_list:
                if (
                    isinstance(decorator, ast.Call)
                    and getattr(decorator.func, "id", None) == "listens"
                    and decorator.args
                    and isinstance(decorator.args[0], ast.Constant)
                ):
                    listened.add(decorator.args[0].value)
        for event in ("offset", "tracks"):
            check(
                event in listened,
                f"{filename} must listen for the session ring's {event!r} — {why}, and a "
                f"mapping that does not follow the ring silently points at the wrong track",
            )

    # And the surface has to hand the ring over, or the listener never gets a subject.
    #
    # ⚠️ **Structural, not a substring search.** The first version of this looked for
    # `"sends.bind_session_ring"` in the source and passed with the call deleted — the *comment*
    # above the call contains the same text. That is the exact trap `_exec_module_function`'s
    # docstring records ("a docstring matched the substring they searched for"), and it caught
    # this guard within minutes of it being written.
    surface_tree = ast.parse(
        open(os.path.join(SCRIPT_DIR, "__init__.py"), encoding="utf-8").read()
    )
    binder = next(
        (
            n
            for n in ast.walk(surface_tree)
            if isinstance(n, ast.FunctionDef) and n.name == "_bind_screen_sources"
        ),
        None,
    )
    check(binder is not None, "__init__.py must define _bind_screen_sources")
    if binder is None:
        return
    receivers = {
        node.func.value.id
        for node in ast.walk(binder)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "bind_session_ring"
        and isinstance(node.func.value, ast.Name)
    }
    for receiver, why in (
        ("sends", "the Sends grid"),
        ("screen_component", "the Mix strips"),
    ):
        check(
            receiver in receivers,
            f"_bind_screen_sources must call {receiver}.bind_session_ring(...) — {why} follows "
            f"the ring, and a listener with no subject never fires",
        )


def test_sends_pages_expand_the_wheel_sequence():
    """⚠️ **A `ModesComponent`'s mode list is fixed; the Sends page count is not.**

    The number of Sends pages is a fact about the user's set — tracks × returns — so it cannot
    be declared in `create_mappings`. `sends` is therefore **one mode that expands into several
    wheel steps**, and `mixpages.py` is what knows how many.

    Declaring `sends_1..8` modes and hiding the empty ones would put a guess about set size into
    the mapping table, and still be wrong for the ninth.
    """
    import ast

    source = open(os.path.join(SCRIPT_DIR, "mixpages.py"), encoding="utf-8").read()
    tree = ast.parse(source)
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    for name in ("bind_sends", "_steps", "_sends_pages", "_current_step"):
        check(name in functions, f"mixpages must define {name}")

    steps = functions.get("_steps")
    if steps is not None:
        check(
            "EXPANDING_MODE" in ast.dump(steps),
            "_steps must expand the sends mode rather than treating it as one page",
        )

    step = functions.get("_step")
    check(step is not None, "mixpages must define _step")
    if step is not None:
        dumped = ast.dump(step)
        check(
            "set_page" in dumped,
            "_step must move the Sends sub-page, not only the mode",
        )
        # ⚠️ Order matters: selecting the mode grabs the layer and re-maps the encoders, so the
        # page has to be set first or the first frame maps the previous page's parameters.
        page_at = dumped.index("set_page")
        mode_at = dumped.index("selected_mode")
        check(
            page_at < mode_at,
            "_step must set the sub-page BEFORE selecting the mode — the layer grab re-maps the "
            "encoders, so a late page change maps the wrong parameters for a frame",
        )

    # The mapping table declares exactly one sends page.
    page_names = [k for k, v in MAPPINGS["Mix_Pages"].items() if isinstance(v, dict)]
    check_equal(
        page_names.count("sends"), 1,
        "there must be exactly one 'sends' mode — its pages are expanded at runtime",
    )


def main():
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    print(f"Motion 32 screen engine — {len(tests)} test groups\n")
    for test in tests:
        print(f"  {test.__name__}")
        before = len(_failures)
        try:
            test()
        except Exception as error:  # a crash is a failure, not an abort
            _failures.append(f"{test.__name__} raised {type(error).__name__}: {error}")
        if len(_failures) > before:
            for failure in _failures[before:]:
                print(f"    FAIL {failure}")

    print(f"\n{_checks[0]} assertions, {len(_failures)} failures")
    if _failures:
        print(f"\nFAILED — {len(_failures)} problem(s) above need fixing before this runs on hardware.")
    else:
        print("\nPASSED — every guard ran and every assertion held.")
    return 1 if _failures else 0


if __name__ == "__main__":
    sys.exit(main())
