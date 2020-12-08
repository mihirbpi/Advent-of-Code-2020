from aocd import get_data

instructions = get_data(day=8).split("\n")[:-1]
acc = 0
index = 0
current_instruction = ""
past_instructions = []

while(current_instruction not in past_instructions):
    current_instruction = (index, instructions[index])
    instruction_array = current_instruction[1].split(" ")


    if(instruction_array[0] == "nop"):
        index += 1
        past_instructions.append(current_instruction)
        current_instruction = (index, instructions[index])

    elif(instruction_array[0] == "acc"):
        increment = instruction_array[1]
        inc = 0
        
        if(increment[0] == "-"):
            inc = -1 * int(increment.strip("-"))

        elif(increment[0] == "+"):
            inc = int(increment.strip("+"))

        acc += inc
        index += 1
        past_instructions.append(current_instruction)
        current_instruction = (index, instructions[index])

    elif(instruction_array[0] == "jmp"):
        increment = instruction_array[1]
        inc = 0

        if(increment[0] == "-"):
            inc = -1 * int(increment.strip("-"))

        elif(increment[0] == "+"):
            inc = int(increment.strip("+"))

        index += inc
        past_instructions.append(current_instruction)
        current_instruction = (index, instructions[index])

print(acc)
