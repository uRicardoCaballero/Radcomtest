from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from app.frontend.pantalla_crearS_comunidad_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
import requests

class PantallaCrearSComunidad(QWidget):
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
        self.ui.ClienteText.mousePressEvent = lambda event: self.label_clicked(event,"ClienteText")
        self.ui.ComunidadText.mousePressEvent = lambda event: self.label_clicked(event,"ComunidadText")
        self.ui.MunicipioText.mousePressEvent = lambda event: self.label_clicked(event,"MunicipioText")
        self.ui.AntenaText.mousePressEvent = lambda event: self.label_clicked(event,"AntenaText")
        self.ui.menuOption7_2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption7_2")
        self.ui.GuardarButton.clicked.connect(self.save_comunidad)
        #self.ui.CancelarButton.clicked.connect(self.clear_fields)

        # Connect button clicks
        #self.ui.GuardarButton.clicked.connect(self.guardar_antena)
        #self.ui.CancelarButton.clicked.connect(self.clear_fields)

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
        elif label_name == "ClienteText":
            self.change_screen(19)
        elif label_name == "ComunidadText":
            self.change_screen(20)
        elif label_name == "MunicipioText":
            self.change_screen(21)
        elif label_name == "AntenaText":
            self.change_screen(22)
        elif label_name == "menuOption7_2":
            self.logout()


    def populate_municipio_dropdown(self):
        self.ui.Select2.clear()
        try:
            response = self.session.get("http://127.0.0.1:5000/api/municipios")
            if response.status_code == 200:
                municipios = response.json()
                for municipio in municipios:
                    # Add municipio name with municipio ID as data
                    self.ui.Select2.addItem(municipio['nombre'], municipio['id'])
            else:
                print("Failed to fetch municipios:", response.status_code)
        except Exception as e:
            print("Exception occurred while fetching municipios:", e)
    
    def save_comunidad(self):
        municipio_id = self.ui.Select2.currentData()  # Get municipio ID from dropdown selection
        nombre_comunidad = self.ui.NombreComunidadHolder.text()
        data = {
            'nombre_comunidad': nombre_comunidad,
            'id_municipio': municipio_id
        }
       
        try:
            # Send POST request to create a community in the municipio
            response = self.session.post("http://127.0.0.1:5000/api/create_community",json=data)
            
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Comunidad assigned to Municipio successfully!")
            elif response.status_code == 400:
                QMessageBox.information(self, "Aviso", "La comunidad se encuentra duplicada")
            else:
                QMessageBox.warning(self, "Error", response.status_code)
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Error", str(e))

    def clearfields(self):
        self.ui.Select2.clear()