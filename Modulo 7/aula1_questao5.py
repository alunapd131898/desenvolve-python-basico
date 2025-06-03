# Lê uma string do usuário
frase = input("Digite uma frase: ")

# Lista de vogais
vogais = "aeiouAEIOU"

# Inicializa a contagem e os índices
indices_vogais = []

# Percorre a frase e verifica se o caractere é uma vogal
for i, letra in enumerate(frase):
    if letra in vogais:
        indices_vogais.append(i)

# Imprime o resultado
print(f"\n{len(indices_vogais)} vogais")
print(f"\nÍndices {indices_vogais}")
