def encontrar_anagramas(frase, palavra_objetivo):
    import re

    palavra_objetivo = palavra_objetivo.lower()
    alvo_ordenado = sorted(palavra_objetivo)

    # Remove pontuação e divide a frase
    palavras = re.findall(r'\b\w+\b', frase.lower())

    anagramas = [
        palavra for palavra in palavras
        if sorted(palavra) == alvo_ordenado
    ]

    return anagramas

# Exemplo:
frase = "Meu amor mora em Roma e me deu um ramo de flores"
palavra_objetivo = "amor"

print(encontrar_anagramas(frase, palavra_objetivo))
