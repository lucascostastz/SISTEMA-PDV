import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ComboBox from List")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.comboBox = QComboBox()
        self.layout.addWidget(self.comboBox)

        # Sua lista de itens
        lista_itens = ["Item 1", "Item 2", "Item 3", "Item 4"]

        # Adiciona os itens ao QComboBox
        self.comboBox.addItems(lista_itens)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
