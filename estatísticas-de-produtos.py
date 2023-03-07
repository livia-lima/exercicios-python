contador = 0
acumulador = menor = totmil = float(0)
nomemaisbarato = ' '
while True:
    # 01 - ler o nome e o preço de vários produtos
    nome_produto = str(input('Digite o nome do produto: '))
    valor_produto = float(input('Digite o preço do produto: '))
    acumulador += valor_produto
    contador += 1

    print(nome_produto)
    print(valor_produto)

    if valor_produto > 1000.0:
        totmil += 1
    if contador == 1 or valor_produto < menor:
        menor = valor_produto
        nomemaisbarato = nome_produto

    # 02 - perguntar se quer continuar ou não
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    if 'n' in continuar:
        break
print(nomemaisbarato)
print(
    f'O total da compra é {acumulador}, {contador} produtos acima de mil reais e \n {nomemaisbarato} é o produto mais barato')
