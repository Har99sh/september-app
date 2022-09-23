from unicodedata import name
from flask import Flask, jsonify, request, make_response,  url_for, redirect, g, session
from flask_login import LoginManager, login_user, current_user, logout_user
from config import config
from Blueprints import users_routes
from database.db import get_connection
from models.users import Users
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import  uuid1

app = Flask(__name__)


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

    conn = get_connection()
    cur= conn.cursor()
    userId = uuid1()

    #Check if account exists 
    cur.execute('SELECT * FROM users WHERE email = %s', (email,))
    account = cur.fetchone()
    print(account)
    if account:
        return jsonify("user email already exist")
    else:
        cur.execute('INSERT INTO users VALUES (%s,%s,%s, %s, %s,%s,%s,%s) RETURNING *', (str(userId), name, surname, email, _hashed_password, company_id, dni, is_admin))

    new_created_user = cur.fetchone()
    print(new_created_user)
    conn.commit()

    cur.close()
    conn.close()

    return jsonify(new_created_user)

@app.post('/login')
def login():
    login_user= request.get_json()
    email = login_user['email']
    password = login_user['password']

    conn = get_connection()
    cur= conn.cursor()
    # Check if account exists using MySQL
    cur.execute('SELECT * FROM users WHERE email = %s', (email,))
    account = cur.fetchone()
    
    if account:
            password_rs = account[4]
            # If account exists in users table in out database
            if check_password_hash(password_rs, password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account[0]
                session['username'] = account[1]
                print(session)
                return jsonify('you are logged in')
                # Redirect to home page
                # return redirect(url_for('home'))
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
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    print(session)
    # Redirect to login page
    #return redirect(url_for('login'))
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









