import random

contador = 0  # pra contabilizar quantas vezes o usuário ganhou
while True:
    # 1 - pc escolher um número de 0-10
    escolha_computador = random.randint(0, 10)

    # 2 - usuário escolher um número de 0-10
    escolha_usuário = int(input('Digite um número: '))

    # 3 - par ou impar
    par_ou_ímpar = str(input('Par ou ímpar? [P/I] ')).strip().lower()

    if par_ou_ímpar == 'p' and (escolha_computador + escolha_usuário) % 2 == 0:
        print(
            f'Você escolheu {escolha_usuário} e o computador escolheu {escolha_computador}.')
        print(
            f'A soma de {escolha_computador + escolha_usuário} é par. VOCÊ VENCEU')
        contador += 1
    if par_ou_ímpar == 'i' and (escolha_usuário + escolha_computador) % 2 != 0:
        print(
            f'Você escolheu {escolha_usuário} e o computador escolheu {escolha_computador}.')
        print(
            f'A soma de {escolha_computador + escolha_usuário} é ímpar. VOCÊ VENCEU.')
        contador += 1
    else:
        print(
            f'Você escolheu {escolha_usuário} e o computador escolheu {escolha_computador}.')
        print(
            f'A soma de {escolha_computador + escolha_usuário} não é {par_ou_ímpar}. ')
        break
print(f'Você ganhou {contador} vezes.')
