class Character:
    def __init__(self, hp, base_damage, base_armor):
        self.max_hp = hp
        self.hp = hp
        self.base_dmg = base_damage
        self.mod_dmg = 0
        self.base_armor = base_armor
        self.mod_armor = 0
        self.equipment = {}
        self.cost = 0

    def attack(self, other):
        damage_capacity = self.base_dmg + self.mod_dmg
        armor_capacity = other.base_armor + other.mod_armor
        if damage_capacity > armor_capacity:
            other.hp -= (damage_capacity - armor_capacity)
            return "dealt {} damage ({} - {})".format(damage_capacity - armor_capacity, damage_capacity, armor_capacity)


def fight(fighter_1, fighter_2):
    while fighter_1.hp > 0 and fighter_2.hp > 0:
        fighter_1.attack(fighter_2)
        if fighter_2.hp > 0:
            fighter_2.attack(fighter_1)

    if fighter_1.hp > 0:
        return True
    return False


input_file = open("shop.txt", "r").read().split("\n")
category = ""
shop = {}
for line in input_file:
    tokens = line.split()
    if len(tokens) == 0:
        continue

    if ":" in tokens[0]:
        category = tokens[0][:len(tokens[0])-1]
        shop[category] = []
    elif category != "Rings":
        description = tokens[0]
        cost = int(tokens[1])
        damage = int(tokens[2])
        armor = int(tokens[3])
        shop[category].append((description, cost, damage, armor))
    elif category == "Rings":
        description = tokens[0] + " " + tokens[1]
        cost = int(tokens[2])
        damage = int(tokens[3])
        armor = int(tokens[4])
        shop[category].append((description, cost, damage, armor))

# print(shop)

winning_spend = 999999
winning_set = None

for weapon in shop["Weapons"]:
    w, wc, wd, wa = weapon
    for armor in shop["Armor"]:
        a, ac, ad, aa = armor
        for ring1 in shop["Rings"]:
            r1, r1c, r1d, r1a = ring1
            for ring2 in shop["Rings"]:
                r2, r2c, r2d, r2a = ring2
                cost = wc + ac + r1c + r2c
                dmg = wd + ad + r1d + r2d
                arm = wa + aa + r1a + r2a

                boss = Character(104, 8, 1)
                player = Character(100, 0, 0)
                player.mod_dmg = dmg
                player.mod_armor = arm
                if fight(player, boss):
                    # print(w, a, r1, r2)
                    if cost < winning_spend:
                        winning_spend = cost
                        winning_set = (w, a, r1, r2)


print("Least you can spend and win: ", winning_spend)
print("What you can win with: ", winning_set)


losing_spend = 0
losing_set = None

for weapon in shop["Weapons"]:
    w, wc, wd, wa = weapon
    for armor in shop["Armor"]:
        a, ac, ad, aa = armor
        for ring1 in shop["Rings"]:
            r1, r1c, r1d, r1a = ring1
            for ring2 in shop["Rings"]:
                r2, r2c, r2d, r2a = ring2
                cost = wc + ac + r1c + r2c
                dmg = wd + ad + r1d + r2d
                arm = wa + aa + r1a + r2a

                boss = Character(104, 8, 1)
                player = Character(100, 0, 0)
                player.mod_dmg = dmg
                player.mod_armor = arm
                if not fight(player, boss):
                    # print(w, a, r1, r2)
                    if cost > losing_spend:
                        losing_spend = cost
                        losing_set = (w, a, r1, r2)

print("Most you can spend and lose: ", losing_spend)
print("What you lost with: ", losing_set)
