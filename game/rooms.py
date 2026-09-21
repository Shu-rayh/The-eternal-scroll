class Room:
    def __init__(self, room_id, name, description, exits=None,
               monsters=None, item_key=None, is_ending=False, ending_text=None) :
        self.room_id = room_id
        self.name = name
        self.description = description
        self.exits = exits or {}
        self.monsters = monsters
        self.item_key = item_key
        self.monster_defeated = False
        self.is_ending = is_ending
        self.ending_text = ending_text
        self.item_taken = False
    def describe(self) :
        lines = [f"== {self.name} ==", self.description]
        if self.item_key and not self.item_taken:
            lines.append(f"There is something here: a {self.item_key.replace('_', ' ')}. (try 'take item')")
        if self.exits:
            lines.append("Exits: " + ", ".join(self.exits.keys()))
        return "\n".join(lines)