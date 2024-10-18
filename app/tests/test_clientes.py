from app.tests.utils import *



def test_admin_access(client):
    # Login as admin
    login_response = login_as(client, 'cesar', '54321')
    
    # Assert admin access is allowed
    assert login_response.status_code == 200

    register_admin = register(client, 'registro admin', '12345', 'admin')

    assert register_admin.status_code == 201

    register_antena = antena(client, 'antena admin', 'en prueba local')

    assert register_antena.status_code == 201

    register_municipios = municipios(client, 'parral', '1')

    assert register_municipios.status_code == 201

    register_zona = zonas(client, 'registro zona central', '1', 1)

    assert register_zona.status_code == 201
    
    register_cliente = clientes(client,
                                        "PAz01357951",
                                        "ricardo caballero",
                                        "6271045990",
                                        1,
                                        "libre",
                                        "pagado",
                                        "en linea",
                                        "11111",
                                        "falso",
                                        "2024-10-16",
                                        "2024-10-31")

    assert register_cliente.status_code == 201

    register_folio = folio(client, '77411', 'PAz01357951')

    assert register_folio.status_code == 201

#------------------------------------------------------------------------------------------------
    # Login as admin
    login_response = login_as(client, 'celina', '54321')
    
    # Assert admin access is allowed
    assert login_response.status_code == 200

    register_admin = register(client, 'registro admin', '12345', 'admin')

    assert register_admin.status_code == 403

    register_antena = antena(client, 'antena user', 'en prueba local')

    assert register_antena.status_code == 403

    register_municipios = municipios(client, 'user', '2')

    assert register_municipios.status_code == 403

    register_zona = zonas(client, 'registro zona central', '2', 2)

    assert register_zona.status_code == 403
    
    register_cliente = clientes(client,
                                        "PAz01357952",
                                        "celina caballero",
                                        "6271045990",
                                        1,
                                        "libre",
                                        "pagado",
                                        "en linea",
                                        "11111",
                                        "falso",
                                        "2024-10-16",
                                        "2024-10-31")

    assert register_cliente.status_code == 201

    register_folio = folio(client, '77412', 'PAz01357952')

    assert register_folio.status_code == 201
