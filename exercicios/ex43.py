maior=0
menor=0
for i in range(1,8,+1):
    idade=int(input('digite seu ano de nascimento: '))
    if 2026-idade>=18:
        maior+=1
    else:
        menor+=1
print('tem {} maiores de idade e {} menores de idade'.format(maior,menor))