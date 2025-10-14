grimorio_ajadão_supremo = ["Que tiro foi esse?","Segura a marimba","Tá com raiva? Morde as costas","Bateu de frente é só rajadão"]
n = int(input())
jafoi = []
for i in range(n):
    grimorio_ajadão_supremo.append(input())

for magia in grimorio_ajadão_supremo:
    quant = 0
    foija = ''
    for mag in grimorio_ajadão_supremo:
        if mag == magia:
            foija = mag
            quant += 1
    if magia not in jafoi:
        print(f'"{magia}": {quant}')

    if quant > 1 :
        jafoi.append(foija)

grimorio_ajadão_supremo.sort()
print(grimorio_ajadão_supremo)