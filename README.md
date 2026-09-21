# The Eternal Scroll:
A 5e-Style Text Adventure game made in python.

## How to run it

```bash
python3 main.py
```

You'll be asked for a character name, then dropped into the Village of Washbone. Type `help` at any time to see the full command list.
### The current command list:
- go <direction>   - move through an exit (e.g. 'go north')look             - redisplay the current room
- take item        - pick up an item in the room, if any
- inventory        - show your bag and gold
- equip <name>     - equip a weapon or armor from your bag (e.g. 'equip short sword')
- use <name>       - use a potion from your bag (e.g. 'use healing potion')
- status           - show your character sheet
- help             - show this list again
- quit             - exit the game


## What's implemented

- **Ability scores & modifiers**: STR/DEX/CON/INT/WIS/CHA with the standard
  5e `(score - 10) // 2` formula.
- **d20 rolls**: attack rolls, saving throw rolls, with critical hit/fail
  detection on natural 20s/1s.
- **Combat**: attack vs. Armor Class, weapon damage dice, flee (DEX check),
  monsters rebuild at full HP if you re-enter a room after fleeing.
- **HP & death**: taking damage, healing potions, `is_alive` check.
- **XP & leveling**: simple threshold table, HP gain on level-up.
- **Inventory**: pick up, equip weapons/armor, use potions.
- **Story branching**: a small but real branching map, not a straight line.


## Testing it yourself

Try to:
1. Fight the goblin on the Forest Path and win.
2. Flee from a fight, leave the room, come back — the goblin should be back
   at full HP.
3. Pick up all three items (dagger, potion, armor), equip the dagger and
   armor, and drink the potion.
4. Reach the Dragon's Lair from BOTH paths (cave route and bridge route).


