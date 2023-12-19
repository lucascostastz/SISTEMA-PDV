from PyQt6.QtWidgets import QMainWindow, QApplication
from form.Usuario.Form_Cad_Usuario import Ui_Form_Cad_Usuario
from funcoes.Banco.Conexao_banco import Classe_Banco
from funcoes.Alertas.Arquivo_Alertas  import Classe_Alertas


class Classe_Cad_Usuario(QMainWindow, Ui_Form_Cad_Usuario):
    def __init__(self, inicio):
        super(Classe_Cad_Usuario, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()
        self.alertas = Classe_Alertas()
        self.inicio = inicio


        self.Bt_CancelarUsuario.clicked.connect(self.fechar_janela)
        self.bt_SalvarUsuario.clicked.connect(self.inserir_usuarios)

    
    def inserir_usuarios(self):
        nome =  self.tx_nome.text()
        login = self.tx_Login.text()
        senha1 = self.tx_Senha.text()
        senha2 = self.tx_Senha2.text()
        nivel_acesso = self.cb_Nivel_Acesso.currentText()
        permissao =  self.cb_Permissoes.currentText()
        self.banco.conectar()
        if nome == "":
            self.alertas.alt_cad_em_branco()
        elif login == "":
                self.alertas.alt_cad_em_branco()
        elif senha1 == "":
                self.alertas.alt_cad_em_branco()
        elif senha2 == "":
                self.alertas.alt_cad_em_branco()
        elif nivel_acesso == "SELECIONE":
                self.alertas.alt_erro_cad_nivel_acesso()
        elif permissao == "SELECIONE":
                self.alertas.alt_erro_cad_permissao()
        elif senha1!= senha2:
                self.alertas.alt_senha_diferente()
        else:
            self.banco.cursorr.execute("INSERT INTO pdv.usuarios (nome,login,senha1,senha2,nivel_de_acesso,permissao) VALUES('"+nome+"','"+
                    login+"','"+senha1+"','"+senha2+"','"+nivel_acesso+"','"+permissao+"')")
            self.banco.query.commit()
            self.banco.query.close()
            self.limpa_campos()
            self.alertas.alt_cadastro_sucesso()
            self.inicio.listar_usuarios()
        

    def limpa_campos(self):
        self.tx_nome.clear()
        self.tx_Login.clear()
        self.tx_Senha.clear()
        self.tx_Senha2.clear()
        self.cb_Nivel_Acesso.setCurrentIndex(0)
        self.cb_Permissoes.setCurrentIndex(0)


    def fechar_janela(self):
        self.limpa_campos()
        self.close()

        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Cad_Usuario()
    system.show()
    sys.exit(app.exec())