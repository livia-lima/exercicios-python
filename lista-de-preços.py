# tupla única com o nome  do produto + preço
listagem = 'Caderno 12 matérias', 6.99, 'Lápis', 1.99, 'Borracha', 0.99, 'Caneta bic', 0.25, 'Caneta de gel', '4.99'

print('-'*30)
print('\033[7;30;44mLISTAGEM DE PREÇOS - PAPELARIA\033[m')
print('-'*30)

for posição in range(len(listagem)):
    if posição % 2 == 0:
        print(f'\033[0;34m{listagem[posição]:.<30}\033[m', end='')
    else:
        print(f'\033[0;33m{listagem[posição]:.>5}\033[m')
