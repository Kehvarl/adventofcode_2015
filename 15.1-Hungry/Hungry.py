
def parse_line(input_line):
    name, rest = input_line.split(":")
    rest = rest.split(",")
    properties = {}
    for token in rest:
        p, v = token.strip().split(" ")
        if p not in properties:
            properties[p] = int(v)

    return name, properties


def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation


def calculate(ingredient, measure):
    capacity = ingredient['capacity'] * measure
    durability = ingredient['durability'] * measure
    flavor = ingredient['flavor'] * measure
    texture = ingredient['texture'] * measure

    return capacity, durability, flavor, texture


input_file = open("input.txt", "r").read().split("\n")

ingredients = {}

for line in input_file:
    pname, pprops = parse_line(line)
    ingredients[pname] = pprops

print(ingredients)

recipes = sums(len(ingredients), 100)

best = 0
for recipe in recipes:
    total_capacity = 0
    total_durability = 0
    total_flavor = 0
    total_texture = 0
    index = 0
    for name in ingredients:

        ingredient = ingredients[name]
        amount = recipe[index]
        capacity, durability, flavor, texture = calculate(ingredient, amount)

        total_capacity += capacity
        total_durability += durability
        total_flavor += flavor
        total_texture += texture
        index += 1

    if total_capacity <= 0 or total_durability <= 0 or total_flavor <= 0 or total_texture <= 0:
        continue
    else:
        current = total_capacity * total_durability * total_flavor * total_texture
        best = max(best, current)

print(best)
