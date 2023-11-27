import sqlite3
import mysql.connector


class Classe_Banco(object):
    def __init__(self):
        super().__init__()

    def conectar(self):
        try:
            bc = sqlite3.connect('banco.db')
            cur = bc.cursor() 
            cur.execute("SELECT *FROM informacoes")
            dados_lidos = cur.fetchall()
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
            self.cursorr = self.query.cursor() 
            cur.close()
        except mysql.connector.Error as err:
            print("Erro no banco de dados")