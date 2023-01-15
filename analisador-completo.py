acumulador = 0
contador = 0
nomemaisvelho = ''

for c in range(1, 5):
    print(f'---- {c}a PESSOA ----')
    nome = str(input('Informe o seu nome: ')).strip()
    idade = int(input('Informe a sua idade: '))
    sexo = str(input('Informe seu sexo: ')).strip().lower()
    print('----------------')

    # somará as idades informadas p dps calcular a média
    acumulador = acumulador + idade

    # analisará qual dos homens é o mais velho
    if c == 1:
        menor = idade
        maior = idade
    else:
        if idade > maior and sexo == 'm':
            maior = idade
            nomemaisvelho = nome
        if idade < menor and sexo == 'm':
            menor = idade

    # contabilizará o número de mulheres com menos de 20 anos
    if sexo == 'f' and idade < 20:
        contador += 1

media_idades = acumulador / 4
print(f'a média das idades desse grupo é de {media_idades} anos.')
print(
    f'o homem mais velho tem {maior} anos e se chama {nomemaisvelho}, e o mais novo tem {menor} anos.')
print(f'nesse grupo, há {contador} mulheres com menos de 20 anos.')
