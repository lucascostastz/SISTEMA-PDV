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

# Defina o ID que deseja selecionar
id_cliente = 11  # Substitua pelo ID desejado

# Execute a consulta para obter os valores de "credito" e "credito_saldo" para o ID selecionado
sql = "SELECT credito, credito_utilizado FROM clientes WHERE idclientes = %s"
valores = (id_cliente,)

cursor.execute(sql, valores)

# Recupere os resultados
resultado = cursor.fetchone()

if resultado:
    credito, credito_utilizado= resultado
    print(f"ID do Cliente: {id_cliente}")
    print(f"Credito: {credito}")
    print(f"Credito Saldo: {credito_utilizado}")
    credito_saldo = float(credito) - float(credito_utilizado)
    print(credito_saldo)
else:
    print(f"Cliente com ID {id_cliente} não encontrado")

# Feche o cursor e a conexão
cursor.close()
connection.close()