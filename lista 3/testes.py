lista = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista}")




n = len(lista)
# Loop externo para controlar o número de passagens
for i in range(n):
    # Loop interno para comparar elementos adjacentes
    for j in range(0, n - i - 1):
        # Compara se o elemento atual é maior que o próximo
        if lista[j] > lista[j + 1]:
            # Troca os elementos de posição
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(f"Lista ordenada: {lista_ordenada}")
# Exemplo de uso:

