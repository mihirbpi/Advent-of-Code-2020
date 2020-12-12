from aocd import get_data

instructions = get_data(day=8).split("\n")[:-1]

def does_terminate(instructs):
    index = 0
    acc = 0
    current_instruct = (0, instructs[0])
    past_instructs = []

    while(current_instruct not in past_instructs):
        instruct_array = current_instruct[1].split(" ")

        if(instruct_array[0] == "nop"):
            index += 1
            past_instructs.append(current_instruct)

            if(index  >= len(instructs)):
                return (acc, True)
            current_instruct = (index, instructs[index])

        elif(instruct_array[0] == "acc"):
            increment = instruct_array[1]
            inc = 0

            if(increment[0] == "-"):
                inc = -1 * int(increment.strip("-"))

            elif(increment[0] == "+"):
                inc = int(increment.strip("+"))

            acc += inc
            index += 1
            past_instructs.append(current_instruct)

            if(index  >= len(instructs)):
                return (acc, True)
            current_instruct = (index, instructs[index])

        elif(instruct_array[0] == "jmp"):
            increment = instruct_array[1]
            inc = 0

            if(increment[0] == "-"):
                inc = -1 * int(increment.strip("-"))

            elif(increment[0] == "+"):
                inc = int(increment.strip("+"))

            index += inc
            past_instructs.append(current_instruct)

            if(index  >= len(instructs)):
                return (acc, True)
            current_instruct = (index, instructs[index])

    return (acc, False)


for i in range(0, len(instructions)):
    instructions_copy = instructions.copy()
    command = instructions_copy[i]

    if("nop" in command):
        instructions_copy[i] = instructions_copy[i].replace("nop", "jmp")
        result = does_terminate(instructions_copy)

        if(result[1]):
            print(result[0])

    elif("jmp" in command):
        instructions_copy[i] = instructions_copy[i].replace("jmp", "nop")
        result = does_terminate(instructions_copy)

        if(result[1]):
            print(result[0])
