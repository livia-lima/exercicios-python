# exercício 54

contador1 = 0
contador2 = 0

# primeiro passo: ler o ano de nascimento de 7 pessoas
for c in range(1, 8):
    ano_nascimento = int(input('Digite seu ano de nascença: '))
    idade = 2023 - ano_nascimento
    if idade >= 18:
        contador1 += 1
        print('você já é maior de idade')
    else:
        contador2 += 1
        print('você ainda não atingiu a maioridade')
print(f'{contador1} pessoas já atingiram a maioridade. {contador2} pessoas ainda são de menor.')
