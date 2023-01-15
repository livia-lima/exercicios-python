for c in range(1, 6):
    peso = float(input(f'Peso da {c}a pessoa: '))
    # para ler o maior e menor peso, ter o primeiro dado lido como referência
    if c == 1:
        maior = peso
        menor = peso
    else:  # analisará os valores colocados na var peso, atualizando o
        # maior e o menor peso
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é de {maior}kg, e o menor de {menor}kg.')
