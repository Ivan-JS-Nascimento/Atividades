

# resumindo:
# imagine todas as combinacoes das 'notas' como uma ramificacoes infinita
# essa funcao usa a 'rota atual'( que nao deixa de ser a repeticao da funcao varias vesez)
# para seguir um caminho ate essas combinacoes ser igual 0 (logo é uma possibilidade, retornando 1 )
# ou ser menor que 0 ( nao e contabilizada, retornando 0 )
# Assim que ele chegar ao fim da linha ele retorna e utiliza o 'pular ... rota' 
# para repetir esse processo em outro caminho

def contar_combinacoes(valor, notas, atual, todas):
    if valor == 0: # quer dizer que nessa rota as combinacoes dao certo
        todas.append(atual.copy())  # salva a combinação atual
        return 1
    if valor < 0 or notas == []:
        return 0

    # rota atual
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
