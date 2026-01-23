import requests

try:
    resposta = requests.get("https://randomuser.me/api/", timeout=5)
    
    resposta.raise_for_status()
    
    dados = resposta.json()
    
    usuario = dados["results"][0]
    
    nome = f'{usuario["name"]["first"]} {usuario["name"]["last"]}'
    email = usuario["email"]
    pais = usuario["location"]["country"]
    
    print("Usuário encontrado:")
    print("Nome:", nome)
    print("E-mail:", email)
    print("País:", pais)

except requests.exceptions.RequestException:
    print(" Tente novamente mais tarde.")
