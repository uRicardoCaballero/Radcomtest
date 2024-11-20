from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from app.frontend.pantalla_folios_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
import requests

class PantallaFolio(QWidget):
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
        self.ui.menuOption7_2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption7_2")
        self.ui.GuardarButton.clicked.connect(self.create_ticket)



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
        elif label_name == "menuOption7_2":
            self.logout()



    def create_ticket(self):
        # Get input values
        ticket = self.ui.NumCuentaHolder.text()  # Assuming you have a QLineEdit for username

        # Prepare the data for the API
        data = {
            "folio": ticket,
        }

        # Send the POST request to the API
        try:
            response = self.session.post("http://127.0.0.1:5000/api/folios", json=data)
            if response.status_code == 201:  # Assuming 201 is the status code for successful creation
                QMessageBox.information(self, "Success", "Ticket Creado Correctamente")
                # Optionally clear input fields after successful creation
                self.ui.NumCuentaHolder.clear()
            else:
                QMessageBox.warning(self, "Error", "Fallo la creacion de Ticket, intenta de nuevo.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Request failed: {e}")

