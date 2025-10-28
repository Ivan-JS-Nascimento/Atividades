op = True
vida = 100


while op:

    madeline = input()

    badeline = input()


def ataque(ata):
    if ata == 'Você não tem o que é necessário para escalar.':
        vida -= 20
        print('Eu nunca vou conseguir chegar ao topo :(')

    if ata == 'NÓS NUNCA DEVERÍAMOS TER SAÍDO DE CASA! VAMOS MORRER NESSA MONTANHA!':
        vida -= 50
        print('NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!')

def defesa(defe):
    if defe == 'Calma Badeline, nós vamos conseguir.':
        vida += 25