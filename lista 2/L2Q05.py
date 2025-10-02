b_andre=int(input())
b_bruno=int(input())
b_clara=int(input())
op=True
erro_a=0
erro_b=0
erro_c=0
a=True
b=True
c=True
gambiarra=''
while(op):
    for i in range(3 if(b_andre!=0 and b_bruno!=0 and b_clara!=0) else 2):
        resultado_rodada = input() if(gambiarra=='') else gambiarra
        gambiarra=''
        if(a==True and b_andre!=0):
            if(resultado_rodada=='acertou'):
                b_andre+=2 if(b_bruno!=0 and b_clara!=0) else 1
                b_bruno-=1 if(b_bruno>=1) else 0
                b_clara-=1 if(b_clara>=1) else 0
                erro_a=0
            else:
                erro_a+=1
                if(erro_a==3):
                    b_andre=0
                    print('andre perdeu feio')
                    if(b_bruno==0 or b_clara==0):
                        i=10
                        op=False
            a=False
        elif(b==True and b_bruno!=0):
            if(resultado_rodada=='acertou'):
                b_bruno+=2 if(b_andre!=0 and b_clara!=0) else 1
                b_andre-=1 if(b_andre>=1) else 0
                b_clara-=1 if(b_clara>=1) else 0
                erro_b=0
            else:
                erro_b+=1
                if(erro_b==3):
                    b_bruno=0
                    print('bruno perdeu feio')
                    if(b_andre==0 or b_clara==0):
                        i=10
                        op=False
            b=False
        elif(c==True and b_clara!=0):
            if(resultado_rodada=='acertou'):
                b_clara+=2 if(b_andre!=0 and b_bruno!=0) else 1
                b_bruno-=1 if(b_bruno>=1) else 0
                b_andre-=1 if(b_andre>=1) else 0
                erro_c=0
            else:
                erro_c+=1
                if(erro_c==3):
                    b_clara=0
                    print('clara perdeu feio')
                    if(b_andre==0 or b_bruno==0):
                        i=10
                        op=False
            c=False
        else:
            gambiarra=resultado_rodada

        if((b_andre==0 and b_bruno==0) or (b_bruno==0 and b_clara==0) or (b_andre==0 and b_clara==0)):
            op=False
            i=718
    else:
        if(b_andre==0 and erro_a<3 and a!=False):
            print('andre saiu do jogo')
        elif(b_bruno==0 and erro_b<3 and b!=False):
            print('bruno saiu do jogo')
        elif(b_clara==0 and erro_c<3 and c!=False):
            print('clara saiu do jogo')
    a=True if(b_andre!=0) else False
    b=True if(b_bruno!=0) else False
    c=True if(b_clara!=0) else False
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