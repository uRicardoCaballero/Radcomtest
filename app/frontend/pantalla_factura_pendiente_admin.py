from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from app.frontend.pantalla_factura_pendiente_admin_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
import requests

class PantallaFacturaPendienteAdmin(QWidget):
    def __init__(self, change_screen_func, logout, session, parent=None):
        super().__init__(parent)

        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI
        self.session = session
        self.change_screen = change_screen_func
        self.logout = logout

        # Aquí puedes agregar más funcionalidades o conectores si es necesario
        self.setup_connections()

    def setup_connections(self):
        # Connect each QLabel's mousePressEvent to the same slot function
        self.ui.menuOption1.mousePressEvent = lambda event: self.label_clicked(event, "menuOption1")
        self.ui.menuOption2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption2")
        self.ui.menuOption3.mousePressEvent = lambda event: self.label_clicked(event, "menuOption3")
        self.ui.menuOption4.mousePressEvent = lambda event: self.label_clicked(event, "menuOption4")
        self.ui.menuOption5.mousePressEvent = lambda event: self.label_clicked(event, "menuOption5")
        self.ui.menuOption6.mousePressEvent = lambda event: self.label_clicked(event, "menuOption6")
        self.ui.menuOption7.mousePressEvent = lambda event: self.label_clicked(event, "menuOption7")
        self.ui.menuOption8.mousePressEvent = lambda event: self.label_clicked(event, "menuOption8")
        self.ui.PendienteText.mousePressEvent = lambda event: self.label_clicked(event,"PendienteText")
        self.ui.NuevaFactText.mousePressEvent = lambda event: self.label_clicked(event,"NuevaFactText")
        self.ui.menuOption7_2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption7_2")
        self.ui.EnviarButton.clicked.connect(self.guardar_factura)

    def label_clicked(self, event, label_name):
        # Determine the screen based on the label clicked
        if label_name == "menuOption1":
            self.change_screen(1)
        elif label_name == "menuOption2":
            self.change_screen(4)
        elif label_name == "menuOption3":
            self.change_screen(7)
        elif label_name == "menuOption4":
            self.change_screen(10)
        elif label_name == "menuOption5":
            self.change_screen(13)
        elif label_name == "menuOption6":
            self.change_screen(18)
        elif label_name == "menuOption7":
            self.change_screen(19)
        elif label_name == "menuOption8":
            self.change_screen(23)
        elif label_name == "PendienteText":
            self.change_screen(10)
        elif label_name == "NuevaFactText":
            self.change_screen(11)
        elif label_name == "menuOption7_2":
            self.logout()


    def guardar_factura(self):
        # Get the input values from the UI
        nombre = self.ui.NombreHolder.text()
        telefono = self.ui.TelefonoHolder.text()

        # Validate inputs
        if not nombre or not telefono:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Prepare the data for the API call
        data = {
            "nombre": nombre,
            "numero": telefono
        }

        # Make the API call
        try:
            response = self.session.post('http://127.0.0.1:5000/api/facturas', json=data)  # Replace with your actual API URL
            if response.status_code == 201:
                QMessageBox.information(self, "Éxito", "Factura Capturada exitosamente.")
                self.clear_fields()  # Clear fields after successful creation
            else:
                error_message = response.json().get("error", "Error al Capturar Factura.")
                QMessageBox.warning(self, "Error", error_message)
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar al servidor: {str(e)}")

    def clear_fields(self):
        # Clear the input fields
        self.ui.NombreHolder.clear()
        self.ui.TelefonoHolder.clear()
