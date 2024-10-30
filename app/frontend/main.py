import sys
import threading
import requests
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QMessageBox, QStackedWidget,QMainWindow
from app.frontend.pantalla_principal_admin import PantallaPrincipalAdmin
from app.frontend.pantalla_principal_facturador import PantallaPrincipalFacturador
from app.frontend.pantalla_principal_cobrador import PantallaPrincipalCobrador
from app.frontend.pantalla_cobro_admin import PantallaCobroAdmin
from app.frontend.pantalla_cobro_facturador import PantallaCobroFacturador
from app.frontend.pantalla_cobro_cobrador import PantallaCobroCobrador
from app.frontend.pantalla_adeudo_admin import PantallaAdeudoAdmin
from app.frontend.pantalla_adeudo_facturador import PantallaAdeudoFacturador
from app.frontend.pantalla_adeudo_cobrador import PantallaAdeudoCobrador
from app.frontend.pantalla_factura_pendiente_admin import PantallaFacturaPendienteAdmin
from app.frontend.pantalla_factura_nueva_admin import PantallaFacturaNuevaAdmin
from app.frontend.pantalla_factura_facturador import PantallaFacturaFacturador
from app.frontend.pantalla_historial_cliente import PantallaHistorialCliente
from app.frontend.pantalla_historial_comunidad import PantallaHistorialComunidad
from app.frontend.pantalla_historial_municipio import PantallaHistorialMunicipio
from app.frontend.pantalla_historial_antena import PantallaHistorialAntena
from app.frontend.pantalla_historial_global import PantallaHistorialGlobal
from app.frontend.pantalla_modificar import PantallaModificar
from app.frontend.pantalla_crearS_cliente import PantallaCrearSCliente
from app.frontend.pantalla_crearS_comunidad import PantallaCrearSComunidad
from app.frontend.pantalla_crearS_municipio import PantallaCrearSMunicipio
from app.frontend.pantalla_crearS_antena import PantallaCrearSAntena
from app.frontend.pantalla_inicio import PantallaInicio  # Asegúrate de que BaseScreen esté importado
from app.main import *


class MainWindow(QMainWindow):  # Hereda de BaseScreen para utilizar la barra personalizada
    def __init__(self):
        super().__init__()  # Pasamos el título a BaseScreen
        self.setGeometry(100, 100, 1320, 800)  # Tamaño de la ventana principal

        self.session = requests.Session()
        #self.user_role = None
        # Crear QStackedWidget para manejar las pantallas
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Crear las pantallas
        self.pantalla_inicio = PantallaInicio(self.session, self)
        self.pantalla_principal_admin = PantallaPrincipalAdmin(self.change_screen,self.logout, self)
        self.pantalla_principal_facturador = PantallaPrincipalFacturador(self.change_screen,self.logout, self)
        self.pantalla_principal_cobrador = PantallaPrincipalCobrador(self.change_screen,self.logout, self)
        self.pantalla_cobro_admin = PantallaCobroAdmin(self.change_screen,self.logout, self.session, self)
        self.pantalla_cobro_facturador = PantallaCobroFacturador(self.change_screen,self.logout, self)
        self.pantalla_cobro_cobrador =  PantallaCobroCobrador(self.change_screen,self.logout, self)
        self.pantalla_adeudo_admin = PantallaAdeudoAdmin(self.change_screen,self.logout, self.session, self)
        self.pantalla_adeudo_facturador = PantallaAdeudoFacturador(self.change_screen,self.logout, self)
        self.pantalla_adeudo_cobrador = PantallaAdeudoCobrador(self.change_screen,self.logout, self)
        self.pantalla_factura_pendiente_admin = PantallaFacturaPendienteAdmin(self.change_screen,self.logout, self)
        self.pantalla_factura_nueva_admin = PantallaFacturaNuevaAdmin(self.change_screen,self.logout, self)
        self.pantalla_factura_facturador = PantallaFacturaFacturador(self.change_screen,self.logout, self)
        self.pantalla_hitorial_cliente = PantallaHistorialCliente(self.change_screen,self.logout, self)
        self.pantalla_historial_comunidad = PantallaHistorialComunidad(self.change_screen,self.logout, self)
        self.pantalla_historial_municipio = PantallaHistorialMunicipio(self.change_screen,self.logout, self)
        self.pantalla_historial_antena = PantallaHistorialAntena(self.change_screen,self.logout, self)
        self.pantalla_historial_global = PantallaHistorialGlobal(self.change_screen,self.logout, self)
        self.pantalla_modificar = PantallaModificar(self.change_screen,self.logout, self.session, self)
        self.pantalla_crearS_cliente = PantallaCrearSCliente(self.change_screen,self.logout, self)
        self.pantalla_crearS_comunidad = PantallaCrearSComunidad(self.change_screen,self.logout, self)
        self.pantalla_crearS_municipio = PantallaCrearSMunicipio(self.change_screen,self.logout, self)
        self.pantalla_crearS_antena = PantallaCrearSAntena(self.change_screen,self.logout, self)
        

        # Añadir las pantallas al QStackedWidget
        self.stacked_widget.addWidget(self.pantalla_inicio)
        self.stacked_widget.addWidget(self.pantalla_principal_admin)
        self.stacked_widget.addWidget(self.pantalla_principal_facturador)
        self.stacked_widget.addWidget(self.pantalla_principal_cobrador)
        self.stacked_widget.addWidget(self.pantalla_cobro_admin)
        self.stacked_widget.addWidget(self.pantalla_cobro_facturador)
        self.stacked_widget.addWidget(self.pantalla_cobro_cobrador)
        self.stacked_widget.addWidget(self.pantalla_adeudo_admin)
        self.stacked_widget.addWidget(self.pantalla_adeudo_facturador)
        self.stacked_widget.addWidget(self.pantalla_adeudo_cobrador)
        self.stacked_widget.addWidget(self.pantalla_factura_pendiente_admin)
        self.stacked_widget.addWidget(self.pantalla_factura_nueva_admin)
        self.stacked_widget.addWidget(self.pantalla_factura_facturador)
        self.stacked_widget.addWidget(self.pantalla_hitorial_cliente)
        self.stacked_widget.addWidget(self.pantalla_historial_comunidad)
        self.stacked_widget.addWidget(self.pantalla_historial_municipio)
        self.stacked_widget.addWidget(self.pantalla_historial_antena)
        self.stacked_widget.addWidget(self.pantalla_historial_global)
        self.stacked_widget.addWidget(self.pantalla_modificar)
        self.stacked_widget.addWidget(self.pantalla_crearS_cliente)
        self.stacked_widget.addWidget(self.pantalla_crearS_comunidad)
        self.stacked_widget.addWidget(self.pantalla_crearS_municipio)
        self.stacked_widget.addWidget(self.pantalla_crearS_antena)

        self.stacked_widget.setCurrentWidget(self.pantalla_inicio)

    def change_screen(self, screen_number):
        self.stacked_widget.setCurrentIndex(screen_number)
        if screen_number == 4:
            self.pantalla_cobro_admin.load_client_data()
        elif screen_number == 7:
            self.pantalla_adeudo_admin.load_client_data()
        elif screen_number == 18:
            self.pantalla_modificar.load_client_data()
        # Añadir el QStackedWidget al layout de contenido en BaseScreen
        # main_layout = QVBoxLayout(self)
        # main_layout.addWidget(self.stacked_widget)
        
        #self.stacked_widget.setCurrentIndex(numberscreen)
    def logout(self):
        url = "http://127.0.0.1:5000/api/logout"
        try:
            response = self.session.post(url)  # Use stored session for logout
            if response.status_code == 200:
                self.change_screen(0)  # Redirect to login screen
                print("Logged out successfully")
            else:
                QMessageBox.warning(self, "Error", "Logout failed. Please try again.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Request failed: {e}")
            print("Logout request failed:", e)

        




    
