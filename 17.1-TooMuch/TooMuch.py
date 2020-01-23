from pprint import pprint


def get_permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    permutations = []
    for i in range(len(lst)):
        m = lst[i]
        rest = lst[:i] + lst[i + 1:]

        for p in get_permutations(rest):
            permutations.append([m] + p)
    return permutations


input_file = open("input.txt", "r").read().split("\n")

containers = []

index = 0
for line in input_file:
    containers.append((int(line), index))
    index += 1

print(containers)

store_amount = 150

usable_containers = list(filter(lambda v: v[0] <= store_amount, containers))

print(usable_containers)

arrangements = get_permutations(usable_containers)

solutions = set()
for arrangement in arrangements:
    remaining = store_amount
    solution = []
    for bottle in arrangement:
        if remaining - bottle[0] > 0:
            remaining -= bottle[0]
            solution.append(bottle)
        elif remaining - bottle[0] == 0:
            solution.append(bottle)
            solutions.add(tuple(sorted(solution)))
            break
        else:
            break

pprint(solutions)

print(len(solutions))
