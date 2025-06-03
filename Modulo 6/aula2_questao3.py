import random
from collections import Counter

# Gerar duas listas com 20 números aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Calcular interseção sem duplicatas
interseccao = sorted(list(set(lista1) & set(lista2)))

# Contagem de elementos nas listas
contagem1 = Counter(lista1)
contagem2 = Counter(lista2)

# Exibir resultados
print("lista1 -", lista1)
print("lista2 -", lista2)
print("\nInterseccao -", interseccao)
print("\nContagem")
for elemento in interseccao:
    print(f"{elemento}: (lista1={contagem1[elemento]}, lista2={contagem2[elemento]})")
