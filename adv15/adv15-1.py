from aocd import get_data

my_list = list(map(int, get_data(year=2020,day=15).split("\n")[0].split(",")))
dict = {}

for i in range(0, len(my_list)):
    dict[my_list[i]] = [i + 1]

last_number = my_list[len(my_list) - 1]

for turn in range(len(my_list) + 1, 2021):

    if(last_number in dict.keys() and len(dict[last_number]) == 1):
        last_number = 0
        dict[0].append(turn)

    elif(last_number in dict.keys() and len(dict[last_number]) > 1):
        last_number = dict[last_number][len(dict[last_number]) - 1] - dict[last_number][len(dict[last_number]) - 2]

        if(last_number in dict.keys()):
            dict[last_number].append(turn)

        else:
            dict[last_number] = [turn]

    elif(last_number not in dict.keys()):
        dict[last_number] = [turn]
        last_number = 0

print(last_number)
