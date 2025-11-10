# nao consegui achar uma maneira pratica de debugar
# eu uso o termux com vim no celular para escrever as atividades
# esse prints com #? é o que eu uso para tentar achar os erros
# se tiverem alguma dica de como fazer isso de um jeito melhor pelo celular, manda no feedback 👍
# Códigos de escape ANSI para cores
c = {
    'cy': '\033[96m',
    'fim': '\033[0m'
}


op = True

# makoto
hp = 300
mana = 70

# ----funcoes----

# Função de Combate
def combate(hp, mana, p, s):
    op = True
    makoto = [p, hp, mana]  # [persona, hp, mana]
    n = len(s)
    golpes_usados = [2, 1]  # [yukari , junpei]
    num_t = 0
    print(c['cy'])
    print(f'makoto: {makoto}')#?
    print(f'sombras: {s}')#?
    print(f'ajudas: {golpes_usados}')#?
    print(c['fim'])

    while op:
        sombras_ativas = False
        print(c['cy'])
        print('while combate ++++++++++++')#?
        print(c['fim'])

        for i in range(n):
            estado = s[i][4]
            print(c['cy'])
            print(f'estado:{estado}')#?
            print(c['fim'])
            if not sombras_ativas and estado == 'a':
                sombras_ativas = True

        if sombras_ativas and makoto[1] > 0:
            makoto, s, golpes_usados, num_t = turno(makoto, s, golpes_usados, num_t)
        else:
            op = False

    return makoto[1] , makoto[2]

# Funções de turno, tanto do Makoto quanto para a Sombra
def turno(makoto, s, g_u, u):
    op = True
    tm = True
    n = len(s) - 1
    index = 0
    i = 0

    while op:
        dano = 0
        print(c['cy'])
        print('while turno +++++++++++++++++')#?
        print(c['fim'])

        op1 = True
        sombra_apanha = ''
        e = 0
        for j in s:
            if j[4] == 'a' and op1:
                op1 = False
                index = e
                sombra_apanha = j
            e += 1
        print(c['cy'])
        print(f'sombra_apanha: {sombra_apanha}')#?
        print(f'index: {index}')#?
        print(f'tm: {tm}')#?
        print(c['fim'])
        sombra_vez = s[i]
        print(c['cy'])
        print(f'sombra_vez: {sombra_vez}')#?
        print(c['fim'])

        if tm:  # turno makoto
            nocaute = False
            print('Makoto: O que fazer...')
            mov = input()
            print(c['cy'])
            print(f'mov: {mov}')#?
            print(f'g_u: {g_u}')#?
            print(c['fim'])

            if mov == 'yukari':
                if g_u[0] > 0:
                    print('Yukari: Aguenta ai, líder!')
                    print('Mitsuru: Bom trabalho, Yukari! Makoto se sente mais revigorado')
                    makoto[1] = min(makoto[1] + 100, 300)
                    g_u[0] -= 1
                else:
                    print('Yukari: Estou exausta, foi mal!')

            elif mov == 'junpei':
                if g_u[1] > 0:
                    print('Junpei: HOOOOOME RUUUUN!!')
                    print(f'Mitsuru: Acerto CRÍTICO de Junpei! {sombra_apanha[0]} sofreu 100 de dano!')
                    dano = 100
                    nocaute = True
                    g_u[1] -= 1
                else:
                    print('Junpei: Cara, tô cansado!')

            elif mov == 'atacar':
                dano = cal_dano('2', makoto[0][1])
                print(f'Mitsuru: Makoto acertou {sombra_apanha[0]} causando {dano} de dano!')

            elif mov == 'persona':
                if makoto[2] >= makoto[0][3]:
                    makoto[2] -= makoto[0][3]

                    l = input().split(' ')
                    lista = [int(w) for w in l]
                    x = bubblesort(lista)

                    if x != 0:
                        dano = cal_dano(makoto[0][2], makoto[0][1])
                        if x == 2:
                            nocaute = True
                            dano = int(dano * 1.5)

                    # outputs
                    if nocaute:
                        print(f'Makoto: Venha {makoto[0][0]}!')
                        print(f'Mitsuru: Makoto acertou {sombra_apanha[0]} causando {dano} de dano!')
                    elif dano != 0:
                        print('Makoto: Persona!')
                        print(f'Mitsuru: Makoto acertou {sombra_apanha[0]} causando {dano} de dano!')
                    else:
                        print('Makoto: O quê?!')
                        print('Mitsuru: Mais foco, Makoto!')

                else:
                    print('Makoto: Estou cansado...')

            tm = False
            sombra_apanha[1] -= dano
            print(c['cy'])
            print(f'sombra_apanha: {sombra_apanha}')#?
            print(f'dano: {dano}')#?
            print(c['fim'])
            if sombra_apanha[1] <= 0:
                sombra_apanha[1] = 0
                sombra_apanha[4] = 'm'
                print(f'Mitsuru: {sombra_apanha[0]} foi derrotada!')
            elif nocaute:
                sombra_apanha[4] = 'd'
                s[index] = sombra_apanha
                v = veri_sombras(s)
                if v == 2:
                    print('MAIS UM!')
                    print('Mitsuru: Você acertou uma fraqueza! Continue no ataque!')
                    u += 1
                    print(f'TURNO {u}:')
                    print(f'HP Makoto: {makoto[1]} / 300')
                    for d in s:
                        if d[4] != 'm':
                            print(f'HP {d[0]}: {d[1]} pontos de vida restantes')
                elif v == 1:
                    op = False
                    print('Mitsuru: Todos os inimigos cairam! Avancem com tudo!')
                    print('MASS DESTRUCTION!')
            s[index] = sombra_apanha

            if nocaute:
                tm = True

        else:  # turno sombra
            print(c['cy'])
            print('e a vez da sombra')#?
            print(f'{sombra_vez}')#?
            print(c['fim'])
            if sombra_vez[4] == 'a':
                dano = cal_dano(sombra_vez[3], sombra_vez[2])
                makoto[1] -= dano
                print(f'Mitsuru: Makoto foi atacado por {sombra_vez[0]} e recebeu {dano} de dano!')
                tm = True
                u += 1
                if makoto[1]>0:
                    print(f'TURNO {u}:')
                    print(f'HP Makoto: {makoto[1]} / 300')
                    for d in s:
                        if d[4] != 'm':
                            print(f'HP {d[0]}: {d[1]} pontos de vida restantes')

            elif sombra_vez[4] == 'd':
                sombra_vez[4] = 'a'
                tm = True
                u += 1
                print(f'TURNO {u}:')
                print(f'HP Makoto: {makoto[1]} / 300')
                for d in s:
                    if d[4] != 'm':
                        print(f'HP {d[0]}: {d[1]} pontos de vida restantes')
            print(c['cy'])
            print(f'hp: {makoto[1]}')#?
            print(f'dano: {dano}')#?
            print(c['fim'])
            i += 1
        print(c['cy'])
        print(f'i: {i}')#?
        print(f'n: {n}')#?
        print(f'verificacao: {veri_sombras(s)}')#?
        print(f'maoto hp: {makoto[1]}')#?
        print(c['fim'])
        if i > n or veri_sombras(s)==0 or makoto[1]<=0:
            op = False

    return makoto, s, g_u, u


# Cálculo de dano
def cal_dano(golpe, atk):
    poder_base = 0

    if golpe in ['Zio', 'Garu', 'Agi', 'Bufu']:
        poder_base = 3

    elif golpe in ['Corte', 'Perfuração', 'Pancada']:
        poder_base = 4

    elif golpe in ['Zionga', 'Garula', 'Agilao', 'Bufula']:
        poder_base = 5

    else:
        poder_base = 2

    dano = int(((poder_base * 15) ** 0.5) * (atk / 2))
    print(c['cy'])
    print('calculando dano+++++++++++++++++++')#?
    print(f'poder_base: {poder_base}')#?
    print(f'atk: {atk}')#?
    print(f'dano: {dano}')#?
    print('-----+')#?
    print(c['fim'])
    return dano


# Função para Bubblesort
def bubblesort(lista):
    x = 0  # 0 == errou ,1 == acerto, 2 == acerto critico
    n = len(lista)
    l_crescente = lista.copy()
    l_decrecente = lista.copy()

    cres = 0
    decres = 0

    for i in range(n - 1):
        for j in range(n - i - 1):
            if l_crescente[j] > l_crescente[j + 1]:
                l_crescente[j], l_crescente[j + 1] = l_crescente[j + 1], l_crescente[j]
                cres += 1

            if l_decrecente[j] < l_decrecente[j + 1]:
                l_decrecente[j], l_decrecente[j + 1] = l_decrecente[j + 1], l_decrecente[j]
                decres += 1

    if cres == 0 or decres == 0:
        x = 2
    else:
        n_alter = min(cres, decres)
        if n_alter <= 5:
            x = 1
    print(c['cy'])
    print('bubblesort +++++++++++++++')#?
    print(f'lista: {lista}')#?
    print(f'l_crescente: {l_crescente}')#?
    print(f'cres: {cres}')
    print(f'l_decrecente: {l_decrecente}')#?
    print(f'decres: {decres}')
    print('-------')#?
    print(c['fim'])
    return x

def veri_sombras(s):
    n = len(s)
    avera = -1 # 
    a = 0
    m = 0
    d = 0

    for x in s:
        if x[4] == 'a':
            a += 1
        elif x[4] == 'm':
            m += 1
        elif x[4] == 'd':
            d += 1

    if m == n:# todo mundo morreu
        avera = 0
        
    elif a > 0:# tem pelo menos 1 ativo
        avera = 2
        
    else:# todo mundo(ou quase todo mundo, pq o resto ta morto) esta derrubado 
        avera = 1


    return avera

# ---------------
print('Mitsuru: Vamos iniciar nossa exploração, tomem cuidado.')
andar_explo = 0

while op:  # cada loop do while é um andar
    persona = []
    sombras = []

    per = input().split(' - ')
    for item in per:
        if item.isdigit():
            persona.append(int(item))
        else:
            persona.append(item)

    print(f'{persona[0]}: Eu sou tu e tu és eu...')

    n_sombras = int(input())
    for i in range(n_sombras):
        somb = input().split(' - ')
        somb.append('a')
        s = []
        for item in somb:
            if item.isdigit():
                s.append(int(item))
            else:
                s.append(item)
        sombras.append(s)
    print('Mitsuru: Inimigos detectados, se preparem!')
    print(c['cy'])
    print(f'hp: {hp}')#?
    print(f'mana: {mana}')#?
    print(c['fim'])
    hp, mana = combate(hp, mana, persona, sombras)
    print(c['cy'])
    print(f'hp: {hp}')#?
    print(f'mana: {mana}')#?
    print(c['fim'])


    if hp > 0:
        print('Mitsuru: Muito bem! Continuem a exploração.')
        hp = (hp + 50) if (hp <= 250) else 300
        mana = (mana + 15) if (mana <= 55) else 70
    else:
        print('Makoto: Argh...')
        print('Mitsuru: Líder? Aconteceu algo? Responda!')
        print()
        print('FIM DE JOGO')
        print(f'Andares explorados: {andar_explo}')
        op = False
    andar_explo += 1
