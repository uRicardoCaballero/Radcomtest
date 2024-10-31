from . import *
from app.models import Cliente,Zona

clientes_bp = Blueprint('clientes',__name__)
@clientes_bp.route('/clientes', methods=['POST'])
@login_required
def crear_cliente():

    data = request.get_json()

    id_cliente = data.get('id_cliente')  # Format: "XXzYYNNNNN"
    nombre = data.get('nombre')
    telefono = data.get('telefono')
    ip = data.get('ip')
    zona_id = data.get('zona_id')
    tipo = data.get('tipo')  # "libre", "mensual", "anual"
    estado_cobro = data.get('estado_cobro')  # "pagado", "por cobrar"
    estatus = data.get('estatus')  # "en linea", "baja temporal"
    folio_cobro = data.get('folio_cobro')
    estado_factura = data.get('estado_factura')  # Boolean
    fecha_cobro = datetime.strptime(data.get('fecha_cobro'), '%Y-%m-%d').date() # Date
    fecha_alerta = datetime.strptime(data.get('fecha_alerta'), '%Y-%m-%d').date()
    plan_pago = data.get('plan_pago')   # "400", "350", "200"
    monto_pagado = data.get('monto_pagado')
    if not all([id_cliente]):
        return jsonify({"error": "Falta id"}), 400
    
    if not nombre:
        return jsonify({"error": "Falta el nombre del cliente"}), 404
    
    if not telefono:
        return jsonify({"error": "Falta el telefono"}), 404
    
    if not zona_id:
        return jsonify({"error": "Falta assignar zona/zona no encontrada"}), 404
    
    if not tipo:
        return jsonify({"error": "Falta el tipo de pago si es mensual, anual o libre"}), 404
    
    if not estado_cobro:
        return jsonify({"error": "Falta el estado del cobro"}), 404
    
    if not estatus:
        return jsonify({"error": "Falta el estatus"}), 404
    
    if not folio_cobro:
        return jsonify({"error": "Falta el folio de cobro"}), 404
    
    if not estado_factura:
        return jsonify({"error": "Falta el estado de la factura"}), 404
    
    if not fecha_cobro:
        return jsonify({"error": "Falta fecha de cobro"}), 404
    
    if not fecha_alerta:
        return jsonify({"error": "Falta fecha de alerta"}), 404
    
    if not plan_pago:
        return jsonify({"error": "Falta el plan de pago"}), 404
    
    if not monto_pagado:
        return jsonify({"error": "Falta el monto pagado"}), 404
    
    # Check if id_cliente is unique
    if Cliente.query.get(id_cliente):
        return jsonify({"error": "id_cliente ya existe"}), 400

    # Check if zona exists
    zona = Zona.query.get(zona_id)
    if not zona:
        return jsonify({"error": "Zona no encontrada"}), 404
    
    if data.get('monto_pagado'):
        monto_pagado = float(data.get('monto_pagado'))
        nuevo_cliente = Cliente(
        id_cliente=id_cliente,
        nombre=nombre,
        telefono=telefono,
        ip=ip,
        zona_id=zona_id,
        tipo=tipo,
        estado_cobro=estado_cobro,
        estatus=estatus,
        folio_cobro=folio_cobro,
        estado_factura=estado_factura,
        fecha_cobro=fecha_cobro,
        fecha_alerta=fecha_alerta,
        plan_pago=plan_pago,
        monto_pagado=monto_pagado
    )
    
    

    db.session.add(nuevo_cliente)
    db.session.commit()

    return jsonify({"message": "Cliente creado exitosamente", "id_cliente": nuevo_cliente.id_cliente}), 201

@clientes_bp.route('/clientes', methods=['GET'])
@login_required
def obtener_clientes():
    clientes = Cliente.query.all()
    clientes_data = []
    for cliente in clientes:
        clientes_data.append({
            "id_cliente": cliente.id_cliente,
            "nombre": cliente.nombre,
            "telefono": cliente.telefono,
            "zona_id": cliente.zona_id,
            "tipo": cliente.tipo,
            "estado_cobro": cliente.estado_cobro,
            "estatus": cliente.estatus,
            "folio_cobro": cliente.folio_cobro,
            "estado_factura": cliente.estado_factura,
            "fecha_cobro": cliente.fecha_cobro.strftime('%Y-%m-%d'),
            "fecha_alerta": cliente.fecha_alerta.strftime('%Y-%m-%d'),
            "fecha_creacion": cliente.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(clientes_data), 200

@clientes_bp.route('/clientes/<string:id_cliente>', methods=['GET'])
@login_required
def obtener_cliente(id_cliente):
    cliente = Cliente.query.get_or_404(id_cliente)
    cliente_data = {
        "id_cliente": cliente.id_cliente,
        "nombre": cliente.nombre,
        "telefono": cliente.telefono,
        "zona_id": cliente.zona_id,
        "tipo": cliente.tipo,
        "estado_cobro": cliente.estado_cobro,
        "estatus": cliente.estatus,
        "folio_cobro": cliente.folio_cobro,
        "estado_factura": cliente.estado_factura,
        "fecha_cobro": cliente.fecha_cobro.strftime('%Y-%m-%d'),
        "fecha_alerta": cliente.fecha_alerta.strftime('%Y-%m-%d'),
        "fecha_creacion": cliente.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')
    }
    return jsonify(cliente_data), 200

@clientes_bp.route('/clientes/<string:id_cliente>', methods=['PUT'])
@login_required
def actualizar_cliente(id_cliente):
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    cliente = Cliente.query.get_or_404(id_cliente)
    data = request.get_json()

    cliente.nombre = data.get('nombre', cliente.nombre)
    cliente.telefono = data.get('telefono', cliente.telefono)
    
    zona_id = data.get('zona_id')
    if zona_id:
        zona = Zona.query.get(zona_id)
        if not zona:
            return jsonify({"error": "Zona no encontrada"}), 404
        cliente.zona_id = zona_id
    cliente.tipo = data.get('tipo', cliente.tipo)
    cliente.estado_cobro = data.get('estado_cobro', cliente.estado_cobro)
    cliente.estatus = data.get('estatus', cliente.estatus)
    cliente.folio_cobro = data.get('folio_cobro', cliente.folio_cobro)
    estado_factura = data.get('estado_factura')
    if estado_factura is not None:
        cliente.estado_factura = bool(estado_factura)
    fecha_cobro = data.get('fecha_cobro')
    if fecha_cobro:
        try:
            cliente.fecha_cobro = datetime.strptime(fecha_cobro)
        except ValueError:
            return jsonify({"error": "Formato de fecha_cobro inválido"}), 400
    fecha_alerta = data.get('fecha_alerta')
    if fecha_alerta:
        try:
            cliente.fecha_alerta = datetime.strptime(fecha_alerta)
        except ValueError:
            return jsonify({"error": "Formato de fecha_alerta inválido"}), 400

    db.session.commit()

    return jsonify({"message": "Cliente actualizado exitosamente"}), 200

@clientes_bp.route('/clientes/<string:id_cliente>', methods=['DELETE'])
@login_required
def eliminar_cliente(id_cliente):
    if current_user.tipo_usuario != 'Administrador':
        return jsonify({"error": "Acceso denegado"}), 403

    cliente = Cliente.query.get_or_404(id_cliente)
    db.session.delete(cliente)
    db.session.commit()

    return jsonify({"message": "Cliente eliminado exitosamente"}), 200
