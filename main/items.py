class Item:

    def __init__(self, name, description, item_type="misc", value=0,
                 damage_dice=None, damage_sides=None, heal_amount=0, ac_bonus=0):
        self.name = name
        self.description = description
        self.item_type = item_type      
        self.value = value              
        self.damage_dice = damage_dice  
        self.damage_sides = damage_sides  
        self.heal_amount = heal_amount  
        self.ac_bonus = ac_bonus        

    def __str__(self):
        return f"{self.name} - {self.description}"
    
class Inventory:
    def _init_(self) :
        self.items =[]
        self.gold = 0
        
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def find_by_name(self, name):
        name = name.lower()
        for item in self.items:
            if item.name.lower() ==name:
                return item
            return None
        
    def list_items(self):
        if not self.items:
            return "Your bag is empty."
        lines = [f"Gold: {self.gold}"]
        for item in self.items:
            lines.append(f" - {item}")
        return "\n".join(lines)
    
    
ITEM_CATALOGUE = {
    "rusty_dagger": Item(
        "Rusty Dagger", "A pitted blade, but still sharp enough.",
        item_type="weapon", value=2, damage_dice=1, damage_sides=4,
    ),
    "short_sword": Item(
        "Short Sword", "A reliable blade favored by adventurers.",
        item_type="weapon", value=10, damage_dice=1, damage_sides=6,
    ),
    "healing_potion": Item(
        "Healing Potion", "A red liquid that mends wounds.",
        item_type="potion", value=15, heal_amount=10,
    ),
    "leather_armor": Item(
        "Leather Armor", "Light armor made of boiled leather.",
        item_type="armor", value=8, ac_bonus=1,
    ),
    "rusty_key": Item(
        "Rusty Key", "It might open something nearby.",
        item_type="key", value=0,
    ),
}
