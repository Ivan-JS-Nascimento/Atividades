dagao = 1800 # vida do dragao fatalis

# pontos de vida dos caçadores
cacador1 = 200 # possue great_sword
cacador2 = 200 # possue glaive_inseto
cacador3 = 200 # possue fuzi_arco

status_da_great_sword = 'desprotegido!'
status_do_glaive_inseto = 'desprotegido!'
status_da_fuzi_arco = 'desprotegido!'

def great_sword(a1):
    dano = 0
    if a1 == 'Golpe Carregado':
        dano = 165
    elif a1 == 'Corte Largo':
        dano = 120
    elif a1 == 'Divisor de Mundos':
        dano = 200

    return dano

def glaive_inseto(a2):
    dano = 0
    cura = 0
    if a2 == 'Corte Aéreo':
        dano = 100
    elif a2 == 'Descida Carregada':
        dano = 120
    elif a2 == 'Kinseto':
        cor_extrato = input()
        if cor_extrato == 'Vermelho':
            dano = 40
        elif cor_extrato == 'Amarelo':
            dano = 15
        elif cor_extrato == 'Verde':
            cura + 40

    return dano, cura

def fuzi_arco(a3):
    dano = 0
    if a3 == 'Tiro Carregado':
        dano = 90
    elif a3 == 'Bala de Penetração':
        dano = 120
    elif a3 == 'Tiro Devastador':
        dano = 150

    return dano
def fatalis(d):
    dano = 0
    if d == 'Ataque com Cauda':
        dano = 55
    elif d == 'Bola de Fogo':
        dano = 65
    elif d == 'Mar de Chamas Negras':
        # ...
x = 4
for i in range(4):
    if dagao > 0:

        if cacador1 > 0:
            a1 = input()
            dagao -= great_sword(a1)

        if cacador2 > 0:
            a2 = input()

        if cacador3 > 0:
            a3 = input()
        
        if dagao > 0:
            d = input()