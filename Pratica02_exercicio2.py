#2- Calculadora de Desconto
#Desenvolva um programa que calcula o desconto em uma loja. 
# Use as seguintes informações:
# Nome do produto: "Camiseta"
# Preço original: R$ 50.00
# Porcentagem de desconto: 20%
#O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

print("Nome do Produto: Camiseta")
print("Preço original: 50")
print("Desconto aplicado: 20 porcento de Desconto") 

valordesconto = (50 * 20)/100
valorfinal = 50 - valordesconto

print("O valor com desconto é: R$" +str(valorfinal))
