from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Antena, db

antenas_bp = Blueprint('antenas', __name__)

@antenas_bp.route('/antenas', methods=['POST'])
@login_required
def crear_antena():
    # Check for admin privileges
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    # Get data from request
    data = request.get_json()
    nombre = data.get('nombre')
    nombreDispositivo = data.get('nombreDispositivo')
    modelo = data.get('modelo')
    ssid = data.get('ssid')

    # Validate required fields
    if not nombre or not nombreDispositivo or not modelo or not ssid:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    # Create a new Antena instance
    nueva_antena = Antena(
        nombre=nombre,
        nombreDispositivo=nombreDispositivo,
        modelo=modelo,
        ssid=ssid
    )

    # Add to the session and commit
    db.session.add(nueva_antena)
    db.session.commit()

    return jsonify({"message": "Antena creada exitosamente", "id": nueva_antena.id}), 201

@antenas_bp.route('/antenas', methods=['GET'])
@login_required
def obtener_antenas():
    antenas = Antena.query.all()
    antenas_data = [
        {
            "id": antena.id,
            "nombre": antena.nombre,
            "nombreDispositivo": antena.nombreDispositivo,
            "modelo": antena.modelo,
            "ssid": antena.ssid
        }
        for antena in antenas
    ]
    return jsonify(antenas_data), 200

@antenas_bp.route('/antenas/<int:antena_id>', methods=['GET'])
@login_required
def obtener_antena(antena_id):
    antena = Antena.query.get_or_404(antena_id)
    antena_data = {
        "id": antena.id,
        "nombre": antena.nombre,
        "nombreDispositivo": antena.nombreDispositivo,
        "modelo": antena.modelo,
        "ssid": antena.ssid
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
    antena.nombreDispositivo = data.get('nombreDispositivo', antena.nombreDispositivo)
    antena.modelo = data.get('modelo', antena.modelo)
    antena.ssid = data.get('ssid', antena.ssid)

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