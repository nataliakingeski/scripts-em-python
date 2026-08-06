frase=input('digite uma frase: ').lower()
print('possui {} letras A'.format(frase.count('a')))
print('a primeira letra A aparece na posição ', frase.find('a')+1)
print('a ultima letra A aparece na posição ', frase.rfind('a')+1)
