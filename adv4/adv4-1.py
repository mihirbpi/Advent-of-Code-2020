from aocd import get_data

my_list = get_data(day=4).split("\n\n")

for i in range (0, len(my_list)):
    my_list[i] = my_list[i].replace("\n", " ").strip()

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def is_valid(passport):
    entries = passport.split(" ")
    fields = []

    for entry in entries:
        field = entry.split(":")[0]
        fields.append(field)

    for required in required_fields:

        if(required not in fields):
            return False
    return True


count = 0

for i in range (0, len(my_list)):

    if(is_valid(my_list[i])):
        count += 1

print(count)
