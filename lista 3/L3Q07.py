numero_eventos = int(input())
sigla = []
evento = []
inicio = []
fim = []
suspeita = 0


for i in range(numero_eventos):
    seg = input()
    seg = seg.split(' - ')

    sigla = seg[0]
    evento = seg[1]
    inicio = seg[2]
    fim = seg[3]

# ORGANIZANDO EM ORDEM CRONOLOGICA - regra 0
n = len(sigla)
for i in range(n-1):
    for j in range(n-i-1):
        if inicio[j] > inicio[j+1]:
            sigla[j] , sigla[j+1]  = sigla[j+1] , sigla[j]
            evento[j], evento[j+1] = evento[j+1], evento[j]
            fim[j]   , fim[j+1]    = fim[j+1]   , fim[j]
            inicio[j], inicio[j+1] = inicio[j+1], inicio[j]

print('Iniciando investigação... Zé Felipe está focado.')

for i in range(n-1):
    # regra 1
    if sigla[i] != 'VJM':
        # Linha do Tempo Ordenada
        print('')
        print('-- Linha do Tempo dos Eventos ---')
        print('{HORA_INICIO}-{HORA_FIM}: {PERSONAGEM} - {EVENTO}')

        # Resumo da Análise
    else:
# Conclusão da Análise