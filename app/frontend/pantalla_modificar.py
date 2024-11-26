from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QButtonGroup
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from app.frontend.pantalla_modificar_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
import requests

class PantallaModificar(QWidget):
    def __init__(self, change_screen_func, logout, session, parent=None):
        super().__init__(parent)

        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI
        self.session = session
        self.change_screen = change_screen_func
        self.logout = logout

        self.populate_antena_dropdown()
        self.populate_municipio_dropdown()
        # Aquí puedes agregar más funcionalidades o conectores si es necesario
        self.setup_connections()
        

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
        self.ui.GuardarButton.mousePressEvent = lambda event: self.guardar_cliente()



        # Connect the live search input to the search function
        self.ui.BuscarHolder.textChanged.connect(self.search_clients)

        # Connect client selection event
        self.ui.listViewClients.clicked.connect(self.client_selected)
        



    def on_municipio_changed(self, index):
        self.populate_antena_dropdown()


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
        search_text = self.ui.BuscarHolder.text().lower()  # Get the search text from QLineEdit
        if self.client_data and search_text:
            # Filter the client data based on the name
            filtered_data = [client for client in self.client_data if search_text in client['nombre'].lower()]
            self.populate_client_list(filtered_data)  # Populate the table with filtered data
        else:
            # If search text is empty or no client data, populate with all data
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

        if 'nombre' in client_data:
            self.ui.NombreHolder.setText(client_data['nombre'])

        if 'telefono' in client_data:
            self.ui.TelHolder.setText(client_data['telefono'])
        
        if 'ip' in client_data:
            self.ui.IPHolder.setText(client_data['ip'])

        if 'calle' in client_data:
            self.ui.CalleHolder.setText(client_data['calle'])
        
        if 'numero' in client_data:
            self.ui.NumHolder.setText(client_data['numero'])

        if 'colonia' in client_data:
            self.ui.ColoniaHolder.setText(client_data["colonia"])

        if 'codigo_postal' in client_data:
            self.ui.CPHolder.setText(client_data["codigo_postal"])

        if 'plan_pago' in client_data:
            self.ui.PaqueteHolder.setText(client_data["plan_pago"])

    def populate_antena_dropdown(self):
        municipio_actual = self.ui.Select2.currentData()
        try:
            # Fetch comunidades (optionally with municipio filter)
            base_url = f"http://127.0.0.1:5000/api/comunidades/{municipio_actual}"
            response = self.session.get(base_url)
            if response.status_code == 200:
                comunidades = response.json()
                
                for comunidad in comunidades:
                    # Add each comunidad to dropdown; store ID as item data
                    self.ui.Select1.addItem(comunidad['nombre_comunidad'], comunidad['id'])
            else:
                print("Error fetching comunidades:", response.status_code)
        except Exception as e:
            print("Exception occurred while fetching comunidades:", e)


   

    def populate_municipio_dropdown(self):
        try:
            response = self.session.get("http://127.0.0.1:5000/api/municipios")
            if response.status_code == 200:
                municipios = response.json()
                for municipio in municipios:
                    # Add municipio name with municipio ID as data
                    self.ui.Select2.addItem(municipio['nombre'], municipio['id'])
            else:
                print("Failed to fetch municipios:", response.status_code)
        except Exception as e:
            print("Exception occurred while fetching municipios:", e)

    def guardar_cliente(self):
    # Collect updated client data from the input fields
        nombre = self.ui.NombreHolder.text()
        telefono = self.ui.TelHolder.text()
        ip = self.ui.IPHolder.text()
        calle = self.ui.CalleHolder.text()
        numero = self.ui.NumHolder.text()
        colonia = self.ui.ColoniaHolder.text()
        codigo_postal = self.ui.CPHolder.text()
        comunidad_id = self.ui.Select1.currentData()  
        municipio_id = self.ui.Select2.currentData()
        plan_pago = self.ui.PaqueteHolder.text()

        self.tipo_group = QButtonGroup(self)
        self.tipo_group.addButton(self.ui.GratuitoOption)
        self.tipo_group.addButton(self.ui.MensualOption)
        self.tipo_group.addButton(self.ui.AnualOption)

        self.status_group = QButtonGroup(self)
        self.status_group.addButton(self.ui.EnLineaOption)
        self.status_group.addButton(self.ui.BajaTemporalOption_2)

        if self.ui.GratuitoOption.isChecked():
            tipo = "Gratuito"
        elif self.ui.MensualOption.isChecked():
            tipo = "Mensual"
        elif self.ui.AnualOption.isChecked():
            tipo = "Anual"
        else:
            QMessageBox.warning(self, "Error", "Please select a user type.")
            return
        
        if self.ui.EnLineaOption.isChecked():
            status = "En Línea"
        elif self.ui.BajaTemporalOption_2.isChecked():
            status = "Baja Temporal"
        else:
            QMessageBox.warning(self, "Error", "Please select a user status.")
            return


        # Validate required fields
        if not nombre or not telefono or not ip or not calle or not numero or not colonia or not codigo_postal:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Validate telefono to ensure it only contains numbers
        if not telefono.isdigit():
            QMessageBox.warning(self, "Error", "El número de teléfono debe contener solo dígitos.")
            return

        # Prepare data for update (dictionary)
        updated_data = {
            "nombre": nombre,
            "telefono": telefono,
            "ip": ip,
            "calle": calle,
            "tipo": tipo,
            "numero": numero,
            "colonia": colonia,
            "status": status,
            "plan_pago" : plan_pago,
            "codigo_postal": codigo_postal,
            "comunidad_id": comunidad_id,
            "municipio_id": municipio_id,
        }

        # Assume the client has an ID stored in the selected client data
        selected_index = self.ui.listViewClients.currentIndex()
        if not selected_index.isValid():
            QMessageBox.warning(self, "Error", "Por favor, seleccione un cliente para modificar.")
            return

        # Get client ID from the selected item
        selected_client = self.client_model.itemFromIndex(selected_index).data()
        client_id = selected_client.get('id_cliente')
        
        try:
            # Send the update request with the data in the body as JSON
            response = self.session.put(f'http://127.0.0.1:5000/api/clientes/{client_id}', json=updated_data)
            
            #QMessageBox.warning(self, "Respuesta del servidor", response.text)

            if response.status_code == 200:
                QMessageBox.information(self, "Éxito", "El cliente ha sido actualizado correctamente.")
                self.load_client_data()  # Refresh client list to reflect changes
            else:
                QMessageBox.warning(self, "Error", f"No se pudo actualizar el cliente: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Error en la solicitud: {e}")


    def clearfields(self):
        self.ui.Select1.clear()
        self.ui.Select2.clear()