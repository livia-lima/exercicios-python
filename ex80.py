# digitar cinco valores numéricos e cadastrá-los em uma lista

lista: list[int] = []
for números in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
