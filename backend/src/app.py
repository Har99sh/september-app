from unicodedata import name
from flask import Flask, jsonify, request, make_response,  url_for, redirect, g, session
from flask_login import LoginManager, login_user, current_user, logout_user
from config import config
from Blueprints import users_routes
from models.users import Users
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import  uuid1
from repository.users_repository import UserRepository

app = Flask(__name__)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(id):
    user_repository = UserRepository()
    user = user_repository.get(id)
    if user is not None:
        g.user = user
    return 

@app.get('/')
def homepage():
    print("paso por aqui")
    return make_response("hello")

@app.post('/register')
def create_user():
    print("ejecutando regiter")
    new_user= request.get_json()
    print(new_user)
    name = new_user['name']
    surname = new_user['surname']
    email = new_user['email']
    password = new_user['password']
    company_id = new_user['company_id']
    dni = new_user['dni']
    is_admin = new_user['is_admin']

    _hashed_password = generate_password_hash(password)
    userId = uuid1()

    user_to_add = Users(str(userId), name, surname, email, _hashed_password, company_id, dni, is_admin)

    #Check if account exists 
    account_exist = UserRepository().get_by_email(email)
    if account_exist:
        return jsonify("user email already exist")
    else:
        UserRepository().add(user_to_add)
        return jsonify("user added correctly")

@app.post('/login')
def login():
    user= request.get_json()
    email = user['email']
    password = user['password']
    user_repository = UserRepository()
    
    userFromDb = user_repository.get_by_email(email)
    
    if userFromDb:
            passwordFromDb = userFromDb.password 
            
            if check_password_hash(passwordFromDb, password):
                login_user(userFromDb, remember=True)
                
                return jsonify('you are logged in')
            else:
                # Account doesnt exist or username/password incorrect
                print('Incorrect password')
                return jsonify('Incorrect password')
    else:
        # Account doesnt exist or username/password incorrect
        print('Incorrect email')
        return jsonify('Incorrect email')


@app.route('/logout')
def logout():
    logout_user()
    return make_response("user logged out")

def page_not_found(error):
    return '<h1> Not found page </h1>'

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(users_routes.main, url_prefix= '/users')

    #Error Handle
    app.register_error_handler(404, page_not_found)
    app.run()

# login_manager = LoginManager(app)









