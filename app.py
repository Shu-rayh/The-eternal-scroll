import uuid
from flask import Flask, request, jsonify, session
from game.character import make_player
from game.items import ITEM_CATALOGUE
from game.world import build_world
from game.combat import resolve_round

app = Flask(__name__)
app.secret_key = "1234567"
GAMES = {}

def get_game():
    game_id = session.get("game_id")
    if game_id is None:
        return None
    return GAMES.get(game_id)

def enter_room(game):
    room = game["world"][game["current_room_id"]]
    if room.monsters and not room.monster_defeated and game["current_monster"] is None:
        game["current_monster"] = room.monsters()
        
def build_state(game):
    player = game["player"]
    room = game["world"][game["current_room_id"]]
    monster = game["current_monster"]
    return {
        "room": {
            "room_id": room.room_id,
            "name": room.name,
            "description": room.description,
            "exits": list(room.exits.keys()),
            "item_here": room.item_key if (room.item_key and not room.item_taken) else None,
            "is_ending": room.is_ending,
            "ending_text": room.ending_text if room.is_ending else None,
            
        },
        "character": player.to_dict(),
        "inventory": player.inventory.to_dict(),
        "in_combat": monster is not None,
        "monster": ({
            "name": monster.name,
            "hp": monster.hp,
            "max_hp": monster.max_hp,
            "armour_class": monster.armour_class,
        }if monster else None),
        "game_over": not player.is_alive,
    }


@app.route("/api/new-game", methods=["POST"])
def new_game():
    data = request.get_json(silent=True) or {}
    name = data.get("name", "Adventurer").strip() or "Adventurer"
    game_id = str(uuid.uuid4())
    session["game_id"] = game_id
    game = {
        "player": make_player(name),
        "world": build_world(),
        "current_room_id": "village",
        "current_monster": None,}
    GAMES[game_id] = game
    enter_room(game)
    return jsonify(build_state(game))

@app.route("/api/state", methods=["GET"])
def state():
    game = get_game()
    if game is None:
        return jsonify({"error": "No active game, please create one"}), 400
    return jsonify(build_state(game))

@app.route("/api/move", methods=["POST"])
def move():
    game = get_game()
    data = request.get_json(silent=True) or {}
    direction = data.get("direction", " ").strip().lower()
    room = game["world"][game["current_room_id"]]
    game["current_room_id"] = room.exits[direction]
    enter_room(game)
    return jsonify(build_state(game))

@app.route("/api/take-item", methods=["POST"])
def take_item():
    game = get_game()    
    room = game["world"][game["current_room_id"]]
    item = ITEM_CATALOGUE[room.item_key]
    game["player"].inventory.add_item(item)
    room.item_taken = True
    return jsonify(build_state(game))

@app.route("/api/equip", methods=["POST"])
def equip():
    game = get_game() 
    data = request.get_json(silent=True) or {}
    item_name = data.get("item_name", " ")
    player = game["player"]
    item = player.inventory.find_by_name(item_name)
    if item.item_type == "weapon":
        player.equip_weapon(item)
    elif item.item_type == "armour":
        player.equip_armour(item)
    return jsonify(build_state(game))

@app.route("/api/use-item", methods=["POST"])
def use_item():
    game = get_game()
    data = request.get_json(silent=True) or {}
    item_name = data.get("item_name", " ")
    player = game["player"]
    item = player.inventory.find_by_name(item_name)
    player.heal(item.heal_amount)
    player.inventory.remove_item(item)
    return jsonify(build_state(game))

@app.route("/api/combat-action", methods=["POST"])
def combat_action():
    game = get_game()
    monster = game["current_monster"]
    data = request.get_json(silent=True) or {}
    action = data.get("action", " ")
    result = resolve_round(game["player"], monster, action)
    if result["outcome"] == "win":
        room = game["world"][game["current_room_id"]]
        room.monster_defeated = True
        game["current_monster"] = None
        result["log"] += game["player"].gain_xp(50)
    elif result["outcome"] in ("flee", "lose"):
        game["current_monster"] = None
    
    response = build_state(game)
    response["combat_outcome"] = result["outcome"]
    return jsonify(response)

@app.route("/api/map", methods=["GET"])
def map_data():
    game = get_game()
    rooms = [ ]
    for room_id, room in game["world"].items():
        rooms.append({"room_id": room_id,
                      "name": room.name,
                      "exits": room.exits,
                      })
        
    return jsonify({"rooms": rooms, "current_room_id": game["current_room_id"]})


if __name__ == "__main__":
    app.run(debug=True)
    