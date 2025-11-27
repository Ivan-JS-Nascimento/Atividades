vida_amorosa = {
    'Jake Gyllenhaal' : ('All too Well', 'We are never ever getting back together', 'Red'),
    'Joe Jonas'       : ('Forver & Always', 'Holy Ground'),
    'Taylor Lautner'  : ('Back to December', 'I can see you', 'Midnight rain'),
    'Tom Hiddleston'  : ('Getaway Car'),
    'Joe Alwyn'       : ('Paper Rings', 'Lover', 'So Long London'),
    'Harry Styles'    : ('Style', 'Out of the Woods', 'All You Had to Do Was Stay'),
    'Travis Kelce'    : ('The Fate of Ophelia', 'The Alchemy', "Wi$h Li$t")
}

acontecimento_carreira = {
    'Fearless'      : ('Ganhou o VMA 2009, porém Kanye West interrompeu seu discurso de vitória. Também ganhou o Grammy de Álbum do Ano (2010), sendo a artista mais jovem da história (na época) a receber esse prêmio.'),
    'Speak Now'     : ('Teve uma turnê mundial massiva que consolidou seu status de superestrela global, o albúm Speak Now vendeu mais de 1 milhão de cópias na primeira semana, superando qualquer outro álbum dos últimos dois anos.'),
    '1989'          : ('“1989” tornou-se o primeiro álbum de Taylor exclusivamente pop; a artista emplacou dois hits mundiais: Blank Space e Bad Blood. Fun Fact: Taylor nasceu em 13 de dezembro de 1989.'),
    'Reputation'    : ('O álbum foi uma resposta à mídia, às traições públicas e ao controle da narrativa sobre sua imagem. Além disso, em 2019, Taylor tem os direitos autorais de seus álbuns roubados.'),
    'The Eras Tour' : ('The Eras Tour é uma turnê comemorativa, com detalhes que buscam fazer jus á tudo que Taylor Swift fez e alcançou em seus anos de carreira. No Brasil, aconteceram seis apresentações em novembro de 2023 em São Paulo e no Rio de Janeiro.')
}

namorado_ano = {
    2008: 'Joe Jonas',
    2009: 'Taylor Lautner',
    2010: 'Jake Gyllenhaal',
    2012: 'Harry Styles',
    2016: 'Tom Hiddleston',
    2020: 'Joe Alwyn',
    2023: 'Travis Kelce'
}

roubados = []

op = True


while op:
    entradas = input()

    if entradas != 'Já chega de fatos sobre a Taylor, vai fazer a lista de IP':
        
        # 1- Informações sobre status de relacionamento:
        if entradas == "Qual a situação de relacionamento?":
            situacao = 'não estão namorando'
            nome = input()
            ano = int(input())

            if namorado_ano[ano] == nome:
                situacao = 'estão namorando'


            print(f'{nome} e Taylor Swift {situacao} em {ano}')

        #2 - Informações sobre alguma música:
        elif entradas == "Qual pessoa está relacionada essa música?":
            musica = input()
            pessoa = ''

            for chave in vida_amorosa:
                if musica in vida_amorosa[chave]:
                    pessoa = chave

            print(f'A pessoa relacionada é {pessoa}, Taylor nunca erra em suas músicas')

        #3- Listar todas as músicas relacionadas a alguém:
        elif entradas == "Quais são todas as músicas relacionadas a essa pessoa?":
            pessoa = input()

            musica = vida_amorosa[pessoa]

            if type(musica) != str:
                print(f'Cartas de amor ou indiretas, as músicas dedicadas a {pessoa} são: {", ".join(musica)}')
            else:
                print(f'Cartas de amor ou indiretas, as músicas dedicadas a {pessoa} são: {musica}')

        #4-Informação sobre alguma era:
        elif entradas == "O que aconteceu nessa era?":
            era = input()

            print(acontecimento_carreira[era])

        # ataques ----------------------------------------
        #5- Os ataques de Wayne Kest estarão sinalizados assim:
        elif entradas == "Wayne nunca deixará Taylor vencer! O CIn precisa manter o hate na diva pop, eu vou alterar as informações":
            era = input()

            frase = acontecimento_carreira[era]
            acontecimento_carreira[era] = f'{frase} Que grande mentira! Taylor Swift só mente'

            print('Cuidado, há um impostor no guia... Informações comprometidas')

        #6- Os ataques de Scooter Braun estarão sinalizados assim:
        elif entradas == "Scooter não liga que ela comprou todos os álbuns de volta, ele vai roubar tudo dessa era":
            era = input()

            roubados.append(era)
            acontecimento_carreira.pop(era)

            print(f'Para onde foi a história sobre {era}? Parece que alguém roubou tudo e não avisou a Taylor')

    else:   
        op = False

if roubados != []:
    print("Big Machine Records roubou:")
    for texto in roubados:
        print(texto)