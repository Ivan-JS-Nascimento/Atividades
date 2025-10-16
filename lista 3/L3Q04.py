n = int(input())
nome_artista = []
seguidores   = []

for i in range(n):
    
    recebendo_tudo = input()
    nosego = recebendo_tudo.split('-')

    nome_artista.append(nosego[0].strip())
    seguidores.append(int(nosego[1].strip()))

print('--- Simulador de Cancelamento ---')
print('')
for i in range(n):
    print(f'A subcelebridade da vez é: {nome_artista[i]}')
    acontecimento = int(input())

    if acontecimento == 1:
        print(f'{nome_artista[i]} perdeu 10% dos seguidores!')
        seguidores[i] -= (seguidores[i]/10)

    elif acontecimento == 2:
        print(f'{nome_artista[i]} ganhou 5% de seguidores!')
        seguidores[i] += (seguidores[i]/20) 

    elif acontecimento == 3:
        print(f'{nome_artista[i]} perdeu 15% dos seguidores!')
        seguidores[i] -= (seguidores[i]*15)/100 
    else:
        print('Nenhum evento relevante. Seguidores continuam os mesmos.')

print('')
print('--- RANKING FINAL DE SEGUIDORES ---')

gamb = [nome_artista , seguidores]
for i in range(n): # para cada valor em gamb
    for j in range(n-i-1): # varre tudo e organiza 
        if gamb[1][j+1] > gamb[1][j]: # se valor no index x for menor que valor em x+1  
            gamb[1][j+1], gamb[1][j] = gamb[1][j], gamb[1][j+1]# passa valor em x+1 para frente da lista
            gamb[0][j+1], gamb[0][j] = gamb[0][j], gamb[0][j+1]

for i in range(n if n<=3 else 3):
    if i < 3:
        print(f'{i+1}º Lugar: {gamb[0][i]} com {int(gamb[1][i])} seguidores.')
