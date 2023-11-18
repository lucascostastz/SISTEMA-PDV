# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(750, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../img/user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_2.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Lb_Img = QtWidgets.QLabel(parent=self.frame_2)
        self.Lb_Img.setMinimumSize(QtCore.QSize(350, 0))
        self.Lb_Img.setMaximumSize(QtCore.QSize(420, 16777215))
        self.Lb_Img.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-right-radius: 35px;\n"
"border-bottom-right-radius: 35px;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.Lb_Img.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Lb_Img.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.Lb_Img.setText("")
        self.Lb_Img.setPixmap(QtGui.QPixmap("../../../../../Downloads/Design sem nome.png"))
        self.Lb_Img.setWordWrap(False)
        self.Lb_Img.setObjectName("Lb_Img")
        self.gridLayout.addWidget(self.Lb_Img, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(400, 0))
        self.frame.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.Tx_Usuario = QtWidgets.QLineEdit(parent=self.frame)
        self.Tx_Usuario.setGeometry(QtCore.QRect(30, 150, 271, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tx_Usuario.sizePolicy().hasHeightForWidth())
        self.Tx_Usuario.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Tx_Usuario.setFont(font)
        self.Tx_Usuario.setStyleSheet("QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"border:0px solid;\n"
"font: 75 12pt \"Arial Narrow\";\n"
"border-bottom:2px solid #1E90FF;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-bottom:2px solid rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"     font: 75 12pt \"Arial Narrow\";\n"
"     border-bottom:2px solid ;\n"
"    color: rgb(255, 0, 0);\n"
"        color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.Tx_Usuario.setText("")
        self.Tx_Usuario.setFrame(True)
        self.Tx_Usuario.setReadOnly(False)
        self.Tx_Usuario.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.Tx_Usuario.setClearButtonEnabled(True)
        self.Tx_Usuario.setObjectName("Tx_Usuario")
        self.Tx_Senha = QtWidgets.QLineEdit(parent=self.frame)
        self.Tx_Senha.setGeometry(QtCore.QRect(30, 210, 271, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tx_Senha.sizePolicy().hasHeightForWidth())
        self.Tx_Senha.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Tx_Senha.setFont(font)
        self.Tx_Senha.setStyleSheet("QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"border:0px solid;\n"
"font: 75 12pt \"Arial Narrow\";\n"
"border-bottom:2px solid #1E90FF;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-bottom:2px solid rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"     font: 75 12pt \"Arial Narrow\";\n"
"     border-bottom:2px solid ;\n"
"    color: rgb(255, 0, 0);\n"
"        color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.Tx_Senha.setText("")
        self.Tx_Senha.setFrame(False)
        self.Tx_Senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.Tx_Senha.setReadOnly(False)
        self.Tx_Senha.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.Tx_Senha.setClearButtonEnabled(True)
        self.Tx_Senha.setObjectName("Tx_Senha")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(0, 40, 201, 41))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")
        self.label.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 201, 51))
        self.label_2.setStyleSheet("border:none;\n"
"font: 75 12pt \"Arial Narrow\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.Bt_check = QtWidgets.QCheckBox(parent=self.frame)
        self.Bt_check.setGeometry(QtCore.QRect(30, 270, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Bt_check.setFont(font)
        self.Bt_check.setStyleSheet("QCheckBox{border:none;}\n"
"QCheckBox::indicator {\n"
"    border: 2px solid #1E90FF;;\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 5px;    \n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid rgb(255, 0, 0);\n"
"\n"
"}\n"
"")
        self.Bt_check.setObjectName("Bt_check")
        self.my_progressBar = QtWidgets.QProgressBar(parent=self.frame)
        self.my_progressBar.setGeometry(QtCore.QRect(30, 390, 271, 31))
        self.my_progressBar.setStyleSheet("QProgressBar{\n"
"background-color: #00557f;\n"
"border-radius: 5px;\n"
"text-align: center;\n"
"color: rgb(255, 0, 0)\n"
"\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 136, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.my_progressBar.setProperty("value", 0)
        self.my_progressBar.setObjectName("my_progressBar")
        self.Lb_Info_banco = QtWidgets.QLabel(parent=self.frame)
        self.Lb_Info_banco.setGeometry(QtCore.QRect(30, 470, 271, 21))
        self.Lb_Info_banco.setStyleSheet("border: none;\n"
"font: 75 12pt \"Sitka Subheading\";\n"
"color: rgb(255, 0, 0);\n"
"\n"
"\n"
"")
        self.Lb_Info_banco.setText("")
        self.Lb_Info_banco.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lb_Info_banco.setObjectName("Lb_Info_banco")
        self.Bt_Login = QtWidgets.QPushButton(parent=self.frame)
        self.Bt_Login.setGeometry(QtCore.QRect(30, 310, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_Login.sizePolicy().hasHeightForWidth())
        self.Bt_Login.setSizePolicy(sizePolicy)
        self.Bt_Login.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.Bt_Login.setStyleSheet("QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#4169E1;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/login_button.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Bt_Login.setIcon(icon1)
        self.Bt_Login.setIconSize(QtCore.QSize(16, 16))
        self.Bt_Login.setObjectName("Bt_Login")
        self.Bt_Sair = QtWidgets.QPushButton(parent=self.frame)
        self.Bt_Sair.setGeometry(QtCore.QRect(190, 310, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_Sair.sizePolicy().hasHeightForWidth())
        self.Bt_Sair.setSizePolicy(sizePolicy)
        self.Bt_Sair.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.Bt_Sair.setStyleSheet("QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#4169E1;\n"
"}")
        self.Bt_Sair.setIcon(icon1)
        self.Bt_Sair.setIconSize(QtCore.QSize(16, 16))
        self.Bt_Sair.setObjectName("Bt_Sair")
        self.Lb_Info = QtWidgets.QLabel(parent=self.frame)
        self.Lb_Info.setGeometry(QtCore.QRect(30, 440, 271, 20))
        self.Lb_Info.setStyleSheet("border: none;\n"
"color: rgb(255, 255, 0);\n"
"font: 75 12pt \"Sitka Subheading\";\n"
"\n"
"")
        self.Lb_Info.setText("")
        self.Lb_Info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lb_Info.setObjectName("Lb_Info")
        self.Lb_Info2 = QtWidgets.QLabel(parent=self.frame)
        self.Lb_Info2.setGeometry(QtCore.QRect(30, 350, 271, 21))
        self.Lb_Info2.setStyleSheet("border: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt;\n"
"\n"
"")
        self.Lb_Info2.setText("")
        self.Lb_Info2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lb_Info2.setObjectName("Lb_Info2")
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LC INFORMÁTICA"))
        self.Tx_Usuario.setPlaceholderText(_translate("MainWindow", "Usuario"))
        self.Tx_Senha.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.label.setText(_translate("MainWindow", "Seja bem vindo"))
        self.label_2.setText(_translate("MainWindow", "Faça login na sua conta"))
        self.Bt_check.setToolTip(_translate("MainWindow", "Clique aqui para visualizar e ocultar a senha"))
        self.Bt_check.setText(_translate("MainWindow", "Visualizar"))
        self.Bt_Login.setText(_translate("MainWindow", "ENTRAR"))
        self.Bt_Sair.setText(_translate("MainWindow", "SAIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
