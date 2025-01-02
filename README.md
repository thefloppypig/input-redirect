# 3DS gamepad remote playback

Capture and playback gamepad inputs

Use modded 3ds input redirection for recording and playback.
Use controller emulator to record inputs from keyboard.
Since 3ds input redirection is using a network connection, the input timings will not be 100% consistent.

Running `python 1record.py` will record inputs and save them to inputstack.txt. Start recording by pressing Z on the controller and stop by pressing RZ.

Running `python 2playback.py \<file-name\>` will playback inputs from that file when F10 is pressed, cancel by pressing F10 again. The sequence can be repeating by pressing F10 again after it is complete or cancelled.

Not all buttons are implemented, just basic ABXY, dpad and joysticks