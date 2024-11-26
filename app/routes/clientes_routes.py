from . import *
from app.models import Cliente, Comunidad, Service, HistorialMovimientos
from sqlalchemy import select
from datetime import datetime
from flask import jsonify

clientes_bp = Blueprint('clientes',__name__)
@clientes_bp.route('/clientes', methods=['POST'])
@login_required
def crear_cliente():

    data = request.get_json()

    nombre = data.get('nombre')
    telefono = data.get('telefono')
    ip = data.get('ip')
    comunidad_id = data.get('comunidad_id')
    municipios_id = data.get("municipio_id")
    #zona_id = data.get('zona_id')
    calle = data.get('calle')
    colonia = data.get('colonia')
    numero = data.get('numero')
    codigo_postal = data.get('codigo_postal')
    tipo = data.get('tipo')  # "libre", "mensual", "anual"
    estado_cobro = data.get('estado_cobro')  # "pagado", "por cobrar"
    estatus = data.get('estatus')  # "en linea", "baja temporal"
    fecha_cobro_str = data.get('fecha_cobro')
    if fecha_cobro_str:
        fecha_cobro = datetime.strptime(fecha_cobro_str, '%Y-%m-%d').date()
    else:
        # Set a default date if 'fecha_cobro' is missing; for example, today’s date
        fecha_cobro = datetime.now().date()

    fecha_alerta_str = data.get('fecha_alerta')
    if fecha_alerta_str:
        fecha_alerta = datetime.strptime(fecha_alerta_str, '%Y-%m-%d').date()
    else:
        # Set a default date if 'fecha_cobro' is missing; for example, today’s date
        fecha_alerta = datetime.now().date()
    plan_pago = data.get('plan_pago')   # "400", "350", "200"
    monto_pagado = data.get('monto_pagado')
    
    if not nombre:
        return jsonify({"error": "Falta el nombre del cliente"}), 404
    
    if not telefono:
        return jsonify({"error": "Falta el telefono"}), 404
    
    if not comunidad_id:
         return jsonify({"error": "Falta assignar comunidad_id"}), 404
    
    if not calle:
         return jsonify({"error": "Falta assignar calle"}), 404
    
    if not colonia:
         return jsonify({"error": "Falta assignar colonia"}), 404
    
    if not numero:
         return jsonify({"error": "Falta assignar numero de casa"}), 404
    
    if not codigo_postal:
         return jsonify({"error": "Falta assignar codigo postal"}), 404
    
    if not tipo:
        return jsonify({"error": "Falta el tipo de pago si es mensual, anual o libre"}), 404
    
    if not estado_cobro:
        return jsonify({"error": "Falta el estado del cobro"}), 404
    
    if not estatus:
        return jsonify({"error": "Falta el estatus"}), 404
    
    if not fecha_cobro:
        return jsonify({"error": "Falta fecha de cobro"}), 404
    
    if not fecha_alerta:
        return jsonify({"error": "Falta fecha de alerta"}), 404
    
    if not plan_pago:
        return jsonify({"error": "Falta el plan de pago"}), 404
    
    if not monto_pagado:
        return jsonify({"error": "Falta el monto pagado"}), 404
    
    if Cliente.query.filter_by(nombre=nombre).first():
        return jsonify({"error": "El cliente ya existe"}), 400
    

    # # Check if zona exists
    # zona = Zona.query.get(zona_id)
    # if not zona:
    #     return jsonify({"error": "Zona no encontrada"}), 404
    
    if data.get('monto_pagado'):
        monto_pagado = float(data.get('monto_pagado'))
        nuevo_cliente = Cliente(
        nombre=nombre,
        telefono=telefono,
        ip=ip,
        comunidad_id=comunidad_id,
        #zona_id=zona_id,
        calle = calle,
        colonia = colonia,
        numero = numero,
        codigo_postal = codigo_postal,
        tipo=tipo,
        estado_cobro=estado_cobro,
        estatus=estatus,
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
            "comunidad_id": cliente.comunidad_id,
            "calle" : cliente.calle,
            "colonia" : cliente.colonia,
            "numero" : cliente.numero,
            "codigo_postal" : cliente.codigo_postal,
            'ip': cliente.ip,
            'monto_pagado': cliente.monto_pagado,
            'monto_debido': cliente.monto_debido,
            "tipo": cliente.tipo,
            "estado_cobro": cliente.estado_cobro,
            "estatus": cliente.estatus,
            "fecha_cobro": cliente.fecha_cobro.strftime('%Y-%m-%d'),
            "fecha_alerta": cliente.fecha_alerta.strftime('%Y-%m-%d'),
            "fecha_creacion": cliente.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(clientes_data), 200

@clientes_bp.route('/clientesid', methods=['GET'])
@login_required
def obtener_clientes_all():
    # Fetch all client IDs
    clientes = Cliente.query.all()
    return jsonify([{"id_cliente": cliente.id_cliente, "nombre": cliente.nombre} for cliente in clientes]), 200

@clientes_bp.route('/clientes/<string:id_cliente>', methods=['GET'])
@login_required
def obtener_cliente(id_cliente):
    cliente = Cliente.query.get_or_404(id_cliente)
    cliente_data = {
        "id_cliente": cliente.id_cliente,
        "nombre": cliente.nombre,
        "telefono": cliente.telefono,
        "comunidad_id": cliente.comunidad_id,
        #"zona_id": cliente.zona_id,
        "tipo": cliente.tipo,
        "estado_cobro": cliente.estado_cobro,
        "estatus": cliente.estatus,
        "fecha_cobro": cliente.fecha_cobro.strftime('%Y-%m-%d'),
        "fecha_alerta": cliente.fecha_alerta.strftime('%Y-%m-%d'),
        "fecha_creacion": cliente.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')
    }
    return jsonify(cliente_data), 200

@clientes_bp.route('/clientes/<string:id_cliente>', methods=['PUT'])
@login_required
def actualizar_cliente(id_cliente):

    cliente = Cliente.query.get_or_404(id_cliente)
    data = request.get_json()

    cliente.nombre = data.get('nombre', cliente.nombre)
    cliente.telefono = data.get('telefono', cliente.telefono)
    cliente.ip = data.get ('ip', cliente.ip)
    cliente.calle = data.get ('calle', cliente.calle)
    cliente.numero = data.get ('numero', cliente.numero)
    cliente.colonia = data.get ('colonia', cliente.colonia)
    cliente.codigo_postal = data.get ('codigo_postal', cliente.codigo_postal)
    cliente.tipo = data.get('tipo', cliente.tipo)
    cliente.estatus = data.get('status', cliente.estatus)
    cliente.estado_cobro = data.get('estado_cobro', cliente.estado_cobro)
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

@clientes_bp.route('/clientes/<string:id_cliente>/pago', methods=['POST'])
def registrar_pago(id_cliente):
    cliente = Cliente.query.get_or_404(id_cliente)
    data = request.get_json()
    monto_pagado = float(data.get('monto_pagado', 0.0))

    if cliente.tipo != 'libre' and monto_pagado > 0:
        cliente.due_balance -= monto_pagado
        cliente.monto_pagado += monto_pagado 
        
        db.session.commit()

    return jsonify({"message": "Pago registrado exitosamente", "due_balance": cliente.due_balance}), 200

@clientes_bp.route('/cobro/<int:id>', methods=['PUT'])
def update_cobro(id):
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({'error': 'Cliente no encontrado'}), 404

    data = request.get_json()
    
    # Fetch the payment amount and ensure it's a valid number
    monto_pagado = float(data.get('monto_pagado', 0.0))
    if monto_pagado <= 0:
        return jsonify({'error': 'Monto de pago debe ser mayor que 0'}), 400
    
    # Update the client details
    cliente.num_cuenta = data.get('num_cuenta')
    cliente.monto_pagado += monto_pagado  # Accumulate the total paid amount
    cliente.monto_debido -= monto_pagado  # Subtract from the amount due
    
    # Create a new payment movement record in the HistorialMovimientos table
    movimiento = HistorialMovimientos(
        cliente_id=cliente.id_cliente,
        descripcion=f"Pago de ${monto_pagado} registrado",
        monto=monto_pagado,
        tipo_movimiento="pago"
    )
    
    # Add and commit the new movement
    db.session.add(movimiento)
    
    try:
        # Commit both the client update and the new movement record
        db.session.commit()
        return jsonify({"message": "Cobro registrado y movimiento agregado exitosamente"}), 200
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500


@clientes_bp.route('/service', methods=['POST'])
def add_service():
    data = request.get_json()
    cliente_id = data.get('cliente_id')
    tipo_servicio = data.get('tipo_servicio')
    materiales = data.get('materiales')
    tecnico = data.get('tecnico')
    precio = data.get('precio')

    try:
        service = Service(
            cliente_id=cliente_id,
            tipo_servicio=tipo_servicio,
            materiales=materiales,
            tecnico=tecnico,
            precio=precio,
        )
        db.session.add(service)
        db.session.commit()
        
        # Update the client's `monto_debido` only for the current month
        cliente = Cliente.query.get(cliente_id)
        if cliente:
            cliente.monto_debido += precio
            db.session.commit()

        return jsonify({"message": "Service added and due amount updated"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@clientes_bp.route('/pruebas', methods=['GET'])
@login_required
def obtener_pruebas():
    statement = select(Cliente.id_cliente, Cliente.nombre, Comunidad.nombre_comunidad).join(Comunidad, Cliente.comunidad_id == Comunidad.id_comunidad)
    clientes = db.session.execute(statement).fetchall()
    clientes_data = []
    for d in clientes:
        clientes_data.append({
            "id_cliente": d.id_cliente,
            "nombre": d.nombre,
            "comunidad": d.nombre_comunidad
        })
    return jsonify(clientes_data), 200

@clientes_bp.route('/historial_movimientos/<int:id_cliente>', methods=['GET'])
def get_historial_movimientos(id_cliente):
    from sqlalchemy import extract

    current_month = datetime.now().month
    current_year = datetime.now().year

    movimientos = HistorialMovimientos.query.filter(
            HistorialMovimientos.cliente_id == id_cliente,
            extract('month', HistorialMovimientos.fecha_movimiento) == current_month,
            extract('year', HistorialMovimientos.fecha_movimiento) == current_year
        ).all()    
    # Return the data as JSON
    movimientos_data = [
        {
            "id": movimiento.id,
            "fecha_movimiento": movimiento.fecha_movimiento.strftime('%Y-%m-%d'),
            "tipo_movimiento": movimiento.tipo_movimiento,
            "monto": movimiento.monto
        }
        for movimiento in movimientos
    ]
    
    total_pagado_mes = sum(movimiento.monto for movimiento in movimientos)

    return jsonify({
        "movimientos": movimientos_data,
        "total_pagado_mes": total_pagado_mes
    }), 200