from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtWidgets
from form.Comanda.Form_Comanda import Ui_Comanda
from funcoes.Banco.Conexao_banco import Classe_Banco

class Classe_Comanda(QMainWindow, Ui_Comanda):
    def __init__(self):
        super(Classe_Comanda, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()

        self.Bt_Fechar_Comanda.clicked.connect(self._fechar_janela)

    def listar_mesa(self):
        self.total = 0
        self.tableWidget.verticalHeader().hide()
        col_widths = [50, 330, 70, 75, 75]
        for i, width in enumerate(col_widths):
            self.tableWidget.setColumnWidth(i, width)
        self.banco.conectar()
        self.banco.cursorr.execute("SELECT idmesa1, produto, valor_unitario, quantidade, valor_total FROM pdv.mesa1")
        dados_lidosc = self.banco.cursorr.fetchall()
        self.tableWidget.setRowCount(len(dados_lidosc))
        self.tableWidget.setColumnCount(5)
        for a, dados in enumerate(dados_lidosc):
            for b, valor in enumerate(dados):
                item = QtWidgets.QTableWidgetItem(str(valor))
                self.tableWidget.setItem(a, b, item)
        self.banco.query.commit()
        self.banco.cursorr.close()
        
        for row in range(self.tableWidget.rowCount()):
            valor_total = float(self.tableWidget.item(row, 4).text())
            print(valor_total)
            self.total += valor_total


    def contar(self):
        self.Lb_Total.setText(str(f"{self.total:.2f}")) 

    def _fechar_janela(self):
        self.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Comanda()
    system.show()
    sys.exit(app.exec())