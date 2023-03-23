# tupla com várias palavras
palavras = 'abacaxi', 'banana', 'garrafa', 'luz', 'cyberpunk', 'cola', 'totoro', 'gato'

for c in palavras:
    print(f'\nNa palavra \033[0;33m{c.upper()}\033[m tem as vogais ', end='')
    for letra in c:  # percorre cada uma das letras da palavra
        if letra in 'aeiou':  # verifica se a letra é uma das vogais
            print(f'\033[0;34m{letra}\033[m', end='')  # se for, printa a letra
