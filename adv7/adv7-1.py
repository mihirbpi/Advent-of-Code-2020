from aocd import get_data

my_list = get_data(day=7).split(".\n")[:-1]
bag_dict = {}

for i in range(0, len(my_list)):
    string = my_list[i]
    parent_bag = string.split("contain")[0].strip()[:-1]
    rest = string.split("contain")[1].strip().split(", ")

    if(rest[0] == "no other bags"):
        rest = []

    for j in range(0, len(rest)):
        rest[j] = rest[j].strip("s")

        if(rest[j].split(" ")[0].isnumeric()):
            rest[j] = rest[j][2:]

    bag_dict[parent_bag] = rest



def contains_gold(bag_name):

    if(bag_name in bag_dict.keys()):

        if("shiny gold bag" in bag_dict[bag_name]):
            return True

        for bag in bag_dict[bag_name]:
            if(contains_gold(bag) ==  True):
                return True
        return False

    return False

count = 0

for bag in bag_dict.keys():

    if(contains_gold(bag)):
        count += 1

print(count)
