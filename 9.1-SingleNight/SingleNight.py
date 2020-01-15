
test = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""".split("\n")

input_file = open("input.txt", "r").read().split("\n")


graph = {}

paths = []
lengths = []

for line in input_file:
    tokens = line.split(" ")
    a = tokens[0]
    b = tokens[2]
    c = tokens[4]
    if not graph.get(a):
        graph[a] = []
    if not graph.get(b):
        graph[b] = []

    graph[a].append((b, c))
    graph[b].append((a, c))


def depth_first(node, path, length):
    recurse = False
    for neighbor, distance in graph[node]:
        if neighbor not in path:
            recurse = True
            # print(length, path)
            depth_first(neighbor, path + [neighbor], length + int(distance))
    if not recurse:
        # print(length, path)
        paths.append(path)
        lengths.append(length)


for node in graph:
    depth_first(node, [node], 0)


print(max(lengths))



