
exigencias = {}
op = True

# fase 1
while op:

    auxi = input()

    if auxi != 'MIMOS RECEBIDOS':

        # auxi = [ 0 - categoria , 1 - item , 2 - quantidade ]
        auxi = auxi.split(': ')

        # se for uma bebida lattet tem que adicionas +1 na quantidade
        if auxi[0] == 'Bebidas' and auxi[1] == "latte":
            auxi[2] = int(auxi[2]) + 1
            
        else:
            auxi[2] = int(auxi[2])
        
        # exigencias = { chave = categoria : valor = tupla( item , quantidade , quant_chegaram) }
        exigencias[auxi[0]] = (auxi[1], auxi[2], 0)

    else:
        op = False


# fase 2
op = True
while op:
    quantidade = 0
    categoria = ''
    item = ''

    # entrada ex:. Chegaram {quantidade} itens da categoria {categoria} (Item: {item_principal})
    chegaram = input()

    if chegaram != "ACABOU, a Glinda está pronta!":

        chegaram = chegaram.split(' ')

        quantidade = int(chegaram[1])
        categoria = chegaram[5]
        item = chegaram[7][:-1]
        
        valor = exigencias.get(categoria, 'nao existe')

        if valor != 'nao existe':
            quant_anterior = valor[1]
            quant_chegaram = valor[2]

            exigencias.update( {categoria : ( item , quant_anterior-quantidade , quant_chegaram+quantidade) } )

    else:
        op = False


#------------- relatorio -------------
print('Relatório de Balanço Final:')
quant_catego_negativas = 0
for key in exigencias:
    frase = 'Você entregou TUDO! O mimo tá mais que garantido.' if( exigencias[key][1] <= 0 )else f'Golpe BAIXÍSSIMO! Faltam {exigencias[key][1]} mimos. Corre!'

    if frase != 'Você entregou TUDO! O mimo tá mais que garantido.':
        quant_catego_negativas += 1


    print(f'Categoria: {key} Item: {exigencias[key][0]} Status: {frase}')
print()


# ------------- Checagens específicas -------------
make = exigencias.get('Maquiagem','ne') 
if make != 'ne' and make[0] == 'Gloss':
    if make[1]<=0:
        print('TUDO! O Gloss tá on. O look de Glinda tá salvo!')
    else:
        print('CADÊ meu gloss? Como divarei? ... A Glinda tá chorando de raiva!')

bebida = exigencias.get('Bebidas','ne')
if bebida != 'ne' and bebida[0] == 'latte':
    if bebida[1]<=0:
        print('Latte gelado pronto! A voz de Glinda está salva. Pode vir o próximo take')
    else:
        print('Cadeia neles! Faltou o Mimo Sagrado. Essa equipe tá perdida!')



# ------------- Veredito da Diva -------------
print()
print('Veredito Final')

if quant_catego_negativas >= 3:
    print('Thank U, Next! A equipe de camarim foi demitida!')
else:
    print('Estoque Aprovado! Glinda vai brilhar em Wicked!')
