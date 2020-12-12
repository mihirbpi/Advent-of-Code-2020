from aocd import get_data

my_list = get_data(day=12).split("\n")
ship_x = 0
ship_y = 0
waypoint_x = 10
waypoint_y = 1

def my_cos(theta):
    if(abs(theta) == 90 or abs(theta) == 270):
        return 0
    if(abs(theta) == 180):
        return -1

def my_sin(theta):
    if(abs(theta) == 180):
        return 0
    if(theta == 90 or theta == -270):
        return 1
    if(theta == -90 or theta == 270):
        return -1

for i in range(0, len(my_list)):
    command = my_list[i]
    command_symbol = command[0]
    command_value = int(command[1:])

    if(command_symbol == "F"):

        ship_x += command_value * waypoint_x
        ship_y += command_value * waypoint_y

    elif(command_symbol == "R" or command_symbol == "L"):
        theta = command_value

        if(command_symbol == "R"):
            theta *= -1

        previous_x = waypoint_x
        previous_y = waypoint_y
        waypoint_x = (previous_x * my_cos(theta)) - (previous_y * my_sin(theta))
        waypoint_y = (previous_x * my_sin(theta)) + (previous_y * my_cos(theta))

    elif(command_symbol == "E"):
        waypoint_x += command_value

    elif(command_symbol == "N"):
        waypoint_y += command_value

    elif(command_symbol == "W"):
        waypoint_x -= command_value

    elif(command_symbol == "S"):
        waypoint_y -= command_value

print(abs(ship_x) + abs(ship_y))
