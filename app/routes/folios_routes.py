from . import *
from app.models import Folio, Cliente

folios_bp = Blueprint('folios', __name__)
@folios_bp.route('/folios', methods=['POST'])
@login_required
def crear_folio():
    if current_user.tipo_usuario not in ['admin', 'worker']:
        return jsonify({"error": "Acceso denegado"}), 403

    data = request.get_json()
    folio = data.get('folio')  # Unique payment ID
    cliente_id = data.get('cliente_id')  # "XXzYYNNNNN"

    if not folio or not cliente_id:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    # Check if folio is unique
    if Folio.query.get(folio):
        return jsonify({"error": "El folio ya existe"}), 400

    # Check if cliente exists
    cliente = Cliente.query.get(cliente_id)
    if not cliente:
        return jsonify({"error": "Cliente no encontrado"}), 404

    nuevo_folio = Folio(
        folio=folio,
        cliente_id=cliente_id
    )

    db.session.add(nuevo_folio)
    db.session.commit()

    return jsonify({"message": "Folio creado exitosamente", "folio": nuevo_folio.folio}), 201

@folios_bp.route('/folios', methods=['GET'])
@login_required
def obtener_folios():
    folios = Folio.query.all()
    folios_data = []
    for folio in folios:
        folios_data.append({
            "folio": folio.folio,
            "cliente_id": folio.cliente_id
        })
    return jsonify(folios_data), 200

@folios_bp.route('/folios/<string:folio>', methods=['GET'])
@login_required
def obtener_folio(folio):
    folio_obj = Folio.query.get_or_404(folio)
    folio_data = {
        "folio": folio_obj.folio,
        "cliente_id": folio_obj.cliente_id
    }
    return jsonify(folio_data), 200

@folios_bp.route('/folios/<string:folio>', methods=['PUT'])
@login_required
def actualizar_folio(folio):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    folio_obj = Folio.query.get_or_404(folio)
    data = request.get_json()

    nuevo_folio = data.get('folio')
    cliente_id = data.get('cliente_id')

    if nuevo_folio:
        # Check if the new folio is unique
        if Folio.query.get(nuevo_folio):
            return jsonify({"error": "El folio ya existe"}), 400
        folio_obj.folio = nuevo_folio

    if cliente_id:
        cliente = Cliente.query.get(cliente_id)
        if not cliente:
            return jsonify({"error": "Cliente no encontrado"}), 404
        folio_obj.cliente_id = cliente_id

    db.session.commit()

    return jsonify({"message": "Folio actualizado exitosamente"}), 200

@folios_bp.route('/folios/<string:folio>', methods=['DELETE'])
@login_required
def eliminar_folio(folio):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    folio_obj = Folio.query.get_or_404(folio)
    db.session.delete(folio_obj)
    db.session.commit()

    return jsonify({"message": "Folio eliminado exitosamente"}), 200