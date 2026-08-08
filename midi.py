"""Motion 32 native-protocol constants.

All integer tuples are ready to pass to ControlSurface.send_midi().
"""

# Native host-mode lifecycle
NATIVE_MODE_ON_MESSAGE = (0x8F, 0x00, 0x7F)
NATIVE_MODE_OFF_MESSAGE = (0x8F, 0x00, 0x00)
IDENTITY_REQUEST_MESSAGE = (0xF0, 0x7E, 0x7F, 0x06, 0x01, 0xF7)

# Fender / Motion SysEx
SYSEX_START = 0xF0
SYSEX_END = 0xF7
FENDER_MANUFACTURER_ID = 0x08
MOTION_32_DEVICE_ID = 0x26
MOTION_SYSEX_HEADER = (SYSEX_START, FENDER_MANUFACTURER_ID, MOTION_32_DEVICE_ID)

MSG_SCREEN_TEMPLATE = 0x20
MSG_SCREEN_UPDATE = 0x21
MSG_GLOBAL_SETTINGS_STATE = 0x22

GLOBAL_SETTINGS_CLOSED = 0x00
GLOBAL_SETTINGS_OPEN = 0x01

REQUIRED_FIRMWARE_VERSION = 1003

# Integrated-mode controls (CC, MIDI channel 1 / zero-based channel 0)
MIDI_CHANNEL = 0

CC_SHIFT = 0x1F

# Encoders 1-8: relative, sign-magnitude with the sign bit at 0x40 (NOT two's
# complement) -> framework MapMode.LinearSignedBit.
CC_ENCODERS = tuple(range(0x0E, 0x16))  # 0x0E-0x15
# Capacitive touch, one per encoder. NOTE: these same CCs are touch-strip-2 LED
# addresses in the host->device direction. Direction disambiguates; see
# Motion32_Control_Surface_Definition.md §2.5.
CC_ENCODER_TOUCH = tuple(range(0x70, 0x78))  # 0x70-0x77

# Encoder halo LEDs have no address of their own — they are written at the
# encoder's own CC.
CC_ENCODER_HALO = CC_ENCODERS

# Screen wheel (relative) and its push button.
CC_WHEEL = 0x1D
CC_WHEEL_PUSH = 0x78

# LCD soft buttons 1-8.
CC_LCD_BUTTONS = tuple(range(0x24, 0x2C))  # 0x24-0x2B

# Bank buttons A-H.
CC_BANK_BUTTONS = tuple(range(0x00, 0x08))

# Navigation — deliberately non-contiguous on this device.
CC_NAV_UP = 0x57
CC_NAV_DOWN = 0x59
CC_NAV_LEFT = 0x5A
CC_NAV_RIGHT = 0x66

# Control-focus buttons.
CC_SONG = 0x46
CC_PLUGIN = 0x47
CC_EDIT = 0x48
CC_MIX = 0x49

# Screen-mode buttons.
CC_ADD = 0x20
CC_SCALE = 0x21
CC_CHORD = 0x22
CC_CONTROL = 0x23

CC_SOLO = 0x4A
CC_MUTE = 0x4B
CC_PRESET_UP = 0x2C
CC_PRESET_DOWN = 0x2D
CC_OCTAVE_UP = 0x40
CC_OCTAVE_DOWN = 0x41
CC_FINE = 0x42  # physically labelled "16"
CC_FIXED = 0x43
CC_PADS = 0x44
CC_LAUNCH = 0x45

# Touch-strip buttons. Same addresses carry the strip LED-bar mode host->device.
CC_TOUCHSTRIP_1_BUTTON = 0x7A
CC_TOUCHSTRIP_2_BUTTON = 0x7B

# Touch-strip LEDs, 9 per strip. Colour-only addresses — the Studio Pro shutdown capture
# resets these on channels 2/3/4 with no channel-1 state byte.
CC_TOUCHSTRIP_1_LEDS = tuple(range(0x37, 0x40))  # 0x37-0x3F
CC_TOUCHSTRIP_2_LEDS = tuple(range(0x70, 0x79))  # 0x70-0x78 (overlaps encoder touch / wheel push)

# Transport — NATIVE-MODE values, CONFIRMED by the official Studio Pro capture (DAW Mode Off):
# pressing Stop/Tap/Record/Play produced From-device CC 0x6F/0x69/0x6B/0x6D respectively, matching
# surface.xml. NOTE: if OUR script instead sees 0x66-0x69 for these buttons, the device has NOT
# fully entered native mode (an incomplete identity handshake) — fix the handshake, don't remap.
CC_TAP = 0x69
CC_RECORD = 0x6B
CC_PLAY = 0x6D
CC_STOP = 0x6F

# Button feedback values (status 0xB0). Three brightnesses; the factory rests an
# "inactive but present" button at DIM rather than OFF.
LED_OFF = 0x00
LED_DIM = 0x3F
LED_ON = 0x7F

# ⚠️ PAD state values (status 0x90) are a DIFFERENT vocabulary — Off / On / Blink / Pulse.
# There is **no dim state for a pad**: `LED_DIM` (63) is not in this set, and sending it
# lights nothing at all. That mistake left the entire keybed dark on its first hardware run.
# Pad brightness comes from the RGB triple instead, which is why the factory updates a lit
# pad with colour-only writes. See Motion32_Implementation_Notes.md §6b-19.
LED_BLINK = 0x01
LED_PULSE = 0x02
#: The complete set a pad's state byte accepts.
PAD_STATES = (LED_OFF, LED_BLINK, LED_PULSE, LED_ON)

# Screen element attributes
ATTR_TEXT = 0x00  # ASCII bytes
ATTR_COLOR = 0x01  # R G B, 7-bit each
ATTR_VALUE = 0x02  # normalized x 127
ATTR_VISIBLE = 0x03  # 0 hidden / 1 shown
ATTR_FONT = 0x04  # 0 regular / 1 bold

# Every LED address we may have lit, for the teardown reset. Studio Pro resets all LEDs and
# the screen *before* sending the native-mode goodbye; matching that stops the device sitting
# there with stale colours after Live unloads us.
#
# Address list corroborated by a MIDI capture of a Studio Pro shutdown, which also covers the
# touch-strip LED ranges, the wheel and the wheel-push address.
LED_ADDRESSES_TO_CLEAR = (
    CC_ENCODERS
    + CC_LCD_BUTTONS
    + CC_BANK_BUTTONS
    + CC_TOUCHSTRIP_1_LEDS
    + CC_TOUCHSTRIP_2_LEDS
    + (
        CC_TOUCHSTRIP_1_BUTTON,
        CC_TOUCHSTRIP_2_BUTTON,
        CC_SHIFT,
        CC_ADD,
        CC_SCALE,
        CC_CHORD,
        CC_CONTROL,
        CC_SONG,
        CC_PLUGIN,
        CC_EDIT,
        CC_MIX,
        CC_SOLO,
        CC_MUTE,
        CC_PRESET_UP,
        CC_PRESET_DOWN,
        CC_OCTAVE_UP,
        CC_OCTAVE_DOWN,
        CC_FINE,
        CC_FIXED,
        CC_PADS,
        CC_LAUNCH,
        CC_NAV_UP,
        CC_NAV_DOWN,
        CC_NAV_LEFT,
        CC_NAV_RIGHT,
        CC_TAP,
        CC_RECORD,
        CC_PLAY,
        CC_STOP,
        CC_WHEEL,
    )
)

# Pad LED addresses (both lanes). Colour writes use 0x91/0x92/0x93.
PAD_NOTES = tuple(range(36, 68))

# Values the factory host sends when releasing the device. NOT black-and-hidden: state goes
# off but the colour goes to full **white**, and screen elements are left empty-but-visible.
# Blanking to black and visible=0 corrupts the device's own standalone UI, which reuses the
# same screen elements — that is what left the Motion dark after unload.
RESET_LED_STATE = 0x00
RESET_RGB = 0x7F
RESET_COLOR = (0x7F, 0x7F, 0x7F)
RESET_VISIBLE = 1
RESET_FONT = 0
RESET_VALUE = 0

# Status bytes for the three RGB component messages.
STATUS_CC = 0xB0
STATUS_CC_RED = 0xB1
STATUS_CC_GREEN = 0xB2
STATUS_CC_BLUE = 0xB3
STATUS_NOTE = 0x90
STATUS_NOTE_RED = 0x91
STATUS_NOTE_GREEN = 0x92
STATUS_NOTE_BLUE = 0x93
