from aocd import get_data

my_list = get_data(day=5).split("\n")


def bin_to_dec(string):
    result = 0

    for i in range(0, len(string)):
        digit = int(string[len(string)-1-i])
        result += digit * (2**i)
    return result

def seat_ID(string):
    row_string = string[0:7].replace("F", "0").replace("B", "1")
    column_string = string[7:10].replace("L", "0").replace("R", "1")
    row = bin_to_dec(row_string)
    column = bin_to_dec(column_string)
    return row * 8 + column


max = 0

for i in range(0, len(my_list)):
    sID = seat_ID(my_list[i])

    if(sID >= max):
        max = sID

print(max)
