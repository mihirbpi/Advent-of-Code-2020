from aocd import get_data

my_list = get_data(day=5).split("\n")


def bin_to_dec(string):
    result = 0

    for i in range(0, len(string)):
        digit = int(string[len(string)-1-i])
        result += digit * (2**i)
    return result

def seat_ID(string):
    row_string = ""
    column_string = ""

    for i in range(0, len(string)):

        if(string[i] == "F"):
            row_string += "0"

        elif(string[i] == "B"):
            row_string += "1"

        elif(string[i] == "L"):
            column_string += "0"

        elif(string[i] == "R"):
            column_string += "1"

    row = bin_to_dec(row_string)
    column = bin_to_dec(column_string)
    return row * 8 + column


max = 0

for i in range(0, len(my_list)):
    sID = seat_ID(my_list[i])

    if(sID >= max):
        max = sID

print(max)
