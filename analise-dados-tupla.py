# ler 4 valores e guardá-los em uma tupla
números = (int(input('Digite um valor: ')), int(input('Digite mais um valor: ')), int(
    input('Digite um valor: ')), int(input('Digite o último valor: ')))
print(números)

# quantas vezes apareceu o número 9
contador = 0
if 9 in números:
    contador += 1
print(f'O número 9 apareceu {contador} vezes')
# poderia usar números.count(9) também

# posição do número 3
if 3 in números:
    print(f'O número 3 está na posição {números.index(3)}')

# mostrar os números pares
for n in números:
    if n % 2 == 0:
        print(f'{n} é par')
