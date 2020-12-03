file = open("adv3-2_input.txt")
map = file.readlines()
height = len(map)
width = len(map[0]) - 1

for i in range(0, height):
    map[i] = map[i][0:width]

def num_trees(right, down):
    x_pos = 0
    symbol = ""
    trees = 0

    for i in range(0, height - down, down):
        x_pos = (x_pos + right) % width
        symbol = map[i + down][x_pos]

        if(symbol == "#"):
            trees += 1

    return trees

print(num_trees(1,1) * num_trees(3,1) * num_trees(5,1) * num_trees(7,1) * num_trees(1,2))
