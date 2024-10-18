from app.main import app
from app.database import db

with app.app_context():
    db.create_all()