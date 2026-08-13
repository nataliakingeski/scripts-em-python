idade=int(input('digite a idade do atleta: '))
if idade<=5:
    print('categoria mirim')
elif idade<=10:
    print('categoria infantil')
elif idade<=16:
    print('categoria junior')
elif idade<=20:
    print('categoria sênior')
else:
    print('categoria master')