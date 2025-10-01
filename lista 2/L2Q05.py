b_andre=int(input())
b_bruno=int(input())
b_clara=int(input())
op=True
while(op):
    l = 3 if(b_andre!=0 and b_bruno!=0 and b_clara!=0) else 2
    for i in range(l):
        a=True if(b_andre!=0) else False
        b=True if(b_bruno!=0) else False
        c=True if(b_clara!=0) else False
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
        if(b):
            if(resultado_rodada=='acertou'):
                b_bruno+=2
                b_andre-=1 if(b_andre>=1) else 0
                b_clara-=1 if(b_clara>=1) else 0
            else:
                erro_b+=1
                if(erro_b==3):
                    b_bruno=0
        if(c):
            if(resultado_rodada=='acertou'):
                b_clara+=2
                b_bruno-=1 if(b_bruno>=1) else 0
                b_andre-=1 if(b_andre>=1) else 0
            else:
                erro_c+=1
                if(erro_c==3):
                    b_clara=0