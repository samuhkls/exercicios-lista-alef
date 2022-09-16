# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.
numero = []
pares = []
impares = []

for i in range(20):
    i = int(input('digite um valor: '))
    numero.append(i)

    if i % 2 == 0:
        pares.append(i)
        
    else:
        impares.append(i)

print(numero)
print(pares)
print(impares)
