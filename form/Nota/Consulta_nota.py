import requests

# Defina as credenciais de acesso à API do Asaas
access_token = '$aact_YTU5YTE0M2M2N2I4MTliNzk0YTI5N2U5MzdjNWZmNDQ6OjAwMDAwMDAwMDAwMDAyODUyMjI6OiRhYWNoXzhiMjUyMjdiLTk4MWYtNGU3Mi05ZGJhLTBiYzE1MjczYzExNQ=='

# Defina o ID da nota fiscal que você deseja consultar
invoice_id = '124'

# Faça uma requisição GET para a API do Asaas, passando o access_token e o invoice_id como parâmetros da URL
response = requests.get(f'http://www.asaas.com/api/v3/invoices/{invoice_id}', headers={'access_token': access_token})

# Verifique se a resposta da API foi bem-sucedida
if response.status_code == 200:
    
    # Faça o que desejar com os dados da nota fiscal, como imprimi-los na tela
    print(response)
else:
    print(f'Erro {response.status_code}: {response.json()["errors"][0]["description"]}')
