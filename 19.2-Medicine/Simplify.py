from pprint import pprint
from random import shuffle


input_file = open("input.txt", "r").read().split("\n")

molecule = input_file[-1]
input_file = input_file[:-1]

replacements = []

for line in input_file:
    m_in, m_out = line.split(" => ")
    replacements.append((m_in, m_out))

target = molecule
steps = 0
path = []

while target != 'e':
    tmp = target
    for m_in, m_out in replacements:
        if m_out not in target:
            continue

        target = target.replace(m_out, m_in, 1)
        steps += 1
        path.append(target)

    if tmp == target:
        target = molecule
        steps = 0
        path = []
        shuffle(replacements)

print(steps)
pprint(path)