# obs: no fim de cada pokemon tem um index a mais, ele representa o hp atual
#  enquanto o na posicao [2] representa o hp totsl
lorelei = [
        ["Lapras", "agua", 220, 50, "Raio de Gelo", 60, "agua", 60, 220],
        ["Blastoise", "agua", 180, 55, "Hidro Bomba", 65, "agua", 78, 180],
        ["Victreebel", "grama", 160, 40, "Folha Navalha", 55, "grama", 70, 160],
        ["Ninetales", "fogo", 170, 45, "Lança-chamas", 60, "fogo", 100, 170]
    
]
bruno = [
        ["Charizard", "fogo", 190, 40, "Presa de Fogo", 70, "fogo", 100, 190],
        ["Arcanine", "fogo", 180, 50, "Velocidade Extrema", 60, "fogo", 95, 180],
        ["Kingler", "agua", 170, 60, "Caranguejo Martelo", 65, "agua", 75, 170],
        ["Jolteon", "eletrico", 150, 35, "Choque do Trovão", 55, "eletrico", 130, 150]
    
]
agatha = [
        ["Venusaur", "grama", 180, 50, "Raio Solar", 70, "grama", 80, 180],
        ["Vileplume", "grama", 160, 45, "Pó do Sono", 50, "grama", 50, 160],
        ["Raichu", "eletrico", 160, 40, "Investida Trovão", 65, "eletrico", 110, 160],
        ["Poliwrath", "agua", 190, 55, "Soco Dinâmico", 60, "agua", 70, 190]
]
lance = [
        ["Electabuzz", "eletrico", 180, 45, "Soco de Trovão", 75, "eletrico", 105, 180],
        ["Jolteon", "eletrico", 170, 35, "Onda de Trovão", 60, "eletrico", 130, 170],
        ["Exeggutor", "grama", 160, 40, "Bomba de Semente", 65, "grama", 55, 160],
        ["Magmar", "fogo", 175, 40, "Giro de Fogo", 55, "fogo", 93, 175]
]
jogador = []

# ------------------bloco das funcoes------------------------

# Uma para calcular o dano que um pokemon irá causar em outro baseado tanto no tipo como poder de ataque e defesa do oponente
def calcular_dano(n, ataque, tipo_a, defesa, tipo_p)->int:
    # tipo_a é o tipo do ataque do pokemon atacante
    # tipo_p é o tipo do pokemon defensor
    dano_base = ataque - (defesa/2)
    mult = 1

    if tipo_a == 'fogo':
        if tipo_p == 'grama':
            mult = 2
        elif tipo_p == 'agua':
            mult = 0.5

    elif tipo_a == 'agua':
        if tipo_p == 'fogo':
            mult = 2
        elif tipo_p == 'grama':
            mult = 0.5

    elif tipo_a == 'grama':
        if tipo_p == 'agua':
            mult = 2
        elif tipo_p == 'fogo':
            mult = 0.5

    elif tipo_a == 'eletrico' and tipo_p == 'agua':
        mult = 2

    if mult == 2:
        print(f'{n} é super efetivo!')
    elif mult == 0.5:
        print(f'{n} não é muito efetivo...')

   
    dano_final = int(dano_base * mult)
    if dano_final<1: dano_final = 1

    return dano_final
    
# Uma para fazer o manejo do combate em turnos entre dois pokemons
def turno(pokemon1, pokemon2, placar):
    op = True
    op1 = False
    num_turno = 1
    # definir quem começa 
    if pokemon1[7]<pokemon2[7]:
        # inverte eles ja que o oponete vai começar 
        pokemon1, pokemon2 = pokemon2, pokemon1
        op1 = True

    while op:
        print()
        print(f'-- Turno {num_turno} --')

        print()
        if op1: # caso eles tenham sido trocados
            print(f'{pokemon1[0]} do oponente usa {pokemon1[4]}!')
        else:
            print(f'{pokemon1[0]} usa {pokemon1[4]}!')

        dano = calcular_dano(pokemon1[4], pokemon1[5], pokemon1[6], pokemon2[3], pokemon2[1])
        pokemon2[8] -= dano if( pokemon2[8]>=dano )else pokemon2[8]
        print(f'Causou {dano} de dano. HP de {pokemon2[0]} agora é {pokemon2[8]}/{pokemon2[2]}.')

        if pokemon2[8]>0: # se o pokemon2 morrer, acaba aqui
            print()
            if op1: # caso eles tenham sido trocados
                print(f'{pokemon2[0]} usa {pokemon2[4]}!')
            else:
                print(f'{pokemon2[0]} do oponente usa {pokemon2[4]}!')
        
            dano = calcular_dano(pokemon2[4], pokemon2[5], pokemon2[6], pokemon1[3], pokemon1[1])
            pokemon1[8] -= dano if( pokemon1[8]>=dano )else pokemon1[8]
            print(f'Causou {dano} de dano. HP de {pokemon1[0]} agora é {pokemon1[8]}/{pokemon1[2]}.')
            if pokemon1[8]<=0:
                print()
                if op1:
                    print(f'{pokemon1[0]} do oponente foi derrotado!')
                    placar[0] += 1
                else:
                    print(f'{pokemon1[0]} foi derrotado!')
                    placar[1] += 1
                op = False
        else:
            print()
            if op1:
                print(f'{pokemon2[0]} foi derrotado!')
                placar[1] += 1
            else:
                print(f'{pokemon2[0]} do oponente foi derrotado!')
                placar[0] += 1
            op = False

        num_turno+=1

    return placar
        
# Uma função principal em que as batalhas de turnos entre os pokemons irão ocorrer.
def main(jogador, oponete):
    placar = [0 , 0]
    op = True
    num_rodada = 1
    ix_p = -1
    ix_o = -1
    print('====================')
    print('A BATALHA VAI COMEÇAR!')
    print('====================')

    # Início da Rodada
    while op:
        op1 = True
        op2 = True

        # escolhe os pokemons disponiveis na sequencia recebida
        for i in range(4):
            if jogador[i][8] > 0 and op1:
                ix_p = i
                op1 = False
        
            if oponete[i][8] > 0 and op2:
                ix_o = i
                op2 = False

        if op1 or op2: # batalha acabou
            if op1:
                print()
                print('========================================')
                print('Que pena! Você foi derrotado.')
                print('========================================')

            else:
                print()
                print('========================================')
                print('Parabéns! Você venceu a batalha Pokémon!')
                print('========================================')

            op = False
        else:
            print()
            print(f'--- Rodada {num_rodada} ---')
            print(f'{jogador[ix_p][0]}, eu escolho você!')
            print(f'{oponete[ix_o][0]}, vai!')
            print('--------------------')

            placar = turno(jogador[ix_p], oponete[ix_o], placar)

            # placar
            print()
            print('--------------------')
            print()
            print(f'Placar: {placar[0]} X {placar[1]}')
 
        num_rodada+=1

def organizar_time():
    time = input().split(' - ')
    for t in time:
        ix = time.index(t)
        if t.isdigit():
            time[ix] = int(t)
    time.append(time[2]) # hp atual
    return time

# -----------------------------------------------------------

print('Hora de montar seu time Pokémon!')
print()
# recebendo time
for i in range(4):
    time = organizar_time()
    jogador.append(time)

print('Qual membro da Elite Four você deseja enfrentar?')
print()
oponete = input()

# fase de batalha
if oponete == 'lorelei':
    main(jogador, lorelei)
elif oponete == 'bruno':
    main(jogador, bruno)
elif oponete == 'agatha':
    main(jogador, agatha)
elif oponete == 'lance':
    main(jogador, lance)
