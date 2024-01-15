import mysql.connector
import random
from faker import Faker

def inserir_dados_produtos():
    # Configurações do banco de dados
    config = {
        'host': '127.0.0.1',
        'user': 'LUCAS',
        'password': 'THMPV.2022',
        'database': 'pdv',
        'port': '1001'
    }

    banco = mysql.connector.connect(**config)
    cursor = banco.cursor()

    cursor.execute('SELECT credito_utilizado FROM clientes')
    valores = cursor.fetchall()
    soma_credito = sum(float(valor[0]) for valor in valores)
    print(f"Soma do crédito utilizado: {soma_credito:.2f}")
        
    """  # Criação do objeto Faker para gerar dados fictícios em português
    faker = Faker('pt_BR')

    produtos = [
    "Arroz",
    "Feijão",
    "Macarrão",
    "Carne bovina",
    "Frango",
    "Peixe",
    "Ovos",
    "Leite",
    "Queijo",
    "Manteiga",
    "Pão",
    "Café",
    "Chá",
    "Açúcar",
    "Sal",
    "Óleo de cozinha",
    "Tomate",
    "Cebola",
    "Alho",
    "Batata",
    "Cenoura",
    "Maçã",
    "Banana",
    "Laranja",
    "Suco de laranja",
    "Refrigerante",
    "Água mineral",
    "Iogurte",
    "Granola"
]



    for _ in range(50):
        # Gerar dados fictícios
        nome = random.choice(produtos)
        categoria = faker.word()
        marca = faker.word()
        estoque = random.randint(1, 100)
        codigo = faker.uuid4()
        preco = round(random.uniform(1, 30), 2)
        v_atacado = round(preco * 0.9, 2)  # 90% do preço
        qm_atacado = random.randint(5, 20)
        data_cadastro = faker.date_this_decade()

        # Inserir dados na tabela
        sql = "INSERT INTO produtos (descricao, categoria, marca, estoque, codigo, preco, v_atacado, qm_atacado, data_cadastro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (nome, categoria, marca, estoque, codigo, preco, v_atacado, qm_atacado, data_cadastro)

        cursor.execute(sql, values)
        banco.commit()

    cursor.close()
    banco.close()

# Chame a função para inserir os dados """
inserir_dados_produtos()