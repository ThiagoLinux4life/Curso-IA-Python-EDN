#2-Crie uma função que verifique se uma palavra ou frase é um palíndromo 
# (lê-se igual de trás para frente, 
# ignorando espaços e pontuação). 
# Se o resultado é True, responda “Sim”, 
# se o resultado for False, responda “Não”.

def eh_palindromo(texto):
    texto_limpo = ""
    texto_invertido = ""

    for caractere in texto:
        if caractere.isalnum():
            texto_limpo = texto_limpo + caractere.lower()

    for caractere in texto_limpo:
        texto_invertido = caractere + texto_invertido

    if texto_limpo == texto_invertido:
        return True
    else:
        return False


entrada = input("Digite uma palavra ou frase: ")

resultado = eh_palindromo(entrada)

if resultado == True:
    print("Sim")
else:
    print("Não")