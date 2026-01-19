#1-Crieu ma função que calcule a gorjeta a ser deixada em um restaurante,
#  baseada no valor total da conta e na porcentagem degorjeta desejada.
#  Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
#Parâmetros:
#a - valor_conta (float): O valor total da conta
#b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
#c - retorna: float: O valor da gorjeta calculada


def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    # Verificação básica dos valores
    if valor_conta > 0 and porcentagem_gorjeta >= 0:
        gorjeta = valor_conta * (porcentagem_gorjeta / 100)
        return gorjeta
    else:
        return 0.0


# Programa principal
valor_conta = float(input("Digite o valor total da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

if valor_gorjeta > 0:
    print("Valor da gorjeta calculada: R$", valor_gorjeta)
elif valor_gorjeta == 0:
    print("Não foi possível calcular a gorjeta. Verifique os valores informados.")
else:
    print("Erro inesperado.")
