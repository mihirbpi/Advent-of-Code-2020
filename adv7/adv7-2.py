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
            rest[j] = (int(rest[j].split(" ")[0]), rest[j][2:])

    bag_dict[parent_bag] = rest


def num_bags_inside(bag_name):
    num_bags = 0

    if(bag_name in bag_dict.keys()):

        if(bag_dict[bag_name] == []):
            return 0

        for bag_tuple in bag_dict[bag_name]:
            num_bags += bag_tuple[0] + bag_tuple[0] * num_bags_inside(bag_tuple[1])

    return num_bags

print(num_bags_inside("shiny gold bag"))
