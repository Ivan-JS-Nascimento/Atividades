def caminho(n, tictac, mapa, byte, saida, vali, visitado):
    guarda_posicao=''
    if visitado != [] and byte in visitado:
        return tictac-1, vali

    visitado.append(byte.copy())

    if byte == saida:
        return tictac, True

    elif tictac >= 60:
        return tictac-1, vali

    if byte[0] < n and byte[1] < n and byte[0] >= 0 and byte[1] >= 0:
        if mapa[byte[0]][byte[1]] == 'A':
            return tictac-1, vali
    else:
        return tictac-1, vali
    
    
    byte[0] += 1 # baixo

    if byte[0] < n and byte[1] < n and byte[0] >= 0 and byte[1] >= 0:
        guarda_posicao = mapa[byte[0]][byte[1]]
        mapa[byte[0]][byte[1]] = 'B'
        for i in mapa:
            print(i)
        print()

    tictac, vali = caminho(n, tictac+1, mapa, byte, saida, vali, visitado)
    if byte[0] < n and byte[1] < n and byte[0] >= 0 and byte[1] >= 0:
        mapa[byte[0]][byte[1]] = guarda_posicao
    for i in mapa:
        print(i)
    print()
    byte[0] -= 1

    

    byte[1] += 1 # direita

    if byte[0] < n and byte[1] < n and byte[0] >= 0 and byte[1] >= 0:
        guarda_posicao = mapa[byte[0]][byte[1]]
        mapa[byte[0]][byte[1]] = 'B'
        for i in mapa:
            print(i)
        print()

    tictac, vali = caminho(n, tictac+1, mapa, byte, saida, vali, visitado)
    if byte[0] < n and byte[1] < n and byte[0] >= 0 and byte[1] >= 0:
        mapa[byte[0]][byte[1]] = guarda_posicao
    for i in mapa:
        print(i)
    print()
    byte[1] -= 1



    byte[0] -= 1 # cima

    if byte[0] < n and byte[1] < n and byte[0] >= 0 and byte[1] >= 0:
        guarda_posicao = mapa[byte[0]][byte[1]]
        mapa[byte[0]][byte[1]] = 'B'
        for i in mapa:
            print(i)
        print()

    tictac, vali = caminho(n, tictac+1, mapa, byte, saida, vali, visitado)
    if byte[0] < n and byte[1] < n and byte[0] >= 0 and byte[1] >= 0:
        mapa[byte[0]][byte[1]] = guarda_posicao
    for i in mapa:
        print(i)
        print()
    byte[0] += 1



    byte[1] -= 1 # esquerda

    if byte[0] < n and byte[1] < n and byte[0] >= 0 and byte[1] >= 0:
        guarda_posicao = mapa[byte[0]][byte[1]]
        mapa[byte[0]][byte[1]] = 'B'
        for i in mapa:
            print(i)
        print()

    tictac, vali = caminho(n, tictac+1, mapa, byte, saida, vali, visitado)
    if byte[0] < n and byte[1] < n and byte[0] >= 0 and byte[1] >= 0:
        mapa[byte[0]][byte[1]] = guarda_posicao
    for i in mapa:
        print(i)
    print()


    return tictac, vali

# ----------------------
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

tic, vali = caminho(n, tictac, mapa, byte, saida, False, [])


if vali:
    precid = tic-tictac
    print(f'CONSEGUIMOS!! Byte precisou de {precid} minuto(s) para conseguir escapar!')

    if precid>10:
        print(f'Abóboras CInistras que nada! Byte mostrou quem é que manda e conseguiu sair faltando {60-tic} minutos para elas acordarem')
    else:
        print('Ufa! Essa foi por pouco! Mas com ajuda dos alunos de IP essas abóboras nem pareciam tão sinistras assim.')
else:
    print('NÃÃÃÃO! Tudo isso por causa de um docinho! Você estará para sempre conosco, Byte!')
