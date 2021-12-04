from aocd import get_data

my_list = get_data(year=2020,day=6).split("\n\n")

for i in range (0, len(my_list)):
    my_list[i] = my_list[i].split("\n")

count = 0

for i in range (0, len(my_list)):
    strings = my_list[i]
    set_list = []

    for j in range(0, len(strings)):
        string = strings[j]
        question_set = set()

        for k in range(0, len(string)):
            question_set.add(string[k])

        set_list.append(question_set)

    count += len(set.intersection(*set_list))

print(count)
