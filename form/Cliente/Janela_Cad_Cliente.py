from PyQt6.QtWidgets import QMainWindow, QApplication
from form.Cliente.Form_Cad_Clientes import Ui_Form_Cad_Clientes
from funcoes.Alertas.Arquivo_Alertas import Classe_Alertas
from funcoes.Banco.Conexao_banco import Classe_Banco

class Classe_Cad_Cliente(QMainWindow, Ui_Form_Cad_Clientes):
    def __init__(self, inicio):
        super(Classe_Cad_Cliente, self).__init__()
        self.setupUi(self)
        self.alertas = Classe_Alertas()
        self.banco = Classe_Banco()
        self.inicio = inicio


        self.Bt_Salvar.clicked.connect(self.inserir_clientes)
        self.Bt_Voltar.clicked.connect(self.fechar_janela)

    
    def inserir_clientes(self):
        nome = self.tx_Nome.text()
        rg = self.tx_rg.text()
        cpf = self.tx_cpf.text()
        telefone = self.tx_Telefone.text()
        email = self.tx_Email.text()
        cep = self.tx_Cep.text()
        endereco = self.tx_Endereco.text()
        numero = self.tx_Numero.text()
        bairro = self.tx_Bairro.text()
        cidade = self.tx_Cidade.text()
        estado = self.tx_Estado.text()
        credito = self.tx_Credito.text()
        credito_utilizado = '0'
        self.banco.conectar()
        self.banco.cursorr.execute("INSERT INTO pdv.clientes (nome,rg,cpf,telefone,email,cep,endereco,numero,bairro,cidade,estado,credito,credito_utilizado,credito_saldo) VALUES('" +
                    nome+"','"+rg+"','"+cpf+"','"+telefone+"','"+email+"','"+cep+"','"+endereco+"','"+numero+"','"+bairro+"','"+cidade+"','"+estado+"', '"+credito+"', '"+credito_utilizado+"', '"+credito+"')")
        self.banco.query.commit()
        self.banco.query.close()
        self.inicio.listar_clientes()
        self.limpar_campos()
        

    def limpar_campos(self):
        self.tx_Nome.clear()
        self.tx_Bairro.clear()
        self.tx_Numero.clear()
        self.tx_Cep.clear()
        self.tx_Cidade.clear()
        self.tx_cpf.clear()
        self.tx_Email.clear()
        self.tx_Estado.clear()
        self.tx_Endereco.clear()
        self.tx_rg.clear()
        self.tx_Telefone.clear()
        self.tx_Credito.clear()
    

    def fechar_janela(self):
        self.limpar_campos()
        self.close()
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Cad_Cliente()
    system.show()
    sys.exit(app.exec())