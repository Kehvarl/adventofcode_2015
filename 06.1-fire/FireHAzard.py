
def parser(command):
    tokens = command.split(" ")
    if tokens[0] == "turn":
        x, y = tokens[2].split(",")
        range_start = (int(x), int(y))
        x, y = tokens[4].split(",")
        range_end = (int(x), int(y))
        set_light(range_start, range_end, tokens[1])
    elif tokens[0] == "toggle":
        x, y = tokens[1].split(",")
        range_start = (int(x), int(y))
        x, y = tokens[3].split(",")
        range_end = (int(x), int(y))
        toggle(range_start, range_end)


def set_light(start, end, state):
    sx, sy = start
    ex, ey = end
    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            if state == "on":
                if (x, y) not in grid:
                    grid.add((x, y))
            elif state == "off":
                if (x, y) in grid:
                    grid.remove((x, y))


def toggle(start, end):
    sx, sy = start
    ex, ey = end
    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            if (x, y) not in grid:
                grid.add((x, y))
            else:
                grid.remove((x, y))


grid = set()

input_file = open("input.txt", "r").read().split("\n")

for line in input_file:
    parser(line)
    # print(grid)

print(len(grid))
