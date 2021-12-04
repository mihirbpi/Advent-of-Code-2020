from aocd import get_data

my_list = get_data(year=2020,day=6).split("\n\n")

for i in range (0, len(my_list)):
    my_list[i] = my_list[i].replace("\n", "")

count = 0

for i in range (0, len(my_list)):
    string = my_list[i]
    questions = set()

    for j in range(0, len(string)):
        questions.add(string[j])

    count += len(questions)

print(count)
