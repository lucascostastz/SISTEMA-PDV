from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtWidgets
from form.Comanda.Form_Comanda import Ui_Comanda
from funcoes.Banco.Conexao_banco import Classe_Banco

class Classe_Comanda(QMainWindow, Ui_Comanda):
    def __init__(self, inicio):
        super(Classe_Comanda, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()
        self.inicio = inicio
        self.Bt_Fechar_Comanda.clicked.connect(self._fechar_janela)


    def _fechar_janela(self):
        self.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Comanda()
    system.show()
    sys.exit(app.exec())