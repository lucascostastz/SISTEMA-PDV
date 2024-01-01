from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QFrame, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6 import QtCore
from funcoes.Banco.Conexao_banco import Classe_Banco
import sqlite3


class MainWindow(QWidget):
    data_changed = pyqtSignal()  # Sinal personalizado para indicar mudanças nos dados

    def __init__(self):
        super().__init__()
        self.banco = Classe_Banco()

        # Mapeamento de frames para tabelas no banco de dados
        self.frame_table_mapping = {}

        # Simulando uma conexão com o banco de dados (SQLite neste exemplo)
        self.db_conn = sqlite3.connect(':memory:')  # Substitua por sua conexão real

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        self.frame_principal = QFrame(self)
        self.grid_layout = QGridLayout(self.frame_principal)

        self.add_frames_with_labels(30)  # Adiciona 3 frames com labels inicialmente (para teste)
        self.frame_principal.setStyleSheet("background-color: rgb(0, 85, 127);")  # Adiciona o fundo ao frame principal
        main_layout.addWidget(self.frame_principal)
        self.setLayout(main_layout)

        self.setLayout(self.grid_layout)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Frames com Labels em PyQt6')
        self.frame_principal.setStyleSheet("background-color: rgb(0, 85, 127);")  # Adiciona o fundo ao frame principal
        self.show()

        # Conecta o sinal data_changed à função check_table_contents
        self.data_changed.connect(self.check_table_contents)

        # Verifica e define as cores iniciais com base no conteúdo das tabelas
        self.data_changed.emit()  # Emite o sinal para realizar a verificação inicial

    def add_frames_with_labels(self, num_frames):
        for i in range(num_frames):
            frame = QFrame(self.frame_principal)
            frame_name = f'frame_mesa{i+1}'
            frame.setObjectName(frame_name)  # Adiciona um nome único para cada frame
            frame.setStyleSheet("""background-color: rgb(255, 255, 255);
                                border-radius:15px;""")
            
            frame.setFrameShape(QFrame.Shape.WinPanel)
            frame.setFrameShadow(QFrame.Shadow.Raised)  # Define o estilo inicial
            frame.setMaximumSize(QtCore.QSize(196, 146))

            layout = QVBoxLayout(frame)

            label_mesa = QLabel(f'Mesa{i+1:02d}', frame)
            label_mesa.setStyleSheet('font: 14pt "MS Shell Dlg 2";')  # Gera o nome dinâmico (Mesa01, Mesa02, ...)

            label_status = QLabel('Livre', frame)
            label_status.setObjectName('label_status')  # Adiciona um nome à label_status
            label_status.setStyleSheet("""color: rgb(0, 170, 127);
                                        font: 75 14pt "MS Shell Dlg 2";""")
            
            button_detalhes = QPushButton('Detalhes', frame)
            button_detalhes.setObjectName(f'button_detalhes_{i+1}')  # Adiciona um nome único para cada botão
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

            # Conecta o sinal clicked do botão à função on_button_click
            button_detalhes.clicked.connect(self.on_button_click)

            layout.addWidget(label_mesa, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label_status, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(button_detalhes, alignment=Qt.AlignmentFlag.AlignCenter)  # Botão na parte inferior

            # Adiciona o frame e as labels na próxima célula da grade
            row, col = divmod(i, 10)  # Duas colunas para cada linha
            self.grid_layout.addWidget(frame, row, col)

            # Mapeia o nome do frame ao nome da tabela correspondente
            table_name = f'mesa{i+1}'
            self.frame_table_mapping[frame_name] = table_name

    def on_button_click(self):
        sender = self.sender()  # Obtém o objeto que emitiu o sinal (o botão clicado)
        frame_name = sender.parent().objectName()  # Obtém o nome do frame pai do botão
        table_name = self.frame_table_mapping.get(frame_name)

        if table_name:
            # Aqui você pode adicionar o código que deseja executar em resposta ao clique do botão
            print(f'Botão clicado no frame {frame_name}. Correspondente à tabela {table_name} no banco de dados.')

    def check_table_contents(self):
        # Verifica o conteúdo de cada tabela e define a cor com base nisso
        for frame_name, table_name in self.frame_table_mapping.items():
            if self.table_has_data(table_name):
                self.set_frame_color(frame_name, 'red')
                self.update_label_status(frame_name, 'Ocupado')
            else:
                self.set_frame_color(frame_name, 'green')
                self.update_label_status(frame_name, 'Livre')

        # Atualiza o layout para garantir que as alterações sejam refletidas
        self.update()

    def table_has_data(self, table_name):
        # Simulação: Verifica se a tabela tem dados (substitua com seu código real)
        self.banco.conectar()
        self.banco.cursorr.execute(f"SELECT COUNT(*) FROM pdv.{table_name}")
        row_count = self.banco.cursorr.fetchone()[0]
        return row_count > 0

    def set_frame_color(self, frame_name, color):
        # Define a cor do frame
        frame = self.findChild(QFrame, frame_name)
        if frame:
            frame.setStyleSheet(f"background-color: {color}; border-radius:15px;")

    def update_label_status(self, frame_name, status_text):
        # Atualiza o texto da label_status
        frame = self.findChild(QFrame, frame_name)
        if frame:
            label_status = frame.findChild(QLabel, 'label_status')
            if label_status:
                label_status.setText(status_text)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()
