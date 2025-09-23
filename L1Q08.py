casos=int(input())
dias=int(input())
as_casos=int(input())
op_campo=int(input())
op_especial=input()
media_diaria=casos/dias

pontuacao = casos*2 + as_casos*1.5 + op_campo*0.5

if op_especial=='sim':
    t_op_especial=input()
    localizacao=input()
    pontuacao = pontuacao*1.5 if t_op_especial=='Infiltração' else pontuacao*30/100 if t_op_especial=='Escuta' else pontuacao*1.2 if t_op_especial=='Invasão' else pontuacao*1.1
    # 1º Requisito
    if localizacao in ['Manhattan', 'Brooklyn']:
        print('Pelo menos nos bairros corretos Jake está!')
    else:
        print('Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!')
# 2º Requisito
if casos>=20:
    print('Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição.')
else:
    print('Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.')
# 3º Requisito
if media_diaria>=0.5:
    print('Parece que Jake é bem consistente na sua média diária de casos.')
else:
    print('A média diária de casos tá muito baixa, Peralta foi desclassificado.')
# 4º Requisito
if as_casos>=5:
    print('Peralta ajudou bastante outros detetives, ele ainda está na competição!')
else:
    print('Desclassificado! Jake precisa ajudar mais os companheiros.')
# 5º Requisito
if op_campo >= 20:
    print('Jake ainda sobrevive por sua participação em campo, será que ele vai levar pra casa o prêmio?')
else:
    print('Peralta precisa sair mais da delegacia, está faltando ação em campo!')

if op_especial=='sim':
    print('Minha nossa! Jake Peralta é realmente um detetive diferenciado.')
else:
    print('Para que operação especial quando se tem números, não é?')
if pontuacao>=70:
    print('Jake é candidato forte ao prêmio. Será que Holt vai premiá-lo?')
elif pontuacao>40:
    print('Muito bem! Mas ainda é incerto se vai ser suficiente para ganhar o prêmio.')
else:
    print('Muito difícil de Jake ganhar o prêmio.')
