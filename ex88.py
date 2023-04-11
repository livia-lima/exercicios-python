import random

lista: list[int] = []  # núm sorteados
jogo: list[int] = []  # lista com os jogos sorteados
contador = 0  # conta qnts números foram adicionados na lista

qntd_jogos = int(input('Digite quantos jogos serão sorteados: '))
total = 0  # gera o núm de jogos digitado

while total < qntd_jogos:
    while True:
        # gera um número aleatório entre 1 e 60
        número = random.randint(1, 60)
        # confere se esse número gerado já está na lista
        if número not in lista:
            # se não estiver, é adicionado na lista
            lista.append(número)
            contador += 1
        if contador == 6:  # para quando 6 num são digitados
            break
    lista.sort()  # coloca a lista em ordem crescente
    # coloca a lista com os num sorteados na lista de jogos criados
    jogo.append(lista[:])
    lista.clear()
    total += 1
print(jogo)
