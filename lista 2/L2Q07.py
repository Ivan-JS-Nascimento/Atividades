op=True

print('Começa agora o treinamento para grande final mundial de cabo de guerra!')
while(op):

    qnt_partidas=int(input())

    if(qnt_partidas%2 != 0):

        print(f'Eles batalharão em {qnt_partidas} longas partidas.')

        forca_arthur=int(input())
        forca_joao=int(input())

        resi=int(input())

        ponto_a=0
        ponto_j=0

        op1=True
        t = True  # tentativa tapear o for
        for i in range(qnt_partidas):  # partidas

            if(t):

                print(f'Começa a {i+1}ª partida!')
                print(f'Placar geral: {ponto_a} X {ponto_j}')


                resi_arthur=resi
                resi_joao=resi

                op2=True

                while(op2):   # rodadas
                    n = int(input())

                    very = (n**0.5)

                    primo = True
                    for i in range(2, n):
                        if( (n % i) == 0 ):
                            primo = False

                    if( (very**2) == n ):  # Vitória de Arthur
                        print('O número é um quadrado perfeito! Arthur consegue puxar mais forte.')
                        resi_arthur += 1
                        if( resi_joao >= 1 ):
                            resi_joao -= 1 
                        else:
                            op2 = False

                    elif(primo): # Vitória de João
                        print('O primo do primo é primo do primo? João puxa mais forte!')
                        resi_joao += 1
                        if( resi_arthur >= 1 ):
                            resi_arthur -= 1 
                        else:
                            op2 = False

                    else:  # Vitória por Força
                        if(forca_arthur>forca_joao):
                            print('Arthur é o mais forte! João não consegue segurar.')
                            resi_arthur += 1
                            if( resi_joao >= 1 ):
                                resi_joao -= 1 
                            else:
                                op2 = False
                        else:
                            print('João é o mais forte! Arthur não consegue segurar.')
                            resi_joao += 1
                            if( resi_arthur >= 1 ):
                                resi_arthur -= 1 
                            else:
                                op2 = False
                else:
                    if(resi_joao == 0):
                        print('Arthur dá orgulho para Maceió e ganha a partida!')
                        ponto_a += 1
                        if(ponto_a > ( qnt_partidas - 1 / 2 )):
                            t =False
                    else:
                        print('João usa seus talentos de mangueboy e leva essa para casa!')
                        ponto_j += 1
                        if(ponto_j > ( qnt_partidas - 1 / 2 )):
                            t =False
                
        else:
            print('')
            print('Agora eles estão prontos para o mundial!')
            print(F'Placar final: {ponto_a} X {ponto_j}')
            if( ponto_a > ponto_j):
                if( ponto_a != 0 and ponto_j != 0):
                   print(f'O ganhador foi Arthur com uma diferença de {ponto_a - ponto_j} partidas.')
                else:
                    print(f'João não teve chance! Arthur venceu todas as partidas.')
            else:
                if( ponto_a != 0 and ponto_j != 0):
                   print(f'O ganhador foi João com uma diferença de {ponto_j - ponto_a} partidas.')
                else:
                    print(f'Arthur não teve chance! João venceu todas as partidas.')

            


        op=False
    else:
        print('Não deverá haver empates! O número de partidas deverá ser ímpar.')