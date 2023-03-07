# 01 - ler quantos termos o usuário quer ver
qntd_termos = int(input('Digite quantos termos você quer mostrar: '))

# 02 - definir os primeiros termos da sequência
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')  # end='' pra não pular linha

# 03 - calcular os próximos termos. o termo seguinte é a soma dos dois últimos
contador = 3  # como os 2 primeiros termos já foram mostrados, começa no 3o
while contador <= qntd_termos:
    t3 = t1 + t2
    print(f' → {t3} ', end='')
    # atualizar os valores para que a sequência continue
    t1 = t2
    t2 = t3
    contador += 1
    # 0 - 1 - 1 - 2 - 3 - 5 - 8
    #         t1  t2, pq vão originar o novo t3
print('→ FIM ･ﾟ *✧･')
