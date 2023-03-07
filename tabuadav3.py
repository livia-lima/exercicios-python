while True:
    número = int(input('Digite um número: '))

    # verifica se o número é negativo antes de realizar a tabuada
    if número < 0:
        break

    for c in range(1, 11):  # cálculo da tabuada
        print(número * c)
