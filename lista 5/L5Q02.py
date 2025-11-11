def num_rep(doces, n):
    if doces == 0:
        return 1

    elif doces < 0 or n > doces:
        return 0

    x = num_rep(doces-n, n) 
    y = num_rep(doces, n+1)

    return x + y

doces = int(input())
quant_particao = num_rep(doces, 1)


print('DOCES OU TRAVESSURAS???')
print(f'sem travessuras por hoje! tenho {quant_particao} sacolinhas pra vocês')

if quant_particao%2 == 0:
    print('doces equilibrados, sem travessuras!')
    
else:
    print('hmm... número ímpar de sacolinhas 🍭 cuidado com as bruxas!')