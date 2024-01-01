import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QFrame, QLabel, QVBoxLayout, QPushButton
from PyQt6 import QtWidgets, QtCore
import pandas as pd
from openpyxl import Workbook
from PyQt6.QtCore import Qt, pyqtSignal
from openpyxl.styles import Font, Alignment, PatternFill
import tkinter.filedialog
from form.Inicio.Form_Inicio import Ui_Form_Inicio
from funcoes.Banco.Conexao_banco import Classe_Banco
from funcoes.Alertas.Arquivo_Alertas import Classe_Alertas


class Classe_Inicio(QMainWindow, Ui_Form_Inicio):
    def __init__(self):
        super(Classe_Inicio, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()
        self.alert = Classe_Alertas()
        self.frame_table_mapping = {}

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.Tx_cliente_relatorio.textChanged.connect(self.pesquisa_cliente_relatorio)
        self.Tx_Usuario_relatorio.textChanged.connect(self.pesquisa_operador_relatorio)
        self.Tx_Venda_relatorio.textChanged.connect(self.pesquisa_n_venda_relatorio)
        self.Bt_Ft_Pagamento.clicked.connect(self.filtro_forma_pgmt_relatorio)
        self.Bt_FtData.clicked.connect(self.filtro_data_relatorio)
        self.tx_BuscaProdutos.textChanged.connect(self.pesquisar_produtos)
        self.tx_BuscaClientes.textChanged.connect(self.pesquisar_clientes)
        self.Bt_Excluir_Cliente.clicked.connect(self.excluir_clientes)
        self.Bt_Remover_Usuario.clicked.connect(self.excluir_usuarios)
        self.Bt_Excluir_Produto.clicked.connect(self.excluir_produtos)
        self.Bt_Sair.clicked.connect(self.fechar_tela_inicio)
        self.Bt_Imprimir_Atendimento.clicked.connect(self.imprimir_atendimento)
        self.tx_BuscaUsuarios.textChanged.connect(self.pesquisar_usuarios)
        self.Bt_Max_Jan.clicked.connect(self.maximizar_jan)
        self.Bt_Min_Jan.clicked.connect(self.minimizar_jan)
        self.Bt_Fechar_Jan.clicked.connect(self.fechar_tela_inicio)
    

    ######## --- Chama StakeWidgets --- ########
        self.Bt_Inicio.clicked.connect(self.tela_inicio)
        self.Bt_Produtos.clicked.connect(self.tela_produtos)
        self.Bt_Clientes.clicked.connect(self.tela_clientes)
        self.Bt_Relatorio.clicked.connect(self.tela_relatorio)
        self.Bt_Fornecedores.clicked.connect(self.tela_fornecedores)
        self.Bt_Usuarios.clicked.connect(self.tela_usuarios)
        self.Bt_Suporte.clicked.connect(self.tela_suporte)
        self.Bt_Mesas.clicked.connect(self.tela_mesa)
        self.frame_name.clicked.connect(self.teste)
        self.frame_lateral.enterEvent = lambda event: self.expaandir_left_menu()
        self.frame_lateral.leaveEvent  = lambda event: self.expaandir_left_menu()

    def teste(self):
        print('Ok.')   
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

    def tela_inicio(self):
        self.stackedWidget.setCurrentIndex(0)

    def tela_produtos(self):
        self.stackedWidget.setCurrentIndex(5)
        self.listar_produtos()

    def tela_clientes(self):
        self.stackedWidget.setCurrentIndex(4)
        self.listar_clientes()

    def tela_relatorio(self):
        self.stackedWidget.setCurrentIndex(2)
        self.listar_relatorio()

    def tela_fornecedores(self):
        self.stackedWidget.setCurrentIndex(6)

    def tela_mesa(self):
        self.stackedWidget.setCurrentIndex(3)
        self.frame_table_mapping.clear()
        for i in reversed(range(self.gridLayout_13.count())):
            item = self.gridLayout_13.takeAt(i)
            if item.widget():
                item.widget().setParent(None)
        self.init_ui()
    
    def tela_usuarios(self):
        self.stackedWidget.setCurrentIndex(7)
        self.listar_usuarios()

    def tela_suporte(self):
        self.stackedWidget.setCurrentIndex(8)


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


    def minimizar_jan(self):
        self.showMinimized()


    def maximizar_jan(self):
        self.showMaximized()

    
    def focus_codigo(self):
        self.Input_Codigo.setFocus()


    def pesquisar_clientes(self):
        self.valor_consulta = self.tx_BuscaClientes.text()
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
    

    def filtro_forma_pgmt_relatorio(self):
        consulta_frm_pgmt_relatorio = self.Tx_FiltroStatus.currentText()
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


    def filtro_data_relatorio(self):
        consulta_data_relatorio = self.Tx_FiltroData.text()
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
    

    def pesquisa_operador_relatorio(self):
        consulta_operador_relatorio = self.Tx_Usuario_relatorio.text()
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
    

    def pesquisar_produtos(self):
        self.valor_consulta = self.tx_BuscaProdutos.text()
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
    

    def pesquisar_usuarios(self):
        self.valor_consulta = self.tx_BuscaUsuarios.text()
        try:
            self.banco.conectar()
            self.banco.cursorr.execute(f"SELECT * FROM pdv.usuarios WHERE nome LIKE '%{self.valor_consulta}%' or login LIKE '%{self.valor_consulta}%'")
            lista = self.banco.cursorr.fetchall()
            lista = list(lista)
            if not lista:
                return  self.alert.alerta_registro()     
            else:   
                self.TableWidget_Usuario.setRowCount(0)
                #primeiro for trás
                for idxLinha, linha in enumerate(lista):
                    self.TableWidget_Usuario.insertRow(idxLinha)
                    for idxColuna, coluna in enumerate(linha):
                        self.TableWidget_Usuario.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
            self.banco.query.commit()
            self.banco.query.close()
        except:
            pass

    
    ######## --- Funções Listar listar Itens --- ######## 
    def listar_clientes(self):
        self.TableWidget_Cliente.verticalHeader().hide()
        col_widths = [50, 200, 100, 90, 90, 150, 77, 200, 60, 200, 150, 50, 100, 100]
        for i, width in enumerate(col_widths):
            self.TableWidget_Cliente.setColumnWidth(i, width)
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

        
    def listar_relatorio(self):
        self.TableWidget_Relatorio.verticalHeader().hide()
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

    
    def listar_produtos(self):
        self.TableWidget_Produto.verticalHeader().hide()
        col_widths = [50, 200, 100, 90, 70, 90, 70, 70, 100, 100, 100]
        for i, width in enumerate(col_widths):
            self.TableWidget_Produto.setColumnWidth(i, width)
        self.banco.conectar()
        self.banco.cursorr.execute("SELECT * FROM pdv.produtos")
        dados_lidos = self.banco.cursorr.fetchall()
        self.TableWidget_Produto.setRowCount(len(dados_lidos))
        self.TableWidget_Produto.setColumnCount(11)
        for a, dados in enumerate(dados_lidos):
            for b, valor in enumerate(dados):
                item = QtWidgets.QTableWidgetItem(str(valor))
                self.TableWidget_Produto.setItem(a, b, item)
        self.banco.query.commit()
        self.banco.cursorr.close()

    
    def listar_usuarios(self):
        self.TableWidget_Usuario.verticalHeader().hide()
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
    

    ######## --- Funções Remover Itens --- ######## 
    def excluir_usuarios(self):
        selected_row = self.TableWidget_Usuario.currentRow()
        if selected_row >= 0:
            self.id_usuarios = int(self.TableWidget_Usuario.item(selected_row, 0).text())
            self.TableWidget_Usuario.removeRow(selected_row)
            self.banco.conectar()
            delete_query = f"DELETE FROM pdv.usuarios WHERE idusuarios = {self.id_usuarios}"
            self.banco.cursorr.execute(delete_query)
            self.banco.query.commit()
            self.banco.cursorr.close()
            self.banco.query.close()
            self.tx_BuscaUsuarios.clear()
            self.listar_usuarios()

    
    def excluir_clientes(self):
        selected_row = self.TableWidget_Cliente.currentRow()
        if selected_row >= 0:
            self.id_clientes = int(self.TableWidget_Cliente.item(selected_row, 0).text())
            self.TableWidget_Cliente.removeRow(selected_row)
            self.banco.conectar()
            delete_query = f"DELETE FROM pdv.clientes WHERE idclientes = {self.id_clientes}"
            self.banco.cursorr.execute(delete_query)
            self.banco.query.commit()
            self.banco.cursorr.close()
            self.banco.query.close()
            self.tx_BuscaClientes.clear()
            self.listar_clientes()
    

    def excluir_produtos(self):
        selected_row = self.TableWidget_Produto.currentRow()
        if selected_row >= 0:
            self.id_produtos = int(self.TableWidget_Produto.item(selected_row, 0).text())
            self.TableWidget_Produto.removeRow(selected_row)
            self.banco.conectar()
            delete_query = f"DELETE FROM pdv.produtos WHERE idprodutos = {self.id_produtos}"
            self.banco.cursorr.execute(delete_query)
            self.banco.query.commit()
            self.banco.cursorr.close()
            self.banco.query.close()
            self.tx_BuscaProdutos.clear()
            self.listar_produtos()


    ##### --- Função de  Expandir o menu lateral --- ######
    def expaandir_left_menu(self):
        tamanho = self.frame_lateral.width()
        if tamanho == 100:
            novo_tamanho = 50
            self.Bt_Clientes.setText("")
            self.Bt_Mesas.setText("")
            self.Bt_Inicio.setText("")
            self.Bt_Produtos.setText("")
            self.Bt_Sair.setText("")
            self.Bt_Suporte.setText("")
            self.Bt_Fornecedores.setText("")
            self.Bt_Usuarios.setText("")
            self.Bt_Relatorio.setText("")
            self.Bt_Vendas.setText("")
        else:
            novo_tamanho = 100
            self.Bt_Inicio.setText('Inicio')
            self.Bt_Clientes.setText("Clientes")
            self.Bt_Fornecedores.setText("Fornecedores")
            self.Bt_Produtos.setText("Produtos")
            self.Bt_Mesas.setText("Mesas")  
            self.Bt_Vendas.setText("Pdv")
            self.Bt_Usuarios.setText("Usuários")
            self.Bt_Relatorio.setText("Relatório")
            self.Bt_Suporte.setText("Suporte")
            self.Bt_Sair.setText("Sair")
        self.animacao = QtCore.QPropertyAnimation(self.frame_lateral,  b"maximumWidth")
        self.animacao.setStartValue(tamanho)
        self.animacao.setEndValue(novo_tamanho)
        self.animacao.setDuration(390)
        self.animacao.start()  

    
    def focus_codigo(self):
        self.Input_Codigo.setFocus()

    
    def imprimir_atendimento(self):
        try:
            data = {}
            headers = []
            for col in range(self.TableWidget_Relatorio.columnCount()):
                header_text = self.TableWidget_Relatorio.horizontalHeaderItem(col).text()
                headers.append(header_text)
                data[header_text] = [self.TableWidget_Relatorio.item(row, col).text() for row in range(self.TableWidget_Relatorio.rowCount())]
            df = pd.DataFrame.from_dict(data)
            local_salvar = tkinter.filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
            workbook = Workbook()
            sheet = workbook.active
            sheet.append(headers)  #### --- Adiciona o cabeçalho à planilha --- ###
            for row in df.itertuples(index=False):
                sheet.append(row)
            for col_index, column_cells in enumerate(sheet.columns, start=1):
                max_length = max(len(str(cell.value)) for cell in column_cells)
                adjusted_width = (max_length + 2) * 1.2
                sheet.column_dimensions[sheet.cell(row=1, column=col_index).column_letter].width = adjusted_width
            for row in sheet.iter_rows(min_row=1, max_row=1):
                for cell in row:
                    cell.font = Font(bold=True)
                    cell.fill = PatternFill(fill_type='solid', fgColor='AAAAAA')
                    cell.alignment = Alignment(horizontal='center', vertical='center')
            for row in sheet.iter_rows(min_row=2):
                for cell in row:
                    cell.alignment = Alignment(horizontal='center', vertical='center')
            workbook.save(local_salvar)
            self.alert.alerta_salvar_relatorio()
        except:
            self.alert.alerta_erro_salvar_relatorio()


    def fechar_tela_inicio(self):
        self.close() 


    def init_ui(self):
        
        self.add_frames_with_labels(30)  # Adiciona 3 frames com labels inicialmente (para teste)
        # Verifica e define as cores iniciais com base no conteúdo das tabelas
        self.check_table_contents()
        

    def add_frames_with_labels(self, num_frames):
        for i in range(num_frames):
            frame = QFrame(self.Frame_Principal)
            frame_name = f'frame_mesa{i+1}'
            frame.setObjectName(frame_name)  # Adiciona um nome único para cada frame
            frame.setStyleSheet("""background-color: rgb(255, 255, 255);
                                border-radius:15px;""")
            
            frame.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)  # Define o estilo inicial
            frame.setMaximumSize(QtCore.QSize(196, 146))

            layout = QVBoxLayout(frame)

            label_mesa = QLabel(f'Mesa{i+1:02d}', frame)
            label_mesa.setStyleSheet('font: 14pt "MS Shell Dlg 2";')  # Gera o nome dinâmico (Mesa01, Mesa02, ...)

            label_status = QLabel('Livre', frame)
            label_status.setObjectName('label_status')  # Adiciona um nome à label_status
            label_status.setStyleSheet("""color: rgb(0, 170, 127);
                                        font: 75 14pt "MS Shell Dlg 2";""")
            
            self.button_detalhes = QPushButton('Detalhes', frame)
            self.button_detalhes.setObjectName(f'button_detalhes_{i+1}')  # Adiciona um nome único para cada botão
            self.button_detalhes.setStyleSheet("""QPushButton{
                                        background-color: rgb(162, 162, 162);
                                        font: 8pt "MS Shell Dlg 2";
                                        font-size:12px;
                                        border-radius:10px;
                                        }
                                        QPushButton:hover{
                                        background-color: #505050;
                                        }""")
            self.button_detalhes.setMaximumSize(QtCore.QSize(85, 25))
            self.button_detalhes.setMinimumSize(QtCore.QSize(85, 25))

            # Conecta o sinal clicked do botão à função on_button_click
            self.button_detalhes.clicked.connect(self.on_button_click)

            layout.addWidget(label_mesa, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label_status, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(self.button_detalhes, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)  # Botão na parte inferior

            # Adiciona o frame e as labels na próxima célula da grade
            row, col = divmod(i, 10)  # Duas colunas para cada linha
            self.gridLayout_13.addWidget(frame, row, col)

            # Mapeia o nome do frame ao nome da tabela correspondente
            table_name = f'mesa{i+1}'
            self.frame_table_mapping[frame_name] = table_name

    def on_button_click(self):
        sender = self.sender()  # Obtém o objeto que emitiu o sinal (o botão clicado)
        frame_name = sender.parent().objectName()  # Obtém o nome do frame pai do botão
        table_name = self.frame_table_mapping.get(frame_name)

        if table_name:
            # Aqui você pode adicionar o código que deseja executar em resposta ao clique do botão
            print(f'Botão clicado no frame {frame_name}. Correspondente à tabela {table_name} no banco de dados.')

    def check_table_contents(self):
        # Verifica o conteúdo de cada tabela e define a cor com base nisso
        for frame_name, table_name in self.frame_table_mapping.items():
            if self.table_has_data(table_name):
                self.set_frame_color(frame_name, 'red')
                self.update_label_status(frame_name, 'Ocupado')
                self.update()
            else:
                self.set_frame_color(frame_name, 'green')
                self.update_label_status(frame_name, 'Livre')
                self.update()

        # Atualiza o layout para garantir que as alterações sejam refletidas
        

    def table_has_data(self, table_name):
        # Simulação: Verifica se a tabela tem dados (substitua com seu código real)
        self.banco.conectar()
        self.banco.cursorr.execute(f"SELECT COUNT(*) FROM pdv.{table_name}")
        row_count = self.banco.cursorr.fetchone()[0]
        self.banco.cursorr.close()
        self.banco.query.close()
        return row_count > 0

    def set_frame_color(self, frame_name, color):
        # Define a cor do frame
        frame = self.findChild(QFrame, frame_name)
        if frame:
            frame.setStyleSheet(f"background-color: {color}; border-radius:15px;")

    def update_label_status(self, frame_name, status_text):
        # Atualiza o texto da label_status
        frame = self.findChild(QFrame, frame_name)
        if frame:
            label_status = frame.findChild(QLabel, 'label_status')
            if label_status:
                label_status.setText(status_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    systen = Classe_Inicio()
    systen.showMaximized()
    sys.exit(app.exec())