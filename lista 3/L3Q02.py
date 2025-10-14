num_convidados = int(input())
convidados = []
comidas = []
valor = []

for i in range(num_convidados):
    nome_convidado = input()

    if nome_convidado != 'Maicon Kuster':
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

if len(convidados) == 0 :
    print("Nenhum convidado marcou presença na festa do calabreso!")
else:
    print(f"Obrigado para o(a) {convidados[valor.index(max(valor))]} pelo(a) excelente {comidas[valor.index(max(valor))]}")
    if len(convidados) > 1:
        print(f"Rapaz, {convidados[valor.index(min(valor))]} trouxe o(a) {comidas[valor.index(min(valor))]} que estava altamente mais ou menos!!!")

    for i in len(valor):
        
