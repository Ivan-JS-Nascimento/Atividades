def ogr_raking(competidoras):
    raking = {}

    i = 0
    for chave in competidoras:
        raking[i] = chave
        i += 1

    n = len(raking)

    for i in range(n-1):
        for j in range(n-i-1):
            if competidoras[raking[j]][4] < competidoras[raking[j+1]][4]:
                raking[j], raking[j+1] = raking[j+1], raking[j]

    return raking


competidoras = {
    'Ivete Sangalo'  : ('Brasil' , 3 , 89 , 200, 54),
    'Azealia Banks' : ('EUA' , 0 , 40 , 1, 12),
    'Anitta' : ('Brasil' , 0 , 88 , 100, 32),
    'Taylor Swift' : ('EUA' , 14 , 98 , 2, 6),
    'Luisa Sonza' : ('Brasil' , 1 , 84 , 148, 10)
}

raking = ogr_raking(competidoras)

print(raking)