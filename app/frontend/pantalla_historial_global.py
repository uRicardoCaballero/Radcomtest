from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
from app.frontend.pantalla_historial_global_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
from io import BytesIO
import os
import pandas as pd
import requests
from datetime import datetime

class PantallaHistorialGlobal(QWidget):
    def __init__(self, change_screen_func, logout, session, parent=None):
        super().__init__(parent)
        self.excel_data = None
        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI

        self.change_screen = change_screen_func
        self.logout = logout
        self.session = session

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
        self.ui.globaltext.mousePressEvent = lambda event: self.label_clicked(event,"globaltext")
        self.ui.menuOption7_2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption7_2")
        self.ui.GuardarButton.clicked.connect(self.excel_download)


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
            self.change_screen(13)
        elif label_name == "ComunidadText":
            self.change_screen(14)
        elif label_name == "MunicipioText":
            self.change_screen(15)
        elif label_name == "AntenaText":
            self.change_screen(16)
        elif label_name == "globaltext":
            self.change_screen(17)
        elif label_name == "menuOption7_2":
            self.logout()



    def excel_read(self):
        # Fetch client data from the API when this screen is displayed
        try:
            response = self.session.get("http://127.0.0.1:5000/api/export/excel")
            
            if response.status_code == 200:
                # Read the Excel file into a DataFrame without saving it
                self.excel_data = pd.read_excel(BytesIO(response.content))
                print("Excel data loaded into memory.")
                
                self.populate_table()
                
            else:
                print("Failed to load clients:", response.status_code)
        
        except requests.RequestException as e:
            print("Request error:", e)

    def excel_download(self):
        if self.excel_data is not None:
            # Get today's date in the format YYYY-MM-DD
            today_date = datetime.now().strftime("%Y-%m-%d")
            
            # Define the path where you want to save the file with today's date
            save_path = os.path.join(os.getcwd(), f"clientes_export_{today_date}.xlsx")
            
            # Write the content of the DataFrame to an Excel file
            with pd.ExcelWriter(save_path, engine='openpyxl') as writer:
                self.excel_data.to_excel(writer, index=False, sheet_name='Clientes')
            
            print(f"Excel file downloaded successfully and saved as {save_path}")
        else:
            print("No Excel data available to download.")

            
    def populate_table(self):
        if self.excel_data is not None:
                # Set the number of columns
            self.ui.Table.setColumnCount(len(self.excel_data.columns))
            self.ui.Table.setHorizontalHeaderLabels(self.excel_data.columns.tolist())  # Set column headers
                
                # Set the number of rows
            self.ui.Table.setRowCount(len(self.excel_data))
                
                # Populate the table with data
            for row in range(len(self.excel_data)):
                for column in range(len(self.excel_data.columns)):
                    self.ui.Table.setItem(row, column, QTableWidgetItem(str(self.excel_data.iat[row, column])))

            print("Table populated with Excel data.")
        else:
            print("No Excel data available to populate the table.")


        