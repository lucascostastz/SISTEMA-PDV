# Form implementation generated from reading ui file 'Form_Finaliza_Venda_Nota.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Fecha_Venda(object):
    def setupUi(self, Fecha_Venda):
        Fecha_Venda.setObjectName("Fecha_Venda")
        Fecha_Venda.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Fecha_Venda.resize(500, 576)
        Fecha_Venda.setMinimumSize(QtCore.QSize(500, 576))
        Fecha_Venda.setMaximumSize(QtCore.QSize(500, 576))
        Fecha_Venda.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=Fecha_Venda)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(55)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Lb_Comanda_Mesa = QtWidgets.QLabel(parent=self.frame_9)
        self.Lb_Comanda_Mesa.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.Lb_Comanda_Mesa.setObjectName("Lb_Comanda_Mesa")
        self.gridLayout_3.addWidget(self.Lb_Comanda_Mesa, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.frame = QtWidgets.QFrame(parent=self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_10 = QtWidgets.QFrame(parent=self.frame)
        self.frame_10.setStyleSheet("")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_2.setMaximumSize(QtCore.QSize(95, 16777215))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.Lb_Nome_Perador = QtWidgets.QLabel(parent=self.frame_10)
        self.Lb_Nome_Perador.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.Lb_Nome_Perador.setObjectName("Lb_Nome_Perador")
        self.horizontalLayout_3.addWidget(self.Lb_Nome_Perador)
        self.gridLayout.addWidget(self.frame_10, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_5.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label = QtWidgets.QLabel(parent=self.frame_5)
        self.label.setGeometry(QtCore.QRect(10, 0, 301, 41))
        self.label.setStyleSheet("font: 25pt \"Rockwell\";\n"
"color: rgb(0, 170, 255);")
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_11.setGeometry(QtCore.QRect(70, 50, 41, 51))
        self.label_11.setStyleSheet("font: 25pt \"Rockwell\";")
        self.label_11.setObjectName("label_11")
        self.Lb_TotalPagar = QtWidgets.QLabel(parent=self.frame_5)
        self.Lb_TotalPagar.setGeometry(QtCore.QRect(130, 50, 331, 51))
        self.Lb_TotalPagar.setMinimumSize(QtCore.QSize(150, 0))
        self.Lb_TotalPagar.setStyleSheet("background: #CFCFCF;\n"
"border-radius: 2px;\n"
"font: 25px \"Arial\" ;\n"
"\n"
"")
        self.Lb_TotalPagar.setObjectName("Lb_TotalPagar")
        self.gridLayout_4.addWidget(self.frame_5, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_5.setGeometry(QtCore.QRect(10, -2, 331, 41))
        self.label_5.setStyleSheet("font: 75 25pt \"Rockwell\";\n"
"color: rgb(0, 170, 255);")
        self.label_5.setObjectName("label_5")
        self.Cb_FormaPagamento = QtWidgets.QComboBox(parent=self.frame_7)
        self.Cb_FormaPagamento.setGeometry(QtCore.QRect(130, 50, 331, 51))
        self.Cb_FormaPagamento.setMinimumSize(QtCore.QSize(0, 25))
        self.Cb_FormaPagamento.setStyleSheet("QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"font: 25px \"Arial\" ;\n"
"\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"color: rgb(0, 0, 0);\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"font: 25px \"Arial\" ;\n"
"}")
        self.Cb_FormaPagamento.setObjectName("Cb_FormaPagamento")
        self.Cb_FormaPagamento.addItem("")
        self.Lb_Nome_cliente = QtWidgets.QLabel(parent=self.frame_7)
        self.Lb_Nome_cliente.setGeometry(QtCore.QRect(120, 140, 361, 61))
        self.Lb_Nome_cliente.setStyleSheet("font: 25px \"Arial\" ;\n"
"color: rgb(0, 170, 127);")
        self.Lb_Nome_cliente.setText("")
        self.Lb_Nome_cliente.setObjectName("Lb_Nome_cliente")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(0, 140, 121, 61))
        self.label_4.setStyleSheet("font: 25px \"Arial\" ;")
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.frame_7, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_13 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Bt_Cancelar_Venda = QtWidgets.QPushButton(parent=self.frame_13)
        self.Bt_Cancelar_Venda.setMinimumSize(QtCore.QSize(0, 35))
        self.Bt_Cancelar_Venda.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 45px;\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.Bt_Cancelar_Venda.setObjectName("Bt_Cancelar_Venda")
        self.horizontalLayout_6.addWidget(self.Bt_Cancelar_Venda)
        self.Bt_Confirmar_Venda = QtWidgets.QPushButton(parent=self.frame_13)
        self.Bt_Confirmar_Venda.setMinimumSize(QtCore.QSize(0, 35))
        self.Bt_Confirmar_Venda.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 45px;\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.Bt_Confirmar_Venda.setObjectName("Bt_Confirmar_Venda")
        self.horizontalLayout_6.addWidget(self.Bt_Confirmar_Venda)
        self.gridLayout_2.addWidget(self.frame_13, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        Fecha_Venda.setCentralWidget(self.centralwidget)

        self.retranslateUi(Fecha_Venda)
        QtCore.QMetaObject.connectSlotsByName(Fecha_Venda)
        Fecha_Venda.setTabOrder(self.Bt_Cancelar_Venda, self.Bt_Confirmar_Venda)

    def retranslateUi(self, Fecha_Venda):
        _translate = QtCore.QCoreApplication.translate
        Fecha_Venda.setWindowTitle(_translate("Fecha_Venda", "Venda Mesa"))
        self.Lb_Comanda_Mesa.setText(_translate("Fecha_Venda", "Fechamento de Venda"))
        self.label_2.setText(_translate("Fecha_Venda", "Operador:"))
        self.Lb_Nome_Perador.setText(_translate("Fecha_Venda", "LUCAS"))
        self.label.setText(_translate("Fecha_Venda", "Valor a Pagar"))
        self.label_11.setText(_translate("Fecha_Venda", "R$"))
        self.Lb_TotalPagar.setText(_translate("Fecha_Venda", "0,00"))
        self.label_5.setText(_translate("Fecha_Venda", "Forma de Pagamento"))
        self.Cb_FormaPagamento.setItemText(0, _translate("Fecha_Venda", "Nota"))
        self.label_4.setText(_translate("Fecha_Venda", "CLIENTE:"))
        self.Bt_Cancelar_Venda.setText(_translate("Fecha_Venda", "Cancelar"))
        self.Bt_Confirmar_Venda.setText(_translate("Fecha_Venda", "Confirmar Venda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fecha_Venda = QtWidgets.QMainWindow()
    ui = Ui_Fecha_Venda()
    ui.setupUi(Fecha_Venda)
    Fecha_Venda.show()
    sys.exit(app.exec())
