# a estrutura de repetição for percorre os itens de uma lista e executa
# uma série de códigos para cada item

import time

pets = ['totoro', 'wandinha', 'branquinho']  # nome dos vscode pets

for n in pets:  # atribui o valor do item para a variável "n"
    print(n)

# percorre todos os itens da lista "pets", imprimindo cada um


for c in range(10, 0, -1):  # exercício 46
    print(c)
    time.sleep(1.0)

for c in range(0, 50, 2):  # exercício 47
    print(c)

# exercício 48
contador = 0
acumulador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        acumulador = acumulador + c
print(
    f'o número de números múltiplos de 3 nesse intervalo é {contador}, e o total é {acumulador}')

# exercício 49
numero = int(input('Escolha um número para fazer sua tabuada: '))

for c in range(1, 11):
    tabuada = numero * c
    print(tabuada)

contador1 = 0
acumulador1 = 0
# exercício 50
for c in range(1, 7):
    escolha = int(input('Digite um número: '))
    if escolha % 2 == 0:
        contador1 = contador1 + 1
        acumulador1 = acumulador1 + c
print(f'você digitou {contador1} números pares. a soma deles é {acumulador1}')


# exercício 52
num = int(input('Digite um número: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        total += 1
print(f'o número {num} foi dividido {total} vezes.')
if total > 2:
    print('portanto, esse número não é primo.')
else:
    print('portanto, esse número é primo.')
