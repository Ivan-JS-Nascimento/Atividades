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

print(f'Pontuação final: \nSheldon: {p_S} \nLeonard: {p_L} \nRaj: {p_R} \nHoward: {p_H}\n')
if (p_S > p_L) and (p_S > p_R) and (p_S > p_H):
    print(f'O cientista da semana é: Sheldon')