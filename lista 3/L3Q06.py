
print('Senhoras e senhores, o desfile de gala do CIn vai começar!')

quant_total_pessoas = int(input())
marca_do_patrocinador = input()
monitores_c_ip = ['Adrieli Queiroz', 'Arthur Jorge', 'César Cavalcanti', 'Elisson Oliveira', 'Filipe Moreira', 'Gabriela Alves', 'Joab Henrique', 'Maria Fernanda', 'Miriam Gonzaga', 'Sofia Remindes']
patrocinadores = 'Thais Linares' if marca_do_patrocinador == 'Tha Beauty' else 'Davi Brito' if marca_do_patrocinador == 'DeGuê?' else 'Edu e Fih'
invasores = []
invasao = 0
entrou = []
desfilantes = []

for i in range(quant_total_pessoas):
    desfilantes.append(input())

um = 1
for i in range(quant_total_pessoas):
    desfilante = desfilantes[i]

    # 1 regra
    if desfilante in monitores_c_ip:
        entrou.append(desfilante)
        monitores_c_ip.remove(desfilante)
        print(f'Desfilante de n° {i+um}: {desfilante}!')

    # 2 regra
    elif desfilante == patrocinadores:

        print('Invasão tolerada por motivos de patrocínio!')
        entrou.append(desfilante)
        print(f'Desfilante de n° {i+um}: {desfilante}!')

    # 3 regra
    else:
        invasao += 1
        invasores.append(desfilante)
        print(f'{desfilante} invadiu a passarela! Segurem ele(a), produção!')
        op = True
        if monitores_c_ip != []:

            for j in range(len(monitores_c_ip)-1):
                if monitores_c_ip[j] not in desfilantes and op :
                    print(f'Desfilante de n° {i+um}: {monitores_c_ip[j]}!')
                    entrou.append(monitores_c_ip[j])
                    monitores_c_ip.remove(monitores_c_ip[j])
                    op = False

        if monitores_c_ip == [] or op :
            print(f'Desfilante de n° {i+um}: {desfilante}?! Pelo visto não havia como substituir...')
            entrou.append(desfilante)

        if invasao == 3:
            um = 2
            print('Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!')
            entrou.append('Core')
            print(f'Desfilante de n° {i+um}: Core!')

if 'Gretchen' in invasores or 'Tulla Luana' in invasores or 'Inês Brasil' in invasores:
    print('Nas arquibancadas do CIn, sussurros indignados agitam a multidão...')

    if 'Gretchen' in invasores:
        print('"Eles tem que respeitar os meus 37 anos de carreira! Eu hoje sou um ícone, se eu morrer hoje eu vou continuar sendo a Gretchen!"')

    if 'Tulla Luana' in invasores:
        print('"Ninguém ser humano está acima de mim! Mas eu estou acima de muitos... é assim que eu penso."')

    if 'Inês Brasil' in invasores:
        print('"É aquele ditado... Vamo fazer o quê?"')