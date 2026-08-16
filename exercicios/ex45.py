m=0
nome=''
id=0
id2=0
for i in range(1,5, +1):
    name=input('digite seu nome: ')
    sexo=input('digite h se você for homem e m se for mulher: ')
    idade=int(input('digite sua idade: '))
    id2+=idade
    if sexo=='h' and idade>id:
        nome=name
        id=idade
    elif sexo=='m' and idade<20:
        m+=1
print('o homem mais velho é: ', nome)
print('tem {} mulheres que tem menos de 20 anos'.format(m))
print('a média de idade é: ', id2//4)