from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from app.frontend.pantalla_adeudo_cobrador_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
import requests

class PantallaAdeudoCobrador(QWidget):
    def __init__(self, change_screen_func, logout, session, parent=None):
        super().__init__(parent)

        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI

        self.change_screen = change_screen_func
        self.logout = logout

        # Aquí puedes agregar más funcionalidades o conectores si es necesario
        self.setup_connections()
        self.session = session

        # Aquí puedes agregar más funcionalidades o conectores si es necesario
        self.client_model = QStandardItemModel(self.ui.listViewClients)
        self.ui.listViewClients.setModel(self.client_model)

        self.client_data = []  # This will store the client data

    def setup_connections(self):
        # Connect each QLabel's mousePressEvent to the same slot function
        self.ui.menuOption1.mousePressEvent = lambda event: self.label_clicked(event, "menuOption1")
        self.ui.menuOption2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption2")
        self.ui.menuOption3.mousePressEvent = lambda event: self.label_clicked(event, "menuOption3")
        self.ui.menuOption7_2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption7_2")


        self.ui.GuardarButton.clicked.connect(self.add_service)

            # Connect the live search input to the search function
        self.ui.lineEdit.textChanged.connect(self.search_clients)

        # Connect client selection event
        self.ui.listViewClients.clicked.connect(self.client_selected)


    def label_clicked(self, event, label_name):
        # Determine the screen based on the label clicked
        if label_name == "menuOption1":
            self.change_screen(3)
        elif label_name == "menuOption2":
            self.change_screen(6)
        elif label_name == "menuOption3":
            self.change_screen(9)
        elif label_name == "menuOption7_2":
            self.logout()


    def search_clients(self):
        search_text = self.ui.lineEdit.text().lower()  # Get the search text from QLineEdit
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
                self.client_data = clients
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




        
    def add_service(self):
        if not self.selected_client_data:
            QMessageBox.warning(self, "Warning", "Porfavor, Selecciona un cliente")
            return

        cliente_id = self.selected_client_data.get("id_cliente")
        tipo_servicio = self.ui.ServicioHolder.text()
        materiales = self.ui.MaterialHolder.text()
        tecnico = self.ui.TecnicoHolder.text()
        precio_text  = self.ui.MontoHolder.text().strip()

        if not precio_text.replace('.', '', 1).isdigit():
            print("Invalid price input. Please enter a valid number.")
            return  # Exit or show an error message to the user

        # Convert the validated input to a float
        precio = float(precio_text)

        # Prepare service data
        data = {
            "cliente_id": cliente_id,
            "tipo_servicio": tipo_servicio,
            "materiales": materiales,
            "tecnico": tecnico,
            "precio": float(precio)
        }

        try:
            response = self.session.post("http://127.0.0.1:5000/api/service", json=data)
            if response.status_code == 201:
                QMessageBox.information(self, "Success", "Servicio agregado correctamente.")
                # Optionally reload client data here if needed
            else:
                error_message = response.json().get("error", "Fallo al agregar servicio, intenta mas tarde.")
                QMessageBox.warning(self, "Error", error_message)
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Could not connect to server: {str(e)}")

