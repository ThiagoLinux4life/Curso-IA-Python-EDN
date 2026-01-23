 import json
    
nome_arquivo = input("Digite o nome do arquivo JSON (ex: pessoa.json): ")

try:
    with open(nome_arquivo, mode="w", encoding="utf-8") as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

    print(f"Arquivo '{nome_arquivo}' salvo com sucesso!\n")

    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        dados_lidos = json.load(arquivo)

    print("Dados carregados do arquivo JSON:")
    print(dados_lidos)

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")

except IOError:
    print("Erro ao escrever ou ler o arquivo.")

except json.JSONDecodeError:
    print("Erro ao interpretar o conteúdo do arquivo JSON.")

except Exception as erro:
    print("Ocorreu um erro inesperado:", erro)

