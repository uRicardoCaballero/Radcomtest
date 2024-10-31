from PyQt5.QtWidgets import QWidget, QApplication
from app.frontend.pantalla_crearS_cliente_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
import requests

class PantallaCrearSCliente(QWidget):
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
        self.ui.ClienteText.mousePressEvent = lambda event: self.label_clicked(event,"ClienteText")
        self.ui.ComunidadText.mousePressEvent = lambda event: self.label_clicked(event,"ComunidadText")
        self.ui.MunicipioText.mousePressEvent = lambda event: self.label_clicked(event,"MunicipioText")
        self.ui.AntenaText.mousePressEvent = lambda event: self.label_clicked(event,"AntenaText")
        self.ui.menuOption7_2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption7_2")

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

    
    def populate_antena_dropdown(self):
        """Fetch antena from API and populate the Select1 dropdown."""
        try:
            response = self.session.get("http://127.0.0.1:5000/api/antenas")  # Replace with your actual API URL
            if response.status_code == 200:
                antena = response.json()
                for antena in antena:
                    self.ui.Select1.addItem(antena['nombre'], antena['id'])  # Use id as data for each item
            else:
                print("Error fetching antena:", response.status_code)
        except Exception as e:
            print("Exception occurred while fetching antena:", e)

    def populate_municipio_dropdown(self):
        """Fetch municipios from API and populate the Select2 dropdown."""
        try:
            response = self.session.get("http://127.0.0.1:5000/api/municipios")  # Replace with your actual API URL
            if response.status_code == 200:
                municipio = response.json()
                for municipio in municipio:
                    self.ui.Select2.addItem(municipio['nombre'], municipio['id'])  # Use id as data for each item
            else:
                print("Error fetching municipio:", response.status_code)
        except Exception as e:
            print("Exception occurred while fetching municipio:", e)

    def populate_comunidad_dropdown(self):
        """Fetch comunidad from API and populate the Select3 dropdown."""
        try:
            response = self.session.get("http://127.0.0.1:5000/api/zonas")  # Replace with your actual API URL
            if response.status_code == 200:
                comunidad = response.json()
                for comunidad in comunidad:
                    self.ui.Select3.addItem(comunidad['nombre'], comunidad['id'])  # Use id as data for each item
            else:
                print("Error fetching comunidad:", response.status_code)
        except Exception as e:
            print("Exception occurred while fetching comunidad:", e)

        

    def guardar_cliente(self):
        # Get the input values from the UI
        nombre = self.ui.NombreHolder.text()
        ip = self.ui.IPHolder.text()
        telefono = self.ui.TelHolder.text()
        calle = self.ui.CalleHolder.text()
        colonia = self.ui.CalleHolder_2.text()
        numero = self.ui.NumHolder.text()
        cp = self.ui.CPHolder()

        # Validate inputs
        if not nombre or not ip or not telefono or not calle or not colonia or not numero or not cp:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        if self.ui.AdministradorOption.isChecked():
            tipo = "Gratuito"
        elif self.ui.FacturadorOption.isChecked():
            tipo = "Mensual"
        elif self.ui.CobradorOption.isChecked():
            tipo = "Anual"
        else:
            QMessageBox.warning(self, "Error", "Please select a user type.")
            return

        # Prepare the data for the API call
        data = {
            "nombre": nombre,
            "ip": ip,
            "telefono": telefono,
            "calle": calle,
            "colonia": colonia,
            "numero": numero,
            "cp": cp,
            "tipo": tipo
        }

        # Make the API call
        try:
            response = self.session.post('http://127.0.0.1:5000/api/clientes', json=data)  # Replace with your actual API URL
            if response.status_code == 201:
                QMessageBox.information(self, "Éxito", "Cliente creado exitosamente.")
                self.clear_fields()  # Clear fields after successful creation
            else:
                error_message = response.json().get("error", "Error al crear el cliente.")
                QMessageBox.warning(self, "Error", error_message)
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar al servidor: {str(e)}")


    def clear_fields(self):
        """Clears the input fields."""
        self.ui.Select1.setCurrentIndex(0)
        self.ui.Select2.setCurrentIndex(0)
        self.ui.Select3.setCurrentIndex(0)
        self.ui.NombreHolder.clear()
        self.ui.IPHolder.clear()
        self.ui.TelHolder.clear()
        self.ui.CalleHolder.clear()
        self.ui.CalleHolder_2.clear()
        self.ui.NumHolder.clear()
        self.ui.CPHolder.clear()
        self.ui.GratuitoOption.setChecked(False)
        self.ui.MensualOption.setChecked(False)
        self.ui.AnualOption.setChecked(False)