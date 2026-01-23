 import csv

nome_arquivo = input("Digite o nome do arquivo CSV a ser lido: ")

try:
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            print(linha)

except FileNotFoundError:
    print("Erro: arquivo não encontrado. Verifique o nome digitado.")

except IOError:
    print("Erro ao tentar ler o arquivo. Verifique as permissões.")

except Exception as erro:
    print("Ocorreu um erro inesperado:", erro)

