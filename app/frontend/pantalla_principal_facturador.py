from PyQt5.QtWidgets import QWidget, QApplication
from app.frontend.pantalla_principal_facturador_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys

class PantallaPrincipalFacturador(QWidget):
    def __init__(self, change_screen_func, logout, parent=None):
        super().__init__(parent)

        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI

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
        self.ui.menuOption7_2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption7_2")

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
        elif label_name == "menuOption7_2":
            self.logout()
