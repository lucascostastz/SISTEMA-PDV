from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar
from PyQt6.QtCore import QTimer
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.progress_bar = QProgressBar(self)
        self.start_button = QPushButton('Iniciar', self)
        self.start_button.clicked.connect(self.start_execution)

        layout = QVBoxLayout(self)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_button)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)

        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle('ProgressBar com PyQt6')
        self.show()

    def start_execution(self):
        # Inicia a execução da função em intervalos regulares
        self.timer.start(100)  # O intervalo é definido em milissegundos

    def update_progress(self):
        # Atualiza a barra de progresso
        current_value = self.progress_bar.value()
        if current_value < 30:
            self.progress_bar.setValue(current_value + 1)
        else:
            print("A função foi concluída!")
            self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec())
