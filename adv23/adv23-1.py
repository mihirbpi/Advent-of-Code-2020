from aocd import get_data

cups_list = list(map(int, list(get_data(year=2020,day=23))))
size = len(cups_list)
current_cup = cups_list[0]

for i in range(0, 100):
    current_cup_index = cups_list.index(current_cup)

    pick_up = []
    pick_up1 = cups_list[(current_cup_index + 1) % size]
    pick_up2 = cups_list[(current_cup_index + 2) % size]
    pick_up3 = cups_list[(current_cup_index + 3) % size]
    pick_up.append(pick_up1)
    pick_up.append(pick_up2)
    pick_up.append(pick_up3)
    pick_up.reverse()
    cups_list.remove(pick_up1)
    cups_list.remove(pick_up2)
    cups_list.remove(pick_up3)

    dest_cup = (current_cup - 1) % size

    if(dest_cup == 0):
        dest_cup = size

    while (dest_cup in pick_up):
        dest_cup = abs((dest_cup - 1) % size)

        if(dest_cup == 0):
            dest_cup = size

    dest_cup_index = cups_list.index(dest_cup)

    for cup in pick_up:
        cups_list.insert(dest_cup_index + 1, cup)

    current_cup_index = cups_list.index(current_cup)
    current_cup = cups_list[(current_cup_index + 1) % size]

start_index = (cups_list.index(1) + 1) % size
result = ""

for i in range(0, size - 1):

    result += str(cups_list[(start_index + i) % size])

print(result)
