# medium-7-admin-diagnostics/app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/health")
def health():
    return "ok"

@app.route("/internal/diag")
def diag():
    # BUG: no protection
    return jsonify({
        "db":"ok",
        "queue":"ok",
        "flag":FLAG
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
