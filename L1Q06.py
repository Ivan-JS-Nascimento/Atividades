nome = input().lower()
valor = float(input())
res = input().lower()
teven = input().lower()

# Regra de ouro
if valor > 100:
    if res == 'angela':
        print('Compra Aprovada!')
        print('Apenas eu tenho discernimento para gastos desta magnitude.')
    else:
        print('Compra Reprovada!')
        print('Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!')
    exit()

# Regra Angela
if res == 'angela':
    print('Compra Aprovada!')
    print('Compra feita por mim, obviamente dentro dos padrões de excelência.')
    exit()

# Regra Michael
if res == 'michael':
    if nome in ['mágica', 'magica', 'fantasia']:
        print('Compra Reprovada!')
        print('O Comitê não financia frivolidades e palhaçadas, Michael.')
        exit()
    if valor > 60:
        print('Compra Aprovada com ressalvas!')
        if teven == 'natal':
            print('O espírito natalino de Michael é... excessivo. A nota será conferida.')
        elif teven == 'aniversário':
            print('Michael nunca gastou tanto nos aniversários dos funcionários, deve ser o dele!')
        exit()
    print('Compra Aprovada!')
    print('Uma compra surpreendentemente sensata vinda do Michael. Suspeito.')
    exit()

# Halloween
if teven == 'halloween':
    if nome == 'abóbora':
        if valor <= 30:
            print('Compra Aprovada!')
            print('Uma abóbora de tamanho e preços personalizados. Eficiente.')
        else:
            print('Compra Aprovada com ressalvas!')
            print('Por que uma abóbora precisa ser tão cara? Extravagância.')
    else:
        print('Compra Aprovada com ressalvas!')
        print('Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo.')
    exit()

# Aniversário
if teven == 'aniversário':
    if nome == 'bolo' and valor <= 40:
        print('Compra Aprovada!')
        print('Um bolo modesto para comemorar mais um ano de produtividade, parabéns!')
    elif nome == 'sorvete de menta com chocolate':
        print('Compra Reprovada!')
        print('Este sabor de sorvete é uma abominação e não entrará no meu evento.')
    else:
        print('Compra Aprovada!')
        print('Itens de aniversário devem ser práticos, não uma distração do trabalho.')
    exit()

# Regra geral
if valor > 50:
    print('Compra Aprovada com ressalvas!')
    print('Está dentro do orçamento, mas não quer dizer que não vou verificar!')
else:
    print('Compra Aprovada!')
    print('Esta compra não viola nenhum regulamento... por enquanto.')