from game.dice import roll_d20, roll_dice, ability_modifier
from game.items import Inventory

xp_thresholds = {
    1: 0,
    2: 300,
    3: 900,
    4: 2700,
    5: 6500,
}
proficiency_bonus = 2

class Character:
    def __init__(self, name, abilities, hit_die=8, base_ac=10,
                proficiency_saves=None, is_player=False):
        self.name = name
        self.abbilities = abilities
        self.hit_dice = hit_die
        self.level = 1
        self.xp = 0
        self.proficiency_saves = proficiency_saves or []
        self.is_player = is_player
        con_mod = self.modifier("CON")
        self.max_hp = hit_die + con_mod
        self.hp = self.max_hp
        self.base_ac = base_ac
        self.inventory = Inventory()
        self.equipped_weapon = None
        self.equipped_armor = None
    def modifier(self, ability_name):
        return ability_modifier(self.abbilities[ability_name])
    
    @property
    def armour_class(self):
        bonus = self.equipped_armor.ac_bonus if self.equipped_armor else 0
        return self.base_ac + self.modifier("DEX") + bonus
    @property
    def is_alive(self):
        return self.hp > 0
    def attack_roll(self, ability_name="STR"):
        mod = self.modifier(ability_name) + proficiency_bonus
        return roll_d20(mod)
    def damage_roll(self, ability_name="STR"):
        if self.equipped_weapon:
            dice, sides = self.equipped_weapon.damage_dice, self.equipped_weapon.damage_sides
        else:
            dice, sides = 1, 4
        return roll_dice(dice, sides, self.modifier(ability_name))
    def saving_throw(self, ability_name, dc):
        mod = self.modifier(ability_name)
        if ability_name in self.proficiency_saves:
            mod += proficiency_bonus
        result = roll_d20(mod)
        return result["total"] >= dc, result
    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)  
    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        
    def equip_weapon(self, item):
        self.equipped_weapon = item 
    def equip_armor(self, item):
        self.equipped_armor = item
    def gain_xp(self, amount):
        self.xp += amount
        messages = [f"{self.name} gains {amount} XP"]
        next_level = self.level + 1
        while next_level in xp_thresholds and self.xp >= xp_thresholds[next_level]:
            self.level_up()
            messages.append(f"*** {self.name} reached level {self.level}! ***")
            next_level = self.level + 1
        return messages
    def level_up(self):
        self.level += 1
        con_mod = self.modifier("CON")
        hp_gain = roll_dice(1, self.hit_dice, con_mod)
        hp_gain = max(1, hp_gain)
        self.max_hp += hp_gain
        self.hp = self.max_hp
    def status_line(self):
        return (f"{self.name} | Lv{self.level} | "
                f"Hp {self.hp}/{self.max_hp} | AC {self.armour_class}")

def make_player(name):
    abilities = {"STR": 14, "DEX":12, "CON": 13, "INT": 10, "WIS": 11, "CHA": 8,}
    player = Character(
        name = name,
        abilities=abilities,
        hit_die=10,
        base_ac=10,
        proficiency_saves=["STR", "CON"],
        is_player=True,
    )       
    return player
        