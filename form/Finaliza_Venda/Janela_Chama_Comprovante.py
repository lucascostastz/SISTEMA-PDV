import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtGui
from form.Finaliza_Venda.Form_Comprovante import Ui_MainWindow


class Classe_Comprovante(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Classe_Comprovante, self).__init__()
        self.setupUi(self)

        self.Lb_Imagem.setPixmap(QtGui.QPixmap("./img/venda.png"))
        self.Bt_Cancela_venda.clicked.connect(self.fechar_janela)
    
    def fechar_janela(self):
        self.close()
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    system = Classe_Comprovante()
    system.show()
    sys.exit(app.exec())