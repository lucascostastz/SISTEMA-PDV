from PyQt6.QtWidgets import *
from form.Finaliza_Venda.Form_Finaliza_Venda_Nota import Ui_Fecha_Venda


class Classe_Finaliza_Venda_CLiente(QMainWindow, Ui_Fecha_Venda):
    def __init__(self):
        super(Classe_Finaliza_Venda_CLiente, self).__init__()
        self.setupUi(self)

        self.Bt_Cancelar_Venda.clicked.connect(self.fechar_janela)

    def fechar_janela(self):
        self.close()