from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import QEvent
from form.Produto.Form_Cad_Produto import Ui_Form_Cad_Produtos

class Classe_Cad_Produto(QMainWindow, Ui_Form_Cad_Produtos):
    def __init__(self):
        super(Classe_Cad_Produto, self).__init__()
        self.setupUi(self)

        self.Bt_CancelarProdutos.clicked.connect(self.fechar_janela)
        # Conectar a função para capturar código de barras ao evento focusInEvent
        self.tx_Codigo.installEventFilter(self)



    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.FocusIn and source is self.tx_Codigo:
            # Aqui você pode chamar a função que lê o código de barras do dispositivo USB
            # No exemplo abaixo, simulamos a leitura de um código de barras fixo
            codigo_barras_lido = self.ler_codigo_barras_usb()
            self.tx_Codigo.setText(codigo_barras_lido)

        return super().eventFilter(source, event)

    def ler_codigo_barras_usb(self):
        # Simulação de leitura de código de barras (substitua isso pelo código real)
        return ''

        
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


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Cad_Produto()
    system.show()
    sys.exit(app.exec())