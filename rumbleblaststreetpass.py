# Performs inputs for the pokemon rumble blast streetpass invite a customer, start the script before the up input is needed, repeats 30 times for 300 coins

import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()

def press_button(button):
    gamepad.press_button(button)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button)
    gamepad.update()
    time.sleep(0.5)

def press_button_a():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

def press_button_up():
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

press_button_a()
time.sleep(10)
for i in range(30):
    print("go")
    press_button_up()
    time.sleep(0.5)
    for i in range(25):
        press_button_a()
        print(i)
    print("stop")