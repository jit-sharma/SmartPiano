# -*- coding: utf-8 -*-
"""
==============================================================================
midi_data.py:
reads config.json and midi/animation data files
[MicroPython ESP32]

get_midi_data_ext: returns 5 parameters
get_midi_data : returns, 2 parameters 

==============================================================================
Usages:
used by midi and animaton display files


@author: Jit_Sharma@gmail.com
------------------------------------------------------------------------------
- Version History:
    * {v# [date] user: comments}
    * v1 [8-Feb-25] Jit Sharma: First version
    * v2 [12-Feb-25] Jit Sharma: 2nd version
    
Last Updated: 12-Feb-25
==============================================================================

"""

import json

midi_filename = None

def set_midi_filename(filename):
    global midi_filename
    midi_filename = filename    

def get_midi_filename():
    return midi_filename

def init():
    pass


def get_midi_data(id=0):
    # Use JSON config file
    config = json.loads(open('config.json').read())
    md = config["midi_data"]
    
    if id == 0:
        midi_id = config["play_midi_num"]
    else:
        midi_id = id
    midi_key =  str(midi_id)
    print("midi_id:", midi_id, "Midi Key:", md[midi_key]["id"])
    print("Midi file name", md[midi_key]["name"])
    filename = md[midi_key]["name"]
    set_midi_filename(filename)
    print(f"Midi File Name: {filename}")
    i = 0
    matrix = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Print each line
                line = line.strip()
                lst = line.split(",")
                lst = [int(item) for item in lst]
                matrix.append(lst)
                # print(f"lst {i}: ",lst)
                i += 1
        f.close()
    except:
        print(f"File not found [{filename}]")
    print("Length:",len(matrix))
    return matrix, filename


def get_midi_data_ext(id=0):
    # Use JSON config file
    config = json.loads(open('config.json').read())
    md = config["midi_data"]
    piano_start_note = config["piano_start_note"] # Note number C3 as 48

    print(f"Piano start note: {piano_start_note} ")


    if id == 0:
        midi_id = config["play_midi_num"]
    else:
        midi_id = id
    midi_key = str(midi_id)
    filename = md[midi_key]["name"]
    start_note = md[midi_key]["start_note"]
    frame_delay = md[midi_key]["frame_delay"]
    color_palette = md[midi_key]["color_palette"]
    midi_dict = {}
    midi_dict["name"] = filename
    midi_dict["start_note"] = start_note
    midi_dict["frame_delay"] = frame_delay
    midi_dict["color_palette"] = color_palette
    
    print("midi_id:", midi_id, "Midi id:", md[midi_key]["id"])
    print("Midi file name", filename)

    
    set_midi_filename(filename)
    print(f"Midi File Name: {filename}")

    i = 0
    matrix = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Print each line
                line = line.strip()
                lst = line.split(",")
                lst = [int(item) for item in lst]
                matrix.append(lst)
                # print(f"lst {i}: ",lst)
                i += 1
        f.close()
    except:
        print(f"File not found [{filename}]")
    print("Length:",len(matrix))
    return matrix, filename, start_note, color_palette, frame_delay


def main():
    print("Standalone test")
    get_midi_data(1)


if __name__ == '__main__':
    main()

