from aocd import get_data
from collections import defaultdict
import copy

my_list = get_data(year=2020,day=24).split("\n")

tile_color_dict = defaultdict(lambda: [1, 0])

def instruction_to_tile(instruction):
    current_tile = [0, 0]
    i = 0

    while(i < len(instruction)):

        if(i + 1 < len(instruction) and instruction[i:i+2] == "se"):
            current_tile[0] += 1
            current_tile[1] -= 3
            i += 2

        elif(i + 1 < len(instruction) and instruction[i:i+2] == "sw"):
            current_tile[0] -= 1
            current_tile[1] -= 3
            i += 2

        elif(i + 1 < len(instruction) and instruction[i:i+2] == "ne"):
            current_tile[0] += 1
            current_tile[1] += 3
            i += 2

        elif(i + 1 < len(instruction) and instruction[i:i+2] == "nw"):
            current_tile[0] -= 1
            current_tile[1] += 3
            i += 2

        elif(instruction[i] == "e"):
            current_tile[0] += 2
            i += 1

        elif(instruction[i] == "w"):
            current_tile[0] -= 2
            i += 1

    return tuple(current_tile)

def neighbors_count(tile_color_dict, tile):

    count = 0

    for delta in [[1, -3], [-1, -3], [1, 3], [-1, 3], [2, 0], [-2, 0]]:

        if(tile_color_dict[(tile[0] + delta[0], tile[1] + delta[1])][0] == -1):
            count += 1

    return count

def update_neighbors(tile_color_dict):

    new_tile_color_dict = copy.deepcopy(tile_color_dict)
    tiles = copy.deepcopy(list(tile_color_dict.keys()))

    for tile in tiles:

        new_tile_color_dict[tile][1] = neighbors_count(tile_color_dict, tile)

    return new_tile_color_dict

def update(tile_color_dict):

    new_tile_color_dict = copy.deepcopy(tile_color_dict)
    tiles = copy.deepcopy(list(tile_color_dict.keys()))

    for tile in tiles:

        if(tile_color_dict[tile][0] == -1):

            if(neighbors_count(tile_color_dict, tile) == 0 or neighbors_count(tile_color_dict, tile) > 2):

                if(tile in new_tile_color_dict):
                    new_tile_color_dict.pop(tile)

        elif(tile_color_dict[tile][0] == 1):

            if(neighbors_count(tile_color_dict, tile) == 2):
                new_tile_color_dict[tile][0] = -1
                new_tile_color_dict[tile][1] = 2

        for delta in [[1, -3], [-1, -3], [1, 3], [-1, 3], [2, 0], [-2, 0]]:
            adjacent_tile = (tile[0] + delta[0], tile[1] + delta[1])

            if(tile_color_dict[adjacent_tile][0] == -1):

                if(neighbors_count(tile_color_dict, adjacent_tile) == 0 or neighbors_count(tile_color_dict, adjacent_tile) > 2):

                    if(adjacent_tile in new_tile_color_dict):
                        new_tile_color_dict.pop(adjacent_tile)

            elif(tile_color_dict[adjacent_tile][0] == 1):

                if(neighbors_count(tile_color_dict, adjacent_tile) == 2):
                    new_tile_color_dict[adjacent_tile][0] = -1
                    new_tile_color_dict[adjacent_tile][1] = 2

    return new_tile_color_dict

for i in range(0, len(my_list)):
    instruction = my_list[i]
    tile = instruction_to_tile(instruction)
    tile_color_dict[tile][0] *= -1

for day in range(0, 100):
    tile_color_dict = update_neighbors(tile_color_dict)
    tile_color_dict = update(tile_color_dict)

black_tile_count = 0

for tile in tile_color_dict:

    if(tile_color_dict[tile][0] == -1):
        black_tile_count += 1

print(black_tile_count)
