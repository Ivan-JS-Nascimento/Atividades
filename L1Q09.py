print('Bem-vindos ao Jimmy Jab!')
p1 = input()
p2 = input()
p3 = input()
p4 = input()
per_b = ''
per_c = ''
if 'Terry' in [p1,p2,p3,p4] or 'Holt' in [p1,p2,p3,p4]:
    print('Jimmy Jab CANCELADO!')
else:
    print('Nosso primeiro evento é...')
    print('A Bocatona!')

    if 'Scully' in [p1,p2,p3,p4]:
        per_b=input()
        print('Scully leva a melhor, não tem como competir com ele.')
        print(f'{per_b} não avançou para a próxima fase!')
    else:
        ven_b=input()
        per_b=input()
        print(f'{ven_b} levou a melhor na Bocatona!')
        print(f'{per_b} não avançou para a próxima fase!')

    print('O segundo evento é A corrida volumosa!')
    t1=int(input())
    t2=int(input())
    t3=int(input())
    maior = t1 if (t1 > t2) and (t1 > t3) else t2 if (t2 > t3) else t3
    menor = t1 if (t1 < t2) and (t1 < t3) else t2 if (t2 < t3) else t3
    
    if p1==per_b:
    	ven_c = p2 if (t1==menor) else p3 if (t2==menor) else p4 
    	per_c = p2 if (t1==maior) else p3 if (t2==maior) else p4
    elif p2==per_b:
    	ven_c = p1 if (t1==menor) else p3 if (t2==menor) else p4
    	per_c = p1 if (t1==maior) else p3 if (t2==maior) else p4
    elif p3==per_b:
    	ven_c = p1 if (t1==menor) else p2 if (t2==menor) else p4
    	per_c = p1 if (t1==maior) else p2 if (t2==maior) else p4
    else:
    	ven_c = p1 if (t1==menor) else p2 if (t2==menor) else p3
    	per_c = p1 if (t1==maior) else p2 if (t2==maior) else p3
	print(f'{ven_c} levou a melhor na Corrida Volumosa!')
	print(f'')