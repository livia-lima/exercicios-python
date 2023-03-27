# ler vários números e colocar em uma lista

lista: list[int] = []
contador = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    contador += 1  # conta quantos números foram digitado

    # verifica se o usuário quer continuar
    continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    if continuar in 'n':
        break
print(lista)

# sort(reverse=True) mostra os valores ordenados de modo decrescente
lista.sort(reverse=True)

# dava para usar o len(lista) p/ mostrar quantos valores foram digitados
print(
    f'Você digitou os valores {lista}.\n{contador} valores foram digitados')

# ver se o 5 aparece e em qual posição está
for i, valor in enumerate(lista):
    if valor == 5:
        print(f'O número 5 apareceu na posição {i} da lista')
    else:
        print('O valor 5 não está presente na lista.')
