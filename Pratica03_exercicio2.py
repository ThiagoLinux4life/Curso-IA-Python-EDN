#2- Calculadora de IMC

#Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
#O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
#calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

#18.5: classificacao = "Abaixo do peso"
# 25: classificacao = "Peso normal"
# 30: classificacao = "Sobrepeso"
#para os demais cenários: classificacao = "Obeso"

massa = int(input("Entre com seu peso: "))
altura = float(input("Entre com sua Altura: "))

imc = massa/altura

if imc <= 18.5:
    print("Seu IMC esta em: " + str(int(imc)) +  "Você está Abaixo do Peso")

elif  18.5 <= imc <= 25:
    print("Seu IMC esta em: " + str(int(imc)) +  "Você esta com peso Normal ")

else:
    print("Seu IMC esta em: " + str(int(imc)) + "Você esta com Sobrepeso!")
          