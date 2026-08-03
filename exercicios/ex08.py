litro=2
l=int(input('digite a largura da parede: '))
a=int(input('digite a altura da parede: '))
area=l*a
print('você precisará de {} litros de tinta'.format(area//litro))