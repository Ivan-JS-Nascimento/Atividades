# numero tentativas
n = int(input())
c_an=0
c_ad=0
c_j=0
c_d=0
for i in range(4):
    jogador = 'Ana' if(i==0)else 'Adrieli' if(i==1)else 'Joab' if(i==2)else 'Duda'
    casa_final = 0
    for i in range(n):
        p = int(input())
        casa_final = p if(i==0)else p if(p>casa_final)else casa_final
    else:
        print(f'{jogador} tentou {n} vezes e completou a última casa {casa_final}')
        if(casa_final==5):
            print(f'{jogador} completou a amarelinha!')
            if(jogador=='Ana'):c_an=1
            if(jogador=='Adrieli'):c_ad=1
            if(jogador=='Joab'):c_j=1
            if(jogador=='Duda'):c_d=1
        else:
            print(f'{jogador} não conseguiu completar a amarelinha!')
else:
    c=c_d+c_j+c_ad+c_an
    if(c==1):
        print(f"O vencedor é {'Ana' if(c_an==1)else 'Adrieli' if(c_ad==1)else 'Joab' if(c_j==1)else 'Duda'}!")
    elif(c==2):
        if(c_an==1 and c_ad==1):
            print(f'Houve empate entre: Ana, Adrieli')
        elif(c_an==1 and c_j==1):
            print(f'Houve empate entre: Ana, Joab')
        elif(c_an==1 and c_d==1):
            print(f'Houve empate entre: Ana, Duda')
        elif(c_ad==1 and c_j==1):
            print(f'Houve empate entre: Adrieli, Joab')
        elif(c_ad==1 and c_d==1):
            print(f'Houve empate entre: Adrieli, Duda')
        else:
            print(f'Houve empate entre: Joab, Duda')
    elif(c==3):
        if(c_an==1 and c_ad==1 and c_j==1):
            print('Houve empate entre: Ana, Adrieli, Joab')
        elif(c_an==1 and c_ad==1 and c_d==1):
            print('Houve empate entre: Ana, Adrieli, Duda')
        elif(c_an==1 and c_j==1 and c_d==1):
            print('Houve empate entre: Ana, Joab, Duda')
        else:
            print('Houve empate entre: Adrieli, Joab, Duda')
    elif(c==4):
        print('Houve empate entre: Ana, Adrieli, Joab, Duda')
