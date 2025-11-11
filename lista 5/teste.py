def contar_combinacoes(valor, notas, atual, todas):
    if valor == 0:
        todas.append(atual.copy())  # salva a combinação atual
        return 1
    if valor < 0 or notas == []:
        return 0

    # primeira rota
    atual.append(notas[0])
    num1 = contar_combinacoes(valor - notas[0], notas, atual, todas)
    atual.pop()

    # pula para a proxima rota
    num2 = contar_combinacoes(valor, notas[1:], atual, todas)

    return num1 + num2

notas = [100, 50, 20, 10, 5]
notas_usadas = [0, 0, 0, 0, 0]

todas = [] # todas as combinaçoes

valor = int(input()) # total a ser pago
combi = contar_combinacoes(valor, notas, [], todas)

print(f'Calculando possibilidades para o valor: {valor}')

if combi == 1:
    print('\nEssa foi fácil! Só existe 1 possibilidade de pagar essa conta.')
elif combi == 0:
    print('\nInfelizmente, não há como pagar essa conta com as notas disponíveis.')


print(f'\nTotal de possibilidades: {combi}')
print('\nUso das notas:')

for i in todas:
    for j in i:
        if j == 5:
            notas_usadas[4] += 1
        elif j == 10:
            notas_usadas[3] += 1
        elif j == 20:
            notas_usadas[2] += 1
        elif j == 50:
            notas_usadas[1] += 1
        elif j == 100:
            notas_usadas[0] += 1

for i in range(5):

    print(f'R${notas[i]}: usada em {notas_usadas[i]} combinações')
