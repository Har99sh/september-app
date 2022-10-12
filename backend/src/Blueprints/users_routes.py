from flask import Blueprint, make_response
from models.users import Users
from database.db import get_connection
from repository.users_repository import UserRepository

users = Blueprint('users', __name__, url_prefix="/users")
usersRepository = UserRepository()


@users.get('/')
def get_users():
    try:
        connection = get_connection()
        users_array = []
        with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, surname, email, password, company_id, dni, is_admin FROM users ORDER BY name ASC")
                resultset = cursor.fetchall()
                for row in resultset:
                    print(row)
                    users = Users(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    users_array.append(users.to_JSON())
        
        connection.close()
        return make_response(users_array)
    except Exception as ex:
        raise Exception(ex)



@users.get('/<id>')
def get_one_user(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, surname, email, company_id, dni, is_admin FROM users WHERE id = %s", (id,))
            row = cursor.fetchone()
            one_user = None
            if row is not None:
               one_user = Users(id=row[0], name=row[1], surname=row[2], email=row[3], company_id=row[4], dni=row[5], is_admin=row[6])
               one_user = one_user.to_JSON()
            
        
        connection.close()
        return one_user
    except Exception as ex:
        raise Exception(ex)


@users.get('/<id>')
def get_user_dashboard_deltails(id):
    usersRepository.get_user_details(id)
            
        
      

