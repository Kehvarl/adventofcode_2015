defaultenemy = [55, 8, 0]
mystats = [50, 0, 0, 500]
spells = [[53, 1, 0, 4, 0, 0], [113, 6, 0, 0, 7, 0], [173, 6, 0, 3, 0, 0], [229, 5, 0, 0, 0, 101], [73, 1, 2, 2, 0, 0]]
mana_threshold = 229 + 179


def tester(max_armor, max_poison, max_regen, max_drain, mana_threshold):
    spell_timers = [0, 0, 0, 0]
    player = mystats[:]
    enemy = defaultenemy[:]
    armor_cast = 0
    poison_cast = 0
    regen_cast = 0
    drain_cast = 0
    tm_used = 0
    while player[0] > 1 and enemy[0] > 0:

        player[0] -= 1  # Hard Mode

        player[1] = 0
        player[2] = 0;
        for index in range(len(spell_timers)):
            if spell_timers[index] > 0:
                for i in range(4):
                    player[i] += spells[index][2 + i]
                spell_timers[index] -= 1
        enemy[0] -= max(0, player[1] - enemy[2])

        # Spells cast here
        if enemy[0] <= spells[0][3]:
            # Magic missile
            enemy[0] -= spells[0][3]  # Dead
            tm_used += spells[0][0]
            player[3] -= spells[0][0]
        elif spell_timers[3] == 0 and player[3] < mana_threshold and regen_cast < max_regen:
            spell_timers[3] = spells[3][1]
            tm_used += spells[3][0]
            player[3] -= spells[3][0]
            regen_cast += 1
        elif spell_timers[2] == 0 and poison_cast < max_poison:
            spell_timers[2] = spells[2][1]
            tm_used += spells[2][0]
            player[3] -= spells[2][0]
            poison_cast += 1
        elif spell_timers[1] == 0 and armor_cast < max_armor:
            spell_timers[1] = spells[1][1]
            tm_used += spells[1][0]
            player[3] -= spells[1][0]
            armor_cast += 1
        elif drain_cast < max_drain:
            enemy[0] -= spells[4][3]
            tm_used += spells[4][0]
            player[3] -= spells[4][0]
            player[0] += spells[4][2]
            drain_cast += 1
        else:
            enemy[0] -= spells[0][3]
            tm_used += spells[0][0]
            player[3] -= spells[0][0]

        if player[3] < 0:
            if regen_cast != max_regen:
                print("Mana less than zero!")
            return None
        if enemy[0] <= 0:
            return tm_used

        player[1] = 0
        player[2] = 0;
        for index in range(len(spell_timers)):
            if spell_timers[index] > 0:
                for i in range(4):
                    player[i] += spells[index][2 + i]
                spell_timers[index] -= 1
        # Accounts for spells
        enemy[0] -= max(0, player[1] - enemy[2])
        if enemy[0] <= 0:
            return tm_used
        player[0] -= max(1, enemy[1] - player[2])
    return None


min_used = 10000
for ma in range(5):
    for mp in range(5):
        for mr in range(0, 3):
            for md in range(5):
                test_val = None
                test_val = tester(ma, mp, mr, md, mana_threshold)
                if test_val:
                    if min_used > test_val:
                        min_used = test_val
                        print(test_val)
