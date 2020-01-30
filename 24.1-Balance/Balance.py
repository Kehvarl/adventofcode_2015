import operator
from itertools import combinations
from functools import reduce

# input_file = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

input_file = [int(x) for x in open("input.txt", "r").read().split("\n")]

set_size = sum(input_file) // 3

possible_groups = [set(seq) for i in range(len(input_file), 0, -1)
                   for seq in combinations(input_file, i)
                   if sum(seq) == set_size]

print(set_size)

shortest_group = 1000
for group in possible_groups:
    if len(group) < shortest_group:
        shortest_group = len(group)

first_groups = filter(lambda grp: (len(grp) == shortest_group), possible_groups)
allowed_groups = {}
while False:
    for first in first_groups:
        for i in range(len(possible_groups)):
            second = possible_groups[i]
            if second == first:
                continue
            if second.isdisjoint(first):
                for i3 in range(i, len(possible_groups)):
                    if i3 == i:
                        continue
                    third = possible_groups[i3]
                    if third == first:
                        continue
                    if (first.isdisjoint(second) and
                            first.isdisjoint(third) and
                            second.isdisjoint(third) and
                            len(first) <= len(second) and
                            len(first) <= len(third)):
                        first_t = tuple(first)
                        if not allowed_groups.get(first_t):
                            allowed_groups[first_t] = []
                        if ((second, third) not in allowed_groups[first_t] and
                                (third, second) not in allowed_groups[first_t]):
                            allowed_groups[first_t].append((second, third))

    print(len(allowed_groups))

    shortest = 1000
    for group in allowed_groups:
        if len(group) < shortest:
            shortest = len(group)

    shortest_groups = list(filter(lambda grp: (len(grp) == shortest), allowed_groups))

QE = []
if len(list(first_groups)) > 0:
    for g in first_groups:
        QE.append(reduce(operator.mul, g))

print(min(QE))
