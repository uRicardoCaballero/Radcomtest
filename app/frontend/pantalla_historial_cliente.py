from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
from app.frontend.pantalla_historial_cliente_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
from io import BytesIO
import os
import pandas as pd
import requests
from datetime import datetime
from PyQt5.QtCore import Qt


class PantallaHistorialCliente(QWidget):
    def __init__(self, change_screen_func, logout, session, parent=None):
        super().__init__(parent)
        self.excel_data = None
        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI

        self.change_screen = change_screen_func
        self.logout = logout
        self.session = session

        # Conexión con las funcionalidades de búsqueda
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
        self.ui.Table.cellClicked.connect(self.on_table_row_selected)


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
        if self.excel_data is not None and search_text:
            # Filter the DataFrame based on the name column
            filtered_data = self.excel_data[self.excel_data['Nombre'].str.contains(search_text, case=False, na=False)]

            self.populate_table(filtered_data)  # Populate the table with filtered data
        else:
            # If search text is empty or data is unavailable, populate with the full data
            self.populate_table(self.excel_data)


    def excel_read(self, client_id):
    # Send a GET request to fetch the client's history and total payments for the current month
        url = f'http://127.0.0.1:5000/api/historial/{client_id}'  # Update with your correct endpoint
        response = self.session.get(url)

        if response.status_code == 200:
        # Unpack the data: historial_data is a list, and total_pago_mes is the total sum
            historial_data, total_pago_mes = response.json()  # Get the historial data and total payment

            # Create a DataFrame only with the historial data
            df = pd.DataFrame(historial_data)

            # Now populate the table with the DataFrame
            self.populate_table(df)

            # Set the total payment amount in the QTextBrowser 'adeudos'
            self.ui.Adeudo.setPlainText(f"Total mes actual: ${total_pago_mes:.2f}")
        else:
            print(f"Failed to fetch data: {response.status_code}")

    

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
            # Exclude the 'id' column from being displayed
            headers = [col for col in data.columns if col != "id"]
            self.ui.Table.setColumnCount(len(headers))
            self.ui.Table.setHorizontalHeaderLabels(headers)

            # Populate the table rows
            self.ui.Table.setRowCount(len(data))
            for row_index, row_data in data.iterrows():
                for col_index, column in enumerate(headers):
                    value = row_data[column]
                    item = QTableWidgetItem(str(value) if pd.notna(value) else "")

                    if column == "id":  # Store `id` as hidden data
                        item.setData(Qt.UserRole, row_data["id"])
                    else:
                        self.ui.Table.setItem(row_index, col_index, item)

            print("Table populated successfully.")
        else:
            self.ui.Table.setRowCount(0)  # Clear the table if no data
            print("No data available to populate the table.")

# Access the hidden ID:
    def on_table_row_selected(self):
        selected_row = self.ui.Table.currentRow()
        if selected_row != -1:
            hidden_id = self.ui.Table.item(selected_row, 0).data(Qt.UserRole)  # Retrieve hidden ID
            print(f"Hidden ID: {hidden_id}")

    def load_client_monthly_payments(self, client_id):
        # Get the current month and year
        current_date = datetime.now()
        current_month = current_date.month
        current_year = current_date.year

        try:
            # Fetch client history data from the API
            response = self.session.get(f"http://127.0.0.1:5000/api/historial/{client_id}")
            if response.status_code == 200:
                historial_data = response.json()  # Parse the JSON data

                # Filter movements for the current month and year
                monthly_movements = [
                    movimiento for movimiento in historial_data
                    if datetime.strptime(movimiento['fecha'], '%Y-%m-%d %H:%M:%S').month == current_month
                    and datetime.strptime(movimiento['fecha'], '%Y-%m-%d %H:%M:%S').year == current_year
                ]

                # Calculate the total sum of payments for the current month
                total_payments = sum(
                    movimiento['monto'] for movimiento in monthly_movements
                    if movimiento['tipo_movimiento'] == 'pago'  # Ensure it's a payment type
                )

                # Print or display the result
                print(f"Total payments for this month: {total_payments}")
                self.show_monthly_payments(total_payments)  # Optional: Display in UI
            else:
                print(f"Failed to fetch client history: {response.status_code}")

        except requests.RequestException as e:
            print("Request error:", e)

    def show_monthly_payments(self, total_payments):
        # Optional: Update the UI with the total payments
        self.ui.Adeudo.setText(f"Total Payments This Month: ${total_payments:.2f}")
