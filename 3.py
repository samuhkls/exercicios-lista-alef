# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(4):
    i = int(input('digite a nota que voce tirou'))
    notas.append(i)

media = (sum(notas))/4
print(media)
