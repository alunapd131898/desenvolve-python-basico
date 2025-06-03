import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    nomes_criptografados = []

    for nome in nomes:
        nome_cript = ''
        for char in nome:
            novo_char = ord(char) + chave
            if novo_char > 126:
                novo_char = 33 + (novo_char - 127)  # loop circular no intervalo visível
            nome_cript += chr(novo_char)
        nomes_criptografados.append(nome_cript)

    return nomes_criptografados, chave
