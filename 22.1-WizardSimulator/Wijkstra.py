from collections import deque
import copy


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
    # Name, Mana_Cost, Damage, Heal, Armor, Duration, Mana_Gain
    if spell[1] > state["player_mana"]:
        return False
    for effect in state["effects"]:
        if effect[0] == spell[0]:
            return False
    return True


def cast(spell, state):
    # Name, Mana_Cost, Damage, Heal, Armor, Duration, Mana_Gain
    if spell[5] > 0:
        state["effects"].add(spell)
        state["player_armor"] += spell[4]
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
    state["player_hp"] -= max(0, dmg)
    return state


def game_over(state):
    return (state["player_hp"] <= 0 or
            state["player_mana"] <= 0 or
            state["boss_hp"] <= 0 or
            state["mana_spent"] >= lowest_spend)


# Name, Mana_Cost, Damage, Heal, Armor, Duration, Mana_Gain
spells = [
    ("Magic Missile", 53, 4, 0, 0, 0, 0),
    ("Drain", 73, 2, 2, 0, 0, 0),
    ("Shield", 113, 0, 0, 7, 6, 0),
    ("Poison", 173, 3, 0, 0, 6, 0),
    ("Recharge", 229, 0, 0, 0, 5, 101),
]

# Boss = 55 HP; 8 DMG
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

lowest_spend = 999999
bfs = deque([initial_state])

while bfs:
    working_state = bfs.popleft()
    working_state["player_hp"] -= 1
    working_state = process_effects(working_state)

    for castable in spells:
        if can_cast(castable, working_state) and working_state["player_hp"] > 0:
            tmp_state = boss_hit(process_effects(cast(castable, copy.deepcopy(working_state))))
            if not game_over(tmp_state):
                bfs.append(tmp_state)
            elif tmp_state["boss_hp"] <= 0:
                if tmp_state["mana_spent"] <= lowest_spend:
                    lowest_spend = tmp_state["mana_spent"]

print(lowest_spend)
