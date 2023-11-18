from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QKeySequence, QShortcut, QPixmap
import datetime
import sys
import subprocess
from fpdf import FPDF
from PyQt6.QtGui import QKeySequence
import requests
import webbrowser
from form.Login.Janela_Login import Classe_Login
from form.Inicio.Janela_Inicio import Classe_Inicio
from form.Usuario.Janela_Cad_Usuario import Classe_Cad_Usuario
from form.Usuario.Janela_Edit_Usuario import Classe_Edit_Usuario
from funcoes.Banco.Conexao_banco import Classe_Banco
from form.Cliente.Janela_Cad_Cliente import Classe_Cad_Cliente
from form.Cliente.Janela_Edit_Cliente import Classe_Edit_Cliente
from form.Produto.Jane_Cad_Produto import Classe_Cad_Produto
from form.Produto.Jan_Edit_Produto import Classe_Edit_Produto
from form.Empresa.Janela_Consulta_Cnpj import Classe_Consulta_Cnpj
from form.Chama_Venda.Janela_Chama_Venda import Classe_Chama_Venda
from form.Comanda.Janela_Comanda import Classe_Comanda
from form.Venda_Mesa.Janela_Chama_Venda import Classe_Venda_Mesa
from form.Finaliza_Venda.Janela_Chama_Venda import Classe_Finaliza_Venda
from form.Finaliza_Venda.Janela_Chama_Venda_nota import Classe_Finaliza_Venda_CLiente
from form.Finaliza_Venda.Janela_Chama_Comprovante import Classe_Comprovante
from form.Finaliza_Venda.Janela_Lista_Cliente import Classe_Lista_Cliente
from form.Finaliza_Venda.Janela_Chama_Comprovante_Nota import Classe_Comprovante_Nota


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.login = Classe_Login()
        self.inicio = Classe_Inicio()
        self.cad_usuario = Classe_Cad_Usuario()
        self.edit_usuario = Classe_Edit_Usuario()
        self.banco = Classe_Banco()
        self.cad_cliente = Classe_Cad_Cliente()
        self.edit_cliente = Classe_Edit_Cliente()
        self.cad_produto = Classe_Cad_Produto()
        self.edit_produto = Classe_Edit_Produto()
        self.consulta_cnpj = Classe_Consulta_Cnpj()
        self.escolha_vendas = Classe_Chama_Venda()
        self.comanda = Classe_Comanda()
        self.venda_mesa = Classe_Venda_Mesa()
        self.jan_fecha_venda = Classe_Finaliza_Venda()
        self.jan_comprovante = Classe_Comprovante()
        self.Jan_lista_cliente = Classe_Lista_Cliente()
        self.jan_fecha_venda_nota = Classe_Finaliza_Venda_CLiente()
        self.jan_comprovante_nota = Classe_Comprovante_Nota()
        
         
        self.listar_prod_venda_Mesa()


######## --- Chama Telas --- ########
        self.login.Bt_Login.clicked.connect(self.verifica_login)
        self.login.Bt_check.clicked.connect(self.password_check)
        self.login.Tx_Senha.returnPressed.connect(self.verifica_login)
        self.login.Tx_Usuario.returnPressed.connect(self.seleciona_password)
        self.inicio.Bt_Sair.clicked.connect(self.fechar_tela_inicio)
        self.inicio.Bt_Add_Usuario.clicked.connect(self.cham_cad_usuario)
        self.inicio.Bt_Edit_Usuario.clicked.connect(self.chama_edit_usuario)
        self.inicio.Bt_Cad_Cliente.clicked.connect(self.chama_cad_cliente)
        self.inicio.Bt_Edit_Cliente.clicked.connect(self.chama_edit_cliente)
        self.inicio.Bt_Add_Produto.clicked.connect(self.chama_cad_produto)
        self.inicio.Bt_Edit_Produto.clicked.connect(self.chama_edit_produto)
        self.inicio.Bt_Edit_Cliente.clicked.connect(self.chama_edit_cliente)
        self.cad_produto.Bt_SalvarProdutos.clicked.connect(self.inserir_produtos)
        self.edit_produto.Bt_SalvarProdutos.clicked.connect(self.salvar_produto_editados)
        self.edit_cliente.bt_Salvar.clicked.connect(self.salvar_cliente_editado)
        self.consulta_cnpj.Bt_Consultar_Cnpj.clicked.connect(self.consulta_pj)
        self.consulta_cnpj.Tx_Cnpj.returnPressed.connect(self.consulta_pj)
        self.cad_cliente.Bt_Salvar.clicked.connect(self.inserir_clientes)
        self.cad_usuario.bt_SalvarUsuario.clicked.connect(self.inserir_usuarios)
        self.inicio.Bt_Whatsapp_2.clicked.connect(self.abre_link_whatsapp)
        self.cad_cliente.tx_Cep.returnPressed.connect(self.busca_cep)
        self.inicio.Bt_Add_Fornecedor.clicked.connect(self.chama_consulta_cnpj)
        self.inicio.frame_lateral.enterEvent = lambda event: self.expaandir_left_menu()
        self.inicio.frame_lateral.leaveEvent  = lambda event: self.expaandir_left_menu()
        self.inicio.Bt_Excluir_Cliente.clicked.connect(self.excluir_clientes)
        self.inicio.Bt_Remover_Usuario.clicked.connect(self.excluir_usuarios)
        self.inicio.Bt_Excluir_Produto.clicked.connect(self.excluir_produtos)
        self.inicio.Bt_Vendas.clicked.connect(self.chama_vendas)
        self.inicio.Bt_Mesa01.clicked.connect(self.chama_comanda)
        self.escolha_vendas.Bt_Venda_Mesa.clicked.connect(self.chama_venda_mesa)
        self.venda_mesa.lineEdit_4.returnPressed.connect(self.tela_prod)
        self.venda_mesa.Bt_Venda.clicked.connect(self.tela_vend)
        self.venda_mesa.tableWidget_Prod.doubleClicked.connect(self.add_prod_venda)
        self.inicio.tx_BuscaUsuarios.textChanged.connect(self.pesquisar_usuarios)
        self.inicio.tx_BuscaClientes.textChanged.connect(self.pesquisar_clientes)
        self.Jan_lista_cliente.tx_BuscaClientes_Venda.textChanged.connect(self.pesquisar_clientes_venda)
        self.inicio.tx_BuscaProdutos.textChanged.connect(self.pesquisar_produtos)
        self.inicio.Input_Codigo.returnPressed.connect(self.focus_quantidade)
        self.inicio.Input_Quantidade.returnPressed.connect(self.adicionar_prod_carrinho)
        self.inicio.Bt_IncluirProduto.clicked.connect(self.adicionar_prod_carrinho)
        self.inicio.Bt_Finalizar_venda.clicked.connect(self.abrir_finaliza_venda)
        self.jan_fecha_venda.Bt_Confirmar_Vanda.clicked.connect(self.confirmar_venda)
        self.jan_fecha_venda.Input_ValorPago.returnPressed.connect(self.confirmar_venda)
        self.cad_produto.bt_AddImagem.clicked.connect(self.inserir_img_produto)
        self.edit_produto.bt_AddImagem.clicked.connect(self.editar_img_produto)
        self.jan_comprovante.Bt_Imprimir.clicked.connect(self.criar_cupom_fiscal)
        self.jan_comprovante.Bt_NovaVenda.clicked.connect(self.nova_vanda)
        self.jan_comprovante_nota.Bt_NovaVenda.clicked.connect(self.nova_vanda)
        self.jan_fecha_venda.Cb_FormaPagamento.currentIndexChanged.connect(self.verificar_selecao)
        self.Jan_lista_cliente.tableWidget_cliente.doubleClicked.connect(self.seleciona_cliente_nota)
        self.Jan_lista_cliente.Bt_SelecionaCliente.clicked.connect(self.seleciona_cliente_nota)
        self.jan_fecha_venda_nota.Bt_Confirmar_Vanda.clicked.connect(self.adiciona_credito_utilizado)
        self.jan_comprovante_nota.Bt_Imprimir.clicked.connect(self.criar_cupom_fiscal_nota)
        self.jan_comprovante_nota.Bt_Cancela_venda.clicked.connect(self.nova_vanda)
        

        shortcut = QShortcut(QKeySequence('F5'), self.inicio.Vendas)
        shortcut.activated.connect(self.abrir_finaliza_venda)
        
        shortcut = QShortcut(QKeySequence('F5'), self.jan_fecha_venda)
        shortcut.activated.connect(self.chama_jan_comprovante)

        shortcut = QShortcut(QKeySequence('Esc'), self.jan_fecha_venda)
        shortcut.activated.connect(self.fecha_jan_venda)

        shortcut = QShortcut(QKeySequence('F1'), self.jan_comprovante)
        shortcut.activated.connect(self.criar_cupom_fiscal)

        shortcut = QShortcut(QKeySequence('F2'), self.jan_comprovante)
        shortcut.activated.connect(self.nova_vanda)

        shortcut = QShortcut(QKeySequence('Delete'), self.inicio.TableWidget_Venda)
        shortcut.activated.connect(self.remove_linha_tb_venda)

        shortcut = QShortcut(QKeySequence('F2'), self.jan_fecha_venda)
        shortcut.activated.connect(self.chama_lista_cliente)
    

######## --- Chama StakeWidgets --- ########
        self.inicio.Bt_Inicio.clicked.connect(
        lambda: self.inicio.stackedWidget.setCurrentWidget(self.tela_inicio()))
        self.tela_inicio()

        self.carrinho = []

        self.total_compra = 0.0
       
    def verificar_selecao(self):
        item_selecionado = self.jan_fecha_venda.Cb_FormaPagamento.currentText()
        if item_selecionado == "Nota":
            self.Jan_lista_cliente.show()
            self.chama_lista_cliente()
        elif item_selecionado == "Dinheiro":
            pass
        elif item_selecionado == "Cartão":
            pass
        elif item_selecionado == "Pix":
            pass
        elif item_selecionado == "Cheque":
            pass
        else:
            self.alerta_pagamento()


    def alerta_pagamento(self):
        msg = QMessageBox()
        msg.setWindowTitle("Atenção!")
        msg.setText("Selecione o tipo de pagamento!")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec() 


    def expaandir_left_menu(self):
        tamanho = self.inicio.frame_lateral.width()
        if tamanho == 100:
            novo_tamanho = 50
            self.inicio.Bt_Clientes.setText("")
            self.inicio.Bt_Mesas.setText("")
            self.inicio.Bt_Inicio.setText("")
            self.inicio.Bt_Produtos.setText("")
            self.inicio.Bt_Sair.setText("")
            self.inicio.Bt_Suporte.setText("")
            self.inicio.Bt_Fornecedores.setText("")
            self.inicio.Bt_Usuarios.setText("")
            self.inicio.Bt_Vendas.setText("")
        else:
            novo_tamanho = 100
            self.inicio.Bt_Inicio.setText('Inicio')
            self.inicio.Bt_Clientes.setText("Clientes")
            self.inicio.Bt_Fornecedores.setText("Fornecedores")
            self.inicio.Bt_Produtos.setText("Produtos")
            self.inicio.Bt_Mesas.setText("Mesas")  
            self.inicio.Bt_Vendas.setText("Pdv")
            self.inicio.Bt_Usuarios.setText("Usuários")
            self.inicio.Bt_Suporte.setText("Suporte")
            self.inicio.Bt_Sair.setText("Sair")
        self.animacao = QtCore.QPropertyAnimation(self.inicio.frame_lateral,  b"maximumWidth")
        self.animacao.setStartValue(tamanho)
        self.animacao.setEndValue(novo_tamanho)
        self.animacao.setDuration(390)
        self.animacao.start()    


    def tela_inicio(self):
        self.inicio.Bt_Inicio.clicked.connect(
        lambda: self.inicio.stackedWidget.setCurrentWidget(self.inicio.inicio))

        
        self.inicio.Bt_Clientes.clicked.connect(
        lambda: self.inicio.stackedWidget.setCurrentWidget(self.tela_usuarios()))   
        self.tela_clientes()

    def tela_clientes(self):
        self.inicio.Bt_Clientes.clicked.connect(
        lambda: self.inicio.stackedWidget.setCurrentWidget(self.inicio.clientes))
        self.listar_clientes()

        self.inicio.Bt_Produtos.clicked.connect(
        lambda: self.inicio.stackedWidget.setCurrentWidget(self.tela_produtos()))
        self.tela_produtos()

    def tela_produtos(self):
        self.inicio.Bt_Produtos.clicked.connect(
        lambda: self.inicio.stackedWidget.setCurrentWidget(self.inicio.produtos))
        self.listar_produtos()
    
        self.escolha_vendas.Bt_Venda_Balcao.clicked.connect(
        lambda: self.inicio.stackedWidget.setCurrentWidget(self.tela_vendas()))
        self.tela_vendas()
        

    def tela_vendas(self):
        self.escolha_vendas.Bt_Venda_Balcao.clicked.connect(
        lambda: self.inicio.stackedWidget.setCurrentWidget(self.inicio.Vendas))
        self.escolha_vendas.close()
        self.focus_codigo()
        

        self.inicio.Bt_Usuarios.clicked.connect(
        lambda: self.inicio.stackedWidget.setCurrentWidget(self.tela_usuarios()))   
        self.tela_usuarios()

    def tela_usuarios(self):
        self.inicio.Bt_Usuarios.clicked.connect(
        lambda: self.inicio.stackedWidget.setCurrentWidget(self.inicio.usuarios))
        self.listar_usuarios()


        self.inicio.Bt_Suporte.clicked.connect(
        lambda: self.inicio.stackedWidget.setCurrentWidget(self.tela_suporte()))
        self.tela_suporte()

    def tela_suporte(self):
        self.inicio.Bt_Suporte.clicked.connect(
            lambda: self.inicio.stackedWidget.setCurrentWidget(self.inicio.suporte))
        
        
        self.inicio.Bt_Fornecedores.clicked.connect(
            lambda: self.inicio.stackedWidget.setCurrentWidget(self.tela_fornecedores()))
        self.tela_fornecedores()
        
    def tela_fornecedores(self):
        self.inicio.Bt_Fornecedores.clicked.connect(
            lambda: self.inicio.stackedWidget.setCurrentWidget(self.inicio.fornecedores))
        

        self.inicio.Bt_Mesas.clicked.connect(
            lambda:self.inicio.stackedWidget.setCurrentWidget(self.inicio.Mesa))
        
    def tela_mesa(self):
        self.inicio.Bt_Mesas.clicked.connect(
            lambda:self.inicio.stackedWidget.setCurrentWidget(self.inicio.Mesa))
        
        self.venda_mesa.lineEdit_4.returnPressed.connect(
        lambda: self.venda_mesa.stackedWidget.setCurrentWidget(self.tela_prod()))
        self.tela_prod()

    def tela_prod(self):
        self.venda_mesa.lineEdit_4.returnPressed.connect(
        lambda: self.venda_mesa.stackedWidget.setCurrentWidget(self.venda_mesa.Produtos))
        self.listar_prod_venda_Mesa()

    
        self.venda_mesa.Bt_Venda.clicked.connect(
        lambda: self.venda_mesa.stackedWidget.setCurrentWidget(self.tela_vend()))
        self.tela_vend()
        

    def tela_vend(self):
        self.venda_mesa.Bt_Venda.clicked.connect(
        lambda: self.venda_mesa.stackedWidget.setCurrentWidget(self.venda_mesa.Venda))


    def nova_vanda(self):
        self.inicio.TableWidget_Venda.setRowCount(0)
        self.inicio.Input_Codigo.clear() 
        self.inicio.Input_Quantidade.clear()
        self.inicio.label_total.setText("0.00")
        self.inicio.Lb_fotoCarrinho.clear()
        self.jan_fecha_venda.Input_ValorPago.clear()
        self.jan_fecha_venda.Lb_Troco.setText('0,00')
        self.jan_fecha_venda.Cb_FormaPagamento.setCurrentIndex(0)
        self.inicio.Lb_Nome_Produto.clear()
        self.jan_comprovante.close()
        self.jan_comprovante_nota.close()
        self.jan_fecha_venda.close()
        self.focus_codigo()


    def adicionar_prod_carrinho(self):
        try:
            input_cod = self.inicio.Input_Codigo.text()
            quantidade = self.inicio.Input_Quantidade.text()
            # Verifique se o código e a quantidade são válidos
            if not input_cod or not quantidade:
                return 
            # Simule a busca do produto usando o código
            produto_encontrado = self.buscar_produto(input_cod)
            if produto_encontrado:
                codigo, descricao, valor = produto_encontrado
                quantidade = int(quantidade)
                valor_unitario = valor
                valor_total = quantidade * valor
                # Adicione o produto à tabela
                row_position = self.inicio.TableWidget_Venda.rowCount()
                self.inicio.TableWidget_Venda.insertRow(row_position)
                self.inicio.TableWidget_Venda.setItem(row_position, 0, QTableWidgetItem(codigo))
                self.inicio.TableWidget_Venda.setItem(row_position, 1, QTableWidgetItem(descricao))
                self.inicio.TableWidget_Venda.setItem(row_position, 2, QTableWidgetItem(str(quantidade)))
                self.inicio.TableWidget_Venda.setItem(row_position, 3, QTableWidgetItem(f'R${valor_unitario:.2f}'))
                self.inicio.TableWidget_Venda.setItem(row_position, 4, QTableWidgetItem(f'R${valor_total:.2f}'))
                self.inicio.Lb_fotoCarrinho.setPixmap(QPixmap(str(self.img_prd_carr)))
                self.inicio.Lb_Nome_Produto.setText(str(descricao))
                self.atualizar_valor_total()
            else:
                self.alerta_registro()
        except:
            self.alerta_valor_invalido()


    def fecha_jan_venda(self):
        self.jan_fecha_venda.close()   


    def remove_linha_tb_venda(self):
        selected_row = self.inicio.TableWidget_Venda.currentRow()
        if selected_row >= 0:
            self.inicio.TableWidget_Venda.removeRow(selected_row)
            self.inicio.Lb_fotoCarrinho.clear()
            
            self.inicio.Input_Codigo.clear()
            self.inicio.Input_Quantidade.clear()
            self.inicio.Input_Codigo.setFocus()
            self.atualizar_valor_total()
        else:
            self.alt_remover_linha()
            

    def buscar_produto(self, input_cod):
        try:
            self.banco.conectar()
            self.banco.cursorr.execute("SELECT * FROM pdv.produtos")
            dados_lidos = self.banco.cursorr.fetchall()
            lista_de_dados = list(dados_lidos)
            self.produtos = []
            self.banco.query.commit()
            self.banco.query.close()
            for item in lista_de_dados:
                codigo = item[5]
                descricao = item[1]
                valor = float(item[6])
                self.img_prd_carr = item[10]
                item_transformado = {"codigo": codigo, "descricao": descricao, "valor": valor}
                self.produtos.append(item_transformado)
            
                for produto in self.produtos:
                        if produto['codigo'] == input_cod:
                            return produto['codigo'], produto['descricao'], produto['valor']
        except:
            self.alt_campo_invalido()

    def focus_quantidade(self):
        self.inicio.Input_Quantidade.setFocus()

    def focus_codigo(self):
        self.inicio.Input_Codigo.setFocus()

    
    def atualizar_valor_total(self):
        self.total = 0
        for row in range(self.inicio.TableWidget_Venda.rowCount()):
            self.valor_total = float(self.inicio.TableWidget_Venda.item(row, 4).text()[2:])
            self.total += self.valor_total
            self.inicio.label_total.setText(str(f"{self.total:.2f}"))
        self.focus_codigo()
        

    def abrir_finaliza_venda(self):
        try:
            self.valor_total_venda = self.jan_fecha_venda.Lb_TotalPagar.setText(str(f'{self.total:.2f}'))
            self.jan_fecha_venda.show()
            self.jan_fecha_venda.Lb_Troco.clear()
            self.jan_fecha_venda.Input_ValorPago.clear()
        except:
            self.alt_insirir_produto()    
    
      
    def confirmar_venda(self):
        try:
            self.valor_pago = float(self.jan_fecha_venda.Input_ValorPago.text())
            valor_total = float(self.jan_fecha_venda.Lb_TotalPagar.text())
            self.troco = float(self.valor_pago - valor_total)
            self.jan_fecha_venda.Lb_Troco.setText(f'{self.troco:.2f}')
            self.forma_pagamento = self.jan_fecha_venda.Cb_FormaPagamento.currentText() 
        except:
            self.valor_invalido()
       

    def chama_jan_comprovante(self):
        self.fecha_jan_venda()
        self.jan_comprovante.show() 

        
    def criar_cupom_fiscal(self):
        try:
            self.banco.conectar()
            self.banco.cursorr.execute("SELECT * FROM pdv.empresa")
            dadoslisdos_empresa = self.banco.cursorr.fetchall()
            razao_social = dadoslisdos_empresa[0][1]
            cnpj = dadoslisdos_empresa[0][2]
            endereco = dadoslisdos_empresa[0][6]
            data = datetime.date.today()
            data_formatada = data.strftime("%d/%m/%Y")
            hora = datetime.datetime.now().time()
            hora_formatada = hora.strftime("%H:%M")

            lista = []
            for linha in range(self.inicio.TableWidget_Venda.rowCount()):
                linha_lista = []
                for coluna in range(self.inicio.TableWidget_Venda.columnCount()):
                    item = self.inicio.TableWidget_Venda.item(linha, coluna)
                    linha_lista.append(item.text())
                lista.append(linha_lista)
            # Inicialize a lista de itens transformados aqui
            itens_transformados = []
            for item in lista:
                codigo = item[0]
                descricao = item[1]
                quantidade = item[2]
                # Remova o "R$" e converta o preço para um float
                preco = float(item[3].replace("R$", "").strip())
                total = item[4]
                item_transformado = {"codigo": codigo, "descricao": descricao, "quantidade": quantidade, "preco": preco, "total": total}
                itens_transformados.append(item_transformado)
            # Especificar o tamanho da página ao criar o objeto FPDF
            largura = 100  # Largura em milímetros
            altura = 297  # Altura em milímetros
            pdf = FPDF(format=(largura, altura))
            pdf.add_page()
            # Configuração da fonte e tamanho
            pdf.set_font("Arial", size=8)
            pdf.cell(45, 5, txt= (f"{str(razao_social)}"), ln=True)
            pdf.cell(45, 5, txt=(f"{cnpj}"), ln=True)
            pdf.cell(45, 5, txt=(f"{endereco}"), ln=True)
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.cell(45, 5, txt=(f"{data_formatada}"), ln=True)
            pdf.cell(45, 5, txt=(f"{hora_formatada}"), ln=True)
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.cell(80, 10, txt="Cupom Fiscal", ln=True, align='C')
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.ln()
            # Cabeçalho da tabela
            pdf.cell(12, 7, txt="Código")
            pdf.cell(45, 7, txt="Descrição")
            pdf.cell(10, 7, txt="Qtd.")
            pdf.cell(10, 7, txt="Val. Un.")
            pdf.ln()   
            # Itens da lista
            for item in itens_transformados:
                pdf.cell(12, 7, txt=item['codigo'])
                pdf.cell(45, 7, txt=item['descricao'])
                pdf.cell(10, 7, txt=item['quantidade'])
                pdf.cell(10, 7, txt="R$: {:.2f}".format(item['preco']))
                pdf.ln()
            # Total
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.ln()
            total = sum(float(item['preco']) for item in itens_transformados)
            pdf.cell(10, 5, txt="Total:")
            pdf.cell(40, 5, txt=f"R$ {self.valor_total}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Valor Pago: R$ {self.valor_pago}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Troco: R$ {self.troco}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Forma de pagamento: {self.forma_pagamento}")
            pdf.ln()
            pdf.cell(45, 5, txt="-----------------------------------------------------------------------------------", ln=True)  
            # Rodapé
            pdf.cell(80, 10, txt="Obrigado por sua compra!", ln=True, align='C')    
            # Salvar o arquivo PDF
            pdf.output("nome_arquivo.pdf")
            caminho_pdf = "nome_arquivo.pdf"
            # Abrir o arquivo PDF com o leitor de PDF padrão
            subprocess.Popen([caminho_pdf], shell=True)
        except:
            razao_social = " RAZÃO SOCIAL NÃO DEFINIDO"
            cnpj = "CNPJ NÃO DEFINIDO"
            endereco = "ENDEREÇO NÃO DEFINIDO"
            data = datetime.date.today()
            data_formatada = data.strftime("%d/%m/%Y")
            hora = datetime.datetime.now().time()
            hora_formatada = hora.strftime("%H:%M")

            lista = []
            for linha in range(self.inicio.TableWidget_Venda.rowCount()):
                linha_lista = []
                for coluna in range(self.inicio.TableWidget_Venda.columnCount()):
                    item = self.inicio.TableWidget_Venda.item(linha, coluna)
                    linha_lista.append(item.text())
                lista.append(linha_lista)
            # Inicialize a lista de itens transformados aqui
            itens_transformados = []
            for item in lista:
                codigo = item[0]
                descricao = item[1]
                quantidade = item[2]
                # Remova o "R$" e converta o preço para um float
                preco = float(item[3].replace("R$", "").strip())
                total = item[4]
                item_transformado = {"codigo": codigo, "descricao": descricao, "quantidade": quantidade, "preco": preco, "total": total}
                itens_transformados.append(item_transformado)
            # Especificar o tamanho da página ao criar o objeto FPDF
            largura = 100  # Largura em milímetros
            altura = 297  # Altura em milímetros
            pdf = FPDF(format=(largura, altura))
            pdf.add_page()
            # Configuração da fonte e tamanho
            pdf.set_font("Arial", size=8)
            pdf.cell(45, 5, txt= (f"{str(razao_social)}"), ln=True)
            pdf.cell(45, 5, txt=(f"{cnpj}"), ln=True)
            pdf.cell(45, 5, txt=(f"{endereco}"), ln=True)
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.cell(45, 5, txt=(f"{data_formatada}"), ln=True)
            pdf.cell(45, 5, txt=(f"{hora_formatada}"), ln=True)
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.cell(80, 10, txt="Cupom Fiscal", ln=True, align='C')
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.ln()
            # Cabeçalho da tabela
            pdf.cell(12, 7, txt="Código")
            pdf.cell(45, 7, txt="Descrição")
            pdf.cell(10, 7, txt="Qtd.")
            pdf.cell(10, 7, txt="Val. Un.")
            pdf.ln()   
            # Itens da lista
            for item in itens_transformados:
                pdf.cell(12, 7, txt=item['codigo'])
                pdf.cell(45, 7, txt=item['descricao'])
                pdf.cell(10, 7, txt=item['quantidade'])
                pdf.cell(10, 7, txt="R$: {:.2f}".format(item['preco']))
                pdf.ln()
            # Total
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.ln()
            total = sum(float(item['preco']) for item in itens_transformados)
            pdf.cell(10, 5, txt="Total:")
            pdf.cell(40, 5, txt=f"R$ {self.total:.2f}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Valor Pago: R$ {self.valor_pago:.2f}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Troco: R$ {self.troco:.2f}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Forma de pagamento: {self.forma_pagamento}")
            pdf.ln()
            pdf.cell(45, 5, txt="-----------------------------------------------------------------------------------", ln=True)  
            # Rodapé
            pdf.cell(80, 10, txt="Obrigado por sua compra!", ln=True, align='C')    
            # Salvar o arquivo PDF
            pdf.output("nome_arquivo.pdf")
            caminho_pdf = "nome_arquivo.pdf"
            # Abrir o arquivo PDF com o leitor de PDF padrão
            subprocess.Popen([caminho_pdf], shell=True)

    
    def criar_cupom_fiscal_nota(self):
        try:
            self.banco.conectar()
            self.banco.cursorr.execute("SELECT * FROM pdv.empresa")
            dadoslisdos_empresa = self.banco.cursorr.fetchall()
            razao_social = dadoslisdos_empresa[0][1]
            cnpj = dadoslisdos_empresa[0][2]
            endereco = dadoslisdos_empresa[0][6]
            data = datetime.date.today()
            data_formatada = data.strftime("%d/%m/%Y")
            hora = datetime.datetime.now().time()
            hora_formatada = hora.strftime("%H:%M")

            lista = []
            for linha in range(self.inicio.TableWidget_Venda.rowCount()):
                linha_lista = []
                for coluna in range(self.inicio.TableWidget_Venda.columnCount()):
                    item = self.inicio.TableWidget_Venda.item(linha, coluna)
                    linha_lista.append(item.text())
                lista.append(linha_lista)
            # Inicialize a lista de itens transformados aqui
            itens_transformados = []
            for item in lista:
                codigo = item[0]
                descricao = item[1]
                quantidade = item[2]
                # Remova o "R$" e converta o preço para um float
                preco = float(item[3].replace("R$", "").strip())
                total = item[4]
                item_transformado = {"codigo": codigo, "descricao": descricao, "quantidade": quantidade, "preco": preco, "total": total}
                itens_transformados.append(item_transformado)
            # Especificar o tamanho da página ao criar o objeto FPDF
            largura = 100  # Largura em milímetros
            altura = 297  # Altura em milímetros
            pdf = FPDF(format=(largura, altura))
            pdf.add_page()
            # Configuração da fonte e tamanho
            pdf.set_font("Arial", size=8)
            pdf.cell(45, 5, txt= (f"{str(razao_social)}"), ln=True)
            pdf.cell(45, 5, txt=(f"{cnpj}"), ln=True)
            pdf.cell(45, 5, txt=(f"{endereco}"), ln=True)
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.cell(45, 5, txt=(f"{data_formatada}"), ln=True)
            pdf.cell(45, 5, txt=(f"{hora_formatada}"), ln=True)
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.cell(80, 10, txt="Cupom Fiscal", ln=True, align='C')
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.ln()
            # Cabeçalho da tabela
            pdf.cell(12, 7, txt="Código")
            pdf.cell(45, 7, txt="Descrição")
            pdf.cell(10, 7, txt="Qtd.")
            pdf.cell(10, 7, txt="Val. Un.")
            pdf.ln()   
            # Itens da lista
            for item in itens_transformados:
                pdf.cell(12, 7, txt=item['codigo'])
                pdf.cell(45, 7, txt=item['descricao'])
                pdf.cell(10, 7, txt=item['quantidade'])
                pdf.cell(10, 7, txt="R$: {:.2f}".format(item['preco']))
                pdf.ln()
            # Total
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.ln()
            total = sum(float(item['preco']) for item in itens_transformados)
            pdf.cell(10, 5, txt="Total:")
            pdf.cell(40, 5, txt=f"R$ {self.total:.2f}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Valor Pago: R$ {self.valor_pago:.2f}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Troco: R$ {self.troco:.2f}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Forma de pagamento: {self.forma_pagamento_nota}")
            pdf.ln()
            pdf.cell(45, 5, txt="-----------------------------------------------------------------------------------", ln=True)  
            # Rodapé
            pdf.cell(80, 10, txt="Obrigado por sua compra!", ln=True, align='C')    
            # Salvar o arquivo PDF
            pdf.output("nome_arquivo.pdf")
            caminho_pdf = "nome_arquivo.pdf"
            # Abrir o arquivo PDF com o leitor de PDF padrão
            subprocess.Popen([caminho_pdf], shell=True)
        except:
            razao_social = " RAZÃO SOCIAL NÃO DEFINIDO"
            cnpj = "CNPJ NÃO DEFINIDO"
            endereco = "ENDEREÇO NÃO DEFINIDO"
            data = datetime.date.today()
            data_formatada = data.strftime("%d/%m/%Y")
            hora = datetime.datetime.now().time()
            hora_formatada = hora.strftime("%H:%M")

            lista = []
            for linha in range(self.inicio.TableWidget_Venda.rowCount()):
                linha_lista = []
                for coluna in range(self.inicio.TableWidget_Venda.columnCount()):
                    item = self.inicio.TableWidget_Venda.item(linha, coluna)
                    linha_lista.append(item.text())
                lista.append(linha_lista)
            # Inicialize a lista de itens transformados aqui
            itens_transformados = []
            for item in lista:
                codigo = item[0]
                descricao = item[1]
                quantidade = item[2]
                # Remova o "R$" e converta o preço para um float
                preco = float(item[3].replace("R$", "").strip())
                total = item[4]
                item_transformado = {"codigo": codigo, "descricao": descricao, "quantidade": quantidade, "preco": preco, "total": total}
                itens_transformados.append(item_transformado)
            # Especificar o tamanho da página ao criar o objeto FPDF
            largura = 100  # Largura em milímetros
            altura = 297  # Altura em milímetros
            pdf = FPDF(format=(largura, altura))
            pdf.add_page()
            # Configuração da fonte e tamanho
            pdf.set_font("Arial", size=8)
            pdf.cell(45, 5, txt= (f"{str(razao_social)}"), ln=True)
            pdf.cell(45, 5, txt=(f"{cnpj}"), ln=True)
            pdf.cell(45, 5, txt=(f"{endereco}"), ln=True)
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.cell(45, 5, txt=(f"{data_formatada}"), ln=True)
            pdf.cell(45, 5, txt=(f"{hora_formatada}"), ln=True)
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.cell(80, 10, txt="Cupom Fiscal", ln=True, align='C')
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.ln()
            # Cabeçalho da tabela
            pdf.cell(12, 7, txt="Código")
            pdf.cell(45, 7, txt="Descrição")
            pdf.cell(10, 7, txt="Qtd.")
            pdf.cell(10, 7, txt="Val. Un.")
            pdf.ln()   
            # Itens da lista
            for item in itens_transformados:
                pdf.cell(12, 7, txt=item['codigo'])
                pdf.cell(45, 7, txt=item['descricao'])
                pdf.cell(10, 7, txt=item['quantidade'])
                pdf.cell(10, 7, txt="R$: {:.2f}".format(item['preco']))
                pdf.ln()
            # Total
            pdf.cell(45, 3, txt="-----------------------------------------------------------------------------------", ln=True)
            pdf.ln()
            total = sum(float(item['preco']) for item in itens_transformados)
            pdf.cell(10, 5, txt="Total:")
            pdf.cell(40, 5, txt=f"R$ {self.total}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Forma de pagamento: {self.forma_pagamento_nota}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Cliente: {self.cliente_selecionado}")
            pdf.ln()
            pdf.ln()
            # Rodapé
            pdf.cell(45, 5, txt="-----------------------------------------------------------------------------------", ln=True)  
            pdf.cell(40, 5, txt=f"                                         Assinatura                    ")
            pdf.ln()
            pdf.cell(80, 10, txt="Obrigado por sua compra!", ln=True, align='C')    
            # Salvar o arquivo PDF
            pdf.output("nome_arquivo.pdf")
            caminho_pdf = "nome_arquivo.pdf"
            # Abrir o arquivo PDF com o leitor de PDF padrão
            subprocess.Popen([caminho_pdf], shell=True)


######## --- Função de validação de usuário --- ########   
    def verifica_login(self):
        try:
            login = self.login.Tx_Usuario.text()
            senha2 = self.login.Tx_Senha.text()
            self.banco.conectar()
            self.banco.cursorr.execute(
            "SELECT senha1, nivel_de_acesso FROM pdv.usuarios WHERE login ='{}'".format(login))
            senha_db = self.banco.cursorr.fetchall()        
            try:
                if senha2 == senha_db[0][0] and (senha_db[0][1]) == 'ADMINISTRADOR':
                    self.login.carregar()
                    self.login.hide()           
                    self.inicio.showMaximized() 
                    self.inicio.Lb_User_Logado.setText(login)
                    self.banco.query.close()
                elif senha2 == senha_db[0][0] and (senha_db[0][1]) == 'USUÁRIO':
                    self.login.carregar()
                    self.login.hide()        
                    self.inicio.showMaximized()
                    self.permissoes_visualizar()
                    self.banco.query.close()
                else:
                    self.login.Lb_Info.setText("Dados de login incorretos!")    
                    self.banco.query.close()
            except:
                self.login.Lb_Info.setText("Dados de login incorretos!")           
                self.banco.query.close()
        except:
            self.login.Lb_Info_banco.setText("Erro ao conectar ao banco de dados!")
            self.banco.query.close()

    def seleciona_password(self):
        self.login.Tx_Senha.setFocus()

    def password_check(self):      
        bt = self.login.Bt_check.sender()
        if bt.isChecked() == True:
            self.login.Tx_Senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:    
            self.login.Tx_Senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  

######## --- Funções chamada de telas --- ########
    def chama_tela_inicio(self):
        self.user_logado = self.login.Tx_Usuario.text()
        self.login.hide()
        self.inicio.show()
        self.inicio.label.setText(self.user_logado)

    def chama_cad_cliente(self):
        self.cad_cliente.show()

    def cham_cad_usuario(self):
        self.cad_usuario.show()
    
    def chama_edit_usuario(self):
        self.edit_usuario.show()

    def chama_cad_produto(self):
        self.cad_produto.show()

    def chama_consulta_cnpj(self):
        self.consulta_cnpj.show()

    def chama_vendas(self):
        self.escolha_vendas.show()
        self.nova_vanda()
    
    def chama_lista_cliente(self):
        self.Jan_lista_cliente.show()
        self.listar_cliente_venda()
        
    def chama_edit_produto(self):
        linha = self.inicio.TableWidget_Produto.currentRow()
        self.banco.conectar()
        self.banco.cursorr.execute("SELECT idprodutos FROM pdv.produtos")
        dados_lidos = self.banco.cursorr.fetchall()
        self.valor_id_editproduto = dados_lidos[linha][0]
        self.banco.cursorr.execute("SELECT * FROM pdv.produtos WHERE idprodutos=" + str(self.valor_id_editproduto)) 
        produto = self.banco.cursorr.fetchall()
        self.edit_produto.show()  
        self.edit_produto.tx_DescricaoProduto.setText(str(produto[0][1]))
        self.edit_produto.cb_CategoriaProduto.setCurrentIndex(0)
        self.edit_produto.tx_Marca.setText(str(produto[0][3]))
        self.edit_produto.tx_Estoque.setText(str(produto[0][4]))
        self.edit_produto.tx_Codigo.setText(str(produto[0][5]))
        self.edit_produto.tx_Preco_Produto.setText(str(produto[0][6]))
        self.edit_produto.tx_Venda_Varejo.setText(str(produto[0][7]))
        self.edit_produto.tx_Venda_Atacado.setText(str(produto[0][8]))
        self.edit_produto.tx_MinimoAtacado.setText(str(produto[0][9]))
        self.edit_produto.Tx_Data_Cadastro.setText(str(produto[0][10]))
        self.edit_produto.Tx_Validade.setText(str(produto[0][11]))
        self.edit_produto.lb_FotoProduto.setPixmap(QPixmap(str(produto[0][12])))
        self.banco.query.commit()
        self.banco.query.close()


    def chama_edit_cliente(self):
        linha = self.inicio.TableWidget_Cliente.currentRow()
        self.banco.conectar()
        self.banco.cursorr.execute("SELECT idclientes FROM pdv.clientes")
        dados_lidos = self.banco.cursorr.fetchall()
        self.valor_id_editcliente = dados_lidos[linha][0]
        self.banco.cursorr.execute("SELECT * FROM pdv.clientes WHERE idclientes=" + str(self.valor_id_editcliente)) 
        produto = self.banco.cursorr.fetchall()
        self.edit_cliente.show()  
        self.edit_cliente.tx_Nome.setText(str(produto[0][1]))
        self.edit_cliente.tx_Rg.setText(str(produto[0][3]))
        self.edit_cliente.tx_Cpf.setText(str(produto[0][2]))
        self.edit_cliente.tx_Telefone.setText(str(produto[0][4]))
        self.edit_cliente.tx_Email.setText(str(produto[0][5]))
        self.edit_cliente.tx_Cep.setText(str(produto[0][6]))
        self.edit_cliente.tx_Endereco.setText(str(produto[0][7]))
        self.edit_cliente.tx_Numero.setText(str(produto[0][8]))
        self.edit_cliente.tx_Bairro.setText(str(produto[0][9]))
        self.edit_cliente.tx_Cidade.setText(str(produto[0][10]))
        self.edit_cliente.tx_Estado.setText(str(produto[0][11]))
        self.edit_cliente.tx_Credito.setText(str(produto[0][12]))
        self.banco.query.commit()
        self.banco.query.close()
        

    def permissoes_visualizar(self):
        self.inicio.Bt_Add_Fornecedor.setDisabled(True)
        self.inicio.Bt_Remover_Fornecedor.setDisabled(True)
        self.inicio.Bt_Edit_Fornecedor.setDisabled(True)
        self.inicio.Bt_Add_Fornecedor.setDisabled(True)
        self.inicio.Bt_Excluir_Produto.setDisabled(True)
        self.inicio.Bt_Edit_Produto.setDisabled(True)
        self.inicio.Bt_Add_Produto.setDisabled(True)
        self.inicio.Bt_Excluir_Cliente.setDisabled(True)
        self.inicio.Bt_Edit_Cliente.setDisabled(True)
        self.inicio.Bt_Cad_Cliente.setDisabled(True)
        self.inicio.Bt_Usuarios.setDisabled(True)
        

    def salvar_produto_editados(self):
        # Valor digitado no lineEdit
        try:
            self.banco.conectar()
            codigo = self.edit_produto.tx_Codigo.text()
            descricao = self.edit_produto.tx_DescricaoProduto.text()
            categoria = self.edit_produto.tx_AddCategoria.text()
            marca = self.edit_produto.tx_AddMarca.text()
            estoque = self.edit_produto.tx_EstoqueMinimoProduto.text()
            preco = self.edit_produto.tx_Preco.text()
            v_varejo = self.edit_produto.tx_ValorVarejoProduto.text()
            v_atacado = self.edit_produto.tx_ValorAtacadoProduto.text()
            minimo_atacado = self.edit_produto.tx_MinimoAtacado.text()
            imagem = self.conteudo_edit_produto[0]
            # Atualizar os dados no banco  
            self.banco.cursorr.execute("UPDATE pdv.produtos SET codigo = '{}', descricao  = '{}', preco = '{}', estoque ='{}', categoria = '{}', marca = '{}', v_varejo = '{}', v_atacado = '{}', qm_atacado = '{}', imagem = '{}'  WHERE idprodutos = {}".format(
                codigo, descricao, preco, estoque, categoria, marca, v_varejo, v_atacado, minimo_atacado, str(imagem) ,self.valor_id_editproduto))
            self.banco.query.commit()
            self.banco.query.close()
            self.listar_produtos()
            self.alerta_produto_editado()
        except:
            self.banco.conectar()
            codigo = self.edit_produto.tx_Codigo.text()
            descricao = self.edit_produto.tx_DescricaoProduto.text()
            categoria = self.edit_produto.tx_AddCategoria.text()
            marca = self.edit_produto.tx_AddMarca.text()
            estoque = self.edit_produto.tx_EstoqueMinimoProduto.text()
            preco = self.edit_produto.tx_Preco.text()
            v_varejo = self.edit_produto.tx_ValorVarejoProduto.text()
            v_atacado = self.edit_produto.tx_ValorAtacadoProduto.text()
            minimo_atacado = self.edit_produto.tx_MinimoAtacado.text()
            # Atualizar os dados no banco  
            self.banco.cursorr.execute("UPDATE pdv.produtos SET codigo = '{}', descricao  = '{}', preco = '{}', estoque ='{}', categoria = '{}', marca = '{}', v_varejo = '{}', v_atacado = '{}', qm_atacado = '{}' WHERE idprodutos = {}".format(
                codigo, descricao, preco, estoque, categoria, marca, v_varejo, v_atacado, minimo_atacado, self.valor_id_editproduto))
            self.banco.query.commit()
            self.banco.query.close()
            self.alerta_produto_editado()
            self.listar_produtos()


    def alerta_produto_editado(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Produto editado!")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec()


    def salvar_cliente_editado(self):
        # Valor digitado no lineEdit
            self.banco.conectar()
            nome = self.edit_cliente.tx_Nome.text()
            rg = self.edit_cliente.tx_Rg.text()
            cpf = self.edit_cliente.tx_Cpf.text()
            telefone = self.edit_cliente.tx_Telefone.text()
            email = self.edit_cliente.tx_Email.text()
            cep = self.edit_cliente.tx_Cep.text()
            endereco = self.edit_cliente.tx_Endereco.text()
            numero = self.edit_cliente.tx_Numero.text()
            bairro = self.edit_cliente.tx_Bairro.text()
            cidade = self.edit_cliente.tx_Cidade.text()
            estado = self.edit_cliente.tx_Estado.text()
            credito = self.edit_cliente.tx_Credito.text()
            # Atualizar os dados no banco  
            self.banco.cursorr.execute("UPDATE pdv.clientes SET nome = '{}', rg  = '{}', cpf = '{}', telefone ='{}', email = '{}', cep = '{}', endereco = '{}', numero = '{}', bairro = '{}', cidade = '{}', estado = '{}', credito = '{}'  WHERE idclientes = {}".format(
                nome, rg, cpf, telefone, email, cep, endereco, numero, bairro, cidade, estado, credito, self.valor_id_editcliente))
            self.banco.query.commit()
            self.banco.query.close()
            self.listar_clientes()
            self.alerta_cliente_editado()


    def alerta_cliente_editado(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Cliente editado!")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec() 


    def fechar_tela_inicio(self):
        self.inicio.close()   


######## --- Funções Inserir itens --- ########    
    def inserir_produtos(self):
        descricao = self.cad_produto.tx_DescricaoProduto.text()
        codigo = self.cad_produto.tx_Codigo.text()
        categoria = self.cad_produto.cb_CategoriaProduto.currentText()
        marca = self.cad_produto.tx_Marca.text()
        estoque = self.cad_produto.tx_Estoque.text()    
        preco = self.cad_produto.tx_Preco_Produto.text()
        v_varejo = self.cad_produto.tx_Venda_Varejo.text()
        v_atacado = self.cad_produto.tx_Venda_Atacado.text()
        qtd_atacado = self.cad_produto.tx_MinimoAtacado.text()
        self.banco.conectar()
        try:
            self.banco.cursorr.execute("INSERT INTO pdv.produtos (descricao,codigo,categoria,marca,estoque,preco,v_varejo,v_atacado,qm_atacado, imagem) VALUES('" +
                        descricao+"','"+codigo+"','"+categoria+"','"+marca+"','"+estoque+"','"+preco+"','"+v_varejo+"','"+v_atacado+"','"+qtd_atacado+"', '"+str(self.file_paths[0])+"')")
            self.banco.query.commit()
            self.banco.query.close()
            self.cad_produto.limpa_campos()
            self.alerta_produto_cadastrado()
            self.listar_produtos()  
        except:
            self.banco.cursorr.execute("INSERT INTO pdv.produtos (descricao,codigo,categoria,marca,estoque,preco,v_varejo,v_atacado,qm_atacado) VALUES('" +
                        descricao+"','"+codigo+"','"+categoria+"','"+marca+"','"+estoque+"','"+preco+"','"+v_varejo+"','"+v_atacado+"','"+qtd_atacado+"')")
            self.banco.query.commit()
            self.banco.query.close()
            self.cad_produto.limpa_campos()
            self.alerta_produto_cadastrado()
            self.listar_produtos()


    def inserir_img_produto(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Escolher Imagem")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm *.tif *.tiff);;Todos os Arquivos (*)")
        file_dialog.exec()
        self.file_paths = file_dialog.selectedFiles()
        self.cad_produto.lb_FotoProduto.setPixmap(QPixmap(self.file_paths[0]))


    def editar_img_produto(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Escolher Imagem")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm *.tif *.tiff);;Todos os Arquivos (*)")
        file_dialog.exec()
        self.conteudo_edit_produto = file_dialog.selectedFiles()
        self.edit_produto.lb_FotoProduto.setPixmap(QPixmap(self.conteudo_edit_produto[0]))
    

    def alerta_produto_cadastrado(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Produto cadastrado!")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec()


    def inserir_clientes(self):
        nome = self.cad_cliente.tx_Nome.text()
        rg = self.cad_cliente.tx_rg.text()
        cpf = self.cad_cliente.tx_cpf.text()
        telefone = self.cad_cliente.tx_Telefone.text()
        email = self.cad_cliente.tx_Email.text()
        cep = self.cad_cliente.tx_Cep.text()
        endereco = self.cad_cliente.tx_Endereco.text()
        numero = self.cad_cliente.tx_Numero.text()
        bairro = self.cad_cliente.tx_Bairro.text()
        cidade = self.cad_cliente.tx_Cidade.text()
        estado = self.cad_cliente.tx_Estado.text()
        credito = self.cad_cliente.tx_Credito.text()
        self.banco.conectar()
        self.banco.cursorr.execute("INSERT INTO pdv.clientes (nome,rg,cpf,telefone,email,cep,endereco,numero,bairro,cidade,estado,credito) VALUES('" +
                    nome+"','"+rg+"','"+cpf+"','"+telefone+"','"+email+"','"+cep+"','"+endereco+"','"+numero+"','"+bairro+"','"+cidade+"','"+estado+"', '"+credito+"')")
        self.banco.query.commit()
        self.banco.query.close()
        self.listar_clientes()
        self.cad_cliente.limpar_campos()
        

    def inserir_usuarios(self):
        nome =  self.cad_usuario.tx_nome.text()
        login = self.cad_usuario.tx_Login.text()
        senha1 = self.cad_usuario.tx_Senha.text()
        senha2 = self.cad_usuario.tx_Senha2.text()
        nivel_acesso = self.cad_usuario.cb_Nivel_Acesso.currentText()
        permissao =  self.cad_usuario.cb_Permissoes.currentText()
        self.banco.conectar()
        if nome == "":
            self.alt_cad_em_branco()
        elif login == "":
                self.alt_cad_em_branco()
        elif senha1 == "":
                self.alt_cad_em_branco()
        elif senha2 == "":
                self.alt_cad_em_branco()
        elif nivel_acesso == "SELECIONE":
                self.alt_erro_cad_nivel_acesso()
        elif permissao == "SELECIONE":
                self.alt_erro_cad_permissao()
        elif senha1!= senha2:
                self.alt_senha_diferente()
        else:
            self.banco.cursorr.execute("INSERT INTO pdv.usuarios (nome,login,senha1,senha2,nivel_de_acesso,permissao) VALUES('"+nome+"','"+
                    login+"','"+senha1+"','"+senha2+"','"+nivel_acesso+"','"+permissao+"')")
            self.banco.query.commit()
            self.banco.query.close()
            self.alt_cadastro_sucesso()
            self.listar_usuarios()


    def alt_erro_cad_nivel_acesso(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Selecione um Nível de Acesso do Usuário!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_erro_cad_permissao(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Selecione as Permissões de Acesso do Usuário!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_cad_em_branco(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Complete os Campos em Branco!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_senha_diferente(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("As Senhas Estão Diferentes!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_insirir_produto(self):
        msg = QMessageBox()
        msg.setWindowTitle("Atenção!")
        msg.setText("Insira um produto")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def valor_invalido(self):
        msg = QMessageBox()
        msg.setWindowTitle("Atenção!")
        msg.setText("Insira um valor válido, utilize ponto no lugar da vírgula")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_remover_linha(self):
        msg = QMessageBox()
        msg.setWindowTitle("Atenção!")
        msg.setText("Selecione um produto para remover")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
        
    def alt_campo_invalido(self):
        msg = QMessageBox()
        msg.setWindowTitle("Verifique!")
        msg.setText("Algum campo do produto buscado pode está incorreto.")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_cadastro_sucesso(self):
        msg = QMessageBox()
        msg.setWindowTitle("Parabéns!")
        msg.setText("Usuário Cadastrado Com Sucesso!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
        self.cad_usuario.tx_nome.clear()
        self.cad_usuario.tx_Login.clear()
        self.cad_usuario.tx_Senha.clear()
        self.cad_usuario.tx_Senha2.clear()
        self.cad_usuario.cb_Nivel_Acesso.setCurrentIndex(0)
        self.cad_usuario.cb_Permissoes.setCurrentIndex(0)


######## --- Funções Listar listar Itens --- ######## 
    def listar_produtos(self):
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


    def listar_clientes(self):
        self.inicio.TableWidget_Cliente.setColumnWidth(0,50)
        self.inicio.TableWidget_Cliente.setColumnWidth(1,200)
        self.inicio.TableWidget_Cliente.setColumnWidth(2,100)
        self.inicio.TableWidget_Cliente.setColumnWidth(3,90)
        self.inicio.TableWidget_Cliente.setColumnWidth(4,90)
        self.inicio.TableWidget_Cliente.setColumnWidth(5,150)
        self.inicio.TableWidget_Cliente.setColumnWidth(6,77)
        self.inicio.TableWidget_Cliente.setColumnWidth(7,200)
        self.inicio.TableWidget_Cliente.setColumnWidth(8,60)
        self.inicio.TableWidget_Cliente.setColumnWidth(9,200)
        self.inicio.TableWidget_Cliente.setColumnWidth(10,150)
        self.inicio.TableWidget_Cliente.setColumnWidth(11,50)
        self.inicio.TableWidget_Cliente.setColumnWidth(13,100)
        self.inicio.TableWidget_Cliente.setColumnWidth(14,100)
        self.inicio.TableWidget_Cliente.verticalHeader().hide()
        self.banco.conectar()
        self.banco.cursorr.execute("SELECT * FROM pdv.clientes")
        dados_lidosc = self.banco.cursorr.fetchall()
        self.inicio.TableWidget_Cliente.setRowCount(len(dados_lidosc))
        self.inicio.TableWidget_Cliente.setColumnCount(15)
        for a in range(0, len(dados_lidosc)):
            for b in range(0, 15):
                self.inicio.TableWidget_Cliente.setItem(
                    a, b, QtWidgets.QTableWidgetItem(str(dados_lidosc[a][b])))
        self.banco.query.commit()

    
    def listar_cliente_venda(self):
        self.Jan_lista_cliente.tableWidget_cliente.setColumnWidth(0,50)
        self.Jan_lista_cliente.tableWidget_cliente.setColumnWidth(1,150)
        self.Jan_lista_cliente.tableWidget_cliente.setColumnWidth(2,85)
        self.Jan_lista_cliente.tableWidget_cliente.setColumnWidth(3,85)
        self.Jan_lista_cliente.tableWidget_cliente.setColumnWidth(4,170)
        self.Jan_lista_cliente.tableWidget_cliente.setColumnWidth(5,75)
        self.Jan_lista_cliente.tableWidget_cliente.setColumnWidth(6,75)
        self.Jan_lista_cliente.tableWidget_cliente.setColumnWidth(7,75)
        self.banco.conectar()
        self.banco.cursorr.execute("SELECT idclientes, nome, cpf, rg, endereco, credito, credito_utilizado, credito_saldo FROM pdv.clientes")
        dados_lidosc = self.banco.cursorr.fetchall()
        self.Jan_lista_cliente.tableWidget_cliente.setRowCount(len(dados_lidosc))
        self.Jan_lista_cliente.tableWidget_cliente.setColumnCount(8)
        for a in range(0, len(dados_lidosc)):
            for b in range(0, 8):
                self.Jan_lista_cliente.tableWidget_cliente.setItem(
                    a, b, QtWidgets.QTableWidgetItem(str(dados_lidosc[a][b])))
        self.banco.query.commit()


    def listar_prod_venda_Mesa(self):
        self.venda_mesa.tableWidget_Prod.verticalHeader().hide()
        self.banco.conectar()
        self.banco.cursorr.execute("SELECT idprodutos, descricao, preco FROM pdv.produtos")
        dados_lidos = self.banco.cursorr.fetchall()
        self.venda_mesa.tableWidget_Prod.setRowCount(len(dados_lidos))
        self.venda_mesa.tableWidget_Prod.setColumnCount(3)
        for a in range(0, len(dados_lidos)):
            for b in range(0, 3):
                self.venda_mesa.tableWidget_Prod.setItem(
                    a, b, QtWidgets.QTableWidgetItem(str(dados_lidos[a][b])))
        self.banco.query.commit()
        self.banco.query.close()


    def busca_cep(self):
        cep1 = self.cad_cliente.tx_Cep.text()
        cep = cep1.replace("-", "")
        link = (f'https://viacep.com.br/ws/{cep}/json/' )
        try:
            requisicao1 = requests.get(link)
            requisicao = (requisicao1.json())
            self.cad_cliente.tx_Cidade.setText(requisicao['localidade'])
            self.cad_cliente.tx_Bairro.setText(requisicao['bairro'])
            self.cad_cliente.tx_Endereco.setText(requisicao['logradouro'])
            self.cad_cliente.tx_Estado.setText(requisicao['uf'])
        except:
            self.alt_cep_invalido()


    def alt_cep_invalido(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("O Cep está inválido!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()    

    def listar_usuarios(self):
        self.inicio.TableWidget_Usuario.verticalHeader().hide()
        self.banco.conectar()
        self.banco.cursorr.execute("SELECT idusuarios, nome, login, nivel_de_acesso, permissao FROM pdv.usuarios")
        dados_lidos = self.banco.cursorr.fetchall()
        self.inicio.TableWidget_Usuario.setRowCount(len(dados_lidos))
        self.inicio.TableWidget_Usuario.setColumnCount(5)
        for a in range(0, len(dados_lidos)):
            for b in range(0,5):
                self.inicio.TableWidget_Usuario.setItem(
                    a, b, QtWidgets.QTableWidgetItem(str(dados_lidos[a][b])))
                
                
######## --- Funções Remover Itens --- ######## 
    def excluir_clientes(self):
        self.banco.conectar()
        linha = self.inicio.TableWidget_Cliente.currentRow()
        self.inicio.TableWidget_Cliente.removeRow(linha)
    ###Remover no banco###
        self.banco.cursorr.execute("SELECT idclientes FROM pdv.clientes")
        dados_lidos = self.banco.cursorr.fetchall()
        valor_id = dados_lidos[linha][0]
        self.banco.cursorr.execute("DELETE FROM pdv.clientes WHERE idclientes =" + str(valor_id))
        self.banco.query.commit()
        self.banco.query.close()
        self.listar_clientes()


    def excluir_usuarios(self):
        self.banco.conectar()
        linha = self.inicio.TableWidget_Usuario.currentRow()
        self.inicio.TableWidget_Usuario.removeRow(linha)
    ###Remover no banco###
        self.banco.cursorr.execute("SELECT idusuarios FROM pdv.usuarios")
        dados_lidos = self.banco.cursorr.fetchall()
        valor_id = dados_lidos[linha][0]
        self.banco.cursorr.execute("DELETE FROM pdv.usuarios WHERE idusuarios =" + str(valor_id))
        self.banco.query.commit()
        self.banco.query.close()
        self.listar_usuarios()


    def excluir_produtos(self):
        self.banco.conectar()
        linha = self.inicio.TableWidget_Produto.currentRow()
        self.inicio.TableWidget_Produto.removeRow(linha)
    ###Remover no banco###
        self.banco.cursorr.execute("SELECT idprodutos FROM pdv.produtos")
        dados_lidos = self.banco.cursorr.fetchall()
        valor_id = dados_lidos[linha][0]
        self.banco.cursorr.execute("DELETE FROM pdv.produtos WHERE idprodutos =" + str(valor_id))
        self.banco.query.commit()
        self.banco.query.close()
        self.listar_produtos()
        

    def consulta_pj(self):
        try:
            session = requests.Session()
            cnpj1 = self.consulta_cnpj.Tx_Cnpj.text()
            cnpj = cnpj1.replace(".", "").replace("/", "").replace("-","")
            url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
            querystring = {"token":"C9A237E3-F452-440B-AC4D-74C354D7761B","cnpj": cnpj, "plugin":"RF"}
            response = session.request("GET", url, params=querystring)
            resp = response.json()
            self.consulta_cnpj.tx_Nome.setText(resp['fantasia'])
            self.consulta_cnpj.tx_Email.setText(resp['email'])
            self.consulta_cnpj.tx_Telefone.setText(resp['telefone'])
            self.consulta_cnpj.txLogradouro.setText(resp['logradouro'])
            self.consulta_cnpj.tx_Cep.setText(resp['cep'])
            self.consulta_cnpj.tx_Bairro.setText(resp['bairro'])
            self.consulta_cnpj.tx_municipio.setText(resp['municipio'])
            self.consulta_cnpj.tx_Uf.setText(resp['uf'])
            self.consulta_cnpj.tx_Numero.setText(resp['numero'])
        except:
            self.alt_cnpj_invalido()


    def alt_cnpj_invalido(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Cnpj Inválido!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()   
    

    def abre_link_whatsapp(self):
        webbrowser.open_new_tab('https://contate.me/lcinformtica')


    def chama_venda_mesa(self):
        self.venda_mesa.show()
        self.escolha_vendas.close()


    def chama_comanda(self):
        self.comanda.show()


    def add_prod_venda(self):
        row_data = []
        for column in range(self.venda_mesa.tableWidget.columnCount()):
            cell = self.venda_mesa.tableWidget_Prod.item(column)
            row_data.append(cell)
        print(row_data)


    def pesquisar_usuarios(self):
        self.banco.conectar()
        self.valor_consulta = self.inicio.tx_BuscaUsuarios.text()
        self.banco.cursorr.execute(f"SELECT * FROM pdv.usuarios WHERE nome LIKE '%{self.valor_consulta}%' or login LIKE '%{self.valor_consulta}%'")
        lista = self.banco.cursorr.fetchall()
        lista = list(lista)
        if not lista:
            return  self.alerta_registro()     
        else:   
            self.inicio.TableWidget_Usuario.setRowCount(0)
            #primeiro for trás
            for idxLinha, linha in enumerate(lista):
                self.inicio.TableWidget_Usuario.insertRow(idxLinha)
                for idxColuna, coluna in enumerate(linha):
                    self.inicio.TableWidget_Usuario.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
        self.banco.query.commit()
        self.banco.query.close()

    
    def pesquisar_clientes(self):
        self.banco.conectar()
        self.valor_consulta = self.inicio.tx_BuscaClientes.text()
        self.banco.cursorr.execute(f"SELECT * FROM pdv.clientes WHERE nome LIKE '%{self.valor_consulta}%' or cpf LIKE '%{self.valor_consulta}%'")
        lista = self.banco.cursorr.fetchall()
        lista = list(lista)
        if not lista:
            return  self.alerta_registro()     
        else:   
            self.inicio.TableWidget_Cliente.setRowCount(0)
            #primeiro for trás
            for idxLinha, linha in enumerate(lista):
                self.inicio.TableWidget_Cliente.insertRow(idxLinha)
                for idxColuna, coluna in enumerate(linha):
                    self.inicio.TableWidget_Cliente.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
        self.banco.query.commit()
        self.banco.query.close()


    def pesquisar_clientes_venda(self):
        self.banco.conectar()
        self.consulta_cliente_venda = self.Jan_lista_cliente.tx_BuscaClientes_Venda.text()
        self.banco.cursorr.execute(f"SELECT * FROM pdv.clientes WHERE nome LIKE '%{self.consulta_cliente_venda}%' or cpf LIKE '%{self.consulta_cliente_venda}%'")
        lista = self.banco.cursorr.fetchall()
        lista = list(lista)
        if not lista:
            return  self.alerta_registro()     
        else:   
            self.Jan_lista_cliente.tableWidget_cliente.setRowCount(0)
            #primeiro for trás
            for idxLinha, linha in enumerate(lista):
                self.Jan_lista_cliente.tableWidget_cliente.insertRow(idxLinha)
                for idxColuna, coluna in enumerate(linha):
                    self.Jan_lista_cliente.tableWidget_cliente.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
        self.banco.query.commit()
        self.banco.query.close()


    def pesquisar_produtos(self):
        self.banco.conectar()
        self.valor_consulta = self.inicio.tx_BuscaProdutos.text()
        self.banco.cursorr.execute(f"SELECT * FROM pdv.produtos WHERE descricao LIKE '%{self.valor_consulta}%' or marca LIKE '%{self.valor_consulta}%'")
        lista = self.banco.cursorr.fetchall()
        lista = list(lista)
        if not lista:
            return  self.alerta_registro()     
        else:   
            self.inicio.TableWidget_Produto.setRowCount(0)
            #primeiro for trás
            for idxLinha, linha in enumerate(lista):
                self.inicio.TableWidget_Produto.insertRow(idxLinha)
                for idxColuna, coluna in enumerate(linha):
                    self.inicio.TableWidget_Produto.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
        self.banco.query.commit()
        self.banco.query.close()


    def alerta_registro(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Registro Não Encontrado!")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec()
   
    
    def alerta_valor_invalido(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Valor inválido!")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec()
    
    
    def abrir_finaliza_venda_nota(self):
        try:
            self.valor_total_venda = self.jan_fecha_venda_nota.Lb_TotalPagar.setText(str(f'{self.total:.2f}'))
            self.jan_fecha_venda_nota.show()
            self.jan_fecha_venda_nota.Lb_Nome_cliente.setText(self.cliente_selecionado)
        except:
            self.alt_insirir_produto() 


    def seleciona_cliente_nota(self):
        linha = self.Jan_lista_cliente.tableWidget_cliente.currentRow()
        if linha >= 0:
            # Obtenha os dados da tabela após a pesquisa
            self.id_cliente = self.Jan_lista_cliente.tableWidget_cliente.item(linha, 0).text()
            self.nome_cliente = self.Jan_lista_cliente.tableWidget_cliente.item(linha, 1).text()
            # Use os dados da tabela para o cliente selecionado
            self.valor_id_cliente_venda = int(self.id_cliente)
            self.cliente_selecionado = self.nome_cliente
            self.Jan_lista_cliente.close()
            self.jan_fecha_venda.close()
            self.abrir_finaliza_venda_nota()

    
    def adiciona_credito_utilizado(self):
        self.banco.conectar() 
        sql = "SELECT credito, credito_utilizado FROM pdv.clientes WHERE idclientes = %s"
        valores = (self.valor_id_cliente_venda,)
        self.banco.cursorr.execute(sql, valores)
        resultado =  self.banco.cursorr.fetchone()
        if resultado:
            credito, credito_utilizado = resultado
            soma_credito_utilizado = float(credito_utilizado) + float(self.total)
            inserir_credito_utilizado = "UPDATE pdv.clientes SET credito_utilizado = %s WHERE idclientes = %s"
            valores_credit_utilizado = (str(soma_credito_utilizado), self.valor_id_cliente_venda)
            self.banco.cursorr.execute(inserir_credito_utilizado, valores_credit_utilizado)
            self.banco.query.commit()
            self.banco.cursorr.close()
            self.banco.query.close()
            self.forma_pagamento_nota = self.jan_fecha_venda_nota.Cb_FormaPagamento.currentText()
            self.jan_fecha_venda_nota.close()
            self.jan_comprovante_nota.show()
            self.add_credito_saldo()
        else:
           self.alerta_id_cliente()


    def alerta_id_cliente(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText(f"Cliente com ID {self.valor_id_cliente_venda} não encontrado")
        msg.setIcon(QMessageBox.Icon.Information)   
        msg.exec()


    def add_credito_saldo(self):
        self.banco.conectar()
        sql = "SELECT credito, credito_utilizado FROM pdv.clientes WHERE idclientes = %s"
        valores = (self.valor_id_cliente_venda,)
        self.banco.cursorr.execute(sql, valores)
        resultado =  self.banco.cursorr.fetchone()
        if resultado:
            credito, credito_utilizado = resultado
            credito_saldo = float(credito) - float(credito_utilizado)
            inserir_credito_saldo = "UPDATE pdv.clientes SET credito_saldo = %s WHERE idclientes = %s"
            valores_credit_saldo = (str(f'{credito_saldo:.2f}'), self.valor_id_cliente_venda)
            self.banco.cursorr.execute(inserir_credito_saldo, valores_credit_saldo)
            self.banco.query.commit()
            self.banco.cursorr.close()
            self.banco.query.close()

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.login.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()