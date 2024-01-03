import mysql.connector
import sqlite3
import random

def criar_tabelas():
    bc = sqlite3.connect('banco.db')
    cur = bc.cursor() 
    cur.execute("SELECT * FROM informacoes")
    dados_lidos = cur.fetchall()
    ip = dados_lidos[0][0]
    porta = dados_lidos[0][1]
    usuario = dados_lidos[0][2]
    senha = dados_lidos[0][3]
    
    banco = mysql.connector.connect(
        host=ip,
        user=usuario,
        port=porta,
        password=senha,
        database='pdv'  # Assuming 'pdv' is the name of your database
    )
    
    # Create a cursor object
    mycursor = banco.cursor()

    nomes_reais = [
    "Ana", "Antônio", "Beatriz", "Bruno", "Carla", "Carlos", "Clara", "Daniel", "Débora", "Eduardo",
    "Fernanda", "Felipe", "Gabriela", "Gustavo", "Helena", "Henrique", "Isabela", "João", "Juliana", "Lucas",
    "Larissa", "Leonardo", "Lívia", "Marcelo", "Mariana", "Mateus", "Natália", "Nicolas", "Patrícia", "Pedro",
    "Priscila", "Rafael", "Raquel", "Renato", "Roberta", "Rodrigo", "Sabrina", "Samuel", "Sofia", "Thiago", "Vanessa",
    "Vinícius", "Viviane", "Wagner", "Yasmin", "Zé Carlos"
]

    for _ in range(50):
        nome = random.choice(nomes_reais)
        cpf = str(random.randint(10000000000, 99999999999))
        rg = str(random.randint(100000000, 999999999))
        telefone = str(random.randint(1000000000, 9999999999))
        email = nome.lower() + str(random.randint(1, 100)) + '@example.com'
        cep = str(random.randint(10000000, 99999999))
        endereco = 'Rua ' + str(random.randint(1, 100))
        numero = str(random.randint(1, 100))
        bairro = 'Bairro' + str(random.randint(1, 10))
        cidade = 'Cidade' + str(random.randint(1, 5))
        estado = 'Estado' + str(random.randint(1, 3))
        credito = '1000.00'
        credito_utilizado = '0.00'
        credito_saldo = '1000.00'
        sql = "INSERT INTO pdv.clientes (nome,cpf,rg,telefone,email,cep,endereco,numero,bairro,cidade,estado,credito,credito_utilizado,credito_saldo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (nome, cpf, rg, telefone, email, cep, endereco, numero, bairro, cidade, estado, credito, credito_utilizado, credito_saldo)

        mycursor.execute(sql, values)
        banco.commit()

    mycursor.close() 
    banco.close()

criar_tabelas()
