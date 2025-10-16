
nome_projeto = input()

quantidade_componente = []
nome_componente = []
ponte = []

op = True

while op :
    nome_quant = input()
    separacao = nome_quant.split(' ')

    for sep in separacao:
        # encerra 
        if sep == 'Construir!':
            op = False

        # aqui vai contecer tudo, ja que o numero e a ultima entrada para cada conponete
        elif sep.isnumeric():
            quantidade_componente.append(int(sep))
            nome_componente.append( " ".join(ponte))
            ponte = []

            ix = len(nome_componente) # ultimo nome add na lista
            h = nome_componente[ix]
            N = quantidade_componente[ix]
            if nome_projeto == 'Memória ROM Simples':
                # Tochas de Redstone

            elif nome_projeto == 'Calculadora de 4 bits':
                # Tochas de Redstone
                # Lâmpadas de Redstone

            elif nome_projeto == 'Sequenciador Musical':
                # Blocos de Notas
                # Observadores

            elif nome_projeto == 'Processador de 8 Bits':
                # Lâmpadas de Redstone
                # Pistões Aderentes


            elif nome_projeto == 'Display de Vídeo 8x8':
                # Comparadores
                # Pistões

            elif nome_projeto == 'Supercomputador V13':
                 # Comparadores
                 # Pistões Aderentes


            # Redstone
            # Repetidores

            # Tochas de Redstone
            # Lâmpadas de Redstone
            # Blocos de Notas
            # Observadores
            # Pistões Aderentes
            # Comparadores
            # Pistões


            if h == 'Redstone':
                print(f'Mais redstone! A energia que move o progresso! (+{N} Redstone)')

            elif h == 'Repetidores':
                print(f'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{N} Repetidores)')

            elif h == 'Tochas de Redstone':
                print(f'Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{N} Tochas de Redstone)')

            elif h == 'Lâmpadas de Redstone':
                print(f'Lâmpadas para o display! O resultado vai ficar bem visível. (+{N} Lâmpadas de Redstone)')

            elif h == 'Blocos de Notas':
                print(f'Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{N} Blocos de Notas)')

            elif h == 'Observadores':
                print(f'Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{N} Observadores)')

            elif h == 'Comparadores':
                print(f'Comparadores para a lógica! A precisão é a alma do negócio. (+{N} Comparadores)')

            elif h == 'Pistões':
                print(f'Pistões para mover as coisas de lugar. Isso vai ser útil! (+{N} Pistões)')

            elif h == 'Pistões Aderentes':
                print(f'Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{N} Pistões Aderentes)')


            # -----

        # guarda temporariamente ate juntar o nome completo
        else:
            ponte.append(sep)

print(nome_componente)
print(quantidade_componente)