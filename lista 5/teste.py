def teste(n, ocupado, linha = 0, tabuleiro=[]):
    print(f' n: {n} , linha: {linha}')
    print(f' tabuleiro ')

    if tabuleiro == []:
        tabuleiro = [[80] * n for _ in range(n)]
        tabuleiro[ocupado[0]][ocupado[1]] = 77
       
    for i in range(n):
        print(tabuleiro[i])

    if linha == n:
        return 1
    
    num  = 0

    for coluna in range(n):
        print('---------------')
        print(f'coluna: {coluna}')
        if tabuleiro[linha][coluna] == 80:
            valido = True

            for i in range(1, linha+ 1):
                print(f' for interno i: {i}')
                if tabuleiro[linha - i][coluna] == 11:
                    print('case 1')
                    valido = False
                    break

                if coluna - i >= 0 and tabuleiro[linha - i][coluna - i] == 11:
                    print('caso 2')
                    valido = False
                    break

                if coluna + i < n and tabuleiro[linha - i][coluna + i] == 11:
                    print('caso 3')
                    valido = False
                    break

            if valido:
                tabuleiro[linha][coluna] = 11
                num += teste(n, ocupado, linha+1, tabuleiro)
                tabuleiro[linha][coluna] = 80

    return num

n = 5
ocupado = [2, 1]
print(teste(n, ocupado))
