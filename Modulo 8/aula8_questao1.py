def caracteres_unicos_ordenados(s):
    s = s.lower()  # Converte tudo para minúsculas
    unicos = set(s)  # Remove duplicatas
    unicos_ordenados = sorted(unicos)  # Ordena alfabeticamente
    return ''.join(unicos_ordenados)  # Junta em uma string

# Exemplo de uso:
entrada = "ExEmplo De String!"
resultado = caracteres_unicos_ordenados(entrada)
print(resultado)
