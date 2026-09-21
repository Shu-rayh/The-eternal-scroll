from game.rooms import Room
from game.combat import monster_goblin, monster_skeleton


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
        item_key="rusty_dagger",
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
        exits={"south": "cave_entrance", "north": "dragon_lair"},
        item_key="healing_potion",
    )

    world["ruined_tower"] = Room(
        room_id="ruined_tower",
        name="Ruined Tower",
        description="A collapsed watchtower. A set of leather armor hangs on a broken rack.",
        exits={"south": "old_bridge", "north": "dragon_lair"},
        item_key="leather_armor",
    )

    world["dragon_lair"] = Room(
        room_id="dragon_lair",
        name="Dragon's Lair",
        description="Both paths converge here, at the mouth of a great cavern glowing with heat.",
        exits={},
        is_ending=True,
        ending_text=(
            "You've reached the Dragon's Lair and lived to tell the tale. "
            " "
        ),
    )

    return world

