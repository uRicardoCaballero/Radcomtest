# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pantalla_adeudo_facturador.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(1275, 725)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1275, 725))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        Form.setAutoFillBackground(False)
        self.frame_white = QtWidgets.QFrame(Form)
        self.frame_white.setGeometry(QtCore.QRect(340, 0, 961, 781))
        self.frame_white.setStyleSheet("QFrame {\n"
"    border: none;       /* Color y grosor del borde */\n"
"    border-radius: 55px;          /* Radio de las esquinas */\n"
"    background-color: #f0f0f0;    /* Color de fondo */\n"
"    margin: 0px;                  /* Margen externo a 0 */\n"
"    padding: 0px;                 /* Espaciado interno a 0 */\n"
"}\n"
"\n"
"")
        self.frame_white.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white.setObjectName("frame_white")
        self.frame_white_grey = QtWidgets.QFrame(self.frame_white)
        self.frame_white_grey.setGeometry(QtCore.QRect(300, 0, 961, 781))
        self.frame_white_grey.setStyleSheet("QFrame {\n"
"    border: none;       /* Color y grosor del borde */\n"
"    border-radius: 55px;          /* Radio de las esquinas */\n"
"    background-color: #37373d;    /* Color de fondo */\n"
"    margin: 0px;                  /* Margen externo a 0 */\n"
"    padding: 0px;                 /* Espaciado interno a 0 */\n"
"}\n"
"\n"
"")
        self.frame_white_grey.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white_grey.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white_grey.setObjectName("frame_white_grey")
        self.GuardarButton = QtWidgets.QPushButton(self.frame_white_grey)
        self.GuardarButton.setGeometry(QtCore.QRect(440, 660, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.GuardarButton.setFont(font)
        self.GuardarButton.setStyleSheet("QPushButton{\n"
"        background: #FFFFFF; \n"
"         border-radius: 15px; \n"
"}")
        self.GuardarButton.setObjectName("GuardarButton")
        self.NombreHolder = QtWidgets.QLineEdit(self.frame_white_grey)
        self.NombreHolder.setGeometry(QtCore.QRect(70, 50, 411, 51))
        font = QtGui.QFont()
        font.setFamily("\"Montserratl\"")
        font.setPointSize(1)
        self.NombreHolder.setFont(font)
        self.NombreHolder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NombreHolder.setStyleSheet("QLineEdit{\n"
"        color: #FFFFFF;\n"
"        Font-family: \\\"Montserratl\\\";\n"
"        font-size: 36px;\n"
"        border: none;\n"
"        background: transparent; \n"
"}")
        self.NombreHolder.setInputMask("")
        self.NombreHolder.setText("")
        self.NombreHolder.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.NombreHolder.setReadOnly(True)
        self.NombreHolder.setPlaceholderText("")
        self.NombreHolder.setObjectName("NombreHolder")
        self.ServicioHolder = QtWidgets.QLineEdit(self.frame_white_grey)
        self.ServicioHolder.setGeometry(QtCore.QRect(60, 260, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        self.ServicioHolder.setFont(font)
        self.ServicioHolder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ServicioHolder.setStyleSheet("QLineEdit{\n"
"    border: 1px solid  #37373d;\n"
"        background: #FFFFFF; \n"
"         border-radius: 20px; \n"
"}")
        self.ServicioHolder.setInputMask("")
        self.ServicioHolder.setText("")
        self.ServicioHolder.setAlignment(QtCore.Qt.AlignCenter)
        self.ServicioHolder.setPlaceholderText("")
        self.ServicioHolder.setObjectName("ServicioHolder")
        self.MontoText_4 = QtWidgets.QTextBrowser(self.frame_white_grey)
        self.MontoText_4.setGeometry(QtCore.QRect(520, 530, 61, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MontoText_4.sizePolicy().hasHeightForWidth())
        self.MontoText_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(5)
        self.MontoText_4.setFont(font)
        self.MontoText_4.setToolTipDuration(-1)
        self.MontoText_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.MontoText_4.setAutoFillBackground(False)
        self.MontoText_4.setStyleSheet("QTextBrowser {\n"
"    background: transparent;  /* Quitar el fondo */\n"
"    color:#FFFFFF;\n"
"    border: none;             /* Quitar el borde */\n"
"    margin: 0;                /* Eliminar márgenes */\n"
"}")
        self.MontoText_4.setObjectName("MontoText_4")
        self.MontoHolder = QtWidgets.QLineEdit(self.frame_white_grey)
        self.MontoHolder.setGeometry(QtCore.QRect(350, 560, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        self.MontoHolder.setFont(font)
        self.MontoHolder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MontoHolder.setStyleSheet("QLineEdit{\n"
"    border: 1px solid  #37373d;\n"
"        background: #FFFFFF; \n"
"         border-radius: 20px; \n"
"}")
        self.MontoHolder.setInputMask("")
        self.MontoHolder.setText("")
        self.MontoHolder.setAlignment(QtCore.Qt.AlignCenter)
        self.MontoHolder.setPlaceholderText("")
        self.MontoHolder.setObjectName("MontoHolder")
        self.Folio = QtWidgets.QTextBrowser(self.frame_white_grey)
        self.Folio.setGeometry(QtCore.QRect(60, 310, 201, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Folio.sizePolicy().hasHeightForWidth())
        self.Folio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(5)
        self.Folio.setFont(font)
        self.Folio.setToolTipDuration(-1)
        self.Folio.setAutoFillBackground(False)
        self.Folio.setStyleSheet("QTextBrowser {\n"
"    background: transparent;  /* Quitar el fondo */\n"
"    color:#FFFFFF;\n"
"    border: none;             /* Quitar el borde */\n"
"    margin: 0;                /* Eliminar márgenes */\n"
"}")
        self.Folio.setObjectName("Folio")
        self.MaterialHolder = QtWidgets.QLineEdit(self.frame_white_grey)
        self.MaterialHolder.setGeometry(QtCore.QRect(60, 340, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        self.MaterialHolder.setFont(font)
        self.MaterialHolder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MaterialHolder.setStyleSheet("QLineEdit{\n"
"    border: 1px solid  #37373d;\n"
"        background: #FFFFFF; \n"
"         border-radius: 20px; \n"
"}")
        self.MaterialHolder.setInputMask("")
        self.MaterialHolder.setText("")
        self.MaterialHolder.setAlignment(QtCore.Qt.AlignCenter)
        self.MaterialHolder.setPlaceholderText("")
        self.MaterialHolder.setObjectName("MaterialHolder")
        self.InfoPago = QtWidgets.QTextBrowser(self.frame_white_grey)
        self.InfoPago.setGeometry(QtCore.QRect(60, 190, 371, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InfoPago.sizePolicy().hasHeightForWidth())
        self.InfoPago.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.InfoPago.setFont(font)
        self.InfoPago.setToolTipDuration(-1)
        self.InfoPago.setAutoFillBackground(False)
        self.InfoPago.setStyleSheet("QTextBrowser {\n"
"    background: transparent;  /* Quitar el fondo */\n"
"    color:#FFFFFF;\n"
"    border: none;             /* Quitar el borde */\n"
"    margin: 0;                /* Eliminar márgenes */\n"
"}")
        self.InfoPago.setObjectName("InfoPago")
        self.TecnicoHolder = QtWidgets.QLineEdit(self.frame_white_grey)
        self.TecnicoHolder.setGeometry(QtCore.QRect(60, 470, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        self.TecnicoHolder.setFont(font)
        self.TecnicoHolder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TecnicoHolder.setStyleSheet("QLineEdit{\n"
"    border: 1px solid  #37373d;\n"
"        background: #FFFFFF; \n"
"         border-radius: 20px; \n"
"}")
        self.TecnicoHolder.setInputMask("")
        self.TecnicoHolder.setText("")
        self.TecnicoHolder.setAlignment(QtCore.Qt.AlignCenter)
        self.TecnicoHolder.setPlaceholderText("")
        self.TecnicoHolder.setObjectName("TecnicoHolder")
        self.MontoText_3 = QtWidgets.QTextBrowser(self.frame_white_grey)
        self.MontoText_3.setGeometry(QtCore.QRect(60, 440, 201, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MontoText_3.sizePolicy().hasHeightForWidth())
        self.MontoText_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(5)
        self.MontoText_3.setFont(font)
        self.MontoText_3.setToolTipDuration(-1)
        self.MontoText_3.setAutoFillBackground(False)
        self.MontoText_3.setStyleSheet("QTextBrowser {\n"
"    background: transparent;  /* Quitar el fondo */\n"
"    color:#FFFFFF;\n"
"    border: none;             /* Quitar el borde */\n"
"    margin: 0;                /* Eliminar márgenes */\n"
"}")
        self.MontoText_3.setObjectName("MontoText_3")
        self.NumCuenta = QtWidgets.QTextBrowser(self.frame_white_grey)
        self.NumCuenta.setGeometry(QtCore.QRect(60, 230, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumCuenta.sizePolicy().hasHeightForWidth())
        self.NumCuenta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(5)
        self.NumCuenta.setFont(font)
        self.NumCuenta.setToolTipDuration(-1)
        self.NumCuenta.setAutoFillBackground(False)
        self.NumCuenta.setStyleSheet("QTextBrowser {\n"
"    background: transparent;  /* Quitar el fondo */\n"
"    color:#FFFFFF;\n"
"    border: none;             /* Quitar el borde */\n"
"    margin: 0;                /* Eliminar márgenes */\n"
"}")
        self.NumCuenta.setObjectName("NumCuenta")
        self.Clientes = QtWidgets.QTextBrowser(self.frame_white)
        self.Clientes.setGeometry(QtCore.QRect(90, 70, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Clientes.sizePolicy().hasHeightForWidth())
        self.Clientes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.Clientes.setFont(font)
        self.Clientes.setToolTipDuration(-1)
        self.Clientes.setAutoFillBackground(False)
        self.Clientes.setStyleSheet("QTextBrowser {\n"
"    background: transparent;  /* Quitar el fondo */\n"
"    color:#37373d;\n"
"    border: none;             /* Quitar el borde */\n"
"    margin: 0;                /* Eliminar márgenes */\n"
"}")
        self.Clientes.setObjectName("Clientes")
        self.listViewClients = QtWidgets.QListView(self.frame_white)
        self.listViewClients.setGeometry(QtCore.QRect(40, 141, 221, 411))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.listViewClients.setFont(font)
        self.listViewClients.setObjectName("listViewClients")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_white)
        self.lineEdit.setGeometry(QtCore.QRect(40, 660, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border: 1px solid  #37373d;\n"
"        background: #FFFFFF; \n"
"         border-radius: 20px; \n"
"}")
        self.lineEdit.setInputMask("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.Select1 = QtWidgets.QComboBox(self.frame_white)
        self.Select1.setGeometry(QtCore.QRect(40, 600, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        self.Select1.setFont(font)
        self.Select1.setStyleSheet("QComboBox{\n"
"     background: #FFFFFF;\n"
"    color: #37373d;\n"
"    border-radius: 5px;\n"
"    font-family: Montserrat; /* Type of font */\n"
"    font-size: 16px;                /* Size of the text */\n"
"}")
        self.Select1.setObjectName("Select1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 0, 261, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("app/frontend/assets/LOGO_M.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 160, 271, 461))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: #37373d;  /* Color de fondo semitransparente */\n"
"    border-radius: 30px;                         /* Bordes redondeados */\n"
"   \n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.menuOption1 = QtWidgets.QTextBrowser(self.frame)
        self.menuOption1.setGeometry(QtCore.QRect(20, 20, 101, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.menuOption1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menuOption1.setFont(font)
        self.menuOption1.setObjectName("menuOption1")
        self.menuOption2 = QtWidgets.QTextBrowser(self.frame)
        self.menuOption2.setGeometry(QtCore.QRect(20, 80, 121, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.menuOption2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.menuOption2.setFont(font)
        self.menuOption2.setObjectName("menuOption2")
        self.menuOption3 = QtWidgets.QTextBrowser(self.frame)
        self.menuOption3.setGeometry(QtCore.QRect(20, 140, 161, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.menuOption3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.menuOption3.setFont(font)
        self.menuOption3.setObjectName("menuOption3")
        self.menuOption4 = QtWidgets.QTextBrowser(self.frame)
        self.menuOption4.setGeometry(QtCore.QRect(20, 200, 161, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.menuOption4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.menuOption4.setFont(font)
        self.menuOption4.setObjectName("menuOption4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 70, 230, 2))
        self.frame_2.setStyleSheet("QFrame {\n"
"    border: none;       /* Color y grosor del borde */\n"
"    border-radius: 55px;          /* Radio de las esquinas */\n"
"    background-color: #f0f0f0;    /* Color de fondo */\n"
"    margin: 0px;                  /* Margen externo a 0 */\n"
"    padding: 0px;                 /* Espaciado interno a 0 */\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(20, 130, 230, 2))
        self.frame_3.setStyleSheet("QFrame {\n"
"    border: none;       /* Color y grosor del borde */\n"
"    border-radius: 55px;          /* Radio de las esquinas */\n"
"    background-color: #f0f0f0;    /* Color de fondo */\n"
"    margin: 0px;                  /* Margen externo a 0 */\n"
"    padding: 0px;                 /* Espaciado interno a 0 */\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(20, 190, 230, 2))
        self.frame_4.setStyleSheet("QFrame {\n"
"    border: none;       /* Color y grosor del borde */\n"
"    border-radius: 55px;          /* Radio de las esquinas */\n"
"    background-color: #f0f0f0;    /* Color de fondo */\n"
"    margin: 0px;                  /* Margen externo a 0 */\n"
"    padding: 0px;                 /* Espaciado interno a 0 */\n"
"}\n"
"\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.menuOption7_2 = QtWidgets.QTextBrowser(Form)
        self.menuOption7_2.setGeometry(QtCore.QRect(30, 660, 271, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.menuOption7_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setKerning(True)
        self.menuOption7_2.setFont(font)
        self.menuOption7_2.setStyleSheet("QTextBrowser {\n"
"    background: transparent;  /* Quitar el fondo */\n"
"    border: none;             /* Quitar el borde */\n"
"}")
        self.menuOption7_2.setPlaceholderText("")
        self.menuOption7_2.setObjectName("menuOption7_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.GuardarButton.setText(_translate("Form", "AÑADIR"))
        self.MontoText_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Monto</span></p></body></html>"))
        self.Folio.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Material</span></p></body></html>"))
        self.InfoPago.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:600;\">SERVICIO:</span></p></body></html>"))
        self.MontoText_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Nombre del Tecnico</span></p></body></html>"))
        self.NumCuenta.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Servicio</span></p></body></html>"))
        self.Clientes.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:600;\">Clientes</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Buscar"))
        self.menuOption1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Inicio</span></p></body></html>"))
        self.menuOption2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Cobros</span></p></body></html>"))
        self.menuOption3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Adeudos</span></p></body></html>"))
        self.menuOption4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Facturas</span></p></body></html>"))
        self.menuOption7_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Cerrar Sesion</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
