a=int(input('digite o comprimento da primeira reta: '))
b=int(input('digite o comprimento da segunda reta: '))
c=int(input('digite o comprimento da terceira reta: '))
if a+b>c and b+c>a and c+a>b:
    print('é um triângulo')
else:
    print('não é um triângulo')