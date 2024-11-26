from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from app.frontend.pantalla_cobro_admin_ui import Ui_Form  # Importa la clase generada por Qt Designer
from PyQt5.QtCore import Qt
import requests
import sys

class PantallaCobroAdmin(QWidget):
    def __init__(self, change_screen_func, logout, session, parent=None):
        super().__init__(parent)
        
        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI
        
        self.change_screen = change_screen_func
        self.logout = logout
        self.setup_connections()
        self.session = session

        self.client_model = QStandardItemModel(self.ui.listViewClients)
        self.ui.listViewClients.setModel(self.client_model)

        self.client_data = []  # This will store the client data

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
        self.ui.GuardarButton.clicked.connect(self.guardar_cobro)

        self.ui.Select1.addItem("Todos")      # Show all clients
        self.ui.Select1.addItem("Con deuda")  # Clients with adeudo > 0
        self.ui.Select1.addItem("Sin deuda")  # Clients with adeudo == 0

        self.ui.Select1.currentIndexChanged.connect(self.search_clients)

        # Connect the live search input to the search function
        self.ui.lineEdit.textChanged.connect(self.search_clients)

        # Connect client selection event
        self.ui.listViewClients.clicked.connect(self.client_selected)

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
        elif label_name == "menuOption7_2":
            self.logout()

    def search_clients(self):
        search_text = self.ui.lineEdit.text().lower()  # Get the search text from QLineEdit
        adeudo_filter = self.ui.Select1.currentText()

        if self.client_data:
            filtered_data = self.client_data

            # Apply text search filter if there is any text
            if search_text:
                filtered_data = [client for client in filtered_data if search_text in client['nombre'].lower()]

            # Apply adeudo filter based on the combo box selection
            if adeudo_filter == "Con deuda":
                filtered_data = [client for client in filtered_data if client.get('monto_debido', 0) > 0]
            elif adeudo_filter == "Sin deuda":
                filtered_data = [client for client in filtered_data if client.get('monto_debido', 0) == 0]

            # Populate the client list with the filtered data
            self.populate_client_list(filtered_data)
        else:
            # If no client data, display all data
            self.populate_client_list(self.client_data)

    def load_client_data(self):
        # Fetch client data from the API when this screen is displayed
        try:
            response = self.session.get("http://127.0.0.1:5000/api/clientes")
            if response.status_code == 200:
                clients = response.json()
                self.client_data = clients  # Store the client data in an attribute
                self.populate_client_list(clients)
            else:
                print("Failed to load clients:", response.status_code)
        except requests.RequestException as e:
            print("Request error:", e)

    def populate_client_list(self, clients):
        self.client_model.clear()
        for client in clients:
            item = QStandardItem(client['nombre'])
            item.setData(client)  # Store client data within the item for easy access
            item.setEditable(False)
            self.client_model.appendRow(item)


    def client_selected(self, index):
        client_data = self.client_model.itemFromIndex(index).data()
        
        self.selected_client_data = client_data

        if 'nombre' in client_data:
            self.ui.NombreHolder.setText(client_data['nombre'])

        if 'telefono' in client_data:
            self.ui.TelHolder.setText(client_data['telefono'])
        
        if 'ip' in client_data:
            self.ui.IPHolder.setText(client_data['ip'])

        if 'monto_debido' in client_data:
            monto_debido = client_data['monto_debido']

            if monto_debido < 0:
                monto_debido_display = abs(monto_debido)  # Use absolute value to remove the negative sign
            else:
                monto_debido_display = monto_debido
    
            self.ui.CobroHolder.setText(f"{monto_debido_display:.2f}")

            # Set text color based on value
            if monto_debido > 0:
                self.ui.CobroHolder.setStyleSheet("color: red; border: none; font-size: 36px;")
            elif monto_debido < 0:
                self.ui.CobroHolder.setStyleSheet("color: green; border: none; font-size: 36px;")
            else:
                self.ui.CobroHolder.setStyleSheet("color: white; border: none; font-size: 36px;")


    def guardar_cobro(self):

        responseerror = {"error": "El folio ya existe"}
        num_cuenta = self.ui.NumCuentaHolder.text()
        folio = self.ui.FolioHolder.text()

        precio_text  = self.ui.MontoHolder.text().strip()

        if not precio_text.replace('.', '', 1).isdigit():
            print("Invalid price input. Please enter a valid number.")
            return  # Exit or show an error message to the user

        # Convert the validated input to a float
        monto = float(precio_text)

        if self.ui.EfectivoOption.isChecked():
            metodo_pago = "Efectivo"
        elif self.ui.DeptTransfOption.isChecked():
            metodo_pago = "DeptTransfOption"
        else:
            QMessageBox.warning(self, "Error", "Porfavor elige un metodo de pago.")
            return
        
        if not hasattr(self, 'selected_client_data') or self.selected_client_data is None:
            QMessageBox.warning(self, "Error", "Por favor selecciona un cliente antes de guardar el cobro.")
            return
    
        cobro_id = self.selected_client_data.get("id_cliente")
        data2 = {
            "folio": folio,
        }
        try:
            response = self.session.post("http://127.0.0.1:5000/api/folios", json=data2)
            if response.status_code == 201:  
                QMessageBox.information(self, "Success", "Ticket Creado Correctamente")
                data = {
                    "num_cuenta": num_cuenta,
                    "monto_pagado": float(monto),
                    "metodo_pago": metodo_pago
                }
                try:
                    update_response = self.session.put(f'http://127.0.0.1:5000/api/cobro/{cobro_id}', json=data)
                    
                    if update_response.status_code == 200:
                        QMessageBox.information(self, "Éxito", "Cobro Agregado.")
                        self.clear_selection()
                    else:
                        error_message = update_response.json().get("error", "Error al agregar cobro.")
                        QMessageBox.warning(self, "Error", error_message)
                except requests.exceptions.RequestException as e:
                    QMessageBox.critical(self, "Error", f"No se pudo conectar al servidor: {str(e)}")
                self.clear_selection()
            if response.status_code == 400: 
                QMessageBox.warning(self, "Error", responseerror["error"])  # Correct usage
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar al servidor: {str(e)}")

    def clear_selection(self):
        self.ui.NombreHolder.clear()
        self.ui.TelHolder.clear()
        self.ui.IPHolder.clear()
        self.ui.CobroHolder.clear()
        self.ui.NumCuentaHolder.clear()
        self.ui.FolioHolder.clear()
        self.ui.MontoHolder.clear()
        self.ui.listViewClients.clearSelection()
        self.selected_client_data = None
        self.load_client_data()
