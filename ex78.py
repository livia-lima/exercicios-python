# ler 5 valores numéricos e guardá-los em uma lista
valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    # analisar quais são o maior e o menor valor da lista
    if c == 0:  # se for o primeiro número analisado...
        maior = menor = valores[0]
    if valores[c] > maior:
        maior = valores[c]
    if valores[c] < menor:
        menor = valores[c]
print(
    f'Os valores digitados foram {valores}, com {maior} sendo o maior valor nas posições ', end='')

for i, valor in enumerate(valores):
    if valor == maior:
        print(f'{i}, ', end='')

print(f'\nE o menor valor foi {menor}, na posição ', end='')
for i, valor in enumerate(valores):
    if valor == menor:
        print(f'{i}, ', end='')
