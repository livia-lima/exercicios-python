continuar = 's'

contador = acumulador = maior = menor = 0
while continuar in 's':
    numero = int(input('Digite um valor: '))
    contador += 1
    acumulador += numero
    if contador == 1:
        menor = maior = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()
print(
    f'a média dos números digitados é {acumulador / contador}, o maior número\n é {maior} e o menor é {menor}')
