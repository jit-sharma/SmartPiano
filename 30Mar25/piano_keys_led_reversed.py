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
    dummy = []  # Dummy list to denote the damaged LED key
    piano = []
    dummy_count = 0
    white_count = 0
    black_count = 0
    piano_key_led_seq = []

    # Key type starting from right end, going towards left
    key_type = [                                     'W', 'B', 'W', 'B', 'W',  # 5 Keys starting from right end [52-48]
                'W', 'B', 'W', 'B', 'W', 'B', 'W',   'W', 'B', 'W', 'B', 'W',    # 12 Keys [47-41, 40-36]
                'W', 'B', 'W', 'B', 'W', 'B', 'W',   'D', 'D', 'W', 'B', 'W',    # 12 Keys [35-29, 28-24] 27,28 Dummy
                'W', 'B', 'W', 'B', 'W', 'B', 'W',   'W', 'B', 'W', 'B', 'W',    # 12 Keys [23-27, 16-12]
                'W', 'B', 'W', 'B', 'W', 'B', 'W',   'D', 'D', 'D', 'D', 'D']  # 7 keys [11-5] , 5 dummy Keys [4-0]
    """ 
    #[52, 51, 50, 49, 48,
      47, 46, 45, 44, 43, 42, 41,   40, 39, 38, 37, 36,   
      35, 34, 33, 32, 31, 30, 29,   28, 27, 26, 25, 24,   
      23, 22, 21, 20, 19, 18, 17,   16, 15, 14, 13, 12,   
      11, 10, 9, 8, 7, 6, 5,        4, 3, 2, 1, 0]
    
    Index used by piano_key_led_seq for display, 0-4 are not used,no LED, also no LED in dummy key
[   0,1,2,3,4,      5,6,7,8,9,10,11,
    12,13,14,15,16, 17,18,19,20,21,22,23,
    24,25,26,27,28, 29,30,31,32,33,34,35, 
    36,37,38,39,40, 41,42,43,44,45,46,47,
    48,49,50,51,52 ]    
    
    5-11 are swapped
    """
    i = init_seq
    #key_type_reversed = key_type[::-1]
    for key in key_type:
        if key == 'W':
            # ("White key")
            white_count += 1
            piano.append(white)
            if i == 0:
                piano_key_led_seq.append(white)
            else:
                seq = [w + i for w in white]
                # add seq of white key to the list in piano_key_led_seq at first position
                piano_key_led_seq.insert(0, seq)
                # piano_key_led_seq.append(seq)
            i += led_white # no of LED in white key
        elif key == 'D':
            # ("Dummy key")
            piano.append(dummy)
            if i == 0:
                piano_key_led_seq.append(dummy)
            else:
                seq = []
                piano_key_led_seq.insert(0, seq)
            # i += 0 # led_dummy  # no of LED in dummy key are ZERO
            dummy_count += 1
        else:
            # ("Black key")
            black_count += 1
            piano.append(black)
            if i == 0:
                piano_key_led_seq.append(black)
            else:
                seq = [b + i for b in black]
                piano_key_led_seq.insert(0, seq)
            i += led_black  # no of LED in black key

    if debug:
        print("Piano keys:", piano)
        # print_2d_array(piano)
        print("Seq keys:", piano_key_led_seq)
        print_2d_array(piano_key_led_seq)
    print(f'piano_key_led_sequence size: {len(piano_key_led_seq)}')
    #piano_key_led_seq = piano_key_led_seq[::-1]
    # swap index 5 with 11 and 6 with 10, 7 with 9
    print(f'piano_key index changed for 6 keys, 5-11')
    piano_key_led_seq[5], piano_key_led_seq[11] = piano_key_led_seq[11], piano_key_led_seq[5]
    piano_key_led_seq[6], piano_key_led_seq[10] = piano_key_led_seq[10], piano_key_led_seq[6]
    piano_key_led_seq[7], piano_key_led_seq[9] = piano_key_led_seq[9], piano_key_led_seq[7]
    if debug:
        print_2d_array(piano_key_led_seq)
        print("piano_key_led_seq[0]:", piano_key_led_seq[0])

    print(f'dummy_count: {dummy_count}, white_count: {white_count}, black_count: {black_count}')

    return piano_key_led_seq

def get_piano_key_led_seq2(init_seq=511, led_white=6, led_black=3, debug = False):
    piano_key_led_seq2 = [[512, 513, 514, 515, 516, 517], [518, 519, 520],
    [521, 522, 523, 524, 525, 526], [527, 528, 529],
    [530, 531, 532, 533, 534, 535],
    [536, 537, 538, 539, 540, 541], [542, 543, 544],
    [545, 546, 547, 548, 549, 550], [551, 552, 553],
    [554, 555, 556, 557, 558, 559], [560, 561, 562],
    [563, 564, 565, 566, 567, 568],

    [569, 570, 571, 572, 573, 574], [575, 576, 577],
    [578, 579, 580, 581, 582, 583], [584, 585, 586],
    [587, 588, 589, 590, 591, 592],
    [593, 594, 595, 596, 597, 598], [599, 600, 601],
    [602, 603, 604, 605, 606, 607], [608, 609, 610],
    [611, 612, 613, 614, 615, 616], [617, 618, 619],
    [620, 621, 622, 623, 624, 625],

    [626, 627, 628, 629, 630, 631], [632, 633, 634],
    [635, 636, 637, 638, 639, 640], [641, 642, 643],
    [644, 645, 646, 647, 648, 649],
    [650, 651, 652, 653, 654, 655], [656, 657, 658],
    [659, 660, 661, 662, 663, 664], [665, 666, 667],
    [668, 669, 670, 671, 672, 673], [674, 675, 676],
    [677, 678, 679, 680, 681, 682],

    [734, 735, 736, 737, 738, 739],
    [725, 726, 727, 728, 729, 730], [731, 732, 733],
    [716, 717, 718, 719, 720, 721], [722, 723, 724],
    [707, 708, 709, 710, 711, 712], [713, 714, 715],
    [701, 702, 703, 704, 705, 706],
    [692, 693, 694, 695, 696, 697], [698, 699, 700],
    [683, 684, 685, 686, 687, 688], [689, 690, 691],
    ]
    print("Seq keys:", piano_key_led_seq2)

def print_2d_array(arr):
    for index, i in enumerate(arr):
        print(f'[{index}: ', end=' ')
        for j in i:
            print(j, end=' ')
        print("]\n")
    """
    for i in arr:
        print("[", end=' ')
        for j in i:
            print(j, end=' ')
        print("]\n")
    """
if __name__ == "__main__":
    get_piano_key_led_seq(debug=False)
    #get_piano_key_led_seq2()
###
"""
Seq keys: [[256, 257, 258, 259, 260, 261], [262, 263, 264], [265, 266, 267, 268, 269, 270], [271, 272, 273], 
[274, 275, 276, 277, 278, 279], [280, 281, 282, 283, 284, 285], [286, 287, 288], [289, 290, 291, 292, 293, 294], [295, 296, 297], 
[298, 299, 300, 301, 302, 303], [304, 305, 306], [307, 308, 309, 310, 311, 312], [313, 314, 315, 316, 317, 318], [319, 320, 321], 
[322, 323, 324, 325, 326, 327], [328, 329, 330], [331, 332, 333, 334, 335, 336], [337, 338, 339, 340, 341, 342], [343, 344, 345], 
[346, 347, 348, 349, 350, 351], [352, 353, 354], [355, 356, 357, 358, 359, 360], [361, 362, 363], [364, 365, 366, 367, 368, 369], 
[370, 371, 372, 373, 374, 375], [376, 377, 378], [379, 380, 381, 382, 383, 384], [385, 386, 387], [388, 389, 390, 391, 392, 393], 
[394, 395, 396, 397, 398, 399], [400, 401, 402], [403, 404, 405, 406, 407, 408]]

Seq keys: 
C2
[[512, 513, 514, 515, 516, 517], [518, 519, 520], 
[521, 522, 523, 524, 525, 526], [527, 528, 529], 
[530, 531, 532, 533, 534, 535],
[536, 537, 538, 539, 540, 541], [542, 543, 544], 
[545, 546, 547, 548, 549, 550], [551, 552, 553], 
[554, 555, 556, 557, 558, 559], [560, 561, 562], 
[563, 564, 565, 566, 567, 568], 
C3
[569, 570, 571, 572, 573, 574], [575, 576, 577], 
[578, 579, 580, 581, 582, 583], [584, 585, 586], 
[587, 588, 589, 590, 591, 592], 
[593, 594, 595, 596, 597, 598], [599, 600, 601], 
[602, 603, 604, 605, 606, 607], [608, 609, 610], 
[611, 612, 613, 614, 615, 616], [617, 618, 619], 
[620, 621, 622, 623, 624, 625], 
C4
[626, 627, 628, 629, 630, 631], [632, 633, 634], 
[635, 636, 637, 638, 639, 640], [641, 642, 643], 
[644, 645, 646, 647, 648, 649], 
[650, 651, 652, 653, 654, 655], [656, 657, 658], 
[659, 660, 661, 662, 663, 664], [665, 666, 667], 
[668, 669, 670, 671, 672, 673], [674, 675, 676], 
[677, 678, 679, 680, 681, 682], 
C5
[683, 684, 685, 686, 687, 688], [689, 690, 691], 
[692, 693, 694, 695, 696, 697], [698, 699, 700], 
[701, 702, 703, 704, 705, 706], 
[707, 708, 709, 710, 711, 712], [713, 714, 715], 
[716, 717, 718, 719, 720, 721], [722, 723, 724], 
[725, 726, 727, 728, 729, 730], [731, 732, 733], 
[734, 735, 736, 737, 738, 739]]
"""
