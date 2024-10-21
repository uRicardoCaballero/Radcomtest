import json



def login_as(client, username, password):
    """Helper function to login a user."""
    response = client.post('/api/login', data=json.dumps({
        'username': username,
        'password': password
    }), content_type='application/json')
    
    # Return session cookies or JWT token depending on how authentication is handled
    return response

def register(client, username, password, tipo):
    """Helper function to register a user."""
    response = client.post('/api/register', data=json.dumps({
        'username': username,
        'password': password,
        'tipo_usuario': tipo
    }), content_type='application/json')
    return response

def antena(client, nombre, ubicacion):
    response = client.post('/api/antenas', data=json.dumps({
        'nombre': nombre,
        'ubicacion': ubicacion
    }), content_type='application/json')
    return response

def municipios(client, nombre, antena_id):
    response = client.post('/api/municipios', data=json.dumps({
        'nombre': nombre,
        'antena_id': antena_id
    }), content_type='application/json')
    return response

def zonas(client, nombre, ubicacion, numero_zona):
    response = client.post('api/zonas', data=json.dumps({
        'nombre': nombre,
        'municipio_id': ubicacion,
        'numero_zona': numero_zona
    }), content_type='application/json')
    return response

def clientes(client, id_cliente, nombre, telefono, zona_id, tipo, estado_cobro, estatus, folio_cobro, estado_factura, fecha_cobro, fecha_alerta):
    response = client.post('/api/clientes', data=json.dumps({
        'id_cliente': id_cliente,
        'nombre': nombre,
        'telefono': telefono,
        'zona_id': zona_id,
        'tipo': tipo,
        'estado_cobro': estado_cobro,
        'estatus': estatus,
        'folio_cobro': folio_cobro,
        'estado_factura': estado_factura,
        'fecha_cobro': fecha_cobro,
        'fecha_alerta': fecha_alerta
    }), content_type='application/json')
    return response

def folio(client, folio, cliente_id):
    response = client.post('/api/folios', data=json.dumps({
        'folio': folio,
        'cliente_id': cliente_id
    }), content_type='application/json')
    return response