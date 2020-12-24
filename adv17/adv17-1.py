from collections import defaultdict
import copy
from aocd import get_data

my_list = get_data(day=17).split("\n")
conway_dict = set()

for x in range(0, len(my_list)):
    string = my_list[x]

    for y in range(0, len(string)):

        if(string[y] == "#"):
            conway_dict.add((x, y, 0))

def update(conway_dict):
    new_conway_dict = set()
    neighbors_dict = defaultdict(lambda: 0)

    for coordinates in conway_dict:
        x = coordinates[0]
        y = coordinates[1]
        z = coordinates[2]

        for dx in [-1, 0, 1]:

            for dy in [-1, 0, 1]:

                for dz in [-1, 0, 1]:

                    if((dx, dy, dz) != (0, 0, 0)):
                        neighbors_dict[(x + dx, y + dy, z + dz)] += 1

    for coordinates in neighbors_dict:

        if(coordinates in conway_dict and (neighbors_dict[coordinates] == 3 or neighbors_dict[coordinates] == 2)):
            new_conway_dict.add(coordinates)

        elif(coordinates not in conway_dict and neighbors_dict[coordinates] == 3):
            new_conway_dict.add(coordinates)

    return new_conway_dict

for cycle in range(0, 6):
    result = update(conway_dict)
    conway_dict = result

print(len(conway_dict))
