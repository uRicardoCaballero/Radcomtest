import sys
from PyQt5 import QtWidgets
import threading 
from app import create_app
from app.routes import *
from app.frontend.RADCOM import MainWindow
from flask_login import LoginManager
from flask_migrate import Migrate
from datetime import datetime, date
import os
import time
import atexit
from app import create_app
from app.models import Usuario
from app.database import db

app = create_app()

shutdown_flag = False
# Flask-Login setup

# set SECRET_KEY=mysecretkeyvalue
# app.secret_key = os.getenv('SECRET_KEY', 'your-default-secret-key')
app.secret_key = 'fX9l3LhCudCwVqUUDZ0q80RvCiswOFnLoYzzXpn64UzfEoqqBy9CRh7lZEnhIUsN'

# Initialize the database
migrate = Migrate(app, db)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.login'



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
app.register_blueprint(zonas_bp, url_prefix='/api')
app.register_blueprint(tests_bp, url_prefix='/api')

@app.route('/')
def home():
    return "Radcom Backend Running"

def run_flask():
    global shutdown_flag
    app.run(debug=True, use_reloader=False)

def shutdown_flask():
    global shutdown_flag
    shutdown_flag = True
    print("Shutting down Flask server...")



# ------------------- Run the Flask App -------------------
if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    # Start the PyQt5 UI
    app = QtWidgets.QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()
    exit_code = app.exec_()

    while not shutdown_flag:
        time.sleep(1)
    flask_thread.join()
    sys.exit(app.exec())
    