from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap
from time import sleep
from form.Login.Form_Login import Ui_MainWindow


from funcoes.Banco.Conexao_banco import Classe_Banco

class Classe_Login(QMainWindow, Ui_MainWindow):
    def __init__(self, inicio):
        super(Classe_Login, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()
        self.inicio = inicio

        pixmap = QPixmap('./img/Banner_LC')
        self.Lb_Img.setPixmap(pixmap)
        self.Lb_Img.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        self.Lb_Img.setPixmap(pixmap)
        self.Lb_Img.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.Bt_Login.clicked.connect(self.verifica_login)
        self.Tx_Senha.returnPressed.connect(self.verifica_login)
        self.Bt_Sair.clicked.connect(self._fechar_janela)
        self.Tx_Usuario.returnPressed.connect(self.seleciona_password)
        self.Bt_check.clicked.connect(self.password_check)


     ######## --- Função de validação de usuário --- #########
    def verifica_login(self):
        try:
            login = self.Tx_Usuario.text()
            senha2 = self.Tx_Senha.text()
            self.banco.conectar()
            self.banco.cursorr.execute(
            "SELECT senha1, nivel_de_acesso FROM pdv.usuarios WHERE login ='{}'".format(login))
            senha_db = self.banco.cursorr.fetchall()        
            try:
                if senha2 == senha_db[0][0] and (senha_db[0][1]) == 'ADMINISTRADOR':
                    self.carregar()
                    self.hide()           
                    self.inicio.showMaximized() 
                    self.user_logado = login
                    self.inicio.Lb_User_Logado.setText(self.user_logado)
                    self.banco.query.close()
                elif senha2 == senha_db[0][0] and (senha_db[0][1]) == 'USUÁRIO':
                    self.carregar()
                    self.hide()        
                    self.inicio.showMaximized()
                    self.inicio.permissoes_visualizar()
                    self.banco.query.close()
                else:
                    self.Lb_Info.setText("Dados de login incorretos!")    
                    self.banco.query.close()
            except:
                self.Lb_Info.setText("Dados de login incorretos!")           
                self.banco.query.close()
        except:
            self.Lb_Info_banco.setText("Erro ao conectar ao banco de dados!")

    def seleciona_password(self):
        self.Tx_Senha.setFocus()

    def password_check(self):      
        bt = self.Bt_check.sender()
        if bt.isChecked() == True:
            self.Tx_Senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:    
            self.Tx_Senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  
    

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

    def _fechar_janela(self):
        self.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Login()
    system.show()
    sys.exit(app.exec())