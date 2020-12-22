import copy
import itertools
import math
from aocd import get_data

my_list = get_data(day=20).split("\n\n")
size = math.isqrt(len(my_list))

tiles_dict = {}

for i in range(0, len(my_list)):
    tile_string = my_list[i]
    rows = tile_string.strip("\n").split("\n")
    id = int(rows[0].strip(":").split(" ")[1])
    rows.pop(0)
    tile = rows
    tiles_dict[id] = tile

def column(tile, i):
    col = ""

    for j in reversed(range(0, len(tile))):
        col += tile[j][i]

    return col

def num_neighbors(id):
    edge_matching_ids = tiles_to_edge_matching_ids_dict[id]
    count = 0

    for i in range(0, len(edge_matching_ids)):

        if(len(edge_matching_ids[i]) > 0):
            count += 1

    return count

tiles_to_edge_list_dict = {}

for id in tiles_dict.keys():
    tile = tiles_dict[id]
    top = tile[0]
    bottom = tile[len(tile) - 1]
    left = column(tile, 0)
    right = column(tile, len(tile) - 1)
    edge_list = [top, right, bottom, left]
    tiles_to_edge_list_dict[id] = edge_list

tiles_to_edge_matching_ids_dict = {}

for id in tiles_to_edge_list_dict:
    matching_ids_list = [[], [], [], []]
    edge_list = tiles_to_edge_list_dict[id]
    top, right, bottom, left = edge_list

    for other_id in tiles_to_edge_list_dict:

        if(other_id != id):
            other_edge_list = tiles_to_edge_list_dict[other_id]

            for other_edge in other_edge_list:

                if(other_edge == top or other_edge[::-1] == top or other_edge == top[::-1] or other_edge[::-1] == top[::-1]):
                    matching_ids_list[0].append(other_id)

                if(other_edge == right or other_edge[::-1] == right or other_edge == right[::-1] or other_edge[::-1] == right[::-1]):
                    matching_ids_list[1].append(other_id)

                if(other_edge == bottom or other_edge[::-1] == bottom or other_edge == bottom[::-1] or other_edge[::-1] == bottom[::-1]):
                    matching_ids_list[2].append(other_id)

                if(other_edge == left or other_edge[::-1] == left or other_edge == left[::-1] or other_edge[::-1] == left[::-1]):
                    matching_ids_list[3].append(other_id)

    tiles_to_edge_matching_ids_dict[id] = matching_ids_list

corner_ids = []

for id in tiles_to_edge_matching_ids_dict:
    edge_matching_ids = tiles_to_edge_matching_ids_dict[id]

    for i in range(0, len(edge_matching_ids)):

        if(num_neighbors(id) == 2 and len(edge_matching_ids[i]) == 0 and len(edge_matching_ids[(i + 1) % 4]) == 0):
            corner_ids.append(id)
            break

print(math.prod(corner_ids))
