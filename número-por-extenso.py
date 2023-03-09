# 01 - tupla totalmente preenchida com números 0-20
números = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:  # loop infinito para verificar se a resposta está dentro do esperado
    número_escolhido = int(input('Digite um número de 0 a 20: '))
    if 0 <= número_escolhido <= 20:
        print(números[número_escolhido])
    else:
        print('Tente novamente')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if continuar in 'n':
        break
