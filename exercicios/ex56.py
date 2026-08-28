lista=[]
par=[]
impar=[]
for i in range(0,10, +1):
    n=int(input('digite um numero: '))
    lista.append(n)
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
print(f'a lista completa {lista}')
print(f'só os pares {par}')
print(f'só os impares {impar}')