from random import randint
n = (randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100))
print('os numeros sorteados foram ', end='')
menor=100
maior=0
for i in n:
    print(f'{i}', end=' ')
print(f'o maior é: {max(n)}')
print(f'o menor é: {min(n)}')