from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
import sys

class ImageApp(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar a interface do usuário
        self.init_ui()

    def init_ui(self):
        # Caminho da imagem
        imagem_caminho = './img/produtos/arroz.jpg'

        # Criar QLabel
        label = QLabel(self)

        # Carregar a imagem no QPixmap
        pixmap = QPixmap(imagem_caminho)

        # Definir a imagem na QLabel
        label.setPixmap(pixmap)

        # Configurar para escalar a imagem, mantendo seu tamanho original
        label.setScaledContents(True)

        # Criar layout
        layout = QVBoxLayout()
        layout.addWidget(label)

        # Definir o layout para a janela principal
        self.setLayout(layout)

        # Configurações da janela
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Imagem Fixa')

def main():
    app = QApplication(sys.argv)
    ex = ImageApp()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
