from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Botões da janela
        close_button = QPushButton('Fechar', self)
        maximize_button = QPushButton('Maximizar', self)
        minimize_button = QPushButton('Minimizar', self)

        # Conectar botões aos slots (ações)
        close_button.clicked.connect(self.close)
        maximize_button.clicked.connect(self.showMaximized)
        minimize_button.clicked.connect(self.showMinimized)

        # Layout vertical para organizar os botões
        layout = QVBoxLayout()
        layout.addWidget(close_button)
        layout.addWidget(maximize_button)
        layout.addWidget(minimize_button)

        # Configurar o layout principal da janela
        self.setLayout(layout)

        # Configurar as flags da janela para remover os botões de fechar, maximizar e minimizar
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
