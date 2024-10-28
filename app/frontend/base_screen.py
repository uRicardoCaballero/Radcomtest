from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class BaseScreen(QWidget):
    def __init__(self, title):
        super().__init__()

        # Ocultar la barra de título predeterminada
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumSize(1275, 725)
        self.setStyleSheet("background-color: #53535e; border-radius: 15px;")  # Agregar bordes redondeados

        # Crear layout principal
        self.main_layout = QVBoxLayout()

        # Crear barra de título personalizada
        self.title_bar = QWidget()
        self.title_bar.setStyleSheet("background-color: #53535e; border-radius: 15px;")
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(0, 0, 0, 0)

        # Botones de minimizar, maximizar y cerrar
        self.minimize_button = QPushButton()
        self.minimize_button.setFixedSize(40, 30)
        self.minimize_button.setIcon(QIcon('app/frontend/assets/Min.png'))
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setStyleSheet("border: none;")

        self.maximize_button = QPushButton()
        self.maximize_button.setFixedSize(40, 30)
        self.maximize_button.setIcon(QIcon('assets/Max.png'))
        self.maximize_button.clicked.connect(self.toggle_maximize_restore)
        self.maximize_button.setStyleSheet("border: none;")

        self.close_button = QPushButton()
        self.close_button.setFixedSize(40, 30)
        self.close_button.setIcon(QIcon('app/frontend/assets/Close.png'))
        self.close_button.clicked.connect(self.close)
        self.close_button.setStyleSheet("border: none;")

        # Añadir los botones a la barra de título
        title_layout.addStretch(1)
        title_layout.addWidget(self.minimize_button)
        title_layout.addWidget(self.maximize_button)
        title_layout.addWidget(self.close_button)
        self.title_bar.setLayout(title_layout)

        # Añadir la barra de título personalizada al layout principal
        self.main_layout.addWidget(self.title_bar)

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

        # Variable para manejar el estado de maximizado
        self.is_maximized = False

    def toggle_maximize_restore(self):
        if self.is_maximized:
            self.showNormal()
            self.is_maximized = False
            self.maximize_button.setIcon(QIcon('app/frontend/assets/Max.png'))
        else:
            self.showMaximized()
            self.is_maximized = True
            self.maximize_button.setIcon(QIcon('app/frontend/assets/Restore.png'))

    # Permitir mover la ventana al arrastrar desde la barra de título
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'offset') and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
