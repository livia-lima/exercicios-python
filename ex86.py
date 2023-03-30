matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# cada [] representa uma linha

# for de alimentação; coloca os valores dentro da matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f'Digite um valor para [{linha}, {coluna}]: '))

# for para organizar o print
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()  # p/ quebrar linha
