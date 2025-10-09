# bolas
b_andre=int(input())
b_bruno=int(input())
b_clara=int(input())

# --- controladores
# while principal
op=True
# caso de erros durante o jogo
erro_a=0
erro_b=0
erro_c=0
# abre e fecha cada turno
a=True
b=True
c=True
# isso é pra não printaar que alguem saiu duas vezes
g1=0;g2=0;g3=0
# ---
while(op):
    for i in range (3 if(b_andre!=0 and b_bruno!=0 and b_clara!=0) else 2):
        # andre
        if(a==True and b_andre!=0):
            resultado_rodada = input()
            if(resultado_rodada=='acertou'):
                b_andre+=2 if(b_bruno!=0 and b_clara!=0) else 1
                b_bruno-=1 if(b_bruno>=1) else 0
                b_clara-=1 if(b_clara>=1) else 0
                erro_a=0
            else:
                erro_a+=1
                if(erro_a==3):
                    print('andre perdeu feio')
                    if((b_bruno==0 or b_clara==0) or erro_b==3 or erro_c==3):
                        op=False
                        b=False
                        c=False
            a=False

        # bruno
        elif(b==True and b_bruno!=0):
            resultado_rodada = input()
            if(resultado_rodada=='acertou'):
                b_bruno+=2 if(b_andre!=0 and b_clara!=0) else 1
                b_andre-=1 if(b_andre>=1) else 0
                b_clara-=1 if(b_clara>=1) else 0
                erro_b=0
            else:
                erro_b+=1
                if(erro_b==3):
                    print('bruno perdeu feio')
                    if(b_andre==0 or b_clara==0 or erro_a==3 or erro_c==3):
                        op=False
                        c=False
            b=False

        # clara
        elif(c==True and b_clara!=0):
            resultado_rodada = input()
            if(resultado_rodada=='acertou'):
                b_clara+=2 if(b_andre!=0 and b_bruno!=0) else 1
                b_bruno-=1 if(b_bruno>=1) else 0
                b_andre-=1 if(b_andre>=1) else 0
                erro_c=0
            else:
                erro_c+=1
                if(erro_c==3):
                    print('clara perdeu feio')
                    if((b_andre==0 or b_bruno==0) or erro_a==3 or erro_b==3):
                        op=False
            c=False

        if((b_andre==0 and b_bruno==0) or (b_bruno==0 and b_clara==0) or (b_andre==0 and b_clara==0)):
            op=False
    else:
        if(b_andre==0 and erro_a<3 and g1==0):
            print('andre saiu do jogo')
            g1=1
        if(b_bruno==0 and erro_b<3 and g2==0):
            print('bruno saiu do jogo')
            g2=1
        if(b_clara==0 and erro_c<3 and g3==0):
            print('clara saiu do jogo')
            g3=1

    a=True if(b_andre!=0 and erro_a!=3) else False
    b=True if(b_bruno!=0 and erro_b!=3) else False
    c=True if(b_clara!=0 and erro_c!=3) else False
    
else:
    if(c==False and b==False):
        print('andre ganhou')
    elif(a==False and c==False):
        print('bruno ganhou')
    else:
        print('clara ganhou')

    print('a quantidade final de bolas foi:')
    print(f'andre: {b_andre}')
    print(f'bruno: {b_bruno}')
    print(f'clara: {b_clara}')