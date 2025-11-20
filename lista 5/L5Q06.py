# funcoes ----
def anagrama(num):
    return sorted(num) == sorted([1,9,8,7])
# main--------

energia  = 100

d_bonnie = 0
d_chica  = 0
d_freddy = 0
d_foxy   = 0

niveis_dificuldade = input().split(' ')
caso_espe = ''.join(niveis_dificuldade)
print(type(caso_espe))
print(type(niveis_dificuldade))

aux = []
op = True
for a in niveis_dificuldade:
    aux.append(int(a))
for a in aux:
    if a < 0 or a > 20:
        op = False

niveis_dificuldade = aux


if len(niveis_dificuldade) == 4 and op:
    bo = niveis_dificuldade[0]
    ch = niveis_dificuldade[1]
    fr = niveis_dificuldade[2]
    fo = niveis_dificuldade[3]
    
    print(anagrama([bo,ch,fr,fo]))
else:
    ...
