import sys
from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow, QApplication
from form.Finaliza_Venda.Form_Comprovante_Nota import Ui_MainWindow


class Classe_Comprovante_Nota(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Classe_Comprovante_Nota, self).__init__()
        self.setupUi(self)

        self.Lb_Imagem.setPixmap(QtGui.QPixmap("./img/venda.png"))
        self.Bt_Cancela_venda.clicked.connect(self.fecha_janela)

    def fecha_janela(self):
        self.close()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    system = Classe_Comprovante_Nota()
    system.show()
    sys.exit(app.exec())