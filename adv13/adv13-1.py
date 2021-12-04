from aocd import get_data
import math

my_list = get_data(year=2020,day=13).split("\n")
arrival_time = int(my_list[0])
bus_IDs = list(map(int, list(filter(lambda x: x != 'x', my_list[1].split(",")))))
earliest_times = list(map(lambda x: x * (int(math.floor(arrival_time / x)) + 1) - arrival_time, bus_IDs))

print(min(earliest_times) * bus_IDs[earliest_times.index(min(earliest_times))])
