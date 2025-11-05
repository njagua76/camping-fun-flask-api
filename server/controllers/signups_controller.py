from flask import Blueprint, request, jsonify
from models.signup import Signup
from models.camper import Camper
from models.activity import Activity
from models import db

signups_bp = Blueprint('signups_bp', __name__, url_prefix='/signups')

@signups_bp.route('', methods=['POST'])
def create_signup():
    data = request.get_json()
    time = data.get('time')
    camper_id = data.get('camper_id')
    activity_id = data.get('activity_id')
    if not isinstance(time, int) or not (0 <= time <= 23):
        return jsonify({"errors": ["validation errors"]}), 400
    camper = Camper.query.get(camper_id)
    activity = Activity.query.get(activity_id)
    if not camper or not activity:
        return jsonify({"errors": ["validation errors"]}), 400
    signup = Signup(time=time, camper_id=camper_id, activity_id=activity_id)
    db.session.add(signup)
    db.session.commit()
    return jsonify({
        "id": signup.id,
        "time": signup.time,
        "camper_id": signup.camper_id,
        "activity_id": signup.activity_id,
        "camper": {
            "id": camper.id,
            "name": camper.name,
            "age": camper.age
        },
        "activity": {
            "id": activity.id,
            "name": activity.name,
            "difficulty": activity.difficulty
        }
    }), 201