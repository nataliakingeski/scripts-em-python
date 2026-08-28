n=[]
quant=int(input('quantos numeros você deseja digitar? '))
for i in range(0, quant, +1):
    n1=int(input('digite um numero: '))
    if n1 in n:
        print(end='')
    else:
        n.append(n1)
n.sort()
print(f'em ordem fica {n}')