import random

# Gerar lista com 20 números aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# Encontrar o intervalo contínuo com a maior quantidade de números negativos
max_negativos = 0
inicio_max = 0
fim_max = 0

# Percorrer todos os possíveis intervalos
for i in range(len(lista)):
    for j in range(i+1, len(lista)+1):
        sublista = lista[i:j]
        negativos = sum(1 for x in sublista if x < 0)
        if negativos > max_negativos:
            max_negativos = negativos
            inicio_max = i
            fim_max = j

# Remover o intervalo da lista
del lista[inicio_max:fim_max]

# Imprimir lista após remoção
print("Editada: ", lista)
