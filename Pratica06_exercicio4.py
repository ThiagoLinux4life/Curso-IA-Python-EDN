import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, BTC): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()  # Verifica erro HTTP

    dados = resposta.json()
    chave = f"{moeda}BRL"

    if chave not in dados:
        print(" Moeda não encontrada.")
    else:
        cotacao = dados[chave]

        print("\n Cotação da moeda em relação ao Real (BRL)")
        print("-" * 40)
        print(f"Moeda: {cotacao['name']}")
        print(f"Valor atual: R$ {float(cotacao['bid']):.2f}")
        print(f"Máxima do dia: R$ {float(cotacao['high']):.2f}")
        print(f"Mínima do dia: R$ {float(cotacao['low']):.2f}")
        print(f"Data/Hora da última atualização: {cotacao['create_date']}")

except requests.exceptions.RequestException:
    print(" Verifique sua conexão com a internet.")
except ValueError:
    print("Erro ao processar os dados da API.")
