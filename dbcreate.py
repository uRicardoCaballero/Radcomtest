from app.main import app
from app.database import db

with app.app_context():
    db.drop_all()
    db.create_all()