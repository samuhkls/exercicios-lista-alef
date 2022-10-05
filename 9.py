"""Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    Telefonou para a vítima?"
    Esteve no local do crime?"
    Mora perto da vítima?" 
    Devia para a vítima?"
    Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5
como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
respostas = []
num = 0

for i in range(len(perguntas)):
    x = int(input(f"\nPergunta N°{i+1} {perguntas[i]}\n1. Sim\n2. Não\n   Insira o número da alternativa: "))
    respostas.append(x)
    if x == 1:
        num =+ 1

if respostas.count(1) < 2:
    classificacao = "Inocente"
elif respostas.count(1) == 2:
    classificacao = "Suspeito"
elif respostas.count(1) == 3 or respostas.count(1) == 4:
    classificacao = "Cumplice"
elif respostas.count(1) == 5:
    classificacao = "Assassino"
print(f"\nEntão você é o {classificacao}")
