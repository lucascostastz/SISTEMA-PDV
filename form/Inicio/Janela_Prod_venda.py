import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from form.Inicio.Form_Tabela_Prod_venda import Ui_MainWindow

class Classe_Prod(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Classe_Prod, self).__init__()
        self.setupUi(self)


   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    system = Classe_Prod()
    system.show()
    sys.exit(app.exec())