from aocd import get_data

program = get_data(day=14).split("\n")
mask = ""
mem = {}

def replacer(string, newstring, index):
    return string[:index] + newstring + string[index + 1:]

def dec_to_bin(dec_string):
    result = bin(int(dec_string)).replace("0b", "")
    return (36 - len(result)) * "0" + result

def bin_to_dec(bin_string):
    return int(bin_string, 2)

def write_value(bin_address_floating, value):
    if(bin_address_floating.count("X") == 1):
        address0 = bin_to_dec(bin_address_floating.replace("X", "0"))
        address1 = bin_to_dec(bin_address_floating.replace("X", "1"))
        mem[address0] = value
        mem[address1] = value
    else:
        bin_address_floating0 = bin_address_floating.replace("X", "0", 1)
        bin_address_floating1 = bin_address_floating.replace("X", "1", 1)
        write_value(bin_address_floating0, value)
        write_value(bin_address_floating1, value)

for i in range(0, len(program)):
    string = program[i]

    if(string.split(" ")[0] == "mask"):
        mask = string.split(" ")[2]

    else:
        address = string.split("mem[")[1].split("]")[0]
        new_value = int(string.split(" ")[2])
        bin_address = dec_to_bin(address)
        bin_address_floating = bin_address

        for i in range(0, len(mask)):
            mask_char = mask[i]
            address_char = bin_address[i]

            if((mask_char == "1" or mask_char == "X") and mask_char != address_char):
                bin_address_floating = replacer(bin_address_floating, mask_char, i)

        write_value(bin_address_floating, new_value)

print(sum(mem.values()))
