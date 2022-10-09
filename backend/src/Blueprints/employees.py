
from flask import Blueprint, make_response
from repository.employee import EmployeeRepository


employee = Blueprint('employee', __name__, url_prefix="/employee")

#Get all employees of a company 
@employee.get('/<company_id>')
def get_employees(company_id):
    try:
        employee_repository = EmployeeRepository()
        list = employee_repository.get_list(company_id=company_id)
        return make_response(list, 200)
    except Exception as e:
        return make_response(e.__str__(), 400)