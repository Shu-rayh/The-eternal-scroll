from flask import Flask, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "dev-only-secret"
@app.route("/hello")
def hello():
    return "Hello shurayh"

@app.route("/greet/<name>")
def greet(name):
    return f"welcome, {name} !"

@app.route("/roll")
def roll():
    return f"{random.randint(1, 20)}"

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json(silent=True) or {}
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"sum": a + b, "inputs": {"a": a, "b": b}})

@app.route("/coins", methods=["GET"])
def get_coins():
    return jsonify({"coins": -42})

@app.route("/coins/spend", methods=["POST"])
def spend_coins():
    coins = 500
    cost = 100
   
    if cost > coins and coins > 0:
        return jsonify({"error": "Not enough cpoins"}), 400
    elif coins < 0:
        return jsonify({"error": "You owe money!"}), 400
    return jsonify({"coins": coins - cost})

@app.route("/visit")
def visit ():
    count = session.get("visits", 0) + 1
    session["visits"] = count
    return f"Youve visited {count} time(s)."


STORAGE = {}
def save_score(player_id, score):
    STORAGE[player_id] = score
    
def get_score(player_id):
    return STORAGE.get(player_id, 0)

save_score("abc123", 50)
save_score("xyz789", 12)
print(get_score("abc123"))
print(get_score("nobody"))     
   
if __name__ == "__main__":
    app.run(debug=True)
