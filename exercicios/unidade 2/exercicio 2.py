faltas = int(input("Faltas do aluno: "))
media = float(input("Qual a media do aluno: "))

m = 6.0
al = 200

if faltas > (al*0.75):
    print("O aluno foi REPROVADO")

elif media < m or faltas > (al*0.75):
    print("O aluno foi REPROVADO")

elif faltas < (al*0.75):
    print("O aluno foi APROVADO <3")
