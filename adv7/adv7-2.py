from aocd import get_data

my_list = get_data(day=7).split(".\n")[:-1]
bag_dict = {}

for i in range(0, len(my_list)):
    string = my_list[i]
    parent_bag = string.split("contain")[0].strip()[:-1]
    inner_bags_info = string.split("contain")[1].strip().split(", ")

    if(inner_bags_info[0] == "no other bags"):
        inner_bags_info = []

    for j in range(0, len(inner_bags_info)):
        inner_bags_info[j] = inner_bags_info[j].strip("s")

        if(inner_bags_info[j].split(" ")[0].isnumeric()):
            inner_bags_info[j] = (int(inner_bags_info[j].split(" ")[0]), inner_bags_info[j][2:])

    bag_dict[parent_bag] = inner_bags_info


def num_bags_inside(bag):
    num_bags = 0

    if(bag in bag_dict.keys()):

        if(bag_dict[bag] == []):
            return 0

        for inner_bag_info in bag_dict[bag]:
            inner_bag = inner_bag_info[1]
            num_inner_bag = inner_bag_info[0]
            num_bags += num_inner_bag * (1 + num_bags_inside(inner_bag))

    return num_bags

print(num_bags_inside("shiny gold bag"))
