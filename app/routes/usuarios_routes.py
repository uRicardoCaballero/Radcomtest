from . import *
from app.models import Usuario

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    tipo_usuario = data.get('tipo_usuario')

    if not username or not password:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    if Usuario.query.filter_by(username=username).first():
        return jsonify({"error": "El nombre de usuario ya existe"}), 400

    hashed_password = generate_password_hash(password)

    new_user = Usuario(
        username=username,
        password=hashed_password,
        tipo_usuario=tipo_usuario
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuario tipo: " + tipo_usuario + " creado exitosamente"}), 201

@usuarios_bp.route('/usuarios', methods=['GET'])
@login_required
def obtener_usuarios():
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    usuarios = Usuario.query.all()
    usuarios_data = []
    for usuario in usuarios:
        usuarios_data.append({
            "id": usuario.id,
            "username": usuario.username,
            "tipo_usuario": usuario.tipo_usuario
        })
    return jsonify(usuarios_data), 200

@usuarios_bp.route('/usuarios/<int:usuario_id>', methods=['GET'])
@login_required
def obtener_usuario(usuario_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    usuario = Usuario.query.get_or_404(usuario_id)
    usuario_data = {
        "id": usuario.id,
        "username": usuario.username,
        "tipo_usuario": usuario.tipo_usuario
    }
    return jsonify(usuario_data), 200

@usuarios_bp.route('/usuarios/<int:usuario_id>', methods=['PUT'])
@login_required
def actualizar_usuario(usuario_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    usuario = Usuario.query.get_or_404(usuario_id)
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    tipo_usuario = data.get('tipo_usuario')

    if username:
        if Usuario.query.filter(Usuario.username == username, Usuario.id != usuario_id).first():
            return jsonify({"error": "El nombre de usuario ya existe"}), 400
        usuario.username = username

    if password:
        usuario.password = generate_password_hash(password)

    if tipo_usuario:
        usuario.tipo_usuario = tipo_usuario

    db.session.commit()

    return jsonify({"message": "Usuario actualizado exitosamente"}), 200

@usuarios_bp.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
@login_required
def eliminar_usuario(usuario_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    usuario = Usuario.query.get_or_404(usuario_id)
    db.session.delete(usuario)
    db.session.commit()

    return jsonify({"message": "Usuario eliminado exitosamente"}), 200
