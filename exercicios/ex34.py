ano=int(input('digite o ano que você nasceu: '))
ano=2026-ano
if ano < 18:
    print('você não precisa se alistar ainda')
elif ano == 18:
    print('já está na hora de se alistar')
else:
    print('já passou do prazo')