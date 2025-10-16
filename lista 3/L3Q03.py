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

# variaveis globais
sequencia = input()
sequencia_list = sequencia.split('-')
matriz = []
meta = ( 100 - habilidade ) / num_sessoes
gol = False
acabo = False
habilidade_goleiro = 0
# ---

print(f'Meta por Partida: {meta}')

for i in range(0,len(sequencia_list),2):
    # break 2.0
    if not acabo:
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
            gol = True
        else:
            # erou, mas que burro, da zero pra ele
            gol = False
        # ---

        pontos_partidas = 0

        if gol :
            # condicoes de cada goleiro
            if nome_goleiro == 'Rokenedy':
                print('Aí não dá, impossível de fazer gol no maior do mundo.')
                gol = False

            elif nome_goleiro == 'IShowSpeed':
                print('REBECA? Is that you?')
                print('Ispidi mai friand, recieve!')
                pontos_partidas = 1.5 * meta

            elif nome_goleiro == 'Sérgio Soares':
                print('DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…')

                if tipo_treino == 'Batida de Pênalti':
                    pontos_partidas = meta
                else:
                    gol = False

            elif nome_goleiro == 'Neymar Jr':
                print('Ele nem sabe agarrar! A arma dele é a sua fragilidade…')
                pontos_partidas = meta / 2

            elif nome_goleiro == 'Gabriel Vasconcelos':
                print('HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…')
                pontos_partidas = meta * 2

            # Goleiro não especial
            else:
                if habilidade > habilidade_goleiro :
                    pontos_partidas = (habilidade-habilidade_goleiro)


            if gol :
                print('RECEBA! GOLAÇO! É O MELHOR DO MUNDO!')
            else:
                print('A jornada ainda não acabou!')
            # --- ---

        habilidade += pontos_partidas
        
        if habilidade > 100:
            print('NÃO TEM JEITO! EU SEMPRE SOUBE QUE IA SER O MELHOR DO MUNDO! RECEBA!')
            acabo = True

        elif habilidade <= 100:
            # Meta da partida
            if pontos_partidas >= meta:
                print(f'VAMO! PARTIDA {(i//2)+1} DE {num_sessoes}!')
            else:
                print('Dá pra recuperar depois! Vamo seguindo!')
    # ---

if habilidade < 100:
    print('Ano que vem tem InterCIn de novo! É só eu treinar mais…')
elif habilidade == 100:
    print('O trono do futebol hoje tem dois reis. Eu e Pelé! Não podia estar com alguém melhor!')