# ler vários números e colocá-los em uma lista
lista_principal: list[int] = []
while True:
    lista_principal.append(int(input('Digite um valor: ')))

    continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if continuar in 'n':
        break
print(f'Os valores digitados foram {lista_principal}')

# lista com apenas os valores pares digitados
lista_pares: list[int] = []
lista_ímpares: list[int] = []
for i, valores in enumerate(lista_principal):
    if valores % 2 == 0:
        lista_pares.append(valores)  # lista com os valores ímpares
    else:
        lista_ímpares.append(valores)
print(f'Os valores pares digitados foram {lista_pares}')
print(f'Os valores ímpares digitados foram {lista_ímpares}')
