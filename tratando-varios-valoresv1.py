# 01 - ler vários números (parar quando o usuário digitar 999)
numero = int(input('Digite um número: '))  # numero = 0 -> solução do guanabara

# qnts números foram digitados e a soma entre eles
contador = 0
acumulador = 0  # simplificar fazendo contador = acumulador = 0

while numero != 999:
    numero = int(input('Digite um número: '))
    if numero == 999:  # flag - condição de parada
        break
    # botar dps da flag para desconsiderá-lo
    acumulador += numero
    contador += 1
print(f'Você digitou {contador} números. A soma entre eles é {acumulador}')
