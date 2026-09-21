from game.dice import roll_d20

def attempt_attack(attacker, defender, ability_name="STR"):
    roll = attacker.attack_roll(ability_name)
    target_ac = defender.armour_class
    if roll["critical_fail"]:
        return f"{attacker.name} rolls a natural 1 and completely misses!"
    hit = roll["critical_hit"] or roll["total"] >= target_ac
    if not hit:
        return (f"{attacker.name} attacks {defender.name}: "
                f"rolled {roll['total']} vs AC {target_ac} -- MISS.")
    damage = attacker.damage_roll(ability_name)
    if roll["critical_hit"]:
        damage *= 2 
    defender.take_damage(damage)
    crit_text = " CRITICAL HIT!" if roll["critical_hit"] else ""
    return (f"{attacker.name} attacks {defender.name}: "
            f"rolled {roll['total']} vs AC {target_ac} -- HIT for {damage} damage!"
            f"{crit_text}")
def run_combat(player, monster, get_player_action):
    print(f"\n--- A {monster.name} attacks! ---")
    print(monster.status_line())
    while player.is_alive and monster.is_alive:
        print(f"\n{player.status_line()}")
        action = get_player_action()
        if action == "attack":
            print(attempt_attack(player, monster, ability_name="STR"))
        elif action == "flee":
            flee_roll = roll_d20(player.modifier("DEX"))
            if flee_roll["total"] >= 12:
                print(f"{player.name} escapes successfully!")
                return "flee"
            else:
                print(f"{player.name} fails to escape!")
        else:
            print("You hesitate and lose your turn.")
        if not monster.is_alive:
            break
        print(attempt_attack(monster, player, ability_name="STR"))
    if not player.is_alive:
        print(f"\n{player.name} has fallen...")
        return "lose"
    print(f"\nThe {monster.name} is defeated!")
    return "win"

"""def monster_(monster name)():
    from game.character import Character
    (name) = Character(
        name=" ",
        abilities={"STR": , "DEX": , "CON": , "INT": , "WIS": , "CHA": },
        hit_die=,
        base_ac=,
    )
    from game.items import Item
    (name).equip_weapon(Item("(item name)", "", "(type)", damage_dice=1, damage_sides=(dice sides)))
    return (name)"""

def monster_goblin():
    from game.character import Character
    goblin = Character(
        name="Goblin",
        abilities={"STR": 8, "DEX": 14, "CON": 10, "INT": 8, "WIS": 8, "CHA": 8},
        hit_die=6,
        base_ac=12,
    )
    from game.items import Item
    goblin.equip_weapon(Item("Rusty Scimitar", "", "weapon", damage_dice=1, damage_sides=6))
    return goblin

def monster_skeleton():
    from game.character import Character
    from game.items import Item
    skeleton = Character(
        name="Skeleton",
        abilities={"STR": 12, "DEX": 12, "CON": 12, "INT": 6, "WIS": 8, "CHA": 5},
        hit_die=8,
        base_ac=13,
    )
    skeleton.equip_weapon(Item("Bone Shortsword", "", "weapon", damage_dice=1, damage_sides=6))
    return skeleton


    
        