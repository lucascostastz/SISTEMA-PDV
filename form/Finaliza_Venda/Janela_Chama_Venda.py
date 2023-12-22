from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
from PyQt6.QtGui import QKeySequence, QShortcut
from form.Finaliza_Venda.Form_Finaliza_Venda import Ui_Fecha_Venda


class Classe_Finaliza_Venda(QMainWindow, Ui_Fecha_Venda):
    def __init__(self):
        super(Classe_Finaliza_Venda, self).__init__()
        self.setupUi(self)

        
        self.Bt_Cancelar_Venda.clicked.connect(self.fechar_janela)
        shortcut = QShortcut(QKeySequence('Esc'), self)
        shortcut.activated.connect(self.fechar_janela)

    def fechar_janela(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    systen = Classe_Finaliza_Venda()
    systen.showMaximized()
    sys.exit(app.exec())