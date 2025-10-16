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