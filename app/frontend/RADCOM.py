import sys
import requests
from flask import Blueprint, jsonify, request, send_file
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox , QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QSizePolicy, QFrame
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from app.frontend.pantalla_principal_admin import Ui_Form

# Pantalla principal que maneja todas las pantallas
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ocultar la barra de título predeterminada
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumSize(1275, 725)
        self.setStyleSheet("background-color: #53535e; border-radius: 15px;")  # Agregar bordes redondeados

        # Crear layout principal
        main_layout = QVBoxLayout()

        # Crear barra de título personalizada
        self.title_bar = QWidget()
        self.title_bar.setStyleSheet("background-color: #53535e; border-radius: 15px;")  # Color igual al fondo de la ventana
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(0, 0, 0, 0)

        # Botones de minimizar, maximizar y cerrar
        self.minimize_button = QPushButton()
        self.minimize_button.setFixedSize(40, 30)
        self.minimize_button.setIcon(QIcon('C:/Users/celin/Desktop/Personal Projects/RADCOM/Radcom/Min.png'))  # Ruta a la imagen de minimizar
        self.minimize_button.setIconSize(QSize(20, 20))  # Ajustar el tamaño del ícono
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setStyleSheet("border: none;")  # Eliminar el borde

        self.maximize_button = QPushButton()
        self.maximize_button.setFixedSize(40, 30)
        self.maximize_button.setIcon(QIcon('C:/Users/celin/Desktop/Personal Projects/RADCOM/Radcom/Max.png'))  # Ruta a la imagen de maximizar
        self.maximize_button.setIconSize(QSize(20, 20))
        self.maximize_button.clicked.connect(self.toggle_maximize_restore)
        self.maximize_button.setStyleSheet("border: none;")  # Eliminar el borde

        self.close_button = QPushButton()
        self.close_button.setFixedSize(40, 30)
        self.close_button.setIcon(QIcon('C:/Users/celin/Desktop/Personal Projects/RADCOM/Radcom/Close.png'))  # Ruta a la imagen de cerrar
        self.close_button.setIconSize(QSize(20, 20))
        self.close_button.clicked.connect(self.close)
        self.close_button.setStyleSheet("border: none;")  # Eliminar el borde

        # Añadir los botones a la barra de título
        title_layout.addStretch(1)  # Añadir espacio para alinear los botones a la derecha
        title_layout.addWidget(self.minimize_button)
        title_layout.addWidget(self.maximize_button)
        title_layout.addWidget(self.close_button)
        self.title_bar.setLayout(title_layout)

        # Añadir la barra de título personalizada al layout principal
        main_layout.addWidget(self.title_bar)

        # Crear el QStackedWidget para manejar todas las pantallas
        self.stacked_widget = QStackedWidget()

        # Crear las 15 pantallas
        self.pantallas = [Pantalla2(), Pantalla3(), Pantalla4(), Pantalla5(),
                          Pantalla6(), Pantalla7(), Pantalla8(), Pantalla9(), Pantalla10(),
                          Pantalla11(), Pantalla12(), Pantalla13(), Pantalla14(), Pantalla15()]

        # Añadir las pantallas al QStackedWidget
        for i, pantalla in enumerate(self.pantallas):
            self.stacked_widget.addWidget(pantalla)

        # Añadir el QStackedWidget al layout principal
        main_layout.addWidget(self.stacked_widget)

        # Contenedor principal
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Cambiar a la primera pantalla
        self.stacked_widget.setCurrentIndex(0)

        # Variable para manejar el estado de maximizado
        self.is_maximized = False

    def toggle_maximize_restore(self):
        if self.is_maximized:
            self.showNormal()
            self.is_maximized = False
            self.maximize_button.setIcon(QIcon('C:/Users/celin/Desktop/Personal Projects/RADCOM/Radcom/Max.png'))  # Icono de maximizar
        else:
            self.showMaximized()
            self.is_maximized = True
            self.maximize_button.setIcon(QIcon('C:/Users/celin/Desktop/Personal Projects/RADCOM/Radcom/Restore.png'))  # Icono de restaurar

    # Permitir mover la ventana al arrastrar desde la barra de título
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'offset') and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)

    def cambiar_pantalla(self, indice):
        self.stacked_widget.setCurrentIndex(indice)


# Clase base para las pantallas
class PantallaBase(QWidget):
    def __init__(self):
        super().__init__()

        # Crear un layout vertical para la pantalla
        main_layout = QVBoxLayout()  # Layout vertical principal

        # Crear un layout horizontal para centrar el logo
        logo_layout = QHBoxLayout()  # Layout para el logo
        
        # Crear un QLabel para el logo
        self.logo = QLabel(self)
        pixmap = QPixmap('C:/Users/celin/Desktop/Personal Projects/RADCOM/Radcom/Logo_P.png')

        # Establecer un tamaño máximo para el logo
        self.logo.setMaximumSize(300, 300)  # Tamaño máximo (ancho, alto)
        self.logo.setPixmap(pixmap)
        self.logo.setScaledContents(True)  # Permitir que el logo se escale automáticamente
        self.logo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Permitir que el label expanda

        # Añadir el logo al layout horizontal
        logo_layout.addWidget(self.logo, alignment=Qt.AlignCenter)  # Alinear horizontalmente el logo

        # Añadir el layout de logo al layout principal
        main_layout.addLayout(logo_layout)  # Agregar el layout del logo al layout principal

        # Crear un QFrame para el cuadro transparente
        self.frame = QFrame(self)
        self.frame.setFixedSize(600, 200)
        self.frame.setStyleSheet("""
            QFrame {
                background-color: none;  /* Fondo transparente */
                border: 2px solid white;  /* Marco blanco */
                border-radius: 15px;  /* Esquinas redondeadas */
                padding: 20px;  /* Espaciado interno */
            }
        """)

        # Crear un layout vertical para el QFrame
        frame_layout = QVBoxLayout(self.frame)

        # Campos de entrada
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("USUARIO")
        self.user_input.setStyleSheet("""
            QLineEdit {
                color: #53535e;
                background-color: none;
                padding: 5px;  /* Espacio interno */
                border: 1px solid lightgray;  /* Borde ligero */
                border-radius: 10px;  /* Esquinas redondeadas */
                width: 50px;  /* Ancho específico */
            }
            QLineEdit:: {
                color: gray;
            }
        """)

        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.pass_input.setPlaceholderText("CONTRASEÑA")
        self.pass_input.setStyleSheet("""
            QLineEdit {
                color: #53535e;
                background-color: none;
                padding: 5px;  /* Espacio interno */
                border: 1px solid lightgray;  /* Borde ligero */
                border-radius: 10px;  /* Esquinas redondeadas */
                width: 100px;  /* Ancho específico */
            }
            QLineEdit::placeholder {
                color: gray;
            }
        """)

        self.login_button = QPushButton('INICIAR SESIÓN')
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                font-size: 16px;
                padding: 10px;
                font-family: 'Montserrat';
                width: 150px;  /* Ancho específico */
            }
            QPushButton:hover {
                background-color: #cccccc;
            }
        """)

        # Añadir los widgets al layout del QFrame
        frame_layout.addWidget(self.user_input)
        frame_layout.addWidget(self.pass_input)
        frame_layout.addWidget(self.login_button)
        frame_layout.setAlignment(Qt.AlignCenter)  # Centrar los widgets



        # Añadir el QFrame al layout principal
        main_layout.addWidget(self.frame, alignment=Qt.AlignCenter)  # Alinear el marco en el centro


        self.create_user_button = QPushButton('CREAR USUARIO')
        self.create_user_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: 1px solid white;
                font-size: 12px;
                padding: 10px;
                font-family: 'Montserrat';
                color: white;
                width: 150px;  /* Ancho específico */
            }
            QPushButton:hover {
                border-color: gray;
            }
        """)
        main_layout.addWidget(self.create_user_button, alignment=Qt.AlignCenter)  # Alinear al centro
        self.setLayout(main_layout)
        self.login_button.clicked.connect(self.iniciar_sesion)
#Movimiento de Pantallas
    
    def crear_usuario(self):
        self.main_window.cambiar_pantalla(0)
        
    def iniciar_sesion(self):
        msg = QMessageBox()
        username = self.user_input.text()
        password = self.pass_input.text()

        if username and password:
            data = {
                'username': username,
                'password': password
            }
            try:
                print("usuario: "+username+ " contraseña:"+password)
                response = requests.post('http://localhost:5000/api/login', json=data)
                if response.status_code == 200:
                    #change to another window
                    print("Login successful!")
                    self.open_main_window() # Go to next screen
                else:
                    msg.setWindowTitle("wut")
                    msg.setText("QN VERGAS ERES??? hola mundo")
                    print(msg.exec())
                    print("Login failed!")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Please fill both fields.")

    def open_main_window(self):
        self.main_window = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        self.close()


# Definición de cada pantalla específica
# class Pantalla1(PantallaBase):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Pantalla 1')
#     def switch_to_new_window(self):
#         self.new_window_ui = QWidget()
#         self.new_window_ui = Ui_Form()
#         self.new_window_ui.setupUi(self.new_window_ui)
#         self.open_new_window.show()
#         self.hide()


class Pantalla2(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 2')


class Pantalla3(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 3')


class Pantalla4(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 4')


class Pantalla5(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 5')


class Pantalla6(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 6')


class Pantalla7(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 7')


class Pantalla8(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 8')


class Pantalla9(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 9')


class Pantalla10(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 10')


class Pantalla11(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 11')


class Pantalla12(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 12')


class Pantalla13(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 13')


class Pantalla14(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 14')


class Pantalla15(PantallaBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pantalla 15')

