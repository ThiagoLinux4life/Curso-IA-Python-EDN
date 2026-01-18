#2 - Criar um código que 
# registre as notas de alunos 
# e calcular a média da turma.

nota1 = int(input("Entre com a primeira nota: "))
nota2 = int(input("Entre coma segunda nota: "))

media = (nota1+nota2)/2

if media >=7:
    print("Sua media foi", media, "você passou de ano")

if media ==6:
    print("Sua media foi:", media, "você esta de recuperação")

if media <6:
    print("Sua media foi:", media , "você foi reprovado!")