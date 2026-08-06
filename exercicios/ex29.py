n1=int(input('digite um numero: '))
n2=int(input('digite um numero: '))
n3=int(input('digite um numero: '))
if n1>n2 and n1>n3:
    print('o maior é ', n1)
elif n2>n1 and n2>n3:
    print('o maior é ', n2)
else:
    print('o maior é ', n3)