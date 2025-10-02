b_andre=int(input())
b_bruno=int(input())
b_clara=int(input())
op=True
erro_a=0
erro_b=0
erro_c=0
while(op):
    a=True if(b_andre!=0) else False
    b=True if(b_bruno!=0) else False
    c=True if(b_clara!=0) else False
    for i in range(3 if(b_andre!=0 and b_bruno!=0 and b_clara!=0) else 2):
        resultado_rodada=input()
        if(a):
            if(resultado_rodada=='acertou'):
                b_andre+=2
                b_bruno-=1 if(b_bruno>=1) else 0
                b_clara-=1 if(b_clara>=1) else 0
            else:
                erro_a+=1
                if(erro_a==3):
                    b_andre=0
                    print(f'{b_andre} perdeu feio')
                    if(b_bruno==0 or b_clara==0):
                        i=10
                        op=False
            a=False
        elif(b):
            if(resultado_rodada=='acertou'):
                b_bruno+=2
                b_andre-=1 if(b_andre>=1) else 0
                b_clara-=1 if(b_clara>=1) else 0
            else:
                erro_b+=1
                if(erro_b==3):
                    b_bruno=0
                    print(f'{b_bruno} saiu do jogo')
                    if(b_andre==0 or b_clara==0):
                        i=10
                        op=False
            b=False
        elif(c):
            if(resultado_rodada=='acertou'):
                b_clara+=2
                b_bruno-=1 if(b_bruno>=1) else 0
                b_andre-=1 if(b_andre>=1) else 0
            else:
                erro_c+=1
                if(erro_c==3):
                    b_clara=0
                    print(f'{b_clara} saiu do jogo')
                    if(b_andre==0 or b_bruno==0):
                        i=10
                        op=False
            c=False
    if op==False:
        print('a quantidade final de bolas foi:')
        print(f'andre: {b_andre}')
        print(f'bruno: {b_bruno}')
        print(f'clara: {b_clara}')