from flask import Blueprint, jsonify
from models.activity import Activity
from models import db

activities_bp = Blueprint('activities_bp', __name__, url_prefix='/activities')

@activities_bp.route('', methods=['GET'])
def get_activities():
    activities = Activity.query.all()
    return jsonify([{"id": a.id, "name": a.name, "difficulty": a.difficulty} for a in activities]), 200

@activities_bp.route('/<int:id>', methods=['DELETE'])
def delete_activity(id):
    activity = Activity.query.get(id)
    if not activity:
        return jsonify({"error": "Activity not found"}), 404
    db.session.delete(activity)
    db.session.commit()
    return '', 204