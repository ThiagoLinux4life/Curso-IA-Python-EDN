#1 - Crie um programa que gere senhas aleatórias com letras,
#  números e símbolos e que o usuário  
# também escolha o tamanho da senha  
# para criar senhas seguras automaticamente.

import random
import string


letras = string.ascii_letters     
numeros = string.digits            
simbolos = string.punctuation      

todos_caracteres = letras + numeros + simbolos

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))

senha = ""


for i in range(tamanho_senha):
    caractere_aleatorio = random.choice(todos_caracteres)
    senha = senha + caractere_aleatorio

# Saída
print("Senha gerada:", senha)
