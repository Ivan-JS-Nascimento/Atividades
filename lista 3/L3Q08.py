op =True
influ = ['Sofia Santino', 'Doarda', 'Ciclopin', 'Bruna Pinheiro']
cantor = ['Thiaguinho', 'Little Thiago', 'Neiff', 'O Diferenciado', 'Veigh', 'Mc Loma']
convidados = []
tuto = False
b1 = 0
b2 = 0

while op:
    entr_inicial = input()

    if entr_inicial == 'WhatsApp: 0 mensagens.':
        op = False
        tuto = True
    elif entr_inicial == 'CABOSSE! Bora simbora organizar essa festa.':
        op = False

    else:
        s = entr_inicial.split(' acabou de confirmar')
        conv = s[0]
        if conv in influ:
            convidados.append(conv)
            b1 = 1
        elif conv in cantor:
            b2 = 1
            if conv == 'Little Thiago':
                convidados.append('Thiaguinho')
            elif conv == 'O Diferenciado':
                convidados.append('Neiff')
            elif conv == 'Mc Loma':
                convidados.append(conv)
                convidados.append('Mirella Santos')
                convidados.append('Mariely Santos')

if tuto:
    print('I hate to tell you this BUT')
    print('Bia tava achando que ia fazer um mousse. O mousse virou uma piada, parceira')
    print('')
    print('Como a vida não precisa ser only fechos, a gente vai finalizar minha franja hoje:')
    print('Essa chapinha eu dei literalmente tipo 50 reais nela. Não é a mais potente, não é a mais mais...')
    print('mas ela é algo. Às vezes a gente só precisa ser algo, não precisa ser tudo.')
    print('E o protetor térmico? Vei, a chapinha sabe que eu tô fazendo de coração, ela nunca queimaria meu cabelo.')
    print('Espera esfriar e você vai barbarizar quando tiver pronto')
    print('É isso, tchau meus amores')

else:
    if b1 == 1 and b2 == 0:
        print('<TARDE DE FOFOCAS>')
        print(f'Convidados: {",".join(convidados)}.')
    elif b2 == 1 and b1 == 0:
        print('<PLANOS PARA FESTA>')
        print(f'Convidados: {",".join(convidados)}.')
        print('Tipo de comemoração: Paredão - Show na minha casa!!')
    else:
        print('Cachaçaria na minha casa hoje, 21h.')
        print('Todo mundo lá em casa! Tem que ser uma festa que dure muito, tipo 27 anos e 3 meses!!')