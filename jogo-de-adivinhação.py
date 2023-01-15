import random

# computador escolhe um número de 0 a 10
numerocomputador = random.randint(0, 10)

# random.randint() retorna um elemento da range definida


# jogador tenta adivinhar o número escolhido
numerojogador = int(input('Qual número o computador escolheu? '))

palpites = 0
while numerojogador != numerocomputador:
    palpites += 1  # contabiliza o número de palpites

    # verifica se o palpite dado é maior ou menor que o número escolhido pelo pc
    if numerojogador < numerocomputador:
        print('O número é maior que isso...')
    if numerojogador > numerocomputador:
        print('O número é menor que isso...')

    numerojogador = int(input('Tente novamente: '))

print(
    f'Parabéns, você acertou o número em {palpites} tentativas. O computador escolheu {numerocomputador}')
