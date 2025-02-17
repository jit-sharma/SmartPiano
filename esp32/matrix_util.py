# -*- coding: utf-8 -*-
"""
==============================================================================
matrix_util.py:
Matrix Utility functions and display helper 
[MicroPython ESP32]
==============================================================================
Usages:


@author: Jit_Sharma@gmail.com
------------------------------------------------------------------------------
- Version History:
    * {v# [date] user: comments}
    * v1 [8-Feb-25] Jit Sharma: First version
    * v2 [12-Feb-25] : 
    
Last Updated: 12-Feb-25
==============================================================================
"""

import machine
from machine import Pin
from neopixel import NeoPixel

# standard
import time
import json

# Program files 
import esp32_colors as color
import midi_data as midi_file
import daisy_chained as dc
import esp32_util as eu




frame_delay = 100  # ms 1/8 sec

matrix_rows = 9
matrix_cols = int(eu.get_matrix_panel_width())
# dcdf = dc.get_dcdf(matrix_cols)

    
_DEBUG = 0
_INFO = 1
_WARNING = 2
_ERROR = 3
print_level = _INFO  # _DEBUG # _INFO # _WARNING # _ERROR
esp32 = True # False #True

def set_print_level(level):
    print_level = level


def shift_row(matrix, row):
    """
    Shifts rows down by 1 in 2D Matrix, insert row at the top of the matrix
    
    Parameters:
    matrix (List): 2D List Matrix
    row (List): 1 D List to be added to Matrix
    
    returns:
    List: updated matrix
    """
    size = len(matrix)
    # Starting from bottom replace with previous one
    for i in range(size-1, 0, -1):
        matrix[i] = matrix[i - 1]
        # print(matrix[i], end=' ')
    # Filling first row with new row
    matrix[0] = row.copy()
    return matrix

def get_col_slice(matrix, col_start=0, col_end=1):
    columns = [row[col_start:col_end] for row in matrix]
    return columns

def get_col(matrix, col_idx):
    column = [row[col_idx] for row in matrix]
    if print_level <= _DEBUG:
        print("Column: ", column)
    return column


def add_lists_colwise(list1, list2):
    joined_list  = [x + y for x, y in zip(list1, list2)]
    return joined_list


def add_col_to_list(lst, column):
    for idx, _ in enumerate(lst):
        # getting all values at same index row
        # extending the initial matrix
        lst[idx].append(column[idx])
    print_list_row_count(lst)
    return lst


def drop_col(lst, i):
    for j in lst:
        # print(f"row={j}, col={i}")
        del j[i]
    #print_word(lst, ",")
    return lst


def print_matrix(matrix, char=" "):
    if print_level <= _DEBUG:
        for row in matrix:
            for col in row:
                if col == "0" or col==0:
                    c = char
                print(col, end=" ")
            print("\n")

def print_list_row_count(lst):
    if print_level <= _DEBUG:
        for i in range(8):
            print(len(lst[i]), end=" ")
        print("\n")

def shift_left(matrix, col):
    if print_level <= _DEBUG:
        print(" Shift left starting....")
    print_list_row_count(matrix)
    # insert column at the right of the matrix and drop the first column
    lst = add_col_to_list(matrix, col)
    print_list_row_count(lst)
    # delete first column
    lst = drop_col(lst,0)

    if print_level <= _DEBUG:
        print(" Shift Left completed")
    return lst


def clear(np):
    np.fill((0, 0, 0))
    np.write()

def wipe(np):
    np.fill((0, 0, 0))


def storm_col(lst2d, col, idx):
    tail = False
    size = len(lst2d[0])
    for i in range(len(lst2d)):
        lst2d[i][idx] = col[i]
        if idx < size - 1:
            lst2d[i][idx + 1] = 0
            tail = True
    # print_2d(lst2d)
    return idx, tail


def storm_left(lst2d, col, final_idx):
    for i in range(len(lst2d[0]) - 1, final_idx - 1, -1):
        #print(f"i: {i} calling scroll_col")
        _,_ = storm_col(lst2d, col, i)
        # Call display function here
    return lst2d

# Print midi row with separator as pipe every octave of 12 keys notes
def print_midi_row(row):
    c = 0
    for i in row:
        if i == 0 or i == '0':
            i = "."
        if c % 12 == 0:
            i = str(i) + " | "
        print(f'{i:2}', end=" ")
        c += 1
    print("\n")


def display_matrix_keys(_df, np, pk_led_seq, esp32=False, disp_color=color.NAVY_BLUE, brightness=100, color_palette=None):
    if print_level <= _DEBUG:
        print(f"{ts()} Display Matrix", _df)
    wipe(np)
    palette = color.get_cp(color_palette)
    """
    if color_palette is None:
        palette = color.cp["c76"]
    else:
        palette = color.cp[color_palette]
    """
    df_cols = len(_df[0])
    
    dcdf = dc.get_dcdf(matrix_cols)
    # For 8 rows on display matrix
    for i in range(matrix_rows - 1):
        for j in range(df_cols): # only run for df col size
            if print_level <= _DEBUG:
                print(_df[i][j], end=' ')
            # pixel_color_code - code in MIDI Bit File
            pixel_color_code = _df[i][j]
            if pixel_color_code >= 1:
                if disp_color is None and pixel_color_code <= 64:  # len(color.d.keys()
                    # get dc9x32 or dc8x32 value at [i,j] np[dc8x32[i,j]]
                    # np[dcdf[i][j]] = color.brightness(color.cp["left"][j], brightness)
                    if color_palette is None:
                        np[dcdf[i][j]] = color.brightness(palette[pixel_color_code], brightness) # data value based color
                    else:
                        np[dcdf[i][j]] = color.brightness(palette[j], brightness) # position based color for Column
                    # np[i * matrix_cols + j] = color.d[pixel_color_code]
                else:
                    np[dcdf[i][j]] = color.brightness(disp_color, brightness)
        if print_level <= _DEBUG:
            print('\n')
    # 9th row for Piano Keys
    piano_row = _df[8:]
    j = 0
    if pk_led_seq is not None:
        for piano_key in pk_led_seq:
            pixel_color_code = _df[8][j]
            # print(f"{j}, color:{pixel_color_code}")
            if pixel_color_code >= 1:
                # print(f'{j}: Piano Key:', len(piano_key), piano_key)
                for led_seq in piano_key:
                    if disp_color is None and pixel_color_code <= 64:  # len(color.d.keys()
                        # get led_seq
                        ## np[led_seq] = color.brightness(color.d[pixel_color_code], 100)  # Full brightness for Piano Keys
                        # print(f'led_seq {led_seq}, color: {pixel_color_code}')
                        if color_palette is None:
                            np[led_seq] = color.brightness(palette[pixel_color_code], 100) # data value based color
                        else:
                            np[led_seq]  = color.brightness(palette[j], 100) # position based color for Column                        
                    else:
                        np[led_seq] = color.brightness(disp_color, 100)  # Full brightness for Piano Keys
                j += 1
    
    np.write()
    if print_level <= _DEBUG:
        print(f'{ts()} Displayed Matrix')



def display_cols(_df, np, cols_id, esp32=False, disp_color=None, brightness=100, speed=1):
    # print("col_id ", cols_id)
    dcdf = dc.get_dcdf(matrix_cols)
    palette = color.get_cp()
    cols_list = [cols_id+i for i in range(speed+1)]
    for i in range(matrix_rows-1):
        first = True
        for j in cols_list:
            if j < matrix_cols:
                if print_level <= _DEBUG:
                    print(f'[{i},{j}]: {_df[i][j]}', end=' ')
                # pixel_color_code - code in MIDI Bit File
                pixel_color_code = int(_df[i][j])
                if first and pixel_color_code >= 1:
                    if disp_color is None and pixel_color_code <= 64: # len(color.d.keys()
                        # get dc9x32 or dc8x32 value at [i,j] np[dc8x32[i,j]]
                        #print("color:", _df[i][j], end=' ')
                        np[dcdf[i][j]] = color.brightness(palette[j], brightness)
                    else:
                        np[dcdf[i][j]] = color.brightness(disp_color, brightness)
                    first = False
                    c = j
                else:
                    np[dcdf[i][j]]  = color.BLACK
                    c = 0
        if print_level <= _DEBUG:
            print(f' c:{c} \n')
    np.write()
    #time.sleep(.5)
    if print_level <= _DEBUG:
        print('Displayed Matrix Cols')

def display_matrix(_df, np, esp32=False, disp_color=None, brightness=100):
    wipe(np)
    dcdf = dc.get_dcdf(matrix_cols)
    palette = color.get_cp("c76")
    for i in range(matrix_rows-1):
        for j in range(matrix_cols):
            if print_level <= _DEBUG:
                print(_df[i][j], end=' ')
            # pixel_color_code - code in MIDI Bit File
            pixel_color_code = int(_df[i][j])
            if pixel_color_code >= 1:
                if disp_color == None and pixel_color_code <= 64: # len(color.d.keys()
                    # get dc9x32 or dc8x32 value at [i,j] np[dc8x32[i,j]]
                    np[dcdf[i][j]] = color.brightness(palette[pixel_color_code], brightness)
                    #np[i * matrix_cols + j] = color.d[pixel_color_code]
                else:
                    np[dcdf[i][j]] = color.brightness(disp_color, brightness)
        if print_level <= _DEBUG:
            print('\n')
    if esp32:
        np.write()
    if print_level <= _DEBUG:
        print('Displayed Matrix')
