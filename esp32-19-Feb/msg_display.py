# -*- coding: utf-8 -*-
"""
==============================================================================
msg_display.py:
Displays Text msg
Mode 0: Stationary for 3 minutes (5 Chars in 8x32, 10 chars in 8x64)
Mode 1: Scrolling text towards left (No limit on text length)
Mode 2: Strom in and Stop towards left (5 Chars in 8x32, 10 chars in 8x64)



Python files:
esp32_colors.py: Colors and Color palette
daisy9x32.py: for LED address of daisy chained 8x32 display
esp32_util.py: esp32 util functions

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
    * v1 [11-Feb-25] Jit Sharma: First version
    * v3 [xx-feb-25] Jit Sharma: Clean up

Last Updated: 12-Feb-25 3p
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
import matrix_util as mu
import ascii_matrix as am

text_storm_delay = 100 # ms
text_scroll_delay = 50  # 50 ms
frame_delay = 250  # 1/8 sec/ 250 ms

_DEBUG = 0
_INFO = 1
_WARNING = 2
_ERROR = 3
print_level = _INFO  # _DEBUG # _INFO # _WARNING # _ERROR
esp32 = True  # False #True
file_name = "LED_display"

matrix_rows = 9
matrix_cols = int(u.get_matrix_panel_width())
# dcdf = dc.get_dcdf(matrix_cols)

start_ms = time.ticks_ms()

BRIGHTNESS = u.get_brightness()  # 10 # in percentage, maximum 100



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



def main(msg='Hello!', mode = 1, duration = 2):
    try:
        # mode 2 for Storming Text, 1 for Scrolling Text, 0 = Stationary
        print(f'{ts()} Hi, There')
        led = machine.Pin(2, machine.Pin.OUT)
        led.value(1)
        time.sleep(0.1)
        led.value(0)

        np = NeoPixel(machine.Pin(4), matrix_rows * matrix_cols + 256)
        # np[0] = color.RED  # set the first pixel to RED
        #np.write()  # write data to all pixels
        #time.sleep(1/4)
        ############################################################################
        word_matrix = am.get_word_matrix(msg, compact=True)
        print(f'\r [{ts()}]: Mat[{matrix_rows}x{matrix_cols}] word_matrix len: {len(word_matrix)} x {len(word_matrix[0])}')
        word_df8x32 = [[0 for i in range(matrix_cols)] for j in range(matrix_rows - 1)]

        start = ms()
        column = []
        mu.display_matrix(word_df8x32, np, esp32=esp32)
        # get index of note_on bit len(df)
        BRIGHTNESS = u.get_brightness()
        
        if mode == 0:
            mat = mu.get_col_slice(word_matrix, 0, matrix_cols)
            mu.display_matrix(mat, np, esp32=esp32, disp_color=color.NAVY_BLUE, brightness=BRIGHTNESS)
            time.sleep(1) # Stays on till next command
            print(f"Text Display: [{msg}] Brightness: {BRIGHTNESS}")
        elif mode==1:
            print(f"Scrolling Text Display {msg} brightness:{BRIGHTNESS}")
        elif mode==2:
            print(f"Storm in and stop Text Display {msg} brightness:{BRIGHTNESS}")
            
        for col_idx in range(len(word_matrix[0])):
            if print_level <= _INFO:
                print(f'\r [{mstr(start)}] [{file_name}-{__name__}]: Processing column {col_idx+1}/{len(word_matrix[0])}',
                      end="")
            # print(f'\r{ts()} {frame_delay * i / 1000}/{len(df) * frame_delay / 1000} sec i={i} ', end="")
            column = mu.get_col(word_matrix, col_idx)
            if mode ==1:
                # Scrolling text
                word_df8x32 = mu.shift_left(word_df8x32, column)
                mu.display_matrix(word_df8x32, np, esp32=esp32, disp_color=color.NAVY_BLUE, brightness=BRIGHTNESS)
                # time.sleep_ms(text_scroll_delay)
                
            elif mode == 2:
                #storm in from left and stop
                disp = True
                speed = 2
                col_int = [int(i) for i in column]
                if sum(col_int)>0:
                    for i in range(len(word_df8x32[0]) - 1, col_idx - 1, -1*speed):
                        # print(f"i: {i} calling scroll_col")
                        a, b = mu.storm_col(word_df8x32, column, i)
                        #mu.display_matrix(word_df8x32, np, esp32=esp32, disp_color=color.NAVY_BLUE, brightness=BRIGHTNESS)
                        mu.display_cols(word_df8x32, np, i, esp32=esp32, disp_color=color.NAVY_BLUE, brightness=BRIGHTNESS, speed=speed)
                    if i > col_idx:
                        i = col_idx
                        a, b = mu.storm_col(word_df8x32, column, i)
                        mu.display_cols(word_df8x32, np, i, esp32=esp32, disp_color=color.NAVY_BLUE, brightness=BRIGHTNESS, speed=speed)
                #time.sleep(duration)
            else:
                pass
                    # time.sleep_ms(text_storm_delay)     
        ############################################################################
        time.sleep(1 / 4)
        if mode > 0:
            clear(np)
        # clear(np)
        print(f"\n{ts()} Display completed")
    except KeyboardInterrupt:
        print("\n\n Program terminated by using Keyboard ")
        clear(np)
    finally:
        #clear(np)
        pass


if __name__ == '__main__':
    print("8x32 LED Display, mode: Stationary, Scroll Left, Storm in")
    main(msg="FLOW NOTE", mode=1)