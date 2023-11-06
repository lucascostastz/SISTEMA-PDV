import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QLineEdit, QWidget
from PyQt6.QtCore import Qt

class DatabaseSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initDatabaseConnection()

    def initUI(self):
        self.setWindowTitle('Search in Database')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.textChanged.connect(self.searchDatabase)
        self.layout.addWidget(self.search_input)

        self.table_widget = QTableWidget()
        self.table_widget.cellClicked.connect(self.onCellClicked)  # Conecta o evento de clique de célula
        self.layout.addWidget(self.table_widget)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def initDatabaseConnection(self):
        self.db = mysql.connector.connect(
            host='192.168.1.2',
            port=1001,
            user='LUCAS',
            password='THMPV.2022',
            database='pdv'
        )

    def searchDatabase(self):
        cursor = self.db.cursor()
        search_text = self.search_input.text()
        query = f"SELECT * FROM clientes WHERE nome LIKE '%{search_text}%'"
        cursor.execute(query)
        result = cursor.fetchall()

        self.table_widget.setRowCount(len(result))
        self.table_widget.setColumnCount(len(result[0]))

        for i, row in enumerate(result):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(i, j, item)

        cursor.close()

    def onCellClicked(self, row, column):
        if column == 1:  # Supondo que a coluna com o nome esteja na segunda coluna (índice 1)
            item = self.table_widget.item(row, column)
            name = item.text()
            print(f"Nome na linha {row}: {name}")

def main():
    app = QApplication(sys.argv)
    window = DatabaseSearchApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
