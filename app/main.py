from flask import Flask, request, jsonify, send_file
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from sqlalchemy.orm import Session
from datetime import datetime, date
import os
import pandas as pd
from io import BytesIO
from pytz import timezone

from app.models import db, Antena, Municipio, Zona, Cliente, Folio, Usuario
from app.database import init_db

app = Flask(__name__)

init_db(app)
# Flask-Login setup
app.secret_key = 'fX9l3LhCudCwVqUUDZ0q80RvCiswOFnLoYzzXpn64UzfEoqqBy9CRh7lZEnhIUsN'

local_tz = timezone('America/Mexico_City')


# Initialize the database
migrate = Migrate(app, db)
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Create directories if they don't exist
os.makedirs(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../ticket_images'), exist_ok=True)

# User loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Usuario,( int(user_id)))
#---------------------

#routes here----

#--------------

# Route to register a new user (Admin only)
@app.route('/register', methods=['POST'])
@login_required
def register():
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    tipo_usuario = data.get('tipo_usuario')  # "admin" or "worker"

    if not username or not password or not tipo_usuario:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    if Usuario.query.filter_by(username=username).first():
        return jsonify({"error": "El nombre de usuario ya existe"}), 400

    hashed_password = generate_password_hash(password)

    nuevo_usuario = Usuario(
        username=username,
        password=hashed_password,
        tipo_usuario=tipo_usuario
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"message": "Usuario registrado exitosamente"}), 201


# Route to login a user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    print(f"Trying to log in with username: {username} and password: {password}")

    if not username or not password:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    usuario = Usuario.query.filter_by(username=username).first()

    if usuario and check_password_hash(usuario.password, password):
        login_user(usuario)
        return jsonify({"message": "Inicio de sesión exitoso", "tipo_usuario": usuario.tipo_usuario}), 200

    return jsonify({"error": "Nombre de usuario o contraseña inválidos"}), 401

# Route to logout a user
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Cierre de sesión exitoso"}), 200

# Utility function to save uploaded images
def save_image(image):
    filename = secure_filename(image.filename)
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    filename = f"{timestamp}_{filename}"
    image_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../ticket_images', filename)
    image.save(image_path)
    return filename  # Return the filename to store in the database

# ------------------- Antenas Routes -------------------

@app.route('/antenas', methods=['POST'])
@login_required
def crear_antena():
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    data = request.get_json()
    nombre = data.get('nombre')
    ubicacion = data.get('ubicacion')  # Optional

    if not nombre:
        return jsonify({"error": "El nombre es requerido"}), 400

    nueva_antena = Antena(
        nombre=nombre,
        ubicacion=ubicacion
    )

    db.session.add(nueva_antena)
    db.session.commit()

    return jsonify({"message": "Antena creada exitosamente", "id": nueva_antena.id}), 201
#----------------------------------------TEMPORAL TESTS!!!!!!!!!!!!!

@app.route('/reset-db', methods=['POST'])  # Add appropriate methods/permissions for this operation
def reset_db():
    db.drop_all()
    db.create_all()  # (Optional) Re-create the tables if you want a fresh schema
    return "Database reset complete."

@app.route('/init_admin', methods=['POST'])
def init_admin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    if Usuario.query.filter_by(username=username).first():
        return jsonify({"error": "El nombre de usuario ya existe"}), 400

    hashed_password = generate_password_hash(password)

    admin_usuario = Usuario(
        username=username,
        password=hashed_password,
        tipo_usuario='admin'
    )

    db.session.add(admin_usuario)
    db.session.commit()

    return jsonify({"message": "Admin creado exitosamente"}), 201




#----------------------------------------TEMPORAL TESTS!!!!!!!!!!!!!
@app.route('/antenas', methods=['GET'])
@login_required
def obtener_antenas():
    antenas = Antena.query.all()
    antenas_data = []
    for antena in antenas:
        antenas_data.append({
            "id": antena.id,
            "nombre": antena.nombre,
            "ubicacion": antena.ubicacion
        })
    return jsonify(antenas_data), 200

@app.route('/antenas/<int:antena_id>', methods=['GET'])
@login_required
def obtener_antena(antena_id):
    antena = Antena.query.get_or_404(antena_id)
    antena_data = {
        "id": antena.id,
        "nombre": antena.nombre,
        "ubicacion": antena.ubicacion
    }
    return jsonify(antena_data), 200

@app.route('/antenas/<int:antena_id>', methods=['PUT'])
@login_required
def actualizar_antena(antena_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    antena = Antena.query.get_or_404(antena_id)
    data = request.get_json()

    antena.nombre = data.get('nombre', antena.nombre)
    antena.ubicacion = data.get('ubicacion', antena.ubicacion)

    db.session.commit()

    return jsonify({"message": "Antena actualizada exitosamente"}), 200

@app.route('/antenas/<int:antena_id>', methods=['DELETE'])
@login_required
def eliminar_antena(antena_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    antena = Antena.query.get_or_404(antena_id)
    db.session.delete(antena)
    db.session.commit()

    return jsonify({"message": "Antena eliminada exitosamente"}), 200

# ------------------- Municipios Routes -------------------

@app.route('/municipios', methods=['POST'])
@login_required
def crear_municipio():
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    data = request.get_json()
    nombre = data.get('nombre')
    antena_id = data.get('antena_id')

    if not nombre or not antena_id:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    # Check if the antena exists
    antena = Antena.query.get(antena_id)
    if not antena:
        return jsonify({"error": "Antena no encontrada"}), 404

    nuevo_municipio = Municipio(
        nombre=nombre,
        antena_id=antena_id
    )

    db.session.add(nuevo_municipio)
    db.session.commit()

    return jsonify({"message": "Municipio creado exitosamente", "id": nuevo_municipio.id}), 201

@app.route('/municipios', methods=['GET'])
@login_required
def obtener_municipios():
    municipios = Municipio.query.all()
    municipios_data = []
    for municipio in municipios:
        municipios_data.append({
            "id": municipio.id,
            "nombre": municipio.nombre,
            "antena_id": municipio.antena_id
        })
    return jsonify(municipios_data), 200

@app.route('/municipios/<int:municipio_id>', methods=['GET'])
@login_required
def obtener_municipio(municipio_id):
    municipio = Municipio.query.get_or_404(municipio_id)
    municipio_data = {
        "id": municipio.id,
        "nombre": municipio.nombre,
        "antena_id": municipio.antena_id
    }
    return jsonify(municipio_data), 200

@app.route('/municipios/<int:municipio_id>', methods=['PUT'])
@login_required
def actualizar_municipio(municipio_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    municipio = Municipio.query.get_or_404(municipio_id)
    data = request.get_json()

    municipio.nombre = data.get('nombre', municipio.nombre)
    antena_id = data.get('antena_id')
    if antena_id:
        # Check if the new antena exists
        antena = Antena.query.get(antena_id)
        if not antena:
            return jsonify({"error": "Antena no encontrada"}), 404
        municipio.antena_id = antena_id

    db.session.commit()

    return jsonify({"message": "Municipio actualizado exitosamente"}), 200

@app.route('/municipios/<int:municipio_id>', methods=['DELETE'])
@login_required
def eliminar_municipio(municipio_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    municipio = Municipio.query.get_or_404(municipio_id)
    db.session.delete(municipio)
    db.session.commit()

    return jsonify({"message": "Municipio eliminado exitosamente"}), 200

# ------------------- Zonas Routes -------------------

@app.route('/zonas', methods=['POST'])
@login_required
def crear_zona():
    if current_user.tipo_usuario != 'admin':
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

@app.route('/zonas', methods=['GET'])
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

@app.route('/zonas/<int:zona_id>', methods=['GET'])
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

@app.route('/zonas/<int:zona_id>', methods=['PUT'])
@login_required
def actualizar_zona(zona_id):
    if current_user.tipo_usuario != 'admin':
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

@app.route('/zonas/<int:zona_id>', methods=['DELETE'])
@login_required
def eliminar_zona(zona_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    zona = Zona.query.get_or_404(zona_id)
    db.session.delete(zona)
    db.session.commit()

    return jsonify({"message": "Zona eliminada exitosamente"}), 200

# ------------------- Clientes Routes -------------------

@app.route('/clientes', methods=['POST'])
@login_required
def crear_cliente():

    data = request.get_json()

    id_cliente = data.get('id_cliente')  # Format: "XXzYYNNNNN"
    nombre = data.get('nombre')
    telefono = data.get('telefono')
    zona_id = data.get('zona_id')
    tipo = data.get('tipo')  # "libre", "mensual", "anual"
    estado_cobro = data.get('estado_cobro')  # "pagado", "por cobrar"
    estatus = data.get('estatus')  # "en linea", "baja temporal"
    folio_cobro = data.get('folio_cobro')
    estado_factura = data.get('estado_factura')  # Boolean
    fecha_cobro = datetime.strptime(data.get('fecha_cobro'), '%Y-%m-%d').date() # Date
    fecha_alerta = datetime.strptime(data.get('fecha_alerta'), '%Y-%m-%d').date()
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
    
    # Check if id_cliente is unique
    if Cliente.query.get(id_cliente):
        return jsonify({"error": "id_cliente ya existe"}), 400

    # Check if zona exists
    zona = Zona.query.get(zona_id)
    if not zona:
        return jsonify({"error": "Zona no encontrada"}), 404

    nuevo_cliente = Cliente(
        id_cliente=id_cliente,
        nombre=nombre,
        telefono=telefono,
        zona_id=zona_id,
        tipo=tipo,
        estado_cobro=estado_cobro,
        estatus=estatus,
        folio_cobro=folio_cobro,
        estado_factura=estado_factura,
        fecha_cobro=fecha_cobro,
        fecha_alerta=fecha_alerta
    )

    db.session.add(nuevo_cliente)
    db.session.commit()

    return jsonify({"message": "Cliente creado exitosamente", "id_cliente": nuevo_cliente.id_cliente}), 201

@app.route('/clientes', methods=['GET'])
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

@app.route('/clientes/<string:id_cliente>', methods=['GET'])
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

@app.route('/clientes/<string:id_cliente>', methods=['PUT'])
@login_required
def actualizar_cliente(id_cliente):
    if current_user.tipo_usuario != 'admin':
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

@app.route('/clientes/<string:id_cliente>', methods=['DELETE'])
@login_required
def eliminar_cliente(id_cliente):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    cliente = Cliente.query.get_or_404(id_cliente)
    db.session.delete(cliente)
    db.session.commit()

    return jsonify({"message": "Cliente eliminado exitosamente"}), 200

# ------------------- Folios Routes -------------------

@app.route('/folios', methods=['POST'])
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

@app.route('/folios', methods=['GET'])
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

@app.route('/folios/<string:folio>', methods=['GET'])
@login_required
def obtener_folio(folio):
    folio_obj = Folio.query.get_or_404(folio)
    folio_data = {
        "folio": folio_obj.folio,
        "cliente_id": folio_obj.cliente_id
    }
    return jsonify(folio_data), 200

@app.route('/folios/<string:folio>', methods=['PUT'])
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

@app.route('/folios/<string:folio>', methods=['DELETE'])
@login_required
def eliminar_folio(folio):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    folio_obj = Folio.query.get_or_404(folio)
    db.session.delete(folio_obj)
    db.session.commit()

    return jsonify({"message": "Folio eliminado exitosamente"}), 200

# ------------------- Usuarios Routes -------------------

@app.route('/usuarios', methods=['GET'])
@login_required
def obtener_usuarios():
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    usuarios = Usuario.query.all()
    usuarios_data = []
    for usuario in usuarios:
        usuarios_data.append({
            "id": usuario.id,
            "username": usuario.username,
            "tipo_usuario": usuario.tipo_usuario
        })
    return jsonify(usuarios_data), 200

@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
@login_required
def obtener_usuario(usuario_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    usuario = Usuario.query.get_or_404(usuario_id)
    usuario_data = {
        "id": usuario.id,
        "username": usuario.username,
        "tipo_usuario": usuario.tipo_usuario
    }
    return jsonify(usuario_data), 200

@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
@login_required
def actualizar_usuario(usuario_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    usuario = Usuario.query.get_or_404(usuario_id)
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    tipo_usuario = data.get('tipo_usuario')

    if username:
        if Usuario.query.filter(Usuario.username == username, Usuario.id != usuario_id).first():
            return jsonify({"error": "El nombre de usuario ya existe"}), 400
        usuario.username = username

    if password:
        usuario.password = generate_password_hash(password)

    if tipo_usuario:
        usuario.tipo_usuario = tipo_usuario

    db.session.commit()

    return jsonify({"message": "Usuario actualizado exitosamente"}), 200

@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
@login_required
def eliminar_usuario(usuario_id):
    if current_user.tipo_usuario != 'admin':
        return jsonify({"error": "Acceso denegado"}), 403

    usuario = Usuario.query.get_or_404(usuario_id)
    db.session.delete(usuario)
    db.session.commit()

    return jsonify({"message": "Usuario eliminado exitosamente"}), 200




@app.route('/export/excel', methods=['GET'])
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


# ------------------- Run the Flask App -------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True, host='0.0.0.0', port=8000)