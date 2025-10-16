num_convidados = int(input())
convidados = []
comidas = []
valor = []
# recebe as entradas de acordo com num_convidados
for i in range(num_convidados):
    nome_convidado = input()
    comida_convidado = input()
    valor_comida = int(input())

    if nome_convidado != 'Maicon Kuster':
        if comida_convidado not in comidas:
            convidados.append(nome_convidado)
            comidas.append(comida_convidado)
            valor.append(valor_comida)

        else:
            print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {nome_convidado}")
    else:
        print("você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
# ---
# se nao tiver convidados
if len(convidados) == 0 :
    print("Nenhum convidado marcou presença na festa do calabreso!")
# caso tenha convidados
else:
    # print convidado com valor maior
    # (*)essas linhas servem para validar quem realmente é a pessoa com o valor maximo com base na ordem lexicográfica
    valor_maximo = max(valor)
    quantos_maximos = valor.count(valor_maximo)
    ix = valor.index(valor_maximo)

    if quantos_maximos > 1 :
        a = ix
        b = ix + 1
        for nao in valor[ix+1:]:
            if nao == valor_maximo:
                if convidados[a] < convidados[b]:
                    a = b
            b += 1
        
        print(f'Obrigado para o(a) {convidados[a]} pelo(a) excelente {comidas[a]}')
    else:
        print(f"Obrigado para o(a) {convidados[ix]} pelo(a) excelente {comidas[ix]}")
    # ---
    # printar convidado com valor menor
    if len(convidados) > 1:
        # mesma logica (*) so que para o menor valor
        valor_minimo = min(valor)
        quantos_maximos = valor.count(valor_minimo)
        ix = valor.index(valor_minimo)
        
        if quantos_maximos > 1 :
            a = ix
            b = ix + 1
            for nao in valor[ix+1:]:
                if nao == valor_minimo:
                    if convidados[a] > convidados[b]:
                        a = b
                b += 1
            print(f"Rapaz, {convidados[ix]} trouxe o(a) {comidas[ix]} que estava altamente mais ou menos!!!")
        else:
            print(f"Rapaz, {convidados[ix]} trouxe o(a) {comidas[ix]} que estava altamente mais ou menos!!!")
        # ---
    # listas de convidados
    print('Lista de convidados do Calabreso')

    x = 1
    while len(valor) > 0 :
        # (*)
        min_v = min(valor)
        cont = valor.count(min_v)
        index = valor.index(min_v)

        if cont > 1:
            a = index
            b = index + 1
            for val in valor[index+1:]:
                if val == min_v:
                    if convidados[a] > convidados[b]:
                        a = b
                b += 1
            print(f'{x}- {convidados[a]}')
            valor.pop(a)
            convidados.pop(a)

        else:
            print(f'{x}- {convidados[index]}')
            valor.pop(index)
            convidados.pop(index)

        x += 1
    # ---