import mysql.connector

# Conecte-se ao banco de dados MySQL
connection = mysql.connector.connect(
    host="192.168.1.2",
    port="1001",
    user="LUCAS",
    password="THMPV.2022",
    database="pdv"
)

# Crie um objeto cursor
cursor = connection.cursor()

# Defina o novo valor de crédito para o cliente "Lucas"
novo_credito = 1000  # Substitua pelo valor desejado

# Atualize o valor de crédito para o cliente "Lucas" com ID 11
sql = "UPDATE clientes SET credito_utilizado = %s WHERE idclientes = %s"
valores = (novo_credito, 11)

cursor.execute(sql, valores)

# Faça o commit das alterações no banco de dados
connection.commit()

# Feche o cursor e a conexão
cursor.close()
connection.close()