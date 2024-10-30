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
    ssid = db.Colum (db.String(100), nullable=False)

    municipios = db.relationship('Municipio', backref='antena', lazy=True)

# Municipios table
class Municipio(db.Model):
    __tablename__ = 'municipios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    antena_id = db.Column(db.Integer, db.ForeignKey('antenas.id'), nullable=False)

    zonas = db.relationship('Zona', backref='municipio', lazy=True)

# Zonas table
class Zona(db.Model):
    __tablename__ = 'zonas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    municipio_id = db.Column(db.Integer, db.ForeignKey('municipios.id'), nullable=False)
    numero_zona = db.Column(db.Integer, nullable=False, unique=True)  # 2-digit number defined by the user

    clientes = db.relationship('Cliente', backref='zona', lazy=True)

# Clientes table
class Cliente(db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column(db.String(20), primary_key=True)  # Format: "XXzYYNNNNN"
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(13
), nullable=False)
    ip = db.Column(db.String(50), nullable=False)
    zona_id = db.Column(db.Integer, db.ForeignKey('zonas.numero_zona'), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # "libre", "mensual", "anual"
    estado_cobro = db.Column(db.String(50), nullable=False)  # "pagado", "por cobrar"
    estatus = db.Column(db.String(50), nullable=False)  # "en linea", "baja temporal"
    folio_cobro = db.Column(db.String(50), nullable=False)
    estado_factura = db.Column(db.String, nullable=False)
    fecha_cobro = db.Column(db.Date, nullable=False)
    fecha_alerta = db.Column(db.Date, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    plan_pago = db.Column(db.String(50), nullable=False)  # '400', '350', '200', 'libre'
    monto_pagado = db.Column(db.Float, default=0.0)  # To track how much the client has paid

    def es_libre(self):
        """Returns True if the client is on the 'libre' plan."""
        return self.plan_pago == 'libre'

    def monto_restante(self):
        """Calculates the remaining amount based on the payment plan."""
        if self.es_libre():
            return 0
        total_plan = float(self.plan_pago)
        return total_plan - self.monto_pagado
    

    folios = db.relationship('Folio', backref='cliente', lazy=True)

# Folios table
class Folio(db.Model):
    __tablename__ = 'folios'
    folio = db.Column(db.String(100), primary_key=True)  # Unique payment ID
    cliente_id = db.Column(db.String(20), db.ForeignKey('clientes.id_cliente'), nullable=False)

#Facturas table
class Factura(db.Model):
    __tablename__ = 'facturas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(100), nullable=False, unique=True)  # Unique to avoid duplicate factura numbers

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