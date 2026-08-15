n=int(input('digite um numero: '))
if (n%2==0 or n%3==0) and n!=2 and n!=3 and n!=0:
    print('o numero não é primo')
else:
    print('o numero é primo')