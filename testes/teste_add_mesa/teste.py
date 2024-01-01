from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QFrame, QLabel, QVBoxLayout, QPushButton
from PyQt6 import QtWidgets, QtCore

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        self.frame_principal = QFrame(self)
        self.grid_layout = QGridLayout(self.frame_principal)

        self.add_frames_with_labels(30)  # Adiciona 10 frames com labels inicialmente
        self.frame_principal.setStyleSheet("background-color: rgb(0, 85, 127);")  # Adiciona o fundo ao frame principal
        main_layout.addWidget(self.frame_principal)
        self.setLayout(main_layout)

        self.setLayout(self.grid_layout)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Frames com Labels em PyQt6')
        self.frame_principal.setStyleSheet("background-color: rgb(0, 85, 127);")  # Adiciona o fundo ao frame principal
        self.show()

    def add_frames_with_labels(self, num_frames):
        for i in range(num_frames):
            frame = QFrame(self.frame_principal)
            frame.setObjectName(f'frame_mesa{i+1}')  # Adiciona um nome único para cada frame
            frame.setStyleSheet("""background-color: rgb(255, 255, 255);
                                border-radius:15px;""")
            
            frame.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)  # Define o estilo inicial
            frame.setMaximumSize(QtCore.QSize(196, 146))

            layout = QVBoxLayout(frame)

            label_mesa = QLabel(f'Mesa{i+1:02d}', frame)
            label_mesa.setStyleSheet('font: 14pt "MS Shell Dlg 2";')  # Gera o nome dinâmico (Mesa01, Mesa02, ...)

            label_status = QLabel('Livre', frame)
            label_status.setStyleSheet("""color: rgb(0, 170, 127);
                                        font: 75 14pt "MS Shell Dlg 2";""")
            
            
            button_detalhes = QPushButton('Detalhes', frame)
            button_detalhes.setObjectName(f'Bt_Detalhes{i+1}')  # Adiciona um nome único para cada botão
            button_detalhes.setStyleSheet("""QPushButton{
                                        background-color: rgb(162, 162, 162);
                                        font: 8pt "MS Shell Dlg 2";
                                        font-size:12px;
                                        border-radius:10px;
                                        }
                                        QPushButton:hover{
                                        background-color: #505050;
                                        }""")

            button_detalhes.setMaximumSize(QtCore.QSize(85, 25))
            button_detalhes.setMinimumSize(QtCore.QSize(85, 25))

            layout.addWidget(label_mesa, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label_status, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(button_detalhes, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)  # Botão na parte inferior

            # Adiciona o frame e as labels na próxima célula da grade
            row, col = divmod(i, 10)  # Duas colunas para cada linha
            self.grid_layout.addWidget(frame, row, col)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()
