from flask import Blueprint, jsonify
from models.UsersModel import UsersModel

main = Blueprint('users_blueprint', __name__)

@main.route('/')
def get_users():
    try:
        users = UsersModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500