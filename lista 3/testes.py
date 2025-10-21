seguidores = [64, 34, 25, 22, 12, 22, 11, 90]
nome_artista = ['a', 'b', 'c', 'd', 'e', 'x', 'f', 'g']


gamb = [nome_artista , seguidores]
print(gamb)
e = 8
for i in range(e): # para cada valor em gamb

    for j in range(e-i-1): # varre tudo e organiza
        if gamb[1][j+1] > gamb[1][j]: # se valor no index x for menor que valor em x+1  
            gamb[1][j+1], gamb[1][j] = gamb[1][j], gamb[1][j+1]# passa valor em x+1 para frente da lista
            gamb[0][j+1], gamb[0][j] = gamb[0][j], gamb[0][j+1]
            print(gamb)


print(gamb)


if h == 'Redstone':
    print(f'Mais redstone! A energia que move o progresso! (+{N} Redstone)')

elif h == 'Repetidores':
    print(f'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{N} Repetidores)')

elif h == 'Tochas de Redstone':
    print(f'Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{N} Tochas de Redstone)')

elif h == 'Lâmpadas de Redstone':
    print(f'Lâmpadas para o display! O resultado vai ficar bem visível. (+{N} Lâmpadas de Redstone)')

elif h == 'Blocos de Notas':
    print(f'Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{N} Blocos de Notas)')

elif h == 'Observadores':
    print(f'Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{N} Observadores)')

elif h == 'Comparadores':
    print(f'Comparadores para a lógica! A precisão é a alma do negócio. (+{N} Comparadores)')

elif h == 'Pistões':
    print(f'Pistões para mover as coisas de lugar. Isso vai ser útil! (+{N} Pistões)')

elif h == 'Pistões Aderentes':
    print(f'Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{N} Pistões Aderentes)')




nome_projeto = input()

quantidade_componente = []
nome_componente = []
ponte = []

op = True

while op :
    nome_quant = input() # nome e quantidades dos componentes juntos
    separacao = nome_quant.split(' ')

    # 1 Redstone
    # 2 Repetidores

    # 3 Tochas de Redstone
    # 4 Lâmpadas de Redstone
    # 5 Blocos de Notas
    # 6 Observadores
    # 7 Pistões Aderentes
    # 8 Comparadores
    # 9 Pistões

    o3 = False
    o4 = False
    o5 = False
    o6 = False
    o7 = False
    o8 = False
    o9 = False
    
    for sep in separacao:
        # encerra 
        if sep == 'Construir!':
            op = False

        # aqui vai contecer tudo, ja que o numero e a ultima entrada para cada conponete
        elif sep.isnumeric():
            quantidade_componente.append(int(sep))
            nome_componente.append( " ".join(ponte)) # junta tudo em ponte para gerar o nome corretamente
            ponte = [] 

            ix = len(nome_componente) # ultimo nome add na lista
            h = nome_componente[ix]
            N = quantidade_componente[ix]
            if nome_projeto == 'Memória ROM Simples':
                # Tochas de Redstone
                o3 = True

            elif nome_projeto == 'Calculadora de 4 bits':
                # Tochas de Redstone
                o3 = True
                # Lâmpadas de Redstone
                o4 = True

            elif nome_projeto == 'Sequenciador Musical':
                # Blocos de Notas
                o5 = True
                # Observadores
                o6 = True

            elif nome_projeto == 'Processador de 8 Bits':
                # Lâmpadas de Redstone
                o4 = True
                # Pistões Aderentes
                o7 = True


            elif nome_projeto == 'Display de Vídeo 8x8':
                # Comparadores
                o8 = True
                # Pistões
                o9 = True

            elif nome_projeto == 'Supercomputador V13':
                 # Comparadores
                 o8 = True
                 # Pistões Aderentes
                 o7 = True

            print(f'Mais redstone! A energia que move o progresso! (+{N} Redstone)')
            print(f'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{N} Repetidores)')

            if o3 :
                print(f'Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{N} Tochas de Redstone)')

            elif o4 :
                print(f'Lâmpadas para o display! O resultado vai ficar bem visível. (+{N} Lâmpadas de Redstone)')

            elif o5 :
                print(f'Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{N} Blocos de Notas)')

            elif o6 :
                print(f'Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{N} Observadores)')

            elif o7 :
                print(f'Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{N} Pistões Aderentes)')

            elif o8 :
                print(f'Comparadores para a lógica! A precisão é a alma do negócio. (+{N} Comparadores)')

            elif o9 :
                print(f'Pistões para mover as coisas de lugar. Isso vai ser útil! (+{N} Pistões)')

            # -----

        # guarda temporariamente ate juntar o nome completo
        else:
            ponte.append(sep)

print(nome_componente)
print(quantidade_componente)