from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QPixmap
from form.Produto.Form_Edit_Produto import Ui_Form_Edit_Produtos
from funcoes.Banco.Conexao_banco import Classe_Banco
from funcoes.Alertas.Arquivo_Alertas import Classe_Alertas


class Classe_Edit_Produto(QMainWindow, Ui_Form_Edit_Produtos):
    def __init__(self, inicio):
        super(Classe_Edit_Produto, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()
        self.alertas = Classe_Alertas()
        self.inicio = inicio


        self.bt_AddImagem.clicked.connect(self.editar_img_produto)
        self.Bt_CancelarProdutos.clicked.connect(self.sair)
        self.Bt_SalvarProdutos.clicked.connect(self.salvar_produto_editados)
        self.inicio.Bt_Edit_Produto.clicked.connect(self.chama_edit_produto)

    
    def chama_edit_produto(self):
        linha = self.inicio.TableWidget_Produto.currentRow()
        self.banco.conectar()
        self.banco.cursorr.execute("SELECT idprodutos FROM pdv.produtos")
        dados_lidos = self.banco.cursorr.fetchall()
        self.valor_id_editproduto = dados_lidos[linha][0]
        self.banco.cursorr.execute("SELECT * FROM pdv.produtos WHERE idprodutos=" + str(self.valor_id_editproduto)) 
        produto = self.banco.cursorr.fetchall()
        self.show()  
        self.tx_DescricaoProduto.setText(str(produto[0][1]))
        self.cb_CategoriaProduto.setCurrentIndex(0)
        self.tx_Marca.setText(str(produto[0][3]))
        self.tx_Estoque.setText(str(produto[0][4]))
        self.tx_Codigo.setText(str(produto[0][5]))
        self.tx_Preco_Produto.setText(str(produto[0][6]))
        self.tx_Venda_Atacado.setText(str(produto[0][7]))
        self.tx_MinimoAtacado.setText(str(produto[0][9]))
        validade_banco_str = (str(produto[0][11]))
        day, month, year = map(int, validade_banco_str.split('/'))
        validade_modificada = QDate(year, month, day)
        self.dateEdit.setDate(validade_modificada)
        data = str(produto[0][11])
        formato = "dd/MM/yyyy"
        data_formatada = QDate.fromString(data, formato)
        self.dateEdit.setDate(data_formatada)
        self.lb_FotoProduto.setPixmap(QPixmap(str(produto[0][12])))
        self.banco.query.commit()
        self.banco.query.close()

    
    def editar_img_produto(self):
        try:
            file_dialog = QFileDialog()
            file_dialog.setWindowTitle("Escolher Imagem")
            file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
            file_dialog.setNameFilter("Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm *.tif *.tiff);;Todos os Arquivos (*)")
            file_dialog.exec()
            self.conteudo_edit_produto = file_dialog.selectedFiles()
            self.lb_FotoProduto.setPixmap(QPixmap(self.conteudo_edit_produto[0]))
        except:
            self.alertas.alerta_imagem()


    def salvar_produto_editados(self):
        try:
            self.banco.conectar()
            codigo = self.tx_Codigo.text()
            descricao = self.tx_DescricaoProduto.text()
            categoria = self.cb_CategoriaProduto.currentText()
            marca = self.tx_Marca.text()
            estoque = self.tx_Estoque.text()
            preco = self.tx_Preco_Produto.text()
            v_atacado = self.tx_Venda_Atacado.text()
            minimo_atacado = self.tx_MinimoAtacado.text()
            imagem = self.conteudo_edit_produto
            caminho_img = str(imagem[0])
            self.banco.cursorr.execute("UPDATE pdv.produtos SET descricao = '{}', categoria = '{}', marca = '{}', estoque ='{}', codigo ='{}', preco = '{}', v_atacado = '{}', qm_atacado = '{}', imagem = '{}'  WHERE idprodutos = {}".format(
                descricao, categoria, marca, estoque, codigo, preco, v_atacado, minimo_atacado, caminho_img, self.valor_id_editproduto))
            self.banco.query.commit()
            self.banco.query.close()
            self.inicio.listar_produtos()
            self.alertas.alerta_produto_editado()
        except:
            self.banco.conectar()
            codigo = self.tx_Codigo.text()
            descricao = self.tx_DescricaoProduto.text()
            categoria = self.cb_CategoriaProduto.currentText()
            marca = self.tx_Marca.text()
            estoque = self.tx_Estoque.text()
            preco = self.tx_Preco_Produto.text()
            v_atacado = self.tx_Venda_Atacado.text()
            minimo_atacado = self.tx_MinimoAtacado.text()
            self.banco.cursorr.execute("UPDATE pdv.produtos SET descricao = '{}', categoria = '{}', marca = '{}', estoque ='{}', codigo ='{}', preco = '{}', v_atacado = '{}', qm_atacado = '{}' WHERE idprodutos = {}".format(
                descricao, categoria, marca, estoque, codigo, preco, v_atacado, minimo_atacado, self.valor_id_editproduto))
            self.banco.query.commit()
            self.banco.query.close()
            self.alertas.alerta_produto_editado()
            self.inicio.listar_produtos()


    def sair(self):
        self.close()

        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Edit_Produto()
    system.show()
    sys.exit(app.exec())