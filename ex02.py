n=int(input('digite um numero: '))
e=int(input('1- ver antecessor\n2- ver sucessor\n3- ver antecessor e sucessor\n'))
def obter_e(e):
    if e==1:
        print('o antecessor é: ', n-1)
    elif e==2:
        print('o sucessor é: ', n+1)
    elif e==3:
        print('o antecessor é: ', n-1, 'e o sucessor é: ', n+1)
    else:
        print('opção invalida')