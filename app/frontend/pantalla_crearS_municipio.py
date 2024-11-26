from PyQt5.QtWidgets import QWidget, QComboBox, QLineEdit, QPushButton, QApplication, QMessageBox, QTableWidgetItem
from app.frontend.pantalla_crearS_municipio_ui import Ui_Form  # Importa la clase generada por Qt Designer
import os
from datetime import datetime
import pandas as pd
from io import BytesIO
import sys
import requests

class PantallaCrearSMunicipio(QWidget):
    def __init__(self, change_screen_func, logout, session, parent=None):
        super().__init__(parent)

        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI
        self.session = session
        self.change_screen = change_screen_func
        self.logout = logout

        self.populate_antena_dropdown()
        self.setup_connections()
        

        # Aquí puedes agregar más funcionalidades o conectores si es necesario
        

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
        

        self.ui.GuardarButton.clicked.connect(self.guardar_municipio)
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

    
    def populate_antena_dropdown(self,):
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



    def guardar_municipio(self):
        # Get the input values from the UI
        antena = self.ui.Select1.currentData()
        municipio = self.ui.AntenaHolder.text()


        # Validate inputs
        if not antena or not municipio:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Prepare the data for the API call
        data = {
            "antena": antena,
            "municipio": municipio
        }

        # Make the API call
        try:
            response = self.session.post('http://127.0.0.1:5000/api/municipios', json=data)  # Replace with your actual API URL
            if response.status_code == 201:
                QMessageBox.information(self, "Éxito", "Antena creada exitosamente.")

            else:
                error_message = response.json().get("error", "Error al crear la antena.")
                QMessageBox.warning(self, "Error", error_message)
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar al servidor: {str(e)}")



    def clearfields(self):
        self.ui.Select1.clear()
