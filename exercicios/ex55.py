numeros=[]
for i in range(0, 10, +1):
    n = int(input('digite um numero: '))
    numeros.append(n)
print(f'foram digitados {len(numeros)} numeros')
if 5 in numeros:
    print('o numero 5 foi digitado')
else:
    print('o numero 5 não foi digitado')
numeros.sort(reverse=True)
print(numeros)