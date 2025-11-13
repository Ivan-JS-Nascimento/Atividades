
def decifrar(alfabeto, chave, kripto, frase, very, index_atual):
    # kripto = mensagem criptografada modificave
    # mensagem_c = mensagem cri... original
    # very = sao as posicoes das armadilhas

    ci = alfabeto.index(chave)
    k = []
    mi = 0

    if kripto == []: # chegou na ultima letra da palavra criptografada
        return frase, very
    else:
        k = kripto[0]

        if k in alfabeto:
            ki = alfabeto.index(k)
            mi = 26 - ((ci - ki) % 26)
            if mi == 26: mi = 0

        else: # encontrou armadilhas
            very.append(str(index_atual))
            f, very = decifrar(alfabeto, chave, kripto[1:], frase, very, index_atual+1) # continua apos armazenar a armadilha
            return f, very

    c = alfabeto[mi]
    frase.append(c)
    f, very = decifrar(alfabeto, c, kripto[1:], frase, very, index_atual+1)
    frase = f
    
    return frase, very

# --------------------------------------------------------

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' ,'U', 'V' ,'W', 'X', 'Y' ,'Z']
aux = []
frase = []
chave_inicial = input()
frase_criptografada = input()
for i in frase_criptografada:
    aux.append(i)
frase_criptografada = aux

# ---------------------------------------------------------
print('Decifrando mensagem do Trickster...')

frase, very = decifrar(alfabeto, chave_inicial, frase_criptografada, [], [], 0)
if very != []:
    very = ", ".join(very)
    print(f'Esse Trickster é um picareta mesmo. Foram encontradas armadilhas nas posições: {very}')
else:   
    print('Nenhuma armadilha encontrada! Até que o Trickster foi bonzinho.')

print(f'Mensagem revelada: {"".join(frase)}')