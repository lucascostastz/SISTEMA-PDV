from PyQt6.QtWidgets import *
from form.Finaliza_Venda.Form_Comprovante import Ui_MainWindow
import sys
from PyQt6 import QtGui

class Classe_Comprovante(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Classe_Comprovante, self).__init__()
        self.setupUi(self)

        self.Lb_Imagem.setPixmap(QtGui.QPixmap("./img/venda.png"))
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    system = Classe_Comprovante()
    system.show()
    sys.exit(app.exec())