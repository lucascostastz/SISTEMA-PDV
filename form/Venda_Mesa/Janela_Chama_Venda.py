from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from form.Venda_Mesa.Form_Venda_Mesa import Ui_Venda_Mesa
from funcoes.Banco.Conexao_banco import Classe_Banco


class Classe_Venda_Mesa(QMainWindow, Ui_Venda_Mesa):
    def __init__(self):
        super(Classe_Venda_Mesa, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()

        self.Bt_Fechar_Comanda.clicked.connect(self.fechar_janela)

        self.format_tabwdgt_venda()
        self.format_tabwdgt_produtos()


    def format_tabwdgt_venda(self):
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,50)
        self.tableWidget.setColumnWidth(2,530)
        self.tableWidget.setColumnWidth(3,75)
        self.tableWidget.setColumnWidth(4,75)

    
    def format_tabwdgt_produtos(self):
        self.tableWidget_Prod.setColumnWidth(0,81)
        self.tableWidget_Prod.setColumnWidth(1,625)
        self.tableWidget_Prod.setColumnWidth(2,85)


    def listar_prod_venda_Mesa(self):
        self.tableWidget_Prod.verticalHeader().hide()
        try:
            self.banco.conectar()
            self.banco.cursorr.execute("SELECT idprodutos, descricao, preco FROM pdv.produtos")
            dados_lidos = self.banco.cursorr.fetchall()
            self.tableWidget_Prod.setRowCount(len(dados_lidos))
            self.tableWidget_Prod.setColumnCount(3)
            for a, dados in enumerate(dados_lidos):
                for b, valor in enumerate(dados):
                    item = QtWidgets.QTableWidgetItem(str(valor))
                    self.tableWidget_Prod.setItem(a, b, item)
            self.banco.query.commit()
            self.banco.cursorr.close()
        except:
            pass
  

    def fechar_janela(self):
        self.close()
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Venda_Mesa()
    system.show()
    sys.exit(app.exec())