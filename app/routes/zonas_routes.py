
from . import *
from app.models import Zona,Municipio

zonas_bp = Blueprint('zonas', __name__)
@zonas_bp.route('/zonas', methods=['POST'])
@login_required
def crear_zona():
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    data = request.get_json()
    nombre = data.get('nombre')
    municipio_id = data.get('municipio_id')
    numero_zona = data.get('numero_zona')

    if not nombre or not municipio_id or numero_zona is None:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    # Validate numero_zona is a 2-digit integer
    if not isinstance(numero_zona, int) or not (0 <= numero_zona <= 99):
        return jsonify({"error": "numero_zona debe ser un entero de 2 dígitos"}), 400

    # Check if the municipio exists
    municipio = Municipio.query.get(municipio_id)
    if not municipio:
        return jsonify({"error": "Municipio no encontrado"}), 404

    nueva_zona = Zona(
        nombre=nombre,
        municipio_id=municipio_id,
        numero_zona=numero_zona
    )

    db.session.add(nueva_zona)
    db.session.commit()

    return jsonify({"message": "Zona creada exitosamente", "id": nueva_zona.id}), 201

@zonas_bp.route('/zonas', methods=['GET'])
@login_required
def obtener_zonas():
    zonas = Zona.query.all()
    zonas_data = []
    for zona in zonas:
        zonas_data.append({
            "id": zona.id,
            "nombre": zona.nombre,
            "municipio_id": zona.municipio_id,
            "numero_zona": zona.numero_zona
        })
    return jsonify(zonas_data), 200

@zonas_bp.route('/zonas/<int:zona_id>', methods=['GET'])
@login_required
def obtener_zona(zona_id):
    zona = Zona.query.get_or_404(zona_id)
    zona_data = {
        "id": zona.id,
        "nombre": zona.nombre,
        "municipio_id": zona.municipio_id,
        "numero_zona": zona.numero_zona
    }
    return jsonify(zona_data), 200

@zonas_bp.route('/zonas/<int:zona_id>', methods=['PUT'])
@login_required
def actualizar_zona(zona_id):
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    zona = Zona.query.get_or_404(zona_id)
    data = request.get_json()

    zona.nombre = data.get('nombre', zona.nombre)
    zona.numero_zona = data.get('numero_zona', zona.numero_zona)

    municipio_id = data.get('municipio_id')
    if municipio_id:
        # Check if the new municipio exists
        municipio = Municipio.query.get(municipio_id)
        if not municipio:
            return jsonify({"error": "Municipio no encontrado"}), 404
        zona.municipio_id = municipio_id

    db.session.commit()

    return jsonify({"message": "Zona actualizada exitosamente"}), 200

@zonas_bp.route('/zonas/<int:zona_id>', methods=['DELETE'])
@login_required
def eliminar_zona(zona_id):
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    zona = Zona.query.get_or_404(zona_id)
    db.session.delete(zona)
    db.session.commit()

    return jsonify({"message": "Zona eliminada exitosamente"}), 200
