# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Define as vogais que devem ser substituídas
vogais = "aeiouAEIOU"

# Substitui cada vogal por '*'
frase_modificada = ""
for caractere in frase:
    if caractere in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += caractere

# Exibe a frase modificada
print("Frase modificada:", frase_modificada)
