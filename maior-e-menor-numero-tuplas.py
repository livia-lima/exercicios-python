import random

'''

01 - gerar um número aleatório que esteja entre 1 e 10.
pra fazer uma tupla com 5 números aleatórios, colocar o
random.randint 5 vezes dentro da variável
(solução do guanabara)

'''
num = (random.randint(1, 10), random.randint(1, 10), random.randint(
    1, 10), random.randint(1, 10), random.randint(1, 10))

# 02 - mostrar a listagem dos números
print(f'Os seguintes números foram sorteados: {num}')

# 03 - maior e menor valor
print(f'O menor valor sorteado foi {min(num)}, e o maior foi {max(num)}')
