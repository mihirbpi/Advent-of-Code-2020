import copy
import itertools
import math
from aocd import get_data

my_list = get_data(day=20).split("\n\n")
tiles_dict = {}

for i in range(0, len(my_list)):
    tile_string = my_list[i]
    rows = tile_string.strip("\n").split("\n")
    id = int(rows[0].strip(":").split(" ")[1])
    rows.pop(0)
    tile = rows
    tiles_dict[id] = tile

size = math.isqrt(len(tiles_dict.keys()))

def column(tile, i):
    col = ""

    for j in reversed(range(0, len(tile))):
        col += tile[j][i]

    return col

def inner_tile(tile):
    inner = []

    for i in range(1, len(tile) - 1):
        inner.append(tile[i][1:len(tile[i])-1])
    return inner

def printtile(tile):
    for row in tile:
        print(row + "\n")
    print("\n\n")

def identity(tile):
    return copy.deepcopy(tile)

def identity_edge_list(edge_list):
    return copy.deepcopy(edge_list)

def rotate90(tile):
    result = []
    tile_copy =  copy.deepcopy(tile)

    for i in range(0, len(tile_copy[0])):
        result.append(column(tile_copy, i))

    return result

def rotate90_edge_list(edge_list):
    list_copy =  copy.deepcopy(edge_list)
    list_copy[1] = edge_list[0]
    list_copy[2] = edge_list[1]
    list_copy[3] = edge_list[2]
    list_copy[0] = edge_list[3]

    return list_copy

def rotate180(tile):
    return rotate90(rotate90(tile))

def rotate180_edge_list(tile):
    return rotate90_edge_list(rotate90_edge_list(tile))

def rotate270(tile):
    return rotate90(rotate90(rotate90(tile)))

def rotate270_edge_list(tile):
    return rotate90_edge_list(rotate90_edge_list(rotate90_edge_list(tile)))

def flip_vert(tile):
    tile_copy =  copy.deepcopy(tile)
    result = []

    for i in range(0, len(tile_copy)):
        result.append(tile_copy[i][::-1])

    return result

def flip_vert_edge_list(edge_list):
    list_copy =  copy.deepcopy(edge_list)
    list_copy[1] = edge_list[3]
    list_copy[3] = edge_list[1]

    return list_copy

def flipv_r90(tile):
    return rotate90(flip_vert(tile))

def flipv_r90_edge_list(edge_list):
    return rotate90_edge_list(flip_vert_edge_list(edge_list))

def flipv_r180(tile):
    return rotate180(flip_vert(tile))

def flipv_r180_edge_list(edge_list):
    return rotate180_edge_list(flip_vert_edge_list(edge_list))

def flipv_r270(tile):
    return rotate270(flip_vert(tile))

def flipv_r270_edge_list(edge_list):
    return rotate270_edge_list(flip_vert_edge_list(edge_list))

def num_neighbors(id):
    edge_matching_ids = tiles_to_edge_matching_ids_dict[id]
    count = 0

    for i in range(0, len(edge_matching_ids)):

        if(len(edge_matching_ids[i]) > 0):
            count += 1

    return count

def does_match(edge_list, id_top, id_right, id_bottom, id_left):

    top_list, right_list, bottom_list, left_list = edge_list
    top_match = ((id_top == 0 and len(top_list) == 0) or (id_top in top_list))
    right_match = ((id_right == 0 and len(right_list) == 0) or (id_right in right_list))
    bottom_match = ((id_bottom == 0 and len(bottom_list) == 0) or (id_bottom in bottom_list))
    left_match = ((id_left == 0 and len(left_list) == 0) or (id_left in left_list))

    return top_match and right_match and bottom_match and left_match

def valid_sea_monster(i, j, image):
    b1 = image[i][j + 18] == "#"
    b2 = image[i + 1][j] == "#" and image[i + 1][j + 5] == "#" and image[i + 1][j + 6] == "#"
    b3 = image[i + 1][j + 11] == "#" and image[i + 1][j + 12] == "#" and image[i + 1][j + 17] == "#"
    b4 = image[i + 1][j + 18] == "#" and image[i + 1][j + 19] == "#" and image[i + 2][j + 1] == "#"
    b5 = image[i + 2][j + 4] == "#" and image[i + 2][j + 7] == "#" and image[i + 2][j + 10] == "#"
    b6 = image[i + 2][j + 13] == "#" and image[i + 2][j + 16] == "#"

    return b1 and b2 and b3 and b4 and b5 and b6

def is_sea_monster(i, j, image):

    if(i >= len(image) or j >= len(image[0]) or i + 2 >= len(image) or j + 19 >= len(image[0])):
        return False

    else:
        return valid_sea_monster(i, j, image)

def num_sea_monsters(image):

    count = 0

    for i in range(0, len(image)):

        for j in range(0, len(image[0])):

            if(is_sea_monster(i, j, image)):
                count += 1

    return count

def roughness(image):
    num_sea_mons = num_sea_monsters(image)
    hash_count = 0

    for i in range(0, len(image)):

        for j in range(0, len(image[0])):

            if(image[i][j] == "#"):
                hash_count += 1

    return hash_count - 15 * num_sea_mons

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

grid = [[None for i in range(0, size)] for j in range(0, size)]

used_ids = []
grid[0][0] = corner_ids[0]
used_ids.append(corner_ids[0])
current = [0, 0]

# Solve first row
for i in range(1, size):

    for id in tiles_to_edge_matching_ids_dict:
        current_id = grid[current[0]][current[1]]
        non_empty_list = []

        for l in tiles_to_edge_matching_ids_dict[current_id]:

            if(len(l) > 0):
                non_empty_list.append(l)

        ids = []

        for l in non_empty_list:

            for idd in l:
                ids.append(idd)


        if(id not in used_ids and id in ids and (num_neighbors(id) == 3 or num_neighbors(id) == 2) ):

            if(current[1] + 1 < size):

                grid[current[0]][current[1] + 1] = id
                current[1] += 1
                used_ids.append(id)
                break

# Solve other rows
current = [0, 0]

for i in range(0, size):

    for j in range(0, size):

        for id in tiles_to_edge_matching_ids_dict:

            current_id = grid[current[0]][current[1]]
            non_empty_list = []

            for l in tiles_to_edge_matching_ids_dict[current_id]:

                if(len(l) > 0):
                    non_empty_list.append(l)

            ids = []

            for l in non_empty_list:

                for idd in l:
                    ids.append(idd)

            if(id not in used_ids and id in ids and (num_neighbors(id) == 3 or num_neighbors(id) == 2 or num_neighbors(id) == 4) ):

                if(current[0] + 1 < size and current[1] < size):
                    grid[current[0] + 1][current[1]] = id
                    current[1] += 1
                    used_ids.append(id)
                    break

    current[0] += 1
    current[1] = 0

for i in range(0, len(grid)):

    for j in range(0, len(grid)):
        id = grid[i][j]
        edge_list = tiles_to_edge_matching_ids_dict[id]
        top_id = 0
        right_id = 0
        bottom_id = 0
        left_id = 0

        if(i - 1 >= 0):
            top_id = grid[i - 1][j]

        if(i + 1 <= len(grid) - 1):
            bottom_id = grid[i + 1][j]

        if(j - 1 >= 0):
            left_id = grid[i][j - 1]

        if(j + 1 <= len(grid) - 1):
            right_id = grid[i][j + 1]

        if(does_match(identity_edge_list(edge_list), top_id, right_id, bottom_id, left_id)):
            tiles_dict[id] = identity(tiles_dict[id])

        elif(does_match(rotate90_edge_list(edge_list), top_id, right_id, bottom_id, left_id)):
            tiles_dict[id] = rotate90(tiles_dict[id])

        elif(does_match(rotate180_edge_list(edge_list), top_id, right_id, bottom_id, left_id)):
            tiles_dict[id] = rotate180(tiles_dict[id])

        elif(does_match(rotate270_edge_list(edge_list), top_id, right_id, bottom_id, left_id)):
            tiles_dict[id] = rotate270(tiles_dict[id])

        elif(does_match(flip_vert_edge_list(edge_list), top_id, right_id, bottom_id, left_id)):
            tiles_dict[id] = flip_vert(tiles_dict[id])

        elif(does_match(flipv_r90_edge_list(edge_list), top_id, right_id, bottom_id, left_id)):
            tiles_dict[id] = flipv_r90(tiles_dict[id])

        elif(does_match(flipv_r180_edge_list(edge_list), top_id, right_id, bottom_id, left_id)):
            tiles_dict[id] = flipv_r180(tiles_dict[id])

        elif(does_match(flipv_r270_edge_list(edge_list), top_id, right_id, bottom_id, left_id)):
            tiles_dict[id] = flipv_r270(tiles_dict[id])


image = [[None] for i in range(0, 8 * size)]

for i in range(0, 8 * size):
    k = abs(i % 8)
    n = int((i - k) / 8)
    str = ""

    for j in range(0, size):
        str += inner_tile(tiles_dict[grid[n][j]])[k]

    image[i] = str

if(num_sea_monsters(identity(image)) > 0):
    print(roughness(identity(image)))

elif(num_sea_monsters(rotate90(image)) > 0):
    print(roughness(rotate90(image)))

elif(num_sea_monsters(rotate180(image)) > 0):
    print(roughness(rotate180(image)))

elif(num_sea_monsters(rotate270(image)) > 0):
    print(roughness(rotate270(image)))

elif(num_sea_monsters(flip_vert(image)) > 0):
    print(roughness(flip_vert(image)))

elif(num_sea_monsters(flipv_r90(image)) > 0):
    print(roughness(flipv_r90(image)))

elif(num_sea_monsters(flipv_r180(image)) > 0):
    print(roughness(flipv_r180(image)))

elif(num_sea_monsters(flipv_r270(image)) > 0):
    print(roughness(flipv_r270(image)))
