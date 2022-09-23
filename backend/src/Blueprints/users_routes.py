from uuid import  uuid1
from flask import Blueprint, jsonify, request, flash
from models.users import Users
from database.db import get_connection


main = Blueprint('users_blueprint', __name__)

@main.route('/')
def get_users():
        try:
            connection = get_connection()
            users_array = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, surname, email, password, company_id, dni, is_admin FROM users ORDER BY name ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    users = Users(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    users_array.append(users.to_JSON())
            
            connection.close()
            return users_array
        except Exception as ex:
            raise Exception(ex)

@main.route('/<id>')
def get_one_user(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, surname, email, password, company_id, dni, is_admin FROM users ORDER BY name ASC WHERE id = %s",(id,))
                row = cursor.fetchone()

                one_user = None
                if row is not None:
                   one_user = Users(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                   one_user = one_user.to_JSON()
                
            
            connection.close()
            return one_user
        except Exception as ex:
            raise Exception(ex)

