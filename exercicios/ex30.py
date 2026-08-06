sal=float(input('digite seu salario: '))
if sal>=1.250:
    aum=(sal*10)/100
    print('com o aumento ficou R${:.4}'.format(aum+sal))
else:
    aum=(sal*15)/100
    print('com o aumento ficou R${:.4}'.format(aum+sal))