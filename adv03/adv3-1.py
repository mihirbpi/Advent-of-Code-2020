from aocd import get_data

map = get_data(year=2020,day=3).split("\n")
height = len(map)
width = len(map[0])

for i in range(0, height):
    map[i] = map[i][0:width]

x_pos = 0
symbol = ""
trees = 0

for i in range(0, height - 1):
    x_pos = (x_pos + 3) % width
    symbol = map[i + 1][x_pos]

    if(symbol == "#"):
        trees += 1

print(trees)
