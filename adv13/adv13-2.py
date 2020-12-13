from aocd import get_data
import math

my_list = get_data(day=13).split("\n")
bus_IDs = list(map(int, list(filter(lambda x: x != 'x', my_list[1].split(",")))))

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):
        # q is quotient
        q = a // m
        t = m
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + m0

    return x

# Chinese Remainder Theorem
N = math.prod(bus_IDs)
products_list = []

for i in range(0, len(bus_IDs)):
    n_i = bus_IDs[i]
    a_i =  -1 * my_list[1].split(",").index(str(n_i)) % n_i
    y_i = int(N / n_i)
    z_i = modInverse(y_i, n_i)
    products_list.append(a_i * y_i * z_i)


print(sum(products_list) % N)
