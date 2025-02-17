# -*- coding: utf-8 -*-
"""
==============================================================================
ascii_matrix.py: Reads ASCII Bitmap into 2D list for LED Matrix display
uses ascii_matrix.txt, should be in same folder

==============================================================================
Usages:
get_word_matrix(word)
get_word_matrix(word, compact = True)
get_word_matrix("Hello, how are you?", True)
@author: Jit_Sharma@gmail.com
------------------------------------------------------------------------------
- Version History:
    * {v# [date] user: comments}
    * v1 [05-Feb-25] Jit Sharma: First version
    * v2 [xx-Feb-25] Jit Sharma:
==============================================================================
"""
_DEBUG = 0
_INFO = 1
_WARNING = 2
_ERROR = 3
print_level = _INFO  # _DEBUG # _INFO # _WARNING # _ERROR
char_count = 95

# chars =""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
# 95 * 7 = 665
# print("Chars: ", len(chars))



values = [[0 for j in range(7)] for i in range(8)]
char_keys = [chr(c) for c in range(32, 127)]

def get_dict_chars():
    dict_chars = {}    # Load empty 2D Matrix in dictionary
    for key in char_keys:
        dict_chars[key] = values.copy()
    return dict_chars

def set_print_level(level):
    print_level = level
    
"""
# Returns 2D ASCII Char Bitmap Matrix

:return
Dictionary of Characters having 2D List of 8x7 char bitmap
"""
ascii_bitmap = 'ascii_bitmap.txt'

def load_matrix(filename=None):
    print(f"Loading 2D bitmap from {filename}")
    i = 0
    matrix = []
    try:
        line_num = 0
        with open(filename, 'r') as f:
            for line in f:
                # Print each line
                line = line.strip()
                lst = line.split(",")
                matrix.append(lst)
        f.close()
    except Exception as e:
        print(f"File not found [{filename}]")
        print(e)
        print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
    if len(matrix) > 0:
        print("Length:",len(matrix), len(matrix[0]))
    return matrix


def load_ascii_matrix(id=0):
    filename = 'ascii_bitmap.txt'
    print(f"Loading ASCII bitmap from {filename}")
    dict_chars = get_dict_chars()
    # print("\n...............................................\n")
    # open data file as per config file JSON
    i = 0
    matrix = []
    try:
        line_num = 0
        with open(filename, 'r') as f:
            for line in f:
                # Print each line
                line = line.strip()
                lst = line.split(",")
                for char_idx in range(95):
                    char_key = char_keys[char_idx]
                    char_bitmap = dict_chars[char_key]
                    #for col in range (char_idx*7, (char_idx+1)*7):
                    elem = lst[char_idx*7:(char_idx+1)*7]
                    char_bitmap[line_num] = elem
                    dict_chars[char_key] = char_bitmap
                # matrix.append(lst)
                # print(f"lst {i}: ",lst)
                # i += 1
                line_num += 1
        f.close()
    except Exception as e:
        print(f"File not found [{filename}]")
        print(e)
        print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
    print("Length:",len(matrix))
    return dict_chars


def get_word_matrix(word, compact=True):
    word_bitmap = None
    i = 0
    dict_chars = load_ascii_matrix() # Load the ascii bitmap

    for c in word:
        # print("Char is ", c)
        char_bitmap = dict_chars[c]
        if c != ' ' and compact:
            char_bitmap = compress_char_bitmap(char_bitmap)
        if i == 0:
            word_bitmap = char_bitmap.copy()
        else:
            word_bitmap  = [x + y for x, y in zip(word_bitmap, char_bitmap)]
        # print(f"i: {i}, c: {c}, {word_bitmap[0]}")
        i += 1
    empty_bitmap = [[0 for i in range(32)] for j in range(8)]
    word_bitmap  = [x + y for x, y in zip(word_bitmap, empty_bitmap)]
    return word_bitmap

def column_sum(l):
    lst = [list(map(int, i)) for i in l]
    return [sum(i) for i in zip(*lst)]

def column_sum1(lst):
    res = []
    for i in range(0, len(lst)):
        s = 0
        for j in range(0, len(lst[i])):
            if(len(lst[i][j])>0):
                s += int(lst[i][j])
        res.append(s)
    return res

def drop_col(lst, i):
     # print_word(lst,",")
    for j in lst:
        # print(f"row={j}, col={i}")
        del j[i]
    # print_word(lst, ",")
    return lst


# Compresses the Character and leaves only one empty space either side, width of i will be 3 columns
def compress_char_bitmap(bitmap):
    lsum = column_sum(bitmap)
    if(len(lsum)<7):
        return bitmap
    # print("Lsum", lsum, len(bitmap))
    empty_col = []
    for k in range(6, 0, -1):
        col_sum = lsum[k]
        #print("k:", k, "Col Sum:",  col_sum)
        if col_sum == 0:
            empty_col.append(k)
        else:
            break
    # print("Empty Columns: ", empty_col, "len:", len(empty_col))
    #print_word(bitmap)
    for k in range(len(empty_col)-1):
        idx = empty_col[k]
        # print("k:", empty_col[k], end=" ")
        # print_word(bitmap, char="_")
        bitmap = drop_col(bitmap,idx)
        #print("After dropping ", idx)
        #print_word(bitmap, char=".")
    #print("\n")
    print_word(bitmap, char=".")
    return bitmap

def print_word(word, char=" "):
    if print_level <= _DEBUG:
        for row in word:
            for c in row:
                if c == "0" or c==0:
                    c = char
                print(c, end=" ")
            print("\n")

# Reads ASCII Char Bitmap CSV, 8 rows height, width 7 char, 95x7



#a = dict_chars["t"]
# print_word(a)
#b = compress_char_bitmap(a)
#print("bitmap")
#print_word(b)

""" Testing 
jit = get_word_matrix('Jit', True)
print("World len", len(jit)," col: " ,len(jit[0]))
print_word(jit,".")
"""

""" 
0	0	0	0	0	0	0
0	0	1	1	1	0	0
0	1	0	0	0	1	0
0	1	0	0	0	1	0
0	1	1	1	1	1	0
0	1	0	0	0	1	0
0	1	0	0	0	1	0
0	0	0	0	0	0	0
"""
