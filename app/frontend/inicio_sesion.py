from PyQt5.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLabel, QFrame, QLineEdit  # Asegúrate de importar QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import requests
from app.frontend.main import *
from app.frontend.pantalla_adeudo_admin import PantallaAdeudoAdmin

class PantallaInicioSesion(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        # Crear un layout vertical para la pantalla
        main_layout = QVBoxLayout()  # Layout vertical principal

        # Crear un layout horizontal para centrar el logo
        logo_layout = QHBoxLayout()  # Layout para el logo
        
        # Crear un QLabel para el logo
        self.logo = QLabel(self)
        pixmap = QPixmap('app/frontend/assets/Logo_P.png')  # Asegúrate de la ruta

        # Establecer un tamaño máximo para el logo
        self.logo.setMinimumSize(300, 300)  # Tamaño máximo (ancho, alto)
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
                border: 2px solid #FFFFFF;  /* Marco blanco */
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
            }
            QLineEdit::placeholder {
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
            }
            QLineEdit::placeholder {
                color: gray;
            }
        """)

        self.login_button = QPushButton('INICIAR SESIÓN')
        self.login_button.setStyleSheet(""" 
            QPushButton {
                background-color: #FFFFFF;
                font-size: 16px;
                padding: 10px;
                font-family: 'Montserrat';
                width: 150px;  /* Ancho específico */
            }
            QPushButton:hover {
                background-color: #cccccc;
            }
        """)
        self.login_button.clicked.connect(self.iniciar_sesion)

        # Añadir los campos al layout del QFrame
        frame_layout.addWidget(self.user_input)
        frame_layout.addWidget(self.pass_input)
        frame_layout.addWidget(self.login_button)

        # Añadir el QFrame al layout principal
        main_layout.addWidget(self.frame, alignment=Qt.AlignCenter)  # Alinear verticalmente el cuadro

        # Establecer el layout principal
        self.setLayout(main_layout)

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
                    self.ui = PantallaAdeudoAdmin()
                    self.main_window.show()
                    self.close()
                else:
                    msg.setWindowTitle("wut")
                    msg.setText("QN VERGAS ERES??? hola mundo")
                    print(msg.exec())
                    print("Login failed!")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Please fill both fields.")
