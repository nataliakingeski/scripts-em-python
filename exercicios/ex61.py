from random import randint
jogos = int(input('quantos jogos você deseja gerar? '))
numeros = list()
lnum = list()
for i in range (0, jogos, +1):
    for n in range (0, 6, +1):
        num = randint(1, 61)
        numeros.append(num)
    lnum.append(numeros[:])
    numeros = []
print(f'os jogos gerados são esses : {lnum}')