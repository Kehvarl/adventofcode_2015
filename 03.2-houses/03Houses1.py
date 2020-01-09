

def do_move(x, y, direction):
    if move == ">":
        x += 1
    elif move == "<":
        x -= 1
    elif move == "^":
        y += 1
    elif move == "v":
        y -= 1
    return x, y


santa_x = 0
santa_y = 0

robo_x = 0
robo_y = 0

houses = set()
moves = open("input.txt", "r").read()
houses.add((0, 0))

santa = True
x, y = (0,0)
for move in moves:
    if santa:
        x, y = do_move(santa_x, santa_y, move)
        print("santa", x, y)
        santa_x, santa_y = x, y
        santa = False
    else:
        x, y = do_move(robo_x, robo_y, move)
        print("robo", x, y)
        robo_x, robo_y = x, y
        santa = True

    if (x,y) not in houses:
        houses.add((x, y))


print(len(houses))
