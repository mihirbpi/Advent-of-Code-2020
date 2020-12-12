from aocd import get_data

my_list = get_data(day=4).split("\n\n")

for i in range (0, len(my_list)):
    my_list[i] = my_list[i].replace("\n", " ").strip()

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
hexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def valid_value(field, value):

    if(field == "byr"):

        if(value.isnumeric() and int(value) >= 1920 and int(value) <= 2002):
            return True
        return False

    elif(field == "iyr"):

        if(value.isnumeric() and int(value) >= 2010 and int(value) <= 2020):
            return True
        return False

    elif(field == "eyr"):

        if(value.isnumeric() and int(value) >= 2020 and int(value) <= 2030):
            return True
        return False

    elif(field == "hgt"):

        if("cm" in value):
            height = value.split("cm")[0]

            if(height.isnumeric() and int(height) >= 150 and int(height) <= 193):
                return True
            return False

        elif("in" in value):
            height = value.split("in")[0]

            if(height.isnumeric() and int(height) >= 59 and int(height) <= 76):
                return True
            return False
        return False

    elif(field == "hcl"):

        if(not value[0] == "#"):
            return False

        for i in range(0, len(value)):

            if(not value[i] in hexa and not value[i] == "#"):
                return False
        return True

    elif(field == "ecl"):

        if(value in ecls):
            return True
        return False

    elif(field == "pid"):

        if(value.isnumeric() and len(value) == 9):
            return True
        return False

    elif(field == "cid"):
        return True
    return False


def is_valid(passport):
    entries = passport.split(" ")
    fields = []

    for entry in entries:
        field = entry.split(":")[0]
        value = entry.split(":")[1]

        if(not valid_value(field, value)):
            return False
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
