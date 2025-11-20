# obs: descomente todos os #? para entender melhor o caminho que byte percorre

def caminho(n, tictac, mapa, byte, saida, vali, visitado, t):
# condicoes de retorno --

#?    guarda_posicao=''
    if visitado != [] and byte in visitado: # ja passou aqui
        return t, vali

    visitado.append(byte.copy()) # guarda o caminho atual

    if byte == saida: # caso chegue na saida 
        if t == 0:
            t = tictac

        elif tictac < t: # guranda o menor caminho
            t = tictac

        return t, True

    elif tictac >= 60: # caso o tempo acabe
        return t, vali

# -----------------------
# movivemtacoes ---------

    b = [byte[0] + 1, byte[1]] # anda uma casa para baixo

    if (b[0] < n and b[1] < n and b[0] >= 0 and b[1] >= 0) and (mapa[ b[0] ][ b[1] ] != 'A') : # esta dentro do mapa e nao esta encima de uma abobora
#?        guarda_posicao = mapa[b[0]][b[1]]
#?        mapa[b[0]][b[1]] = 'B'
#?        for i in mapa:
#?            print(i)
#?        print()

        t, vali = caminho(n, tictac+1, mapa, b, saida, vali, visitado.copy(), t)

#?        mapa[b[0]][b[1]] = guarda_posicao
#?        for i in mapa:
#?            print(i)
#?        print()

    

    b = [byte[0],byte[1] + 1] # anda uma casa para a direita

    if (b[0] < n and b[1] < n and b[0] >= 0 and b[1] >= 0) and (mapa[b[0]][b[1]] != 'A') : # esta dentro do mapa e nao esta encima de uma abobora
#?        guarda_posicao = mapa[b[0]][b[1]]
#?        mapa[b[0]][b[1]] = 'B'
#?        for i in mapa:
#?            print(i)
#?        print()

        t, vali = caminho(n, tictac+1, mapa, b, saida, vali, visitado.copy(), t)

#?        mapa[b[0]][b[1]] = guarda_posicao
#?        for i in mapa:
#?            print(i)
#?        print()



    b = [byte[0] - 1,byte[1]] # anda uma casa para cima

    if (b[0] < n and b[1] < n and b[0] >= 0 and b[1] >= 0) and (mapa[b[0]][b[1]] != 'A') : # esta dentro do mapa e nao esta encima de uma abobora
#?        guarda_posicao = mapa[b[0]][b[1]]
#?        mapa[b[0]][b[1]] = 'B'
#?        for i in mapa:
#?            print(i)
#?        print()

        t, vali = caminho(n, tictac+1, mapa, b, saida, vali, visitado.copy(), t)

#?        mapa[b[0]][b[1]] = guarda_posicao
#?        for i in mapa:
#?            print(i)
#?        print()



    b = [byte[0],byte[1] - 1] # anda uma casa para esquerda

    if (b[0] < n and b[1] < n and b[0] >= 0 and b[1] >= 0) and (mapa[b[0]][b[1]] != 'A') : # esta dentro do mapa e nao esta encima de uma abobora
#?        guarda_posicao = mapa[b[0]][b[1]]
#?        mapa[b[0]][b[1]] = 'B'
#?        for i in mapa:
#?            print(i)
#?        print()

        t, vali = caminho(n, tictac+1, mapa, b, saida, vali, visitado.copy(), t)

#?        mapa[b[0]][b[1]] = guarda_posicao
#?        for i in mapa:
#?            print(i)
#?        print()
# ---------------------

    return t, vali

# fim da funcao ----------------------
# main -------------------------------

byte = []
saida = []
mapa = []
hora = input()
auxiliar = hora.split(':')
tictac = int(auxiliar[1])

print(f'O relógio marca 23 horas e {tictac} minuto(s)! Byte tem apenas {60-tictac} minuto(s) para escapar!')

n = int(input())

for i in range(n):
    m = input()
    mapa.append(list(m))

for i in range(n):
    for l in mapa[i]: 
        if l == 'S':
            saida = [i , mapa[i].index(l)]

        elif l == 'B':
            byte = [i , mapa[i].index(l)]

tic, vali = caminho(n, tictac, mapa, byte, saida, False, [], 0)


if vali:
    precid = tic-tictac
    folga = 60-tic
    print(f'CONSEGUIMOS!! Byte precisou de {precid} minuto(s) para conseguir escapar!')

    if folga>10:
        print(f'Abóboras CInistras que nada! Byte mostrou quem é que manda e conseguiu sair faltando {folga} minutos para elas acordarem')
    else:
        print('Ufa! Essa foi por pouco! Mas com ajuda dos alunos de IP essas abóboras nem pareciam tão sinistras assim.')
else:
    print('NÃÃÃÃO! Tudo isso por causa de um docinho! Você estará para sempre conosco, Byte!')
