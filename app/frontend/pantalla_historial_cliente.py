from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
from app.frontend.pantalla_historial_cliente_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
from io import BytesIO
import os
import pandas as pd
import requests
from datetime import datetime
from PyQt5.QtCore import Qt
import re

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
        self.filtered_data = pd.DataFrame()

        if self.excel_data is not None and not self.excel_data.empty and search_text:
            # Filter the DataFrame based on the name column
            self.filtered_data = self.excel_data[
                self.excel_data['nombre_cliente'].str.contains(search_text, case=False, na=False)
            ]
            
            # Reset the index to start from 0
            self.filtered_data.reset_index(drop=True, inplace=True)

            self.populate_table(self.filtered_data)

            total_monthly_payments = self.filtered_data['descripcion'].apply(self.extract_payment_amount).sum()

            # Display the total payments in the UI (modify as needed)
            self.ui.Adeudo.setText(f"Pagos totales este mes de: {search_text}, ${total_monthly_payments:.2f}")

        else:
            # If search text is empty or data is unavailable, populate with the full data
            self.populate_table(self.excel_data)




    def excel_read_all_clients(self):
    # Fetch all client IDs
        client_ids_url = 'http://127.0.0.1:5000/api/clientesid'
        client_ids_response = self.session.get(client_ids_url)

        if client_ids_response.status_code == 200:
            all_client_ids = client_ids_response.json()  # [{"id_cliente": 1, "nombre": "John"}, ...]

            all_data = []
            for client in all_client_ids:
                client_id = client["id_cliente"]
                url = f'http://127.0.0.1:5000/api/historial/{client_id}'
                response = self.session.get(url)
                if response.status_code == 200:
                    historial_data, _ = response.json()
                    all_data.extend(historial_data)

            # Combine all data into a DataFrame and populate the table
            df = pd.DataFrame(all_data)
            self.excel_data = df
            self.ui.Table.clear()
            self.populate_table(df)
            self.load_all_clients_monthly_payments()

        else:
            print(f"Failed to fetch client IDs: {client_ids_response.status_code}")

    

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

# Access the hidden ID:
    def on_table_row_selected(self):
        selected_row = self.ui.Table.currentRow()
        if selected_row != -1:
            hidden_id = self.ui.Table.item(selected_row, 0).data(Qt.UserRole)  # Retrieve hidden ID

    def load_all_clients_monthly_payments(self):
        # Get the current month and year
        current_date = datetime.now()
        current_month = current_date.month
        current_year = current_date.year

        try:
            # Fetch all client IDs
            client_ids_url = 'http://127.0.0.1:5000/api/clientesid'
            client_ids_response = self.session.get(client_ids_url)

            if client_ids_response.status_code == 200:
                all_client_ids = client_ids_response.json()  # [{"id_cliente": 1, "nombre": "John"}, ...]

                total_all_clients_payments = 0  # To store the total sum for all clients

                for client in all_client_ids:
                    client_id = client["id_cliente"]
                    # Fetch client history data from the API
                    response = self.session.get(f"http://127.0.0.1:5000/api/historial/{client_id}")

                    if response.status_code == 200:
                        try:
                            # Unpack the tuple returned by the API
                            historial_data, total_pago_mes = response.json()

                            # Filter movements for the current month and year
                            monthly_movements = [
                                movimiento for movimiento in historial_data
                                if 'fecha' in movimiento and 'tipo_movimiento' in movimiento and
                                datetime.strptime(movimiento['fecha'], '%Y-%m-%d %H:%M:%S').month == current_month and
                                datetime.strptime(movimiento['fecha'], '%Y-%m-%d %H:%M:%S').year == current_year
                            ]

                            # Sum up payments for this client
                            total_client_payments = sum(
                                movimiento['monto'] for movimiento in monthly_movements
                                if movimiento.get('tipo_movimiento') == 'pago'  # Ensure it's a payment type
                            )

                            # Add this client's payments to the total
                            total_all_clients_payments += total_client_payments
                        except (KeyError, ValueError) as e:
                            print(f"Error processing client {client_id}'s data: {e}")
                    else:
                        print(f"Failed to fetch history for client {client_id}: {response.status_code}")

                # Display the total payments for all clients
                self.show_total_monthly_payments(total_all_clients_payments)
            else:
                print(f"Failed to fetch client IDs: {client_ids_response.status_code}")

        except requests.RequestException as e:
            print("Request error:", e)

    def show_total_monthly_payments(self, total_payments):
        # Update the UI with the total payments for all clients
        self.ui.Adeudo.setText(f"Pagos totales este mes: ${total_payments:.2f}")
        print(f"Total payments for all clients this month: ${total_payments:.2f}")


    def extract_payment_amount(self, movimiento):
    
        match = re.search(r'\$(\d+(?:\.\d{1,2})?)', movimiento)  # Matches amounts like $100 or $100.50
        if match:
            return float(match.group(1))
        return 0.0