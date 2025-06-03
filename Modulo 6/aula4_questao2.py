# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Define as vogais
vogais_ref = "aeiouAEIOU"

# Lista de vogais (ordenada alfabeticamente)
vogais = sorted([letra for letra in frase if letra in vogais_ref])

# Lista de consoantes (removendo espaços)
consoantes = [letra for letra in frase if letra.isalpha() and letra not in vogais_ref]

# Imprime os resultados
print(f"\nVogais: {vogais}")
print(f"Consoantes: {consoantes}")
