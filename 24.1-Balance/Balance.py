import operator
from itertools import combinations
from functools import reduce

# input_file = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

input_file = [int(x) for x in open("input.txt", "r").read().split("\n")]

set_size = sum(input_file) // 4

possible_groups = [set(seq) for i in range(len(input_file), 0, -1)
                   for seq in combinations(input_file, i)
                   if sum(seq) == set_size]

print(set_size)

shortest_group = 1000
for group in possible_groups:
    if len(group) < shortest_group:
        shortest_group = len(group)

first_groups = list(filter(lambda grp: (len(grp) == shortest_group), possible_groups))

QE = []
if len(first_groups) > 0:
    for g in first_groups:
        QE.append(reduce(operator.mul, g))

print(min(QE))
