
def parse_line(input_line):
    parsed_name, rest = input_line.split(":")
    rest = rest.split(",")
    properties = {}
    for token in rest:
        p, v = token.strip().split(" ")
        if p not in properties:
            properties[p] = int(v)

    return parsed_name, properties


def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation


def calculate(ingredient_to_calculate, measure):
    calc_capacity = ingredient_to_calculate['capacity'] * measure
    calc_durability = ingredient_to_calculate['durability'] * measure
    calc_flavor = ingredient_to_calculate['flavor'] * measure
    calc_texture = ingredient_to_calculate['texture'] * measure
    calc_calories = ingredient_to_calculate['calories'] * measure

    return calc_capacity, calc_durability, calc_flavor, calc_texture, calc_calories


input_file = open("input.txt", "r").read().split("\n")

ingredients = {}

for line in input_file:
    p_name, p_props = parse_line(line)
    ingredients[p_name] = p_props

print(ingredients)

recipes = sums(len(ingredients), 100)

best = 0
for recipe in recipes:
    total_capacity = 0
    total_durability = 0
    total_flavor = 0
    total_texture = 0
    total_calories = 0
    index = 0
    for name in ingredients:

        ingredient = ingredients[name]
        amount = recipe[index]
        capacity, durability, flavor, texture, calories = calculate(ingredient, amount)

        total_capacity += capacity
        total_durability += durability
        total_flavor += flavor
        total_texture += texture
        total_calories += calories
        index += 1

    if total_capacity <= 0 or total_durability <= 0 or total_flavor <= 0 or total_texture <= 0:
        continue
    elif total_calories == 500:
        current = total_capacity * total_durability * total_flavor * total_texture
        best = max(best, current)

print(best)
