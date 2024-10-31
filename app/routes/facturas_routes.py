from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Factura, db

facturas_bp = Blueprint('facturas', __name__)

@facturas_bp.route('/facturas', methods=['POST'])
@login_required
def crear_factura():
    # Check for admin privileges
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    # Get data from request
    data = request.get_json()
    nombre = data.get('nombre')
    numero = data.get('numero')

    # Validate required fields
    if not nombre or not numero:
        return jsonify({"error": "Nombre y número son obligatorios"}), 400

    # Check if the factura number already exists
    if Factura.query.filter_by(numero=numero).first():
        return jsonify({"error": "El número de factura ya existe"}), 400

    # Create a new Factura instance
    nueva_factura = Factura(
        nombre=nombre,
        numero=numero
    )

    # Add to the session and commit
    db.session.add(nueva_factura)
    db.session.commit()

    return jsonify({"message": "Factura creada exitosamente", "id": nueva_factura.id}), 201

@facturas_bp.route('/facturas', methods=['GET'])
@login_required
def obtener_facturas():
    facturas = Factura.query.all()
    facturas_data = [
        {
            "id": factura.id,
            "nombre": factura.nombre,
            "numero": factura.numero
        }
        for factura in facturas
    ]
    return jsonify(facturas_data), 200

@facturas_bp.route('/facturas/<int:factura_id>', methods=['GET'])
@login_required
def obtener_factura(factura_id):
    factura = Factura.query.get_or_404(factura_id)
    factura_data = {
        "id": factura.id,
        "nombre": factura.nombre,
        "numero": factura.numero
    }
    return jsonify(factura_data), 200

@facturas_bp.route('/facturas/<int:factura_id>', methods=['PUT'])
@login_required
def actualizar_factura(factura_id):
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    factura = Factura.query.get_or_404(factura_id)
    data = request.get_json()

    # Update fields if provided in the request
    factura.nombre = data.get('nombre', factura.nombre)
    nuevo_numero = data.get('numero')
    if nuevo_numero and nuevo_numero != factura.numero:
        # Check if the new number is already in use
        if Factura.query.filter_by(numero=nuevo_numero).first():
            return jsonify({"error": "El nuevo número de factura ya existe"}), 400
        factura.numero = nuevo_numero

    db.session.commit()

    return jsonify({"message": "Factura actualizada exitosamente"}), 200

@facturas_bp.route('/facturas/<int:factura_id>', methods=['DELETE'])
@login_required
def eliminar_factura(factura_id):
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    factura = Factura.query.get_or_404(factura_id)
    db.session.delete(factura)
    db.session.commit()

    return jsonify({"message": "Factura eliminada exitosamente"}), 200