# The Eternal Scroll
A 5e-Style Text Adventure game made in python.
**Download it here → https://github.com/Shu-rayh/The-eternal-scroll/releases/tag/pre**

## Quick start

1. Open the link above and download the main.exe file.
2. Open the file after download and start playing
3. You'll be asked for a character name, then dropped into the Village of Washbone. Type `help` at any time to see the full command list.

### The current command list:
- go <direction>   - move through an exit (e.g. 'go north')look             - redisplay the current room
- take item        - pick up an item in the room, if any
- inventory        - show your bag and gold
- equip <name>     - equip a weapon or armour from your bag (e.g. 'equip short sword')
- use <name>       - use a potion from your bag (e.g. 'use healing potion')
- status           - show your character sheet
- help             - show this list again
- quit             - exit the game

## Current Features (more coming soon)
- **Ability scores & modifiers**: STR/DEX/CON/INT/WIS/CHA with the standard
  5e `(score - 10) // 2` formula.
- **d20 rolls**: attack rolls, saving throw rolls, with critical hit/fail
  detection on natural 20s/1s.
- **Combat**: attack vs. armour Class, weapon damage dice, flee (DEX check),
  monsters rebuild at full HP if you re-enter a room after fleeing.
- **HP & death**: taking damage, healing potions, `is_alive` check.
- **XP & leveling**: simple threshold table, HP gain on level-up.
- **Inventory**: pick up, equip weapons/armour, use potions.
- **Story branching**: a small but real branching map, not a straight line.

## Testing it yourself

Try to:
1. Fight the goblin on the Forest Path and win.
2. Flee from a fight, leave the room, come back — the goblin should be back
   at full HP.
3. Pick up all three items (dagger, potion, armour), equip the dagger and
   armour, and drink the potion.
4. Reach the Dragon's Lair from BOTH paths (cave route and bridge route).

## Some images
![screenshot](Screenshot (3).webp)
![screenshot](Screenshot (4).webp)
![screenshot](Screenshot (5).webp)

## Run it yourself
```bash
git clone https://github.com/Shu-rayh/The-eternal-scroll
cd The-eternal-scroll
```
## More to come
Eventually I want to have the python game running as a backend to a website where you can play the game, view images of the scenery, view your inventory and view your character sheet.

## Why did I make this?
D&D and coding are 2 things im passionate about and I wanted tto try and build my own Text based adventure game so I thought why not add D&D mechanics.

## How Ai was used
I used claudes assistance for debugging 



