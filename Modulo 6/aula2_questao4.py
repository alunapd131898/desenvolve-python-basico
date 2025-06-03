# Função para ler uma lista de números do usuário
def ler_lista(numero_lista):
    qtd = int(input(f"Digite a quantidade de elementos da lista {numero_lista}: "))
    lista = []
    print(f"Digite os {qtd} elementos da lista {numero_lista}:")
    for _ in range(qtd):
        elemento = int(input())
        lista.append(elemento)
    return lista

# Função para intercalar duas listas
def intercalar_listas(lista1, lista2):
    intercalada = []
    len1, len2 = len(lista1), len(lista2)
    min_len = min(len1, len2)

    # Intercala os elementos até o final da menor lista
    for i in range(min_len):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])

    # Adiciona os elementos restantes da maior lista
    if len1 > len2:
        intercalada.extend(lista1[min_len:])
    else:
        intercalada.extend(lista2[min_len:])

    return intercalada

# Programa principal
lista1 = ler_lista(1)
lista2 = ler_lista(2)

lista_intercalada = intercalar_listas(lista1, lista2)

print("Lista intercalada:", *lista_intercalada)
