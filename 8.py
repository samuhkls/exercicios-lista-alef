"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
"""
pessoas = []

for i in range(10):
    altura = float(input('digite a altura: '))
    peso = float(input('digite o peso: '))
    pessoas.append(altura)
    pessoas.append(peso)

print(pessoas[::-1])


