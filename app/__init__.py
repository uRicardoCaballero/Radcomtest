from flask import Flask
from app.database import init_db, db
from flask_migrate import Migrate
from flask_session import Session

def create_app():
    app = Flask(__name__)
    app.secret_key = 'fX9l3LhCudCwVqUUDZ0q80RvCiswOFnLoYzzXpn64UzfEoqqBy9CRh7lZEnhIUsN'
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)
    init_db(app)
    return (app)
