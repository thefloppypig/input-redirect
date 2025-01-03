
if __name__ == '__main__':    
    import sys
    import time
    import keyboard
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
                [float(line.strip().split(" ")[0])] +
                line.strip().split(" ")[1:2] +
                [int(line.strip().split(" ")[2])]
                for line in f.readlines()
            ]
            return input_stack
        
    def playback():
        floppygamepad.cleanup()
        input_stack = parse_input_stack()
        for entry in input_stack:
            delta_time = float(entry[0])
            if delta_time > 0: time.sleep(delta_time)
            if cancel: 
                floppygamepad.cleanup()
                break
            print(entry)
            floppygamepad.internalInputToVgamepad(key=entry[1], value=entry[2])
            
        print("Done")

    print(f"Press {start_key} to start playback")
    while True:
        if keyboard.is_pressed(start_key):
            print("Starting playback")
            cancel = False
            t = threading.Thread(target=playback,daemon=True)
            t.start()
            time.sleep(1)
            while t.is_alive():
                if keyboard.is_pressed(start_key):
                    print("Cancel")
                    cancel = True
                    t.join()
                    cancel = False
                    time.sleep(1)
                time.sleep(0.01)
        else:
            time.sleep(0.01) # Wait for f10 to be pressed

