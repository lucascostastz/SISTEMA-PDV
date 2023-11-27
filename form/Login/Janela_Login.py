from PyQt6.QtWidgets import *
from time import sleep
from form.Login.Form_Login import Ui_MainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class Classe_Login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Classe_Login, self).__init__()
        self.setupUi(self)

        self.Bt_Sair.clicked.connect(self._fechar_janela)
    
        
        pixmap = QPixmap('./img/Banner_LC')
        self.Lb_Img.setPixmap(pixmap)
        self.Lb_Img.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        self.Lb_Img.setPixmap(pixmap)
        self.Lb_Img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
    
    def _fechar_janela(self):
        self.close()

    def carregar(self):
        self.Tx_Usuario.clear()
        self.Tx_Senha.clear()
        self.Lb_Info.clear()
        self.Lb_Info2.setText("Carregando...")
        self.my_progressBar.show()
        sleep(0.5)
        self.my_progressBar.setValue(10)
        sleep(0.5)
        self.my_progressBar.setValue(20)
        sleep(0.5)
        self.my_progressBar.setValue(30)
        sleep(0.5)
        self.Lb_Info2.setText("Aguarde...")
        self.my_progressBar.setValue(40)
        sleep(0.5)
        self.my_progressBar.setValue(50)
        sleep(0.5)
        self.my_progressBar.setValue(60)
        sleep(0.5)
        self.Lb_Info2.setText("Iniciando o sistema...")
        self.my_progressBar.setValue(70)
        sleep(0.5)
        self.my_progressBar.setValue(80)
        sleep(0.3)
        self.my_progressBar.setValue(90)
        sleep(0.1)
        self.my_progressBar.setValue(100)
        sleep(0.5)
        self.my_progressBar.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Login()
    system.show()
    sys.exit(app.exec())