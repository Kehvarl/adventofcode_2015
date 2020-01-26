from itertools import combinations
from functools import reduce
from math import sqrt
from pprint import pprint


def factors(x):
    found_factors = [1, x]
    twos = 0
    while x % 2 == 0:
        x = x//2
        twos += 1
        found_factors.append(twos * 2)

    for i in range(2, int(x)):
        if x % i == 0:
            found_factors.append(i)

    return found_factors


def factors_1(n):
    step = 2 if n%2 else 1
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


def sum_to(target, houses, tolerance = 0):
    results = []
    dataArray = list(range(1,houses))

    for i in range(1, len(dataArray) + 1):
        for comb in combinations(dataArray, i):
            if abs(sum(comb) - target) <= tolerance:
                results.append(comb)

    return results


target = 34000000
# target = 150
# target = 3400000
value = 0
for i in range(1, target):
    if sum(factors_1(i)) * 10 >= target:
        print(i)
        break


# pprint(sum_to(34000000//10, 100000, 0))
