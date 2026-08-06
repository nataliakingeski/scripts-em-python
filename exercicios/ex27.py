distancia=float(input('digite a distancia: '))
if distancia<=200:
    print('a passagem custará R${}'.format(distancia*0.50))
else:
    print('a passagem custará R${}'.format(distancia*0.45))