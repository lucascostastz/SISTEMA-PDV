import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()

        # Adicione os widgets que você deseja empilhar
        self.page1 = QWidget()
        self.page1_button = QPushButton('Ir para a Página 2')
        self.page1_button.clicked.connect(self.show_page2)
        layout_page1 = QVBoxLayout(self.page1)
        layout_page1.addWidget(self.page1_button)

        self.page2 = QWidget()
        self.page2_button = QPushButton('Ir para a Página 1')
        self.page2_button.clicked.connect(self.show_page1)
        layout_page2 = QVBoxLayout(self.page2)
        layout_page2.addWidget(self.page2_button)

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.stacked_widget)

        self.setWindowTitle('QStackedWidget Example')

    def show_page2(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_page1(self):
        self.stacked_widget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
