dic_divas = {
    1:{'nome_diva': 'Diva B', 'num_music': 15, 'media_str': 1},
    2:{'nome_diva': 'Diva A', 'num_music': 10, 'media_str': 1}, # P1: A
    3:{'nome_diva': 'Diva C', 'num_music': 20, 'media_str': 2}, # P1: C
    4:{'nome_diva': 'Diva Z', 'num_music': 5,  'media_str': 25}, # P1: B
    5:{'nome_diva': 'Diva X', 'num_music': 10, 'media_str': 2}, # P1: A (Empate com Diva A)
    6:{'nome_diva': 'Diva Y', 'num_music': 20, 'media_str': 7}, # P1: C (Empate com Diva C)
    7:{'nome_diva': 'Diva W', 'num_music': 18, 'media_str': 14}  # P1: C
}




def organizar(dic_divas):
    n = len(dic_divas)

    for i in range(1,n):
        for j in range(1,n-i+1):
            antes = dic_divas[j]
            depois= dic_divas[j+1]
            


            if antes['media_str'] < depois['media_str']:
                dic_divas[j], dic_divas[j+1] =  dic_divas[j+1],  dic_divas[j]

            elif antes['media_str'] == depois['media_str']:

                if antes['num_music'] < depois['num_music']:
                    dic_divas[j], dic_divas[j+1] =  dic_divas[j+1],  dic_divas[j]

                elif antes['num_music'] == depois['num_music']:

                    if antes['nome_diva'] > depois['nome_diva']:
                        dic_divas[j], dic_divas[j+1] =  dic_divas[j+1],  dic_divas[j]

    return
 
organizar(dic_divas)

for num in dic_divas:
    print(dic_divas[num])
