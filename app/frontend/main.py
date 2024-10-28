import sys
import threading
from PyQt5.QtWidgets import QApplication, QStackedWidget
from app.frontend.inicio_sesion import PantallaInicioSesion
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
from app.frontend.base_screen import BaseScreen  # Asegúrate de que BaseScreen esté importado
from app.main import *

class MainWindow(BaseScreen):  # Hereda de BaseScreen para utilizar la barra personalizada
    def __init__(self,numberscreen):
        super().__init__(title="RADCOM")  # Pasamos el título a BaseScreen
        self.setGeometry(100, 100, 1320, 800)  # Tamaño de la ventana principal

        # Crear QStackedWidget para manejar las pantallas
        self.stacked_widget = QStackedWidget()

        # Crear las pantallas
        self.pantalla_inicio = PantallaInicioSesion(self)
        self.pantalla_principal_admin = PantallaPrincipalAdmin(self)
        self.pantalla_principal_facturador = PantallaPrincipalFacturador(self)
        self.pantalla_principal_cobrador = PantallaPrincipalCobrador(self)
        self.pantalla_cobro_admin = PantallaCobroAdmin(self)
        self.pantalla_cobro_facturador = PantallaCobroFacturador(self)
        self.pantalla_cobro_cobrador =  PantallaCobroCobrador(self)
        self.pantalla_adeudo_admin = PantallaAdeudoAdmin(self)
        self.pantalla_adeudo_facturador = PantallaAdeudoFacturador(self)
        self.pantalla_adeudo_cobrador = PantallaAdeudoCobrador(self)
        self.pantalla_factura_pendiente_admin = PantallaFacturaPendienteAdmin(self)
        self.pantalla_factura_nueva_admin = PantallaFacturaNuevaAdmin(self)
        self.pantalla_factura_facturador = PantallaFacturaFacturador(self)
        self.pantalla_hitorial_cliente = PantallaHistorialCliente(self)
        self.pantalla_historial_comunidad = PantallaHistorialComunidad(self)
        self.pantalla_historial_municipio = PantallaHistorialMunicipio(self)
        self.pantalla_historial_antena = PantallaHistorialAntena(self)
        self.pantalla_historial_global = PantallaHistorialGlobal(self)
        self.pantalla_modificar = PantallaModificar(self)
        self.pantalla_crearS_cliente = PantallaCrearSCliente(self)
        self.pantalla_crearS_comunidad = PantallaCrearSComunidad(self)
        self.pantalla_crearS_municipio = PantallaCrearSMunicipio(self)
        self.pantalla_crearS_antena = PantallaCrearSAntena(self)


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


        # Añadir el QStackedWidget al layout de contenido en BaseScreen
        self.layout().insertWidget(1, self.stacked_widget)

        # Establecer la pantalla de inicio
    def change_screen(self, screen_number):
        self.stacked_widget.setCurrentIndex(screen_number)

app = None
main_window = None
def frontend(screenumber):
    global app, main_window

    if app is None:
        app = QApplication(sys.argv)
        main_window = MainWindow(screenumber)
        main_window.show()
    else:
        main_window.change_screen(screenumber)

if __name__ == "__main__":
    flask_thread.start()
    sys.exit(app.exec_())
