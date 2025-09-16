nome_competidor1 = input()
pasteis_competidor1 = int(input())
nome_competidor2 = input()
pasteis_competidor2 = int(input())
nome_competidor3 = input()
pasteis_competidor3 = int(input())

if nome_competidor1.lower() == 'lineu' or nome_competidor2.lower() == 'lineu' or nome_competidor3.lower() == 'lineu':
    print('Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!')
else:
    campeao= ''
    p_campeao=0

    if pasteis_competidor1 > pasteis_competidor2:
        if pasteis_competidor1 > pasteis_competidor3:
            campeao = nome_competidor1
            p_campeao = pasteis_competidor1
        else:
            campeao = nome_competidor3
            p_campeao = pasteis_competidor3
    else:
        if pasteis_competidor2>pasteis_competidor3:
            campeao = nome_competidor2
            p_campeao = pasteis_competidor2
        else:
            campeao = nome_competidor3
            p_campeao = pasteis_competidor3
    
    print(f'A(O) campeã(o) é {campeao}, com {p_campeao} pastéis consumidos!')

    if nome_competidor1.lower() == 'floriano' or nome_competidor2.lower() == 'floriano' or nome_competidor3.lower() == 'floriano':
        if campeao.lower!='floriano':
            print(f'Anos comendo pastel e perdeu justo para {campeao}, lastimável, Sr. Flor!')
    
    if campeao.lower == 'agostinho':
        if p_campeao>100:
            print('Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!')
        if 50 < p_campeao < 100:
            print('Agostinho madrugou no taxi e veio cheio de fome para a competição!')