matr1= []
det1 = 0
matr2= []
det2 = 0

print('Sejam bem-vindos à Big Sub Brasil, onde a fama é temporária, os barracos são eternos, e só um vai conquistar o título de maior subcelebridade do país!')

participantes = input().split(', ')


numeros_aleatórios_1 = input().split(' ')
numeros_aleatórios_1 = [int(x) for x in numeros_aleatórios_1]
numeros_aleatórios_2 = input().split(' ')
numeros_aleatórios_2 = [int(x) for x in numeros_aleatórios_2]


print(f'{participantes[0].capitalize()} e {participantes[1].capitalize()} disputarão entre si.')

min1 = sorted(numeros_aleatórios_1)[:3]
max1 = sorted(numeros_aleatórios_1, reverse=True)[:3]
matr1.append(sorted(max1))
matr1.append(sorted(min1))

for m in min1: # add min
    numeros_aleatórios_1.remove(m)
for a in max1: # add max
    numeros_aleatórios_1.remove(a)
l_add = []
for i in numeros_aleatórios_1[:3]: # add número consecutivo dos primeiros três números restantes 
    l_add.append(i+1)
matr1.append(sorted(l_add))

# determinante
a,b,c = matr1[0]
d,e,f = matr1[1]
g,h,i = matr1[2]

det1 = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

print(f'{a} {b} {c}')
print(f'{d} {e} {f}')   
print(f'{g} {h} {i}')
print(f'{participantes[0].capitalize()} está com pontuação {det1} pontos.')

min2 = sorted(numeros_aleatórios_2)[:3]
max2 = sorted(numeros_aleatórios_2, reverse=True)[:3]
matr2.append(sorted(max2))
matr2.append(sorted(min2))

for m in min2: # add min
    numeros_aleatórios_2.remove(m)
for a in max2: # add max
    numeros_aleatórios_2.remove(a)
l_add = []
for i in numeros_aleatórios_2[:3]: # add número consecutivo dos primeiros três números restantes
    l_add.append(i+1)
matr2.append(sorted(l_add))

# determinante
a,b,c = matr2[0]
d,e,f = matr2[1]
g,h,i = matr2[2]

det2 =a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

print(f'{a} {b} {c}')
print(f'{d} {e} {f}')
print(f'{g} {h} {i}')
print(f'{participantes[1].capitalize()} está com pontuação {det2} pontos.')

if det1 != det2:
    if det1>det2:
        print(f'Com talento duvidoso e esforço máximo, a vitória é de {participantes[0].capitalize()}!')
    else:
        print(f'Com talento duvidoso e esforço máximo, a vitória é de {participantes[1].capitalize()}!')
else:
    print('RODADA DESEMPATE!!')
    
    if numeros_aleatórios_1[-1] == numeros_aleatórios_2[-1]:# se o que sobrou for igual
        print('Como isso é possível?? Os participantes empataram até na rodada desempate! EU DESISTO!!!')
    else:
        if numeros_aleatórios_1[-1]>numeros_aleatórios_2[-1]:
            print(f'Contra todas as expectativas (inclusive as nossas), {participantes[0].capitalize()} venceu a rodada!')
            print(f'Seu momento de brilhar virou eclipse {participantes[1].capitalize()}. Melhor sorte no próximo flop!')
            print(f'Com talento duvidoso e esforço máximo, a vitória é de {participantes[0].capitalize()}!')
        else:
            print(f'Contra todas as expectativas (inclusive as nossas), {participantes[1].capitalize()} venceu a rodada!')
            print(f'Seu momento de brilhar virou eclipse {participantes[0].capitalize()}. Melhor sorte no próximo flop!')
            print(f'Com talento duvidoso e esforço máximo, a vitória é de {participantes[1].capitalize()}!')