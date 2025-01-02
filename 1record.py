import inputs
import time

found = False
start_time = None
inputstack = []

while True:
    try:
        events = inputs.get_gamepad()
        if not found:
            print("Gamepad found!")
            found = True
    except inputs.UnpluggedError:
        print("Error getting gamepad, trying again in 1 second")
        time.sleep(1)
        found = False
        continue
    for event in events:
        if event.ev_type == "Absolute" or event.ev_type == "Key":
            if event.code == "ABS_Z":
                if event.state == 255:
                    start_time = time.time()
                    print("Start time:", start_time)
            if event.code == "ABS_RZ":
                if event.state == 255:
                    start_time = None
                    with open("inputstack.txt", "w") as f:
                        for item in inputstack:
                            f.write("%s,%s,%s,%s\n" % item)
                        inputstack = []
                        print("End time:", time.time())
    if start_time is not None:
        elapsed_time = time.time() - start_time
        inputstack.append((elapsed_time, event.ev_type, event.code, event.state))
        print(f"Code: {event.code}, Event: {event.ev_type}, State: {event.state}, Elapsed Time: {elapsed_time}")




