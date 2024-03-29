from aocd import get_data

list = get_data(year=2020,day=2).split("\n")
valid_strings = 0

for i in range (0, len(list)):
    list[i] = list[i][0:len(list[i])]
    numbers = list[i].split(" ")[0]
    letter = list[i].split(" ")[1].split(":")[0]
    string = list[i].split(" ")[2]
    pos1 = int(numbers.split("-")[0]) - 1
    pos2 = int(numbers.split("-")[1]) - 1

    if( (string[pos1] == letter) ^ (string[pos2] == letter) ):
        valid_strings += 1

print(valid_strings)
