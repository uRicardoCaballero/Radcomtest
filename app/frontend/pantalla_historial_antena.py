from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QApplication, QTableWidget, QComboBox
from app.frontend.pantalla_historial_antena_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
import pandas as pd
import requests
from io import BytesIO
class PantallaHistorialAntena(QWidget):
    def __init__(self, change_screen_func, logout, session, parent=None):
        super().__init__(parent)

        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI
        self.session = session
        self.change_screen = change_screen_func
        self.logout = logout
        self.table = self.findChild(QTableWidget,"Table")
        self.select1 = self.findChild(QComboBox, "Select1")

        # Aquí puedes agregar más funcionalidades o conectores si es necesario
        self.setup_connections()

    def excel_read(self):
        try:
            response = self.session.get("http://127.0.0.1:5000/api/export/excel")
                
            if response.status_code == 200:
                    # Load Excel data directly into a DataFrame
                self.excel_data = pd.read_excel(BytesIO(response.content))
                    
                    # Populate the table with the fetched data
                self.populate_table()
                self.populate_combobox()
            else:
                QMessageBox.critical(self, "Error", f"Failed to load data: {response.status_code}")
            
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request error: {e}")

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


    def filter_by_comunidad(self):
        """Filter table rows based on the selected comunidad in the ComboBox."""
        selected_antena = self.ui.Select1.currentText()
        
        # If no comunidad is selected, clear the table and return
        if selected_antena == "Seleccionar Antena":
            self.table.clearContents()
            self.table.setRowCount(0)
            return
    
        # Match the selected comunidad_name with comunidad_id in the data
        filtered_data = self.excel_data[self.excel_data['Antena'] == selected_antena]
        
        self.display_table_data(filtered_data)



    def populate_table(self):
        if self.excel_data is not None:
            self.ui.Table.setColumnCount(len(self.excel_data.columns))
            self.ui.Table.setHorizontalHeaderLabels(self.excel_data.columns.tolist())  # Set column headers
                
            self.ui.Table.setRowCount(len(self.excel_data))  # Set the number of rows
            for row in range(len(self.excel_data)):
                for column in range(len(self.excel_data.columns)):
                    self.ui.Table.setItem(row, column, QTableWidgetItem(str(self.excel_data.iat[row, column])))
        else:
            QMessageBox.critical(self, "Error", "No Excel data available to populate the table.")



    
    def display_table_data(self, data):

        self.ui.Table.setRowCount(0)  # This line is necessary to clear previous data
        
        # Debugging - check if the data is empty
        if data.empty:
            return  # Exit if there's no data to display
        
        # Insert new rows
        for row_num, row_data in data.iterrows():
            self.ui.Table.insertRow(0)
            for col_num, value in enumerate(row_data):
                self.ui.Table.setItem(0, col_num, QTableWidgetItem(str(value)))


    def populate_combobox(self):
        if self.excel_data is not None and "Antena" in self.excel_data.columns:
            # Ensure all values are treated as strings
            comunidades = self.excel_data["Antena"].dropna().astype(str).unique()  # Convert to string
            self.ui.Select1.clear()
            self.ui.Select1.addItem("Seleccionar Antena")  # Add a blank item for showing all data
            self.ui.Select1.addItems(sorted(comunidades, key=str))  # Sort as strings explicitly
        else:
            QMessageBox.critical(self, "Error", "No Antena data found or 'Antena' column missing.")
