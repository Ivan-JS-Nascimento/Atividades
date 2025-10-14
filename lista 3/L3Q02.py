num_convidados = int(input())
convidados = []
comidas = []
valor = []

for i in range(num_convidados):
    
    nome_convidado = input()

    if nome_convidado != 'Maicon Kuster' :

        comida_convidado = input()

        if comida_convidado not in comidas:

            valor_comida = int(input())

            convidados.append(nome_convidado)
            comidas.append(comida_convidado)
            valor.append(valor_comida)
        else:
            print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {nome_convidado}")
    else:
        print("você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")