inicio = int(input('Digite o início: '))  # primeiro termo da P.A
fim = int(input('Digite o fim: '))  # último termo da P.A
razao = int(input('Digite a razão: '))

contador = 0
for progressao in range(inicio, fim+1, razao):
    print(progressao)
    contador = contador + 1
print('fim')

# SOMA DE UMA P.A = (inicio + fim)*contador / 2

soma = ((inicio + fim) * contador) / 2
print(soma)
