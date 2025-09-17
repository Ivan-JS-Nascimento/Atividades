print('Ativando a máquina...')
nome=input().capitalize()
ano=int(input())
n=len(nome)
if (ano % n) == 0:
    if nome == 'Frink':
        print('Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!')
    else:
        print(f'Previsão confiável! O rebigulador será real em {ano}!')
else:
    if nome == 'Frink':
        print('Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!')
    else:
        print(f'Previsão instável! {nome} também deve achar que o rebigulador é ridículo...')