

from pynput.keyboard import Key, Listener, KeyCode
import time
import vgamepad as vg
from floppyconfig import pynputKeyToInternalCodeMap
import sys

start_time = None
inputstack = []
keys_pressed = set()  

emulate = not (len(sys.argv) > 1 and sys.argv[1] == '-n')
print(f"Emulate Controller: {emulate}")
if __name__ == '__main__':
    try:
        if emulate:
            import floppygamepad
            floppygamepad.setup()
            floppygamepad.cleanup()

        def on_press(key):
            global start_time
            global inputstack
            if key not in keys_pressed:
                keys_pressed.add(key)
            else:
                return

            if key == Key.esc:
                # Stop listener
                return False
            elif key == Key.f7:
                start_time = time.time()
                print("Start recording")
            elif key == Key.f8:
                start_time = None
                if len(inputstack) > 0:
                    prevtime = 0
                    with open("inputstack.txt", "w") as f:
                        for item in inputstack:
                            deltatime = item[0] - prevtime
                            prevtime = item[0]
                            f.write(f"{deltatime} {item[1]} {item[2]}\n")
                    inputstack = []
                    print("End recording")
            elif str(key) in pynputKeyToInternalCodeMap:
                internalKey = pynputKeyToInternalCodeMap[str(key)]
                if emulate:
                    floppygamepad.internalInputToVgamepad(key=internalKey, value=1)
                if start_time is not None:
                    elapsed_time = time.time() - start_time
                    print(f'{elapsed_time} {internalKey} pressed')
                    inputstack.append((elapsed_time, internalKey, 1))

        def on_release(key):
            global start_time
            global inputstack
            try:
                keys_pressed.remove(key)
            except KeyError:
                pass  # started with key pressed?
            if str(key) in pynputKeyToInternalCodeMap:
                internalKey = pynputKeyToInternalCodeMap[str(key)]
                if emulate:
                    floppygamepad.internalInputToVgamepad(key=internalKey, value=0)
                if start_time is not None :
                    elapsed_time = time.time() - start_time
                    print(f'{elapsed_time} {internalKey} released')
                    inputstack.append((elapsed_time, internalKey, 0))

        # Collect events until released
        with Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
    except Exception:
        floppygamepad.cleanup()