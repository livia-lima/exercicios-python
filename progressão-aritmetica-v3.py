# ler os termos da P.A
primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))


# cálculo dos 10 primeiros termos

contador = 1
total = 0
termos_extras = 10
while termos_extras != 0:
    total += termos_extras
    while contador <= total:
        cálculo_termo = int(primeiro_termo + (contador - 1) * razão)
        print(f'{cálculo_termo}', ' → ', end='')
        contador += 1
        termos_extras = int(input('Qnts termos a mais? '))
print(f'FIM ♡⋆.ೃ࿔* Você montou uma P.A de {total} termos.')
