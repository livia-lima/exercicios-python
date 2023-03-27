# digitar cinco valores numéricos e cadastrá-los em uma lista

lista: list[int] = []
for c in range(0, 5):
    numero = (int(input('Digite um valor: ')))

    if not lista or numero > lista[-1]:
        lista.append(numero)

    else:
        posição = 0
        # percorre todas as posições da lista, do início ao fim
        while posição < len(lista):
            # se o número for menor/igual o que está naquela determinada
            # posição, inserir o número nessa posição
            if numero <= lista[posição]:
                lista.insert(posição, numero)
                break
            posição += 1
print(lista)
