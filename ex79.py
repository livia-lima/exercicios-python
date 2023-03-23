listagem: list[int] = []

while True:
    # receber um número para armazenar na lista
    numero = int(input('Digite um valor: '))

    if numero in listagem:  # verificar se o número já está na lista
        print('Esse número já está na lista.')
    else:  # se não estiver, adicionar o número na lista
        listagem.append(numero)

    # verificar se o usuário deseja continuar ou não
    continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    if continuar in 'n':
        break
print(listagem.sort())
