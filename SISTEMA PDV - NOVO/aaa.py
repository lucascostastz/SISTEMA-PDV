from fpdf import FPDF
from form.Banco.banco import Classe_Banco
import datetime
import mysql.connector

def criar_cupom_fiscal():
        banco = Classe_Banco()
        try:
            banco.conectar()
            banco.cursorr.execute("SELECT * FROM pdv.empresa")
            dadoslisdos_empresa = banco.cursorr.fetchall()
            razao_social = dadoslisdos_empresa[0][1]
            cnpj = dadoslisdos_empresa[0][2]
            endereco = dadoslisdos_empresa[0][6]
            data = datetime.date.today()
            data_formatada = data.strftime("%d/%m/%Y")
            hora = datetime.datetime.now().time()
            hora_formatada = hora.strftime("%H:%M")

            lista = []
            for linha in range(inicio.TableWidget_Venda.rowCount()):
                linha_lista = []
                for coluna in range(inicio.TableWidget_Venda.columnCount()):
                    item = inicio.TableWidget_Venda.item(linha, coluna)
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
            pdf.cell(45, 5, txt=(f"{str(data_formatada), str(hora_formatada)}"), ln=True)
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
            pdf.cell(40, 5, txt=f"R$ {total}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Valor Pago: R$ {valor_pago}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Troco: R$ {troco}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Forma de pagamento: {forma_pagamento}")
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
            for linha in range(inicio.TableWidget_Venda.rowCount()):
                linha_lista = []
                for coluna in range(inicio.TableWidget_Venda.columnCount()):
                    item = inicio.TableWidget_Venda.item(linha, coluna)
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
            pdf.cell(40, 5, txt=f"R$ {total}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Valor Pago: R$ {valor_pago}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Troco: R$ {troco}")
            pdf.ln()
            pdf.cell(40, 5, txt=f"Forma de pagamento: {forma_pagamento}")
            pdf.ln()
            pdf.cell(45, 5, txt="-----------------------------------------------------------------------------------", ln=True)  
            # Rodapé
            pdf.cell(80, 10, txt="Obrigado por sua compra!", ln=True, align='C')    
            # Salvar o arquivo PDF
            pdf.output("nome_arquivo.pdf")
            caminho_pdf = "nome_arquivo.pdf"
            # Abrir o arquivo PDF com o leitor de PDF padrão
            subprocess.Popen([caminho_pdf], shell=True)