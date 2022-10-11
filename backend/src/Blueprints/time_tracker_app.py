from datetime import date, datetime
from flask import Blueprint, make_response, jsonify, request
from uuid import uuid1
from models.time_tracker_app import TimeTracker
from repository.time_tracker_app import TimeTrackerRepository
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity, JWTManager


time_tracker = Blueprint('time_tracker', __name__, url_prefix="/time_tracker")
jwtManager = JWTManager()
time_tracker_repository = TimeTrackerRepository()

@time_tracker.get('/mine/<employee_id>')
@jwt_required()
def get_my_shift_tracker(employee_id):
    try:
        time_tracker_list = time_tracker_repository.get_my_shift(employee_id)
        return make_response(time_tracker_list, 200)
    except Exception as e:
        return make_response(e.__str__(), 400)

@time_tracker.get('/')
def get_time_tracker():
    claims= get_jwt()
    if claims["isAdmin"]:
        try:
            time_tracker_list = time_tracker_repository.get_list()
            return make_response(time_tracker_list, 200)
        except Exception as e:
            return make_response(e.__str__(), 400)

@time_tracker.post('/start/<id>')
@jwt_required()
def start_shift(id):
    try:
        #Create data variables from request
        timeTracker_id = str(uuid1())
        work_day = date.today()
        sign_in = datetime.now()
        sign_out = None
        employee_id = id               
        #Create time tracker object from model
        created_time_tracker = TimeTracker(timeTracker_id, work_day, sign_in, sign_out, employee_id)
        # Add to db
        time_tracker_repository.checkin(created_time_tracker)
        
        return make_response("Shift has started", 200)
    except Exception as e:
            return make_response(e.__str__(), 400)


@time_tracker.post('/end/<id>')
@jwt_required()
def end_shift(id):
    try:
        work_day = date.today()
        time_tracker_repository.checkout(work_day, id)
        return make_response('Shift has ended', 200)
    except Exception as e:
        return make_response(e.__str__(), 400)