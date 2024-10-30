import pytest
from app.main import app as testapp
from app.models import Usuario
from app.database import db
from werkzeug.security import generate_password_hash  

@pytest.fixture
def app():
    # Set up the test client
    testapp.config['TESTING'] = True  # Enable testing mode
    testapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory database for testing


    # Initialize the database with the app
    with testapp.app_context():
        db.session.remove()
        db.drop_all()
        db.create_all()  # Create the tables in the in-memory database
        password_hash=generate_password_hash("54321")
        db.session.add(Usuario(username='cesar', password=password_hash, tipo_usuario='Administrador'))
        db.session.add(Usuario(username='celina', password=password_hash, tipo_usuario='worker'))
        
        db.session.commit()
           
        yield testapp 

        # Clean up after tests
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()