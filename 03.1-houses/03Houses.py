

x = 0
y = 0
houses = set()
moves = open("input.txt", "r").read()
houses.add((x, y))
for move in moves:
    if move == ">":
        x += 1
    elif move == "<":
        x -= 1
    elif move == "^":
        y += 1
    elif move == "v":
        y -= 1
    if (x,y) not in houses:
        houses.add((x, y))


print(len(houses))
