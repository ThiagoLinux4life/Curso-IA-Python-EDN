import csv

pessoas = [
    ["Ana Silva", 28, "São Paulo"],
    ["Carlos Souza", 35, "Rio de Janeiro"],
    ["Mariana Lima", 22, "Belo Horizonte"]
]

nome_arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")

try:
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Cidade"])

        escritor.writerows(pessoas)

    print(f"Arquivo '{nome_arquivo}' gravado com sucesso!")

except IOError:
    print("Erro ao escrever no arquivo. Verifique permissões ou o nome do arquivo.")
