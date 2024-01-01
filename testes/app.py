import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QFrame, QLabel, QPushButton

class MyTable(QTableWidget):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)

        self.setWindowTitle("QTableWidget Example")
        self.setGeometry(100, 100, 600, 400)

        self.initUI()

    def initUI(self):
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                # Criar um widget que contém um frame
                cell_widget = QWidget()
                cell_layout = QVBoxLayout(cell_widget)
                frame = QFrame()

                # Adicionar uma QLabel com o texto "Mesa"
                label_mesa = QLabel("Mesa")
                cell_layout.addWidget(label_mesa)

                # Adicionar uma QLabel com o texto "Livre"
                label_livre = QLabel("Livre")
                cell_layout.addWidget(label_livre)

                # Adicionar um QPushButton com o texto "Detalhes"
                button_detalhes = QPushButton("Detalhes")
                cell_layout.addWidget(button_detalhes)

                frame.setLayout(cell_layout)

                # Adicionar um item à célula (pode ser vazio)
                item = QTableWidgetItem()
                item.setFlags(item.flags() ^ 0x0001)  # Desativar edição da célula
                self.setItem(row, col, item)

                # Definir o widget como o widget da célula
                self.setCellWidget(row, col, frame)

def main():
    app = QApplication(sys.argv)
    table = MyTable(5, 5)
    table.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
