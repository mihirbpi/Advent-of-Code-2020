from aocd import get_data

my_list = get_data(year=2020,day=16).split("\n\n")
fields = my_list[0].split("\n")
nearby_tickets = my_list[2].split("\n")
fields_list = []
nearby_tickets_list = []

for i in range(0, len(fields)):
    string = fields[i]
    x1 = int(string.split(":")[1].strip(" ").split(" ")[0].split("-")[0])
    x2 = int(string.split(":")[1].strip(" ").split(" ")[0].split("-")[1])
    y1 = int(string.split(":")[1].strip(" ").split(" ")[2].split("-")[0])
    y2 = int(string.split(":")[1].strip(" ").split(" ")[2].split("-")[1])
    fields_list.append([x1, x2, y1, y2])

for i in range(1, len(nearby_tickets)):
    nearby_ticket = list(map(int, nearby_tickets[i].split(",")))
    nearby_tickets_list.append(nearby_ticket)

def invalid_values(ticket):
    invalid_value_list = []

    for i in range(0, len(ticket)):
        field_value = ticket[i]
        valid_count = 0

        for j in range(0, len(fields_list)):
            field = fields_list[j]

            if((field_value >= field[0] and field_value <= field[1]) or (field_value >= field[2] and field_value <= field[3])):
                valid_count += 1

        if(valid_count == 0):
            invalid_value_list.append(field_value)

    return invalid_value_list

error_rate = 0

for i in range(0, len(nearby_tickets_list)):
    ticket = nearby_tickets_list[i]
    error_rate += sum(invalid_values(ticket))

print(error_rate)
