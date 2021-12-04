from aocd import get_data

my_list = get_data(year=2020,day=7).split(".\n")[:-1]
bag_dict = {}

for i in range(0, len(my_list)):
    string = my_list[i]
    parent_bag = string.split("contain")[0].strip()[:-1]
    inner_bags = string.split("contain")[1].strip().split(", ")

    if(inner_bags[0] == "no other bags"):
        inner_bags = []

    for j in range(0, len(inner_bags)):
        inner_bags[j] = inner_bags[j].strip("s")

        if(inner_bags[j].split(" ")[0].isnumeric()):
            inner_bags[j] = inner_bags[j][2:]

    bag_dict[parent_bag] = inner_bags


def contains_gold(bag):

    if(bag in bag_dict.keys()):

        if("shiny gold bag" in bag_dict[bag]):
            return True

        for inner_bag in bag_dict[bag]:

            if(contains_gold(inner_bag) ==  True):
                return True
        return False

    return False

count = 0

for bag in bag_dict.keys():

    if(contains_gold(bag)):
        count += 1

print(count)
