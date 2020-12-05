from aocd import get_data

list = get_data(day=1).split("\n")

for i in range (0,len(list)):
    list[i] = int(list[i][0:len(list[i])])

for i in range(0, len(list)):
    element1 = list[i]

    for j in range(i+1, len(list)):
        element2 = list[j]

        if(element1 + element2 == 2020):
            assert(element1 + element2 == 2020)
            print(element1 * element2)
