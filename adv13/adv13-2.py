from aocd import get_data
import math

my_list = get_data(year=2020,day=13).split("\n")
bus_IDs = list(map(int, list(filter(lambda x: x != 'x', my_list[1].split(",")))))

# Chinese Remainder Theorem
N = math.prod(bus_IDs)
products_list = []

for i in range(0, len(bus_IDs)):
    n_i = bus_IDs[i]
    a_i =  -1 * my_list[1].split(",").index(str(n_i))
    y_i = int(N / n_i)
    z_i = pow(y_i, -1, n_i) # z_i = y_i^(-1) mod n_i
    products_list.append(a_i * y_i * z_i)

print(sum(products_list) % N)
