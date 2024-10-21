from . import *
from app.models import Usuario

login_bp = Blueprint('login', __name__)
@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    print(f"Trying to log in with username: {username} and password: {password}")

    if not username or not password:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    usuario = Usuario.query.filter_by(username=username).first()

    if usuario and check_password_hash(usuario.password, password):
        login_user(usuario)
        return jsonify({"message": "Inicio de sesión exitoso", "tipo_usuario": usuario.tipo_usuario}), 200

    return jsonify({"error": "Nombre de usuario o contraseña inválidos"}), 401