file = open("adv2-1_input.txt")
list = file.readlines()

valid_strings = 0

for i in range (0, len(list)):
    list[i] = list[i][0:len(list[i])-1]
    numbers = list[i].split(" ")[0]
    letter = list[i].split(" ")[1].split(":")[0]
    string = list[i].split(" ")[2]
    min_count = int(numbers.split("-")[0])
    max_count = int(numbers.split("-")[1])
    count = 0

    for j in range(0, len(string)):

        if (string[j] == letter):
            count += 1

    if(count >= min_count and count <= max_count):
        valid_strings += 1

print(valid_strings)
