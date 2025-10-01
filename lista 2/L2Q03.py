doce=int(input())
n_rodadas=int(doce/10 if (doce%10==0) else (doce/10)+1)
jg1=input()
jg2=input()
if (jg1!='Arthur' and jg2!='Arthur'):
    print('Epa!!! E cadê o dono dos doces??')
else:
    print('A batalha vai começar!')
    for i in range(n_rodadas):
        if (i ==0 and doce%10!=0):
            print(f'Pra aquecer, essa primeira vale menos, só {doce%10} doces!')
        else:
            print(f'Batalha número {i+1}!')        
        vida1=10
        vida2=10
        while( vida1 != 0 and vida2 != 0):
            jogadax=input()
            jogaday=input()
            if (jogadax!=jogaday):
                if(jogadax=='papel' and jogaday=='tesoura'):
                    vida1-=3 if vida1>=3 else vida1
                    vida2+=1
                elif(jogadax=='tesoura' and jogaday=='papel'):
                    vida2-=3 if vida2>=3 else vida2
                    vida1+=1

                elif(jogadax=='pedra' and jogaday=='papel'):
                    vida1-=2 if vida1>=2 else vida1
                    vida2+=2
                elif(jogadax=='papel' and jogaday=='pedra'):
                    vida2-=2 if vida2>=2 else vida2
                    vida1+=2

                elif(jogadax=='pedra' and jogaday=='tesoura'):
                    vida2-=4 if vida2>=4 else vida2
                elif(jogadax=='tesoura' and jogaday=='pedra'):
                    vida1-=4 if vida1>=4 else vida1

                print(f'Esse turno terminou com {jg1} tendo {vida1} de vida e {jg2} tendo {vida2}!')
            else:
                print('Eita, jogaram a mesma coisa dessa vez.')
        print(f'A rodada {i+1} vai para {jg1 if vida1!=0 else jg2}, que garante seus doces!')