times = 'palmeiras', 'internacional', 'fluminense', 'corinthians', 'flamengo', 'athletico-PR', 'atlético-MG', 'Fortaleza', 'São Paulo', 'américa-mg', 'botafogo', 'santos', 'goiás', 'bragantino', 'coritiba', 'cuiabá', 'ceará', 'athletico-GO', 'avaí', 'juventude'

# mostrar os 5 primeiros times
print(times[0:5])

# mostrar os 4 últimos colocados
print(times[-4:])

# mostrar os times em ordem alfabética
print(sorted(times))

'''
a função sorted() retorna strings em ordem alfabética e números em ordem
crescente. não dá pra usar essa função com variáveis compostas que contenham
strings e números
'''

# mostrar em que posição está o athletico-PR
print(f'o athletico-PR está na {times.index("athletico-PR")} posição')
# vai dar erro por causa das ''. usar " "

'''

o método .index() retorna a posição da primeira ocorrência de um valor
específico,colocado entre os parênteses. no exercício, esse valor é
uma string (athletico-PR)

'''
