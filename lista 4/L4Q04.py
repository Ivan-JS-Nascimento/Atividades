
Lorelei = [
        ["Lapras", "agua", 220, 50, "Raio de Gelo", 60, "agua", 60],
        ["Blastoise", "agua", 180, 55, "Hidro Bomba", 65, "agua", 78],
        ["Victreebel", "grama", 160, 40, "Folha Navalha", 55, "grama", 70],
        ["Ninetales", "fogo", 170, 45, "Lança-chamas", 60, "fogo", 100]
    
]

bruno = [
        ["Charizard", "fogo", 190, 40, "Presa de Fogo", 70, "fogo", 100],
        ["Arcanine", "fogo", 180, 50, "Velocidade Extrema", 60, "fogo", 95],
        ["Kingler", "agua", 170, 60, "Caranguejo Martelo", 65, "agua", 75],
        ["Jolteon", "eletrico", 150, 35, "Choque do Trovão", 55, "eletrico", 130]
    
]

agatha = [
        ["Venusaur", "grama", 180, 50, "Raio Solar", 70, "grama", 80],
        ["Vileplume", "grama", 160, 45, "Pó do Sono", 50, "grama", 50],
        ["Raichu", "eletrico", 160, 40, "Investida Trovão", 65, "eletrico", 110],
        ["Poliwrath", "agua", 190, 55, "mico", 60, "agua", 70]
]

lance = [
        ["Electabuzz", "eletrico", 180, 45, "Soco de Trovão", 75, "eletrico", 105],
        ["Jolteon", "eletrico", 170, 35, "Onda de Trovão", 60, "eletrico", 130],
        ["Exeggutor", "grama", 160, 40, "Bomba de Semente", 65, "grama", 55],
        ["Magmar", "fogo", 175, 40, "Giro de Fogo", 55, "fogo", 93]
]

jogador: list[Unknown] = []
# Uma para calcular o dano que um pokemon irá causar em outro baseado tanto no tipo como poder de ataque e defesa do oponente
# Uma para fazer o manejo do combate em turnos entre dois pokemons
# Uma função principal em que as batalhas de turnos entre os pokemons irão ocorrer.
def main(jogador, oponete):
    print('====================
    print(' BATALHA VAI COMEÇAR!')
    print('====================')

def organizar_time():
    time = input().split(' - ')
    for t in time:
        ix = time.index(t)
        if t.isdigit():
            time[ix] = int(t)
    return time


print('Hora de montar seu time Pokémon!')
# recebendo time
for i in range(4):
    time = organizar_time()
    jogador.append(time)

print('Qual membro da Elite Four você deseja enfrentar?')
oponete = input()

# fase de batalha
main(jogador, oponete)
