
diva_era = {
    'Dua Lipa'       : ('Future_Nostalgia','Radical_Optimism'),
    'Olivia Rodrigo' : ('SOUR','GUTS'),
    'Katy Perry'     : ('Teenage_Dream','Prism')
}

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

spotify = {
    'Dua Lipa'       : {},
    'Olivia Rodrigo' : {},
    'Katy Perry'     : {}
}

podio = {
    1 : (),
    2 : (),
    3 : ()
}

op = True
quant_m_dua    = 23
quant_m_olivia = 23
quant_m_katy   = 25
parte1 = True
parte2 = False
parte3 = False

# -------------------------------FUNÇÔES-----------------------------------
def organizar_podio(podio, spotify):
    return

#  --------------------------------MAIN------------------------------------
while op:

    entrada = input()

    if parte1: 
        if entrada != 'FIM':

            # musica(str) - diva(str) - Era(str) - stream(int)
            entrada = entrada.split(' - ')

            musica = entrada[0]
            diva   = entrada[1]
            era    = entrada[2]
            stream = int(entrada[3])

            if (era in dic) and (musica in dic[era]) and (era in diva_era[diva]):
                
                if musica not in spotify[diva]:
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

                parte2 = True


    elif parte2:
        if entrada != 'FIM':
            ...
        else:
            parte1 = False
            parte2 = True

    elif parte3:
        if entrada != '':
            ...
        else:
            parte1 = False
            parte2 = True
