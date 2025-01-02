
import sys
import time
import keyboard
import vgamepad as vg
import floppygamepad
import threading

if len(sys.argv) != 2:
    print("Usage: python3 2playback.py <input stack file>")
    exit()

floppygamepad.setup()


start_key = 'f10'
cancel = False

def parse_input_stack():
    with open(sys.argv[1], "r") as f:
        input_stack = [
            [float(line.strip().split(",")[0])] +
            line.strip().split(",")[1:3] +
            [int(line.strip().split(",")[3])]
            for line in f.readlines()
        ]
        return input_stack
    
def playback():
    prev_time = 0
    floppygamepad.cleanup()
    input_stack = parse_input_stack()
    for entry in input_stack:
        elapsed_time = float(entry[0])
        delta_time = elapsed_time - prev_time
        prev_time = elapsed_time
        print(entry)
        floppygamepad.inputToVgamepad(key=entry[2], value=entry[3])
        if delta_time > 0: time.sleep(delta_time)
        if cancel: 
            floppygamepad.cleanup()
            break
    print("Done")

print(f"Press {start_key} to start playback")
while True:
    if keyboard.is_pressed(start_key):
        print("Starting playback")
        cancel = False
        t = threading.Thread(target=playback,daemon=True)
        t.start()
        time.sleep(2)
        while t.is_alive():
            if keyboard.is_pressed(start_key):
                print("Cancel")
                cancel = True
                t.join()
                cancel = False
        time.sleep(2)
    else:
        time.sleep(0.1) # Wait for f10 to be pressed

