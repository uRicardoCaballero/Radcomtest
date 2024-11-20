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

    # Create a new Factura instance
    nueva_factura = Factura(
        nombre=nombre,
        numero=numero,
        pendiente="true"
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
            "numero": factura.numero,
            "pendiente": factura.pendiente,
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
        "numero": factura.numero,
        "pendiente": factura.pendiente,
    }
    return jsonify(factura_data), 200

@facturas_bp.route('/factura/<int:id>', methods=['PUT'])
def update_factura_pendiente(id):
    factura = Factura.query.get(id)
    if not factura:
        return jsonify({'error': 'Factura not found'}), 404

    # Update pendiente to "false"
    factura.pendiente = "false"
    db.session.commit()

    return jsonify({"message": "Factura actualizada exitosamente"}), 200

@facturas_bp.route('/factura/pendiente', methods=['GET'])
def get_first_pending_factura():
    # Query for the first factura with pendiente = 'true'
    factura = Factura.query.filter_by(pendiente='true').first()
    
    # Check if a factura was found
    if factura:
        return jsonify({
            'id': factura.id,
            'nombre': factura.nombre,
            'numero': factura.numero,
            'pendiente': factura.pendiente
        }), 200
    else:
        return jsonify({'error': 'No pending factura found'}), 404
