from email.header import Header
import imp
from flask import Flask, jsonify, request, make_response,  url_for, redirect, g, session
from flask_login import LoginManager, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token

from flask_cors import CORS, cross_origin

from unicodedata import name
from uuid import  uuid1

#User modules
from Blueprints.users_routes import users
from models.users import Users
from repository.users_repository import UserRepository

#Task app
from Blueprints.task_app import tasks

#Company
from Blueprints.company_blueprint import company
from models.company import Company
from repository.company_repository import CompanyRepository

#Employees
from Blueprints.employees import employee

#Time Tracker
from Blueprints.time_tracker_app import time_tracker

from config import config

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_SECRET_KEY'] = config["JWT_KEY"]
app.config["JWT_AUTHMAXAGE"] = 86400

CORS(app)


login_manager = LoginManager(app)
jwt = JWTManager(app)

app.register_blueprint(tasks)
app.register_blueprint(company)
app.register_blueprint(employee)
app.register_blueprint(time_tracker)

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
    print("ejecutando register")
    new_user = request.get_json()
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
        return make_response(status=409)
    else:
        UserRepository().add(user_to_add)
        return jsonify("user added correctly")

@app.post('/login')
def login():
    user = request.get_json()
    email = user['email']
    password = user['password']
    # Query your database for username and password
    user_repository = UserRepository()
    userFromDb = user_repository.getUserByEmail(email)
    passwordFromDb = userFromDb.password
    if userFromDb is None:
        return jsonify({"msg": "Incorrect username or password"})
    
    # create a new token with the user id inside
    if check_password_hash(passwordFromDb, password): 
        additional_claims = {"isAdmin": f"{userFromDb.is_admin}", "companyID": f"{userFromDb.company_id}"}
        access_token = create_access_token(identity=userFromDb.id, additional_claims=additional_claims)
        return make_response(jsonify({ "token": access_token, "user_id": userFromDb.id }), 200)

    return make_response("Erro")
 #------------------------------------------------------------------------------------   
    # user= request.get_json()
    # email = user['email']
    # password = user['password']
    # user_repository = UserRepository()
    
    # userFromDb = user_repository.get_by_email(email)
    
    # if userFromDb:
    #         passwordFromDb = userFromDb.password 
            
    #         if check_password_hash(passwordFromDb, password):
    #             login_user(userFromDb, remember=True)
                
    #             return jsonify('you are logged in')
    #         else:
    #             # Account doesnt exist or username/password incorrect
    #             print('Incorrect password')
    #             return jsonify('Incorrect password')
    # else:
    #     # Account doesnt exist or username/password incorrect
    #     print('Incorrect email')
    #     return jsonify('Incorrect email')


#Company register
@app.post('/register-company')
def create_company():
    new_company = request.get_json()
    name = new_company['name']
    cif = new_company['cif']
    email = new_company['email']
    telephone = new_company['telephone']
    
    companyId = uuid1()

    company_to_add = Company(str(companyId), name, cif, email, telephone)
    #Check if account exists 
    account_exist = CompanyRepository().get_by_email(email)
    if account_exist:
        return make_response("Company email already exist", status=403)
    else:
        CompanyRepository().add(company_to_add)
        return make_response("Company added correctly", status=200)


def page_not_found(error):
    return '<h1> Not found page </h1>'

if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    #Blueprints
    app.register_blueprint(users)
    
    #Error Handle
    app.register_error_handler(404, page_not_found) 
    app.run()










