palavras=('carta', 'casa', 'dado', 'livro')
for i in palavras:
    print(f'\nNa palavra {i} temos ', end='')
    for l in i:
        if l in 'aeiou':
            print(l, end=' ')