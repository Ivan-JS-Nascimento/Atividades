
def num_rep(doces, n):
    # condicoes de retorno de uma rota
    if doces == 0: # é uma combinacao possivel
        return 1

    elif doces < 0 or n > doces: # nao é uma combinacao possivel
        return 0
    # -----------------
    x = num_rep(doces-n, n) # rota linear
    y = num_rep(doces, n+1) # muda de rota para continuar procurando outras possibilidades

    return x + y

# ----------------------

doces = int(input())
quant_particao = num_rep(doces, 1)


# outputs

print('DOCES OU TRAVESSURAS???')
print(f'sem travessuras por hoje! tenho {quant_particao} sacolinhas pra vocês')

if quant_particao%2 == 0:
    print('doces equilibrados, sem travessuras!')
    
else:
    print('hmm... número ímpar de sacolinhas 🍭 cuidado com as bruxas!')