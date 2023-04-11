'''
o programa conta com três parâmetros: número de linhas, número de colunas e
o valor a ser digitado pelo usuário.
'''
num_linhas = int(input('Digite o número de linhas: '))
num_colunas = int(input('Digite o número de colunas: '))

matriz: list[int] = []  # lista vazia para armazenar as linhas da matriz
for i in range(num_linhas):  # cria a linha i
    linha: list[int] = []  # a linha i em si
    for j in range(num_colunas):
        valor = int(input(f'Digite o elemento [{i, j}]: '))
        linha.append(valor)  # add o valor à linha
    matriz.append(linha)

for i in range(num_linhas):
    for j in range(num_colunas):
        print(f'\033[0;35m[{matriz[i][j]}]\033[m', end='')
    print()
