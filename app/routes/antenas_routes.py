from . import *
from app.models import Antena

antenas_bp = Blueprint('antenas', __name__)
@antenas_bp.route('/antenas', methods=['POST'])
@login_required
def crear_antena():
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    data = request.get_json()
    nombre = data.get('nombre')
    ubicacion = data.get('ubicacion')  # Optional

    if not nombre:
        return jsonify({"error": "El nombre es requerido"}), 400

    nueva_antena = Antena(
        nombre=nombre,
        ubicacion=ubicacion
    )

    db.session.add(nueva_antena)
    db.session.commit()

    return jsonify({"message": "Antena creada exitosamente", "id": nueva_antena.id}), 201

@antenas_bp.route('/antenas', methods=['GET'])
@login_required
def obtener_antenas():
    antenas = Antena.query.all()
    antenas_data = []
    for antena in antenas:
        antenas_data.append({
            "id": antena.id,
            "nombre": antena.nombre,
            "ubicacion": antena.ubicacion
        })
    return jsonify(antenas_data), 200

@antenas_bp.route('/antenas/<int:antena_id>', methods=['GET'])
@login_required
def obtener_antena(antena_id):
    antena = Antena.query.get_or_404(antena_id)
    antena_data = {
        "id": antena.id,
        "nombre": antena.nombre,
        "ubicacion": antena.ubicacion
    }
    return jsonify(antena_data), 200

@antenas_bp.route('/antenas/<int:antena_id>', methods=['PUT'])
@login_required
def actualizar_antena(antena_id):
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    antena = Antena.query.get_or_404(antena_id)
    data = request.get_json()

    antena.nombre = data.get('nombre', antena.nombre)
    antena.ubicacion = data.get('ubicacion', antena.ubicacion)

    db.session.commit()

    return jsonify({"message": "Antena actualizada exitosamente"}), 200

@antenas_bp.route('/antenas/<int:antena_id>', methods=['DELETE'])
@login_required
def eliminar_antena(antena_id):
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    antena = Antena.query.get_or_404(antena_id)
    db.session.delete(antena)
    db.session.commit()

    return jsonify({"message": "Antena eliminada exitosamente"}), 200