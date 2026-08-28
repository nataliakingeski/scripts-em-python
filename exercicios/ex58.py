numeros = [[],[]]
for i in range(0, 7,+1):
    n=int(input('digite um numero: '))
    if n%2==0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'os numeros impares são {numeros[1]} e os pares são {numeros[0]}')