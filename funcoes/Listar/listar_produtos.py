from PyQt6 import QtWidgets
from form.Inicio.Janela_Inicio import Classe_Inicio
from funcoes.Banco.Conexao_banco import Classe_Banco

class Classe_Listar():
    def __init__(self):
        super().__init__()
        self.inicio = Classe_Inicio()
        self.banco = Classe_Banco()

    def lista_produtos(self):
            self.inicio.TableWidget_Produto.verticalHeader().hide()
            self.banco.conectar()
            self.banco.cursorr.execute("SELECT * FROM pdv.produtos")
            dados_lidos = self.banco.cursorr.fetchall()
            self.inicio.TableWidget_Produto.setRowCount(len(dados_lidos))
            self.inicio.TableWidget_Produto.setColumnCount(10)
            for a in range(0, len(dados_lidos)):
                for b in range(0, 10):
                    self.inicio.TableWidget_Produto.setItem(
                        a, b, QtWidgets.QTableWidgetItem(str(dados_lidos[a][b])))
            self.banco.query.commit()
            self.banco.query.close()
            self.lista_produtos()