from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from database import get_connection, init_db

# Cafe API: the /staff endpoint returns all staff members from the database

app = Flask(__name__)
CORS(app)
app.config["DATABASE"] = None  # None ka matlab asli cafe.db


def db():
    return get_connection(app.config["DATABASE"])


@app.route("/staff", methods=["GET"])
def get_staff():
    conn = db()
    rows = conn.execute("SELECT * FROM staff").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


# ---- Agle phases ka naya code is line se UPAR paste karna ----

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
