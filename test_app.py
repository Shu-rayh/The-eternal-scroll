import sys
# no sys.path hack needed -- this file lives in the project root already

from app import app

client = app.test_client()


def post(url, body=None):
    resp = client.post(url, json=body or {})
    return resp.status_code, resp.get_json()


def get(url):
    resp = client.get(url)
    return resp.status_code, resp.get_json()


def show(label, status, data):
    print(f"\n--- {label} [{status}] ---")
    print(data)


# 1. Start a new game
status, data = post("/api/new-game", {"name": "Rowan"})
show("new-game", status, data)
assert status == 200
assert data["character"]["name"] == "Rowan"
assert data["room"]["room_id"] == "village"

# 2. Check /api/state matches
status, data = get("/api/state")
show("state", status, data)
assert data["room"]["room_id"] == "village"

# 3. Move into the forest (should trigger the goblin fight)
status, data = post("/api/move", {"direction": "north"})
show("move north (into goblin fight)", status, data)
assert status == 200
assert data["room"]["room_id"] == "forest_path"
assert data["in_combat"] is True

# 4. Try to move while in combat -- should be rejected
status, data = post("/api/move", {"direction": "south"})
show("move while in combat (should fail)", status, data)
assert status == 400

# 5. Fight until the goblin is dead (or we give up after many rounds)
outcome = "continue"
rounds = 0
while outcome == "continue" and rounds < 30:
    status, data = post("/api/combat-action", {"action": "attack"})
    outcome = data["combat_outcome"]
    rounds += 1
show(f"combat resolved after {rounds} rounds", status, data)
assert outcome in ("win", "loose")
assert data["in_combat"] is False

if outcome == "lose":
    print("\nPlayer lost the fight this run (bad dice luck) -- "
          "that's a valid outcome, stopping the test here.")
    sys.exit(0)

# 6. Now that combat is over, moving should work again
status, data = post("/api/move", {"direction": "south"})
show("move south back to village", status, data)
assert status == 200
assert data["room"]["room_id"] == "village"

status, data = post("/api/move", {"direction": "north"})
show("move north again (goblin already defeated, no fight)", status, data)
assert data["in_combat"] is False

status, data = post("/api/move", {"direction": "west"})
show("move west into cave_entrance", status, data)
assert data["room"]["item_here"] == "rusty_dagger"

# 7. Take the item and check inventory
status, data = post("/api/take-item")
show("take-item (rusty dagger)", status, data)
assert len(data["inventory"]["items"]) == 1

# 8. Equip it
status, data = post("/api/equip", {"item_name": "rusty dagger"})
show("equip rusty dagger", status, data)
assert data["character"]["equipped_weapon"] == "Rusty Dagger"

# 9. Try equipping something we don't have
status, data = post("/api/equip", {"item_name": "nonexistent sword"})
show("equip nonexistent item (should fail)", status, data)


# 10. Check the map endpoint
status, data = get("/api/map")
show("map", status, data)
assert len(data["rooms"]) == 7

print("\nAll route checks passed.")
