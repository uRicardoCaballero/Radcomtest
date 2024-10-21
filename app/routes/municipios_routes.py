from . import *
from app.models import Antena,Municipio

municipios_bp = Blueprint('municipios', __name__)
@municipios_bp.route('/municipios', methods=['POST'])
@login_required
def crear_municipio():
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    data = request.get_json()
    nombre = data.get('nombre')
    antena_id = data.get('antena_id')

    if not nombre or not antena_id:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    # Check if the antena exists
    antena = Antena.query.get(antena_id)
    if not antena:
        return jsonify({"error": "Antena no encontrada"}), 404

    nuevo_municipio = Municipio(
        nombre=nombre,
        antena_id=antena_id
    )

    db.session.add(nuevo_municipio)
    db.session.commit()

    return jsonify({"message": "Municipio creado exitosamente", "id": nuevo_municipio.id}), 201

@municipios_bp.route('/municipios', methods=['GET'])
@login_required
def obtener_municipios():
    municipios = Municipio.query.all()
    municipios_data = []
    for municipio in municipios:
        municipios_data.append({
            "id": municipio.id,
            "nombre": municipio.nombre,
            "antena_id": municipio.antena_id
        })
    return jsonify(municipios_data), 200

@municipios_bp.route('/municipios/<int:municipio_id>', methods=['GET'])
@login_required
def obtener_municipio(municipio_id):
    municipio = Municipio.query.get_or_404(municipio_id)
    municipio_data = {
        "id": municipio.id,
        "nombre": municipio.nombre,
        "antena_id": municipio.antena_id
    }
    return jsonify(municipio_data), 200

@municipios_bp.route('/municipios/<int:municipio_id>', methods=['PUT'])
@login_required
def actualizar_municipio(municipio_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    municipio = Municipio.query.get_or_404(municipio_id)
    data = request.get_json()

    municipio.nombre = data.get('nombre', municipio.nombre)
    antena_id = data.get('antena_id')
    if antena_id:
        # Check if the new antena exists
        antena = Antena.query.get(antena_id)
        if not antena:
            return jsonify({"error": "Antena no encontrada"}), 404
        municipio.antena_id = antena_id

    db.session.commit()

    return jsonify({"message": "Municipio actualizado exitosamente"}), 200

@municipios_bp.route('/municipios/<int:municipio_id>', methods=['DELETE'])
@login_required
def eliminar_municipio(municipio_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    municipio = Municipio.query.get_or_404(municipio_id)
    db.session.delete(municipio)
    db.session.commit()

    return jsonify({"message": "Municipio eliminado exitosamente"}), 200