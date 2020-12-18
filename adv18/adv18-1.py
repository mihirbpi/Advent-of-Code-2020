from aocd import get_data

my_list = get_data(day=18).split("\n")

def find_closing_index(string, open_index):
    counter = 1
    close_index = open_index

    while (counter > 0):
        char = string[close_index + 1]
        close_index += 1

        if(char == "("):
            counter += 1

        elif(char == ")"):
            counter -= 1

    return close_index


def get_parenth_dict(string):
    dict = {}

    for i in range(0, len(string)):

        if(string[i] == "("):
            dict[i] = find_closing_index(string, i)

    return dict


def get_array(string):
    arr = []
    index = 0
    dict = get_parenth_dict(string)

    while (index < len(string)):

        curr_char = string[index]

        if(curr_char != "("):
            new_index = index
            curr_string = ""

            while(curr_char != " " and not (new_index >= len(string) or string[new_index] == " " )):
                curr_char = string[new_index]
                curr_string += curr_char
                new_index += 1

            arr.append(curr_string)
            index += len(curr_string) + 1

        elif(curr_char == "("):
            close_index = dict[index]
            arr.append(string[index:close_index + 1])
            index = close_index + 2

    return arr

def calculate(string):
    array = get_array(string)
    result = 0

    if(array[0][0] != "("):
        result = int(array[0])

    elif(array[0][0] == "("):
        result = calculate(array[0][1:len(array[0]) - 1])

    index = 1

    while (index < len(array)):

        if(array[index] == "*"):
            result = result * calculate(array[index + 1])

        elif(array[index] == "+"):
            result = result + calculate(array[index + 1])

        index += 1

    return result

sum = 0

for i in range(0, len(my_list)):
    sum += calculate(my_list[i])

print(sum)
