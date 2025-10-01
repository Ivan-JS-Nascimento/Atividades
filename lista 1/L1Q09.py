print('Bem-vindos ao Jimmy Jab!')
p1 = input()
p2 = input()
p3 = input()
p4 = input()

per_b = ''
per_c = ''
finali1 = ''
finali2 = ''

if (p1=='Terry' or p2=='Terry' or p3=='Terry' or p4=='Terry') or (p1=='Holt' or p2=='Holt' or p3=='Holt' or p4=='Holt'):
    print('Jimmy Jab CANCELADO!')
else:
    print('Nosso primeiro evento é...')
    print('A Bocatona!')

    if p1=='Scully' or p2=='Scully' or p3=='Scully' or p4=='Scully':
        per_b = input()
        print('Scully leva a melhor, não tem como competir com ele.')
        print(f'{per_b} não avançou para a próxima fase!')
    else:
        ven_b = input()
        per_b = input()
        print(f'{ven_b} levou a melhor na Bocatona!')
        print(f'{per_b} não avançou para a próxima fase!')

    print('O segundo evento é A corrida volumosa!')
    t1 = int(input())
    t2 = int(input())
    t3 = int(input())

    maior = t1 if (t1 > t2) and (t1 > t3) else t2 if (t2 > t3) else t3
    menor = t1 if (t1 < t2) and (t1 < t3) else t2 if (t2 < t3) else t3

    if p1 == per_b:
        finali1 = p2 if (t1 == menor) else p3 if (t2 == menor) else p4
        per_c = p2 if (t1 == maior) else p3 if (t2 == maior) else p4
    elif p2 == per_b:
        finali1 = p1 if (t1 == menor) else p3 if (t2 == menor) else p4
        per_c = p1 if (t1 == maior) else p3 if (t2 == maior) else p4
    elif p3 == per_b:
        finali1 = p1 if (t1 == menor) else p2 if (t2 == menor) else p4
        per_c = p1 if (t1 == maior) else p2 if (t2 == maior) else p4
    else:
        finali1 = p1 if (t1 == menor) else p2 if (t2 == menor) else p3
        per_c = p1 if (t1 == maior) else p2 if (t2 == maior) else p3

    finali2 = p1 if (finali1 != p1 and per_c != p1 and per_b != p1) else p2 if (finali1 != p2 and per_c != p2 and per_b != p2) else p3 if (finali1 != p3 and per_c != p3 and per_b != p3) else p4

    print(f'{finali1} levou a melhor na Corrida Volumosa!')
    print(f'{per_c} não avançou para a próxima fase!')

    if (finali1=='Jake' or finali1=='Amy') and (finali2=='Jake' or finali2=='Amy'):
        print('Jake ficou com o 2º lugar!')
        print('Amy VENCEU O JIMMY JABS!')
    else:
        vencedor = input()
        if finali1 == vencedor:
            print(f'{finali2} ficou com o 2º lugar!')
            print(f'{finali1} VENCEU O JIMMY JABS!')
        else:
            print(f'{finali1} ficou com o 2º lugar!')
            print(f'{finali2} VENCEU O JIMMY JABS!')