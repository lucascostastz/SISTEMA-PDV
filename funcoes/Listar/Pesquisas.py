from PyQt6 import QtWidgets
from funcoes.Banco.Conexao_banco import Classe_Banco
from funcoes.Alertas.Arquivo_Alertas import Classe_Alertas
from form.Inicio.Form_Inicio import Ui_Form_Inicio

class Classe_Pesquisa():
    def __init__(self):
        super().__init__()
        self.banco = Classe_Banco()
        self.alert = Classe_Alertas()
        self.ini = Classe_Inicio

    def pesquisa_cliente_relatorio(self):
        consulta_cliente_relatorio = self.ini.Tx_cliente_relatorio.text()
   
        self.banco.conectar()
        self.banco.cursorr.execute(f"SELECT * FROM pdv.vendas WHERE cliente LIKE '%{consulta_cliente_relatorio}%'")
        lista = self.banco.cursorr.fetchall()
        lista = list(lista)
        if not lista:
            return  self.alert.alerta_registro()
        else:   
            self.inicio.TableWidget_Relatorio.setRowCount(0)
            for idxLinha, linha in enumerate(lista):
                self.inicio.TableWidget_Relatorio.insertRow(idxLinha)
                for idxColuna, coluna in enumerate(linha):
                    self.inicio.TableWidget_Relatorio.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
        self.banco.query.commit()
        self.banco.query.close()
        self.banco.cursorr.close()
      
        
            
