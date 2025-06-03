import re

# Lê o conteúdo do arquivo 'frase.txt'
with open("frase.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Usa expressão regular para manter apenas letras e espaços entre palavras
# \w inclui letras e números, então usamos uma alternativa mais precisa com unicode para acentos
palavras = re.findall(r'\b[\wÀ-ÿ]+\b', conteudo)

# Salva cada palavra em uma linha no novo arquivo
with open("palavras.txt", "w", encoding="utf-8") as arquivo_palavras:
    for palavra in palavras:
        arquivo_palavras.write(palavra + "\n")

# Lê e imprime o conteúdo do novo arquivo
with open("palavras.txt", "r", encoding="utf-8") as resultado:
    print(resultado.read())
