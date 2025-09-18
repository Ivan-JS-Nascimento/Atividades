a_Sheldon = int(input())
a_Leonard = int(input())
a_Raj = int(input())
a_Howard = int(input())

e_Sheldon = int(input())
e_Leonard = int(input())
e_Raj = int(input())
e_Howard = int(input())

p_S = a_Sheldon * 2 + e_Sheldon * 3
p_L = a_Leonard * 2 + e_Leonard * 3
p_R = a_Raj * 2 + e_Raj * 3
p_H = a_Howard * 2 + e_Howard * 3

sgg = 0
lgg = 0
rgg = 0
hgg = 0

print(f'Pontuação final: \nSheldon: {p_S} \nLeonard: {p_L} \nRaj: {p_R} \nHoward: {p_H}\n')
# S != L != R != H
if (p_H != p_R) and (p_H != p_L) and (p_H != p_S) and (p_R != p_L) and (p_R != p_S) and (p_L != p_S):
    # S > LRH
    if (p_S > p_L) and (p_S > p_R) and (p_S > p_H):
        sgg = 1

    # L > SRH
    if (p_L > p_S) and (p_L > p_R) and (p_L > p_H):
        lgg = 1

    # R > LSH
    if (p_R > p_S) and (p_R > p_L) and (p_R > p_H):
        rgg = 1

    # H > LRS
    if (p_H > p_S) and (p_H > p_L) and (p_H > p_R):
        hgg = 1

#------------------------------------------------------------------------------
else:
    # S = L = R = H
    if (p_S == p_L) and (p_L == p_R) and (p_R == p_H):
        sgg = 1
    else:
# casos de 3
        # S = L = R 
        if (p_S == p_L) and (p_L == p_R):
            if p_S > p_H:
                sgg = 1
            else:
                hgg = 1

        # S = L = H
        if (p_S == p_L) and (p_L == p_H):
            if p_S > p_R:
                sgg = 1
            else:
                rgg = 1

        # S = R = H
        if (p_S == p_R) and (p_R == p_H):
            if p_S > p_L:
                sgg = 1
            else:
                lgg = 1
        # L = R = H
        if (p_L == p_R) and (p_R == p_H):
            lgg = 1
# casos de 2
        # S = L
        if (p_S == p_L):
            if p_R!=p_H:
                if (p_S > p_R) and (p_S > p_H):
                    sgg = 1
                elif p_R > p_S and p_R > p_H:
                    rgg=1
                else:
                    hgg=1
            else:
                if p_S > p_R:
                    sgg=1
                else:
                    rgg=1
        # S = R
        if (p_S == p_R):
            if p_L!=p_H:
                if (p_S > p_L) and (p_S > p_H):
                    sgg = 1
                elif p_L > p_S and p_L > p_H:
                    lgg=1
                else:
                    hgg=1
            else:
                if p_S > p_L:
                    sgg=1
                else:
                    lgg=1
        # S = H
        if (p_S == p_H):
            if p_L!=p_R:
                if (p_S > p_L) and (p_S > p_R):
                    sgg = 1
                elif p_L > p_S and p_L > p_R:
                    lgg=1
                else:
                    rgg=1
            else:
                if p_S > p_L:
                    sgg=1
                else:
                    lgg=1

#-------------
        # L = R
        if (p_L == p_R) and (p_S!=p_H):
            if (p_L > p_S) and (p_L > p_H):
                lgg = 1
            elif p_H > p_S and p_H > p_L:
                hgg=1
            else:
                sgg=1
        # L = H
        if (p_L == p_H) and (p_S!=p_R):
            if (p_L > p_S) and (p_L > p_R):
                lgg = 1
            elif p_S > p_L and p_S > p_R:
                sgg=1
            else:
                rgg=1

        # R = H
        if (p_R == p_H) and (p_S!=p_L):
            if (p_R > p_S) and (p_R > p_L):
                rgg = 1
            elif p_S > p_L and p_S > p_R:
                sgg=1
            else:
                lgg=1
#Leonard → Raj → Howard.
# agora falta a logica para printar
print(str(sgg) + '. ' + str(lgg) + '. ' + str(rgg) + '. ' + str(hgg) + '. ')

if sgg==1:
    print(f'O cientista da semana é: Sheldon')
    print('Não é atoa que ele ganhou o prêmio Nobel')
elif lgg==1:
    print(f'O cientista da semana é: Leonard')
    print('A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.')
elif rgg==1:
    print(f'O cientista da semana é: Raj')
    print('Ele comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.')
else:
    print(f'O cientista da semana é: Howard')
    print('Um pequeno passo para a ciência, um grande salto para alguém com mestrado.')