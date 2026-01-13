#4- Verificador de Ano Bissexto
#Faça um programa que determine se um ano inserido pelo usuário é 
# bissexto ou não.
#Um ano é bissexto se for divisível por 4, 
# exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

ano = int(input("Entre com o ano: "))
print(" Verificando se o", ano , "é Bissexto. Aguarde...")

if 0 == ano%4:
    print(" O" , ano ,"é bissexto")

if 0 == ano%100:
   print("Este ano é centenário!")

else:
    print("É um ano Normal!")