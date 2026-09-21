from game.character import make_player
from game.items import ITEM_CATALOGUE
from game.world import build_world
from game.combat import run_combat

HELP = """
Commands:
  go <direction>   - move through an exit (e.g. 'go north')
  look             - redisplay the current room
  take item        - pick up an item in the room, if any
  inventory        - show your bag and gold
  equip <name>     - equip a weapon or armor from your bag (e.g. 'equip short sword')
  use <name>       - use a potion from your bag (e.g. 'use healing potion')
  status           - show your character sheet
  help             - show this list again
  quit             - exit the game
"""

def get_player_combat_action():
    while True:
        choice = input("Combat> (attack / item / flee ) : ").strip().lower()
        if choice in ("attack", "a") :
            return "attack"
        if choice in ("flee", "run", "f") :
            return "flee"
        if choice in ("item", "i") :
            return "item"
        print("Please type 'attack', 'item', or 'flee'.")
def handle_room_entry(player, room):
    print("\n" + room.describe())
    if room.monsters and not room.monster_defeated:
        monster = room.monsters()
        result = run_combat(player, monster, get_player_combat_action)
        if result == "loose":
            return "game_over"
        if result == "win":
            room.monster_defeated = True
            for message in player.gain_xp(50):
                print(message)   
    if room.is_ending:
        print("\n" + room.ending_text)
        return "game_over"
    return "continue"

def handle_command(player, world, current_rooms, command):
    command = command.strip().lower()
    if command in ("help", "h", "?"):
        print(HELP)
    elif command in ("look", "1"):
        print("\n" + current_rooms.describe())
    elif command in ("status", "sheet"):
        print("\n" + player.status_line())
        print(f"Abilities:{player.abbilities}")
    elif command in ("inventory", "inv", "i"):
        print("\n" + player.inventory.list_items())
    elif command == "take item":
        if current_rooms.item_key and not current_rooms.item_taken:
            item = ITEM_CATALOGUE[current_rooms.item_key]
            player.inventory.add_item(item)
            current_rooms.item_take = True
            print(f"You picked up: {item}")
        else:
            print("There appears to be nothing here to take.")   
    elif command.startswith("equip "):
        name = command[len("equip "):]
        item = player.inventory.find_by_name(name)
        if item is None:
            print(f"You don't have a ' {name}'.")
        elif item.item_type == "weapon":
            player.equip_weapon(item)
            print(f"You equip the {item.name}.")
        elif item.item_type == "armor":
            player.equip_armour(item)
            print(f"You equip the {item.name}.")
        else:
            print(f"You can't equip the {item.name}.")
    elif command.startswith("use "):
        name = command[len("use "):]
        item = player.inventory.find_by_name(name)
        if item is None:
            print(f"You don't have a '{name}'.")
        elif item.item_type == "potion":
            player.heal(item.heal_amount)
            player.inventory.remove_item(item)
            print(f"You drink the {item.name} and heal {item.heal_amount} HP.")
            print(player.status_line())
        else:
            print(f"You can't use the {item.name} that way.")
    elif command.startswith("go "):
        direction = command[len("go "):]
        if direction in current_rooms.exits:
            next_room_id = current_rooms.exits[direction]
            return world[next_room_id]
        else:
            print(f"You can't go '{direction}' from here.")

    else:
        print("Unknown command. Type 'help' for a list of commands.")

    return current_rooms

def main():
    print("=" * 50)
    print("  The Eternal Scroll: A 5e-Style Text Adventure (Phase 1)")
    print("=" * 50)
    name = input("What is your character's name? ").strip() or "Adventurer"
    player = make_player(name)
    world = build_world()
    current_room = world["village"]
    print(f"\nWelcome, {player.name}! Type 'help' any time.")
    status = handle_room_entry(player, current_room)
    if status == "game_over":
        return

    while True:
        command = input("\n> ").strip().lower()

        if command in ("quit", "exit", "q"):
            print("Thanks for playing!")
            break

        new_room = handle_command(player, world, current_room, command)
        if new_room is not current_room:
            current_room = new_room
            status = handle_room_entry(player, current_room)
            if status == "game_over":
                break
if __name__ == "__main__":
    main()


   