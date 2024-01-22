import sys
from datetime import datetime
from PyQt6.QtWidgets import QMainWindow
from form.Inicio.Form_Inicio import Ui_Form_Inicio
from funcoes.Banco.Conexao_banco import Classe_Banco


class Classe_Dashboard(QMainWindow, Ui_Form_Inicio):
    def __init__(self):
        super(Classe_Dashboard, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()

    
    def venda_hj(self):
        data_atual = datetime.now()
        data_formatada = data_atual.strftime("%d/%m/%Y")

        self.banco.cursorr.execute(f"SELECT * FROM pdv.vendas WHERE data LIKE '%{data_formatada}%'")
        resultados = self.banco.cursorr.fetchall()
        self.banco.desconectar()
        
        soma_valor_venda = 0

    # Somar os valores da terceira coluna (valor_venda)
        for resultado in resultados:
            valor_venda = float(resultado[2])  # Converter para float, se necessário
            soma_valor_venda += valor_venda

        # Imprimir apenas o resultado final
        print("Total da coluna 'valor_venda':", soma_valor_venda)

if __name__ == '__main__':
    systen = Classe_Dashboard()
