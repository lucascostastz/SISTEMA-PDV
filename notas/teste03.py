from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QWidget
from PyQt6.QtCore import Qt, QDate

class ParcelasApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Inserir Parcelas')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_quantidade = QLabel('Quantidade de Parcelas:')
        self.input_parcelas = QLineEdit()

        self.label_valor = QLabel('Valor Total:')
        self.input_valor = QLineEdit()

        self.label_data = QLabel('Data de Vencimento Inicial:')
        self.input_data = QLineEdit()

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Parcela', 'Valor', 'Data de Vencimento'])

        self.layout.addWidget(self.label_quantidade)
        self.layout.addWidget(self.input_parcelas)
        self.layout.addWidget(self.label_valor)
        self.layout.addWidget(self.input_valor)
        self.layout.addWidget(self.label_data)
        self.layout.addWidget(self.input_data)
        self.layout.addWidget(self.table)

        self.input_parcelas.textChanged.connect(self.inserir_parcelas)

        self.central_widget.setLayout(self.layout)

    def inserir_parcelas(self):
        self.table.setRowCount(0)  # Limpa as linhas atuais

        try:
            num_parcelas = int(self.input_parcelas.text())
            valor_total = float(self.input_valor.text())
            data_inicial = self.input_data.text()

            if num_parcelas <= 0 or valor_total <= 0:
                return

            data = QDate.fromString(data_inicial, "yyyy-MM-dd")

            valor_parcela = valor_total / num_parcelas

            for i in range(1, num_parcelas + 1):
                self.table.insertRow(self.table.rowCount())
                self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(str(i)))
                self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(f'{valor_parcela:.2f}'))
                self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(data.toString("yyyy-MM-dd")))

                data = data.addDays(30)  # Incrementa a data de vencimento em 30 dias (pode ser ajustado conforme necessário)
        except (ValueError, ZeroDivisionError):
            pass

def main():
    app = QApplication([])
    window = ParcelasApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
