op = True
vida = 100

def ataque(ata, v):
    if ata == 'Você não tem o que é necessário para escalar.':
        v -= 20
        print('Eu nunca vou conseguir chegar ao topo :(')

    if ata == 'NÓS NUNCA DEVERÍAMOS TER SAÍDO DE CASA! VAMOS MORRER NESSA MONTANHA!':
        v -= 50
        print('NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!')

    return v


def defesa(defe, v):
    if defe == 'Calma Badeline, nós vamos conseguir.':
        v += 25

    if defe == 'Eu sei que somos capazes! Vamos em frente!':
        n = int(input())
        v += 10*n

    if defe == 'Madeline, nós estamos com você. Continue!':
        v += 60

    return v

while op:

    madeline = input()
    vida = ataque(madeline, vida)
    if vida <= 0:
        op = False
        print('Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima.')
    else:
        badeline = input()
        vida = defesa(badeline, vida)
        if vida >= 150:
            op = False
            print('Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista.')
