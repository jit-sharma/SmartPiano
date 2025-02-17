# -*- coding: utf-8 -*-
"""
==============================================================================
led_matrix_piano_keys_w6b3.py:
MIDI to 8x32 LED Matrix display along with Piano key 6,3 White/Black LED

Displays MIDI bitmap data in raindrop style
+ 1 keyboard row added to the display, 6 LED in White an3 3 in Black Keys for 32 keys
Usages bitmap file csv/txt, config.json,
Python files:
esp32_colors.py: Colors and Color palette
midi_data.py: Reads midi Bitmap data, based on config.json
daisy9x32.py: for LED address of daisy chained 8x32 display
esp32_util.py: esp32 util functions
piano_keys_led.py: for getting LED sequence numbers for 32 White and Black keys
matrix_util.py Matrix utility functions
ascii_matrix.py ASCII datamap


==============================================================================
Usages:
Call main function with midi_file_id number and name of user
set print level to _INFO for less output, _DEBUG for debugging

@author: Jit_Sharma@gmail.com
------------------------------------------------------------------------------
- Version History:
    * {v# [date] user: comments}
    * v1 [07-Feb-25] Jit Sharma: First version
    * v3 [09-feb-25] Jit Sharma: Clean up

Last Updated: 11-Feb-25
=====
"""
import machine
from machine import Pin
from neopixel import NeoPixel

""" standard """
import time
import json

""" Program other files """
import esp32_colors as color
import esp32_util as u
import midi_data as midi_file
import daisy_chained as dc
import piano_keys_led as pk
import matrix_util as mu
import ascii_matrix as am
import msg_display as m

text_storm_delay = 100 # ms
text_scroll_delay = 50  # 50 ms
frame_delay = 250  # 1/8 sec/ 250 ms

matrix_rows = 8
matrix_cols = int(u.get_matrix_panel_width())
dcdf = dc.get_dcdf(matrix_cols)

_DEBUG = 0
_INFO = 1
_WARNING = 2
_ERROR = 3
print_level = _INFO  # _DEBUG # _INFO # _WARNING # _ERROR
esp32 = True  # False #True
file_name = "LED_display"



start_ms = time.ticks_ms()

BRIGHTNESS = u.get_brightness()  # 10 # in percentage, maximum 100


def set_brightness(b=100):
    global BRIGHTNESS
    BRIGHTNESS = u.update_brightness(b)  # u.get_brightness()


def ms():
    return time.ticks_ms()


def mstr(start=0):
    return u.mstr(start)


def ts():
    return u.ts()


def shift_row(matrix, row):
    return mu.shift_row(matrix, row)


def clear(np):
    return mu.clear(np)


def wipe(np):
    return mu.wipe(np)


def display_matrix(_df, np, pk_led_seq=None, esp32=False, disp_color=None, brightness=100):
    return mu.display_matrix(_df, np, esp32=False, disp_color=disp_color,
                                  brightness=brightness)


def display_mat(_df, np, pk_led_seq, disp_color=color.NAVY_BLUE, brightness=100, color_palette=None):
    mu.display_matrix_keys(_df, np, pk_led_seq=pk_led_seq, esp32=True, disp_color=disp_color,
                                  brightness=brightness, color_palette=color_palette)


# Print midi row with separator as pipe every octave of 12 keys notes
def print_midi_row(row):
    mu.print_midi_row(row)


def main(midi_file_id=1):
    try:
        PLAY_MIDI_RAINDROP = True
        print(f'{ts()} Hi, There')
        led = machine.Pin(2, machine.Pin.OUT)
        led.value(1)
        time.sleep(1)
        led.value(0)

        np = NeoPixel(machine.Pin(16), matrix_rows * matrix_cols + 152)
        np[0] = color.RED  # set the first pixel to RED
        np.write()  # write data to all pixels

        # Midi Data
        midi_data, midi_filename, start_note, cp, _ = midi_file.get_midi_data_ext(midi_file_id)
        if len(midi_data[0]) > matrix_cols:
            midi_data = mu.get_col_slice(midi_data,0,matrix_cols)
        #if len(midi_filename) > 7:
        #    midi_filename = midi_filename[:7]
        # midi_filename = midi_file.get_midi_filename()
        midi_data_rows = len(midi_data)
        print(f"{ts()} Midi Data lines:{midi_data_rows}x{len(midi_data[0])}, File: {midi_filename}")
        midi_time_length = midi_data_rows * frame_delay / 1000

        # Piano Keys LED Sequence, in 2D array
        pk_led_seq = None
        # display matrix size 8x32 display
        # initialize a 2 D list with 0 using lambda function
        led_matrix = [[0 for i in range(matrix_cols)] for j in range(matrix_rows)]
        ############################################################################
        start = ms()
        print("\n Raindrop Start ms:", mstr(), BRIGHTNESS, midi_data[0])
        # Starting Midi Raindrop
        if PLAY_MIDI_RAINDROP:
            for i in range(midi_data_rows):
                if print_level <= _INFO:
                    print(f'\r{mstr(start)} {frame_delay * i / 1000:5.2f}/{midi_time_length:5.2f} sec i={i:3} ', end="")
                next_row = midi_data[i]
                print_midi_row(next_row)
                led_matrix = shift_row(led_matrix, next_row)
                # calling display matrix
                display_mat(led_matrix, np, pk_led_seq=pk_led_seq, disp_color=None, brightness=BRIGHTNESS, color_palette = "rainbow")

                # display_matrix(led_matrix, np, pk_led_seq=pk_led_seq, esp32=esp32, disp_color=color.NAVY_BLUE, brightness = BRIGHTNESS)
                time.sleep_ms(frame_delay - 52)  # Correction for time taken for program 52 ms

            # Post Midi Raindrop

            np.write()
            print(f"{ts()} Midi Display completed")
        time.sleep(1 / 4)
        clear(np)
        print(f"{ts()} Display completed")
    except KeyboardInterrupt:
        print("Program terminated by using Keyboard ")
    finally:
        clear(np)        


if __name__ == '__main__':
    main(20)
