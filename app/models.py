from datetime import datetime
from pytz import timezone
from app.database import db
local_tz = timezone('America/Mexico_City')

# Antenas table
class Antena(db.Model):
    __tablename__ = 'antenas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    nombreDispositivo = db.Column(db.String(100), nullable=False)
    modelo = db.Column (db.String(100), nullable=False)
    ssid = db.Column (db.String(100), nullable=False)
    municipios = db.relationship('Municipio', backref='antena', lazy=True)

# Municipios table
# class Municipio(db.Model):
#     __tablename__ = 'municipios'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     nombre = db.Column(db.String(100), nullable=False)
#     antena_id = db.Column(db.Integer, db.ForeignKey('antenas.id'), nullable=False)
#     comunidad_id = db.Column(db.Integer, autoincrement=True)
#     nombre_comunidad = db.Column(db.String(100), nullable=True)
#     numero_comunidad = db.Column(db.Integer, nullable=True)

class Municipio(db.Model):
    __tablename__ = 'municipios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    antena_id = db.Column(db.Integer, db.ForeignKey('antenas.id'), nullable=False)



class Comunidad(db.Model):
    __tablename__ = 'comunidad'
    id_comunidad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_comunidad = db.Column(db.String(100), nullable=False)
    id_municipio = db.Column(db.Integer, db.ForeignKey('municipios.id'), nullable=False)



# Clientes table
class Cliente(db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Format: "XXzYYNNNNN"
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(13), nullable=False)
    ip = db.Column(db.String(50), nullable=False)
    num_cuenta = db.Column(db.String(50), nullable=True)
    comunidad_id = db.Column(db.Integer, db.ForeignKey('comunidad.id_comunidad'), nullable=False)  # Updated line
    calle = db.Column(db.String(50), nullable=False)
    colonia = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.String(50), nullable=False)
    codigo_postal = db.Column(db.String(13), nullable=False) 
    tipo = db.Column(db.String(50), nullable=False)  # "libre", "mensual", "anual"
    estado_cobro = db.Column(db.String(50), nullable=False)  # "pagado", "por cobrar"
    estatus = db.Column(db.String(50), nullable=False)  # "en linea", "baja temporal"
    fecha_cobro = db.Column(db.Date, nullable=False)
    fecha_alerta = db.Column(db.Date, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    tipo_cuenta = db.Column(db.String(50), nullable=True)
    plan_pago = db.Column(db.String(50), nullable=False)  # '400', '350', '200', 'libre'
    monto_pagado = db.Column(db.Float, default=0.0)  # To track how much the client has paid
    monto_debido = db.Column(db.Float, default=0.0)
    services = db.relationship("Service", back_populates="cliente")
    historial_movimientos = db.relationship("HistorialMovimientos", back_populates="cliente", cascade="all, delete-orphan")


class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
    tipo_servicio = db.Column(db.String(100), nullable=False)
    materiales = db.Column(db.String(255))
    tecnico = db.Column(db.String(100))
    precio = db.Column(db.Float, nullable=False)

    # Establish a relationship with the Cliente model if necessary
    cliente = db.relationship("Cliente", back_populates="services")

# Folios table
class Folio(db.Model):
    __tablename__ = 'folios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    folio = db.Column(db.String(100), nullable=False)  # Unique payment ID

#Facturas table
class Factura(db.Model):
    __tablename__ = 'facturas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(100), nullable=False)  # Unique to avoid duplicate factura numbers
    pendiente = db.Column(db.String(100), nullable=False)

class HistorialMovimientos(db.Model):
    __tablename__ = 'historial_movimientos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)  # Description of the movement
    fecha = db.Column(db.DateTime, default=datetime.now)  # Timestamp of the movement
    monto = db.Column(db.Float, nullable=True)  # Optional: Amount involved in the movement
    tipo_movimiento = db.Column(db.String(50), nullable=False)  # e.g., 'pago', 'ajuste', 'descuento'

    # Relationships
    cliente = db.relationship("Cliente", back_populates="historial_movimientos")

# Usuarios table
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    tipo_usuario = db.Column(db.String(20), nullable=False)  # "admin", "worker"

    @property
    def is_authenticated(self):
        # Return True if the user is authenticated
        return True  # Adjust this if you have any authentication logic to check
    
    @property
    def is_active(self):
        # Return True if the user is active (allowed to login)
        return True  # Modify this logic if necessary

    @property
    def is_anonymous(self):
        # Return False because this is a logged-in user
        return False

    def get_id(self):
        # Return the unique identifier for the user as a string
        return str(self.id)
    