from PyQt6.QtWidgets import *
from time import sleep
from PyQt6.QtCore import Qt
from form.Chama_Venda.Form_Chama_Venda import Ui_Chama_Venda
from form.Venda_Mesa.Janela_Chama_Venda import Classe_Venda_Mesa



class Classe_Chama_Venda(QMainWindow, Ui_Chama_Venda):
    def __init__(self):
        super(Classe_Chama_Venda, self).__init__()
        self.setupUi(self)
        self.venda_mesa = Classe_Venda_Mesa()


        self.Bt_Voltar.clicked.connect(self._fechar_janela)
        

    
    def _fechar_janela(self):
        self.close()

        