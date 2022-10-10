from flask import Blueprint, make_response, jsonify, request
from uuid import uuid1
from models.task_app import Tasks
from repository.task_app import TasksRepository
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity, JWTManager


tasks = Blueprint('tasks', __name__, url_prefix="/tasks")
jwtManager = JWTManager()
task_repository = TasksRepository()

@tasks.get('/')
@jwt_required()
def get_tasks():
    try:
        task_list = task_repository.get_list()
        return make_response(task_list)
    except Exception as e:
        return make_response(e.__str__(), 400)

@tasks.get('/mine/<employee_id>')
@jwt_required()
def get_my_tasks(employee_id):
    try:
        task_list = task_repository.get_my_tasks(employee_id)
        return make_response(task_list, 200)
    except Exception as e:
        return make_response(e.__str__(), 400)
    
@tasks.get('/<id>')
@jwt_required()
def get_one_task(id):
    try:
        task = task_repository.get_one(id)
        if task is None:
            raise ValueError(f"Task with id {id} doesn't exist")
        return make_response(task)
    except Exception as e:
        return make_response(e.__str__(), 400)
    
@tasks.delete('/delete/<id>')
@jwt_required()
def delete_by_id(id):
    claims= get_jwt()
    if claims["isAdmin"]:
        try:
            task_repository.delete(id)
            return make_response("Deleted")
        except Exception as e:
            return make_response(e.__str__(), 400)

@tasks.post('/create')
@jwt_required()
def create():
    claims= get_jwt()
    if claims["isAdmin"]:
        try:
            task_data = request.get_json()
            #Create data variables from request
            task_id = str(uuid1())
            employee_id = task_data["employee_id"]
            assigned_by_id = task_data["assigned_by_id"]
            company_id = task_data["company_id"]
            title = task_data["title"]
            description = task_data["description"]
            due_date = task_data["due_date"] 
            is_completed = task_data["is_completed"]
            #Create task object from model
            created_task = Tasks(task_id, employee_id, assigned_by_id, company_id, title, description,due_date,is_completed)
            # Add to db
            task_repository.create(created_task)
            
            return make_response("task is created", 200)
        except Exception as e:
            return make_response(e.__str__(), 400)
    
@tasks.put('/done/≤id>')
@jwt_required()
def mark_as_done():
    try:
        task_repository.update('done', id)
        return make_response('Task is done', 200)
    except Exception as e:
        return make_response(e.__str__(), 400)