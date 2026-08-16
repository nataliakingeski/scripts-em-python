peso=float(input('digite seu peso: '))
maior=peso
menor=peso
for i in range(1, 5, +1):
    peso=float(input('digite seu peso: '))
    if peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
print('o menor peso é: {} e o maior é: {}'.format(menor,maior))