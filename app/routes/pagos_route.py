# In app/routes/pagos.py or in your main routes file (e.g., routes.py)
from . import *
from app.models import Cliente
from app.utils.utils import aplicar_descuento

pagos_bp = Blueprint('pagos', __name__)
@pagos_bp.route('/api/pagos', methods=['POST'])
@login_required
def procesar_pago():
    data = request.get_json()
    cliente_id = data.get('cliente_id')
    monto = float(data.get('monto', 0))
    
    cliente = Cliente.query.get(cliente_id)
    
    if not cliente:
        return jsonify({'error': 'Cliente no encontrado'}), 404

    if cliente.es_libre():
        return jsonify({'message': 'Este cliente no requiere pagos (libre).'}), 200

    # Calculate the discounted amount based on the special yearly discount
    monto_descuento = aplicar_descuento(cliente)
    monto_restante = monto_descuento - cliente.monto_pagado

    if monto >= monto_restante:
        cliente.monto_pagado += monto
        db.session.commit()
        return jsonify({'message': f'Pago recibido, deuda saldada. Monto pagado: {cliente.monto_pagado}.'}), 200
    else:
        cliente.monto_pagado += monto
        db.session.commit()
        return jsonify({'message': f'Pago parcial registrado. Restante: {monto_restante - monto}.'}), 200