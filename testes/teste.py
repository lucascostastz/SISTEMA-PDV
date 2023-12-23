import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget
from funcoes.Banco.Conexao_banco import Classe_Banco

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.banco = Classe_Banco()

        self.setWindowTitle("ComboBox from List")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.comboBox = QComboBox()
        self.layout.addWidget(self.comboBox)

       
        self.banco.conectar()
        self.banco.cursorr.execute('SELECT categorias FROM pdv.configuracoes')
        lista_categorias = self.banco.cursorr.fetchall()
        for categorias in lista_categorias:
             self.comboBox.addItems(categorias)
             print(categorias)
        self.banco.query.close()

        # Adiciona os itens ao QComboBox
        """ self.comboBox.addItems(categorias) """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
