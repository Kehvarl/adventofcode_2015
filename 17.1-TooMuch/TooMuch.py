from pprint import pprint
from itertools import combinations


input_file = open("input.txt", "r").read().split("\n")

containers = []

index = 0
for line in input_file:
    containers.append(int(line))
    index += 1

print(containers)

store_amount = 150

usable_containers = list(filter(lambda v: v <= store_amount, containers))

print(usable_containers)

solutions = [bottles for i in range(len(usable_containers), 0, -1)
             for bottles in combinations(usable_containers, i)
             if sum(bottles) == store_amount]

least_bottles = len(solutions[0])
for solution in solutions:
    if len(solution) < least_bottles:
        least_bottles = len(solution)

short_solutions = [bottles for i in range(len(usable_containers), 0, -1)
                   for bottles in combinations(usable_containers, i)
                   if sum(bottles) == store_amount and len(bottles) == least_bottles]
pprint(solutions)

print(len(solutions))

print(least_bottles)

pprint(short_solutions)

print(len(short_solutions))
