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

pprint(solutions)

print(len(solutions))
