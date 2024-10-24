from flask import Blueprint, jsonify, request, send_file
from flask_login import login_required, current_user, logout_user, login_user
from app.database import db
from datetime import datetime, date
import pandas as pd
from io import BytesIO
from pytz import timezone
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from app.routes.antenas_routes import antenas_bp
from app.routes.clientes_routes import clientes_bp
from app.routes.excel_route import excel_bp
from app.routes.folios_routes import folios_bp
from app.routes.logout_route import logout_bp
from app.routes.login_route import login_bp
from app.routes.municipios_routes import municipios_bp
from app.routes.register_route import register_bp
from app.routes.usuarios_routes import usuarios_bp
from app.routes.zonas_routes import zonas_bp
from app.routes.pagos_route import pagos_bp
from app.routes.tests import tests_bp
local_tz = timezone('America/Mexico_City')

antenas_bp = antenas_bp
clientes_bp = clientes_bp
excel_bp = excel_bp
folios_bp = folios_bp
logout_bp = logout_bp
login_bp = login_bp  
municipios_bp = municipios_bp
register_bp = register_bp
usuarios_bp = usuarios_bp
zonas_bp = zonas_bp
pagos_bp = pagos_bp
tests_bp = tests_bp