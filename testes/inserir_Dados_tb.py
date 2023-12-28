import mysql.connector
import sqlite3
import random


def criar_tabelas():
  bc = sqlite3.connect('banco.db')
  cur = bc.cursor() 
  cur.execute("SELECT *FROM informacoes")
  dados_lidos = cur.fetchall()
  ip = dados_lidos[0][0]
  porta = dados_lidos[0][1]
  usuario = dados_lidos[0][2]
  senha = dados_lidos[0][3]
  banco = mysql.connector.connect(
  host=ip,
  user=usuario,
  port=porta,
  password=senha)
  # Crie um objeto cursor
  mycursor = banco.cursor()
  for _ in range(15):
      id = 'id' + str(random.randint(1, 100))
      nome = 'Cliente' + str(random.randint(1, 100))
      cpf = str(random.randint(10000000000, 99999999999))
      rg = str(random.randint(100000000, 999999999))
      telefone = str(random.randint(1000000000, 9999999999))
      email = 'cliente' + str(random.randint(1, 100)) + '@example.com'
      cep = str(random.randint(10000000, 99999999))
      endereco = 'Rua ' + str(random.randint(1, 100))
      numero = str(random.randint(1, 100))
      bairro = 'Bairro' + str(random.randint(1, 10))
      cidade = 'Cidade' + str(random.randint(1, 5))
      estado = 'Estado' + str(random.randint(1, 3))
      credito = str(random.uniform(1000, 5000))
      credito_utilizado = str(random.uniform(0, 500))
      credito_saldo = str(float(credito) - float(credito_utilizado))
      mycursor.execute("INSERT INTO pdv.clientes VALUES (idclientes, nome,cpf,rg,telefone,email,cep,endereco,numero,bairro,cidade,estado,credito,credito_utilizado,credito_saldo) VALUES('" +
                    id+"','"+nome+"',,'"+cpf+"','"+rg+"','"+telefone+"','"+email+"','"+cep+"','"+endereco+"','"+numero+"','"+bairro+"','"+cidade+"','"+estado+"', '"+credito+"', '"+credito_utilizado+"', '"+credito_saldo+"')")
      

      banco.commit()
      mycursor.close() 
      banco.close()
criar_tabelas()

