# -*- coding: utf-8 -*-
"""
==============================================================================
ble_helper.py:
calls external files/functions based on calls

[MicroPython ESP32]
==============================================================================
Usages:
used by midi_bluetooth.py
called on data: 0
reset_LEDs()
called on data: 1-20, Midi File Number
play_midi_raindrop(file_id=1)
called on data: A
display_msg(msg="Hello!")


@author: Jit_Sharma@gmail.com
------------------------------------------------------------------------------
- Version History:
    * {v# [date] user: comments}
    * v1 [8-Feb-25] Jit Sharma: First version
    * v2 [d-Mon-25] Jit Sharma: 2nd version
    
Last Updated: 9-Feb-25
==============================================================================

"""
import time
# import led_matrix_piano_keys_w6b3 as midi_raindrop
import led_display as midi_raindrop
#import msg_display
#import anim_display
import neopixel_reset as np_reset
import esp32_util as u

def set_brightness(brightness=100):
    print("set_brightness Function  called")
    midi_raindrop.set_brightness(brightness)
    time.sleep(1)
    print("set_brightness Function ended")


def reset_LEDs():
    print("Function Reset LEDs called")
    np_reset.main("Reset called from Bluetooth service")
    time.sleep(1)
    print("Function Reset LEDs ended")


def play_midi_raindrop(file_id=1):
    print(f"{__name__}, Playing MIDI file = {file_id} in 3 seconds")
    time.sleep(1)
    print("2 sec")
    time.sleep(1)
    print("1 sec")
    #time.sleep(1)
    midi_raindrop.main(name="There", midi_file_id=file_id)
    print(f"{__name__} ended")
    
def display_msg(msg = "Hello!", mode=0):
    print(f"display_msg Function called")
    # call here
    msg_display.main(msg = msg, mode=mode)
    print(f"display_msg ended")    

def display_anim():
    print(f"display_animation Function called")
    # call here
    anim.main(name="Welcome Animation", midi_file_id=20, play_msg=False)
    # msg_display.main("SmartPiano", mode=mode)
    print(f"display_animation ended")


def display_welcome_anim(msg = "Hello!", mode=0):
    print(f"Display Welcome Animation Function called")
    # call here
    anim_display.display(mode=mode)
    print(f"display_msg ended")

def main(name):
    file_id = 1
    # play_midi_raindrop(file_id)
    reset_LEDs()
    
    
if __name__ == '__main__':
    #print (f"{__filename__} is being run directly") 
    main("Midi Piano  Helper")
    