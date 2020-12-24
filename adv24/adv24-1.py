from aocd import get_data
from collections import defaultdict

my_list = get_data(day=24).split("\n")

tile_color_dict = defaultdict(lambda: 1)

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

for i in range(0, len(my_list)):
    instruction = my_list[i]
    tile = instruction_to_tile(instruction)

    if(tile in tile_color_dict.keys()):
        tile_color_dict[tile] *= -1

    else:
        tile_color_dict[tile] = -1

black_tile_count = 0

for tile in tile_color_dict.keys():

    if(tile_color_dict[tile] == -1):
        black_tile_count += 1

print(black_tile_count)
