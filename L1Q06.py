nome=input().capitalize()
valor=float(input())
res=input().capitalize()
teven=input().capitalize()

if valor > 100:
    # Regra Angela
    # R1
    if res == 'Angela' and teven!='Halloween' and teven!='Aniverário':
        print('Compra Aprovada!')
        print('Apenas eu tenho discernimento para gastos desta magnitude.')
    # R2
    else:
        print('Compra Reprovada!')
        print('Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!')
else:
    #R3
    if res =='Angela':
        print('Compra Aprovada!')
        print('Compra feita por mim, obviamente dentro dos padrões de excelência.')
    # ----

    # Regra Michael
    elif res == 'Michael' and teven != 'Halloween' and teven != 'Aniverário':
        # R1
        if nome =='Mágica' or nome == 'Fantasia':
            print('Compra Reprovada!')
            print('O Comitê não financia frivolidades e palhaçadas, Michael.')
        # R2
        elif valor > 60:
            print('Compra Aprovada com ressalvas!')
            if( teven == 'Natal' ):
                print('O espírito natalino de Michael é... excessivo. A nota será conferida.')
            if( teven == 'Aniversário' ):
                print('Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!')
        # R3
        else:
            print('Compra Aprovada!')
            print('Uma compra surpreendentemente sensata vinda do Michael. Suspeito.')
    # ----

    # Halloween
    elif teven == 'Halloween':
        # R1
        if nome == 'Abóbora' and valor<=30:
            print('Compra Aprovada!')

            # entra em R3 de Angela
            if res == 'Angela':
                print('Compra feita por mim, obviamente dentro dos padrões de excelência.')
            # ----

            # entra em R3 de Michael
            elif res == 'Michael':
                print('Uma compra surpreendentemente sensata vinda do Michael. Suspeito.')
            # ----

            print('Uma abóbora de tamanho e custo razoáveis. Eficiente.')
        
        # R2
        elif(nome=='Abóbora' and valor>30):
            # R3 de angela
            if res == 'Angela':
                print('Compra Aprovada!')
                print('Compra feita por mim, obviamente dentro dos padrões de excelência.')
            # R3 de michael
            elif res == 'Michael':
                print('Compra Aprovada!')
                print('Uma compra surpreendentemente sensata vinda do Michael. Suspeito.')
            # ---
            else:
                print('Compra Aprovada com ressalvas!')
            print('Por que uma abóbora precisa ser tão cara? Extravagância.')
        
        # R3
        else:   
            if valor > 100:
                if res == 'Angela':
                    print('Compra Reprovada!')
                    print('Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!')
                else:
                    print('Compra Aprovada com ressalvas!')
                    print('Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo.')
            else:
              print('Compra Reprovada!')
              if res != 'Michael' and nome != 'Fantasia' and nome != 'Mágica':
                print('Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!')
              else:
                print('O Comitê não financia frivolidades e palhaçadas, Michael.')
    # ----

    # Aniversário
    elif res == 'Aniversário':
        # R1
        if nome == 'Bolo' and valor<=40:
            print('Compra Aprovada!')
            if res == 'Angela':
                print('Compra feita por mim, obviamente dentro dos padrões de excelência.')
            elif res == 'Michael':
                print('Uma compra surpreendentemente sensata vinda do Michael. Suspeito.')
            print('Um bolo modesto para celebrar mais um ano de produtividade, parabéns!')

        # R2
        elif nome == 'Sorvete de Menta com Chocolate':
            print('Compra Reprovada!')
            print('Este sabor de sorvete é uma abominação e não entrará em meu evento.')
        
        # R3
        else:
            print('Compra Aprovada!')
            print('Itens de aniversário devem ser práticos, não uma distração do trabalho.')
        
    # ----
    else:
        if valor > 50:
            print('Compra Aprovada com ressalvas!')
            print('Está dentro do orçamento, mas não quer dizer que não vou verificar!')
        else:
            print('Compra Aprovada!')
            print('Esta compra não viola nenhum regulamento... por enquanto.')