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


# Name, Mana_Cost, Damage, Heal, Armor, Duration, Mana_Gain
spells = [
    ("Magic Missile", 53, 4, 0, 0, 0, 0),
    ("Drain", 73, 2, 2, 0, 0, 0),
    ("Shield", 113, 0, 0, 7, 6, 0),
    ("Poison", 173, 3, 0, 7, 6, 0),
    ("Recharge", 229, 0, 0, 7, 5, 101),
]


