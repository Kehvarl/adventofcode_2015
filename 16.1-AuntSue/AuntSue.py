
input_file = open("input.txt", "r").read().split("\n")

sues = [None] * 501

for line in input_file:
    # Sue 1: cars: 9, akitas: 3, goldfish: 0
    aunt, rest = line.split(": ", maxsplit=1)
    aunt = aunt.split(" ")
    aunt_num = aunt[1]
    analysis = {}
    for compound in rest.split(", "):
        result, amount = compound.split(": ")
        analysis[result] = int(amount)

    sues[int(aunt_num)] = analysis

print(sues)

gifter = {"children": 3,
          "cats": 7,
          "samoyeds": 2,
          "pomeranians": 3,
          "akitas": 0,
          "vizslas": 0,
          "goldfish": 5,
          "trees": 3,
          "cars": 2,
          "perfumes": 1}

possible_sues = []
for sue in sues:
    if sue is None:
        continue
    possible = True
    number = sues.index(sue)
    for prop in gifter:
        if sue.get(prop):
            if prop == "cats" or prop == "trees":
                if sue[prop] <= gifter[prop]:
                    possible = False
            elif prop == "pomeranians" or prop == "goldfish":
                if sue[prop] >= gifter[prop]:
                    possible = False
            else:
                if sue[prop] != gifter[prop]:
                    possible = False
    if possible:
        possible_sues.append(number)


print(possible_sues)
for pos in possible_sues:
    print(sues[pos])
