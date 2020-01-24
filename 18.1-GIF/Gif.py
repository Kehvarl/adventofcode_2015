from pprint import pprint


def apply_rules(my_x, my_y, my_grid):

    if (my_x, my_y) in [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]:
        return 1

    status = my_grid[y][x]
    neighbors = [(-1, -1), (0, -1),(1, -1),
                 (-1, 0), (1, 0),
                 (-1, 1), (0, 1), (1, 1)]

    count = 0

    for neighbor in neighbors:
        dx, dy = neighbor
        nx = my_x + dx
        ny = my_y + dy

        if 0 <= ny < height and 0 <= nx < width:
            count += my_grid[ny][nx]

    if status == 1 and count in [2, 3]:
        return 1
    elif status == 0 and count == 3:
        return 1
    else:
        return 0


input_file = open("input.txt", "r").read().split("\n")

width = len(input_file[0])
height = len(input_file)

grid = [[0 for _ in range(width)] for _ in range(height)]

for y in range(height):
    for x in range(width):
        grid[y][x] = 1 if input_file[y][x] == "#" else 0


for (x, y) in [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]:
    grid[y][x] = 1


pprint(grid)
print()

for _ in range(100):
    new_grid = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            new_grid[y][x] = apply_rules(x, y, grid)
    grid = new_grid

pprint(grid)

total = 0
for line in grid:
    total += sum(line)

print(total)
