
#-----fumcoes------
def mostrar_casas(catalogo, rc, casa_encontrada):
    score = 0

    for casa in catalogo:
        quartos = catalogo[casa]['quartos']
        quartos_min = rc[0]
        preco = catalogo[casa]['preco']
        preco_max = rc[1]

        if quartos >= quartos_min and preco <= preco_max:

            if casa_encontrada == []:
                score = score_compatibilidade(quartos)
                casa_encontrada = casa

            else:
                score2 = score_compatibilidade(quartos)
                if score2 > score:
                    score = score2
                    casa_encontrada = casa


    return casa_encontrada, score


def score_compatibilidade(quartos):
    return quartos * 10


def atendimento(catalogo, vendas):
    requisitos_cliente = {}
    nome = input()

    if nome == 'FIM':
        return vendas
    
    else:
        auxi = input().split('-')
        requisitos_cliente[nome] = (int(auxi[0]), int(auxi[1]))

    casa_encontrada, score = mostrar_casas(catalogo, requisitos_cliente[nome], [])

    if casa_encontrada == []:
        print(f'Puxa, {nome}, vou te avisar se algo aparecer. Não tenho nada com esses requisitos.')
        print()
    else:
        v = 0
        bairro = catalogo[casa_encontrada]['bairro']
        print(f'🎤 Bem-vindo ao House Tour de {bairro}, {nome}!')
        print(f'➡ Casa: {casa_encontrada}')
        print(f'💖 Score: {score} pontos')
        print()
        
        # reacao do cliente

        # Sabrina Carpenter
        if nome == 'Sabrina Carpenter':
            if score >= 40:
                v += 1
                print("\"Uau, Phil! Acho que finalmente encontrei o cenário perfeito para o clipe de House Tour!\"")
            else:
                print("\"Hmm... Sabe Phil, a letra não era tão literal assim…\"")

        # Taylor Swift
        elif nome == 'Taylor Swift':
            if score >= 40:
                v += 1
                print("\"Essa casa é perfeita para passar as férias na praia!\"")
            else:
                print("\"Nós nunca vamos comprar essa casa juntos, Phil!\"")

        # qualquer outro cliente
        else:
            if score >= 40:
                v += 1
                print(f"\"{nome} ficou encantado(a)! Phil comemora mais uma venda de sucesso!\"")
            else:
                print("\"Parece que a música não ajudou nas vendas dessa vez…\"")
        print()
        # -----------------

        # Mensagens de Resultado Final
        if v > 0:
            print('Venda concluída! Phil dança triunfante ao som de "House Tour"!')
            print()
        else:
            print('Talvez a Sabrina realmente não estivesse falando de imóveis…')
            print()

        vendas += v

    vendas = atendimento(catalogo, vendas)

    return vendas

#-----main-----

catalogo = {}

print('Phil, querido... Você tem certeza que essa música é literalmente sobre... casas?')
print('A própria Sabrina disse que nada na música é uma metáfora! Além disso, o sobrenome dela é carpinteira, acho que ela tem lugar de fala…')
print()

n = int(input())

for i in range(n):
    #casa = [ bairro - endereco - quartos-preco ]
    casa = input().split(' - ')
    casa[2] = casa[2].split('-')
    
#   catalogo[endereco]= ( bairro  ,  quartos   ,   preco    )
    catalogo[casa[1]] = {
        'bairro'  : casa[0], 
        'quartos' : int(casa[2][0]), 
        'preco'   : int(casa[2][1]) 
    }

print('Catálogo concluído! Quem será que irá comprar uma casa de Phil?')
print()

x = atendimento(catalogo, 0)

print('===== RELATÓRIO DE VENDAS =====')
print(f'Total de casas vendidas: {x}')

print('===============================')


