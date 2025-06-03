# Todos os números pares entre 20 e 50
pares_20_50 = [x for x in range(20, 51) if x % 2 == 0]

# Os quadrados dos valores da lista [1,2,3,4,5,6,7,8,9]
quadrados = [x**2 for x in [1,2,3,4,5,6,7,8,9]]

# Todos os números entre 1 e 100 que são divisíveis por 7
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]

# Para todos os valores em range(0,30,3), escreva "par" ou "ímpar"
paridade = ['par' if x % 2 == 0 else 'ímpar' for x in range(0, 30, 3)]

# Exibindo os resultados
print("Pares entre 20 e 50:", pares_20_50)
print("Quadrados de 1 a 9:", quadrados)
print("Divisíveis por 7 de 1 a 100:", divisiveis_por_7)
print("Paridade em range(0,30,3):", paridade)
