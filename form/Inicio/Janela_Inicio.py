import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtWidgets
from form.Inicio.Form_Inicio import Ui_Form_Inicio
from funcoes.Banco.Conexao_banco import Classe_Banco
from funcoes.Alertas.Arquivo_Alertas import Classe_Alertas


class Classe_Inicio(QMainWindow, Ui_Form_Inicio):
    def __init__(self):
        super(Classe_Inicio, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()
        self.alert = Classe_Alertas()


        self.Tx_cliente_relatorio.textChanged.connect(self.pesquisa_cliente_relatorio)
        self.Tx_Usuario_relatorio.textChanged.connect(self.pesquisa_operador_relatorio)
        self.Tx_Venda_relatorio.textChanged.connect(self.pesquisa_n_venda_relatorio)
        self.Bt_Ft_Pagamento.clicked.connect(self.filtro_forma_pgmt_relatorio)
        self.Bt_FtData.clicked.connect(self.filtro_data_relatorio)
        self.tx_BuscaProdutos.textChanged.connect(self.pesquisar_produtos)
        self.tx_BuscaClientes.textChanged.connect(self.pesquisar_clientes)
        self.Input_Codigo.returnPressed.connect(self.focus_quantidade)


    ##### --- Função de Permissões de acesso --- #####
    def permissoes_visualizar(self):
        self.Bt_Add_Fornecedor.setDisabled(True)
        self.Bt_Remover_Fornecedor.setDisabled(True)
        self.Bt_Edit_Fornecedor.setDisabled(True)
        self.Bt_Add_Fornecedor.setDisabled(True)
        self.Bt_Excluir_Produto.setDisabled(True)
        self.Bt_Edit_Produto.setDisabled(True)
        self.Bt_Add_Produto.setDisabled(True)
        self.Bt_Excluir_Cliente.setDisabled(True)
        self.Bt_Edit_Cliente.setDisabled(True)
        self.Bt_Cad_Cliente.setDisabled(True)
        self.Bt_Usuarios.setDisabled(True)

    
    def focus_quantidade(self):
        self.Input_Quantidade.setFocus()


    def pesquisar_clientes(self):
        self.valor_consulta = self.tx_BuscaClientes.text()
        try:
            self.banco.conectar()
            self.banco.cursorr.execute(f"SELECT * FROM pdv.clientes WHERE nome LIKE '%{self.valor_consulta}%' or cpf LIKE '%{self.valor_consulta}%'")
            lista = self.banco.cursorr.fetchall()
            lista = list(lista)
            if not lista:
                return  self.alert.alerta_registro()     
            else:   
                self.TableWidget_Cliente.setRowCount(0)
                ###primeiro for trás###
                for idxLinha, linha in enumerate(lista):
                    self.TableWidget_Cliente.insertRow(idxLinha)
                    for idxColuna, coluna in enumerate(linha):
                        self.TableWidget_Cliente.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
            self.banco.query.commit()
            self.banco.query.close()
        except:
            pass
        
########## --- FITLTRO  RELATÓRIO VENDAS --- ########## 
    def pesquisa_cliente_relatorio(self):
        consulta_cliente_relatorio = self.Tx_cliente_relatorio.text()
   
        self.banco.conectar()
        self.banco.cursorr.execute(f"SELECT * FROM pdv.vendas WHERE cliente LIKE '%{consulta_cliente_relatorio}%'")
        lista = self.banco.cursorr.fetchall()
        lista = list(lista)
        if not lista:
            return  self.alert.alerta_registro()
        else:   
            self.TableWidget_Relatorio.setRowCount(0)
            for idxLinha, linha in enumerate(lista):
                self.TableWidget_Relatorio.insertRow(idxLinha)
                for idxColuna, coluna in enumerate(linha):
                    self.TableWidget_Relatorio.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
        self.banco.query.commit()
        self.banco.query.close()
        self.banco.cursorr.close()

    
    def pesquisa_n_venda_relatorio(self):
        consulta_n_venda_relatorio = self.Tx_Venda_relatorio.text()
        try:
            self.banco.conectar()
            self.banco.cursorr.execute(f"SELECT * FROM pdv.vendas WHERE idvendas LIKE '%{consulta_n_venda_relatorio}%'")
            lista = self.banco.cursorr.fetchall()
            lista = list(lista)
            if not lista:
                return  self.alert.alerta_registro()    
            else:   
                self.TableWidget_Relatorio.setRowCount(0)
                for idxLinha, linha in enumerate(lista):
                    self.TableWidget_Relatorio.insertRow(idxLinha)
                    for idxColuna, coluna in enumerate(linha):
                        self.TableWidget_Relatorio.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
            self.banco.query.commit()
            self.banco.query.close()
            self.banco.cursorr.close()
        except:
            pass
    

    def filtro_forma_pgmt_relatorio(self):
        consulta_frm_pgmt_relatorio = self.Tx_FiltroStatus.currentText()
        try:
            self.banco.conectar()
            self.banco.cursorr.execute(f"SELECT * FROM pdv.vendas WHERE tipo_venda LIKE '%{consulta_frm_pgmt_relatorio}%'")
            lista = self.banco.cursorr.fetchall()
            lista = list(lista)
            if not lista:
                return  self.alert.alerta_registro()    
            else:   
                self.TableWidget_Relatorio.setRowCount(0)
                for idxLinha, linha in enumerate(lista):
                    self.TableWidget_Relatorio.insertRow(idxLinha)
                    for idxColuna, coluna in enumerate(linha):
                        self.TableWidget_Relatorio.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
            self.banco.query.commit()
            self.banco.query.close()
            self.banco.cursorr.close()
        except:
            pass


    def filtro_data_relatorio(self):
        consulta_data_relatorio = self.Tx_FiltroData.text()
        try:
            self.banco.conectar()
            self.banco.cursorr.execute(f"SELECT * FROM pdv.vendas WHERE data LIKE '%{consulta_data_relatorio}%'")
            lista = self.banco.cursorr.fetchall()
            lista = list(lista)
            if not lista:
                return  self.alert.alerta_registro()    
            else:   
                self.TableWidget_Relatorio.setRowCount(0)
                for idxLinha, linha in enumerate(lista):
                    self.TableWidget_Relatorio.insertRow(idxLinha)
                    for idxColuna, coluna in enumerate(linha):
                        self.TableWidget_Relatorio.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
            self.banco.query.commit()
            self.banco.query.close()
            self.banco.cursorr.close()
        except:
            pass
        

    def pesquisa_operador_relatorio(self):
        consulta_operador_relatorio = self.Tx_Usuario_relatorio.text()
        try:
            self.banco.conectar()
            self.banco.cursorr.execute(f"SELECT * FROM pdv.vendas WHERE operador LIKE '%{consulta_operador_relatorio}%'")
            lista = self.banco.cursorr.fetchall()
            lista = list(lista)
            if not lista:
                return  self.alert.alerta_registro()    
            else:   
                self.TableWidget_Relatorio.setRowCount(0)
                for idxLinha, linha in enumerate(lista):
                    self.TableWidget_Relatorio.insertRow(idxLinha)
                    for idxColuna, coluna in enumerate(linha):
                        self.TableWidget_Relatorio.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
            self.banco.query.commit()
            self.banco.query.close()
            self.banco.cursorr.close()
        except:
            pass

    
    ######## --- Funções Listar listar Itens --- ######## 
    def listar_clientes(self):
        self.TableWidget_Cliente.verticalHeader().hide()
        col_widths = [50, 200, 100, 90, 90, 150, 77, 200, 60, 200, 150, 50, 100, 100]
        for i, width in enumerate(col_widths):
            self.TableWidget_Cliente.setColumnWidth(i, width)
        try:
            self.banco.conectar()
            self.banco.cursorr.execute("SELECT * FROM pdv.clientes")
            dados_lidosc = self.banco.cursorr.fetchall()
            self.TableWidget_Cliente.setRowCount(len(dados_lidosc))
            self.TableWidget_Cliente.setColumnCount(15)
            for a, dados in enumerate(dados_lidosc):
                for b, valor in enumerate(dados):
                    item = QtWidgets.QTableWidgetItem(str(valor))
                    self.TableWidget_Cliente.setItem(a, b, item)
            self.banco.query.commit()
            self.banco.cursorr.close()
        except:
            pass

        
    def listar_relatorio(self):
        self.TableWidget_Relatorio.verticalHeader().hide()
        try:
            self.banco.conectar()
            self.banco.cursorr.execute("SELECT * FROM pdv.vendas")
            dados_lidos = self.banco.cursorr.fetchall()
            self.TableWidget_Relatorio.setRowCount(len(dados_lidos))
            self.TableWidget_Relatorio.setColumnCount(6)
            for a, dados in enumerate(dados_lidos):
                for b, valor in enumerate(dados):
                    item = QtWidgets.QTableWidgetItem(str(valor))
                    self.TableWidget_Relatorio.setItem(a, b, item)
            self.banco.query.commit()
            self.banco.cursorr.close()
        except:
            pass

    
    def listar_produtos(self):
        self.TableWidget_Produto.verticalHeader().hide()
        self.TableWidget_Produto.verticalHeader().hide()
        # Ajuste de largura de coluna usando loop
        col_widths = [50, 200, 100, 90, 70, 90, 70, 70, 70, 85, 100,85]
        for i, width in enumerate(col_widths):
            self.TableWidget_Produto.setColumnWidth(i, width)
        try:
            self.banco.conectar()
            self.banco.cursorr.execute("SELECT * FROM pdv.produtos")
            dados_lidos = self.banco.cursorr.fetchall()
            # Defina o número de linhas uma vez
            self.TableWidget_Produto.setRowCount(len(dados_lidos))
            self.TableWidget_Produto.setColumnCount(12)
            for a, dados in enumerate(dados_lidos):
                for b, valor in enumerate(dados):
                    item = QtWidgets.QTableWidgetItem(str(valor))
                    self.TableWidget_Produto.setItem(a, b, item)
            self.banco.query.commit()
            self.banco.cursorr.close()
        except:
            pass

    
    def listar_usuarios(self):
        self.TableWidget_Usuario.verticalHeader().hide()
        try:
            self.banco.conectar()
            self.banco.cursorr.execute("SELECT idusuarios, nome, login, nivel_de_acesso, permissao FROM pdv.usuarios")
            dados_lidos = self.banco.cursorr.fetchall()
            self.TableWidget_Usuario.setRowCount(len(dados_lidos))
            self.TableWidget_Usuario.setColumnCount(5)
            for a, dados in enumerate(dados_lidos):
                for b, valor in enumerate(dados):
                    item = QtWidgets.QTableWidgetItem(str(valor))
                    self.TableWidget_Usuario.setItem(a, b, item)
            self.banco.query.commit()
            self.banco.cursorr.close()
            self.banco.query.close()
        except:
            pass
    

    def pesquisar_produtos(self):
        self.valor_consulta = self.tx_BuscaProdutos.text()
        try:
            self.banco.conectar()
            self.banco.cursorr.execute(f"SELECT * FROM pdv.produtos WHERE descricao LIKE '%{self.valor_consulta}%' or marca LIKE '%{self.valor_consulta}%'")
            lista = self.banco.cursorr.fetchall()
            lista = list(lista)
            if not lista:
                return  self.alert.alerta_registro()     
            else:   
                self.TableWidget_Produto.setRowCount(0)
                #primeiro for trás
                for idxLinha, linha in enumerate(lista):
                    self.TableWidget_Produto.insertRow(idxLinha)
                    for idxColuna, coluna in enumerate(linha):
                        self.TableWidget_Produto.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
            self.banco.query.commit()
            self.banco.query.close()
            self.banco.cursorr.close()
        except:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    systen = Classe_Inicio()
    systen.showMaximized()
    sys.exit(app.exec())