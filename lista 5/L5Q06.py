# funcoes ----

def custo_acao(acao):
    custo = 1 # gasto base por hora
    if acao[0] == 's': custo += 7
    if acao[1] == 's': custo += 7
    if acao[2] == 's': custo += 5
    if acao[3] == 's': custo += 9
    #print()
    #print('>calculando acao')
    #print(f' custo { custo }')
    #print()
    return custo

def custo_fruatrado(e, nome, ataques, tronic, taxa):
    ix = tronic.index(nome)
    #print()
    #print('>calculando custo:')
    #print(f' e {e}')
    #print(f' ataques[ix] { ataques[ix] }')
    #print(f' taxa { taxa }')
    #print(e + ( ataques[ix] * taxa ))
    #print()
    return e + ( ataques[ix] * taxa )

def escolha(energia, ataques, tronic, acao, acao_custo_min, custo):
    #print()
    #print(' ESCOLHA ---')
    #print()
    #print(f' energia {energia}')
    #print(f' ataques {ataques}')
    #print(f' tronic  {tronic}')
    #print(f' acao    {acao}')
    #print(f' acao_custo_min {acao_custo_min}')
    #print(f' custo   {custo}')
    #print()
    # acao [ pe, pd, lz, cam ]

    if acao!=[]:
        c = 0
        if 'bo' in tronic:
            if acao[0]=='s' or (acao[2]=='s' and acao[3]=='n'):
                c += custo_fruatrado(3,'bo',ataques,tronic,0.25)
            else:
                return acao_custo_min, custo
        
        if 'ch' in tronic:
            if acao[1]=='s' or acao[3]=='s':
                c += custo_fruatrado(2,'ch',ataques,tronic,0.35)
            else:
                return acao_custo_min, custo
        
        if 'fo' in tronic:
            if acao[0]=='s':
                c += custo_fruatrado(5,'fo',ataques,tronic,0.15)
            else:
                return acao_custo_min, custo
        
        if 'fr' in tronic:
            if acao[3]=='s' or (acao[0]=='s' and acao[1]=='s'):
                c += custo_fruatrado(3,'fr',ataques,tronic,0.35)
            else:
                return acao_custo_min, custo
        
        if 'gf' in tronic:
            if acao[3]=='s':
                c += custo_fruatrado(10,'gf',ataques,tronic,1.95)
            else:
                return acao_custo_min, custo

        # calculos
        
        c += custo_acao(acao)

        if energia-c > 0:
            if custo != 0:
                if custo > c:
                    acao_custo_min = acao.copy()
                    custo = c
                    return acao_custo_min, custo
                else: 
                    return acao_custo_min, custo
            else:
                acao_custo_min = acao.copy()
                custo = c
                return acao_custo_min, custo
        else:
            return acao_custo_min, custo
        

    
    for pe in ['s','n']:
        for pd in ['s','n']:
            for lz in ['s','n']:
                for cam in ['s','n']:
                    acao = [pe, pd, lz, cam]
                    acao_custo_min, custo = escolha(energia, ataques, tronic, acao, acao_custo_min, custo)

    return acao_custo_min, custo


def jogar(vida, energia, hora, d_bo, d_ch, d_fo, d_fr, d_gf, escolhas):
    #print()
    #print(' ------------ JOGAR --------------')
    #print()
    ataques = []
    tronic  = []

    # verificar hora
    if hora == 6:
        return escolhas, energia
    # verificar vida
    if not vida:
        return
    # verifucar energia
    if energia<=0:
        return
    # ataques
    # > Bonnir
    if d_bo>0 and (hora==0 or hora==3):
        ataques.append(d_bo)
        tronic.append('bo')
    # > Chica
    if d_ch>0 and (hora==1 or hora==4):
        ataques.append(d_ch)
        tronic.append('ch')
    # > Foxy
    if d_fo>0 and hora==4 and energia>50:
        ataques.append(d_fo)
        tronic.append('fo')
    # > Freddy
    if d_fr>0 and hora==5:
        ataques.append(d_fr)
        tronic.append('fr')
    # > Golden Freddy
    if d_gf>0 and hora==5:
        ataques.append(d_gf)
        tronic.append('gf')

    # escolha
    acao, custo = escolha(energia, ataques, tronic, [] , [], 0)
    #print()
    #print(f'acao {acao}')
    #print(f'custo {custo}')
    if acao!=[]:
        escolhas.append(acao)
        energia -= custo
        escolhas, energia = jogar(vida, energia, hora+1, d_bo, d_ch, d_fo, d_fr, d_gf, escolhas)
    else: # ele morreu, nao tinha possibilidades
        return escolhas, energia

    return escolhas, energia


def anagrama(num):
    special = False
    anag = False

    auxi1 = []
    for i in num:
        auxi1.append(str(i))
    auxi1 = ''.join(auxi1)
    auxi1 = list(auxi1)
    auxi2 = auxi1.copy()
    for a in auxi2:
        if a == '0':
            auxi1.remove(a)
            special = True


    if len(auxi1) == 4 and special:
        anag = ''.join(sorted(auxi1)) == ''.join(sorted('1987'))
    else:
        anag = sorted(num) == sorted([1,9,8,7])

    return anag, special

# main--------

energia  = 100
escolhas = []

d_bo = 0
d_ch = 0
d_fr = 0
d_fo = 0
d_gf = 0

# > recebe as dificuldades e converte para int
niveis_dificuldade = input().split(' ')

aux = []
op = True
for nd in niveis_dificuldade:
    aux.append(int(nd))
for a in aux:
    if a < 0 or a > 20:
        op = False

niveis_dificuldade = aux

# > entrada valida
if len(niveis_dificuldade) == 4 and op:
    d_bo = niveis_dificuldade[0]
    d_ch = niveis_dificuldade[1]
    d_fr = niveis_dificuldade[2]
    d_fo = niveis_dificuldade[3]
    

    if d_bo == 0 and d_ch == 0 and d_fr == 0 and d_fo == 0:
        print('"Uh, olá? Olá? Phone Guy falando. Não tem ninguém aqui..."')
        
    else:
        op = True
        anag, special = anagrama([d_bo,d_ch,d_fr,d_fo])
        
        if anag and not special:
            d_gf = d_fr
            escolhas, energia = jogar(True, energia, 0, d_bo, d_ch, d_fo, d_fr, d_gf, [])
            
        elif anag and special:
            print(""" "IT'S ME" """)
            op = False
        else:
            escolhas, energia = jogar(True, energia, 0, d_bo, d_ch, d_fo, d_fr, d_gf, [])
            

        if op:
            if len(escolhas) < 6: # nao sobrevivel
                print('"Uh, Phone Guy falando. Uh, não tem mais ninguém do outro lado, não é?"')
            else:
                print(f'"Uh, olá? Ei, wow, dia sete, parabéns. E ainda com {energia:.2f}% de energia. Eu sabia que você conseguiria."')
                for i in range(6):
                    print(f"0{i}:00 AM -> PE: {'SIM' if (escolhas[i][0] == 's')else 'NÃO'} | PD: {'SIM' if(escolhas[i][1] == 's')else 'NÃO'} | LZ: {'SIM' if(escolhas[i][2] == 's')else 'NÃO'} | CAM: {'SIM' if(escolhas[i][3] == 's')else 'NÃO'}")


# entrada invalida
else:
    print('"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."')

