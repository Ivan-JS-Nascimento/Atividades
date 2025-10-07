op=True

print('Começa agora o treinamento para grande final mundial de cabo de guerra!')
while(op):
    qnt_partidas=int(input())

    if(qnt_partidas%2!=0):
        print(f'Eles batalharão em {qnt_partidas} longas partidas.')

        
        forca_arthur=int(input())
        forca_joao=int(input())
        resi=int(input())
        resi_arthur=resi
        resi_joao=resi
        op1=True
        for i in range(qnt_partidas):
            n=int(input())



        op=False
    else:
        print('Não deverá haver empates! O número de partidas deverá ser ímpar.')