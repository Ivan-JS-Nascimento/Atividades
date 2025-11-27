
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

# ato 1
op = True
while op:
    entrada = input

    if entrada != "FIM_ATO_1":
        entrada = entrada.split(', ')

        nome_musica  = entrada[0]
        genero = entrada[1]
        duracao_minutos_segundos = entrada[2]

        # afronta da Taylor Swift
        if nome_musica !=  "Actually Romantic":

            # genero do ato
            if genero in ["Hyperpop", "Pop"]:
                duracao_segundos = cal_time(duracao_minutos_segundos)

                # maximo 600 segundos (10 minutos)
                if (time_ato1 - duracao_segundos) >= 0:
                    time_ato1 -= duracao_segundos
                    
 

    else:
        op = False
# ato 2
op = True
while op:
    entrada = input

    if entrada != "FIM_ATO_2":
        ...


# ato 3
op = True
while op:
    entrada = input

    if entrada != "FIM_SHOW":
        ...
