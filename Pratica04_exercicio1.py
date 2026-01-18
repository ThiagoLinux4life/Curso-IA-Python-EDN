#1 - Criar um código que 
# faça uma calculadora que 
# tenha as operações básicas(+,-,*,/).

numero1 = int(input("Entre com o Primeiro Numero: "))
operação = input("Entre com a operação desejada: ")
numero2 = int(input("Entre com segundo número: "))


if operação == "+":
    soma = numero1 + numero2 
    print("A soma do", numero1, "e", numero2, "é:" , soma)

if operação == "-":
    menos = numero1 - numero2
    print("A subtração do", numero1, "e", numero2, "é:" , menos)

if operação == "x":
    vezes = numero1*numero2
    print("A multiplicação de", numero1 , "e" , numero2, "é:", vezes)

if operação == ":":
    if numero2 == 0:
        print("Erro: não é possível dividir por zero.")
    else:
        dividir = numero1 / numero2
        print("A divisão de", numero1, "e", numero2, "é:", dividir)






