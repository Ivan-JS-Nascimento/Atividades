def posi_alma(n, i, j, ocupada):

    if i == n:
        if j == n:
            return
        else:
            posi_alma(n, i, j, ocupada)
    else:
        if i == ocupada[0]: 
            return
        if j == ocupada[1]:
            return
        else:
            posi_alma(n, i+1, j, ocupada)

    return num

# -------------------------
op1 = True
op2 = True
# número de almas e de alas e lotes do cemitério.
n = int(input())

while op1:
#  index da ala que contém o túmulo ocupado
    ala_ocupada = int(input())
    if ala_ocupada <= n:
        op1 = False

while op2:
# index do lote que contém o túmulo ocupado
    lote_ocupado = int(input())
    if lote_ocupado <= n:
        op2 = False

ocupada = [ala_ocupada, lote_ocupado]

matrix = []
for i in range(n):
    for j in range(n):
        if i == ala_ocupada and j == lote_ocupado:
            matrix[i][j] = "X"
        else:
            matrix[i][j] = "0"