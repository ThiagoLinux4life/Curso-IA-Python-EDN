import requests

cep = input("Digite o CEP (somente números): ").strip()

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()  # verifica erro HTTP

    dados = resposta.json()

    if "erro" in dados:
        print(" CEP não encontrado.")
    else:
        print("\n Endereço encontrado:")
        print("Logradouro:", dados.get("logradouro"))
        print("Bairro:", dados.get("bairro"))
        print("Cidade:", dados.get("localidade"))
        print("Estado:", dados.get("uf"))

except requests.exceptions.RequestException:
    print(" Verifique sua conexão ou tente novamente.")
