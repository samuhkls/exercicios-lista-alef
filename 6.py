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
