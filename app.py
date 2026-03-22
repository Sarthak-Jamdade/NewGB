from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/memories")
def memories():
    return render_template("memories.html")

@app.route("/message")
def message():
    return render_template("message.html")

@app.route("/surprise")
def surprise():
    return render_template("surprise.html")

@app.route("/lastsurprise")
def lastsurprise():
    return render_template("lastsurprice.html")

@app.route("/add_message", methods=["POST"])
def add_message():
    data = request.json
    msg = data.get("message")
    if msg:
        messages.append(msg)
    return jsonify({"status": "ok"})

@app.route("/get_messages")
def get_messages():
    return jsonify(messages)

if __name__ == "__main__":
    app.run(debug=True)
