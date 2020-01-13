from pprint import pprint
from collections import deque


def parse(command):
    tokens = command.split(" ")
    output = tokens[-1]
    if "AND" in tokens:
        x = tokens[0]
        y = tokens[2]
        if x in wires and y in wires:
            wires[output] = wires[x] & wires[y]
            return True
        elif x.isnumeric() and y in wires:
            wires[output] = int(x) & wires[y]
            return True
        elif x in wires and y.isnumeric():
            wires[output] = wires[x] & int(y)
            return True
    elif "OR" in tokens:
        x = tokens[0]
        y = tokens[2]
        if x in wires and y in wires:
            wires[output] = wires[x] | wires[y]
            return True
        elif x.isnumeric() and y in wires:
            wires[output] = int(x) | wires[y]
            return True
        elif x in wires and y.isnumeric():
            wires[output] = wires[x] | int(y)
            return True
    elif "NOT" in tokens:
        x = tokens[1]
        if x in wires:
            wires[output] = ~wires[x]
            return True
    elif "LSHIFT" in tokens:
        x = tokens[0]
        amount = tokens[2]
        if x in wires:
            wires[output] = wires[x] << int(amount)
            return True
    elif "RSHIFT" in tokens:
        x = tokens[0]
        amount = tokens[2]
        if x in wires:
            wires[output] = wires[x] >> int(amount)
            return True
    elif tokens[0] in wires:
        wires[output] = wires[tokens[0]]
        return True
    elif tokens[0].isnumeric():
        wires[output] = int(tokens[0])
        return True

    return False


wires = {}

input_file = open("input.txt", "r").read().split("\n")

processing = deque()

for line in input_file:
    processing.append(line)


while processing:
    command = processing.popleft()
    if not parse(command):
        processing.append(command)

pprint(wires)
print()
print(wires["a"])
