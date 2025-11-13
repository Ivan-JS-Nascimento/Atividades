def teste(n, ocupado, linha = 0, tabuleiro=[]):

    if tabuleiro == []:
        tabuleiro = [[0] * n for _ in range(n)]

        for i in range(n):
            tabuleiro[ocupado[0]][i] = -1
            tabuleiro[i][ocupado[1]] = -1

    if linha == n:
        return 1
    
    num  = 0

    for coluna in range(n):

        if tabuleiro[linha][coluna] == 0:
            valido = True

            for i in range(1, linha+ 1):
                if tabuleiro[linha - i][coluna] == 1:
                    valido = False
                    break

                if coluna -i >= 0 and tabuleiro[linha - 1][coluna - 1] == 1:
                    valido = False
                    break

                if coluna + i < n and tabuleiro[linha - 1][coluna + 1] == 1:
                    valido = False
                    break

            if valido:
                tabuleiro[linha][coluna] = 1
                num += teste(n, ocupado, linha+1, tabuleiro)
                tabuleiro[linha][coluna] = 0

    return num


n = 5
ocupado = [3, 2]
print(teste(n, ocupado))