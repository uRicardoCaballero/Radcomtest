from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor
from datetime import datetime
import requests
from app.frontend.pantalla_principal_admin_ui import Ui_Form  # Importa la clase generada por Qt Designer


class PantallaPrincipalAdmin(QWidget):
    def __init__(self, change_screen_func, logout, session, parent=None):
        super().__init__(parent)

        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI
        
        self.change_screen = change_screen_func
        self.logout = logout

        # Call the function to set up connections
        self.setup_connections()
        
        # Call the function to update the date
        self.update_date()

        # Timer to update the date every second (for testing) or set it to every day in production
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_date)
        self.timer.start(1000)  # Update every second for testing, use 86400000 ms for daily

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
        self.ui.pushButton.mousePressEvent = lambda event: self.create_user()

    def label_clicked(self, event, label_name):
        # Determine the screen based on the label clicked
        if label_name == "menuOption2":
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

    def create_user(self):
        # Get input values
        username = self.ui.Usuario.text()  # Assuming you have a QLineEdit for username
        password = self.ui.Contrasena.text()  # Assuming you have a QLineEdit for password

        # Get user type from radio buttons
        if self.ui.AdministradorOption.isChecked():
            user_type = "Administrador"
        elif self.ui.FacturadorOption.isChecked():
            user_type = "Facturador"
        elif self.ui.CobradorOption.isChecked():
            user_type = "Cobrador"
        else:
            QMessageBox.warning(self, "Error", "Please select a user type.")
            return

        # Prepare the data for the API
        data = {
            "username": username,
            "password": password,
            "tipo_usuario": user_type
        }

        # Send the POST request to the API
        try:
            response = requests.post("http://127.0.0.1:5000/api/usuarios", json=data)
            if response.status_code == 201:  # Assuming 201 is the status code for successful creation
                QMessageBox.information(self, "Success", "User created successfully.")
                # Optionally clear input fields after successful creation
                self.ui.Usuario.clear()
                self.ui.Contrasena.clear()
                self.ui.AdministradorOption.setChecked(False)
                self.ui.FacturadorOption.setChecked(False)
                self.ui.CobradorOption.setChecked(False)
            else:
                QMessageBox.warning(self, "Error", "User creation failed. Please try again.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Request failed: {e}")

    def update_date(self):
        # Get today's date and day number
        today = datetime.now()
        day = today.day
        formatted_date = today.strftime("%d-%m-%Y")
        
        # Update the QLineEdit text with the current date
        self.ui.lineEdit.setText(formatted_date)
        
        # Apply color based on the day of the month
        if day <= 10:  # Days 1 to 10
            self.ui.lineEdit.setStyleSheet("color: white; border: none; font-family: 'Montserratl'; font-size: 70px;")
        elif 11 <= day <= 15:  # Days 11 to 15
            # Gradually transition from yellow to red
            red_intensity = int(255 * ((day - 10) / 5))  # From 0 to 255 between days 11 and 15
            green_intensity = 255 - red_intensity  # Decrease green intensity
            color = QColor(255, green_intensity, 0)  # RGB: full red, decreasing green
            self.ui.lineEdit.setStyleSheet(f"color: rgb({color.red()}, {color.green()}, {color.blue()}); border: none; font-family: 'Montserratl'; font-size: 70px;")
        else:  # Days 16 to the end of the month
            self.ui.lineEdit.setStyleSheet("color: white; border: none; font-family: 'Montserratl'; font-size: 70px;")
