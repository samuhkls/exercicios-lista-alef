# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vogais = ['a', 'e', 'i', 'o', 'u']

palavra = input("digite a palavra: ")

consoantes = 0

for i in range(len(palavra)):

    if palavra[i] in vogais:
        pass
    else:
        print(palavra[i])
        consoantes += 1

print(f'em {palavra} tem {consoantes} consoantes')
