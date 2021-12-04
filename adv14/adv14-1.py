from aocd import get_data

program = get_data(year=2020,day=14).split("\n")
mask = ""
mem = {}

def replacer(string, newstring, index):
    return string[:index] + newstring + string[index + 1:]

def dec_to_bin(dec_string):
    result = bin(int(dec_string)).replace("0b", "")
    return (36 - len(result)) * "0" + result

def bin_to_dec(bin_string):
    return int(bin_string, 2)

def new_dec_value(dec_string, mask_string):
    bin_string = dec_to_bin(dec_string)
    new_bin_string = bin_string

    for i in range(0, len(mask_string)):
        char = mask_string[i]

        if(char == "0" or char == "1"):
            new_bin_string = replacer(new_bin_string, char, i)

    return bin_to_dec(new_bin_string)

for i in range(0, len(program)):
    string = program[i]

    if(string.split(" ")[0] == "mask"):
        mask = string.split(" ")[2]

    else:
        dec_string = string.split(" ")[2]
        new_value = new_dec_value(dec_string, mask)
        address = int(string.split("mem[")[1].split("]")[0])
        mem[address] = new_value

print(sum(mem.values()))
