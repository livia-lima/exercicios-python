# ler os termos da P.A
primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))

print(primeiro_termo, razão)

# cálculo dos 10 primeiros termos
# termo = primeiro_termo -> resolução do guanabara
contador = 0
while contador <= 10:
    contador += 1
    cálculo_termo = primeiro_termo + (contador - 1) * razão
    # termo += razão -> resolução do guanabara
    print(f'{cálculo_termo}', ' → ', end='')
print('FIM ♡⋆.ೃ࿔* ')
