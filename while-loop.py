''' executa um bloco de código enquanto uma condição for verdadeira.
é utilizada em situações onde o laço é indefinido. '''

i = 1  # precisa ter a variável inicializada
while i < 6:  # imprime i enquanto for menor que 6
    print(i)
    i += 1

# exercício 57 - curso em vídeo
sexo = str(input('Informe seu sexo: ')).strip().lower()[0]
while sexo not in 'mf':
    sexo = str(input(
        'Dados inválidos. Por favor, informe seu sexo novamente: ')).strip().lower()[0]
print('O registro foi completado com sucesso.')
