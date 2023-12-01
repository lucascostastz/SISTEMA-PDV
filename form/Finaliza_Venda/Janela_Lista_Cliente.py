import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from form.Finaliza_Venda.Form_Lista_Cliente import Ui_Lista_Cliente
from funcoes.Banco.Conexao_banco import Classe_Banco
from funcoes.Alertas.Arquivo_Alertas import Classe_Alertas


class Classe_Lista_Cliente(QMainWindow, Ui_Lista_Cliente):
    def __init__(self):
        super(Classe_Lista_Cliente, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()
        self.alert = Classe_Alertas()


        self.Bt_Cancelar.clicked.connect(self.fecha_lista_cliente)
        self.tx_BuscaClientes_Venda.textChanged.connect(self.pesquisar_clientes_venda)

        
    def listar_cliente_venda(self):
        self.tableWidget_cliente.verticalHeader().hide()
        col_widths = [50, 150, 85, 85, 170, 75, 75, 75]
        for i, width in enumerate(col_widths):
            self.tableWidget_cliente.setColumnWidth(i, width)
        try:
            self.banco.conectar()
            self.banco.cursorr.execute("SELECT idclientes, nome, cpf, rg, endereco, credito, credito_utilizado, credito_saldo FROM pdv.clientes")
            dados_lidosc = self.banco.cursorr.fetchall()
            self.tableWidget_cliente.setRowCount(len(dados_lidosc))
            self.tableWidget_cliente.setColumnCount(8)
            for a, dados in enumerate(dados_lidosc):
                for b, valor in enumerate(dados):
                    item = QtWidgets.QTableWidgetItem(str(valor))
                    self.tableWidget_cliente.setItem(a, b, item)
            self.banco.query.commit()
            self.banco.cursorr.close()
        except:
            pass
        

    def pesquisar_clientes_venda(self):
        self.consulta_cliente_venda = self.tx_BuscaClientes_Venda.text()
        try:
            self.banco.conectar()
            self.banco.cursorr.execute(f"SELECT * FROM pdv.clientes WHERE nome LIKE '%{self.consulta_cliente_venda}%' or cpf LIKE '%{self.consulta_cliente_venda}%'")
            lista = self.banco.cursorr.fetchall()
            lista = list(lista)
            if not lista:
                return  self.alert.alerta_registro()    
            else:   
                self.tableWidget_cliente.setRowCount(0)
                #primeiro for trás
                for idxLinha, linha in enumerate(lista):
                    self.tableWidget_cliente.insertRow(idxLinha)
                    for idxColuna, coluna in enumerate(linha):
                        self.tableWidget_cliente.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
            self.banco.query.commit()
            self.banco.query.close()
            self.banco.cursorr.close()
        except:
            pass

    
    def fecha_lista_cliente(self):
        self.close()
  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    system = Classe_Lista_Cliente()
    system.show()
    sys.exit(app.exec())