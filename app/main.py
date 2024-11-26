import sys
from apscheduler.schedulers.background import BackgroundScheduler
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import threading 
from app import create_app
from flask import Flask
from app.routes import *
from app.models import Cliente
from app.frontend.main import *
from flask_login import LoginManager
from flask_migrate import Migrate
from datetime import datetime, date
import os
import time
import atexit
from app.models import Usuario
from app.database import db
from flask_cors import CORS
from flask_session import Session
from PIL import Image
from pyupdater.client import Client


app = create_app()

CORS(app, supports_credentials=True)
UPDATE_URL = "https://github.com/uRicardoCaballero/Radcomtest/archive/refs/tags/mainrelease.zip"
shutdown_flag = False
client = Client(__name__)

# Flask-Login setup

# set SECRET_KEY=mysecretkeyvalue
# app.secret_key = os.getenv('SECRET_KEY', 'your-default-secret-key')

# Initialize the database
migrate = Migrate(app, db)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.login'



def add_monthly_payments():
    """Increment monthly payments for all clients."""
    with app.app_context():  # Ensure this runs within the Flask app context
        clients = Cliente.query.all()
        for client in clients:
            if client.plan_pago:  # Check if the client has a payment plan
                client.monto_debido += client.plan_pago
        db.session.commit()

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(add_monthly_payments, 'cron', day=1, hour=0, minute=0)  # Every 1st of the month at midnight
scheduler.start()


# Create directories if they don't exist
os.makedirs(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../ticket_images'), exist_ok=True)

# User loader callback
@login_manager.user_loader
def load_user(user_id):
    user = db.session.get(Usuario,( int(user_id)))
    return user if user else None


# Utility function to save uploaded images
# def save_image(image):
#     filename = secure_filename(image.filename)
#     timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
#     filename = f"{timestamp}_{filename}"
#     image_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../ticket_images', filename)
#     image.save(image_path)
#     return filename  # Return the filename to store in the database

# ------------------- Usuarios Routes -------------------

app.register_blueprint(antenas_bp, url_prefix='/api')
app.register_blueprint(clientes_bp, url_prefix='/api')
app.register_blueprint(excel_bp, url_prefix='/api')
app.register_blueprint(folios_bp, url_prefix='/api')
app.register_blueprint(login_bp, url_prefix='/api')
app.register_blueprint(logout_bp, url_prefix='/api')
app.register_blueprint(municipios_bp, url_prefix='/api')
app.register_blueprint(register_bp, url_prefix='/api')
app.register_blueprint(usuarios_bp, url_prefix='/api')
app.register_blueprint(tests_bp, url_prefix='/api')
app.register_blueprint(facturas_bp, url_prefix='/api')



def run_flask():
    app.run(debug=True, use_reloader=False)

def main():
    
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget { background-color: #37373d; }")
    main_window = MainWindow()
    main_window.setMinimumSize(1275, 725)
    main_window.setMaximumSize(1275, 725)
    main_window.show()
    sys.exit(app.exec_())
    
    


# ------------------- Run the Flask App -------------------
if __name__ == '__main__':
    main()
