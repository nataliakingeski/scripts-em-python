ficha = list()
while True:
    nome = input('nome: ')
    n1 = float(input('nota 1: '))
    n2 = float(input('nota 2: '))
    media = (n1 + n2)/2
    ficha.append([nome, [n1, n2], media])
    resp = input('quer continuar? [s/n]: ')
    if resp in 'Nn':
        break
print(f'{"no.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('mostrar as notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('finalizado')
        break
    if opc <= len(ficha) -1:
        print(f'notas de {ficha[opc][0]} são {ficha[opc][1]}')