# -*- coding: utf-8 -*-
"""
==============================================================================
piano_keys_led.py:
Project: MIDI to 8x32 LED Matrix display in raindrop style and LED lit Piano Keys
This file is used to generate the list of piano keys and the corresponding LED sequence.
White key has 6 LEDs and Black key has 3 LEDs.
The sequence of 12 keys in an Octave is as follows:
White, Black, White, Black, White, White, Black, White, Black, White, Black, White,
C, C#, D, D#, E, F, F#, G, G#, A, A#, B,
This sequence is repeated for 8 Octaves. We have 8 White keys and 5 Black keys in an Octave.
We have 32 keys in this program. C3 - 12 keys, C4 - 12 keys and 8 keys from C5 Octave.
The LED sequence is generated for 32 keys after 8x32 matrix is daisy chained.
Starting 256 till 408, having total 152 LEDs.

2 panels - 256 * 2 = 512, starting value is updated to 512
20*9 = 180
8*6 = 48
Total: 228
512 + 228
Total: 740
used by led_display.py
==============================================================================
Usages:
# Refer 2D array piano_key_led_seq to address the LED by its sequence.

@author: Jit_Sharma@gmail.com
------------------------------------------------------------------------------
- Version History:
    * {v# [date] user: comments}
    * v1 [6-Feb-25] Jit Sharma: First version
    * v2 [dd-Mon-yy] Jit Sharma:
    
    17-Feb-25
==============================================================================
"""


def get_piano_key_led_seq(init_seq=511, led_white=6, led_black=3, debug = False):
    # white = [1, 2, 3, 4, 5, 6]
    # black = [1, 2, 3]
    white = [i for i in range(1, led_white + 1)]
    black = [i for i in range(1, led_black + 1)]
    piano = []
    piano_key_led_seq = []



    # W	B	W	B	W	W	B	W	B	W	B	W	W	B	W	B	W	W	B	W	B	W	B	W	W	B	W	B	W	W	B	W
    key_type = ['W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
                'W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
                'W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
                'W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W',]
    i = init_seq
    for key in key_type:
        if key == 'W':
            # ("White key")
            piano.append(white)
            if i == 0:
                piano_key_led_seq.append(white)
            else:
                seq = [w + i for w in white]
                piano_key_led_seq.append(seq)
            i += led_white # no of LED in white key
        else:
            # ("Black key")
            piano.append(black)
            if i == 0:
                piano_key_led_seq.append(black)
            else:
                seq = [b + i for b in black]
                piano_key_led_seq.append(seq)
            i += led_black  # no of LED in black key

    if debug:
        print("Piano keys:", piano)
        print_2d_array(piano)
        print("Seq keys:", piano_key_led_seq)
        print_2d_array(piano_key_led_seq)
    print(f'piano_key_led_sequence size: {len(piano_key_led_seq)}')
    return piano_key_led_seq


def print_2d_array(arr):
    for i in arr:
        for j in i:
            print(j, end=' ')
        print("\n")

if __name__ == "__main__":
    #get_piano_key_led_seq(debug=True)
    get_piano_key_led_seq()
###
"""
Seq keys: [[256, 257, 258, 259, 260, 261], [262, 263, 264], [265, 266, 267, 268, 269, 270], [271, 272, 273], 
[274, 275, 276, 277, 278, 279], [280, 281, 282, 283, 284, 285], [286, 287, 288], [289, 290, 291, 292, 293, 294], [295, 296, 297], 
[298, 299, 300, 301, 302, 303], [304, 305, 306], [307, 308, 309, 310, 311, 312], [313, 314, 315, 316, 317, 318], [319, 320, 321], 
[322, 323, 324, 325, 326, 327], [328, 329, 330], [331, 332, 333, 334, 335, 336], [337, 338, 339, 340, 341, 342], [343, 344, 345], 
[346, 347, 348, 349, 350, 351], [352, 353, 354], [355, 356, 357, 358, 359, 360], [361, 362, 363], [364, 365, 366, 367, 368, 369], 
[370, 371, 372, 373, 374, 375], [376, 377, 378], [379, 380, 381, 382, 383, 384], [385, 386, 387], [388, 389, 390, 391, 392, 393], 
[394, 395, 396, 397, 398, 399], [400, 401, 402], [403, 404, 405, 406, 407, 408]]

"""
