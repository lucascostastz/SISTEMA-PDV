from PyQt6.QtWidgets import *
from form.Finaliza_Venda.Form_Comprovante import Ui_Dialog

class Classe_Comprovante(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(Classe_Comprovante, self).__init__()
        self.setupUi(self)

   
    def fechar_janela(self):
        self.close()