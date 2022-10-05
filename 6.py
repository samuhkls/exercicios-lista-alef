<<<<<<< HEAD
#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
#imprima o número de alunos com média maior ou igual a 7.0.
import random
import math

lista = []
tempMedia = 0
media = []
aluno = 0

for i in range(40):
    x = round(random.uniform(0.0, 10.0),1)
    lista.append(x)
    aluno = aluno + 1
    
    if aluno == 4:
        print(lista)
        for i in range(aluno):
            tempMedia = tempMedia + lista[i]
        media.append(round((tempMedia/aluno),1))

        #Limpando
        tempMedia=0
        lista.clear()
        aluno=0
        
print(media)
for i in range(len(media)):
    if media[i] >= 7:
        print(f"\nO aluno aluno {i+1} teve uma nota igual ou superior a 7 (nota: {media[i]})")
=======
# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []
a = 0

for i in range(10):
    nota1 = float(input('digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    nota3 = float(input('digite a terceira nota: '))
    nota4 = float(input('digite a quarta nota: '))
    res = (nota1 + nota2 + nota3 + nota4)/4
    medias.append(res)

for i in medias:
    if i >=7:
        a =+ 1

print(f'{a} alunos foram aprovados')
>>>>>>> 055edf86ad2cc500a532757b559606377b2734ee
