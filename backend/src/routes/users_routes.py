from uuid import  uuid1
from flask import Blueprint, jsonify, request, flash
from models.UsersModel import UsersModel
from database.db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('users_blueprint', __name__)

@main.route('/')
def get_users():
    try:
        users = UsersModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.post('/add')
def create_user():
    new_user= request.get_json()
    name = new_user['name']
    surname = new_user['surname']
    email = new_user['email']
    password = new_user['password']
    company_name = new_user['company_name']
    company_id = new_user['company_id']
    role = new_user['role']
    dni = new_user['dni']

    _hashed_password = generate_password_hash(password)

    conn = get_connection()
    cur= conn.cursor()
    userId = uuid1()

    #Check if account exists 
    cur.execute('SELECT * FROM client_users WHERE email = %s', (email,))
    account = cur.fetchone()
    print(account)
    if account:
        return jsonify("user email already exist")
    else:
        cur.execute('INSERT INTO client_users VALUES (%s,%s, %s, %s, %s,%s,%s, %s, %s) RETURNING *', (str(userId), name, surname, email, company_name, company_id, role, dni, _hashed_password))

    new_created_user = cur.fetchone()
    print(new_created_user)
    conn.commit()

    cur.close()
    conn.close()

    return jsonify(new_created_user)