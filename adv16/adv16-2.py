from aocd import get_data

my_list = get_data(day=16).split("\n\n")
fields = my_list[0].split("\n")
my_ticket = list(map(int, my_list[1].split(":\n")[1].split(",")))
nearby_tickets = my_list[2].split("\n")
fields_list = []
nearby_tickets_list = []
invalid_tickets = []
fields_dict = {}

for i in range(0, len(fields)):
    string = fields[i]
    x1 = int(string.split(":")[1].strip(" ").split(" ")[0].split("-")[0])
    x2 = int(string.split(":")[1].strip(" ").split(" ")[0].split("-")[1])
    y1 = int(string.split(":")[1].strip(" ").split(" ")[2].split("-")[0])
    y2 = int(string.split(":")[1].strip(" ").split(" ")[2].split("-")[1])
    fields_list.append((string.split(":")[0], [x1, x2, y1, y2]))

for i in range(1, len(nearby_tickets)):
    nearby_ticket = list(map(int, nearby_tickets[i].split(",")))
    nearby_tickets_list.append(nearby_ticket)

def invalid_values(ticket):

    for i in range(0, len(ticket)):
        field_value = ticket[i]
        valid_count = 0

        for j in range(0, len(fields_list)):
            field = fields_list[j][1]

            if ((field_value >= field[0] and field_value <= field[1]) or (field_value >= field[2] and field_value <= field[3])):
                valid_count += 1

        if(valid_count == 0):
            invalid_tickets.append(ticket)

fields_dict = {i[0]: set() for i in fields_list}

def find_field_index(field):
    name = field[0]
    rules = field[1]
    x1 = rules[0]
    x2 = rules[1]
    y1 = rules[2]
    y2 = rules[3]

    for field_index in range(0, len(nearby_tickets_list[0])):
        invalid_count = 0

        for i in range(0, len(nearby_tickets_list)):
            field_value = nearby_tickets_list[i][field_index]

            if(not ((field_value >= x1 and field_value <= x2) or (field_value >= y1 and field_value <= y2))):
                invalid_count += 1

        if(invalid_count == 0):
            fields_dict[field[0]].add(field_index)


for i in range(0, len(nearby_tickets_list)):
    ticket = nearby_tickets_list[i]
    invalid_values(ticket)

for i in range(0, len(invalid_tickets)):
    nearby_tickets_list.remove(invalid_tickets[i])

for i in range(0, len(fields_list)):
    find_field_index(fields_list[i])

actual_fields = {}
fields_dict = sorted(fields_dict.items(), key=lambda x: len(x[1]))
used = set()

for s in fields_dict:
    field_index = (s[1] - used).pop()
    used.add(field_index)
    actual_fields[field_index] =  s[0]

product = 1

for i in range(0, len(my_ticket)):
        if(actual_fields[i].split(" ")[0] == "departure"):
            product *= my_ticket[i]

print(product)
