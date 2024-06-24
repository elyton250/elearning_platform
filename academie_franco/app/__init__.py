from flask import Flask, jsonify
from flask_pymongo import PyMongo
from authlib.integrations.flask_client import OAuth
from flask_login import LoginManager
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse
import os
from dotenv import load_dotenv
from api.v1.engine import uri
app = Flask(__name__)
app.config.from_object('config.Config')
    
# uri = "mongodb://localhost:27017/edu_app"

# uri = "mongodb://localhost:27017/edu_app"
# app.config["MONGO_URI"] = uri
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

try:
    # Create a new client and connect to the server
    # mongo = MongoClient(uri, server_api=ServerApi('1'))

    # Initialize PyMongo with the client
    # mongo = PyMongo(app)
    # mongo.init_app(app)
    client = MongoClient(uri, server_api=ServerApi('1'))
    mongo = client['edu_app_db']
    
        
    @app.route('/test_db_connection')
    def test_db_connection():
        try:
            mongo.command('ping')  # Attempt to ping database server
            return jsonify(message='Database connection successful'), 200
        except Exception as e:
            return jsonify(message=f'Database connection error: {str(e)}'), 500
        

    # Initialize OAuth
    

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.get(user_id)

    # Register main blueprint
    from app.routes import main
    app.register_blueprint(main)
    # from app.test import test
    # app.register_blueprint(test)

    # Store OAuth object in app config
except Exception as e:
    print("An error occurred while connecting to MongoDB:")
    print(e)
