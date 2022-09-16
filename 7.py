# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

mult = 1
numeros = []

for i in range(5):
    
    i = int(input('digite um valor: '))
    numeros.append(i)
    print(numeros)

soma = sum(numeros)
print(soma)
multiplicacao = []

for i in numeros:  
    
    mult = numeros[i-1] * mult
    multiplicacao.append(mult)

print(f'os numeros foram {numeros}\n a soma deles é {soma}\n a multiplicação é {multiplicacao[4]}')
