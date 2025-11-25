

exigencias = {}
op = True

while op:
    auxi = input()

    if auxi != 'MIMOS RECEBIDOS':
        # fase 1
        auxi = auxi.split(': ')
        if auxi[0] == 'Bebidas' and auxi[1] == "latte":
            auxi2 = int(auxi[2]) +1
            auxi[2] = auxi2

        exigencias[auxi[0]] = (auxi[1], auxi[2])

    else:
        op = False

# fase 2
op = True
while op:
    quantidade = 0
    categoria = ''
    item = ''

    chegaram = input()

    if chegaram != "ACABOU, a Glinda está pronta!":
        chegaram = chegaram.split()
        quantidade = int(chegaram[1])
        categoria = chegaram[5]
        item = chegaram[7][:-1]
        
    else:
        ...
