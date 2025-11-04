op = True

# makoto
hp = 300
mana = 70

# ----funcoes----

# Função de Combate
def combate(hp, mana, p, s):
    op = True
    makoto = [p, hp, mana]
    n = len(s)
    s_luta = 0 # sombra que ira lutar
    golpes_usados = [2 , 1]# [yukari , junpei]

    while op:
        sombras_ativas = False
        
        for i in range(n):
            nocaute = s[i][5]

            if not sombras_ativas and nocaute == 'a':
                sombras_ativas = True
                s_luta = i


        if sombras_ativas:
            if hp > 0:
                makoto, s[s_luta], golpes_usados = turno(makoto, s[s_luta], golpes_usados)
        else:
            op = False



# Funções de turno, tanto do Makoto quanto para a Sombra
def turno(makoto, sombra, g_u):
    
    for i in range(2):

        if i==0:# makoto
            mov = input()

            if mov == 'Yukari':
                if g_u[0] > 0:
                    makoto[1] = makoto[1] + 100 if( makoto[1]<=200)else 300
                    g_u[0] -= 1
            elif mov == 'Junpei':
                if g_u[1] > 0:
                    sombra[1] -= 100
                    sombra[5] = 'd' if( alejado and sombra[1]>0 )else 'm'
                    g_u[1] -= 1
            else:
                if mov == 'Persona':
                    makoto[2] -= makoto[0][3]

                dano, alejado = cal_dano(mov, makoto[0])
                sombra[1] -= dano
                sombra[5] = 'd' if( alejado and sombra[1]>0 )else 'm' if( sombra[1]<=0 )else 'a'
        else:# sombra
            if sombra[5] == 'a':
                dano = cal_dano(sombra)
                makoto[1] -= dano

    return makoto, sombra, g_u

# Cálculo de dano
def cal_dano(mov = '', persona = [], sombra = []):
# atk_usuario: inteiro que representa a força do usuário.
# poder_base: inteiro que representa o poder base do golpe utilizado.
    poder_base = 0
    if persona == []:
        if persona[2] in ['Zio', 'Garu', 'Agi', 'Bufu']:
            poder_base = 3

        elif persona[2] in ['Corte', 'Perfuração', 'Pancada']:
            poder_base = 4

        elif persona[2] in ['Zionga', 'Garula', 'Agilao', 'Bufula']:
            poder_base = 5

    else:
        if sombra[3] in ['Zio', 'Garu', 'Agi', 'Bufu']:
            poder_base = 3

        elif sombra[3] in ['Corte', 'Perfuração', 'Pancada']:
            poder_base = 4

        elif sombra[3] in ['Zionga', 'Garula', 'Agilao', 'Bufula']:
            poder_base = 5

    atk_usuario = persona[1] if( persona != [])else sombra[2]

    dano = 0
    alejado = False

    if mov == 'Persona':
        lista = input().split(' ')
        x = bubblesort(lista)

        if x != 0:
            if x == 2:
                alejado = True

            dano = int(((poder_base * 15) ** 0.5) * (atk_usuario / 2))

        return dano, alejado
    
    elif mov == 'Atacar':
        # nesse caso o atk é o da persona
        dano = int((( 2 * 15) ** 0.5) * (atk_usuario / 2))

        return dano, alejado

    else: # else para a sombra
        dano = int((( poder_base * 15) ** 0.5) * (atk_usuario / 2))

        return dano
    
    
# Função para Bubblesort
def bubblesort(lista):
    x = 0 # 0 == errou ,1 == acerto, 2 == acerto critico
    n = len(lista)
    l_crescente = lista
    l_decrecente = lista

    cres = 0 # contadoir de crescente
    decres = 0 # contador de trocas decrescente

    for i in range(n-1):
        for j in range(n-i-1):
            if l_crescente[j] > l_crescente[j+1]:
                l_crescente[j], l_crescente[j+1] = l_crescente[j+1], l_crescente[j]
                cres += 1
            
            if l_decrecente[j] < l_decrecente[j+1]:
                l_decrecente[j], l_decrecente[j+1] = l_decrecente[j+1], l_decrecente[j]
                decres += 1

    if cres == 0 or decres == 0:
        x = 2
    else:
        n_alter = min(cres, decres)
        if n_alter <= 5:
            x = 1

    return x
# ---------------

print('Mitsuru: Vamos iniciar nossa exploração, tomem cuidado.')
while op: # cada volta do while é um andar
    persona = []
    sombras = []

    per = input().split(' - ')
    # converte o que for digito para int
    for item in per:
        if item.isdigit():
            persona.append(int(item))
        else:
            persona.append(item)
    
    print(f'{persona[0]}: Eu sou tu e tu és eu...')

    n_sombras = int(input())
    # recebe todas as sombras
    for i in range(n_sombras):
        somb = input().split(' - ')
        somb.append('a') # adicionei o estado de cada sombras, sendo eles a(ativo), d(derrubado), m(morto)
        s = []
        # converte digito para int
        for item in somb:
            if item.isdigit():
                s.append(int(item))
            else:
                s.append(item)
        sombras.append(s)


    combate(hp, mana, persona, sombras)

    if hp > 0:
        hp = (hp + 50) if(hp <= 250)else 300
        mana = (mana + 15) if( mana <= 55)else 70
    else:
        op = False

