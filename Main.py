from PyQt6.QtWidgets import QApplication, QTableWidgetItem,QMessageBox
from PyQt6 import QtWidgets
from PyQt6.QtGui import QKeySequence, QShortcut, QPixmap
import datetime
import subprocess
import sys
import requests
import webbrowser
from fpdf import FPDF
from form.Login.Janela_Login import Classe_Login
from form.Inicio.Janela_Inicio import Classe_Inicio
from form.Usuario.Janela_Cad_Usuario import Classe_Cad_Usuario
from form.Usuario.Janela_Edit_Usuario import Classe_Edit_Usuario
from funcoes.Banco.Conexao_banco import Classe_Banco
from form.Cliente.Janela_Cad_Cliente import Classe_Cad_Cliente
from form.Cliente.Janela_Edit_Cliente import Classe_Edit_Cliente
from form.Produto.Jan_Cad_Produto import Classe_Cad_Produto
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
from funcoes.Alertas.Arquivo_Alertas import Classe_Alertas
from form.Produto.Jan_add_categoria import Classe_Add_Categoria


class Main():
    def __init__(self):
        super(Main, self).__init__()
        self.inicio = Classe_Inicio()
        self.login = Classe_Login(self.inicio)
        self.cad_usuario = Classe_Cad_Usuario(self.inicio)
        self.edit_usuario = Classe_Edit_Usuario()
        self.banco = Classe_Banco()
        self.cad_cliente = Classe_Cad_Cliente(self.inicio)
        self.edit_cliente = Classe_Edit_Cliente(self.inicio)
        self.cad_produto = Classe_Cad_Produto(self.inicio)
        self.edit_produto = Classe_Edit_Produto(self.inicio)
        self.consulta_cnpj = Classe_Consulta_Cnpj()
        self.escolha_vendas = Classe_Chama_Venda()
        self.comanda = Classe_Comanda()
        self.venda_mesa = Classe_Venda_Mesa()
        self.jan_fecha_venda = Classe_Finaliza_Venda()
        self.jan_comprovante = Classe_Comprovante()
        self.Jan_lista_cliente = Classe_Lista_Cliente()
        self.jan_fecha_venda_nota = Classe_Finaliza_Venda_CLiente()
        self.jan_comprovante_nota = Classe_Comprovante_Nota()
        self.alertas = Classe_Alertas()
        self.cad_categoria = Classe_Add_Categoria()
    

######## --- Chama Telas --- ########
        self.inicio.Bt_Add_Usuario.clicked.connect(self.cham_cad_usuario)
        self.inicio.Bt_Edit_Usuario.clicked.connect(self.chama_edit_usuario)
        self.inicio.Bt_Cad_Cliente.clicked.connect(self.chama_cad_cliente)
        self.consulta_cnpj.Bt_Consultar_Cnpj.clicked.connect(self.consulta_pj)
        self.consulta_cnpj.Tx_Cnpj.returnPressed.connect(self.consulta_pj)
        self.inicio.Bt_Whatsapp_2.clicked.connect(self.abre_link_whatsapp)
        self.cad_cliente.tx_Cep.returnPressed.connect(self.busca_cep)
        self.inicio.Bt_Add_Fornecedor.clicked.connect(self.chama_consulta_cnpj)
        self.inicio.Bt_Vendas.clicked.connect(self.chama_vendas)
        self.inicio.Bt_Mesa01.clicked.connect(self.chama_comanda)
        self.inicio.tx_BuscaUsuarios.textChanged.connect(self.pesquisar_usuarios)
        self.inicio.Input_Quantidade.returnPressed.connect(self.adicionar_prod_carrinho)
        self.inicio.Bt_IncluirProduto.clicked.connect(self.adicionar_prod_carrinho)
        self.inicio.Bt_Finalizar_venda.clicked.connect(self.abrir_finaliza_venda)
        self.jan_fecha_venda.Bt_Confirmar_Vanda.clicked.connect(self.confirmar_venda)
        self.jan_fecha_venda.Input_ValorPago.returnPressed.connect(self.calcula_troco)
        self.jan_comprovante.Bt_NovaVenda.clicked.connect(self.nova_venda)
        self.jan_comprovante_nota.Bt_NovaVenda.clicked.connect(self.nova_venda)
        self.jan_fecha_venda.Cb_FormaPagamento.currentIndexChanged.connect(self.verificar_selecao)
        self.Jan_lista_cliente.tableWidget_cliente.doubleClicked.connect(self.seleciona_cliente_nota)
        self.Jan_lista_cliente.Bt_SelecionaCliente.clicked.connect(self.seleciona_cliente_nota)
        self.jan_fecha_venda_nota.Bt_Confirmar_Venda.clicked.connect(self.confirmar_venda_nota)
        self.jan_comprovante_nota.Bt_Cancela_venda.clicked.connect(self.nova_venda)
        self.jan_fecha_venda.Bt_Confirmar_Vanda.clicked.connect(self.confirmar_venda)
        self.jan_comprovante.Bt_Imprimir.clicked.connect(self.criar_cupom_fiscal)
        self.jan_comprovante_nota.Bt_Imprimir.clicked.connect(self.criar_cupom_fiscal_nota)
        self.cad_categoria.Bt_Salvar.clicked.connect(self.add_categoria)
        self.inicio.Bt_Add_Produto.clicked.connect(self.chama_cad_produto)
        self.cad_produto.Bt_Add_Categoria.clicked.connect(self.chama_cad_categoria)
        
        
    ######## --- Chama StakeWidgets --- ########
        self.escolha_vendas.Bt_Venda_Balcao.clicked.connect(self.tela_vendas)
        
        ###### --- Funções Teclas --- #####
        shortcut = QShortcut(QKeySequence('F5'), self.inicio.Vendas)
        shortcut.activated.connect(self.abrir_finaliza_venda)

        shortcut = QShortcut(QKeySequence('Esc'), self.inicio.Vendas)
        shortcut.activated.connect(self.cancelar_venda)
        
        shortcut = QShortcut(QKeySequence('F5'), self.jan_fecha_venda)
        shortcut.activated.connect(self.confirmar_venda)

        shortcut = QShortcut(QKeySequence('F1'), self.jan_comprovante)
        shortcut.activated.connect(self.criar_cupom_fiscal)

        shortcut = QShortcut(QKeySequence('F2'), self.jan_comprovante)
        shortcut.activated.connect(self.nova_venda)

        shortcut = QShortcut(QKeySequence('Delete'), self.inicio.TableWidget_Venda)
        shortcut.activated.connect(self.remover_item_selecionado)

        shortcut = QShortcut(QKeySequence('F2'), self.jan_fecha_venda)
        shortcut.activated.connect(self.chama_lista_cliente)

        

    def tela_vendas(self):
        self.inicio.stackedWidget.setCurrentIndex(1)
        self.escolha_vendas.close()
        self.inicio.focus_codigo()
        self.inicio.Lb_Operado.setText(self.login.user_logado)
    

        self.carrinho = []
        self.total_compra = 0.0

    
    ##### --- Chamada de Telas --- #####
    def chama_cad_cliente(self):
        self.cad_cliente.show()

    def chama_cad_produto(self):
        self.cad_produto.show()
        self.list_categorias()

    def cham_cad_usuario(self):
        self.cad_usuario.show()
    
    def chama_edit_usuario(self):
        self.edit_usuario.show()

    def chama_consulta_cnpj(self):
        self.consulta_cnpj.show()

    def chama_vendas(self):
        self.escolha_vendas.show()
        self.nova_venda()

    def chama_cad_categoria(self):
        self.cad_categoria.show()
    
    def chama_lista_cliente(self):
        self.Jan_lista_cliente.show()
        self.jan_fecha_venda.Input_ValorPago.clear()
        self.jan_fecha_venda.Lb_Troco.setText('00,00')
        self.Jan_lista_cliente.listar_cliente_venda()


######## --- Funções Inserir itens --- ########    
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
            self.alertas.alt_cep_invalido()
        

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
            self.alertas.alt_cnpj_invalido()


    def abre_link_whatsapp(self):
        webbrowser.open_new_tab('https://contate.me/lcinformtica')


    def chama_comanda(self):
        self.comanda.show()


    def pesquisar_usuarios(self):
        self.valor_consulta = self.inicio.tx_BuscaUsuarios.text()
        try:
            self.banco.conectar()
            self.banco.cursorr.execute(f"SELECT * FROM pdv.usuarios WHERE nome LIKE '%{self.valor_consulta}%' or login LIKE '%{self.valor_consulta}%'")
            lista = self.banco.cursorr.fetchall()
            lista = list(lista)
            if not lista:
                return  self.alertas.alerta_registro()     
            else:   
                self.inicio.TableWidget_Usuario.setRowCount(0)
                #primeiro for trás
                for idxLinha, linha in enumerate(lista):
                    self.inicio.TableWidget_Usuario.insertRow(idxLinha)
                    for idxColuna, coluna in enumerate(linha):
                        self.inicio.TableWidget_Usuario.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
            self.banco.query.commit()
            self.banco.query.close()
        except:
            pass


    def abrir_finaliza_venda_nota(self):
        try:
            self.valor_total_venda = self.jan_fecha_venda_nota.Lb_TotalPagar.setText(str(f'{self.total:.2f}'))
            self.jan_fecha_venda_nota.show()
            self.jan_fecha_venda_nota.Lb_Nome_cliente.setText(self.cliente_selecionado)
        except:
            self.alertas.alt_insirir_produto() 


    def seleciona_cliente_nota(self):
        linha = self.Jan_lista_cliente.tableWidget_cliente.currentRow()
        if linha >= 0:
            # Obtenha os dados da tabela após a pesquisa
            self.id_cliente = self.Jan_lista_cliente.tableWidget_cliente.item(linha, 0).text()
            self.nome_cliente = self.Jan_lista_cliente.tableWidget_cliente.item(linha, 1).text()
            self.debito = self.Jan_lista_cliente.tableWidget_cliente.item(linha, 6).text()
            self.debito_cliente = float(self.debito) + float(self.valor_total)
            # Use os dados da tabela para o cliente selecionado
            self.valor_id_cliente_venda = int(self.id_cliente)
            self.cliente_selecionado = self.nome_cliente
            self.Jan_lista_cliente.close()
            self.jan_fecha_venda.close()
            self.abrir_finaliza_venda_nota()

    
######## --- Função adicionar_prod_carrinho --- ########
    def adicionar_prod_carrinho(self):
        try:
            input_cod = self.inicio.Input_Codigo.text()
            quantidade = self.inicio.Input_Quantidade.text()
            if not input_cod or not quantidade:
                return
            produto_encontrado = self.buscar_produto(input_cod)
            if produto_encontrado:
                codigo, descricao, valor, estoque_atual = produto_encontrado
                if int(quantidade) > estoque_atual:
                    self.alertas.estoque_insuficiente()
                    return

                valor_unitario = valor
                valor_total = int(quantidade) * valor

                ##### --- Adiciona o produto ao carrinho de uma forma que preserve o estoque original --- ######
                carrinho_item = {"codigo": codigo, "descricao": descricao, "valor": valor, "quantidade": int(quantidade)}
                self.carrinho.append(carrinho_item)

                ##### --- Adiciona o produto à tabela --- ######
                row_position = self.inicio.TableWidget_Venda.rowCount()
                self.inicio.TableWidget_Venda.verticalHeader().hide()
                self.inicio.TableWidget_Venda.insertRow(row_position)
                self.inicio.TableWidget_Venda.setItem(row_position, 0, QTableWidgetItem(codigo))
                self.inicio.TableWidget_Venda.setItem(row_position, 1, QTableWidgetItem(descricao))
                self.inicio.TableWidget_Venda.setItem(row_position, 2, QTableWidgetItem(str(quantidade)))
                self.inicio.TableWidget_Venda.setItem(row_position, 3, QTableWidgetItem(f'R${valor_unitario:.2f}'))
                self.inicio.TableWidget_Venda.setItem(row_position, 4, QTableWidgetItem(f'R${valor_total:.2f}'))
                # Atualiza o estoque
                novo_estoque = estoque_atual - int(quantidade)
                self.atualizar_estoque_produto(input_cod, novo_estoque)
                self.inicio.Lb_fotoCarrinho.setPixmap(QPixmap(str(self.img_prd_carr)))
                self.inicio.Lb_Nome_Produto.setText(str(descricao))
                self.atualizar_valor_total()
            else:
                self.alertas.alerta_registro()
        except:
            self.alertas.alerta_valor_invalido()
        


    ##### --- Função cancelar_venda --- ######
    def cancelar_venda(self):
        # Percorre os itens do carrinho e atualiza o estoque e a quantidade de volta ao estado original no banco de dados
        for item in self.carrinho:
            codigo = item['codigo']
            quantidade = item['quantidade']
            estoque_atual = self.buscar_produto(codigo)[3]  # Obtém o estoque atual do banco de dados
            novo_estoque = estoque_atual + quantidade
            self.atualizar_estoque_produto(codigo, novo_estoque)
            # Atualiza a quantidade de volta no banco de dados
            self.banco.conectar()
            self.banco.cursorr.execute("UPDATE pdv.produtos SET estoque = %s WHERE codigo = %s", (novo_estoque, codigo))
            self.banco.query.commit()
            self.banco.query.close()
        # Limpa o carrinho
        self.carrinho = []
        # Limpa a tabela de vendas e atualiza o valor total
        self.inicio.TableWidget_Venda.setRowCount(0)
        self.atualizar_valor_total()
        self.inicio.Lb_fotoCarrinho.clear()
        self.inicio.Input_Codigo.clear()
        self.inicio.Input_Quantidade.clear()
        self.inicio.Input_Codigo.setFocus()
        self.inicio.label_total.clear()
        self.inicio.Lb_Nome_Produto.clear()


    def remover_item_selecionado(self):
        try:
            selected_row = self.inicio.TableWidget_Venda.currentRow()
            if selected_row != -1:
                codigo = self.inicio.TableWidget_Venda.item(selected_row, 0).text()
                quantidade = int(self.inicio.TableWidget_Venda.item(selected_row, 2).text())
                # Atualiza o estoque no banco de dados
                estoque_atual = self.buscar_produto(codigo)[3]
                novo_estoque = estoque_atual + quantidade
                self.atualizar_estoque_produto(codigo, novo_estoque)
                # Remove o item da tabela
                self.inicio.TableWidget_Venda.removeRow(selected_row)
                self.inicio.Lb_fotoCarrinho.clear()
                self.inicio.Input_Codigo.clear()
                self.inicio.Input_Quantidade.clear()
                self.inicio.Input_Codigo.setFocus()
                self.inicio.label_total.clear()
                self.inicio.Lb_Nome_Produto.clear()
                self.atualizar_valor_total()
                # Atualiza o valor total
            else:
                self.alertas.alerta_selecione_item()
        except Exception as e:
            print(f"Erro ao remover item: {e}")


    def atualizar_estoque_produto(self, input_cod, novo_estoque):
        try:
            # Atualiza o estoque no banco de dados
            self.banco.conectar()
            self.banco.cursorr.execute("UPDATE pdv.produtos SET estoque = %s WHERE codigo = %s", (novo_estoque, input_cod))
            self.banco.query.commit()
            self.banco.query.close()
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Alerta!")
            msg.setText(f"Erro ao atualizar estoque: {e}")
            msg.setIcon(QMessageBox.Icon.Information)   
            msg.exec()
    
    
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
                self.estoque = item[4]
                codigo = item[5]
                descricao = item[1]
                valor = float(item[6])
                estoque_atual = int(item[4])
                self.img_prd_carr = item[12]
                item_transformado = {"codigo": codigo, "descricao": descricao, "valor": valor, "estoque_atual": estoque_atual}
                self.produtos.append(item_transformado)
                for produto in self.produtos:
                    if produto['codigo'] == input_cod:
                        return produto['codigo'], produto['descricao'], produto['valor'], produto['estoque_atual']
        except:
            self.alertas.alt_campo_invalido()

       
    def verificar_selecao(self):
        item_selecionado = self.jan_fecha_venda.Cb_FormaPagamento.currentText()
        if item_selecionado == "Nota":
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
            self.alertas.alerta_pagamento()


    def nova_venda(self):
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
        self.inicio.focus_codigo()

    
    def atualizar_valor_total(self):
        self.total = 0
        for row in range(self.inicio.TableWidget_Venda.rowCount()):
            self.valor_total = float(self.inicio.TableWidget_Venda.item(row, 4).text()[2:])
            self.total += self.valor_total
            self.inicio.label_total.setText(str(f"{self.total:.2f}"))
        self.inicio.focus_codigo()
        

    def abrir_finaliza_venda(self):
        try:
            self.valor_total_venda = self.jan_fecha_venda.Lb_TotalPagar.setText(str(f'{self.total:.2f}'))
            self.jan_fecha_venda.show()
            self.jan_fecha_venda.Lb_Troco.clear()
            self.jan_fecha_venda.Input_ValorPago.clear()
        except:
            self.alertas.alt_insirir_produto()    


    def calcula_troco(self):
        self.valor_pago = float(self.jan_fecha_venda.Input_ValorPago.text())
        valor_total = float(self.jan_fecha_venda.Lb_TotalPagar.text())
        self.troco = float(self.valor_pago - valor_total)
        self.jan_fecha_venda.Lb_Troco.setText(f'{self.troco:.2f}')
    
        
    def criar_cupom_fiscal(self):
        try:
            data = datetime.date.today()
            data_formatada = data.strftime("%d/%m/%Y")
            hora = datetime.datetime.now().time()
            hora_formatada = hora.strftime("%H:%M")
            self.banco.conectar()
            self.banco.cursorr.execute("SELECT * FROM pdv.empresa")
            dadoslisdos_empresa = self.banco.cursorr.fetchall()
            razao_social = dadoslisdos_empresa[0][1]
            cnpj = dadoslisdos_empresa[0][2]
            endereco = dadoslisdos_empresa[0][6]
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
            pdf.output("Comprovante.pdf")
            caminho_pdf = "Comprovante.pdf"
            # Abrir o arquivo PDF com o leitor de PDF padrão
            subprocess.Popen([caminho_pdf], shell=True)
        except:
            razao_social = " RAZÃO SOCIAL NÃO DEFINIDO"
            cnpj = "CNPJ NÃO DEFINIDO"
            endereco = "ENDEREÇO NÃO DEFINIDO"
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
            pdf.output("Comprovante.pdf")
            caminho_pdf = "Comprovante.pdf"
            subprocess.Popen([caminho_pdf], shell=True)

    
    def criar_cupom_fiscal_nota(self):
        try:
            data = datetime.date.today()
            data_formatada = data.strftime("%d/%m/%Y")
            hora = datetime.datetime.now().time()
            hora_formatada = hora.strftime("%H:%M")
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
            pdf.output("Comprovante.pdf")
            caminho_pdf = "Comprovante.pdf"
            # Abrir o arquivo PDF com o leitor de PDF padrão
            subprocess.Popen([caminho_pdf], shell=True)
        except:
            razao_social = " RAZÃO SOCIAL NÃO DEFINIDO"
            cnpj = "CNPJ NÃO DEFINIDO"
            endereco = "ENDEREÇO NÃO DEFINIDO"
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
            pdf.cell(40, 5, txt=f"Débido: R${self.debito_cliente:.2f}")
            pdf.ln()
            # Rodapé
            pdf.cell(45, 5, txt="-----------------------------------------------------------------------------------", ln=True)  
            pdf.cell(40, 5, txt=f"                                         Assinatura                    ")
            pdf.ln()
            pdf.cell(80, 10, txt="Obrigado por sua compra!", ln=True, align='C')    
            # Salvar o arquivo PDF
            pdf.output("Comprovante.pdf")
            caminho_pdf = "Comprovante.pdf"
            # Abrir o arquivo PDF com o leitor de PDF padrão
            subprocess.Popen([caminho_pdf], shell=True)


    def add_credito_saldo(self):
        try:
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
        except:
            pass


    def confirmar_venda_nota(self):
        self.adiciona_credito_utilizado()
        self.add_credito_saldo()
        self.inserir_vendas_relatorio_cliente()
    
    
    def adiciona_credito_utilizado(self):
        try:
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
            else:
                self.alertas.alerta_id_cliente()
        except:
            pass
    

    def inserir_vendas_relatorio_cliente(self):
        try:
            hora = datetime.datetime.now().time()
            hora_formatada = hora.strftime("%H:%M")
            data = datetime.date.today()
            data_formatada = data.strftime("%d/%m/%Y")
            data_hora = (f'{data_formatada}: {hora_formatada}')
            self.banco.conectar()
            self.banco.cursorr.execute("INSERT INTO pdv.vendas (data,valor_venda,operador,tipo_venda,cliente) VALUES('" +data_hora+"','"+str(self.valor_total)+"','"+self.login.user_logado+"','"+self.forma_pagamento_nota+"','"+self.cliente_selecionado+"')")
            self.banco.query.commit()
            self.banco.cursorr.close()
            self.banco.query.close()
        except:
            pass 
        

    def confirmar_venda(self):
        try:
            self.forma_pagamento = self.jan_fecha_venda.Cb_FormaPagamento.currentText() 
            self.jan_fecha_venda.close()
            self.inserir_vendas_relatorio()
            self.jan_comprovante.show() 
            self.inicio.Input_Codigo.clear() 
            self.inicio.Input_Quantidade.clear()
            self.inicio.label_total.setText("0.00")
            self.inicio.Lb_fotoCarrinho.clear()
            self.jan_fecha_venda.Input_ValorPago.clear()
            self.jan_fecha_venda.Lb_Troco.setText('0,00')
            self.inicio.Lb_Nome_Produto.clear()
            self.inicio.TableWidget_Venda.setRowCount(0)
        except:
            self.alertas.valor_invalido()
            

    def inserir_vendas_relatorio(self):
        try:
            hora = datetime.datetime.now().time()
            hora_formatada = hora.strftime("%H:%M")
            data = datetime.date.today()
            data_formatada = data.strftime("%d/%m/%Y")
            data_hora = (f'{data_formatada}: {hora_formatada}')
            not_defined = 'Não definido'
            self.banco.conectar()
            self.banco.cursorr.execute("INSERT INTO pdv.vendas (data,valor_venda,operador,tipo_venda,cliente) VALUES('" +data_hora+"','"+str(self.valor_total)+"','"+self.login.user_logado+"','"+self.forma_pagamento+"','"+not_defined+"')")
            self.banco.query.commit()
            self.banco.cursorr.close()
            self.banco.query.close()
        except:
            pass
        
    
    def list_categorias(self):
        self.cad_produto.cb_CategoriaProduto.clear()
        self.banco.conectar()
        self.banco.cursorr.execute('SELECT categorias FROM pdv.configuracoes')
        lista_categorias = self.banco.cursorr.fetchall()
        for categorias in lista_categorias:
            self.cad_produto.cb_CategoriaProduto.addItems(categorias)
        self.banco.cursorr.close()
        self.banco.query.close()

        
    def add_categoria(self):
        descricao = self.cad_categoria.Tx_Descricao.text()
        self.banco.conectar()
        self.banco.cursorr.execute("INSERT INTO pdv.configuracoes (categorias) VALUES ('"+descricao+"')")
        self.banco.query.commit()
        self.banco.query.close()
        self.banco.cursorr.close()
        self.alertas.alerta_categoria()
        self.cad_categoria.Tx_Descricao.clear() 
        self.list_categorias()
        

def main():
        app = QApplication(sys.argv)
        window = Main()
        window.login.show()
        sys.exit(app.exec())
if __name__ == '__main__':
    main()