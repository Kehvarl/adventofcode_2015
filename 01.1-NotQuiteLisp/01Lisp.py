
def process(pattern, floor):
    for c in pattern:
        if c == "(":
            floor += 1
        if c == ")":
            floor -= 1
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

print(process(open("input.txt", "r").read(), 0))
