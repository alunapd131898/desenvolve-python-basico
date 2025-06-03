import random

def carrega_palavra():
    with open('gabarito_forca.txt', 'r', encoding='utf-8') as arquivo:
        palavras = arquivo.read().splitlines()
    return random.choice(palavras).lower()

def carrega_enforcado():
    with open('gabarito_enforcado.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    estagios = conteudo.strip().split("=========\n")
    estagios = [s + "=========" for s in estagios if s]
    return estagios

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogo_da_forca():
    palavra = carrega_palavra()
    estagios = carrega_enforcado()
    letras_descobertas = ["_" for _ in palavra]
    letras_erradas = []
    tentativas = 0
    max_erros = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")

    while tentativas < max_erros and "_" in letras_descobertas:
        print("\nPalavra:", " ".join(letras_descobertas))
        print("Letras erradas:", ", ".join(letras_erradas))
        letra = input("Digite uma letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Digite apenas uma letra.")
            continue

        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
        else:
            tentativas += 1
            letras_erradas.append(letra)
            imprime_enforcado(tentativas, estagios)

    if "_" not in letras_descobertas:
        print("\nParabéns! Você adivinhou a palavra:", palavra)
    else:
        print("\nVocê foi enforcado! A palavra era:", palavra)

# Executa o jogo
if __name__ == "__main__":
    jogo_da_forca()
