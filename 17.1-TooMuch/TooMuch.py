

input_file = open("test.txt", "r").read().split("\n")

containers = []

for line in input_file:
    containers.append(int(line))

print(containers)
