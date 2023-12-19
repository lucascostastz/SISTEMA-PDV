from PyQt6.QtWidgets import QMainWindow, QApplication
from form.Produto.Form_add_categoria import Ui_add_categoria
from funcoes.Banco.Conexao_banco import Classe_Banco


class Classe_Add_Categoria(QMainWindow, Ui_add_categoria):
    def __init__(self):
        super(Classe_Add_Categoria, self).__init__()
        self.setupUi(self)
        self.banco = Classe_Banco()

        self.Bt_Cancelar.clicked.connect(self.fechar_janela)
    

    def fechar_janela(self):
        self.close()
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Add_Categoria()
    system.show()
    sys.exit(app.exec())