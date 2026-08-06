v=int(input('digite a quantos quilometros por hora você esta: '))
if v>80:
    multa= 7*(v-80)
    print('você terá que pagar R${},00 de multa'.format(multa))
else:
    print('você está no limite de velocidade')