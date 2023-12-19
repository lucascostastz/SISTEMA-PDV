# Form implementation generated from reading ui file 'Form_Edit_Produto.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Edit_Produtos(object):
    def setupUi(self, Form_Edit_Produtos):
        Form_Edit_Produtos.setObjectName("Form_Edit_Produtos")
        Form_Edit_Produtos.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Form_Edit_Produtos.resize(1000, 500)
        Form_Edit_Produtos.setMinimumSize(QtCore.QSize(1000, 500))
        Form_Edit_Produtos.setMaximumSize(QtCore.QSize(1000, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../img/produtos-.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_Edit_Produtos.setWindowIcon(icon)
        self.fr_FormProdutos = QtWidgets.QFrame(parent=Form_Edit_Produtos)
        self.fr_FormProdutos.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormProdutos.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormProdutos.setObjectName("fr_FormProdutos")
        self.lb_FormProdutos = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(410, 10, 491, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.lb_FotoProduto = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FotoProduto.setGeometry(QtCore.QRect(20, 40, 301, 401))
        self.lb_FotoProduto.setStyleSheet("border: 1px solid #A2A2A2;\n"
"background: url(\'Images/icon/Photo.svg\') center no-repeat \n"
"")
        self.lb_FotoProduto.setText("")
        self.lb_FotoProduto.setScaledContents(True)
        self.lb_FotoProduto.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_FotoProduto.setObjectName("lb_FotoProduto")
        self.lb_FormProdutos_2 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_2.setGeometry(QtCore.QRect(410, 60, 150, 20))
        self.lb_FormProdutos_2.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_2.setObjectName("lb_FormProdutos_2")
        self.tx_DescricaoProduto = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_DescricaoProduto.setGeometry(QtCore.QRect(410, 80, 501, 25))
        self.tx_DescricaoProduto.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_DescricaoProduto.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_DescricaoProduto.setClearButtonEnabled(True)
        self.tx_DescricaoProduto.setObjectName("tx_DescricaoProduto")
        self.lb_FormProdutos_3 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_3.setGeometry(QtCore.QRect(410, 130, 211, 20))
        self.lb_FormProdutos_3.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_3.setObjectName("lb_FormProdutos_3")
        self.cb_CategoriaProduto = QtWidgets.QComboBox(parent=self.fr_FormProdutos)
        self.cb_CategoriaProduto.setGeometry(QtCore.QRect(410, 150, 210, 25))
        self.cb_CategoriaProduto.setMinimumSize(QtCore.QSize(210, 0))
        self.cb_CategoriaProduto.setStyleSheet("QComboBox{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QComboBox::down-arrow {\n"
"     image: url(\"+self.resourcepath(\'Images/down.png\')+\");\n"
" }\n"
"")
        self.cb_CategoriaProduto.setObjectName("cb_CategoriaProduto")
        self.cb_CategoriaProduto.addItem("")
        self.cb_CategoriaProduto.addItem("")
        self.cb_CategoriaProduto.addItem("")
        self.cb_CategoriaProduto.addItem("")
        self.cb_CategoriaProduto.addItem("")
        self.lb_FormProdutos_4 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_4.setGeometry(QtCore.QRect(720, 130, 191, 20))
        self.lb_FormProdutos_4.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_4.setObjectName("lb_FormProdutos_4")
        self.lb_FormProdutos_5 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_5.setGeometry(QtCore.QRect(410, 200, 201, 20))
        self.lb_FormProdutos_5.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_5.setObjectName("lb_FormProdutos_5")
        self.lb_FormProdutos_6 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(720, 200, 191, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_Estoque = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_Estoque.setGeometry(QtCore.QRect(410, 220, 210, 25))
        self.tx_Estoque.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_Estoque.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Estoque.setText("")
        self.tx_Estoque.setPlaceholderText("")
        self.tx_Estoque.setClearButtonEnabled(True)
        self.tx_Estoque.setObjectName("tx_Estoque")
        self.tx_Codigo = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_Codigo.setGeometry(QtCore.QRect(700, 220, 210, 25))
        self.tx_Codigo.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_Codigo.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Codigo.setPlaceholderText("")
        self.tx_Codigo.setClearButtonEnabled(True)
        self.tx_Codigo.setObjectName("tx_Codigo")
        self.lb_FormProdutos_8 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(410, 260, 461, 21))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_8.setText("")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.tx_Preco_Produto = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_Preco_Produto.setGeometry(QtCore.QRect(410, 310, 210, 25))
        self.tx_Preco_Produto.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_Preco_Produto.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 14px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Preco_Produto.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tx_Preco_Produto.setClearButtonEnabled(True)
        self.tx_Preco_Produto.setObjectName("tx_Preco_Produto")
        self.lb_FormProdutos_10 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_10.setGeometry(QtCore.QRect(410, 290, 50, 20))
        self.lb_FormProdutos_10.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_10.setObjectName("lb_FormProdutos_10")
        self.lb_FormProdutos_13 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_13.setGeometry(QtCore.QRect(730, 290, 150, 20))
        self.lb_FormProdutos_13.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_13.setObjectName("lb_FormProdutos_13")
        self.tx_Venda_Atacado = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_Venda_Atacado.setGeometry(QtCore.QRect(700, 310, 210, 25))
        self.tx_Venda_Atacado.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_Venda_Atacado.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 14px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Venda_Atacado.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tx_Venda_Atacado.setClearButtonEnabled(True)
        self.tx_Venda_Atacado.setObjectName("tx_Venda_Atacado")
        self.fr_BotoesFormProdutos = QtWidgets.QFrame(parent=self.fr_FormProdutos)
        self.fr_BotoesFormProdutos.setGeometry(QtCore.QRect(0, 470, 1000, 30))
        self.fr_BotoesFormProdutos.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_BotoesFormProdutos.setObjectName("fr_BotoesFormProdutos")
        self.Bt_CancelarProdutos = QtWidgets.QPushButton(parent=self.fr_BotoesFormProdutos)
        self.Bt_CancelarProdutos.setGeometry(QtCore.QRect(880, 0, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bt_CancelarProdutos.setFont(font)
        self.Bt_CancelarProdutos.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Bt_CancelarProdutos.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Bt_CancelarProdutos.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.Bt_CancelarProdutos.setStyleSheet("QPushButton {\n"
"background-color: #1E87F0;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/sair/delete_delete_exit_1577.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Bt_CancelarProdutos.setIcon(icon1)
        self.Bt_CancelarProdutos.setIconSize(QtCore.QSize(75, 25))
        self.Bt_CancelarProdutos.setObjectName("Bt_CancelarProdutos")
        self.Bt_SalvarProdutos = QtWidgets.QPushButton(parent=self.fr_BotoesFormProdutos)
        self.Bt_SalvarProdutos.setGeometry(QtCore.QRect(750, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bt_SalvarProdutos.setFont(font)
        self.Bt_SalvarProdutos.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Bt_SalvarProdutos.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Bt_SalvarProdutos.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.Bt_SalvarProdutos.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/salvar/salvar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Bt_SalvarProdutos.setIcon(icon2)
        self.Bt_SalvarProdutos.setIconSize(QtCore.QSize(50, 25))
        self.Bt_SalvarProdutos.setObjectName("Bt_SalvarProdutos")
        self.lb_qtdeMin = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_qtdeMin.setGeometry(QtCore.QRect(890, 350, 40, 35))
        self.lb_qtdeMin.setText("")
        self.lb_qtdeMin.setObjectName("lb_qtdeMin")
        self.tx_MinimoAtacado = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_MinimoAtacado.setGeometry(QtCore.QRect(700, 400, 210, 25))
        self.tx_MinimoAtacado.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_MinimoAtacado.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 12px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_MinimoAtacado.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tx_MinimoAtacado.setPlaceholderText("")
        self.tx_MinimoAtacado.setClearButtonEnabled(True)
        self.tx_MinimoAtacado.setObjectName("tx_MinimoAtacado")
        self.lb_FormProdutos_14 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_14.setGeometry(QtCore.QRect(730, 380, 140, 20))
        self.lb_FormProdutos_14.setStyleSheet("QLabel{\n"
"font-size: 10px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: normal;\n"
"color: red\n"
"}")
        self.lb_FormProdutos_14.setObjectName("lb_FormProdutos_14")
        self.tx_Marca = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_Marca.setGeometry(QtCore.QRect(700, 150, 210, 25))
        self.tx_Marca.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Marca.setClearButtonEnabled(True)
        self.tx_Marca.setObjectName("tx_Marca")
        self.bt_AddImagem = QtWidgets.QPushButton(parent=self.fr_FormProdutos)
        self.bt_AddImagem.setGeometry(QtCore.QRect(20, 440, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_AddImagem.setFont(font)
        self.bt_AddImagem.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_AddImagem.setIcon(icon1)
        self.bt_AddImagem.setObjectName("bt_AddImagem")
        self.line = QtWidgets.QFrame(parent=self.fr_FormProdutos)
        self.line.setGeometry(QtCore.QRect(370, 70, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.label.setGeometry(QtCore.QRect(590, 150, 31, 25))
        self.label.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.label_2.setGeometry(QtCore.QRect(590, 220, 31, 25))
        self.label_2.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.label_3.setGeometry(QtCore.QRect(880, 150, 31, 25))
        self.label_3.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.label_4.setGeometry(QtCore.QRect(880, 220, 31, 25))
        self.label_4.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.label_5.setGeometry(QtCore.QRect(880, 80, 31, 25))
        self.label_5.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.Tx_Validade = QtWidgets.QDateEdit(parent=self.fr_FormProdutos)
        self.Tx_Validade.setGeometry(QtCore.QRect(410, 400, 210, 25))
        self.Tx_Validade.setStyleSheet("background: #CFCFCF;")
        self.Tx_Validade.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Tx_Validade.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.Tx_Validade.setObjectName("Tx_Validade")
        self.label_6 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.label_6.setGeometry(QtCore.QRect(410, 310, 31, 25))
        self.label_6.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.label_7.setGeometry(QtCore.QRect(700, 310, 31, 25))
        self.label_7.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.label_8.setGeometry(QtCore.QRect(700, 400, 31, 25))
        self.label_8.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.label_10.setGeometry(QtCore.QRect(410, 400, 31, 25))
        self.label_10.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.lb_FormProdutos_15 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_15.setGeometry(QtCore.QRect(410, 380, 141, 20))
        self.lb_FormProdutos_15.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_15.setObjectName("lb_FormProdutos_15")
        self.label_9 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 301, 31))
        self.label_9.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"color: #FFF")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.tx_Marca.raise_()
        self.lb_FormProdutos.raise_()
        self.lb_FotoProduto.raise_()
        self.lb_FormProdutos_2.raise_()
        self.tx_DescricaoProduto.raise_()
        self.lb_FormProdutos_3.raise_()
        self.cb_CategoriaProduto.raise_()
        self.lb_FormProdutos_4.raise_()
        self.lb_FormProdutos_5.raise_()
        self.lb_FormProdutos_6.raise_()
        self.tx_Estoque.raise_()
        self.tx_Codigo.raise_()
        self.lb_FormProdutos_8.raise_()
        self.tx_Preco_Produto.raise_()
        self.lb_FormProdutos_10.raise_()
        self.lb_FormProdutos_13.raise_()
        self.tx_Venda_Atacado.raise_()
        self.fr_BotoesFormProdutos.raise_()
        self.lb_qtdeMin.raise_()
        self.tx_MinimoAtacado.raise_()
        self.lb_FormProdutos_14.raise_()
        self.bt_AddImagem.raise_()
        self.line.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.Tx_Validade.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.lb_FormProdutos_15.raise_()
        self.label_9.raise_()

        self.retranslateUi(Form_Edit_Produtos)
        QtCore.QMetaObject.connectSlotsByName(Form_Edit_Produtos)
        Form_Edit_Produtos.setTabOrder(self.tx_DescricaoProduto, self.cb_CategoriaProduto)
        Form_Edit_Produtos.setTabOrder(self.cb_CategoriaProduto, self.tx_Marca)
        Form_Edit_Produtos.setTabOrder(self.tx_Marca, self.tx_Estoque)
        Form_Edit_Produtos.setTabOrder(self.tx_Estoque, self.tx_Codigo)
        Form_Edit_Produtos.setTabOrder(self.tx_Codigo, self.tx_Preco_Produto)
        Form_Edit_Produtos.setTabOrder(self.tx_Preco_Produto, self.tx_Venda_Atacado)
        Form_Edit_Produtos.setTabOrder(self.tx_Venda_Atacado, self.Tx_Validade)
        Form_Edit_Produtos.setTabOrder(self.Tx_Validade, self.tx_MinimoAtacado)
        Form_Edit_Produtos.setTabOrder(self.tx_MinimoAtacado, self.bt_AddImagem)

    def retranslateUi(self, Form_Edit_Produtos):
        _translate = QtCore.QCoreApplication.translate
        Form_Edit_Produtos.setWindowTitle(_translate("Form_Edit_Produtos", "LC INFORMÁTICA | CADASTRO PRODUTOS"))
        self.lb_FormProdutos.setText(_translate("Form_Edit_Produtos", "CADASTRAR PRODUTO"))
        self.lb_FotoProduto.setToolTip(_translate("Form_Edit_Produtos", "Insira uma imagem"))
        self.lb_FormProdutos_2.setText(_translate("Form_Edit_Produtos", "DESCRIÇÃO"))
        self.tx_DescricaoProduto.setPlaceholderText(_translate("Form_Edit_Produtos", "DESCRIÇÃO DO PRODUTO"))
        self.lb_FormProdutos_3.setText(_translate("Form_Edit_Produtos", "CATEGORIA"))
        self.cb_CategoriaProduto.setItemText(0, _translate("Form_Edit_Produtos", "SELECIONE"))
        self.cb_CategoriaProduto.setItemText(1, _translate("Form_Edit_Produtos", "ALIMENTOS "))
        self.cb_CategoriaProduto.setItemText(2, _translate("Form_Edit_Produtos", "BEBIDAS"))
        self.cb_CategoriaProduto.setItemText(3, _translate("Form_Edit_Produtos", "INFORMÁTICA"))
        self.cb_CategoriaProduto.setItemText(4, _translate("Form_Edit_Produtos", "ELETRÔNICOS"))
        self.lb_FormProdutos_4.setText(_translate("Form_Edit_Produtos", "MARCA"))
        self.lb_FormProdutos_5.setText(_translate("Form_Edit_Produtos", "ESTOQUE"))
        self.lb_FormProdutos_6.setText(_translate("Form_Edit_Produtos", "CÓDIGO"))
        self.tx_Preco_Produto.setPlaceholderText(_translate("Form_Edit_Produtos", "R$ 0.00"))
        self.lb_FormProdutos_10.setText(_translate("Form_Edit_Produtos", "PREÇO"))
        self.lb_FormProdutos_13.setText(_translate("Form_Edit_Produtos", "VENDA ATACADO"))
        self.tx_Venda_Atacado.setPlaceholderText(_translate("Form_Edit_Produtos", "R$ 0.00"))
        self.Bt_CancelarProdutos.setText(_translate("Form_Edit_Produtos", "CANCELAR"))
        self.Bt_SalvarProdutos.setText(_translate("Form_Edit_Produtos", "SALVAR"))
        self.lb_FormProdutos_14.setText(_translate("Form_Edit_Produtos", "QTDE. MÍNIMA P/ ATACADO"))
        self.tx_Marca.setPlaceholderText(_translate("Form_Edit_Produtos", "NOVA MARCA"))
        self.bt_AddImagem.setToolTip(_translate("Form_Edit_Produtos", "<html><head/><body><p>CADASTRAR IMGEM</p></body></html>"))
        self.bt_AddImagem.setText(_translate("Form_Edit_Produtos", "INSERIR IMAGEM"))
        self.lb_FormProdutos_15.setText(_translate("Form_Edit_Produtos", "DATA VALIDADE"))
        self.label_9.setText(_translate("Form_Edit_Produtos", "PRODUTO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Edit_Produtos = QtWidgets.QFrame()
    ui = Ui_Form_Edit_Produtos()
    ui.setupUi(Form_Edit_Produtos)
    Form_Edit_Produtos.show()
    sys.exit(app.exec())
