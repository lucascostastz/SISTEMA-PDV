from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from Form_Cad_Produto import Ui_Form_Cad_Produtos
from banco import Classe_Banco


class Classe_Cad_Produto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.janela_cad_produto = Ui_Form_Cad_Produtos()
        self.janela_cad_produto.setupUi(self)
        self.janela_banco = Classe_Banco()
        self.janela_cad_produto.Bt_SalvarProdutos.clicked.connect(self.cadastrar_produto)
        self.janela_cad_produto.Bt_CancelarProdutos.clicked.connect(self.sair_cad_produto)

    def cadastrar_produto(self):
        self.janela_banco.cadastrar()
        descricao = self.janela_cad_produto.tx_DescricaoProduto.text()
        codigo = self.janela_cad_produto.tx_Codigo.text()
        categoria = self.janela_cad_produto.cb_CategoriaProduto.currentText()   
        marca = self.janela_cad_produto.tx_Marca.text()
        estoque = self.janela_cad_produto.tx_Estoque.text()
        preco = self.janela_cad_produto.tx_Preco_Produto.text()
        v_varejo = self.janela_cad_produto.tx_Venda_Varejo.text()
        v_atacado = self.janela_cad_produto.tx_Venda_Atacado.text()
        qm_atacado = self.janela_cad_produto.tx_MinimoAtacado.text()
        imagem = 'teste'

        if descricao == "":
            self.alt_cad_em_branco()
        elif estoque == "":
                self.alt_cad_em_branco()
        elif preco == "":
                self.alt_cad_em_branco()
        elif categoria == "SELECIONE":
                self.alt_categoria()
        else:
            self.janela_banco.cursorr.execute("INSERT INTO pdv.produtos (descricao,categoria,marca,estoque,codigo,preco,v_varejo,v_atacado,qm_atacado,imagem) VALUES('"+descricao+"','"+
                    categoria+"','"+marca+"','"+estoque+"','"+codigo+"','"+preco+"','"+v_varejo+"','"+v_atacado+"','"+qm_atacado+"','"+imagem+"')")
            self.janela_banco.banco.commit()
            self.janela_banco.banco.close()
            self.alt_cadastro_sucesso()
    

    def sair_cad_produto(self):
        self.janela_cad_produto.tx_DescricaoProduto.clear()
        self.janela_cad_produto.tx_Codigo.clear()
        self.janela_cad_produto.cb_CategoriaProduto.setCurrentIndex(0)
        self.janela_cad_produto.tx_Marca.clear()
        self.janela_cad_produto.tx_Estoque.clear()
        self.janela_cad_produto.tx_Preco_Produto.clear()
        self.janela_cad_produto.tx_Venda_Varejo.clear()
        self.janela_cad_produto.tx_Venda_Atacado.clear()
        self.janela_cad_produto.tx_MinimoAtacado.clear()
        self.close()


    def alt_cadastro_sucesso(self):
        msg = QMessageBox()
        msg.setWindowTitle("Parabéns!")
        msg.setText("Produto Cadastrado Com Sucesso!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
        self.janela_cad_produto.tx_DescricaoProduto.clear()
        self.janela_cad_produto.cb_CategoriaProduto.setCurrentIndex(0)
        self.janela_cad_produto.tx_Marca.clear()        
        self.janela_cad_produto.tx_Estoque.clear()
        self.janela_cad_produto.tx_Codigo.clear()
        self.janela_cad_produto.tx_Preco_Produto.clear() 
        self.janela_cad_produto.tx_Venda_Varejo.clear()
        self.janela_cad_produto.tx_Venda_Atacado.clear()
        self.janela_cad_produto.tx_MinimoAtacado.clear()


    def alt_cad_em_branco(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Complete os Campos em Branco!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
    

    def alt_categoria(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Selecione uma categoria!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    window = Classe_Cad_Produto()
    window.show()
    (app.exec())