
#-----fumcoes------



#-----main-----

catalogo = {}


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


print(catalogo)





