from aocd import get_data

my_list = list(map(int, get_data(day=9).split("\n")[:-1]))

def is_valid(previous_list, number):

    for i in range(0, len(previous_list)):
        x = previous_list[i]
        y = 0

        for j in range(i + 1, len(previous_list)):
            y = previous_list[j]

            if(x + y == number):
                return True
    return False


def first_not_valid(preamble_length):
    preamble = my_list[0:preamble_length]

    for i in range(len(preamble), len(my_list)):
        previous_list = my_list[i - preamble_length:i]

        if(not is_valid(previous_list, my_list[i])):
            return my_list[i]

print(first_not_valid(25))
