from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from app.frontend.pantalla_factura_facturador_ui import Ui_Form
import requests
import sys

class PantallaFacturaFacturador(QWidget):
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
        # Aquí puedes conectar señales a slots, por ejemplo:
        # self.ui.someButton.clicked.connect(self.some_function)
        pass


    def setup_connections(self):
        # Connect each QLabel's mousePressEvent to the same slot function
        self.ui.menuOption1.mousePressEvent = lambda event: self.label_clicked(event, "menuOption1")
        self.ui.menuOption2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption2")
        self.ui.menuOption3.mousePressEvent = lambda event: self.label_clicked(event, "menuOption3")
        self.ui.menuOption4.mousePressEvent = lambda event: self.label_clicked(event, "menuOption4")
        self.ui.menuOption7_2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption7_2")
        self.ui.EnviarButton.clicked.connect(lambda: self.mark_factura_as_completed(self.current_factura_id))

    def label_clicked(self, event, label_name):
        # Determine the screen based on the label clicked
        if label_name == "menuOption1":
            self.change_screen(2)
        elif label_name == "menuOption2":
            self.change_screen(5)
        elif label_name == "menuOption3":
            self.change_screen(8)
        elif label_name == "menuOption4":
            self.change_screen(12)
        elif label_name == "menuOption8":
            self.change_screen(23)
        elif label_name == "menuOption7_2":
            self.logout()
            
    def mark_factura_as_completed(self, factura_id):
    # Update the current factura to pendiente = "false"
        try:
            update_response = self.session.put(f'http://127.0.0.1:5000/api/factura/{factura_id}')
            
            if update_response.status_code == 200:
                QMessageBox.information(self, "Éxito", "Factura completada.")
                # Now fetch the next pending factura
                self.get_next_pending_factura()
            else:
                error_message = update_response.json().get("error", "Error al actualizar factura.")
                QMessageBox.warning(self, "Error", error_message)
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar al servidor: {str(e)}")

    def get_next_pending_factura(self):
        # Fetch the next factura with pendiente = "true"
        try:
            response = self.session.get('http://127.0.0.1:5000/api/factura/pendiente')
            if response.status_code == 200:
                factura = response.json()
                self.display_factura(factura)
            else:
                QMessageBox.information(self, "Info", "No hay facturas pendientes.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar al servidor: {str(e)}")

    def display_factura(self, factura):
        # Display the factura details on the screen
        self.ui.NombreHolder.setText(factura['nombre'])
        self.ui.TelefonoHolder.setText(factura['numero'])
        self.current_factura_id = factura['id']  # Save the ID for marking as completed
            
    