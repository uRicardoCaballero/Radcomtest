from . import *
from app.models import Usuario

tests_bp = Blueprint('test', __name__)

# @app.route('/reset-db', methods=['POST'])  # Add appropriate methods/permissions for this operation
# def reset_db():
#     db.drop_all()
#     db.create_all()  # (Optional) Re-create the tables if you want a fresh schema
#     return "Database reset complete."

@tests_bp.route('/init_admin', methods=['POST'])
def init_admin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    if Usuario.query.filter_by(username=username).first():
        return jsonify({"error": "El nombre de usuario ya existe"}), 400

    hashed_password = generate_password_hash(password)

    admin_usuario = Usuario(
        username=username,
        password=hashed_password,
        tipo_usuario='Administrador'
    )

    db.session.add(admin_usuario)
    db.session.commit()

    return jsonify({"message": "Administrador creado exitosamente"}), 201