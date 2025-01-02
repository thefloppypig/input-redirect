
import time
import vgamepad as vg

gamepad = vg.VX360Gamepad()
joystickLeft = {
    "x": 0,
    "y": 0
}
joystickRight = {
    "x": 0,
    "y": 0
}
dpad = {
    "up": 0,
    "right": 0,
    "down": 0,
    "left": 0
}
def setup():
    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    gamepad.update()
    time.sleep(0.1)

def inputToVgamepad(key, value):
    match key:
        case "BTN_SOUTH":
            _updateButton(vg.XUSB_BUTTON.XUSB_GAMEPAD_A, value)
        case "BTN_EAST":
            _updateButton(vg.XUSB_BUTTON.XUSB_GAMEPAD_B, value)
        case "BTN_NORTH":
            _updateButton(vg.XUSB_BUTTON.XUSB_GAMEPAD_X, value)
        case "BTN_WEST":
            _updateButton(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y, value)
        case "BTN_SELECT":
            _updateButton(vg.XUSB_BUTTON.XUSB_GAMEPAD_START, value)
        case "ABS_HAT0Y":
            _updateDpadY(value)
        case "ABS_HAT0X":
            _updateDpadX(value)
        case "ABS_X":
            _updateLeftJoystick("x", value)
        case "ABS_Y":
            _updateLeftJoystick("y", value)
        case "ABS_RX":
            _updateRightJoystick("x", value)
        case "ABS_RY":
            _updateRightJoystick("y", value)
        case "SYN_REPORT":
            gamepad.update()
        case _:
            print("Unknown key: " + key)

def _updateButton(button, value):
    if (value == 1):
        gamepad.press_button(button)
    else:
        gamepad.release_button(button)

def _updateDpadY(value):
    if (value == -1):
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        dpad["up"] = 1
    elif (value == 1):
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        dpad["down"] = 1
    else:
        if (dpad["up"] == 1):
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        if (dpad["down"] == 1):
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        dpad["up"] = 0
        dpad["down"] = 0

def _updateDpadX(value):
    if (value == 1):
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        dpad["right"] = 1
    elif (value == -1):
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        dpad["left"] = 1
    else:
        if (dpad["right"] == 1):
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        if (dpad["left"] == 1):
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        dpad["right"] = 0
        dpad["left"] = 0


def _updateLeftJoystick(axis, value):
    joystickLeft[axis] = value
    gamepad.left_joystick(joystickLeft["x"], joystickLeft["y"])

def _updateRightJoystick(axis, value):
    joystickRight[axis] = value
    gamepad.right_joystick(joystickRight["x"], joystickRight["y"])

def cleanup():
    gamepad.reset()
    gamepad.update()
    time.sleep(0.1)