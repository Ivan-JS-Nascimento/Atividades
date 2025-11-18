def x(tictac, mapa, byte, saida):

    if tictac == 0:
        if byte == saida:

        return

    return

# ----------------------

byte = []
saida = []
hora = input()
auxiliar = hora.split(':')
tictac = auxiliar[1]

n = int(input())

mapa = [[input()] for _ in range(n)]

for i in range(n):
    auxi = []

    for l in mapa[i]:
        if l == 'S':
            saida = [i , mapa[i].index(l)]

        elif l == 'B':
            byte = [i , mapa[i].index(l)]

        auxi.append(l)
    mapa[i] = auxi

x(tictac, mapa)


