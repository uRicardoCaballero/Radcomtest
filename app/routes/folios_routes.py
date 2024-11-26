from . import *
from app.models import Folio, Cliente

folios_bp = Blueprint('folios', __name__)
@folios_bp.route('/folios', methods=['POST'])
@login_required
def crear_folio():
    data = request.get_json()
    folio = data.get('folio')  # Unique payment ID

    if not folio:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    # Check if folio is unique
    if Folio.query.filter_by(folio=folio).first():
        return jsonify({"error": "El folio ya existe"}), 400

    nuevo_folio = Folio(
        folio=folio
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
        })
    return jsonify(folios_data), 200

@folios_bp.route('/folios/<string:folio>', methods=['GET'])
@login_required
def obtener_folio(folio):
    folio_obj = Folio.query.get_or_404(folio)
    folio_data = {
        "folio": folio_obj.folio,
    }
    return jsonify(folio_data), 200

