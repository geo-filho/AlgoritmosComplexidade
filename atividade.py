# Exemplo 1 - Buscar Linear
# O algoritmo percorre a lista do início ao fim procurando por um elemento.
def busca_linear(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # encontrou o elemento
    return -1  # não encontrado


# Exemplo de uso:
lista1 = [10, 20, 30, 40, 50]
print("Lista:", lista1)
print("Buscando 30:", busca_linear(lista1, 30))  # deve retornar 2
print("Buscando 60:", busca_linear(lista1, 60))  # deve retornar -1
print("-" * 40)

# Exemplo 2 - Ordenação por Seleção (Selection Sort)
# O algoritmo percorre a lista várias vezes, para cada posição, encontra o menor elemento no restante da lista.
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

# Exemplo de uso:
lista2 = [64, 25, 12, 22, 11]
print("Lista original:", lista2)
print("Lista ordenada:", selection_sort(lista2))
print("-" * 40)

# Exemplo 3 - Fatorial Recursivo
# A função chama a si mesma até atingir a condição específica.
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
# Exemplo de uso:
for i in range(6):
    print(f"Fatorial de {i} = {fatorial(i)}")
