# -------funçoes----------

def permuta(nome1, nome2)->bool:
    validacao = False

    if ''.join(sorted(nome1, key=str.lower)) == ''.join(sorted(nome2, key=str.lower)):
        validacao = True

    return validacao

def cal_pontuacao(grammys, popularidade, shows_no_brasil):
    return  (grammys*15)+(popularidade*10)+(shows_no_brasil*5)

# --------main---------
op = True
conflitos = {
    'Katy Perry': ('Taylor Swift',),
    'Taylor Swift': ('Katy Perry', 'Ariana Grande', 'Olivia Rodrigo', 'Dua Lipa'),
    'Madonna': ('Lady Gaga',),
    'Lady Gaga': ('Madonna',),
    'Mariah Carey': ('Jennifer Lopez',),
    'Jennifer Lopez': ('Mariah Carey',),
    'Christina Aguilera': ('Britney Spears',),
    'Britney Spears': ('Christina Aguilera',),
    'Nicki Minaj': ('Doja Cat'),
    'Anitta': ('Ludmilla',),
    'Ludmilla': ('Anitta',),
    'Ariana Grande': ('Taylor Swift', 'Cynthia Erivo'),
    'Sabrina Carpenter': ('Camila Cabello', 'Olivia Rodrigo', 'Doja Cat'),
    'Camila Cabello': ('Sabrina Carpenter',),
    'Olivia Rodrigo': ('Taylor Swift', 'Sabrina Carpenter'),
    'Dua Lipa': ('Taylor Swift',),
    'Doja Cat': ('Nicki Minaj', 'Sabrina Carpenter'),
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

while op:

    #{nome_candidata} - {país} - {grammys} - {popularidade} - {shows_no_brasil}
    entrada = input()

    if entrada != 'FIM DAS INSCRIÇÕES.':
    # fase 1
        entrada = entrada.split(' - ')

        nome_candidata  = entrada[0]
        pais            = entrada[1]
        grammys         = entrada[2]
        popularidade    = entrada[3]
        shows_no_brasil = entrada[4]

        #1- A pontuação é calculada pela fórmula de Impacto Cultural Ponderado:
        pontuacao = cal_pontuacao(grammys, popularidade, shows_no_brasil)

        #2- Bônus e Penalidades:
        if pais == 'Brasil':
            pontuacao += 50
        elif pais == 'EUA':
            pontuacao = pontuacao-50 if(pontuacao>=50)else 0

        #3- Diva Banida:
        if not permuta('Azealia Banks',nome_candidata):
            #4- Infiltração Americana:
            if pais != 'EUA':
                for diva in divas_estadunidenses:
                    if permuta(nome_candidata, diva):
                        pontuacao = pontuacao-100 if(pontuacao>=100)else 0
                        nome_candidata = diva
                        pais = 'EUA'

            #OBS
            if nome_candidata not in competidoras:
                competidoras[nome_candidata] = (pais, grammys, popularidade, shows_no_brasil, pontuacao)

    # fase 2

    else:
        op = False