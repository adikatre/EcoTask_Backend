from flask import Blueprint, jsonify
from db import db

leaderboard_bp = Blueprint("leaderboard", __name__)

@leaderboard_bp.route("", methods=["GET"])
def leaderboard():
    top_users = db.users.find({}, {"username": 1, "points": 1, "_id": 0}).sort("points", -1).limit(10)
    return jsonify(list(top_users))
