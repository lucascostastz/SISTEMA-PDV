from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
import datetime
from PyQt6.QtGui import QPixmap
from form.Produto.Form_Cad_Produto import Ui_Form_Cad_Produtos
from funcoes.Banco.Conexao_banco import Classe_Banco
from funcoes.Alertas.Arquivo_Alertas import Classe_Alertas


class Classe_Cad_Produto(QMainWindow, Ui_Form_Cad_Produtos):
    def __init__(self, inicio):
        super(Classe_Cad_Produto, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()
        self.alertas = Classe_Alertas()
        self.inicio = inicio

        self.Bt_CancelarProdutos.clicked.connect(self.fechar_janela)
        self.Bt_SalvarProdutos.clicked.connect(self.inserir_produtos)
        self.bt_AddImagem.clicked.connect(self.inserir_img_produto)
    

    def inserir_produtos(self):
        try:
            data = datetime.date.today()
            data_formatada = data.strftime("%d/%m/%Y")
            descricao = self.tx_DescricaoProduto.text()
            codigo = self.tx_Codigo.text()
            categoria = self.cb_CategoriaProduto.currentText()
            marca = self.tx_Marca.text()
            estoque = self.tx_Estoque.text()    
            preco = self.tx_Preco_Produto.text()
            v_atacado = self.tx_Venda_Atacado.text()
            qtd_atacado = self.tx_MinimoAtacado.text()
            self.banco.conectar()
            try:
                self.banco.cursorr.execute("INSERT INTO pdv.produtos (descricao, codigo, categoria, marca, estoque, preco, v_atacado, qm_atacado, data_cadastro, imagem) VALUES('" +
                            descricao+"','"+codigo+"','"+categoria+"','"+marca+"','"+estoque+"','"+preco+"','"+v_atacado+"','"+qtd_atacado+"','"+str(data_formatada)+"','"+str(self.file_paths[0])+"')")
                self.banco.query.commit()
                self.banco.query.close()
                self.limpar_campos()
                self.alertas.alerta_produto_cadastrado()
                self.inicio.listar_produtos()
            except:
                self.banco.cursorr.execute("INSERT INTO pdv.produtos (descricao,codigo,categoria,marca,estoque,preco,v_atacado,qm_atacado, data_cadastro) VALUES('" +
                            descricao+"','"+codigo+"','"+categoria+"','"+marca+"','"+estoque+"','"+preco+"','"+v_atacado+"','"+qtd_atacado+"','"+str(data_formatada)+"')")
                self.banco.query.commit()
                self.banco.query.close()
                self.limpar_campos()
                self.alertas.alerta_produto_cadastrado()
                self.inicio.listar_produtos()
        except:
            pass
    
    def inserir_img_produto(self):
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("Escolher Imagem")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Imagens (*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm *.tif *.tiff);;Todos os Arquivos (*)")
        file_dialog.exec()
        self.file_paths = file_dialog.selectedFiles()
        self.lb_FotoProduto.setPixmap(QPixmap(self.file_paths[0]))

        
    def fechar_janela(self):
        self.limpar_campos()
        self.close()
        

    def limpar_campos(self):
        self.tx_DescricaoProduto.clear()
        self.tx_Codigo.clear()
        self.tx_Estoque.clear()
        self.tx_Marca.clear()
        self.tx_Preco_Produto.clear()
        self.tx_MinimoAtacado.clear()
        self.tx_Venda_Atacado.clear()
        self.cb_CategoriaProduto.setCurrentIndex(0)
        self.lb_FotoProduto.clear()
        self.dateEdit.clear()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Cad_Produto()
    system.show()
    sys.exit(app.exec())