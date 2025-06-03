import string

def eh_palindromo(frase):
    # Remove espaços, pontuação e converte para minúsculas
    frase_limpa = ''.join(
        c.lower() for c in frase if c.isalnum()
    )
    return frase_limpa == frase_limpa[::-1]

while True:
    entrada = input('Digite uma frase (digite "fim" para encerrar): ')
    
    if entrada.strip().lower() == 'fim':
        break

    if eh_palindromo(entrada):
        print(f'"{entrada}" é palíndromo\n')
    else:
        print(f'"{entrada}" não é palíndromo\n')
