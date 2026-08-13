n1=float(input('digite sua primeira nota: '))
n2=float(input('digite sua segunda nota: '))
m = (n1+n2)/2
if m<=4:
    print('você foi reprovado')
elif m<7:
    print('você está em recuperação')
else:
    print('você passou')