import re

# Abrir o arquivo para leitura
with open("estomago.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

# 1. Imprimir as primeiras 25 linhas
print(">>> Primeiras 25 linhas do roteiro:\n")
for linha in linhas[:25]:
    print(linha.rstrip())

# 2. Número total de linhas
num_linhas = len(linhas)
print(f"\n>>> Número total de linhas: {num_linhas}")

# 3. Linha com maior número de caracteres
linha_maior = max(linhas, key=len)
print("\n>>> Linha com maior número de caracteres:")
print(linha_maior.strip())

# 4. Número de menções aos personagens "Nonato" e "Íria" (case-insensitive e cuidado com substrings)
texto_completo = ''.join(linhas)

# Usar regex para garantir que estamos pegando palavras completas
nonato_count = len(re.findall(r'\bnonato\b', texto_completo, flags=re.IGNORECASE))
iria_count = len(re.findall(r'\bíria\b', texto_completo, flags=re.IGNORECASE))

print(f"\n>>> Número de menções a 'Nonato': {nonato_count}")
print(f">>> Número de menções a 'Íria': {iria_count}")
