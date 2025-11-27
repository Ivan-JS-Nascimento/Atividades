
# ---------funcoes-----------
def cal_time(time):
    auxi = time.split(':')
    minutos  = int(auxi[0])
    segundos = int(auxi[1])
    segundos += minutos*60

    return segundos

# --------main-----------
time_ato1 = 600
time_ato2 = 480
time_ato3 = 720

n_total_musicas = 0
n_total_descartadas = 0

dicionario_principal = { 

    'ato1' : [],

    'ato2' : [],

    'ato3' : []

    }


print("Don't sleep, don't eat, just do it on repeat! Keep bumpin' that!!!")
print()

# ato 1 -------------------------------
op = True

print('Iniciando montagem do Ato 1 (Hyperpop e Pop):')
print()

while op:
    entrada = input()

    if entrada != "FIM_ATO_1":
        entrada = entrada.split(', ')

        nome_musica  = entrada[0]
        genero = entrada[1]
        duracao_minutos_segundos = entrada[2]

        print(f'Música em análise: {nome_musica}')

        # afronta da Taylor Swift
        if nome_musica !=  "Actually Romantic":
            
            if nome_musica ==  "Talk Talk featuring troye sivan":
                print('A MAIOR AMIZADE DO POP NO PALCO? Talk to them in your own made-up language!')

            elif nome_musica ==  "Von dutch a. g. cook remix featuring addison rae":
                print("‘CAUSE THEY’RE JUST LIVING THAT LIFE! Addison Rae, a maior revelação do pop desde Britney Spears, no palco ao lado da sua amiga Charli XCX!")

            elif nome_musica == "Guess featuring billie eilish":
                print('Hey, Billie, you there?')

            # genero do ato
            if genero in ["Hyperpop", "Pop"]:
                duracao_segundos = cal_time(duracao_minutos_segundos)

                # maximo 600 segundos (10 minutos)
                if (time_ato1 - duracao_segundos) >= 0:
                    n_total_musicas += 1
                    time_ato1 -= duracao_segundos
                    dicionario_principal["ato1"].append( ( nome_musica , genero , duracao_minutos_segundos ) )
                    print(f'{nome_musica} adicionada ao Ato 1 ;).')

                else:
                    n_total_descartadas += 1
                    print(f'Muito longa! O Ato 1 já está com {600-time_ato1} segundos e essa música tem {duracao_segundos} segundos.')

            else:
                n_total_descartadas += 1
                print('Gênero errado para esse ato! Cuidado, uma música deslocada mata a vibe de um show…')

        else:
            n_total_descartadas += 1
            print('Já não basta ter exposto a Charli nessa música, agora a Taylor quer que a própria cante? GOLPE BAIXÍSSIMO!!!')
                    
    else:
        op = False
        print()


# ato 2 -------------------------------
op = True

print('Iniciando montagem do Ato 2 (Sentimental e Ballad):')
print()

while op:
    entrada = input()

    if entrada != "FIM_ATO_2":
        entrada = entrada.split(', ')

        nome_musica = entrada[0]
        genero = entrada[1]
        duracao_minutos_segundos = entrada[2]

        print(f'Música em análise: {nome_musica}')

        # afronta da Taylor Swift
        if nome_musica !=  "Actually Romantic":
            
            if nome_musica ==  "Talk Talk featuring troye sivan":
                print('A MAIOR AMIZADE DO POP NO PALCO? Talk to them in your own made-up language!')

            elif nome_musica ==  "Von dutch a. g. cook remix featuring addison rae":
                print("‘CAUSE THEY’RE JUST LIVING THAT LIFE! Addison Rae, a maior revelação do pop desde Britney Spears, no palco ao lado da sua amiga Charli XCX!")

            elif nome_musica == "Guess featuring billie eilish":
                print('Hey, Billie, you there?')

            # genero do ato
            if genero in [ "Sentimental", "Ballad"]:
                duracao_segundos = cal_time(duracao_minutos_segundos)

                # maximo 480 segundos (8 minutos)
                if (time_ato2 - duracao_segundos) >= 0:
                    n_total_musicas += 1
                    time_ato2 -= duracao_segundos
                    dicionario_principal["ato2"].append( ( nome_musica , genero , duracao_minutos_segundos ) )
                    print(f'{nome_musica} adicionada ao Ato 2 ;).')
                
                else:
                    n_total_descartadas += 1
                    print(f'Muito longa! O Ato 2 já está com {480-time_ato2} segundos e essa música tem {duracao_segundos} segundos.')

            else:
                n_total_descartadas += 1
                print('Gênero errado para esse ato! Cuidado, uma música deslocada mata a vibe de um show…')

        else:
            n_total_descartadas += 1
            print('Já não basta ter exposto a Charli nessa música, agora a Taylor quer que a própria cante? GOLPE BAIXÍSSIMO!!!')

    else:
        op = False
        print()


# ato 3 -------------------------------
op = True

print('Iniciando montagem do Ato 3 (Hyperpop e Banger):')
print()

while op:
    entrada = input()

    if entrada != "FIM_SHOW":
        entrada = entrada.split(', ')

        nome_musica = entrada[0]
        genero = entrada[1]
        duracao_minutos_segundos = entrada[2]

        print(f'Música em análise: {nome_musica}')  

        # afronta da Taylor Swift
        if nome_musica !=  "Actually Romantic":

            if nome_musica ==  "Talk Talk featuring troye sivan":
                print('A MAIOR AMIZADE DO POP NO PALCO? Talk to them in your own made-up language!')

            elif nome_musica ==  "Von dutch a. g. cook remix featuring addison rae":
                print("‘CAUSE THEY’RE JUST LIVING THAT LIFE! Addison Rae, a maior revelação do pop desde Britney Spears, no palco ao lado da sua amiga Charli XCX!")

            elif nome_musica == "Guess featuring billie eilish":
                print('Hey, Billie, you there?')

            # genero do ato
            if genero in [ "Hyperpop", "Banger" ]:
                duracao_segundos = cal_time(duracao_minutos_segundos)

                # maximo 720 segundos (12 minutos)
                if (time_ato3 - duracao_segundos) >= 0:
                    n_total_musicas += 1
                    time_ato3 -= duracao_segundos
                    dicionario_principal["ato3"].append( ( nome_musica , genero , duracao_minutos_segundos ) )
                    print(f'{nome_musica} adicionada ao Ato 3 ;).')

                else:
                    n_total_descartadas += 1
                    print(f'Muito longa! O Ato 3 já está com {720-time_ato3} segundos e essa música tem {duracao_segundos} segundos.')

            else:
                n_total_descartadas += 1
                print('Gênero errado para esse ato! Cuidado, uma música deslocada mata a vibe de um show…')

        else:
            n_total_descartadas += 1
            print('Já não basta ter exposto a Charli nessa música, agora a Taylor quer que a própria cante? GOLPE BAIXÍSSIMO!!!')

    else:
        op = False
        print()

# verifique se algum Ato ficou menor que 70% do tempo limite
prin = False
if (((600-time_ato1) * 100) / 600) < 70:
    prin = True
if (((480-time_ato2) * 100) / 480) < 70:
    prin = True
if (((720-time_ato3) * 100) / 720) < 70:
    prin = True

if prin:
    print('Tem certeza que isso é um show? Rápido desse jeito, a Charli XCX deve estar pensando nos doces do backstage…')
    print()

# --------- setlist final -----------

print('--- Ato 1 (Abertura) ---')
for valor in dicionario_principal["ato1"]:
    print(f'{valor[0]} ({valor[1]})')

else:
    if dicionario_principal["ato1"] == []:
        print('Nenhuma música adicionada a este Ato.')

    print(f'Duração total do ato: {600-time_ato1} segundos.')
    print()

print('--- Ato 2 (Sentimental) ---')
for valor in dicionario_principal["ato2"]:
    print(f'{valor[0]} ({valor[1]})')

else:
    if dicionario_principal["ato2"] == []:
        print('Nenhuma música adicionada a este Ato.')

    print(f'Duração total do ato: {480-time_ato2} segundos.')
    print()

print('--- Ato 3 (Encerramento) ---')
for valor in dicionario_principal["ato3"]:
    print(f'{valor[0]} ({valor[1]})')

else:
    if dicionario_principal["ato3"] == []:
        print('Nenhuma música adicionada a este Ato.')

    print(f'Duração total do ato: {720-time_ato3} segundos.')


# ----------------------------------
print()
print('=== RESUMO DO SHOW (BRAT APPROVED) ===')
print(f'Total de músicas na setlist: {n_total_musicas}')
print(f'Total de músicas barradas: {n_total_descartadas}')