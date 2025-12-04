
dic = {
# ============ Dua Lipa =================
    'Future_Nostalgia' : (
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

    'Radical_Optimism' : (
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
    'Teenage_Dream' : (
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
    'Dua Lipa'       : ('Future_Nostalgia','Radical_Optimism'),
    'Olivia Rodrigo' : ('SOUR','GUTS'),
    'Katy Perry'     : ('Teenage_Dream','Prism')
}

spotify = {
    #                 musica : (era, stream)
    'Dua Lipa'       : {},
    'Olivia Rodrigo' : {},
    'Katy Perry'     : {}
}

podio = {
    1 : '',
    2 : '',
    3 : ''
}

entradas_fase2 = {}

quant_mus_era ={
    'Future_Nostalgia': 0,
    'Radical_Optimism' : 0,
    'SOUR' : 0,
    'GUTS' : 0,
    'Teenage_Dream' : 0,
    'Prism' : 0
}

musicas_raking = []

votacao = {
    'Dua Lipa'       : 0,
    'Olivia Rodrigo' : 0,
    'Katy Perry'     : 0
}

fas = {}

op = True
quant_m_dua    = 23
quant_m_olivia = 23
quant_m_katy   = 25
parte1 = True
parte2 = False
parte3 = False

# -------------------------------FUNÇÔES-----------------------------------

def organizar_podio(podio, spotify):

    media_stream = 0
    somatorio_streams_diva = 0
    total_musicas_diva = 0
    list_divas = []
    list_d_ordenada = []

    for diva in spotify:
        for music in spotify[era]:

            total_musicas_diva += 1
            somatorio_streams_diva += spotify[era][music][1]

            media_stream = somatorio_streams_diva/total_musicas_diva

        list_divas.append({
            'nome_diva' : diva,
            'num_music' : total_musicas_diva,
            'media_str' : media_stream
        })

    list_d_ordenada = sorted(list_divas, key=lambda x : (-x['media_str'], -x['num_music'], x['nome_diva']))

    podio[1] = list_d_ordenada[0]['nome_diva']
    podio[2] = list_d_ordenada[1]['nome_diva']
    podio[3] = list_d_ordenada[2]['nome_diva']

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
                novo_ix = 26 - novo_ix

            if caracter.isupper():
                mens_descripto += indice_letra[novo_ix].upper()
            else:
                mens_descripto += indice_letra[novo_ix]
        else:
            mens_descripto += caracter

    return mens_descripto

#  --------------------------------MAIN------------------------------------

while op:

    entrada = input()

    if parte1: # -----------------------------------------------------
        if entrada != 'FIM':

            # musica(str) - diva(str) - Era(str) - stream(int)
            entrada = entrada.split(' - ')

            musica = entrada[0]
            diva   = entrada[1]
            era    = entrada[2]
            stream = int(entrada[3])

            if (era in dic) and (musica in dic[era]) and (era in diva_era[diva]):
                
                if musica not in spotify[diva] and quant_mus_era[era] < 3:
                    quant_mus_era[era] += 1
                    spotify[diva][musica] = (era, stream)

                else:
                    ...
            else:
                ...

        else:
            parte1 = False
            if spotify.items() == {}:
                op = False
                parte2 = False
            else:
                organizar_podio(podio, spotify)
                parte2 = True

    elif parte2: # -----------------------------------------------------
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
            parte2 = False
            if entradas_fase2 != {}:

                for mus in entradas_fase2:
                    musicas_raking.append({
                        'musica'    : mus,
                        'quant_mus' : entradas_fase2[mus][0],
                        'stream'    : entradas_fase2[mus][1]
                    })
                    
                musicas_raking = sorted(musicas_raking, key=lambda x : (-x['quant_mus'],-x['stream'],x['musica']))

                if musicas_raking[0]['musica'] in spotify[podio[1]]:
                    ...
                else:
                    parte3 = True

    elif parte3: # -----------------------------------------------------
        # Fa_criptografado(str) - chave_de_criptografia_fa(int) - diva_criptografada(str) - chave_de_criptografia_diva(int)
        entrada = entrada.split(' - ')

        fa_crip = entrada[0]
        chave_fa = entrada[1]
        diva_crip = entrada[2]
        chave_di = entrada[3]

        fa = descripto(fa_crip, chave_fa)
        diva = descripto(diva_crip, chave_di)

        if fa.lower() != 'fim' and diva.lower() != 'fim':

            if diva in spotify:
                votacao[diva] += 1
                if fa in fas:
                    n = fas[fa]
                    fas[fa] = n + 1
                else:
                    fas[fa] = 1

        else:
            ...
