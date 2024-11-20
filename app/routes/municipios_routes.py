from . import *
import json
from app.models import Antena,Municipio,Cliente,Comunidad

municipios_bp = Blueprint('municipios', __name__)
@municipios_bp.route('/municipios', methods=['POST'])
@login_required
def crear_municipio():
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    data = request.get_json()
    nombre = data.get('municipio')
    antena_id = data.get('antena')
    #comunidad_id = data.get('comunidad_id')
    # nombre_comunidad = data.get('nombre_comunidad')
    # numero_comunidad = data.get('numero_comunidad')


    # if not nombre or not antena_id or not nombre_comunidad or not numero_comunidad:
    if not nombre or not antena_id:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    # Check if the antena exists
    antena = Antena.query.get(antena_id)
    if not antena:
        return jsonify({"error": "Antena no encontrada"}), 404

    nuevo_municipio = Municipio(
        nombre=nombre,
        antena_id=antena_id,
        #comunidad_id=comunidad_id,
        # nombre_comunidad=nombre_comunidad,
        # numero_comunidad=numero_comunidad
    )

    db.session.add(nuevo_municipio)
    db.session.commit()

    return jsonify({"message": "Municipio creado exitosamente", "id": nuevo_municipio.id}), 201

@municipios_bp.route('/comunidades/<int:municipio_id>', methods=['GET'])
def get_comunidades(municipio_id):
    if not municipio_id:
        return jsonify({"message": "Missing id_municipio"}), 409
    
    comunidades = Comunidad.query.filter_by(id_municipio=municipio_id).all()
    comunidad_list = [{"id": com.id_comunidad, "nombre_comunidad": com.nombre_comunidad} for com in comunidades]
    return jsonify(comunidad_list)

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

@municipios_bp.route('/update_comunidad/<int:municipio_id>', methods=['PUT'])
def update_comunidad(municipio_id):
    data = request.get_json()
    nombre_comunidad = data.get('nombre_comunidad')
    
    # Check if numero_comunidad is provided, if not, calculate the next number
    numero_comunidad = data.get('numero_comunidad')
    if numero_comunidad is None:
        numero_comunidad = get_next_numero_comunidad(municipio_id)

    # Fetch the municipio to update
    municipio = Municipio.query.get(municipio_id)
    if not municipio:
        return jsonify({"error": "Municipio not found"}), 404

    # Update the municipio with comunidad information
    municipio.nombre_comunidad = nombre_comunidad
    municipio.numero_comunidad = numero_comunidad

    try:
        db.session.commit()
        return jsonify({"message": "Comunidad updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@municipios_bp.route('/create_community', methods=['POST'])
def create_community():
    data = request.get_json()
    nombre_comunidad = data.get('nombre_comunidad')
    id_municipio = data.get('id_municipio')
    # Fetch the municipio to update
    if not nombre_comunidad:
        return jsonify({"error": "Missing community name"}), 409
    elif not id_municipio:
        return jsonify({"error": "Missing city id"}), 409

    try:
        new_community = Comunidad(
            nombre_comunidad=nombre_comunidad,
            id_municipio=id_municipio,
        )
        db.session.add(new_community)
        db.session.commit()
        return jsonify({"message": "Comunidad updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500



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
    if current_user.tipo_usuario != 'Administrador':
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
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    municipio = Municipio.query.get_or_404(municipio_id)
    db.session.delete(municipio)
    db.session.commit()

    return jsonify({"message": "Municipio eliminado exitosamente"}), 200

def get_next_numero_comunidad(municipio_id):
    # Get the maximum numero_comunidad for the given municipio
    max_numero = db.session.query(db.func.max(Municipio.numero_comunidad)).filter(
        Municipio.id == municipio_id
    ).scalar()
    
    # If max_numero is None (no comunidad has been assigned yet), start from 1
    return (max_numero or 0) + 1