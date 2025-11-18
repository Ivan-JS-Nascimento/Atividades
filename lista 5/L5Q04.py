def posi_alma(n, cemiterio, linha):
    num = 0
    if linha == n: # caso chegue na ultima linha(ala) do cemiterio
        return 1 
    
    for coluna in range(n):
        
        if cemiterio[linha][coluna] == '0':
            valido = True

            for i in range(1,linha+1): # for utilizado para procurar em linhas anteriores
                # verifica se nessa coluna ja tem uma alma
                if cemiterio[linha-i][coluna] == '1':
                    valido = False
                
                # verifica a existencia de almas nas diagonais
                if coluna-i >= 0 and (cemiterio[linha-i][coluna-i] == '1'):
                    valido = False

                if coluna+i < n and (cemiterio[linha-i][coluna+i] == '1'):
                    valido = False

            # caso nao tenha conflitos
            if valido:
                cemiterio[linha][coluna] = '1' # coloca uma alma nessa posicao
                num += posi_alma(n, cemiterio, linha+1) # continua procurando a partir da proxima linha
                cemiterio[linha][coluna] = '0'
        
    return num

# -------------------------
op = True
# número de almas e de alas e lotes do cemitério.
n = int(input())

while op:
    ala_ocupada = int(input())
    lote_ocupado = int(input())

    if lote_ocupado <= n and  ala_ocupada <= n and lote_ocupado > 0 and ala_ocupada > 0:
        op = False
    else:
        print(f'Rogério e Chaguinha não encontraram o túmulo ocupado na posição ({ala_ocupada}, {lote_ocupado}). Assim eles nunca vão conseguir sair do cemitério!')

print(f'Rogério e Chaguinha conseguiram encontrar o túmulo ocupado em ({ala_ocupada}, {lote_ocupado})!')
print()

selo= [ala_ocupada, lote_ocupado]

cemiterio = [['0'] * n for _ in range(n)]
cemiterio[selo[0]-1][selo[1]-1] = 'X'

num = posi_alma(n, cemiterio, 0)

print(f'Rogério e Chaguinha conseguiram encontrar {num} possíveis posições para as almas se posicionarem sem conflitos!')

if num == 0:
    print('Não existe nenhuma configuração segura para as almas... Rogério e Chaguinha estão presos no meio da guerra das almas!')

elif num <= 10:
    print('Os amigos vão precisar tomar muito cuidado para não pegar um caminho errado!')

elif num <= 50:
    print('Uau! São tantas opções que eles até se perderam contando!')

else:
    print('Em pleno Halloween e as almas descansando em paz! Rogério e Chaguinha vão conseguir sair logo do cemitério.')
