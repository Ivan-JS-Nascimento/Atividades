print('Vai começar o esconde-esconde UFPE 2025!')
nome1=input();p1=0
nome2=input();p2=0
nome3=input();p3=0
for i in range(3):
    print(f'\nProntos ou não, lá vai {nome1 if i==0 else nome2 if i==1 else nome3}.')
    for j in range(3):
        print(f"Agora {nome1 if i==0 else nome2 if i==1 else nome3} procurará no {'CFCH' if j==0 else 'CTG' if j==1 else 'CIN'}.")
        op=True
        while op:
            var=input()
            if var=='Achou uma pessoa!':
                print(f'{nome1 if i==0 else nome2 if i==1 else nome3} achou uma pessoa!')
                if i==0: p1+=1 
                elif i==1: p2+=1 
                else: p3+=1
            else:
                op=False
else:
    if p1==0 and p2==0 and p3==0:
        print('\nNinguém foi encontrado, nenhum dos buscadores ganhou a disputa.')
    else:
        print(f'\n{nome1 if p1>p2 and p1>p3 else nome2 if p2>p3 else nome3} é o(a) melhor no esconde-esconde da UFPE!')