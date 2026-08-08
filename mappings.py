"""Declarative Ableton component/control assignments.

Left side of each entry = the component's own control name; right side = an element name
from `elements.py`. Shift variants use the framework-generated `*_with_shift`.

**How the framework reads this** (`control_surface_mapping.pyc`): every key that names a
component in `component_map` becomes that component with a `Layer` built from the entry.
Every key that does *not* is treated as a **modes component** — which is how `Main_Modes`
exists without being a built-in. Inside a modes section, a plain string value binds a mode
button, and a dict value defines a mode.
"""

from ableton.v3.control_surface.mode import ImmediateBehaviour

# Song-mode encoder assignments, in physical order: top row 1-4, bottom row 5-8.
#
# Each entry is (framework control name, screen label, owning component). Keeping all three
# together means a label cannot drift from the knob under it, and the per-component layers
# below are derived rather than hand-maintained.
#
# Labels are the *full* names: Song mode renders on Template 3, which has a separate label
# and value element per tile, so there is room for a real word instead of a 7-character
# abbreviation. Budget is MAXCHARS_PARAMS_LABEL.
SONG_ENCODERS = (
    ("tempo_coarse_encoder", "Tempo", "Transport"),
    ("arrangement_position_encoder", "Position", "Transport"),
    ("loop_start_encoder", "Loop Start", "Transport"),
    # ⚠️ **This label is wrong and the readout is wrong with it** (audit 2026-08-03). The
    # control is `loop_length_encoder`, so it changes the loop's *length*, not its end — and
    # `screen_component._song_encoder_readout` then runs that length through `_format_beats`,
    # which assumes an absolute position and adds 1 to bar and beat. A 2-bar loop at bar 3
    # reads `3.1`: neither the end (bar 5) nor the length (2 bars). Fix all three together —
    # label, control and formatter — see `Motion32_Ableton_Build_Handoff.md` §7.
    ("loop_length_encoder", "Loop End", "Transport"),
    ("horizontal_zoom_encoder", "H Zoom", "Zoom"),
    ("vertical_zoom_encoder", "V Zoom", "Zoom"),
    ("cue_encoder", "Cue", "Transport"),
    # Live's preview/cue level, off the master track's mixer device. A genuinely global
    # control, and more use day to day than a second tempo encoder.
    ("prehear_volume_control", "Cue Vol", "Mixer"),
)

# Song-mode bindings that are not encoders, by component. Merged with the encoder layer below
# so each component gets **one** layer per mode — a component's `layer` is a single object, so
# two parts naming the same component in one mode is a shape best avoided.
SONG_EXTRA_BINDINGS = {
    # Soft buttons. Top row 1-4 is over the screen, bottom row 5-8 under it
    # (skin.xml LcdButtonTopRow/BottomRow). Per-mode, not global, so they go dark in any mode
    # that does not claim them.
    "Transport": {
        "loop_toggle_button": "soft_buttons_raw[2]",
        "back_to_arrangement_button": "soft_buttons_raw[3]",
        "set_cue_button": "soft_buttons_raw[6]",
    },
    "View_Toggle": {
        "main_view_toggle_button": "soft_buttons_raw[4]",
        "browser_view_toggle_button": "soft_buttons_raw[5]",
        # Clip <-> Device: shows/hides Live's "Detail/Clip", so hiding it puts the device
        # chain in the detail pane. Lit while Clip view is showing.
        "clip_view_toggle_button": "soft_buttons_raw[7]",
    },
    # Nav moves the selection while in Song mode.
    "View_Control": {
        "prev_track_button": "left_button",
        "next_track_button": "right_button",
        "prev_scene_button": "up_button",
        "next_scene_button": "down_button",
    },
}

#: Every component Song mode touches, in layer order.
SONG_COMPONENTS = ("Transport", "Zoom", "Mixer", "View_Toggle", "View_Control")


def _song_encoder_layer(component):
    """The encoder bindings owned by one component, at their physical positions."""
    return {
        name: f"encoders_raw[{index}]"
        for index, (name, _label, owner) in enumerate(SONG_ENCODERS)
        if owner == component
    }


def _song_layer(component):
    """One merged layer per component: its encoders plus its buttons."""
    return dict(
        {"component": component},
        **_song_encoder_layer(component),
        **SONG_EXTRA_BINDINGS.get(component, {}),
    )


def create_mappings(_):
    return {
        "Modifier_Background": {
            "shift": "shift_button",
        },

        # The Shift pad overlay (Phase 8). **Global, like the keyboard it replaces** — holding
        # Shift should give the same sixteen commands whatever the screen is showing.
        #
        # These are `pads_with_shift` elements, which are a *different element* from the pads
        # the keyboard binds. `ComboElement.priority_increment = 0.5` means a bound one outranks
        # the plain binding while the modifier is held, so Shift+pad fires the command and the
        # keyboard underneath never sees the press. No mode switching, no layer juggling.
        "Motion_Commands": {
            "command_pads": "command_pads",
        },

        # ⚠️ **The top lane has to be *consumed*, not merely left unbound.** Priority is
        # asserted by being in a live layer, so an unbound modified element claims nothing and
        # its pad would keep playing its note under Shift — half the keybed sounding notes while
        # the other half runs destructive edits. `BackgroundComponent` grabs an element with a
        # `NopControl`, which is exactly "claimed, and does nothing".
        #
        # Same reasoning as the four dead keyboard pads, which are silenced by *mode* rather
        # than by being disabled: on this surface, "unbound" and "silent" are opposites.
        "Shift_Pad_Background": {
            "muted_pads_with_shift": "muted_pads_with_shift",
        },

        # The pads, as a piano. Global rather than per-mode: the keybed should play
        # whatever is armed regardless of which view the screen is showing.
        #
        # This binding is what makes the pads reach a track at all. An element the script
        # declares but does not translate is consumed by the control surface — the press
        # shows in Live's Key/MIDI indicator and plays nothing. `PlayableComponent` sets each
        # element's identifier/channel so Live's engine rewrites the note and forwards it.
        "Motion_Keyboard": {
            "matrix": "pads",
            # Octave +/- belongs with the keyboard: it changes the translation.
            "octave_up_button": "octave_up_button",
            "octave_down_button": "octave_down_button",
            # A-H: the pad bank, i.e. where the root sits. Global with the rest of the
            # keyboard — the keybed should answer the same buttons whatever the screen shows.
            # A strict radio resting on E; see keyboard.py.
            "bank_a_button": "bank_a_button",
            "bank_b_button": "bank_b_button",
            "bank_c_button": "bank_c_button",
            "bank_d_button": "bank_d_button",
            "bank_e_button": "bank_e_button",
            "bank_f_button": "bank_f_button",
            "bank_g_button": "bank_g_button",
            "bank_h_button": "bank_h_button",
        },

        # Transport buttons are global — they work in every mode. The component subclasses
        # the framework's TransportComponent (transport.py), so these are its own control
        # names; only `record_button` is ours.
        "Transport": {
            "play_button": "play_button",
            "stop_button": "stop_button",
            "record_button": "record_button",
            "tap_tempo_button": "tap_button",
            "loop_button": "play_button_with_shift",         # Shift+Play -> Loop
            "capture_midi_button": "record_button_with_shift",  # Shift+Rec -> Capture MIDI
            "metronome_button": "tap_button_with_shift",     # Shift+Tap -> Metronome
        },

        # The Control button: leave Scale/Chord for whichever mode was showing before. Global,
        # because it is a way *back* rather than a destination — see scalemode.py for why it is
        # not a fourth entry in the Main_Modes radio.
        "Motion_Mode_Return": {
            "control_button": "control_button",
        },

        # Undo is its own component in the framework, not part of Transport.
        "Undo_Redo": {
            "undo_button": "stop_button_with_shift",          # Shift+Stop -> Undo
        },

        # Solo / Mute follow the focused track. Target_Channel_Strip extends
        # ChannelStripComponent, which is where `solo_button` / `mute_button` come from.
        # Global rather than per-mode: the focused track is meaningful in every view.
        "Target_Channel_Strip": {
            "solo_button": "solo_button",
            "mute_button": "mute_button",
        },

        # Owns Template 0. Encoder touch reveals the parameter value, which then times out
        # — the tile has one text element, so name and value share it, as on the factory.
        "Motion_Screen": {
            "encoder_touch_buttons": "encoder_touch_buttons",
        },

        # The control-focus buttons select the main mode. **Plugin is what reveals the
        # device detail view**, and the encoders are mapped only there, so they cannot
        # silently move parameters while another view is on screen.
        #
        # Only the modes we actually implement are declared. A mode button whose mode has
        # no content is a needless risk, so **Edit** stays unmapped — its element exists in
        # elements.py, ready for whenever that view is designed. Mix was in the same state
        # until 2026-07-29 and is now a full mode, below.
        #
        # The four nav buttons are per-mode rather than global, which lets each mode give
        # them the meaning that fits it and avoids two components fighting over one button.
        "Main_Modes": {
            # **Strict radio: every mode uses ImmediateBehaviour, no toggling.**
            #
            # Plugin previously had ToggleBehaviour so re-pressing it fell back to Song. With
            # only two modes that reads as "Song and Plugin toggle each other", but it does
            # not survive Edit and Mix arriving: "toggle off" has no well-defined destination
            # once there are four peers, and the mode buttons would stop meaning "show me
            # this". A radio scales, and exactly one button is lit at all times either way.
            "default_behaviour": ImmediateBehaviour(),
            "song_button": "song_button",
            "plugin_button": "plugin_button",
            "mix_button": "mix_button",
            # Scale joins the same radio, so pressing Song / Plugin / Mix leaves it — which is
            # what the user asked for and what a radio gives for free.
            "scale_button": "scale_button",

            # First mode listed is the startup default.
            "song": {
                "modes": [_song_layer(component) for component in SONG_COMPONENTS],
            },

            "plugin": {
                "modes": [
                    {
                        # The framework's Device component owns banking, including Live's
                        # curated bank definitions. `prev/next_bank_button` reach the
                        # bank-navigation sub-component through DeviceComponent.__getattr__,
                        # which forwards any `set_*bank*` attribute.
                        "component": "Device",
                        "parameter_controls": "encoders",
                        # The big wheel scrolls parameter banks. `bank_scroll_encoder` reaches
                        # the bank-navigation sub-component via DeviceComponent.__getattr__,
                        # which forwards any `set_*bank*` attribute.
                        "bank_scroll_encoder": "wheel_encoder",
                        # Bank on up/down. Left/right is track navigation below — you need to
                        # reach a channel that *has* a device before banking is any use.
                        "prev_bank_button": "up_button",
                        "next_bank_button": "down_button",
                    },
                    {
                        # Left/right walks the tracks, so any channel with a device is
                        # reachable without touching the mouse.
                        "component": "View_Control",
                        "prev_track_button": "left_button",
                        "next_track_button": "right_button",
                    },
                    {
                        # Step the device selection along the track's chain, on Preset Up/Down.
                        #
                        # The control names are `scroll_up_button` / `scroll_down_button`:
                        # DeviceNavigationComponent extends ScrollComponent, and there is no
                        # `prev_button`/`next_button`. Those were bound here previously and did
                        # nothing at all — an unknown control name in a Layer fails **silently**,
                        # which is why device navigation appeared simply absent.
                        #
                        # Skin keys `Device.Navigation` / `Device.NavigationPressed` and
                        # `Device.Bank.*` all exist in the framework's default skin, and
                        # `create_skin` merges ours *over* those defaults, so no extra skin
                        # entries are needed.
                        # Preset Up steps *forward* through the chain, Preset Down back —
                        # scroll_up moves toward the start of the device list, so the buttons
                        # are crossed deliberately to match the expected direction.
                        "component": "Device_Navigation",
                        "scroll_up_button": "preset_down_button",
                        "scroll_down_button": "preset_up_button",
                    },
                    {
                        # Wheel click: next device on the track, wrapping at the end.
                        # Device_Navigation stops at the ends, so this is ours (wheel.py).
                        "component": "Motion_Wheel",
                        "push_button": "wheel_push_button",
                    },
                ]
            },

            # Scale — Template 1, the factory's own list screen (Phase 10).
            #
            # The pads re-lay to the scale; the wheel scrolls the list; the soft buttons are the
            # factory's `Main / Modes / Key` plus the single `Guide/Locked` toggle top-right.
            # Layout and screen both come from `scalemode.py` + `scales.py`.
            "scale": {
                "modes": [
                    {
                        "component": "Motion_Scale",
                        # The wheel selects the scale or the key, per the State Trace. Same
                        # control, same gesture as paging Mix and scrolling banks in Plugin.
                        "scroll_encoder": "wheel_encoder",
                        # ⚠️ The single top-right toggle is soft button **4** (index 3), not a
                        # pair. Guide and Locked are two states of one setting.
                        "guide_lock_button": "soft_buttons_raw[3]",
                        "category_main_button": "soft_buttons_raw[4]",
                        "category_modes_button": "soft_buttons_raw[5]",
                        # soft_buttons_raw[6] is deliberately blank — the factory leaves a gap
                        # here and so do we; an unlabelled button is dark and does nothing.
                        "category_key_button": "soft_buttons_raw[7]",
                    },
                ]
            },

            # Mix — Template 2, eight channel strips (Phase 7).
            "mix": {
                "modes": [
                    {
                        # Enabling a modes component from inside a mode is how a *nested* mode
                        # set gets scoped. `_create_modes_component` registers `Mix_Pages` in
                        # `component_map`, and a mode part naming a component with no mappings
                        # resolves to the component itself — which the mode system enables on
                        # enter and disables on leave.
                        "component": "Mix_Pages",
                    },
                    {
                        # The wheel pages Volume <-> Pan. Nothing in `ableton.v3` switches
                        # modes from an encoder — `ModesComponent` has only
                        # `cycle_mode_button` and `PageComponent` pages a `Pageable` — so this
                        # is ours. See mixpages.py.
                        "component": "Motion_Mix_Pages",
                        "scroll_encoder": "wheel_encoder",
                    },
                    {
                        # ⚠️ **`volume_controls` is plural and it is not a typo.**
                        # `MixerComponent` has no such attribute; `__getattr__` catches any
                        # name starting with `set` and returns
                        # `partial(self._set_strip_controls, name[4:-1])` — dropping `set_`
                        # and the trailing `s`. So `set_volume_controls` becomes
                        # `volume_control`, which is then looked up on **each channel strip**
                        # with `getattr(strip, name)`. The singular lives on
                        # `ChannelStripComponent`, the plural is the mixer-wide spelling.
                        #
                        # A typo here fails *loudly* rather than silently, unusually for a
                        # Layer name: `getattr(strip, "volumes_control")` raises AttributeError
                        # at bind time. Verified by disassembling `components/mixer.pyc`.
                        # ⚠️ **One layer per component per mode.** A component's `layer` is a
                        # single object, so two sections naming `Mixer` in this mode would
                        # have the second silently replace the first — the same reason
                        # `SONG_EXTRA_BINDINGS` is merged into one dict per component rather
                        # than listed separately. Volume and arm therefore share this entry.
                        # ⚠️ **The encoders are NOT bound here.** They belong to whichever
                        # page is showing, so `volume_controls` / `pan_controls` live in the
                        # `Mix_Pages` component below. Arm stays at Mix level because it means
                        # the same thing on both pages.
                        "component": "Mixer",
                        # The eight LCD buttons arm the eight strips. `arm_buttons` is the
                        # plural spelling that `MixerComponent.__getattr__` maps onto
                        # `arm_button` on each channel strip, so it needs the *matrix*, not
                        # the individual `soft_buttons_raw[i]` elements.
                        #
                        # The LED is driven by the framework from Live's own `track.arm`, not
                        # by us: `_update_arm_button` in `mixer.pyc` listens to the track. So
                        # arming from the mouse lights the button too, and there is no
                        # script-side toggle to fall out of step.
                        "arm_buttons": "soft_buttons",
                    },
                    {
                        # 🐛 **This was `View_Control` and that was wrong.** `prev/next_track`
                        # moves Live's *selected track* one at a time and never touches the
                        # session ring, so the eight strips stayed put while the selection
                        # crawled — and because Solo/Mute follow the target (selected) track,
                        # they followed the crawl too. One wrong component, three symptoms.
                        #
                        # `Session_Navigation`'s **page** buttons move the ring by a whole
                        # bank, which is what "next eight strips" means. Its plain
                        # `left_button`/`right_button` scroll by one, which is the behaviour
                        # we just removed.
                        "component": "Session_Navigation",
                        "page_left_button": "left_button",
                        "page_right_button": "right_button",
                    },
                ]
            },
        },

        # Mix mode's two pages. A **modes component**, because the eight encoders have to
        # rebind between them and only a layer swap can do that.
        #
        # ⚠️ `"enable": False` is load-bearing. A modes component is enabled by default —
        # `_setup_modes_component` ends with `set_enabled(modes_config.pop("enable", True))` —
        # and an always-on page layer would hold the encoders in Song and Plugin mode too. Mix
        # mode enables it by naming it as a mode part.
        #
        # The **first** mode listed is the default: `_setup_modes_component` assigns
        # `selected_mode = modes[0]` when none is set, so Mix mode opens on Volume.
        "Mix_Pages": {
            "enable": False,

            # Volume: Template 2's faders — Mix mode's own strip view.
            "volume": {
                "modes": [
                    {
                        "component": "Mixer",
                        "volume_controls": "encoders",
                    },
                ]
            },

            # Sends: the eight encoders as a (track x send) grid — columns are tracks, rows are
            # sends, so encoder 1 and encoder 5 are send A and B of the same track. Ours rather
            # than `Mixer.send_controls`, because the framework maps `controls[x]` onto
            # `_channel_strips[x]` and a four-wide matrix would leave half the ring unreachable.
            # See `sends.py`.
            #
            # ⚠️ **One mode, several wheel steps.** The number of Sends pages depends on the
            # set — tracks x return tracks — and a `ModesComponent`'s mode list is fixed at
            # mapping time. So `mixpages.py` expands this one mode into as many steps as the
            # set needs.
            "sends": {
                "modes": [
                    {
                        "component": "Motion_Sends",
                        "send_controls": "encoders",
                    },
                ]
            },

            # Pan: Template 0's eight arcs. Template 2 has **no pan element at all**, so this
            # page borrows the encoder-tile view — an arc reads a pan far better than a number,
            # and it is the same renderer Plugin mode uses with different content.
            "pan": {
                "modes": [
                    {
                        "component": "Mixer",
                        "pan_controls": "encoders",
                    },
                ]
            },
        },
    }
