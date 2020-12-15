from aocd import get_data

my_list = list(map(int, get_data(day=15).split("\n")[0].split(",")))

dict = {}

for i in range(0, len(my_list)):
    dict[my_list[i]] = i + 1

last_number_spoken = my_list[len(my_list) - 1]

for turn in range(len(my_list), 30000000):

    if(last_number_spoken not in dict.keys()):
        dict[last_number_spoken] = turn
        last_number_spoken = 0

    else:
        to_speak = turn - dict[last_number_spoken]
        dict[last_number_spoken] = turn
        last_number_spoken = to_speak

print(last_number_spoken)
