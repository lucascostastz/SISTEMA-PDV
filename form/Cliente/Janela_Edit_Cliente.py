from PyQt6.QtWidgets import QMainWindow, QApplication
from form.Cliente.Form_Edit_Clientes import Ui_Form_Edit_Clientes
from funcoes.Banco.Conexao_banco import Classe_Banco
from funcoes.Alertas.Arquivo_Alertas import Classe_Alertas


class Classe_Edit_Cliente(QMainWindow, Ui_Form_Edit_Clientes):
    def __init__(self, inicio):
        super(Classe_Edit_Cliente, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()
        self.alertas = Classe_Alertas()
        self.inicio = inicio

        self.inicio.Bt_Edit_Cliente.clicked.connect(self.seleciona_cliente_edit)
        self.inicio.TableWidget_Cliente.doubleClicked.connect(self.seleciona_cliente_edit)
        self.bt_Salvar.clicked.connect(self.salvar_cliente_editado)
        self.bt_Voltar.clicked.connect(self.fecha_janela)

    
    def chama_edit_cliente(self):
        self.show()  
        self.tx_Nome.setText(self.nome_cliente_edit)
        self.tx_Cpf.setText(self.cpf_cliente_edit)
        self.tx_Rg.setText(self.rg_cliente_edit)
        self.tx_Telefone.setText(self.telefone_cliente_edit)
        self.tx_Email.setText(self.email_cliente_edit)
        self.tx_Cep.setText(self.cep_cliente_edit)
        self.tx_Endereco.setText(self.endereco_cliente_edit)
        self.tx_Numero.setText(self.numero_cliente_edit)
        self.tx_Bairro.setText(self.bairro_cliente_edit)
        self.tx_Cidade.setText(self.cidade_cliente_edit)
        self.tx_Estado.setText(self.estado_cliente_edit)
        self.tx_Credito.setText(self.limite_cliente_edit)

    
    def seleciona_cliente_edit(self):
        linha = self.inicio.TableWidget_Cliente.currentRow()
        if linha >= 0:
            # Obtenha os dados da tabela após a pesquisa
            self.id_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 0).text()
            self.nome_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 1).text()
            self.cpf_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 2).text()
            self.rg_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 3).text()
            self.telefone_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 4).text()
            self.email_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 5).text()
            self.cep_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 6).text()
            self.endereco_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 7).text()
            self.numero_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 8).text()
            self.bairro_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 9).text()
            self.cidade_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 10).text()
            self.estado_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 11).text()
            self.limite_cliente_edit = self.inicio.TableWidget_Cliente.item(linha, 12).text()
            self.chama_edit_cliente()


    def salvar_cliente_editado(self):
            nome = self.tx_Nome.text()
            rg = self.tx_Rg.text()
            cpf = self.tx_Cpf.text()
            telefone = self.tx_Telefone.text()
            email = self.tx_Email.text()
            cep = self.tx_Cep.text()
            endereco = self.tx_Endereco.text()
            numero = self.tx_Numero.text()
            bairro = self.tx_Bairro.text()
            cidade = self.tx_Cidade.text()
            estado = self.tx_Estado.text()
            credito = self.tx_Credito.text()
            #### Atualizar os dados no banco ###
            self.banco.conectar()
            self.banco.cursorr.execute("UPDATE pdv.clientes SET nome = '{}', rg  = '{}', cpf = '{}', telefone ='{}', email = '{}', cep = '{}', endereco = '{}', numero = '{}', bairro = '{}', cidade = '{}', estado = '{}', credito = '{}'  WHERE idclientes = {}".format(
                nome, rg, cpf, telefone, email, cep, endereco, numero, bairro, cidade, estado, credito, self.id_cliente_edit))
            self.banco.query.commit()
            self.banco.query.close()
            self.inicio.listar_clientes()
            self.alertas.alerta_cliente_editado()
         

    def fecha_janela(self):
        self.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Edit_Cliente()
    system.show()
    sys.exit(app.exec())