from aocd import get_data

list = get_data(year=2020,day=1).split("\n")

for i in range (0,len(list)):
    list[i] = int(list[i][0:len(list[i])])

for i in range(0, len(list)):
    element1 = list[i]

    for j in range(i+1, len(list)):
        element2 = list[j]

        for k in range(j+1, len(list)):
            element3 = list[k]

            if(element1 + element2 + element3 == 2020):
                assert(element1 + element2 + element3 == 2020)
                print(element1 * element2 * element3)
