from flask import Flask
from app.database import init_db, db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    init_db(app)
    return (app)
