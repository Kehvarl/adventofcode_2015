from functools import reduce
from math import sqrt


def factors_1(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


target = 34000000
# target = 150
# target = 3400000
value = 0
for h in range(1, target):
    if sum(factors_1(h)) * 10 >= target:
        print(h)
        break
