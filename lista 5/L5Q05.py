# -------funçoes----------

def conta_caracteres(palavra):
    contagem = {}
    for letra in palavra:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    return contagem


def permutacao(palavra1, palavra2)->bool:
    # Se os tamanhos forem diferentes, já não são permutação
    palavra1 = palavra1.lower().replace(" ","")
    palavra2 = palavra2.lower().replace(" ","")

    if len(palavra1) != len(palavra2):
        return False
    return conta_caracteres(palavra1) == conta_caracteres(palavra2)


def cal_pontuacao(grammys, popularidade, shows_no_brasil):
    return  (grammys*15)+(popularidade*10)+(shows_no_brasil*5)


def ogr_raking(competidoras):
    raking = {}

    i = 0
    for chave in competidoras:
        raking[i] = chave
        i += 1

    n = len(raking)

    for i in range(n-1):
        for j in range(n-i-1):
            if competidoras[raking[j]][4] < competidoras[raking[j+1]][4]:
                raking[j], raking[j+1] = raking[j+1], raking[j]

            elif competidoras[raking[j]][4] == competidoras[raking[j+1]][4]:
                # 1º Maior popularidade 
                if competidoras[raking[j]][2] < competidoras[raking[j+1]][2]:
                    raking[j], raking[j+1] = raking[j+1], raking[j]

                elif competidoras[raking[j]][2] == competidoras[raking[j+1]][2]:
                    # 2º Ordem lexicográfica do nome.
                    if raking[j].lower() > raking[j+1].lower():
                        raking[j], raking[j+1] = raking[j+1], raking[j]

    return raking


def combate(comp1, comp2, comps):

    print(f'DRAMA! A rivalidade entre {comp1} e {comp2} vai ser resolvida no palco, AGORA!')

    if comps[comp1][4] < comps[comp2][4]:
        print(f'Eliminada(s): {comp1}')
        del comps[comp1]
    elif comps[comp1][4] > comps[comp2][4]:
        print(f'Eliminada(s): {comp2}')
        del comps[comp2]
    else:
        print(f'Eliminada(s): {comp1} e {comp2}')
        del comps[comp1]
        del comps[comp2]

    return

def placar(numero_fase, raking, competidoras):
    print(f'=== PLACAR DA {numero_fase}ª FASE ===')
    for i in raking:
        nome_diva = raking[i]
        pontos = competidoras[nome_diva][4]
        print(f'{nome_diva} --- {int(pontos)}')

# --------main---------
op = True
conflitos = {
    'Katy Perry'        : ('Taylor Swift',),
    'Taylor Swift'      : ('Katy Perry', 'Ariana Grande', 'Olivia Rodrigo', 'Dua Lipa'),
    'Madonna'           : ('Lady Gaga',),
    'Lady Gaga'         : ('Madonna',),
    'Mariah Carey'      : ('Jennifer Lopez',),
    'Jennifer Lopez'    : ('Mariah Carey',),
    'Christina Aguilera': ('Britney Spears',),
    'Britney Spears'    : ('Christina Aguilera',),
    'Nicki Minaj'       : ('Doja Cat',),
    'Anitta'            : ('Ludmilla',),
    'Ludmilla'          : ('Anitta',),
    'Ariana Grande'     : ('Taylor Swift', 'Cynthia Erivo'),
    'Sabrina Carpenter' : ('Camila Cabello', 'Olivia Rodrigo', 'Doja Cat'),
    'Camila Cabello'    : ('Sabrina Carpenter',),
    'Olivia Rodrigo'    : ('Taylor Swift', 'Sabrina Carpenter'),
    'Dua Lipa'          : ('Taylor Swift',),
    'Doja Cat'          : ('Nicki Minaj', 'Sabrina Carpenter'),
}
divas_estadunidenses = (
    'Olivia Rodrigo',
    'Sabrina Carpenter',
    'Beyoncé', 
    'Taylor Swift',
    'Lady Gaga', 
    'Azealia Banks', 
    'Katy Perry', 
    'Madonna',
    'Ariana Grande',
    'Mariah Carey',
    'Whitney Houston',
    'Britney Spears',
    'Christina Aguilera',
    'Janet Jackson',
    'Cher',
    'Nicki Minaj',
    'Cardi B',
    'Doja Cat',
    'Billie Eilish'
)

competidoras = {}
raking = {}

print('A BATALHA DAS DIVAS começa... AGORA!')
print()


while op:

    #{nome_candidata} - {país} - {grammys} - {popularidade} - {shows_no_brasil}
    entrada = input()

    if entrada != 'FIM DAS INSCRIÇÕES':
    # fase 1
        entrada = entrada.split(' - ')

        nome_candidata  = entrada[0]
        pais            = entrada[1]
        grammys         = int(entrada[2])
        popularidade    = int(entrada[3])
        shows_no_brasil = int(entrada[4])

        #1- A pontuação é calculada pela fórmula de Impacto Cultural Ponderado:
        pontuacao = cal_pontuacao(grammys, popularidade, shows_no_brasil)

        #2- Bônus e Penalidades:
        if pais == 'Brasil':
            pontuacao += 50
        elif pais == 'EUA':
            pontuacao = pontuacao-50 if(pontuacao>=50)else 0

        #3- Diva Banida:
        if not permutacao('Azealia Banks',nome_candidata):
            validar_print = True
            competidoras[nome_candidata] = (pais, grammys, popularidade, shows_no_brasil, pontuacao)

            #4- Infiltração Americana:
            if pais != 'EUA':
                for diva in divas_estadunidenses:
                    if permutacao(nome_candidata, diva):
                        print(f'{diva} acaba de entrar na Batalha das Divas!')

                        validar_print = False
                        del competidoras[nome_candidata]
                        nome_candidata = diva
                        print(f'A CASA CAIU! A produção pegou {nome_candidata} no pulo do gato tentando se livrar da penalidade! Por essa tentativa de malandragem, o preço veio dobrado.')
                        pontuacao -= 100
                        if pais == 'Brasil':
                            pontuacao -= 50

                        #OBS
                        if nome_candidata not in competidoras:
                            competidoras[nome_candidata] = (pais, grammys, popularidade, shows_no_brasil, pontuacao)
                        else:
                            print(f'Só pode ter uma {nome_candidata} na arena. Inscrição duplicada negada!')

            if validar_print:
                print(f'{nome_candidata} acaba de entrar na Batalha das Divas!')

                if pais == 'Brasil':
                    print(f'ESSA TEM O TEMPERO BRASILEIRO! Por jogar em casa, {nome_candidata} já larga com 50 pontos de vantagem.')
                elif pais == 'EUA':
                    print(f'Por excesso de "estrelas e listras", {nome_candidata} recebe uma penalidade de 50 pontos.')

        else:
            print(f'Eita, climão! Parece que o histórico de polêmicas de Azealia Banks falou mais alto. A produção barrou a entrada e aqui no Brasil ela não canta!')

    else:
        op = False

        # organizando raking
        raking = ogr_raking(competidoras)
        print()

if len(raking) > 1:
    placar(1, raking, competidoras)
    print()

# fase 2
if len(raking) > 1:
    vali = False
    for i in raking:
        competidor1 = raking[i]
        if competidor1 in conflitos:
            if type(conflitos[competidor1]) == str:
                competidor2 = conflitos[competidor1]
                if competidor2 in competidoras:
                    vali = True
            else:
                for i in conflitos[competidor1]:
                    if i in competidoras:
                        vali = True

    if vali:
        print('SALTO ALTO NO TABLADO! HORA DO DUELO!')
    else:
        print('O palco estava montado. Os holofotes, ligados. Mas o conflito não apareceu. Fase 2 cancelada: as divas escolheram reinar em paz.')


    for i in raking:
        competidor1 = raking[i]

        if competidor1 in conflitos and competidor1 in competidoras:

            if type(conflitos[competidor1]) == str:
                competidor2 = conflitos[competidor1]
                if competidor2 in competidoras:
                    combate(competidor1,competidor2, competidoras)

            else:
                for competidor2 in conflitos.get(competidor1, []):
                    if competidor2 != [] and competidor1 in competidoras:
                        if competidor2 in competidoras:
                            combate(competidor1,competidor2, competidoras)
    print()

    raking = ogr_raking(competidoras)

    if len(raking) != 0 and vali:
        
        placar(2, raking, competidoras)
        print()

# fase 3
vali = False
if 'Lady Gaga' in competidoras:
    if len(raking) > 3 and raking[0] != 'Lady Gaga' and raking[1] != 'Lady Gaga' and raking[2] != 'Lady Gaga':

        ix_oponente = -1
        n = len(raking)
        for i in range(n-1, -1, -1):
            if raking[i] != 'Lady Gaga' and ix_oponente == -1:
                ix_oponente = i

        popularidade_oponete = competidoras[raking[ix_oponente]][2]
        popularidade_lady = competidoras['Lady Gaga'][2]

        porcentagem = popularidade_oponete * 100 / popularidade_lady

        if not vali:
            print('O PALCO VAI TREMER! HORA DAS JOGADAS ESPECIAIS!')
            vali = True
        #Sucesso:
        if porcentagem <= 125:
            
            print(f'ARRASOU! O blefe de Lady Gaga funcionou! Ela enganou os jurados com seu "Poker Face" e roubou a cena de {raking[ix_oponente]}!')

            x = competidoras[raking[ix_oponente]][4]
            y = competidoras['Lady Gaga'][4]

            competidoras['Lady Gaga'] = (competidoras['Lady Gaga'][0], competidoras['Lady Gaga'][1], competidoras['Lady Gaga'][2], competidoras['Lady Gaga'][3], x+y)
            del competidoras[raking[ix_oponente]]
            
        #Falha:
        else:
            print('QUE REVIRAVOLTA! O público não caiu no "Poker Face" de Lady Gaga! A farsa foi descoberta e ela está eliminada!')
            del competidoras['Lady Gaga']
    
    raking = ogr_raking(competidoras)


if 'Beyoncé' in competidoras:
    l = len(raking)
    if l > 2:
        # somar pontuação das duas competidoras mais fracas
        pessoa1 = {}
        pessoa2 = {}
        ponto_beyonce = competidoras['Beyoncé'][4]
        op1 = True
        op2 = True

        # pegando as duas pessoas (que não seja beyonce) com menor pontuação
        for i in range(l-1, -1, -1):

            if raking[i] != 'Beyoncé' and op1:
                op1 = False
                pessoa1[1] = (raking[i], competidoras[raking[i]][4])

            elif raking[i] != 'Beyoncé' and op2:
                op2 = False
                pessoa2[1] = (raking[i], competidoras[raking[i]][4])

        if pessoa2 != {} and pessoa1 != {}:
            if not vali:
                print('O PALCO VAI TREMER! HORA DAS JOGADAS ESPECIAIS!')
                vali = True
            #Sucesso:
            if ( pessoa1[1][1] + pessoa2[1][1] ) <= ponto_beyonce:
            
                print('PAREM TUDO! Queen Bey ativou a "Formation"! Ela reorganizou o jogo, elevou as novatas e saiu ainda mais forte!')
                acrecimo1 = pessoa1[1][1] * 10 / 100
                acrecimo2 = pessoa2[1][1] * 10 / 100

                competidoras[pessoa1[1][0]] = (competidoras[pessoa1[1][0]][0], competidoras[pessoa1[1][0]][1], competidoras[pessoa1[1][0]][2], competidoras[pessoa1[1][0]][3], competidoras[pessoa1[1][0]][4]+acrecimo1)
                competidoras[pessoa2[1][0]] = (competidoras[pessoa2[1][0]][0], competidoras[pessoa2[1][0]][1], competidoras[pessoa2[1][0]][2], competidoras[pessoa2[1][0]][3], competidoras[pessoa2[1][0]][4]+acrecimo2)

                competidoras['Beyoncé'] = (competidoras['Beyoncé'][0], competidoras['Beyoncé'][1], competidoras['Beyoncé'][2], competidoras['Beyoncé'][3], competidoras['Beyoncé'][4]+acrecimo1+acrecimo2 )

            #Falha:
            else:
                print('CHOQUE! A estratégia de Beyoncé foi ousada demais! A "Formation" não convenceu e ela foi desclassificada por manipulação!')
                del competidoras['Beyoncé']

    raking = ogr_raking(competidoras)


if 'Anitta' in competidoras:
    if raking[0] != 'Anitta':
        popularidade_rank1 = competidoras[raking[0]][2]
        popularidade_anita = competidoras['Anitta'][2]

        if not vali:
            print('O PALCO VAI TREMER! HORA DAS JOGADAS ESPECIAIS!')
            vali = True
        #Sucesso:
        if popularidade_anita >= (popularidade_rank1 * 90 / 100):
            
            print(f'A PATROA TÁ ON! Anitta usou "Envolver" e fez {raking[0]} dançar conforme sua música, virando o placar a seu favor!')
            # roubando 25% dos pontos da lider
            p_roubados = (competidoras[raking[0]][4]-competidoras['Anitta'][4]) * 25 / 100

            competidoras['Anitta'] = (competidoras['Anitta'][0], competidoras['Anitta'][1], competidoras['Anitta'][2], competidoras['Anitta'][3], competidoras['Anitta'][4]+p_roubados)
            competidoras[raking[0]] = (competidoras[raking[0]][0], competidoras[raking[0]][1], competidoras[raking[0]][2], competidoras[raking[0]][3], competidoras[raking[0]][4]-p_roubados)
        #Falha:
        else:
            print('DEU RUIM! A tentativa de "Envolver" de Anitta não funcionou! A jogada foi arriscada e o público não comprou a ideia.')
            competidoras['Anitta'] = (competidoras['Anitta'][0], competidoras['Anitta'][1], competidoras['Anitta'][2], competidoras['Anitta'][3], competidoras['Anitta'][4]-75)

    raking = ogr_raking(competidoras)

if not vali:
    if len(raking) > 1:
        print('Silêncio no palco... Nenhuma habilidade especial foi ativada.')
        print()
else:
    if len(raking) > 1:
        print()
        placar(3, raking, competidoras)
        print()


# Resultado Final:--------------------------------------------------
if raking == {}:
    print('INACREDITÁVEL! A Batalha das Divas terminou em caos, sem nenhuma vencedora! O palco está vazio... MAS O CALOR DA BRIGA FEZ O IMPOSSÍVEL! O Rei descongelou, subiu ao palco, olhou para a confusão e disse:')
    print('Obrigado pela ajuda, meninas, mas o show já tem atração... e Esse Cara Sou Eu.')
    print('O RÉVEILLON ESTÁ SALVO!')
else:
    print('=== HABEMUS DIVAM! ===')
    print('A GUERRA ACABOU! A nova dona do palco, a chefe do Réveillon, a única... é ELA!')

    if 'Taylor Swift' in competidoras and raking[0] != 'Taylor Swift':
        l = len(raking)
        if l > 3:
            if raking[1] == 'Taylor Swift' or raking[2] == 'Taylor Swift':
                print(f'PARABÉNS, {raking[0][:3].upper()}... TAYLOR SWIFT!!!')
                print('MAS O QUE É ISSO?! Uma reviravolta de última hora! O conselheiro Filipe Moreira acaba de invadir a sala de controle! Alegando fazer parte de uma "comissão cinterna" de Swifties, ele anulou o resultado final e declarou que a verdadeira Era do Réveillon pertence à Taylor Swift! O show está garantido... e a rainha dele também!')
            else:
                print(f'PARABÉNS, {raking[0].upper()}!!! O Rei pode descansar em paz (no gelo), pois o show está garantido!')
        else:
            print(f'PARABÉNS, {raking[0][:3].upper()}... TAYLOR SWIFT!!!')
            print('MAS O QUE É ISSO?! Uma reviravolta de última hora! O conselheiro Filipe Moreira acaba de invadir a sala de controle! Alegando fazer parte de uma "comissão cinterna" de Swifties, ele anulou o resultado final e declarou que a verdadeira Era do Réveillon pertence à Taylor Swift! O show está garantido... e a rainha dele também!')
        
    else:
        print(f'PARABÉNS, {raking[0].upper()}!!! O Rei pode descansar em paz (no gelo), pois o show está garantido!')
