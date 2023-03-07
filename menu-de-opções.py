# ler dois valores
primeirovalor = int(input('Digite o primeiro valor: '))
segundovalor = int(input('Digite o segundo valor: '))

# ler a opção
opção = int(input('Informe a sua opção: '))

while opção != 5:
    # menu de opções
    print('''   -------- OPÇÕES --------'
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior')
    [ 4 ] novos números
    [ 5 ] sair do programa
    -----------------------''')

    if opção == 1:
        print(primeirovalor + segundovalor)
    if opção == 2:
        print(primeirovalor * segundovalor)
