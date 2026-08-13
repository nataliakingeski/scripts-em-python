sal=float(input('digite seu salario: '))
casa=float(input('qual o valor da casa: '))
anos=int(input('digite a quantidade de anos que você pretende ficar pagando: '))
parc=(casa/anos)/12
if (sal*30)/100 < parc:
    print('você não poderá comprar a casa')
else:
    print('você poderá comprar a casa')