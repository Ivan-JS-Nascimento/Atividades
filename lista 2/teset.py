ponto_a=0
ponto_j=0

o=True
op=True
op1=True

t = True

print('Começa agora o treinamento para grande final mundial de cabo de guerra!')
 # ------------ repete ate que a partida seja impar
while(o==True):
    qnt_partidas=int(input())
    if( qnt_partidas%2 != 0 ):
        o=False
    else:
        print('Não deverá haver empates! O número de partidas deverá ser ímpar.')
# ---------------
forca_arthur=int(input())
forca_joao=int(input())

resi=int(input())

while(op):   # partidas 
    i = 1

    print(f'Eles batalharão em {qnt_partidas} longas partidas.')
    print(f'Começa a {i}ª partida!')
    print(f'Placar geral: {ponto_a} X {ponto_j}')

    resi_arthur=resi
    resi_joao=resi

    i += 1



