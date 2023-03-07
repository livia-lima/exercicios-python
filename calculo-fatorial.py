# resolução 01 - usando a lib math
from math import factorial

numero = int(input('Digite um número: '))
fatorial = factorial(numero)

print(f'O fatorial de {numero} é {fatorial}')

# resolução 02 - com o while
contador = numero
fatorial2 = 1  # como é uma multiplicação, começa com 1
while contador > 0:
    print(contador, end='')
    print('x' if contador > 1 else '=', end='')
    fatorial2 *= contador
    contador -= 1
print(fatorial2)

contador2 = numero
fatorial3 = 1
# resolução 03 - com o for
for c in range(numero, 0, -1):
    fatorial3 *= c
    contador2 -= 1
print(fatorial3)
