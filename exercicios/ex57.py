pessoa = list()
pessoas = list()
pesadas = list()
leves = list()
for i in range(0, 5, +1):
    nome = input('digite seu nome: ')
    peso = float(input('digite seu peso: '))
    pessoa.append(nome)
    pessoa.append(peso)
    pessoas.append(pessoa[:])
    if peso > 70:
        pesadas.append(nome)
    else:
        leves.append(nome)
print(f'foram cadastradas {len(pessoas)} pessoas')
print(f'os mais pesadas são {pesadas} e os mais leves são {leves}')