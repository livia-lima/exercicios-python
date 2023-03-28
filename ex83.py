expressão = str(input('Digite a expressão: '))

pilha = []

'''
verifica se, para cada parênteses aberto, há um parênteses o fechando.
ao receber a expressão, o for percorre toda a expressão e verifica se há
parênteses abertos. se houver, os adiciona na lista "pilha".

ao encontrar um parênteses fechado, verifica se há um parênteses aberto
correspondente. se houver, um parênteses aberto é retirado da pilha. se
não houver, adiciona-se um parêntese fechado à pilha.

no final, é verificado se a pilha está vazia. se estiver, a expressão está
correta
'''

for símbolo in expressão:  # percorre a expressão inteira
    # se encontrar um parêntese aberto, adiciona na pilha
    if símbolo == '(':
        pilha.append('(')

    # se encontra um parêntese fechado, verifica se há um aberto na pilha
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
            # se houver, um parêntese aberto é retirado
        else:
            pilha.append(')')
            # se não houver, um parêntese fechado é adicionado

if len(pilha) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')

'''
esse exercício também poderia ser feito contando o número de parênteses abertos
e fechados e dps verificando se o número é igual. porém essa solução não
levaria em conta a ordem dos parênteses.

expressao = input('Digite a expressão: ')

abertos = 0
fechados = 0

for caracter in expressao:
    if caracter == '(':
        abertos += 1
    elif caracter == ')':
        fechados += 1

if abertos == fechados:
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')

'''
