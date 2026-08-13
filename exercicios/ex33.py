n1=int(input('digite um numero: '))
n2=int(input('digite mais um numero: '))
if n1>n2:
    print('o maior é ', n1)
    print('o menor é ', n2)
elif n1==n2:
    print('eles são iguais')
else:
    print('o maior é ', n2)
    print('o menor é: ', n1)