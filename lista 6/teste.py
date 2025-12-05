dicionario = {
    0:{'nome_diva': 'Diva B', 'num_music': 15, 'media_str': 1},
    1:{'nome_diva': 'Diva A', 'num_music': 10, 'media_str': 1}, # P1: A
    2:{'nome_diva': 'Diva C', 'num_music': 20, 'media_str': 2}, # P1: C
    3:{'nome_diva': 'Diva Z', 'num_music': 5,  'media_str': 25}, # P1: B
    4:{'nome_diva': 'Diva X', 'num_music': 10, 'media_str': 2}, # P1: A (Empate com Diva A)
    5:{'nome_diva': 'Diva Y', 'num_music': 20, 'media_str': 7}, # P1: C (Empate com Diva C)
    6:{'nome_diva': 'Diva W', 'num_music': 18, 'media_str': 14}  # P1: C
}




def soorted(dicionario, valor_1, valor_2, valor_3):

    n = len(dicionario)

    for i in range(n-1):
        for j in range(n-i-1):
            antes = dicionario[j]
            depois= dicionario[j+1]
            

            if antes[valor_1] < depois[valor_1]:
                dicionario[j], dicionario[j+1] =  dicionario[j+1],  dicionario[j]

            elif antes[valor_1] == depois[valor_1]:

                if antes[valor_2] < depois[valor_2]:
                    dicionario[j], dicionario[j+1] =  dicionario[j+1],  dicionario[j]

                elif antes[valor_2] == depois[valor_2]:

                    if antes[valor_3] > depois[valor_3]:
                        dicionario[j], dicionario[j+1] =  dicionario[j+1],  dicionario[j]

    return
 
soorted(dicionario, 'media_str', 'num_music', 'nome_diva')

for num in dicionario:
    print(dicionario[num])
