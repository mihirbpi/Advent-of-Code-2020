from aocd import get_data
import math

my_list = get_data(year=2020,day=25).split("\n")
door_public_key = int(my_list[0])
card_public_key = int(my_list[1])

def find_loop_size(public_key):
    i = 0
    previous = 0
    b = 20201227

    while(True):

        a = pow(7, i, 20201227)

        if (a == public_key):
            return i

        b = b - a + previous

        if(b == public_key):
            return i + int((20201227 - 1) / 2)

        i += 1
        previous = a

def transform(subject_number, loop_size):
    return pow(subject_number, loop_size, 20201227)

door_loop_size = find_loop_size(door_public_key)
encryption_key = transform(card_public_key, door_loop_size)
print(encryption_key)
