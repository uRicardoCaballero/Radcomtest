# In app/routes/pagos.py or in your main routes file (e.g., routes.py)
from . import *
from app.models import Cliente
from app.utils.utils import aplicar_descuento

pagos_bp = Blueprint('pagos', __name__)
@pagos_bp.route('/api/pagos', methods=['POST'])
@login_required
def record_payment():
    data = request.json  # Get the data from the request
    client_id = data.get('id_cliente')
    payment_amount = data.get('payment_amount')

    # Find the client in the database
    cliente = Cliente.query.filter_by(id_cliente=client_id).first()

    if not cliente:
        return jsonify({"error": "Client not found"}), 404

    # Update `monto_pagado` and `monto_debido`
    cliente.monto_pagado += payment_amount
    cliente.monto_debido -= payment_amount

    # Ensure `monto_debido` does not go negative
    if cliente.monto_debido < 0:
        cliente.monto_debido = 0

    db.session.commit()  # Save changes

    return jsonify({"message": "Payment recorded successfully", "monto_pagado": cliente.monto_pagado, "monto_debido": cliente.monto_debido}), 200
