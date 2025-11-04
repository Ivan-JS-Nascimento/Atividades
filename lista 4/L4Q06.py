op = True

# makoto
hp = 300
mana = 70

# ----funcoes----

# Função de Combate
def combate(hp, mana, p, s):
    op = True
    n = len(s)

    while op:
        sombras_ativas = False
        
        for i in range(n):
            hp_s = s[i][1]
            if hp_s>0:
                sombras_ativas = True

# Funções de turno, tanto do Makoto quanto para a Sombra

# Cálculo de dano

# Função para Bubblesort

# ---------------

print('Mitsuru: Vamos iniciar nossa exploração, tomem cuidado.')
while op: # cada volta do while é um andar
    persona = []
    Sombras = []

    per = input().split(' - ')
    # converte o que for digito para int
    for item in per:
        if item.isdigit():
            persona.append(int(item))
        else:
            persona.append(item)
    
    print(f'{persona[0]}: Eu sou tu e tu és eu...')

    n_sombras = int(input())
    # recebe todas as sombras
    for i in range(n_sombras):
        somb = input().split(' - ')
        s = []
        # converte digito para int
        for item in somb:
            if item.isdigit():
                s.append(int(item))
            else:
                s.append(item)
        sombras.append(s)


    combate(hp, mana, persona, sombras)


