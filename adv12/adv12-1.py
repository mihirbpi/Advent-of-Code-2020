from aocd import get_data

my_list = get_data(year=2020,day=12).split("\n")
ship_x = 0
ship_y = 0
ship_dir_index = 0
dirs = ["E", "S", "W", "N"]

for i in range(0, len(my_list)):
    command = my_list[i]
    command_symbol = command[0]
    command_value = int(command[1:])
    ship_dir = dirs[ship_dir_index]

    if(command_symbol == "F"):

        if(ship_dir == "E"):
            ship_x += command_value

        elif(ship_dir == "N"):
            ship_y += command_value

        elif(ship_dir == "W"):
            ship_x -= command_value

        elif(ship_dir == "S"):
            ship_y -= command_value

    elif(command_symbol == "R"):
        ship_dir_index += int(command_value / 90)
        ship_dir_index  = ship_dir_index % 4

    elif(command_symbol == "L"):
        ship_dir_index -= int(command_value / 90)
        ship_dir_index  = ship_dir_index % 4

    elif(command_symbol == "E"):
        ship_x += command_value

    elif(command_symbol == "N"):
        ship_y += command_value

    elif(command_symbol == "W"):
        ship_x -= command_value

    elif(command_symbol == "S"):
        ship_y -= command_value

print(abs(ship_x) + abs(ship_y))
