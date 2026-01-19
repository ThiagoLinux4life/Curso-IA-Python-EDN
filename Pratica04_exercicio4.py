#4 - Criar um código que serve para 
# analisar números digitados pelo usuário, 
# classificando-os como pares ou ímpares e 
# contabilizando quantos de cada tipo foram inseridos.

pares = 0
impares = 0

print("Digite números inteiros (digite 0 para encerrar):")

for _ in range(100):
    numero = int(input("Número: "))

    if numero == 0:
        break
    elif numero % 2 == 0:
        print("Par")
        pares += 1
    else:
        print("Ímpar")
        impares += 1

print("\nResultado final:")
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
