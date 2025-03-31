"""
2D array to store index of column daisy chain in 9x32 matrix
dc9x32 is column daisy chain in 8x32 matrix, first col, 0 to 7, second and all odd col 8 to 15 bottom to up,
 third col 16 to 23, fourth col 24 to 31

Midi bitmap to use masked dc8x32 or dc8x64
Piano Keys LED Sequence, either matched with midi data or all keys or

"""
debug = False



def print_2d(short=False, lst=None):
    print("List length: ", len(lst),"x" ,len(lst[0]))
    for i in range(len(lst[0])):
        print(f'---', end='_')
    print("\n")
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if short:
                print('{:03}'.format(lst[i][j]), end=' ')
            else:
                print(f'dc[{i},{j}]: {lst[i][j]}', end=' ')
        print("\n")
    for i in range(len(lst[0])):
        print(f'---', end='_')
    print("\n")


# print("2D List:", df)

def get_dc9x32x64():
    # sample 2d list = [[0 for i in range(8)] for j in range(32)]
    # 9th row for piano keys in sequence
    row9 = [k + 8 * 32 for k in range(32)]
    # 8x32 matrix initialization in sequence left to right, top to bottom

    # 8x32 matrix initialization in sequence top to bottom, left to right,
    dc9x32 = [[i + j * 8 for j in range(32)] for i in range(8)]
    dc9x32.append(row9.copy())

    # 8x64 matrix initialization in sequence top to bottom, left to right,
    dc9x64 = [[i + j * 8 for j in range(64)] for i in range(8)]
    row9x = [k + 8 * 64 for k in range(64)]
    dc9x64.append(row9x.copy())
    if debug:
        print_2d(short=True, lst=dc9x32[:8])
        for i in range(8):
            for j in range(32):
                print(f'[{i},{j}]: {dc9x32[i][j]}', end=' ')
            print("\n")


    # reverse odd columns
    for j in range(1, 64, 2):
        for i in range(4):
            temp = dc9x64[7 - i][j]
            dc9x64[7 - i][j] = dc9x64[i][j]
            dc9x64[i][j] = temp

    for j in range(1, 32, 2):
        for i in range(4):
            temp = dc9x32[7 - i][j]
            dc9x32[7 - i][j] = dc9x32[i][j]
            dc9x32[i][j] = temp
            if debug: print(f'[{i},{j}]: {dc9x32[i][j]}', end=' ')
        if debug: print("\n")

    return dc9x32, dc9x64


def get_dcdf(matrix_cols):
    dcdf = None
    dc9x32, dc9x64 = get_dc9x32x64()
    dc8x32 = dc9x32[:8]
    dc8x64 = dc9x64[:8]
    if debug:
        print_2d(True, dc9x32)

    if matrix_cols == 32:
        dcdf = dc8x32
    else:
        dcdf = dc8x64
    return dcdf


# Convert to masked

def get_masked_dcdf(matrix_cols):
    # 5,11, 17, 21, 29, 2, 8, 14,20,26,32
    # index starting 0, 4,10,16,20,28, 33, 39, 45, 51, 57, 63 
    masked = [4, 10, 16, 20, 28, 33, 39, 45, 51, 57, 63]
    if matrix_cols == 32:
        dcdf = get_masked_dc8x32(masked)
    else:
        dcdf = get_masked_dc8x64(masked)
    return dcdf

def get_masked_dc8x64(masked):
    """
    Remove masked columns from 8x64 matrix.
    Bitmap should not have data for masked columns, columns number should match after masked column count.
    64 columns in 8x64 matrix, 11 columns masked, 53 columns in masked matrix
    :param masked: List of column index to be removed
    :return: List of 8x64 matrix with masked columns removed
    """
    _, dc9x64 = get_dc9x32x64()
    masked_dc8x64 =[row.copy() for row in dc8x64]
    for j in masked:
        for row in masked_dc8x64:
            del row[j]  #
    return masked_dc8x64

def get_masked_dc8x32(masked):
    dc9x32, _ = get_dc9x32x64()
    masked_dc8x32 =[row.copy() for row in dc8x32]
    for j in masked:
        for row in masked_dc8x32:
            del row[j]  #
    return masked_dc8x32

"""
test_mask = [5, 11, 17, 22]
print_2d(short=True, lst=get_masked_dc8x64(test_mask))
print("original:")
print_2d(short=True, lst=dc9x64)
"""

"""
0 15 16 31 32
1 14 17 30 33
2 13 18 29 34
3 12 19 28 35
4 11 20 27 36
5 10 21 26 37
6 9 22 25 38
7 8 23 24 39 40
000 015 016 031 032 047 048 063 064 079 080 095 096 111 112 127 128 143 144 159 160 175 176 191 192 207 208 223 224 239 240 255 

001 014 017 030 033 046 049 062 065 078 081 094 097 110 113 126 129 142 145 158 161 174 177 190 193 206 209 222 225 238 241 254 

002 013 018 029 034 045 050 061 066 077 082 093 098 109 114 125 130 141 146 157 162 173 178 189 194 205 210 221 226 237 242 253 

003 012 019 028 035 044 051 060 067 076 083 092 099 108 115 124 131 140 147 156 163 172 179 188 195 204 211 220 227 236 243 252 

004 011 020 027 036 043 052 059 068 075 084 091 100 107 116 123 132 139 148 155 164 171 180 187 196 203 212 219 228 235 244 251 

005 010 021 026 037 042 053 058 069 074 085 090 101 106 117 122 133 138 149 154 165 170 181 186 197 202 213 218 229 234 245 250 

006 009 022 025 038 041 054 057 070 073 086 089 102 105 118 121 134 137 150 153 166 169 182 185 198 201 214 217 230 233 246 249 

007 008 023 024 039 040 055 056 071 072 087 088 103 104 119 120 135 136 151 152 167 168 183 184 199 200 215 216 231 232 247 248 

256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 
"""
