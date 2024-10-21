import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    # Absolute path to the database file
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '../database/tickets.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
