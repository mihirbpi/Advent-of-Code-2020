from aocd import get_data

adapter_list = list(map(int, get_data(day=10).split("\n")))

def num_arrangements(joltage, dict):

    if(joltage in dict.keys()):
        return dict[joltage]

    if(joltage == 1):
        dict[1] = 1
        return 1

    if(joltage == 2 or joltage == 3):
        num = 1

        for i in range (0, len(adapter_list)):

            if(joltage - adapter_list[i] in [1, 2, 3]):
                num += num_arrangements(adapter_list[i], dict)

        dict[joltage] = num
        return num

    else:
        num = 0

        for i in range (0, len(adapter_list)):

            if(joltage - adapter_list[i] in [1, 2, 3]):
                num += num_arrangements(adapter_list[i], dict)

        dict[joltage] = num
        return num

dict = {}
print(num_arrangements(max(adapter_list) + 3, dict))
