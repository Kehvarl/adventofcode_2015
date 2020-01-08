
def process(pattern, floor, target=None):
    position = 0
    for c in pattern:
        position += 1
        if c == "(":
            floor += 1
        if c == ")":
            floor -= 1
        if target and floor == target:
            return position

    return floor


tests = [
    ["(())", 0],
    ["()()", 0],
    ["(((", 3],
    ["(()(()(", 3],
    ["())", -1],
    ["))(", -1],
    [")))", -3],
    [")())())", -3]
]


for test in tests:
    print(process(test[0], 0), test[1])

print(process(open("input.txt", "r").read(), 0, -1))
