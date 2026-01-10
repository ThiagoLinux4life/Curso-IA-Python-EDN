#1- Conversor de Moeda
#Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
# Valor em reais: R$ 100.00
# Taxa do dólar: R$ 5.20
# Taxa do euro: R$ 6.15
#O programa deve calcular e exibir os valores convertidos, 
#arredondando para duas casas decimais.

valor = float(input("Entre com valor em Reais: "))

dolares = valor/5.20
euros = valor/6.15

print(f" O valor em Dolares é: ${dolares:.2f}")
print(f" O valor em Euros é : €{euros:.2f}")