from enum import Enum


floor = ['a', 'a', 'b', 'a', 'b', 'd', 'c', 'd']

floor2 = ['d', 'a', 'a', 'a', 'a', 'c', 'c', 'a']



def value_to_tile(value):
    res = 'a'
    if value == 1:
        res = 'b'
    if value == 2:
        res = 'c'
    if value == 3:
        res = 'd'
    return res


def tile_to_value(tile):
    res = 0
    if tile == 'b':
        res = 1
    if tile == 'c':
        res = 2
    if tile == 'd':
        res = 3
    return res


def tile_add(tile, x):
    res = (tile_to_value(tile) + x) % 4
    return value_to_tile(res)


def tile_sub(tile, x):
    res = (tile_to_value(tile) + 4 - x) % 4
    return value_to_tile(res)


def rotate_90(floor):
    sym = ['', '', '', '', '', '', '', '']
    for i in range(0, len(floor)):
        sym[(i + 2) % 8] = floor[i]
    for i in range(0, len(sym)):
        if sym[i] == 'a' or sym[i] == 'b':
            sym[i] = tile_add(sym[i], 2)
        elif sym[i] == 'c':
            sym[i] = tile_sub(sym[i], 1)
        elif sym[i] == 'd':
            sym[i] = tile_add(sym[i], 1)
    return sym



def rotate_180(floor):
    return rotate_90(rotate_90(floor))


def rotate_270(floor):
    return rotate_90(rotate_180(floor))


def horizontal(floor):
    sym = ['', '', '', '', '', '', '', '']
    for i in range(0, len(floor)):
        if i == 0 or i == 4:
            sym[i] = floor[i]
        elif i == 1:
            sym[7] = floor[i]
        elif i == 2:
            sym[6] = floor[i]
        elif i == 3:
            sym[5] = floor[i]
        elif i == 5:
            sym[3] = floor[i]
        elif i == 6:
            sym[2] = floor[i]
        elif i == 7:
            sym[1] = floor[i]
    for i in range(0, len(sym)):
        sym[i] = tile_add(sym[i], 2)
    return sym


def vertical(floor):
    sym = ['', '', '', '', '', '', '', '']
    for i in range(0, len(floor)):
        if i == 6 or i == 2:
            sym[i] = floor[i]
        elif i == 0:
            sym[4] = floor[i]
        elif i == 1:
            sym[3] = floor[i]
        elif i == 3:
            sym[1] = floor[i]
        elif i == 4:
            sym[0] = floor[i]
        elif i == 5:
            sym[7] = floor[i]
        elif i == 7:
            sym[5] = floor[i]
    for i in range(0, len(sym)):
        if sym[i] == 'a' or sym[i] == 'c':
            sym[i] = tile_add(sym[i], 1)
        elif sym[i] == 'b' or sym[i] == 'd':
            sym[i] = tile_sub(sym[i], 1)
    return sym


def diagonal_a(floor):
    sym = ['', '', '', '', '', '', '', '']
    for i in range(0, len(floor)):
        if i == 1 or i == 5:
            sym[i] = floor[i]
        elif i == 0:
            sym[2] = floor[i]
        elif i == 2:
            sym[0] = floor[i]
        elif i == 3:
            sym[7] = floor[i]
        elif i == 4:
            sym[6] = floor[i]
        elif i == 6:
            sym[4] = floor[i]
        elif i == 7:
            sym[3] = floor[i]
    for i in range(0, len(sym)):
        if sym[i] == 'a':
            sym[i] = tile_add(sym[i], 1)
        elif sym[i] == 'b':
            sym[i] = tile_sub(sym[i], 1)
    return sym


def diagonal_b(floor):
    sym = ['', '', '', '', '', '', '', '']
    for i in range(0, len(floor)):
        if i == 3 or i == 7:
            sym[i] = floor[i]
        elif i == 0:
            sym[6] = floor[i]
        elif i == 1:
            sym[5] = floor[i]
        elif i == 2:
            sym[4] = floor[i]
        elif i == 4:
            sym[2] = floor[i]
        elif i == 5:
            sym[1] = floor[i]
        elif i == 6:
            sym[0] = floor[i]
    for i in range(0, len(sym)):
        if sym[i] == 'c':
            sym[i] = tile_add(sym[i], 1)
        elif sym[i] == 'd':
            sym[i] = tile_sub(sym[i], 1)
    return sym


def check_all_symmetries(known_floors, new_floor):
    result = True \
        & rotate_90 not in known_floors \
        & rotate_180 not in known_floors \
        & rotate_270 not in known_floors
    return result

print(floor2)
print(rotate_90(floor2))
print(rotate_180(floor2))
print(rotate_270(floor2))
print(rotate_180(rotate_180(floor2)))
print(horizontal(floor2))
print(vertical(floor2))
print(diagonal_a(floor2))
print(diagonal_b(floor2))