from flask import Blueprint, make_response, jsonify, request
from uuid import uuid1
from models.task_app import Tasks
from repository.task_app import TasksRepository

tasks = Blueprint('tasks', __name__, url_prefix="/tasks")
task_repository = TasksRepository()

@tasks.get('/')
def get_tasks():
    try:
        task_list = task_repository.get_list()
        return make_response(task_list)
    except Exception as e:
        return make_response(e.__str__(), 400)

@tasks.get('/<id>')
def get_one_task(id):
    try:
        task = task_repository.get_one(id)
        if task is None:
            raise ValueError(f"Task with id {id} doesn't exist")
        return make_response(task)
    except Exception as e:
        return make_response(e.__str__(), 400)
    
@tasks.delete('/delete/<id>')
def delete_by_id(id):
    try:
        task_repository.delete(id)
        return make_response("Deleted")
    except Exception as e:
        return make_response(e.__str__(), 400)

@tasks.post('/create')
def create():
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
        created_task = Tasks(task_id, employee_id, assigned_by_id, company_id, title,description,due_date,is_completed)
        # Add to db
        task_repository.create(created_task)
        
        return make_response("task is created", 200)
    except Exception as e:
        return make_response(e.__str__(), 400)