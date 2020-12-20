import copy
import itertools
import math

file = open("input.txt", "r")

my_list = file.read().split("\n\n")

tiles_dict = {}

for i in range(0, len(my_list)):
    tile_string = my_list[i]
    rows = tile_string.strip("\n").split("\n")
    id = int(rows[0].strip(":").split(" ")[1])
    rows.pop(0)
    tile = rows
    tiles_dict[id] = tile

def printtile(tile):

    for i in range(0, len(tile)):
        print(tile[i] + "\n")

def column(tile, i):
    col = ""

    for j in reversed(range(0, len(tile))):
        col += tile[j][i]

    return col

def identity(tile):
    return copy.deepcopy(tile)

def rotate90(tile):
    result = []
    tile_copy =  copy.deepcopy(tile)

    for i in range(0, len(tile_copy[0])):
        result.append(column(tile_copy, i))

    return result


def rotate180(tile):
    return rotate90(rotate90(tile))

def rotate270(tile):
    return rotate90(rotate90(rotate90(tile)))

def flip_horiz(tile):
    tile_copy =  copy.deepcopy(tile)
    result = [""]*len(tile_copy)

    for i in range(0, len(tile_copy[0])):
        toreplace = column(tile_copy, i)

        for j in range(0, len(tile_copy)):
            result[j] += toreplace[j]

    return result

def flip_vert(tile):
    tile_copy =  copy.deepcopy(tile)
    result = []

    for i in range(0, len(tile_copy)):
        result.append(tile_copy[i][::-1])

    return result

all_tiles_list = []

for id in tiles_dict.keys():
    tile = tiles_dict[id]
    all_tiles_list.append((identity(tile), id))
    all_tiles_list.append((rotate90(tile), id))
    all_tiles_list.append((rotate180(tile), id))
    all_tiles_list.append((rotate270(tile), id))
    all_tiles_list.append((flip_vert(tile), id))
    all_tiles_list.append((flip_horiz(tile), id))


def num_match_top(tile, tile_id):
    count = 0
    keys = list(tiles_dict.keys())
    remove = [x for x in keys if x != tile_id]

    for id in remove:

        tile_check = tiles_dict[id]
        rotations = []
        rotations.append(identity(tile_check))
        rotations.append(rotate90(tile_check))
        rotations.append(rotate180(tile_check))
        rotations.append(rotate270(tile_check))
        rotations.append(flip_vert(tile_check))
        rotations.append(flip_horiz(tile_check))

        for t_c in rotations:

            if(tile[0] == t_c[len(t_c) - 1]):
                count += 1

    return count


def num_match_bottom(tile, tile_id):
    count = 0
    keys = list(tiles_dict.keys())
    remove = [x for x in keys if x != tile_id]

    for id in remove:

        tile_check = tiles_dict[id]
        rotations = []
        rotations.append(identity(tile_check))
        rotations.append(rotate90(tile_check))
        rotations.append(rotate180(tile_check))
        rotations.append(rotate270(tile_check))
        rotations.append(flip_vert(tile_check))
        rotations.append(flip_horiz(tile_check))

        for t_c in rotations:

            if(tile[len(tile) - 1] == t_c[0]):
                count += 1

    return count

def num_match_right(tile, tile_id):
    count = 0
    keys = list(tiles_dict.keys())
    remove = [x for x in keys if x != tile_id]

    for id in remove:

        tile_check = tiles_dict[id]
        rotations = []
        rotations.append(identity(tile_check))
        rotations.append(rotate90(tile_check))
        rotations.append(rotate180(tile_check))
        rotations.append(rotate270(tile_check))
        rotations.append(flip_vert(tile_check))
        rotations.append(flip_horiz(tile_check))

        for t_c in rotations:

            if(column(tile, len(tile[0]) - 1) == column(t_c, 0)):
                count += 1

    return count


def num_match_left(tile, tile_id):
    count = 0
    keys = list(tiles_dict.keys())
    remove = [x for x in keys if x != tile_id]

    for id in remove:

        tile_check = tiles_dict[id]
        rotations = []
        rotations.append(identity(tile_check))
        rotations.append(rotate90(tile_check))
        rotations.append(rotate180(tile_check))
        rotations.append(rotate270(tile_check))
        rotations.append(flip_vert(tile_check))
        rotations.append(flip_horiz(tile_check))

        for t_c in rotations:

            if(column(tile, 0) == column(t_c, len(t_c[0]) - 1)):
                count += 1

    return count

s = set()

for tup in all_tiles_list:

    if(num_match_top(*tup) == 0 and num_match_right(*tup) == 1 and num_match_left(*tup) == 0 and num_match_bottom(*tup) == 1):
        s.add(tup[1])

print(math.prod(s))
