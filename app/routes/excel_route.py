from . import *
from app.models import Cliente

excel_bp = Blueprint('excel', __name__)
@excel_bp.route('/export/excel', methods=['GET'])
def export_excel():
    # Fetch data from the Clientes table
    clientes = Cliente.query.all()

    # Create a list of dictionaries for each client
    data = []
    for cliente in clientes:

        data.append({
            'ID Cliente': cliente.id_cliente,
            'Nombre': cliente.nombre,
            'Teléfono': cliente.telefono,
            'Zona ID': cliente.zona_id,
            'Tipo': cliente.tipo,
            'Estado Cobro': cliente.estado_cobro,
            'Estatus': cliente.estatus,
            'Folio Cobro': cliente.folio_cobro,
            'Estado Factura': cliente.estado_factura,
            'Fecha Cobro': cliente.fecha_cobro,
            'Fecha Alerta': cliente.fecha_alerta,
            'Fecha Creación': cliente.fecha_creacion
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