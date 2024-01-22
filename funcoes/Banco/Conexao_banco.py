import sqlite3
import mysql.connector
from PyQt6.QtWidgets import QMessageBox

class Classe_Banco(object):
    def __init__(self):
        super().__init__()


    def conectar(self):
        try:
            banco_sqlite = sqlite3.connect('banco.db')
            cursor_sqlite = banco_sqlite.cursor() 
            cursor_sqlite.execute("SELECT *FROM informacoes")
            dados_lidos = cursor_sqlite.fetchall()
            self.ip = dados_lidos[0][0]
            self.porta = dados_lidos[0][1]
            self.usuario = dados_lidos[0][2]
            self.senha = dados_lidos[0][3]
            self.database = dados_lidos[0][4]
            self.query = mysql.connector.connect(
                host=self.ip,
                user=self.usuario,
                port=self.porta,
                password=self.senha)
            if self.query.is_connected():
                self.cursorr = self.query.cursor()
            cursor_sqlite.close()
            banco_sqlite.close()
        except:
            self.alerta_erro_conexão()
    

    def desconectar(self):
        if self.query.is_connected():
            self.cursorr.close()
            self.query.close()
            

    def alerta_erro_conexão(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Erro ao conectar ao banco de dados")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
    
    