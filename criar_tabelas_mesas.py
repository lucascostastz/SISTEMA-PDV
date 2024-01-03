import mysql.connector

def criar_tabelas(num_tabelas):
    # Configurações de conexão com o banco de dados MySQL
    config = {
        'host': '127.0.0.1',
        'port': '1001',
        'user': 'LUCAS',
        'password': 'THMPV.2022',
        'database': 'pdv'
    }

    # Conecta ao banco de dados
    conexao = mysql.connector.connect(**config)
    cursor = conexao.cursor()

    # Loop para criar as tabelas
    for i in range(1, num_tabelas + 1):
        nome_tabela = f'mesa{i}'

        # Consulta SQL para criar a tabela
        sql = f'''
            CREATE TABLE {nome_tabela} (
                idmesa INT AUTO_INCREMENT PRIMARY KEY,
                cliente VARCHAR(50), 
                produto VARCHAR(50),
                quantidade VARCHAR(25),
                valor_unitario VARCHAR(25),
                valor_total VARCHAR(25)

            )
        '''

        # Executa a consulta
        cursor.execute(sql)
        print(f'Tabela {nome_tabela} criada com sucesso.')

    # Fecha a conexão com o banco de dados
    cursor.close()
    conexao.close()

# Exemplo de uso: criar 3 tabelas
criar_tabelas(30)
