nome=input().lower()
valor=float(input())
res=input().lower()
teven=input().lower()

if valor > 100:
    # Regra Angela
    # R1
    if res == 'angela' and teven!='halloween' and teven!='aniverário':
        print('Compra Aprovada!')
        print('Apenas eu tenho discernimento para gastos desta magnitude.')
    # R2
    else:
        print('Compra Reprovada!')
        print('Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!')
else:
    #R3
    if res =='angela':
        print('Compra Aprovada!')
        print('Compra feita por mim, obviamente dentro dos padrões de excelência.')
    # ----

    # Regra Michael
    elif res == 'michael' and teven != 'halloween' and teven != 'aniverário':
        # R1
        if nome =='mágica' or nome == 'fantasia':
            print('Compra Reprovada!')
            print('O Comitê não financia frivolidades e palhaçadas, Michael.')
        # R2
        elif valor > 60:
            print('Compra Aprovada com ressalvas!')
            if( teven == 'natal' ):
                print('O espírito natalino de Michael é... excessivo. A nota será conferida.')
            if( teven == 'aniversário' ):
                print('Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!')
        # R3
        else:
            print('Compra Aprovada!')
            print('Uma compra surpreendentemente sensata vinda do Michael. Suspeito.')
    # ----

    # Halloween
    elif teven == 'halloween':
        # R1
        if nome == 'abóbora' and valor<=30:
            print('Compra Aprovada!')

            # entra em R3 de Angela
            if res == 'angela':
                print('Compra feita por mim, obviamente dentro dos padrões de excelência.')
            # ----

            # entra em R3 de Michael
            elif res == 'michael':
                print('Uma compra surpreendentemente sensata vinda do Michael. Suspeito.')
            # ----

            print('Uma abóbora de tamanho e custo razoáveis. Eficiente.')
        
        # R2
        elif(nome=='abóbora' and valor>30):
            # R3 de angela
            if res == 'angela':
                print('Compra Aprovada!')
                print('Compra feita por mim, obviamente dentro dos padrões de excelência.')
            # R3 de michael
            elif res == 'michael':
                print('Compra Aprovada!')
                print('Uma compra surpreendentemente sensata vinda do Michael. Suspeito.')
            # ---
            else:
                print('Compra Aprovada com ressalvas!')
            print('Por que uma abóbora precisa ser tão cara? Extravagância.')
        
        # R3
        else:   
            if valor > 100:
                if res == 'angela':
                    print('Compra Reprovada!')
                    print('Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!')
                else:
                    print('Compra Aprovada com ressalvas!')
                    print('Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo.')
            else:
              print('Compra Reprovada!')
              if res != 'michael' and nome != 'fantasia' and nome != 'mágica':
                print('Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!')
              else:
                print('O Comitê não financia frivolidades e palhaçadas, Michael.')
    # ----

    # Aniversário
    elif teven == 'aniversário':
        # R1
        if nome == 'bolo' and valor<=40:
            print('Compra Aprovada!')
            if res == 'angela':
                print('Compra feita por mim, obviamente dentro dos padrões de excelência.')
            elif res == 'michael':
                print('Uma compra surpreendentemente sensata vinda do Michael. Suspeito.')
            print('Um bolo modesto para celebrar mais um ano de produtividade, parabéns!')

        # R2
        elif nome == 'sorvete de menta com chocolate':
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