
dic = {
# ============ Dua Lipa =================
    'Future Nostalgia' : (
        'Future Nostalgia',
        "Don't Start Now",
        'Cool',
        'Physical',
        'Levitating',
        'Pretty Please',
        'Hallucinate',
        'Love Again',
        'Break My Heart',
        'Good in Bed',
        'Boys Will Be Boys',
        'Fever'),

    'Radical Optimism' : (
        'End of an Era',
        'Houdini',
        'Training Season',
        'These Walls',
        'Whatcha Doing',
        'French Exit',
        'Illusion',
        'Falling Forever',
        'Anything for Love',
        'Maria',
        'Happy for You'),
    # ==============================
    # ========== Olivia Rodrigo ==========
    'SOUR' : (
        'Brutal',
        'Traitor',
        'Drivers License',
        '1 Step Forward, 3 Steps Back',
        'Deja Vu',
        'Good 4 U',
        'Enough For You',
        'Happier',
        'Jealousy, Jealousy',
        'Favorite Crime',
        'Hope Ur Ok'),

    'GUTS' : (
        'All-American Bitch',
        'Bad Idea Right?', 
        'Vampire', 
        'Lacy', 
        'Ballad Of A Homeschooled Girl',
        'Making The Bed', 
        'Logical', 
        'Get Him Back!', 
        'Love Is Embarrassing', 
        'The Grudge', 
        "Pretty Isn't Pretty", 
        'Teenage Dream'),
    # ==================================
    # =========== Katy Perry =============
    'Teenage Dream' : (
        'Teenage Dream', 
        'Last Friday Night (T.G.I.F.)', 
        'California Gurls', 
        'Firework', 
        'Peacock', 
        'Circle the Drain', 
        'The One That Got Away', 
        'E.T.', 
        'Who Am I Living For?', 
        'Pearl', 
        'Hummingbird Heartbeat', 
        'Not Like the Movies'),

    'Prism' : (
        'Roar', 
        'Legendary Lovers', 
        'Birthday', 
        'Walking on Air', 
        'Unconditionally', 
        'Dark Horse', 
        'This Is How We Do', 
        'International Smile', 
        'Ghost', 
        'Love Me', 
        'This Moment', 
        'Double Rainbow', 
        'By theGrace of God')
# ==============================
}

diva_era = {
    'Dua Lipa'       : ('Future Nostalgia','Radical Optimism'),
    'Olivia Rodrigo' : ('SOUR','GUTS'),
    'Katy Perry'     : ('Teenage Dream','Prism')
}

spotify = {
    #                 musica : (era, stream)
    'Dua Lipa'       : {},
    'Olivia Rodrigo' : {},
    'Katy Perry'     : {}
}

podio = {
    1 : (),
    2 : (),
    3 : ()
}

entradas_fase2 = {}

quant_mus_era ={
    'Future Nostalgia': 0,
    'Radical Optimism' : 0,
    'SOUR' : 0,
    'GUTS' : 0,
    'Teenage Dream' : 0,
    'Prism' : 0
}

musicas_raking = {}

votacao = {
    'Dua Lipa'       : 0,
    'Olivia Rodrigo' : 0,
    'Katy Perry'     : 0
}

fas = {}

diva_que_nao_foi_campea_nem_teve_melhor_musica = ''

op = True
quant_m_dua    = 23
quant_m_olivia = 23
quant_m_katy   = 25
parte1 = True
parte2 = False
parte3 = False

# -------------------------------FUNÇÔES-----------------------------------

def soorted(dicionario, valor_1, valor_2, valor_3):

    n = len(dicionario)

    for i in range(n-1):
        for j in range(n-i-1):
            antes = dicionario[j]
            depois= dicionario[j+1]
            
            if antes[valor_1] < depois[valor_1]:
                dicionario[j], dicionario[j+1] =  dicionario[j+1],  dicionario[j]

            elif antes[valor_1] == depois[valor_1]:

                if antes[valor_2] < depois[valor_2]:
                    dicionario[j], dicionario[j+1] =  dicionario[j+1],  dicionario[j]

                elif antes[valor_2] == depois[valor_2]:

                    if antes[valor_3] > depois[valor_3]:
                        dicionario[j], dicionario[j+1] =  dicionario[j+1],  dicionario[j]

    return

def organizar_podio(podio, spotify):

    media_stream = 0
    somatorio_streams_diva = 0
    total_musicas_diva = 0
    dic_ordenado = {}

    cont = 0
    for diva in spotify:
        media_stream = 0
        somatorio_streams_diva = 0
        total_musicas_diva = 0
        for music in spotify[diva]:

            total_musicas_diva += 1
            somatorio_streams_diva += spotify[diva][music][1]

            media_stream = somatorio_streams_diva/total_musicas_diva

        dic_ordenado[cont] = {
            'nome_diva' : diva,
            'num_music' : total_musicas_diva,
            'media_str' : media_stream
        }

        cont += 1

    soorted(dic_ordenado, 'media_str', 'num_music', 'nome_diva')

    podio[1] = (dic_ordenado[0]['nome_diva'] , dic_ordenado[0]['media_str'])
    podio[2] = (dic_ordenado[1]['nome_diva'] , dic_ordenado[1]['media_str'])
    podio[3] = (dic_ordenado[2]['nome_diva'] , dic_ordenado[2]['media_str'])

    return

def descripto(mensagem, chave):
    indice_letra = {
        0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r',
        18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'
    }
    letra_indice = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
        's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
    }

    mens_descripto = ''

    for caracter in mensagem:
        if caracter.isalpha():
            indice = letra_indice[caracter.lower()]

            novo_ix = (indice-chave)
            if novo_ix < 0:
                novo_ix = 26 + novo_ix

            if caracter.isupper():
                mens_descripto += indice_letra[novo_ix].upper()
            else:
                mens_descripto += indice_letra[novo_ix]
        else:
            mens_descripto += caracter

    return mens_descripto

#  --------------------------------MAIN------------------------------------

print("Vai começar a disputa das DIVAS")

while op:

    if parte1: # -----------------------------------------------------
        entrada = input()


        if entrada != 'FIM':

            # musica(str) - diva(str) - Era(str) - stream(int)
            entrada = entrada.split(' - ')

            musica = entrada[0]
            diva   = entrada[1]
            era    = entrada[2]
            stream = int(entrada[3])

            if (era in dic): 

                if (musica in dic[era]): 

                    if (diva in diva_era) and (era in diva_era[diva]):

                        if quant_mus_era[era] < 3:

                            if musica not in spotify[diva]: 

                                quant_mus_era[era] += 1
                                spotify[diva][musica] = (era, stream)

                            else:
                                print("A musica ja foi mencionada")
                        else:
                            print("Quantidade maxima de musicas dessa era atingida")
                    else:
                        print("Diva errada, tente novamente!")
                else:
                    print('Essa musica não pertence a essa ERA, tente novamente!')
            else:
                print("Essa Era não esta na disputa, tente novamete!")

        else:
            parte1 = False
            if spotify['Dua Lipa'] == {} and spotify['Olivia Rodrigo'] == {} and spotify['Katy Perry'] == {}:
                op = False

            else:
                organizar_podio(podio, spotify)
                parte2 = True

                print('===== Pódio =====')
                print(f"1° {podio[1][0]} com {int(podio[1][1])} Streams por música")
                print(f"2° {podio[2][0]} com {int(podio[2][1])} Streams por música")
                print(f"3° {podio[3][0]} com {int(podio[3][1])} Streams por música")

                if podio[1][0] == 'Katy Perry':
                    print("Katy Perry 'ruge'! Os KatyCats provam que 'Teenage Dream' e 'Prism' são eternos!")
                elif podio[1][0] == 'Olivia Rodrigo':
                    print("É 'brutal' aqui! Os Livies mostraram a força de 'SOUR' e 'GUTS'.")
                elif podio[1][0] == 'Dua Lipa':
                    print("Ela está 'Levitating', se voce não quer me ver ganhando, não aparece, não venha! Dua Lipa e seu 'Future Nostalgia' dominaram o pop.")


    elif parte2: # -----------------------------------------------------
        entrada = input()


        if entrada != 'FIM':
            #
            entrada = entrada.split(' - ')

            musica = entrada[0]
            diva   = entrada[1]

            if musica in spotify[diva]:
                if musica in entradas_fase2:
                    n = entradas_fase2[musica][0]
                    entradas_fase2[musica] = (n+1, spotify[diva][musica][1])
                else:
                    entradas_fase2[musica] = (1, spotify[diva][musica][1])
            else:
                print("Essa musica não pertence ao catálogo, tente outra")
            
        else:
            parte2 = False
            if entradas_fase2 != {}:
                
                cont = 0
                for mus in entradas_fase2:
                    musicas_raking[cont] = {
                        'musica'    : mus,
                        'quant_mus' : entradas_fase2[mus][0],
                        'stream'    : entradas_fase2[mus][1]
                    }
                    cont += 1

                soorted(musicas_raking, 'quant_mus', 'stream', 'musica')
                print(f"E a música campeã foi {musicas_raking[0]['musica']}!")

                if musicas_raking[0]['musica'] in spotify[podio[1][0]]:
                    op = False
                    print(f"Domínio completo! {podio[1][0]} levou o pódio e a melhor música")

                else:
                    parte3 = True
                    diva_melhor_musica = 'Dua Lipa' if(musicas_raking[0]['musica'] in spotify['Dua Lipa'])else 'Katy Perry' if(musicas_raking[0]['musica'] in spotify['Katy Perry'])else 'Olivia Rodrigo'

                    for d in spotify:
                        if d != podio[1][0] and d != diva_melhor_musica:
                            diva_que_nao_foi_campea_nem_teve_melhor_musica = d

                    print(f"Apesar da {podio[1][0]} ter vencido no Pódio, a melhor música ficou com {diva_melhor_musica}")
                    print(f"Por isso teremos uma segunda chance para {diva_melhor_musica}")
                    print("A decisão será feita por votação popular, mas aparentemente faltou verba para o Spotify, pois os nomes vieram bagunçados, Quem será a Campeã?")

            else:
                op = False
                print('Nenhuma música foi mencionada, acho que no fim elas estão sem hype')

    elif parte3: # -----------------------------------------------------
        entrada = input()

        
        # Fa_criptografado(str) - chave_de_criptografia_fa(int) - diva_criptografada(str) - chave_de_criptografia_diva(int)
        entrada = entrada.split(' - ')

        fa_crip = entrada[0]
        chave_fa = int(entrada[1])
        diva_crip = entrada[2]
        chave_di = int(entrada[3])

        fa = descripto(fa_crip, chave_fa)
        diva = descripto(diva_crip, chave_di)

        if fa.lower() != 'fim' and diva.lower() != 'fim':

            if diva in spotify:
                print(f"Voto de {fa} computado para {diva}")

                votacao[diva] += 1
                if fa in fas:
                    n = fas[fa]
                    fas[fa] = n + 1

                else:
                    fas[fa] = 1

        else:
            op = False

            if fas == {}:
                print("Aparentemente os Streams das duas foram comprados, a vencedora só pode ser a que não comprou nenhum voto")
                print(f"Parabéns {diva_que_nao_foi_campea_nem_teve_melhor_musica}, a campeã final!")
            else:
                diva_campea = ''
                dc = 0
                maior_fan = ''
                mf = 0

                for v in votacao:
                    if votacao[v] > dc:
                        diva_campea = v
                        dc = votacao[v]

                for f in fas:
                    if fas[f] > mf:
                        maior_fan = f
                        mf = fas[f]

                print(f"A campeã final é {diva_campea}")
                print(f"E o(A) maior fã da diva {diva_campea} é {maior_fan}")

