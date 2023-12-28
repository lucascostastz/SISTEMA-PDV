import datetime

def calcular_data_vencimento(data_inicial, num_parcelas):
    data_vencimentos = []
    for i in range(num_parcelas):
        data_vencimento = data_inicial + datetime.timedelta(days=30 * (i + 1))  # Parcelas a cada 30 dias
        data_vencimentos.append(data_vencimento)
    return data_vencimentos

def main():
    valor_venda = float(input("Digite o valor da venda: R$ "))
    num_parcelas = int(input("Digite o número de parcelas: "))
    data_atual = datetime.date.today()

    data_vencimentos = calcular_data_vencimento(data_atual, num_parcelas)
    valor_parcela = valor_venda / num_parcelas

    for i, data_vencimento in enumerate(data_vencimentos):
        print(f"Parcela {i + 1} - Valor: R$ {valor_parcela:.2f} - Data de Vencimento: {data_vencimento.strftime('%d/%m/%Y')}")

if __name__ == "__main__":
    main()
