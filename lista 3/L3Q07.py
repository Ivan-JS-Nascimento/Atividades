numero_eventos = int(input())

sigla = []
evento = []
inicio = []
fim = []

sus = 0
en_suspeitos = 0
alibis = 0
vjm = False

for i in range(numero_eventos):
    if not vjm:
        seg = input()
        seg = seg.split(' - ')
        if seg[0] == 'VJM':
            vjm =True
            sus = 100
        else:
            sigla.append(seg[0])
            evento.append(seg[1])
            inicio.append(seg[2])
            fim.append(seg[3])

# ORGANIZANDO EM ORDEM CRONOLOGICA - regra 0
n = len(sigla)
for i in range(n-1):
    for j in range(n-i-1):
        if inicio[j] > inicio[j+1]:
            sigla[j] , sigla[j+1]  = sigla[j+1] , sigla[j]
            evento[j], evento[j+1] = evento[j+1], evento[j]
            fim[j]   , fim[j+1]    = fim[j+1]   , fim[j]
            inicio[j], inicio[j+1] = inicio[j+1], inicio[j]

        elif inicio[j] == inicio[j+1]:
            if fim[j] > fim[j+1]:
                sigla[j] , sigla[j+1]  = sigla[j+1] , sigla[j]
                evento[j], evento[j+1] = evento[j+1], evento[j]
                fim[j]   , fim[j+1]    = fim[j+1]   , fim[j]
                inicio[j], inicio[j+1] = inicio[j+1], inicio[j]

# investigando
for i in range(n):

    if sigla[i]=='V':
        for j in range(n):
            if j > i:
                if inicio[j] < fim[i] and sigla[j]=='JM' and evento[i]==evento[j]:
                    sus += 35
                    en_suspeitos += 1
                if inicio[j] < fim[i] and sigla[j]=='ZF' and evento[i]==evento[j]:
                    sus -= 20 if( sus>=20 )else 0
                    alibis += 1

    elif sigla[i]=='JM':
        for j in range(n):
            if j > i:
                if inicio[j] < fim[i] and sigla[j]=='V' and evento[i]==evento[j]:
                    sus += 35
                    en_suspeitos += 1

    elif sigla[i]=='ZF':
        for j in range(n):
            if j > i:
                if inicio[j] < fim[i] and sigla[j]=='V' and evento[i]==evento[j]:
                    sus -= 20 if( sus>=20 )else 0
                    alibis += 1


print('Iniciando investigação... Zé Felipe está focado.')

if not vjm:
    # Linha do Tempo Ordenada
    print('')
    print('--- Linha do Tempo dos Eventos ---')
    for i in range(n):
        pers = 'Virgínia' if sigla[i] == 'V' else 'Jogador Misterioso' if sigla[i] == 'JM' else 'Zé Felipe' if sigla[i] == 'ZF' else 'Virginia e Jogador Misterioso'
        print(f'{inicio[i]}-{fim[i]}: {pers} - {evento[i]}')

    # Resumo da Análise
    print('')
    print('--- Resumo da Análise ---')
    print(f'Encontros Suspeitos: {en_suspeitos}')
    print(f'Álibis Confirmados: {alibis}')

# Conclusão da Análise
print('')
if sus>=100:
    print('TRAIÇÃO CONFIRMADA! Zé Felipe vai fazer uma música sobre isso.')
elif sus>=70 and sus<100:
    print(f'Nível de Suspeita: {sus} - MUITO SUSPEITO! Zé Felipe vai ter uma conversa séria com a Virgínia.')
elif sus>=30 and sus<70:
    print(f'Nível de Suspeita: {sus} - Hmmm, algo de estranho não está certo. Zé Felipe vai ficar de olho.')
else:
    print(f'Nível de Suspeita: {sus} - Não há motivo para preocupação. Zé Felipe pode respirar aliviado e voltar a brincar com a Maria Flor.')