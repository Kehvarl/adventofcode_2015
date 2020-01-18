import json


def sum_nums(input_node):
    sum_total = 0

    if isinstance(input_node, dict):
        for k, v in input_node.items():
            if k == "red" or v == "red":
                return 0
            if isinstance(v, dict) or isinstance(v, list):
                sum_total += sum_nums(v)
            elif isinstance(v, int):
                sum_total += v

    elif isinstance(input_node, list):
        for item in input_node:
            if isinstance(item, dict) or isinstance(item, list):
                sum_total += sum_nums(item)
            elif isinstance(item, int):
                sum_total += item

    elif isinstance(input_node, int):
        sum_total += input_node

    return sum_total


input_file = open("input.txt", "r").read().split("\n")

total = 0
for line in input_file:
    data = json.loads(line)
    total += sum_nums(data)
    print(sum_nums(data))


print(total)
