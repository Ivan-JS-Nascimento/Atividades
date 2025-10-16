print('RECEBA! É hoje que eu me torno o melhor dos melhores.')

num_sessoes = int(input())
habilidade = int(input())

# print para cada valor de habilidade
if habilidade <= 5 :
    print('A gente tem que começar de algum lugar, né? RECEBA!')
elif habilidade <= 15 :
    print('Não tem jeito, vou ser o melhor do mundo!')
else:
    print('O Pai tá estourado! RECEBA!')
# ---

# variaveis
sequencia = input()
sequencia_list = sequencia.split('-')
matriz = []
meta = ( 100 - habilidade ) / num_sessoes
gol = 0
# ---

print(f'Meta por Partida: {meta}')

for i in range(0,len(sequencia_list),2):

    tipo_treino = sequencia_list[i]
    nome_goleiro = sequencia_list[i+1]

    # Relatório por partida
    print(f'TIPO DE PARTIDA: {tipo_treino}')
    print(f'Nome do Goleiro: {nome_goleiro}')
    # ---

    # se o goleiro nao for especial
    if nome_goleiro not in ['Rokenedy','IShowSpeed','Sérgio Soares','Neymar Jr','Gabriel Vasconcelos']:
        habilidade_goleiro = int(input())
    
    matriz = eval(input())
    x = int(input())
    y = int(input())

    # acertou o gol ou nao?
    if matriz[x][y] == 1 :
        # sim. OOou sera que nao???
        gol = 1
    else:
        # erou, mas que burro, da zero pra ele
        gol = 0
        print('A jornada ainda não acabou!')
    # ---

    pontos_partidas = 0

    if gol == 1 :
        # condicoes de cada goleiro
        if nome_goleiro == 'Rokenedy':
            
        elif nome_goleiro == 'IShowSpeed':
        elif nome_goleiro == 'Sérgio Soares':
        elif nome_goleiro == 'Neymar Jr':
        elif nome_goleiro == 'Gabriel Vasconcelos':
        # Goleiro não especial
        else:
