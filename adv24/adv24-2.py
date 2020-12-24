from aocd import get_data
from collections import defaultdict
import copy

my_list = get_data(day=24).split("\n")

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

def update(black_tiles):

    new_black_tiles = set()
    neighbors_dict = defaultdict(lambda: 0)

    for tile in black_tiles:

        for delta in [[1, -3], [-1, -3], [1, 3], [-1, 3], [2, 0], [-2, 0]]:
            neighbors_dict[(tile[0] + delta[0], tile[1] + delta[1])] += 1

    for tile in neighbors_dict:

        if(tile in black_tiles and neighbors_dict[tile] <= 2):
           new_black_tiles.add(tile)

        if(tile not in black_tiles and neighbors_dict[tile] == 2):
            new_black_tiles.add(tile)

    return new_black_tiles

black_tiles = set()

for i in range(0, len(my_list)):

    instruction = my_list[i]
    tile = instruction_to_tile(instruction)

    if(tile in black_tiles):
        black_tiles.remove(tile)

    else:
        black_tiles.add(tile)

for day in range(0, 100):

    black_tiles = update(black_tiles)

print(len(black_tiles))
