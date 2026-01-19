#4 - Crie um programa que calcule 
# a quantos dias um individuo 
# está vivo de acordo com a data do dia.

anofinal = int(input("Entre com o ano Atual: "))
ano_nasc = int(input("Entre com o ano de seu nascimento: "))

idade = anofinal - ano_nasc
totaldedias = idade * 365
print("Você esta com:", idade , "anos e " , totaldedias, "dias vividos")