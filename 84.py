#  leia nome e peso de várias pessoas, guardando tudo em uma lista

pessoas = []
dados = []
contador = 0
while True:
    # coleta de dados
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    contador += 1  # conta quantas pessoas foram cadastradas

    # verificar o maior e o menor peso cadastrados
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]

    # colocar a cópia de dados na lista pessoa
    pessoas.append(dados[:])
    # limpa a lista para que os msms dados não sejam adicionados duas vzs
    dados.clear()

    continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    if continuar in 'n':
        break
print(f'{contador} pessoas foram cadastradas.')
print(
    f'O maior peso cadastrado foi {maiorpeso}kg, e o menor foi {menorpeso}kg')
