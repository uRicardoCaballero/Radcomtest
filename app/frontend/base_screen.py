from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class BaseScreen(QWidget):
    def __init__(self, title):
        super().__init__()

        # Restablece la barra de título predeterminada
        self.setWindowFlag(Qt.FramelessWindowHint, False)

        # Configuración de la pantalla
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumSize(1275, 725)
        self.setStyleSheet("background-color: #53535e;")  # Fondo sin bordes redondeados

        # Crear layout principal
        self.main_layout = QVBoxLayout()

        # Crear un contenedor para el contenido (pantallas)
        self.content_area = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_area.setLayout(self.content_layout)

        # Añadir el contenedor de contenido al layout principal
        self.main_layout.addWidget(self.content_area)

        # Establecer el layout principal
        self.setLayout(self.main_layout)

        # Título de la pantalla
        self.setWindowTitle(title)