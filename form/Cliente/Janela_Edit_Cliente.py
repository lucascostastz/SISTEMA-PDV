from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from form.Cliente.Form_Edit_Clientes import Ui_Form_Edit_Clientes

class Classe_Edit_Cliente(QMainWindow, Ui_Form_Edit_Clientes):
    def __init__(self):
        super(Classe_Edit_Cliente, self).__init__()
        self.setupUi(self)

        self.bt_Voltar.clicked.connect(self.fecha_janela)
    
    def fecha_janela(self):
        self.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Edit_Cliente()
    system.show()
    sys.exit(app.exec())