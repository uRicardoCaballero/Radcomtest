from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from app.frontend.pantalla_adeudo_admin_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys
import requests

class PantallaAdeudoAdmin(QWidget):
    def __init__(self, change_screen_func, logout, session, parent=None):
        super().__init__(parent)

        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI

        self.change_screen = change_screen_func
        self.logout = logout
        self.setup_connections()
        self.session = session

        # Aquí puedes agregar más funcionalidades o conectores si es necesario
        self.client_model = QStandardItemModel(self.ui.listViewClients)
        self.ui.listViewClients.setModel(self.client_model)

    def setup_connections(self):
        # Connect each QLabel's mousePressEvent to the same slot function
        self.ui.menuOption1.mousePressEvent = lambda event: self.label_clicked(event, "menuOption1")
        self.ui.menuOption2.mousePressEvent = lambda event: self.label_clicked(event, "menuOption2")
        self.ui.menuOption3.mousePressEvent = lambda event: self.label_clicked(event, "menuOption3")
        self.ui.menuOption4.mousePressEvent = lambda event: self.label_clicked(event, "menuOption4")
        self.ui.menuOption5.mousePressEvent = lambda event: self.label_clicked(event, "menuOption5")
        self.ui.menuOption6.mousePressEvent = lambda event: self.label_clicked(event, "menuOption6")
        self.ui.menuOption7.mousePressEvent = lambda event: self.label_clicked(event, "menuOption7")
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
        elif label_name == "menuOption7_2":
            self.logout()


    def load_client_data(self):
        # Fetch client data from the API when this screen is displayed
        try:
            response = self.session.get("http://127.0.0.1:5000/api/clientes")
            if response.status_code == 200:
                clients = response.json()
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

    def filter_clients(self, text):
        for row in range(self.client_model.rowCount()):
            item = self.client_model.item(row)
            item.setHidden(text.lower() not in item.text().lower())

    def client_selected(self, index):
        client_data = self.client_model.itemFromIndex(index).data()
        print("Selected client data:", client_data)


