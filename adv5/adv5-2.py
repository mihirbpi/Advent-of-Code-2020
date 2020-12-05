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

    
flight_seat_IDs = []

for i in range(0, len(my_list)):
    sID = seat_ID(my_list[i])
    flight_seat_IDs.append(sID)

all_seat_IDs = range(min(flight_seat_IDs), max(flight_seat_IDs) + 1)
missing_ID = 0

for i in range(0, len(all_seat_IDs)):

    if(all_seat_IDs[i] not in flight_seat_IDs):
        missing_ID = all_seat_IDs[i]

print(missing_ID)
