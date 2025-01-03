import vgamepad as vg
from pynput.keyboard import Key

pynputKeyToInternalCodeMap = {
    str(Key.left): "left",
    str(Key.right): "right",
    str(Key.up): "up",
    str(Key.down): "down",
    "<102>": "A",
    "<98>": "B",
    "<104>": "X",
    "<100>": "Y",
    str(Key.shift_r): "start"
}

controllerToInternalCodeMap = {
    "BTN_SOUTH": "A",
    "BTN_EAST": "B",
    "BTN_NORTH": "X",
    "BTN_WEST": "Y",
    "BTN_SELECT": "start"
}

internalCodeToVgamepadMap = {
    "left": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    "right": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    "up": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    "down": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    "A": vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    "B": vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    "X": vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    "Y": vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
    "start": vg.XUSB_BUTTON.XUSB_GAMEPAD_START
}