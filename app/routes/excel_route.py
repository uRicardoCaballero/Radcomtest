from . import *
from app.models import Cliente, Comunidad, Municipio, Antena, HistorialMovimientos
from sqlalchemy import select
from datetime import datetime
from sqlalchemy import func


excel_bp = Blueprint('excel', __name__)
@excel_bp.route('/export/excel', methods=['GET'])
def export_excel():
    # Fetch data from the Clientes table
    statement = select(
        Cliente.nombre, 
        Cliente.telefono,
        Cliente.tipo,
        Cliente.ip,
        Cliente.monto_pagado,
        Cliente.monto_debido,
        Cliente.num_cuenta,
        Cliente.estatus,
        Cliente.estado_cobro,
        Cliente.tipo_cuenta,
        Cliente.fecha_cobro,
        Cliente.fecha_alerta,
        Cliente.fecha_creacion,
        Comunidad.nombre_comunidad,
        Municipio.nombre.label("nombre_municipio"),
        Antena.nombre.label("nombre_antena"),
        HistorialMovimientos.descripcion.label("Movimiento")
    ).join(
        Comunidad, Cliente.comunidad_id == Comunidad.id_comunidad
    ).join(
        Municipio, Comunidad.id_municipio == Municipio.id
    ).join(
        Antena, Municipio.antena_id == Antena.id
    ).outerjoin(
        HistorialMovimientos, HistorialMovimientos.cliente_id == Cliente.id_cliente
    )
    clientes = db.session.execute(statement).fetchall()

    # Create a list of dictionaries for each client
    data = []
    for cliente in clientes:
        data.append({
            'Nombre': cliente.nombre,
            'Teléfono': cliente.telefono,
            'Comunidad': cliente.nombre_comunidad,
            "Municipio": cliente.nombre_municipio,
            "Antena": cliente.nombre_antena,
            "Numero de cuenta": cliente.num_cuenta,
            'Tipo': cliente.tipo,
            'Ip': cliente.ip,
            'Tipo de cuenta': cliente.tipo_cuenta,
            'Monto': cliente.monto_pagado,
            'Monto Debido': cliente.monto_debido,
            'Estado Cobro': cliente.estado_cobro,
            'Estatus': cliente.estatus,
            'Fecha Cobro': cliente.fecha_cobro,
            'Fecha Alerta': cliente.fecha_alerta,
            'Fecha Creación': cliente.fecha_creacion,
            'Movimiento': cliente.Movimiento,
        })

    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Create an Excel file in memory
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Clientes')

    output.seek(0)

    # Send the Excel file as a response
    return send_file(output, 
                     download_name='clientes_export.xlsx', 
                     as_attachment=True)


@excel_bp.route('/historial/<int:cliente_id>', methods=['GET'])
@login_required
def obtener_historial(cliente_id):
    # Clear the session to ensure no cached data is used
    db.session.remove()  # Clears the session cache
    
    # Get the current year and month
    current_month = datetime.now().month
    current_year = datetime.now().year

    # Use an explicit join to fetch client details along with movements
    movimientos = db.session.query(
        HistorialMovimientos,
        Cliente.nombre.label("nombre_cliente")
    ).join(
        Cliente, HistorialMovimientos.cliente_id == Cliente.id_cliente
    ).filter(
        HistorialMovimientos.cliente_id == cliente_id,
        func.extract('month', HistorialMovimientos.fecha) == current_month,
        func.extract('year', HistorialMovimientos.fecha) == current_year
    ).order_by(HistorialMovimientos.fecha.desc()).all()

    # Calculate the total payment for the current month
    total_pago_mes = sum([movimiento.HistorialMovimientos.monto for movimiento in movimientos])

    # Serialize the results
    historial_data = []
    for movimiento, nombre_cliente in movimientos:
        historial_data.append({
            "nombre_cliente": nombre_cliente,  # From the explicit join
            "id": movimiento.id,
            "descripcion": movimiento.descripcion,
            "fecha": movimiento.fecha.strftime('%Y-%m-%d %H:%M:%S'),
            "monto": movimiento.monto,
            "tipo_movimiento": movimiento.tipo_movimiento
        })

    # Return the historial data along with the total payment sum
    return jsonify(historial_data, total_pago_mes), 200