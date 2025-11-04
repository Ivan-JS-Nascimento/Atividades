matriz = []
op = True
hp_sam = 100
hp_neil = 100
arma_atual = 'Rifle'
danoNeil = 0
hitsFogo = 0
acoes = 0 # quantidade de ações de sam
dns = 0 # quantidade de vezes que neil sofrel dano

# cordenadas
sam = []
piso_s = 'P'
neil = []
piso_n = 'P'
dist = 0

# ---funcoes---

# Função para calcular a distância de Chebyshev
def chebyshev(a,b):
    return max( abs(b[0]-a[0]), abs(b[1]-a[1]))

# Função para a ação de atirar de Sam
def arsenal(arma_atual, dist):
    dano = 0
    if arma_atual == 'Espingarda' and dist <= 2:
        dano = 25
    elif arma_atual == 'Rifle':
        if dist == 3:
            dano = 15
        else:
            dano = 5
    else:
        if dist >= 4:
            dano = 15

    return dano
# Função para a mecânica de teletransporte de Neil
def tp(sam, neil, matriz, piso_n):
    mx = 0
    matriz[neil[0]][neil[1]] = piso_n

    for i in range(6):
        for j in range(6):
            maximo = chebyshev(sam, b=[i,j])
            if maximo >= mx and matriz[i][j]!='I':
                mx = maximo
                neil = [i,j]

    piso_n = matriz[neil[0]][neil[1]]
    matriz[neil[0]][neil[1]] = 'N'

    return neil, matriz , piso_n

def mover_sam(matriz, sam, piso_s, mov):
    x = sam[0]
    y = sam[1]
    matriz[x][y] = piso_s # devolve a matriz onde sam estava em cima

    # inpede que ele se mova para fora da matriz e para a casa I
    if mov == 'W':
        if x != 0:
            if matriz[x-1][y] != 'I':
                x -= 1
        
    elif mov == 'A':
        if y != 0:
            if matriz[x][y-1] != 'I':
                y -= 1
        
    elif mov == 'S':
        if x != 5:
            if matriz[x+1][y] != 'I':
                x +=1
     
    elif mov == 'D':
        if y != 5:
            if matriz[x][y+1] != 'I':
                y += 1

    piso_s = matriz[x][y] # recebe o novo piso
    matriz[x][y] = 'S' # a matriz recebe a nova posicao de sam
    sam = [x,y]

    return matriz, sam, piso_s


# -------------

for i in range(6):
    m = input().split(' ')
    matriz.append(m)

for i in range(6):
    for j in range(6):
        if matriz[i][j] == 'S':
            sam = [ i , j ]
        
        if matriz[i][j] == 'N':
            neil = [ i , j ]

print('Sam: Mas que lugar é esse aqui?')
print('Dollman: WASD... Num exclusivo de PS5? Ah, fala sério!')
print()

uma_vez = True
while op:
    dist = chebyshev(sam, neil)
    mov = input()

    if mov in['W','A','S','D']:
        matriz, sam, piso_s = mover_sam(matriz, sam, piso_s, mov)
        if piso_s == 'F':
            hitsFogo += 1
            hp_sam -= 5
     
    elif mov in ['Rifle','Metralhadora','Espingarda']:
        arma_atual = mov
        print(f'Arma trocada para {arma_atual}.')
        
    else:
        dano = arsenal(arma_atual, dist)
        hp_neil -= dano
        if dns < 3 and dano > 0:
            dns += 1
            if dns == 3 and hp_neil > 0:
                dns = 0
                neil, matriz, piso_n = tp(sam, neil, matriz, piso_n)
                for linha in matriz:
                    print(*linha)

    # contabilizar as acoes de sam
    if acoes < 4:
        acoes += 1
        if acoes == 4 and hp_neil > 0:
            acoes = 0
            hp_sam -= 15
            danoNeil += 15
            print('>>> Você recebe um disparo de Neil! <<<')
            
    # verifica se a vida de sam chegou em <= 40 pela primeira vez
    if hp_sam<=40 and uma_vez:
        print('Dollman: A Fragile comeu todos os criptobiontes da DHV Magalhães... Se curar não é uma opção. Tome cuidado, Sam.')
        uma_vez = False

    # encerra o programa
    if hp_neil <= 0:
        op = False
     
        print()
        print('MISSÃO COMPLETA! - Investigue a Anomalia')
        print('========================================')
        likes = 1000 - (danoNeil*8) - (hitsFogo*10)
        print(f'Likes recebidos: 👍 {likes}')
     
    elif hp_sam <= 0:
        op = False
     
        print()
        print('MISSÃO FALHOU')
        print('==============')
        print('Sam foi derrotado.')
        print('[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]')
