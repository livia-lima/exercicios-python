cont1 = cont2 = cont3 = 0
while True:
    # 1 - ler idade e gênero
    idade = int(input('Digite sua idade: '))
    gênero = str(input('Digite seu gênero [M/F]: ')).strip().lower()

    # 2 - perguntar se quer continuar
    continuação = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if 'n' in continuação:
        break
    else:
        if idade > 18:  # quantas pessoas tem mais de 18 anos
            cont1 += 1
        if 'm' in gênero:  # quantos homens foram cadastrados
            cont2 += 1
        if 'f' in gênero and idade <= 20:  # quantas mulheres tem menos de 20 anos
            cont3 += 1
print(f'{cont1} pessoas tem mais de 18 anos, {cont2} pessoas são homens e {cont3} mulheres tem menos de 20 anos')
