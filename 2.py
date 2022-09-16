# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

for a in range(10):
    a = int(input('digite um valor: '))
    lista.append(a)

lista = lista[::-1]
for i in lista:
    print(i)
