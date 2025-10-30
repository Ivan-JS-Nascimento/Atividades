dagao = 1800 # vida do dragao fatalis

# pontos de vida dos caçadores
cacador1 = 200 # possue great_sword
cacador2 = 200 # possue glaive_inseto
cacador3 = 200 # possue fuzi_arco

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
            cura = 40

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

def fatalis(d, v1, v2, v3):
    if d == 'Ataque com Cauda':
        v1 -= 55
        v2 -= 55
        v3 -= 55

    elif d == 'Bola de Fogo':
        v1 -= 65
        v2 -= 65
        v3 -= 65
    elif d == 'Mar de Chamas Negras':
        sg = input()
        si = input()
        sf = input()

        if sg == 'Desprotegido':
            v1 = 0
        if si == 'Desprotegido':
            v2 = 0
        if sf == 'Desprotegido':
            v3 = 0

    return v1, v2, v3

print('Hora de Lutar contra a Historia!')
print()

for i in range(4):
    if dagao > 0 and (cacador1>0 or cacador2>0 or cacador3>0):
        if cacador1 > 0:
            a1 = input()
            dagao -= great_sword(a1)

        if cacador2 > 0:
            a2 = input()
            x, y = glaive_inseto(a2)
            dagao -= x
            cacador2 += y

        if cacador3 > 0:
            a3 = input()
            dagao -= fuzi_arco(a3)
        
        if dagao > 0:
            d = input()
            cacador1, cacador2, cacador3 = fatalis(d, cacador1, cacador2, cacador3,)

if dagao>0:
    print('O Fatalis conseguiu sobreviver ao combate...')
    print('O mundo corre perigo!')
else:
    print('Eu não acredito, vocês conseguiram!')
    print('Obrigado caçadores! O mundo está salvo.')
