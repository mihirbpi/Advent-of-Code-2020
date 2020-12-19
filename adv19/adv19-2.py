from aocd import get_data
import itertools

my_list = get_data(day=19).split("\n\n")
rules = my_list[0].split("\n")
strings = my_list[1].split("\n")
rules_dict = {}

for i in range(0, len(rules)):
    rule_string = rules[i]
    rule_number = rule_string.split(": ")[0]
    rule_code = rule_string.split(": ")[1]
    rules_dict[rule_number] = rule_code

def valid_strings_set(rule_number):
    rule_code = rules_dict[rule_number]
    result = set()

    if(rule_code[0] == '"'):
        result = set()
        result.add(rule_code.strip('"'))
        return result

    elif("|" not in rule_code):
        result = set()
        r = rule_code.split(" ")
        length = len(r)
        x = list(map(valid_strings_set, r))

        for p in itertools.product(*x):
            result.add("".join(p))

        return result

    r1 = rule_code.split("|")[0].strip(" ").split(" ")
    length1 = len(r1)
    x1 = list(map(valid_strings_set, r1))

    for p1 in itertools.product(*x1):
        result.add("".join(p1))

    r2 = rule_code.split("|")[1].strip(" ").split(" ")
    length2 = len(r2)
    x2 = list(map(valid_strings_set, r2))

    for p2 in itertools.product(*x2):
        result.add("".join(p2))

    return result

valid42strings = valid_strings_set("42")
valid31strings = valid_strings_set("31")

def follows8(string):

    if(string in valid42strings):
        return True

    for i in range(0, len(string) + 1):
        substring = string[0:i]

        if(substring in valid42strings):
            string = string.replace(substring, "", 1)
            return follows8(string)

    return False

def follows11(string):

    for i in range(0, len(string)):
        substring = string[0:i]

        if(substring in valid42strings):
            string = string.replace(substring, "", 1)

            if(string in valid31strings):
                return True

            for j in reversed(range(0, len(string))):

                if(string[j:] in valid31strings):
                    return follows11(string[0:j])

            return False

    return False

def follows0(string):

    for i in range(0, len(string) + 1):
        substring = string[0:i]

        if(follows8(substring)):
            check = string.replace(substring, "", 1)

            if(follows11(check)):
                return True

    return False

count = 0

for i in range(0, len(strings)):

    if(follows0(strings[i])):
        count +=1

print(count)
