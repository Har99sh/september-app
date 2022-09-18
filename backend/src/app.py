from unicodedata import name
from flask import Flask, jsonify, request
from config import config
from routes import users_routes
from database.db import get_connection
from models.entities.users import Users

app = Flask(__name__)

def page_not_found(error):
    return '<h1> Not found page </h1>'

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(users_routes.main, url_prefix= '/users')

    #Error Handle
    app.register_error_handler(404, page_not_found)
    app.run()



# @app.get('/users/<id>')
