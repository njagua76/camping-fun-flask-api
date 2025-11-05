from flask import Blueprint, request, jsonify
from models.camper import Camper
from models.signup import Signup
from models.activity import Activity
from models import db

campers_bp = Blueprint('campers_bp', __name__, url_prefix='/campers')

@campers_bp.route('', methods=['GET'])
def get_campers():
    campers = Camper.query.all()
    return jsonify([{"id": c.id, "name": c.name, "age": c.age} for c in campers]), 200

@campers_bp.route('/<int:id>', methods=['GET'])
def get_camper(id):
    camper = Camper.query.get(id)
    if not camper:
        return jsonify({"error": "Camper not found"}), 404
    return jsonify({
        "id": camper.id,
        "name": camper.name,
        "age": camper.age,
        "signups": [{
            "id": s.id,
            "time": s.time,
            "camper_id": s.camper_id,
            "activity_id": s.activity_id,
            "activity": {
                "id": s.activity.id,
                "name": s.activity.name,
                "difficulty": s.activity.difficulty
            }
        } for s in camper.signups]
    }), 200

@campers_bp.route('', methods=['POST'])
def create_camper():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    if not name or not isinstance(age, int) or not (8 <= age <= 18):
        return jsonify({"errors": ["validation errors"]}), 400
    camper = Camper(name=name, age=age)
    db.session.add(camper)
    db.session.commit()
    return jsonify({"id": camper.id, "name": camper.name, "age": camper.age}), 201

@campers_bp.route('/<int:id>', methods=['PATCH'])
def update_camper(id):
    camper = Camper.query.get(id)
    if not camper:
        return jsonify({"error": "Camper not found"}), 404
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    if age is not None and (not isinstance(age, int) or not (8 <= age <= 18)):
        return jsonify({"errors": ["validation errors"]}), 400
    if name:
        camper.name = name
    if age:
        camper.age = age
    db.session.commit()
    return jsonify({"id": camper.id, "name": camper.name, "age": camper.age}), 202