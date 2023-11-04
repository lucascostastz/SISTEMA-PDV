import sys
from PyQt6.QtWidgets import *
from form.Finaliza_Venda.Form_Lista_Cliente import Ui_Lista_Cliente


class Classe_Lista_Cliente(QMainWindow, Ui_Lista_Cliente):
    def __init__(self):
        super(Classe_Lista_Cliente, self).__init__()
        self.setupUi(self)

        

  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    system = Classe_Lista_Cliente()
    system.show()
    sys.exit(app.exec())