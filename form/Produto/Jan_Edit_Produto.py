from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from form.Produto.Form_Edit_Produto import Ui_Ui_Edit_Produto

class Classe_Edit_Produto(QMainWindow, Ui_Ui_Edit_Produto):
    def __init__(self):
        super(Classe_Edit_Produto, self).__init__()
        self.setupUi(self)

        self.Bt_CancelarProdutos.clicked.connect(self.sair)


    def sair(self):
        self.close()

        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Edit_Produto()
    system.show()
    sys.exit(app.exec())