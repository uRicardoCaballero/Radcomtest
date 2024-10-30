from PyQt5.QtWidgets import QWidget, QApplication
from app.frontend.pantalla_inicio_ui import Ui_Form  # Importa la clase generada por Qt Designer
import requests
import sys

class PantallaInicio(QWidget):
    def __init__(self, session, parent=None):
        super().__init__(parent)
        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI
        self.session = session

        self.parent = parent

        # Aquí puedes agregar más funcionalidades o conectores si es necesario
        self.ui.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.Usuario.text()
        password = self.ui.Contrasena.text()

        url = "http://127.0.0.1:5000/api/login"
        data = {"username": username, "password": password}

        try:
            response = self.session.post(url, json=data)
            if response.status_code == 200:
                user_data = response.json()
                role = user_data.get("tipo_usuario")

                self.parent.user_role = role
                if role == "Administrador":
                    self.parent.change_screen(1)
                elif role == "Facturador":
                    self.parent.change_screen(2)
                elif role == "Cobrador":
                    self.parent.change_screen(3)
            else:
                print("Login failed")
        except requests.RequestException as e:
            print("request failed:", e)

