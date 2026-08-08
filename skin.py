"""Motion 32 LED skin — colors + brightness per the Studio One source and the agreed spec.

⚠️ **A missing skin key does not raise. It silently becomes a `BasicColors`.** From
`skin.pyc.Skin.__getitem__`:

```python
if key not in self.colors:
    if key.lower().endswith(ON_SUFFIXES):   # ('enabled', 'on', 'pressed', 'selected')
        return BasicColors.ON
    return BasicColors.OFF
```

A `BasicColors` carries a state byte and **no RGB triple**, so on this device it renders
colourless: `OFF` writes state 0 and the button goes dark, `ON` writes state 127 over whatever RGB
the last mode happened to leave there. That is why `ViewControl`, `Device` and `Session` are
declared here — none of them have a usable framework default.

**Note the asymmetry, because it is what makes this hard to spot:** a key ending in `On`/`Pressed`
still lights (wrong colour), while its `Off`/rest partner goes *dark*. So the symptom is "the
button only works when I press it", not "the button is broken".

**How to find the keys a component wants:** decompile its `.pyc` and read the skin strings out of
the constants. Most are literals (`'Session.Navigation'`, `'UndoRedo.Undo'`). Two are **built at
runtime and can never be scraped**, so they are recorded here:

    ModifierBackgroundComponent._setup_control_state:
        base = self.name.title().replace("_", "")   -> "ModifierBackground"
        ctrl = name.title().replace("_", "")        -> "Shift"
        color = "{}.{}"  pressed_color = "{}.{}Pressed"
    ScrollComponent:
        pressed key = "{}Pressed".format(scroll_skin_name)

`tests/test_screen.py` now checks both halves — that every skin namespace a bound component
references exists here, and that every LED-bearing control we map has its exact keys.

**One key is deliberately absent.** `Mixer.ImplicitArmOn` is wrapped in an `OptionalSkinEntry`
with `fallback_name='Mixer.ArmOn'`, and `Skin._from_wrapper` follows the fallback when the
preferred name is undeclared. So an implicitly-armed track already gets our red. Declaring it
would only be to give implicit arm a *different* colour from explicit arm, which we do not want.

  Play   : dim green at rest -> full green when playing
  Record : dim red at rest   -> full red when armed
  Stop   : steady orange (lit always), flashes white when pressed
  Tap    : steady blue (full), flashes white when tapped
  Shift  : magenta while held

`Flash` is the pressed_color used by momentary buttons. Play color is a choice (green, DAW
convention); the source's generic default is blue — change Transport.Play* to Rgb.BLUE* if preferred.
"""

from .colors import Rgb


class Skin:
    class DefaultButton:
        On = Rgb.WHITE
        Off = Rgb.OFF
        Disabled = Rgb.OFF

    class ModifierBackground:
        """Shift. ⚠️ The keys are `ModifierBackground.Shift` / `…ShiftPressed`.

        This class used to be called `Modifier`, with `On` / `Off` — a name nothing in the
        framework ever asks for, so Shift resolved to `BasicColors.OFF` at rest (dark) and
        `BasicColors.ON` while held (state-only, wearing whatever RGB was last on that
        address). It looked like a working momentary light and was neither of its colours.

        `ModifierBackgroundComponent` derives the keys from its own component name and the
        mapped control name — see the module docstring. `Modifier_Background` → `Shift` is the
        only pair we bind.
        """

        Shift = Rgb.PURPLE
        ShiftPressed = Rgb.WHITE

    class Scale:
        """Scale mode's soft buttons (Phase 10). Ours — no framework component asks for these.

        The three category buttons are a radio, so they follow the A-H model: dim blue at rest,
        dim white for the selected one, full white while held. `Guide` / `Locked` is a **single**
        button with two faces, so its two colours are two *states* rather than on/off.
        """

        CategoryOff = Rgb.BLUE_DIM
        CategoryOn = Rgb.WHITE_DIM
        # Locked is the default and the safe state, so it wears the resting blue; Guide is the
        # one that opens the keybed up, and reads as "something is different".
        Locked = Rgb.BLUE
        Guide = Rgb.YELLOW
        # The Control button: lit only as a way out, so a plain available-blue.
        Return = Rgb.BLUE

    class Session:
        """Mix mode's Left/Right — they page the session ring by eight.

        `SessionNavigationComponent` composes `ScrollComponent`s with the skin base
        `'Session.Navigation'`, and `ScrollComponent` derives the pressed key as
        `'{}Pressed'`. Neither was declared before 2026-08-03, so both buttons resolved to
        `BasicColors` and **went dark the moment Mix mode was entered**.

        Blue = available / white = pressed, matching `ViewControl` and `Device.Navigation`, so
        the four nav keys read the same in every mode even though three different components
        own them.
        """

        Navigation = Rgb.BLUE
        NavigationPressed = Rgb.WHITE

    class UndoRedo:
        """Shift+Stop. Only Undo is mapped; Redo is declared so the pair cannot drift.

        Blue while Shift is held, matching the other three Shift combos — the shift layer
        recolours all four transport keys to their modified meaning, which is what tells you
        the layer is live.
        """

        Undo = Rgb.BLUE
        UndoPressed = Rgb.WHITE
        Redo = Rgb.BLUE
        RedoPressed = Rgb.WHITE

    class Transport:
        # Key names must match what the framework's TransportComponent asks for, otherwise
        # they silently fall back to the framework default skin (create_skin merges ours
        # over it). The full list of keys it requests is in
        # Motion32_Implementation_Notes.md §6b.
        Flash = Rgb.WHITE          # pressed_color for our record button

        PlayOn = Rgb.GREEN
        PlayOff = Rgb.GREEN_DIM
        RecordOn = Rgb.RED         # our own record_button (see transport.py)
        RecordOff = Rgb.RED_DIM

        StopOn = Rgb.ORANGE        # steady orange...
        StopOff = Rgb.ORANGE       # ...in both states: Stop is always available
        StopPressed = Rgb.WHITE    # white flash on press

        TapTempo = Rgb.BLUE        # steady, full
        TapTempoPressed = Rgb.WHITE

        # **Yellow when looping, to match Live's own loop brace** (user, 2026-08-03). Blue at
        # rest = "this control is live". Both keys are shared by two controls — the framework's
        # `loop_button` on Shift+Play and our `loop_toggle_button` on soft button 3 — which is
        # deliberate: one loop state, one colour, wherever you read it.
        LoopOn = Rgb.YELLOW
        LoopOff = Rgb.BLUE

        # Ours (no framework control exists for it). Lit white when Live has session playback
        # overriding the arrangement, i.e. when there is something to go back to.
        BackToArrangementOn = Rgb.WHITE
        BackToArrangementOff = Rgb.BLUE
        # Shift+Tap. **Yellow when the metronome is on, dark when off** (user, 2026-08-03) —
        # the same yellow as Loop, because both are "Live is doing this to your timing".
        # Dark rather than blue at rest: the metronome is a state you want to *notice*, and a
        # resting blue on a key you only reach through Shift says nothing useful.
        MetronomeOn = Rgb.YELLOW
        MetronomeOff = Rgb.OFF

        CanCaptureMidi = Rgb.WHITE

        # Soft buttons under the screen: blue at rest so they read as live controls,
        # white when pressed / when the state they report is active.
        SetCue = Rgb.BLUE
        SetCuePressed = Rgb.WHITE
        CanReEnableAutomation = Rgb.BLUE

    class ViewToggle:
        # Blue = available, white = that view is currently showing.
        SessionOn = Rgb.WHITE
        SessionOff = Rgb.BLUE
        BrowserOn = Rgb.WHITE
        BrowserOff = Rgb.BLUE
        DetailOn = Rgb.WHITE
        DetailOff = Rgb.BLUE
        ClipOn = Rgb.WHITE
        ClipOff = Rgb.BLUE

    class ViewControl:
        # **Why the directional keys were dark.** The framework default for these is
        # `BasicColors.ON`, which carries only the state byte and no RGB triple — and a
        # state-only colour renders colourless on the Motion (notes §3). Any framework
        # component whose skin defaults to BasicColors needs a ComplexColor here or its
        # buttons simply never light.
        Track = Rgb.BLUE
        TrackPressed = Rgb.WHITE
        Scene = Rgb.BLUE
        ScenePressed = Rgb.WHITE

    class Device:
        # Same reason as ViewControl: the framework defaults are BasicColors.
        On = Rgb.BLUE
        Off = Rgb.OFF
        FoldOn = Rgb.BLUE
        FoldOff = Rgb.OFF
        LockOn = Rgb.WHITE
        LockOff = Rgb.BLUE
        Navigation = Rgb.BLUE          # Preset Up/Down: step through the device chain
        NavigationPressed = Rgb.WHITE

        class Bank:
            Selected = Rgb.WHITE
            NotSelected = Rgb.BLUE
            Navigation = Rgb.BLUE      # Up/Down in Plugin mode: parameter bank
            NavigationPressed = Rgb.WHITE

    class Keyboard:
        # The factory octave model, decoded from a Studio Pro capture (2026-07-26). The state
        # byte and the RGB carry **different** meanings and must not be conflated:
        #
        #   state byte  press feedback — 63 at rest, 127 while physically held
        #   RGB         this direction's engagement — blue at rest, white when engaged
        #
        # The proof is that pressing Octave *Down* rewrote *Up*'s RGB back to blue, because the
        # offset had returned to 0; Down's own press only changed its state byte and left its
        # colour alone. So both buttons read one shared value, each showing its own direction.
        #
        # `Octave` is `color`, `OctaveShifted` is `on_color`, and `keyboard.py` flips `is_on`.
        Octave = Rgb.BLUE_DIM
        OctaveShifted = Rgb.WHITE_DIM
        # One deliberate divergence: the factory holds the hue on press and only brightens, so
        # a *disengaged* button pressed would flash full blue. ButtonControl has a single
        # `pressed_color`, and white is the right choice for the other three cases, so a
        # disengaged press flashes white for ~100 ms instead. Momentary and cosmetic.
        OctavePressed = Rgb.WHITE

        # A-H pad banks. Same two-channel model as Octave — state byte for press, RGB for
        # state — but a **radio** rather than two directional readouts, so exactly one is
        # white at any time and the other seven sit dim blue.
        #
        # Dim blue / dim white rather than the `Device.Bank` blue / full white used for
        # parameter banks: A-H sits in the pad block next to Octave, and a full-brightness
        # button there would out-shout the keybed it is describing. Brightness stays reserved
        # for "you are physically holding this".
        Bank = Rgb.BLUE_DIM
        BankSelected = Rgb.WHITE_DIM
        BankPressed = Rgb.WHITE

    class Mixer:
        # Factory colour: solo yellow (kChannelSolo).
        SoloOn = Rgb.YELLOW
        SoloOff = Rgb.BLUE

        # **Mute follows Live's Track Activator, not the factory** (user, 2026-08-03): yellow
        # while the track is *playing*, red while it is muted.
        #
        # ⚠️ **`MuteOn` means "the track is muted", not "the button is active".** Verified in
        # `channel_strip.pyc`:
        #     self.mute_button.is_on = self._track.mute or self._track.muted_via_solo
        # so `MuteOn` is the muted state and `MuteOff` is the audible one. Reading it the
        # other way round inverts the whole control, which is why it is written down here.
        #
        # ⚠️ This puts Mute-audible and Solo-engaged on the same yellow. They sit on adjacent
        # keys and mean different things; if that reads badly on the hardware, move Solo to
        # Live's own solo blue rather than moving Mute — Mute is the one matching Live.
        MuteOn = Rgb.RED
        MuteOff = Rgb.YELLOW
        # Arm sits on the eight LCD soft buttons in Mix mode. **Red when armed, dark when
        # not** (user, 2026-07-29) — unlike Solo/Mute, which sit on dedicated buttons where a
        # resting blue reads as "this control is live". A row of eight blue lights over the
        # screen would compete with the strips underneath, and "armed" is the only state
        # worth seeing at a glance.
        #
        # The LED is driven from Live: `MixerComponent._update_arm_button` listens to the
        # track's own `arm`, so arming with the mouse lights the button too. Nothing here is
        # a script-side toggle.
        ArmOn = Rgb.RED
        ArmOff = Rgb.OFF
