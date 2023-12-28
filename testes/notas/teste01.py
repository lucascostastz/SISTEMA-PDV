import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFormLayout
from PyQt6.QtCore import Qt
import datetime

class VendasApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Vendas a Prazo")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_valor = QLabel("Valor da venda:")
        self.edit_valor = QLineEdit()
        self.layout.addWidget(self.label_valor)
        self.layout.addWidget(self.edit_valor)

        self.label_parcelas = QLabel("Número de parcelas:")
        self.edit_parcelas = QLineEdit()
        self.layout.addWidget(self.label_parcelas)
        self.layout.addWidget(self.edit_parcelas)

        self.calcular_button = QPushButton("Calcular Parcelas")
        self.calcular_button.clicked.connect(self.calcular_parcelas)
        self.edit_parcelas.textChanged.connect(self.calcular_parcelas)
        self.layout.addWidget(self.calcular_button)

        self.result_layout = QFormLayout()

        self.central_widget.setLayout(self.layout)

    def calcular_parcelas(self):
        self.layout
        
        valor_venda = float(self.edit_valor.text())
        num_parcelas = int(self.edit_parcelas.text())
        data_atual = datetime.date.today()

        data_vencimentos = self.calcular_data_vencimento(data_atual, num_parcelas)
        valor_parcela = valor_venda / num_parcelas

        for i, data_vencimento in enumerate(data_vencimentos):
            label = QLabel(f"Parcela {i + 1}:")
            valor_label = QLabel(f"Valor: R$ {valor_parcela:.2f}")
            data_label = QLabel(f"Data de Vencimento: {data_vencimento.strftime('%d/%m/%Y')}")

            self.result_layout.addRow(label, valor_label)
            self.result_layout.addRow(data_label, QLabel(""))  # Espaço em branco entre as informações

        self.layout.addLayout(self.result_layout)

    def calcular_data_vencimento(self, data_inicial, num_parcelas):
        data_vencimentos = []
        for i in range(num_parcelas):
            data_vencimento = data_inicial + datetime.timedelta(days=30 * (i + 1))
            data_vencimentos.append(data_vencimento)
        return data_vencimentos

def main():
    app = QApplication(sys.argv)
    window = VendasApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
