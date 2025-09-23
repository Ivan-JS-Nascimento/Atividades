casos=int(input())
dias=int(input())
as_casos=int(input())
op_campo=int(input())
op_especial=input()
media_diaria=casos/dias

pontuacao = (casos*2 + as_casos*1.5 + op_campo*0.5)/4

if op_especial=='sim':
    t_op_especial=input()
    localizacao=input()
    pontuacao = pontuacao*1.5 if t_op_especial=='Infiltração' else pontuacao*30/100 if t_op_especial=='Escuta' else pontuacao*1.2 if t_op_especial=='Invasão' else pontuacao*1.1
    if localizacao in ['Manhattan', 'Brooklyn']:
        print('Pelo menos nos bairros corretos Jake está!')
    else:
        print('Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!')

if casos>=20:
    print('Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição.')
else:
    print('Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.')

if media_diaria>=0.5:
    print('Parece que Jake é bem consistente na sua média diária de casos.')
else:
    print('A média diária de casos tá muito baixa, Peralta foi desclassificado.')

if as_casos>=5:
    print('Peralta ajudou bastante outros detetives, ele ainda está na competição!')
else:
    print('Desclassificado! Jake precisa ajudar mais os companheiros.')
