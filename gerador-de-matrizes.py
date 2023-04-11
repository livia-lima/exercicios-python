'''
o programa conta com três parâmetros: número de linhas, número de colunas e
o valor a ser colocado
'''
num_linhas = int(input('Digite o número de linhas: '))
num_colunas = int(input('Digite o número de colunas: '))
valor = int(input('Digite o valor a ser colocado: '))

matriz: list[int] = []  # lista vazia para armazenar as linhas da matriz
for i in range(num_linhas):  # cria a linha i
    linha: list[int] = []  # a linha i em si
    for j in range(num_colunas):
        linha.append(valor)
    matriz.append(linha)
print(matriz)
