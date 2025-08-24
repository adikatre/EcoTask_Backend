from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from db import db

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("", methods=["GET"])
def list_tasks():
    tasks = list(db.tasks.find({}, {"_id": 0}))
    return jsonify(tasks)

@tasks_bp.route("", methods=["POST"])
@jwt_required()
def create_task():
    data = request.json
    task = {
        "title": data["title"],
        "points": data.get("points", 10),
        "category": data.get("category", "other")
    }
    db.tasks.insert_one(task)
    return jsonify(task), 201
