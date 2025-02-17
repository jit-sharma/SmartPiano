# -*- coding: utf-8 -*-
"""
==============================================================================
esp32_colors.py:
Holds Color Definitions and palettes
color tuple in RGB format: (r,g,b)
[MicroPython ESP32]
==============================================================================
Usages:
color_list[] or dict d[]: list of 40 colors
brightness function
get_color_palette(palette_id): returns list of color code for palette
color_transition(color1, color2, n): returns list of n colors between color1 and color2


@author: Jit_Sharma@gmail.com
------------------------------------------------------------------------------
- Version History:
    * {v# [date] user: comments}
    * v1 [8-Jan-25] Jit Sharma: First version
    * v2 [12-Feb-25]: brightness function added
    * v3: color palette added

Last Updated: 12-Feb-25
==============================================================================

"""
from collections import OrderedDict

# BW 0 1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# RGB 2 3 4
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# CMY 5 6 7
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

# Gray 8 9
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)

# Misc 10 11 12
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
VIOLET = (238, 130, 238)

# Other 13 14 15
INDIGO = (75, 0, 130)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)

# List of colors 200 150 180 Saturation
# 16 17 18
RED200 = (200, 0, 0)
GREEN200 = (0, 200, 0)
BLUE200 = (0, 0, 200)

# 19 20 21
RED150 = (150, 0, 0)
GREEN150 = (0, 150, 0)
BLUE150 = (0, 0, 150)

# 22 23 24
CYAN200 = (0, 200, 200)
MAGENTA200 = (200, 0, 200)
YELLOW200 = (200, 200, 0)

# 25 26 27
CYAN150 = (0, 150, 150)
MAGENTA150 = (150, 0, 150)
YELLOW150 = (150, 150, 0)

# 28 29 30
ORANGE200 = (200, 120, 0)
VIOLET180 = (180, 100, 180)
INDIGO150 = (75, 0, 150)

# 31 32 33
CYAN_BLUE = (0, 127, 255)
CYAN_BLUE200 = (0, 100, 200)
RED_BLUE = (127, 0, 255)

# 34 35 36
PARROT_GREEN = (0, 255, 127)
PARROT_GREEN200 = (0, 200, 100)
DARK_GREEN = (0, 100, 0)

# 37 38 39
BLUE_RED = (255, 0, 127)
BLUE_RED200 = (200, 0, 100)
NAVY_BLUE = (0, 0, 100)

# To make benefit of ordered keys, OrderedDict should be initialized
# from sequence of (key, value) pairs.
"""
d = OrderedDict()
d[0] = BLACK
d[1] = WHITE
d[2] = RED
d[3] = GREEN
d[4] = BLUE
d[5] = CYAN
d[6] = MAGENTA
d[7] = YELLOW
d[8] = SILVER
d[9] = GRAY
d[10] = ORANGE
d[11] = PURPLE
d[12] = VIOLET
d[13] = INDIGO
d[14] = MAROON
d[15] = OLIVE
d[16] = RED200
d[17] = GREEN200
d[18] = BLUE200
d[19] = RED150
d[20] = GREEN150
d[21] = BLUE150
d[22] = CYAN200
d[23] = MAGENTA200
d[24] = YELLOW200
d[25] = CYAN150
d[26] = MAGENTA150
d[27] = YELLOW150
d[28] = ORANGE200
d[29] = VIOLET180
d[30] = INDIGO150
d[31] = CYAN_BLUE
d[32] = CYAN_BLUE200
d[33] = RED_BLUE
d[34] = PARROT_GREEN
d[35] = PARROT_GREEN200
d[36] = DARK_GREEN
d[37] = BLUE_RED
d[38] = BLUE_RED200
d[39] = NAVY_BLUE
"""

color_list = [BLACK, WHITE,
              RED, GREEN, BLUE,
              CYAN, MAGENTA, YELLOW, SILVER, GRAY,
              ORANGE, PURPLE, VIOLET,
              INDIGO, MAROON, OLIVE,
              RED200, GREEN200, BLUE200,
              RED150, GREEN150, BLUE150,
              CYAN200, MAGENTA200, YELLOW200,
              CYAN150, MAGENTA150, YELLOW150,
              ORANGE200, VIOLET180, INDIGO150,
              CYAN_BLUE, CYAN_BLUE200, RED_BLUE,
              PARROT_GREEN, PARROT_GREEN200, DARK_GREEN,
              BLUE_RED, BLUE_RED200, NAVY_BLUE]





def get_single_color12(color):
    return [color for i in range(12)]


def get_cp(color_palette = "c76"):
    # print(f"color_palette: [{color_palette}]")
    RAINBOW32 = [(255, 0, 0), (255, 0, 50), (255, 0, 101), (255, 0, 153), (255, 0, 204),    # Red to Violet
                 (255, 0, 255), (204, 0, 255), (153, 0, 255), (101, 0, 255), (50, 0, 255),  # Violet to Blue
                 (0, 0, 255), (0, 50, 255), (0, 101, 255), (0, 153, 255), (0, 204, 255),    # Blue to Cyan
                 (0, 255, 255), (0, 255, 204), (0, 255, 153), (0, 255, 101), (0, 255, 50),  # Cyan to Green
                 (0, 255, 0), (50, 255, 0), (101, 255, 0), (153, 255, 0), (204, 255, 0),    # Green to Yellow
                 (255, 255, 0), (255, 204, 0), (255, 153, 0), (255, 127, 0), (255, 101, 0), # Yellow to Red
                 (255, 50, 0), (255, 25, 0)]

    RAINBOW32_1 = (255, 0, 0)
    RAINBOW32_2 = (255, 0, 50)
    RAINBOW32_3 = (255, 0, 101)
    RAINBOW32_4 = (255, 0, 153)
    RAINBOW32_5 = (255, 0, 204)
    RAINBOW32_6 = (255, 0, 255)
    RAINBOW32_7 = (204, 0, 255)
    RAINBOW32_8 = (153, 0, 255)
    RAINBOW32_9 = (101, 0, 255)
    RAINBOW32_10 = (50, 0, 255)
    RAINBOW32_11 = (0, 0, 255)
    RAINBOW32_12 = (0, 50, 255)
    RAINBOW32_13 = (0, 101, 255)
    RAINBOW32_14 = (0, 153, 255)
    RAINBOW32_15 = (0, 204, 255)
    RAINBOW32_16 = (0, 255, 255)
    RAINBOW32_17 = (0, 255, 204)
    RAINBOW32_18 = (0, 255, 153)
    RAINBOW32_19 = (0, 255, 101)
    RAINBOW32_20 = (0, 255, 50)
    RAINBOW32_21 = (0, 255, 0)
    RAINBOW32_22 = (50, 255, 0)
    RAINBOW32_23 = (101, 255, 0)
    RAINBOW32_24 = (153, 255, 0)
    RAINBOW32_25 = (204, 255, 0)
    RAINBOW32_26 = (255, 255, 0)
    RAINBOW32_27 = (255, 204, 0)
    RAINBOW32_28 = (255, 153, 0)
    RAINBOW32_29 = (255, 127, 0)
    RAINBOW32_30 = (255, 101, 0)
    RAINBOW32_31 = (255, 50, 0)
    RAINBOW32_32 = (255, 25, 0)

    # Color palette of 32 Colors (Red to Magenta), (Red to Yellow), (Green to Yellow), (Blue to Cyan), (Blue to Magenta), (Cyan to Green)
    my_color_palette_RM6 = [RAINBOW32_1, RAINBOW32_2, RAINBOW32_3, RAINBOW32_4, RAINBOW32_5, RAINBOW32_6]
    my_color_palette_RY8 = [RAINBOW32_1, RAINBOW32_32, RAINBOW32_31, RAINBOW32_30, RAINBOW32_29, RAINBOW32_28, RAINBOW32_27, RAINBOW32_26]
    my_color_palette_GY6 = [RAINBOW32_21, RAINBOW32_22, RAINBOW32_23, RAINBOW32_24, RAINBOW32_25, RAINBOW32_26]
    my_color_palette_BC6 = [RAINBOW32_11, RAINBOW32_12, RAINBOW32_13, RAINBOW32_14, RAINBOW32_15, RAINBOW32_16]
    my_color_palette_BM6 = [RAINBOW32_11, RAINBOW32_10, RAINBOW32_9, RAINBOW32_8, RAINBOW32_7, RAINBOW32_6]
    my_color_palette_CG6 = [RAINBOW32_16, RAINBOW32_17, RAINBOW32_18, RAINBOW32_19, RAINBOW32_20, RAINBOW32_21]

    RAINBOW48 = [(0,0,0) for i in range(48)]

    # print(RAINBOW48)

    RAINBOW48[0] = (255, 0, 0)
    RAINBOW48[1] = (255, 0, 31)
    RAINBOW48[2] = (255, 0, 63)
    RAINBOW48[3] = (255, 0, 95)
    RAINBOW48[4] = (255, 0, 127)
    RAINBOW48[5] = (255, 0, 159)
    RAINBOW48[6] = (255, 0, 191)
    RAINBOW48[7] = (255, 0, 223)
    RAINBOW48[8] = (255, 0, 255)
    RAINBOW48[9] = (223, 0, 255)
    RAINBOW48[10] = (191, 0, 255)
    RAINBOW48[11] = (159, 0, 255)
    RAINBOW48[12] = (127, 0, 255)
    RAINBOW48[13] = (95, 0, 255)
    RAINBOW48[14] = (63, 0, 255)
    RAINBOW48[15] = (31, 0, 255)
    RAINBOW48[16] = (0, 0, 255)
    RAINBOW48[17] = (0, 31, 255)
    RAINBOW48[18] = (0, 63, 255)
    RAINBOW48[19] = (0, 95, 255)
    RAINBOW48[20] = (0, 127, 255)
    RAINBOW48[21] = (0, 159, 255)
    RAINBOW48[22] = (0, 191, 255)
    RAINBOW48[23] = (0, 223, 255)
    RAINBOW48[24] = (0, 255, 255)
    RAINBOW48[25] = (0, 255, 223)
    RAINBOW48[26] = (0, 255, 191)
    RAINBOW48[27] = (0, 255, 159)
    RAINBOW48[28] = (0, 255, 127)
    RAINBOW48[29] = (0, 255, 95)
    RAINBOW48[30] = (0, 255, 63)
    RAINBOW48[31] = (0, 255, 31)
    RAINBOW48[32] = (0, 255, 0)
    RAINBOW48[33] = (31, 255, 0)
    RAINBOW48[34] = (63, 255, 0)
    RAINBOW48[35] = (95, 255, 0)
    RAINBOW48[36] = (127, 255, 0)
    RAINBOW48[37] = (159, 255, 0)
    RAINBOW48[38] = (191, 255, 0)
    RAINBOW48[39] = (223, 255, 0)
    RAINBOW48[40] = (255, 255, 0)
    RAINBOW48[41] = (255, 223, 0)
    RAINBOW48[42] = (255, 191, 0)
    RAINBOW48[43] = (255, 159, 0)
    RAINBOW48[44] = (255, 127, 0)
    RAINBOW48[45] = (255, 95, 0)
    RAINBOW48[46] = (255, 63, 0)
    RAINBOW48[47] = (255, 31, 0)

    # print(RAINBOW48[i])

    RAINBOW12 = [i for i in range(12)]
    for i in range(12):
        RAINBOW12[i] = RAINBOW48[i*4]
    # print(RAINBOW12)

    RAINBOW12b = [i for i in range(12)]
    for i in range(12):
        RAINBOW12b[i] = RAINBOW48[i*4+1]
    # print(RAINBOW12b)

    RAINBOW12c = [i for i in range(12)]
    for i in range(12):
        RAINBOW12c[i] = RAINBOW48[i*4+2]
    # print(RAINBOW12c)

    RAINBOW12d = [i for i in range(12)]
    for i in range(12):
        RAINBOW12d[i] = RAINBOW48[i*4+3]
    # print(RAINBOW12d)    
    
    color_pal_rainbow = RAINBOW12 + RAINBOW12b + RAINBOW12c + RAINBOW12d + RAINBOW12 + RAINBOW12b
    # Octave 2 and 3 in rainbow 12 colors and Octave 4, 5, 6, 7 in green
    color_pal_left = RAINBOW12 + get_single_color12(GREEN) * 5

    # Octave 2 and 3 in GREEN and Octave 4, 5, 6  rainbow 12 colors
    color_pal_right = get_single_color12(BLUE) + RAINBOW12 + RAINBOW12b + RAINBOW12c + RAINBOW12d + RAINBOW12
   
    cp = dict()
    cp["rainbow"] = color_pal_rainbow
    cp["left"] = color_pal_left # left24_rainbow_green
    cp["right"] = color_pal_right # right24_blue_rainbow
    cp["c40"] = color_list
    cp["c76"] = color_list[2:]+color_list[2:]
    #print(cp.keys(), color_palette)
    #print(f"returning cp {color_palette:} {len(cp[color_palette])}")
    return cp[color_palette] 
    

# -----------------------------------------------------------------------------
# changing brightness, value 0-100 in %
def brightness(c, brightness_pc):
    """
    Return color with brightness percentage changed
    minimum brightness is 10% and maximum is 100%
    """
    return tuple([int(i*brightness_pc/100) for i in c])


def color_transition(color1, color2, n):
    """
    Return a list of n colors from color1 to color2
    """
    color_list = []
    for i in range(n):
        r = color1[0] + (color2[0] - color1[0]) * i / n
        g = color1[1] + (color2[1] - color1[1]) * i / n
        b = color1[2] + (color2[2] - color1[2]) * i / n
        color_list.append((r, g, b))
    return color_list


# -----------------------------------------------------------------------------
def main():
    print("ESP32 MicroPython NeoPixel Color Palette")
    print("Color List:", len(color_list))

    print("RAINBOW32:", len(RAINBOW32))
    print("RAINBOW48:", len(RAINBOW48))
    print("rainbow:", len(cp["rainbow"]), len(cp["left"]), len(cp["right"]) )

    for j in range(12):
        print("rainbow", j, cp["left"][j])


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()

# =============================================================================
