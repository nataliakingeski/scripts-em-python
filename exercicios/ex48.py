true=1
while true==1:
    n=int(input('digite um numero: '))
    if n > 0:
        for i in range(1, 11, +1):
            print('{} x {} = {}'.format(n, i, n*i))
    else:
        break
