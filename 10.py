# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar números
# aleatórios, simulando os lançamentos dos dados.

import random

dado = [1, 2, 3, 4, 5, 6]
vezes = [0, 0, 0, 0, 0, 0]
lista = []
for i in range(100):
    x = random.randint(1, 6)
    lista.append(x)
    
for i in lista:
    if i == dado[0]:
        vezes[0] += 1
    elif i == dado[1]:
        vezes[1] += 1
    elif i == dado[2]:
        vezes[2] += 1
    elif i == dado[3]:
        vezes[3] += 1
    elif i == dado[4]:
        vezes[4] += 1
    elif i == dado[5]:
        vezes[5] += 1
        
print(f"\nO número 1 rolou {vezes[0]} \nO número 2 rolou {vezes[1]} \nO número 3 rolou {vezes[2]} \nO número 4 rolou {vezes[3]} \nO número 5 rolou {vezes[4]} \nO número 6 rolou {vezes[5]}")
print(sum(vezes))