from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId
from db import db

completions_bp = Blueprint("completions", __name__)

@completions_bp.route("", methods=["POST"])
@jwt_required()
def complete_task():
    data = request.json
    user_id = get_jwt_identity()
    task = db.tasks.find_one({"_id": ObjectId(data["task_id"])})
    if not task:
        return jsonify({"error": "Task not found"}), 404

    # Record completion
    db.completions.insert_one({
        "user_id": user_id,
        "task_id": str(task["_id"])
    })

    # Update user points
    db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$inc": {"points": task["points"]}}
    )
    return jsonify({"msg": "Task completed"}), 201
