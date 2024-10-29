from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from app.frontend.pantalla_cobro_cobrador_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
import requests

class PantallaCobroCobrador(QWidget):
    def __init__(self, session, change_screen_func, parent=None):
        super().__init__(parent)

        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI

        self.change_screen = change_screen_func
        self.session = session

        # Aquí puedes agregar más funcionalidades o conectores si es necesario
        self.setup_connections()

    def setup_connections(self):
        # Connect each QLabel's mousePressEvent to the same slot function
        self.ui.menuOption1.mousePressEvent = lambda event: self.label_clicked(event, "menuOption1")
        self.ui.menuOption2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption2")
        self.ui.menuOption3.mousePressEvent = lambda event: self.label_clicked(event, "menuOption3")
        self.ui.menuOption7_2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption7_2")


    def label_clicked(self, event, label_name):
        # Determine the screen based on the label clicked
        if label_name == "menuOption1":
            self.change_screen(3)
        elif label_name == "menuOption2":
            self.change_screen(6)
        elif label_name == "menuOption3":
            self.change_screen(9)
        elif label_name == "menuOption7_2":
            self.logout_user()

    
    def logout_user(self):
        # Make a request to log out
        try:
            response = self.session.post("http://127.0.0.1:5000/api/logout")
            if response.status_code == 200:
                self.change_screen(0)  # Redirect to login screen on successful logout
                print("Logged out successfully")
            else:
                QMessageBox.warning(self, "Error", "Logout failed. Please try again.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Request failed: {e}")
            print("Logout request failed:", e)