from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
from app.frontend.pantalla_historial_global_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
from io import BytesIO
import os
import pandas as pd
import requests
from datetime import datetime
import re

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

        self.ui.lineEdit.textChanged.connect(self.filter_table_by_name)
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

    def filter_table_by_name(self):
        search_text = self.ui.lineEdit.text().lower()  # Get the search text from QLineEdit
        self.filtered_data = pd.DataFrame()

        if self.excel_data is not None and not self.excel_data.empty and search_text:
            # Filter the DataFrame based on the name column
            self.filtered_data = self.excel_data[
                self.excel_data['Tipo de cuenta'].str.contains(search_text, case=False, na=False)
            ]
            
            # Reset the index to start from 0
            self.filtered_data.reset_index(drop=True, inplace=True)

            self.populate_table(self.filtered_data)

            total_monthly_payments = self.filtered_data['Movimiento'].apply(self.extract_payment_amount).sum()

            # Display the total payments in the UI (modify as needed)
            self.ui.Adeudo.setText(f"Pagos totales este mes de: {search_text}, ${total_monthly_payments:.2f}")

            #self.ui.Adeudo.setText(f"Pagos totales este mes de: {search_text}, ${total_payments:.2f}")
        else:
            # If search text is empty or data is unavailable, populate with the full data
            self.populate_table(self.excel_data)

    def excel_read(self):
        # Fetch client data from the API when this screen is displayed
        try:
            response = self.session.get("http://127.0.0.1:5000/api/export/excel")
            
            if response.status_code == 200:
                # Read the Excel file into a DataFrame without saving it
                self.excel_data = pd.read_excel(BytesIO(response.content))
                
                self.populate_table(self.excel_data)
                
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

            
    def populate_table(self, data):
        if data is not None and not data.empty:
            headers = [col for col in data.columns if col != "id"]
            self.ui.Table.setColumnCount(len(headers))
            self.ui.Table.setHorizontalHeaderLabels(headers)

            # Clear previous data and set the row count to match new data
            self.ui.Table.setRowCount(len(data))
            
            for row_index, row_data in data.iterrows():
                for col_index, column in enumerate(headers):
                    value = row_data[column] if pd.notna(row_data[column]) else ""  # Handle NaN as empty string
                    item = QTableWidgetItem(str(value))

                    if column == "id":
                        item.setData(Qt.UserRole, row_data["id"])
                    else:
                        self.ui.Table.setItem(row_index, col_index, item)
        else:
            self.ui.Table.setRowCount(0)  # Clear the table if no data
            print("No data available to populate the table.")


    def extract_payment_amount(self, movimiento):
    
        match = re.search(r'\$(\d+(?:\.\d{1,2})?)', movimiento)  # Matches amounts like $100 or $100.50
        if match:
            return float(match.group(1))
        return 0.0