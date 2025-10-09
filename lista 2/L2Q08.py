front=6
front_morto=0
back=6
back_morto=0

op1=True

while(op1):
    time_atacante=input()
    if(time_atacante=='Front-End' or time_atacante=='Back-End'):
        op1=False

op2=True

while(op2):
    resultado_ataque=input()
    if(resultado_ataque=='acertou' or resultado_ataque=='errou'):
        op2=False

if(resultado_ataque=='acertou'):
    