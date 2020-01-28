# Name, Mana_Cost, Damage, Heal, Armor, Duration, Mana_Gain
spells = [
    ("Magic Missile", 53, 4, 0, 0, 0, 0),
    ("Drain", 73, 2, 2, 0, 0, 0),
    ("Shield", 113, 0, 0, 7, 6, 0),
    ("Poison", 173, 3, 0, 7, 6, 0),
    ("Recharge", 229, 0, 0, 7, 5, 101),
]

# Boss = 55 HP; 5 DMG
# Player = 50 HP; 500 MANA

initial_state = {
    "effects": set(),
    "player_hp": 50,
    "player_mana": 500,
    "player_armor": 0,
    "boss_hp": 55,
    "boss_dmg": 8,
    "mana_spent": 0,
    "spells": []
}


def process_effects(state):
    # Name, Mana_Cost, Damage, Heal, Armor, Duration, Mana_Gain
    output = set()
    while state["effects"]:
        effect = state["effects"].pop()
        state["boss_hp"] -= effect[2]
        state["player_hp"] += effect[3]
        state["player_mana"] += effect[6]
        if effect[5] - 1 > 0:
            eff = (effect[0], effect[1], effect[2], effect[3], effect[4], effect[5] - 1, effect[6])
            output.add(eff)
        else:
            state["player_armor"] -= effect[4]

    state["effects"] = output

    return state


def can_cast(spell, state):
    for effect in state["effects"]:
        if effect[0] == spell[0]:
            return False
    if spell[1] > state["player_mana"]:
        return False
    return True


def cast(spell, state):
    if spell[5] > 0:
        state["effects"].add(spell)
    else:
        state["boss_hp"] -= spell[2]
        state["player_hp"] += spell[3]
    state["spells"].append(spell)
    state["player_mana"] -= spell[1]
    state["mana_spent"] += spell[1]

    return state


def boss_hit(state):
    if state["boss_hp"] <= 0:
        return state
    dmg = state["boss_dmg"] - state["player_armor"]
    state["player_hp"] -= dmg
    return state


def game_over(state):
    return not (state["player_hp"] > 0 and
                state["player_mana"] > 0 and
                state["boss_hp"] > 0 and
                state["mana_spent"] <= lowest_spend)


def bfs(state):
    state = process_effects(state)
    for spell in spells:
        if can_cast(spell, state):
            tmp = boss_hit(cast(spell, state.copy()))
            if not game_over(tmp):
                bfs(tmp)
            elif tmp["boss_hp"] <= 0:
                print(tmp["mana_spent"], tmp["player_hp"], tmp["player_mana"], tmp["boss_hp"])
                global lowest_spend
                if tmp["mana_spent"] <= lowest_spend:
                    lowest_spend = tmp["mana_spent"]
                    print(tmp["mana_spent"])


lowest_spend = 999999
bfs(initial_state)

print(lowest_spend)
