numeros=(int(input('digite um numero: ')), int(input('digite um numero: ')), int(input('digite um numero: ')), int(input('digite um numero: ')))
print(numeros)
nove=0
par=0
t=0
for i in range(0, 4, +1):
    if numeros[i]==9:
        nove+=1
    elif numeros[i]%2==0:
        par+=1
    elif numeros[i]==3 and t==0:
        t=i
print(f'tem {par} pares, o nove aparece {nove} vezes e o três aparece primeiro na posição {t}') 