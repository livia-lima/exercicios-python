# o primeiro [] é p/ os números pares, e o segundo p/ os ímpares
números: list[int] = [[], []]

for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        números[0].append(valor)
    else:
        números[1].append(valor)
números[0].sort()
print(f'Os valores pares digitados foram {números[0]}')
números[1].sort()
print(f'Os valores ímpares digitados foram {números[1]}')
