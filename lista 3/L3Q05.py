
nome_projeto = input()

quantidade_componente = []
nome_componente = []
ponte = []

pronto = False
opp = True
op = True

# 1 Redstone
# 2 Repetidores
# 3 Tochas de Redstone
# 4 Lâmpadas de Redstone
# 5 Blocos de Notas
# 6 Observadores
# 7 Pistões Aderentes
# 8 Comparadores
# 9 Pistões
o1 = 0
o2 = 0
o3 = 0
o4 = 0
o5 = 0
o6 = 0
o7 = 0
o8 = 0
o9 = 0

# minimo de componetes
lista_f = []

esp = [] # os componentes do projeto

if nome_projeto == 'Memória ROM Simples':
    esp = ['Redstone','Repetidores','Tochas de Redstone']
    lista_f = [256, 64, 128]

elif nome_projeto == 'Calculadora de 4 bits':
    esp = ['Redstone','Repetidores','Tochas de Redstone','Lâmpadas de Redstone']
    lista_f = [512, 128, 64, 256]

elif nome_projeto == 'Sequenciador Musical':
    esp = ['Redstone','Repetidores','Blocos de Notas','Observadores']
    lista_f = [1024, 256, 64, 128]

elif nome_projeto == 'Processador de 8 Bits':
    esp = ['Redstone','Repetidores','Lâmpadas de Redstone','Pistões Aderentes']
    lista_f = [4096, 1024, 2048, 512]

elif nome_projeto == 'Display de Vídeo 8x8':
    esp = ['Redstone','Repetidores','Comparadores','Pistões']
    lista_f = [2048, 512, 256, 128]

elif nome_projeto == 'Supercomputador V13':
    esp = ['Redstone','Repetidores','Comparadores','Pistões Aderentes']
    lista_f = [8192, 2048, 1024, 1024]

while opp:
    
    while op :
        nome_quant = input() # nome e quantidades dos componentes juntos
        separacao = nome_quant.split(' ')
        
        for sep in separacao:
            # encerra 
            if sep == 'Construir!':
                op = False

            # aqui vai contecer tudo, ja que o numero e a ultima entrada para cada conponete
            elif sep.isnumeric():
                quantidade_componente.append(int(sep))
                nome_componente.append( " ".join(ponte)) # junta tudo em ponte para gerar o nome corretamente
                ponte = []

                ix = len(nome_componente) - 1  # ultimo nome add na lista
                h = nome_componente[ix]
                N = quantidade_componente[ix]

                # prints para cada projeto
                if nome_projeto == 'Memória ROM Simples':

                    if h == 'Redstone':
                        print(f'Mais redstone! A energia que move o progresso! (+{N} Redstone)')
                        o1 += N

                    elif h == 'Repetidores':
                        print(f'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{N} Repetidores)')
                        o2 += N

                    elif h == 'Tochas de Redstone':
                        print(f'Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{N} Tochas de Redstone)')
                        o3 += N

                    else:
                        print(f'Hmm, {h} não parece ser útil para este projeto.')

                    if o1 >= 256 and o2 >= 64 and o3 >= 128:
                        pronto = True

                elif nome_projeto == 'Calculadora de 4 bits':

                    if h == 'Redstone':
                        print(f'Mais redstone! A energia que move o progresso! (+{N} Redstone)')
                        o1 += N

                    elif h == 'Repetidores':
                        print(f'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{N} Repetidores)')
                        o2 += N

                    elif h == 'Tochas de Redstone':
                        print(f'Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{N} Tochas de Redstone)')
                        o3 += N

                    elif h == 'Lâmpadas de Redstone':
                        print(f'Lâmpadas para o display! O resultado vai ficar bem visível. (+{N} Lâmpadas de Redstone)')
                        o4 += N

                    else:
                        print(f'Hmm, {h} não parece ser útil para este projeto.')

                    if o1 >= 512 and o2 >= 128 and o3 >= 64 and o4 >= 256:
                        pronto = True

                elif nome_projeto == 'Sequenciador Musical':

                    if h == 'Redstone':
                        print(f'Mais redstone! A energia que move o progresso! (+{N} Redstone)')
                        o1 += N

                    elif h == 'Repetidores':
                        print(f'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{N} Repetidores)')
                        o2 += N

                    elif h == 'Blocos de Notas':
                        print(f'Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{N} Blocos de Notas)')
                        o5 += N

                    elif h == 'Observadores':
                        print(f'Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{N} Observadores)')
                        o6 += N

                    else:
                        print(f'Hmm, {h} não parece ser útil para este projeto.')

                    if o1 >= 1024 and o2 >= 256 and o5 >= 64 and o6 >= 128:
                        pronto = True


                elif nome_projeto == 'Processador de 8 Bits':

                    if h == 'Redstone':
                        print(f'Mais redstone! A energia que move o progresso! (+{N} Redstone)')
                        o1 += N

                    elif h == 'Repetidores':
                        print(f'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{N} Repetidores)')
                        o2 += N

                    elif h == 'Lâmpadas de Redstone':
                        print(f'Lâmpadas para o display! O resultado vai ficar bem visível. (+{N} Lâmpadas de Redstone)')
                        o4 += N
                    
                    elif h == 'Pistões Aderentes':
                        print(f'Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{N} Pistões Aderentes)')
                        o7 += N

                    else:
                        print(f'Hmm, {h} não parece ser útil para este projeto.')

                    if o1 >= 4096 and o2 >= 1024 and o4 >= 2048 and o7 >= 512:
                        pronto = True

                elif nome_projeto == 'Display de Vídeo 8x8':


                    if h == 'Redstone':
                        print(f'Mais redstone! A energia que move o progresso! (+{N} Redstone)')
                        o1 += N

                    elif h == 'Repetidores':
                        print(f'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{N} Repetidores)')
                        o2 += N

                    elif h == 'Comparadores':
                        print(f'Comparadores para a lógica! A precisão é a alma do negócio. (+{N} Comparadores)')
                        o8 += N

                    elif h == 'Pistões':
                        print(f'Pistões para mover as coisas de lugar. Isso vai ser útil! (+{N} Pistões)')
                        o9 += N

                    else:
                        print(f'Hmm, {h} não parece ser útil para este projeto.')

                    if o1 >= 2048 and o2 >= 512 and o8 >= 256 and o9 >=128:
                        pronto = True

                elif nome_projeto == 'Supercomputador V13':

                    if h == 'Redstone':
                        print(f'Mais redstone! A energia que move o progresso! (+{N} Redstone)')
                        o1 += N

                    elif h == 'Repetidores':
                        print(f'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{N} Repetidores)')
                        o2 += N

                    elif h == 'Comparadores':
                        print(f'Comparadores para a lógica! A precisão é a alma do negócio. (+{N} Comparadores)')
                        o8 += N

                    elif h == 'Pistões Aderentes':
                        print(f'Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{N} Pistões Aderentes)')
                        o7 += N
                        
                    else:
                        print(f'Hmm, {h} não parece ser útil para este projeto.')

                    if o1 >= 8192 and o2 >= 2048 and o8 >= 1024 and o7 >=1024:
                        pronto = True

                for u in nome_componente:  # caso componente se repita 
                    u_ix = nome_componente.index(u)
                    if u == nome_componente[ix] and ix > u_ix:
                        quantidade_componente[u_ix]+=N
                        nome_componente.pop()
                        quantidade_componente.pop()
                        ix -= 1
                # -----

            # guarda temporariamente ate juntar o nome completo
            else:
                ponte.append(sep)

    # ------------------------------------------

    if pronto: # caso os materias estejam ok
        opp = False
        print('')
        print(f'Viniccius13 conseguiu construir o {nome_projeto}! Partiu programar!')
        print('')
        print(f'Para construirmos a(o) {nome_projeto}, utilizamos:')
        print('')

        ip = [] # index dos intes que nao fazem parte

        for a in nome_componente:
            x = nome_componente.index(a)
            if a in esp:
                print(f'{a} : {quantidade_componente[x]}')
            else:
                ip.append(x) 

        if ip!=[]:
            print('')
            print('Mas, em nossa jornada, também coletamos:')
            print('')
            for p in ip:
                print(f'{nome_componente[p]} : {quantidade_componente[p]}')
    else:
        op = True
        print('')
        print(f'Ainda não é possível construir o {nome_projeto}! Faltam:')
        print('')

        w = 0
        for t in esp:
            if t in nome_componente:
                t_ix = nome_componente.index(t)
                if quantidade_componente[t_ix] < lista_f[w]: # se o que ele tem for maior ou igual ao que ele precisa
                    packs = int((lista_f[w] - quantidade_componente[t_ix]) / 64)
                    if packs == 0:
                        packs = 1
                    print(f'{packs} pack(s) de {nome_componente[t_ix]}')
            else:
                packs = int(lista_f[w] / 64)
                print(f'{packs} pack(s) de {t}')
            w += 1
        print('')
