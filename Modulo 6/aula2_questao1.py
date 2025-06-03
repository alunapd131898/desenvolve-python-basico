import random

# 1. Gerar 20 valores inteiros aleatórios entre -100 e 100
lista_original = [random.randint(-100, 100) for _ in range(20)]

# 2. Lista ordenada (sem modificar a original)
lista_ordenada = sorted(lista_original)

# 3. Índices do maior e menor valor
indice_maior = lista_original.index(max(lista_original))
indice_menor = lista_original.index(min(lista_original))

# 4. Imprimir os resultados
print("Lista ordenada (sem modificar a original):")
print(lista_ordenada)

print("\nLista original:")
print(lista_original)

print(f"\nÍndice do maior valor ({max(lista_original)}): {indice_maior}")
print(f"Índice do menor valor ({min(lista_original)}): {indice_menor}")
