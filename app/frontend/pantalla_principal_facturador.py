from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTimer, Qt
from app.frontend.pantalla_principal_facturador_ui import Ui_Form  # Importa la clase generada por Qt Designer
from PyQt5.QtGui import QColor
import sys
from datetime import datetime

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

