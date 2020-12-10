from aocd import get_data

adapter_list = list(map(int, get_data(day=10).split("\n")))

def check_adapters(adapter):
    choices = []

    for i in range(0, len(adapter_list)):
        adap = adapter_list[i]

        if(adap != adapter and adap - adapter in [1, 2, 3]):
            choices.append(adap)

    if(len(choices) > 0):

        if(min(choices) - adapter == 1):
            diff_one.add(min(choices))

        elif(min(choices) - adapter == 2):
            diff_two.add(min(choices))

        elif(min(choices) - adapter == 3):
            diff_three.add(min(choices))

        check_adapters(min(choices))

adapter_list.sort()
diff_one = set()
diff_two = set()
diff_three = set()
diff_three.add(max(adapter_list) + 3)

if(1 in adapter_list):
    diff_one.add(1)
    check_adapters(1)

if(2 in adapter_list and 2 not in diff_one):
    diff_two.add(2)
    check_adapters(2)

if(3 in adapter_list and 3 not in set.union(diff_one, diff_two)):
    diff_three.add(3)
    check_adapters(3)

print(len(diff_one) * len(diff_three))
