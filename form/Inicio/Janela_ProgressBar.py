from form.Inicio.Form_Progressbar import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys

class Classe_ProgressBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Classe_ProgressBar, self).__init__()
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    systen = Classe_ProgressBar()
    systen.show()
    sys.exit(app.exec())