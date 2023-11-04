from PyQt6.QtWidgets import *
from time import sleep
from PyQt6.QtCore import Qt
from form.Comanda.Form_Comanda import Ui_Comanda

class Classe_Comanda(QMainWindow, Ui_Comanda):
    def __init__(self):
        super(Classe_Comanda, self).__init__()
        self.setupUi(self)

        self.Bt_Salvar.clicked.connect(self._fechar_janela)
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,50)
        self.tableWidget.setColumnWidth(2,530)
        self.tableWidget.setColumnWidth(3,75)
        self.tableWidget.setColumnWidth(4,75)

    def _fechar_janela(self):
        self.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Comanda()
    system.show()
    sys.exit(app.exec())