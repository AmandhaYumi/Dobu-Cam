from flask import Flask, jsonify
import time

app = Flask(__name__)

pet_detected = False
last_seen = "Nunca"

@app.route("/status")
def status():
    return jsonify({
        "pet_detected": pet_detected,
        "last_seen": last_seen
    })

@app.route("/update/<state>")
def update(state):
    global pet_detected, last_seen

    if state == "1":
        pet_detected = True
        last_seen = time.strftime("%H:%M:%S")
    else:
        pet_detected = False

    return "OK"

app.run(debug=True)