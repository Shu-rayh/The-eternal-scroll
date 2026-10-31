from game.rooms import Room
from game.combat import monster_goblin, monster_skeleton, monster_guard


def build_world():
    world = {}

    """ world[" "] = Room(
        room_id=" ",
        name=" ",
        description=(
            " "
            " "
        ),
        exits={" ": " ", " ": " "},
    ) """
    
    world["village"] = Room(
        room_id="village",
        name="Village of washbone",
        description=(
            "You stand at the edge of a quiet village. Lanterns flicker "
            "in the evening mist. An old signpost points toward a dark forest."
        ),
        exits={"north": "forest_path"},
    )
    
    world["forest_path"] = Room(
        room_id="forest_path",
        name="Forest Path",
        description=(
            "Twisted trees crowd a narrow trail. It splits in two directions: "
            "a damp cave entrance to the west, and a rickety rope bridge to the east."
        ),
        exits={"south": "village", "west": "cave_entrance", "east": "old_bridge"},
        monsters=monster_goblin,
    )
    world["cave_entrance"] = Room(
        room_id="cave_entrance",
        name="Cave Entrance",
        description="Cold air drifts from a dark cave mouth. Something glints on the floor.",
        exits={"east": "forest_path", "north": "treasure_room"},
        item_key="short_sword",
    )
    
    world["old_bridge"] = Room(
        room_id="old_bridge",
        name="Old Rope Bridge",
        description="The bridge sways over a deep ravine. A skeletal figure blocks the far side.",
        exits={"west": "forest_path", "north": "ruined_tower"},
        monsters=monster_skeleton,
    )

    world["treasure_room"] = Room(
        room_id="treasure_room",
        name="Treasure Room",
        description="Dusty chests line the walls. Most are empty, but one holds a healing potion.",
        exits={"south": "cave_entrance", "north": "cave2"},
        item_key="healing_potion",
    )
    
    world["cave2"] = Room(
        room_id="cave2",
        name="cave",
        description="As you walk through the cave you hear a sound",
        exits={"south": "treasure_room", "north": "cave3"},
        monsters=monster_skeleton,
        
    )  

    world["cave3"] = Room(
        room_id="cave3",
        name="cave",
        description="cave",
        exits={"south": "cave2", "north": "cave4"},
        monsters=monster_guard,
        
    )  

    
    world["cave4"] = Room(
        room_id="cave4",
        name="cave",
        description="cave",
        exits={"south": "cave3", "north": "dragon_lair"},
        monsters=monster_goblin,
        
    )  

    

    world["ruined_tower"] = Room(
        room_id="ruined_tower",
        name="Ruined Tower",
        description="A collapsed watchtower. A set of leather armour hangs on a broken rack.",
        exits={"south": "old_bridge", "north": "dragon_lair"},
        item_key="leather_armour",
    )

    world["dragon_lair"] = Room(
        room_id="dragon_lair",
        name="Dragon's Lair",
        description="You stand at the mouth of a great cavern glowing with heat.",
        exits={},
        is_ending=True,
        ending_text=(
            "You've reached the Dragon's Lair and lived to tell the tale. "
            " "
        ),
    )

    world["dungeon"] = Room(
        room_id="dungeon",
        name="cavedungeon",
        description="Both paths converge here, at the mouth of a great cavern glowing with heat.",
        exits={},
        is_ending=True,
        ending_text=(
            "You've reached the Dragon's Lair and lived to tell the tale. "
            " "
        ),
    )
    return world

