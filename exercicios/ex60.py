soma=0
soma2=0
numeros = [[2, 4, 7], [3, 5, 8], [6, 9, 10]]
for i in range(0, 3, +1):
    for n in range(0, 3, +1):
        print(numeros[i][n], end = ' ')
        soma+=numeros[i][n]
        if n==2:
            soma2+=numeros[i][n]
    print('')
print(soma)
print(soma2)
print(max(numeros[1]))