from itertools import permutations
from collections import deque
from random import choice


class Character:
    def __init__(self, hp, base_damage, base_armor, mana):
        self.max_hp = hp
        self.hp = hp
        self.max_mana = mana
        self.mana = mana
        self.base_dmg = base_damage
        self.mod_dmg = 0
        self.base_armor = base_armor
        self.mod_armor = 0
        self.equipment = {}
        self.cost = 0
        self.effects = []

    def process_effects(self, other):
        if len(self.effects) > 0:
            for i in range(len(self.effects)):
                effect = self.effects[i]
                effect[5] -= 1
                other.hp -= effect[2]
                self.hp += effect[3]
                self.mana += effect[6]
                if effect[5] <= 0:
                    self.mod_armor -= effect[4]

            for i in range(len(self.effects), 0, -1):
                effect = self.effects[i]
                if effect[5] <= 0:
                    self.effects.remove(effect)

    def attack(self, other):
        damage_capacity = self.base_dmg + self.mod_dmg
        armor_capacity = other.base_armor + other.mod_armor
        if damage_capacity > armor_capacity:
            other.hp -= (damage_capacity - armor_capacity)
            return "dealt {} damage ({} - {})".format(damage_capacity - armor_capacity,
                                                      damage_capacity,
                                                      armor_capacity)

    def spell_in_use(self, spell_name):
        for effect in self.effects:
            if effect[0] == spell_name:
                return True
        return False

    def cast(self, other, spell):
        if spell[5] > 0:
            if not self.spell_in_use(spell[0]):
                self.effects.append(spell)
        else:
            other.hp -= spell[2]
            self.hp += spell[3]


def Wiz_AI(wiz, other):
    spell = choice(spells)
    while wiz.spell_in_use(spell[0]) or spell[1] >= wiz.mana:
        spell = choice(spells)

    return spell


def NoAI(other, wiz):

    if other.hp <= 4:
        return spells[0] # Magic Missile
    elif wiz.hp <= (other.base_dmg - wiz.mod_armor):
        if not wiz.spell_in_use(spells[2][0]): # Not shielding
            return spells[3] # Shield!!
        else:
            return spells[1] # Drain, I guess
    elif wiz.mana <= 113:
        return spells[4] # Get More Mana
    elif not wiz.spell_in_use(spells[3][0]): #Not Poisoned?
        return spells[3]
    return spells[0]  # Magic Missile



# Name, Mana_Cost, Damage, Heal, Armor, Duration, Mana_Gain
spells = [
    ("Magic Missile", 53, 4, 0, 0, 0, 0),
    ("Drain", 73, 2, 2, 0, 0, 0),
    ("Shield", 113, 0, 0, 7, 6, 0),
    ("Poison", 173, 3, 0, 7, 6, 0),
    ("Recharge", 229, 0, 0, 7, 5, 101),
]

while False:
    spell_chains = permutations([x % 5 for x in range(25)], 15)

    lowest_spend = 999999
    lowest_chain = None

    for chain in spell_chains:
        working_chain = deque(chain)

lowest_spend = 999999
for _ in range(1000000):

    # Boss = 55 HP; 5 DMG
    # Player = 50 HP; 500 MANA
    Boss = Character(55, 5, 0, 0)
    Player = Character(50, 0, 0, 500)

    spent_mana = 0

    while Player.hp > 0 and Player.mana > 0 and Boss.hp > 0:
        spell = Wiz_AI(Player, Boss)
        spent_mana += spell[1]
        Player.cast(Boss, spell)
        if Boss.hp > 0:
            Boss.attack(Player)

    if Player.hp > 0 and Player.mana > 0:
        if spent_mana < lowest_spend:
            lowest_spend = spent_mana
            # lowest_chain = chain

print(lowest_spend)  # , lowest_chain)
