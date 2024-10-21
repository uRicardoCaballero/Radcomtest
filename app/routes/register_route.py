from . import *
from app.models import Usuario

register_bp = Blueprint('register', __name__)
@register_bp.route('/register', methods=['POST'])
@login_required
def register():
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    tipo_usuario = data.get('tipo_usuario')  # "admin" or "worker"

    if not username or not password or not tipo_usuario:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    if Usuario.query.filter_by(username=username).first():
        return jsonify({"error": "El nombre de usuario ya existe"}), 400

    hashed_password = generate_password_hash(password)

    nuevo_usuario = Usuario(
        username=username,
        password=hashed_password,
        tipo_usuario=tipo_usuario
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"message": "Usuario registrado exitosamente"}), 201
