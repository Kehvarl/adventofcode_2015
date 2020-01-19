
def parseline(input_line):
    tokens = input_line.strip(".").split(" ")

    parse_subject = tokens[0]
    parse_amount = int(tokens[3])
    parse_amount = -parse_amount if tokens[2] == "lose" else parse_amount
    parse_target = tokens[-1]

    return parse_subject, parse_amount, parse_target


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


def get_happiness(people, a, b):
    happiness = 0
    if a == "Me" or b == "Me":
        return 0
    happiness += people[a][b]
    happiness += people[b][a]
    return happiness


graph = {}

input_text = open("input.txt", "r").read().split("\n")


for line in input_text:
    subject, amount, target = parseline(line)
    if not graph.get(subject):
        graph[subject] = {}
    graph[subject][target] = amount


subjects = []
for key in graph:
    subjects.append(key)

subjects.append("Me")

seating_arrangements = get_permutations(subjects)
totals = []

for arrangement in seating_arrangements:
    total = 0
    for index in range(len(arrangement) - 1):
        total += get_happiness(graph, arrangement[index], arrangement[index + 1])
    total += get_happiness(graph, arrangement[-1], arrangement[0])

    print(arrangement, total)
    totals.append(total)

print(max(totals))
