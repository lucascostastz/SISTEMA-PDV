from funcoes.Banco.Conexao_banco import Classe_Banco


class Classe_Inicio():
    def pesquisar_produtos():
        banco = Classe_Banco()
        resultados = []
        termo_pesquisa = input("Digite o termo para buscar informações: ")
        banco.conectar()
        banco.cursorr.execute(f"SELECT * FROM pdv.clientes")
        dados_pessoais =banco.cursorr.fetchall()
        banco.query.close()
        banco.cursorr.close()

        for pessoa in dados_pessoais:
            if  termo_pesquisa == '':
                return print("Digite alguma informação.")
            elif termo_pesquisa.lower() in pessoa[1].lower():
                resultados.append(pessoa)
        
        if resultados:
            print("Informações encontradas:")
            for resultado in resultados:
                print("Nome:", resultado[1])
                print("Cpf:", resultado[2])
                print("Telefone:", resultado[4])
                print("Email:", resultado[5])
        else:
            print("Nenhuma informação encontrada para o termo fornecido.")
    pesquisar_produtos()